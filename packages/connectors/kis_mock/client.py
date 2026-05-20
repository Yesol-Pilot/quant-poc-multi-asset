"""Async KIS mock client — token lifecycle + retry/backoff + canonical mapping.

Design for the W2 D8 unblock:
- Until the owner completes KIS Developers signup, `config.has_credentials` is
  False and the client runs in OFFLINE mode: every network method raises
  `OfflineMode` instead of touching the network. This lets the rest of the
  stack import and unit-test the client today.
- The moment the owner injects KIS_APP_KEY / KIS_APP_SECRET into .env, the
  client is live against the MOCK endpoint — no code change required.

httpx is the transport. Tests inject a `httpx.MockTransport` via the
`transport` kwarg, so no real network call happens in CI.
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone

import httpx

from core.types import MarketBar  # canonical type (Option C)
from connectors.kis_mock.config import KisConfig
from connectors.kis_mock.models import (
    OrderRequest,
    OrderResponse,
    QuoteResponse,
    TokenResponse,
)


class OfflineMode(RuntimeError):
    """Raised when a network method is called without credentials."""


class KisApiError(RuntimeError):
    """Raised when KIS returns a non-success rt_cd or an HTTP error persists."""


class KisMockClient:
    def __init__(
        self,
        config: KisConfig,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.config = config
        self._token: TokenResponse | None = None
        self._lock = asyncio.Lock()
        # `transport` lets tests inject httpx.MockTransport. None => real network.
        self._client = httpx.AsyncClient(
            base_url=config.base_url,
            timeout=config.timeout_s,
            transport=transport,
        )

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "KisMockClient":
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    # ── token lifecycle ────────────────────────────────────────────────
    async def _ensure_token(self) -> TokenResponse:
        if not self.config.has_credentials:
            raise OfflineMode(
                "KIS credentials absent — running in offline scaffold mode. "
                "Inject KIS_APP_KEY + KIS_APP_SECRET to go live (mock endpoint)."
            )
        async with self._lock:
            if self._token is not None and not self._token.is_expired():
                return self._token
            resp = await self._request_with_retry(
                "POST",
                "/oauth2/tokenP",
                json={
                    "grant_type": "client_credentials",
                    "appkey": self.config.app_key,
                    "appsecret": self.config.app_secret,
                },
                authed=False,
            )
            token = TokenResponse.model_validate(resp.json())
            self._token = token
            return token

    async def _auth_headers(self, tr_id: str) -> dict[str, str]:
        token = await self._ensure_token()
        return {
            "authorization": f"Bearer {token.access_token}",
            "appkey": self.config.app_key,
            "appsecret": self.config.app_secret,
            "tr_id": tr_id,
            "content-type": "application/json; charset=utf-8",
        }

    # ── retry/backoff ──────────────────────────────────────────────────
    async def _request_with_retry(
        self,
        method: str,
        path: str,
        *,
        params: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        authed: bool = True,  # noqa: ARG002 - reserved; auth handled by caller
    ) -> httpx.Response:
        last_exc: Exception | None = None
        for attempt in range(self.config.max_retries):
            try:
                resp = await self._client.request(
                    method, path, params=params, json=json, headers=headers
                )
                # Retry on 5xx + 429 (rate limit); 4xx (except 429) is terminal.
                if resp.status_code >= 500 or resp.status_code == 429:
                    raise httpx.HTTPStatusError(
                        f"retryable {resp.status_code}", request=resp.request, response=resp
                    )
                resp.raise_for_status()
                return resp
            except (httpx.HTTPStatusError, httpx.TransportError) as exc:
                last_exc = exc
                if attempt < self.config.max_retries - 1:
                    # exponential backoff: 0.5, 1.0, 2.0, ...
                    await asyncio.sleep(0.5 * (2**attempt))
        raise KisApiError(f"request failed after {self.config.max_retries} retries: {last_exc}")

    # ── public API ─────────────────────────────────────────────────────
    async def get_quote(self, symbol: str) -> QuoteResponse:
        """Current price snapshot. tr_id FHKST01010100 = 주식현재가 시세."""
        headers = await self._auth_headers("FHKST01010100")
        resp = await self._request_with_retry(
            "GET",
            "/uapi/domestic-stock/v1/quotations/inquire-price",
            params={"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": symbol},
            headers=headers,
        )
        out = QuoteResponse.model_validate(resp.json())
        if not out.ok:
            raise KisApiError(f"quote {symbol} failed: {out.msg_cd} {out.msg1}")
        return out

    async def quote_to_bar(self, symbol: str, timeframe: str = "1d") -> MarketBar:
        """Convenience: fetch a quote and map it into the canonical MarketBar."""
        q = await self.get_quote(symbol)
        o = q.output
        # KIS snapshot doesn't carry a bar timestamp; stamp now (UTC).
        return MarketBar(
            symbol=symbol,
            timeframe=timeframe,
            ts=datetime.now(timezone.utc),
            open=o.open or o.price,
            high=o.high or o.price,
            low=o.low or o.price,
            close=o.price,
            volume=o.volume,
        )

    async def place_order(
        self, symbol: str, qty: int, *, side: str = "buy", price: int | None = None
    ) -> OrderResponse:
        """Cash order (PAPER/mock only). tr_id VTTC0802U = buy, VTTC0801U = sell
        on the mock (vts) domain. price=None => market order."""
        if not self.config.account_no:
            raise KisApiError("KIS_ACCOUNT_NO not configured")
        cano = self.config.account_no.split("-")[0]
        tr_id = "VTTC0802U" if side == "buy" else "VTTC0801U"
        body = OrderRequest(
            CANO=cano,
            ACNT_PRDT_CD=self.config.account_prod,
            PDNO=symbol,
            ORD_DVSN="00" if price is not None else "01",
            ORD_QTY=str(qty),
            ORD_UNPR=str(price or 0),
        )
        headers = await self._auth_headers(tr_id)
        resp = await self._request_with_retry(
            "POST",
            "/uapi/domestic-stock/v1/trading/order-cash",
            json=body.model_dump(),
            headers=headers,
        )
        out = OrderResponse.model_validate(resp.json())
        if not out.ok:
            raise KisApiError(f"order {symbol} failed: {out.msg_cd} {out.msg1}")
        return out


__all__ = ["KisMockClient", "OfflineMode", "KisApiError"]
