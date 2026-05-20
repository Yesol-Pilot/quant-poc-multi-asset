"""Tests for the KIS mock connector — no real network (httpx.MockTransport).

Covers the safety-critical guards (live-endpoint refusal, offline mode) and the
happy-path quote/order flows against simulated KIS responses.
"""

import sys
from pathlib import Path

import httpx
import pytest

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "packages"))

from core.types import MarketBar  # noqa: E402
from connectors.kis_mock import (  # noqa: E402
    KisApiError,
    KisConfig,
    KisMockClient,
    LiveEndpointError,
    MOCK_BASE_URL,
    OfflineMode,
    load_from_env,
)


# ── config guards ──────────────────────────────────────────────────────
def test_config_rejects_live_endpoint() -> None:
    with pytest.raises(LiveEndpointError):
        KisConfig(
            app_key="k", app_secret="s",
            base_url="https://openapi.koreainvestment.com:9443",  # LIVE
        )


def test_config_accepts_mock_endpoint() -> None:
    cfg = KisConfig(app_key="k", app_secret="s", base_url=MOCK_BASE_URL)
    assert cfg.is_mock is True
    assert cfg.has_credentials is True


def test_load_from_env_offline_when_no_keys() -> None:
    cfg = load_from_env({})  # empty env
    assert cfg.has_credentials is False
    assert cfg.is_mock is True  # defaults to mock URL


def test_load_from_env_reads_keys() -> None:
    cfg = load_from_env({"KIS_APP_KEY": "abc", "KIS_APP_SECRET": "xyz"})
    assert cfg.has_credentials is True


# ── offline mode ─────────────────────────────────────────────────────────
@pytest.mark.asyncio
async def test_offline_mode_raises_without_credentials() -> None:
    cfg = load_from_env({})  # no credentials
    async with KisMockClient(cfg) as kis:
        with pytest.raises(OfflineMode):
            await kis.get_quote("005930")


# ── happy-path quote (mock transport) ────────────────────────────────────
def _mock_transport() -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/oauth2/tokenP":
            return httpx.Response(
                200, json={"access_token": "tok-123", "token_type": "Bearer", "expires_in": 86400}
            )
        if "inquire-price" in request.url.path:
            return httpx.Response(
                200,
                json={
                    "rt_cd": "0", "msg_cd": "MCA00000", "msg1": "정상",
                    "output": {
                        "stck_prpr": "70500", "stck_oprc": "70000",
                        "stck_hgpr": "71000", "stck_lwpr": "69500",
                        "acml_vol": "12345678", "prdy_ctrt": "0.71",
                    },
                },
            )
        if "order-cash" in request.url.path:
            return httpx.Response(
                200,
                json={"rt_cd": "0", "msg_cd": "APBK", "msg1": "주문 전송 완료",
                      "output": {"ODNO": "0001234567"}},
            )
        return httpx.Response(404, json={"rt_cd": "1", "msg1": "not found"})

    return httpx.MockTransport(handler)


@pytest.mark.asyncio
async def test_get_quote_happy_path() -> None:
    cfg = KisConfig(app_key="k", app_secret="s", account_no="12345678-01")
    async with KisMockClient(cfg, transport=_mock_transport()) as kis:
        q = await kis.get_quote("005930")
        assert q.ok
        assert q.output.price == 70500.0
        assert q.output.high == 71000.0


@pytest.mark.asyncio
async def test_quote_to_bar_maps_to_canonical() -> None:
    cfg = KisConfig(app_key="k", app_secret="s")
    async with KisMockClient(cfg, transport=_mock_transport()) as kis:
        bar = await kis.quote_to_bar("005930")
        assert isinstance(bar, MarketBar)
        assert bar.close == 70500.0
        assert bar.high == 71000.0
        assert bar.low == 69500.0
        assert bar.ts.tzinfo is not None


@pytest.mark.asyncio
async def test_place_order_happy_path() -> None:
    cfg = KisConfig(app_key="k", app_secret="s", account_no="12345678-01")
    async with KisMockClient(cfg, transport=_mock_transport()) as kis:
        res = await kis.place_order("005930", qty=10, side="buy")
        assert res.ok
        assert res.order_no == "0001234567"


@pytest.mark.asyncio
async def test_token_cached_across_calls() -> None:
    calls = {"token": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/oauth2/tokenP":
            calls["token"] += 1
            return httpx.Response(200, json={"access_token": "t", "expires_in": 86400})
        return httpx.Response(
            200, json={"rt_cd": "0", "output": {"stck_prpr": "100"}}
        )

    cfg = KisConfig(app_key="k", app_secret="s")
    async with KisMockClient(cfg, transport=httpx.MockTransport(handler)) as kis:
        await kis.get_quote("A")
        await kis.get_quote("B")
        assert calls["token"] == 1  # token fetched once, reused


@pytest.mark.asyncio
async def test_retry_on_500_then_success() -> None:
    state = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/oauth2/tokenP":
            return httpx.Response(200, json={"access_token": "t", "expires_in": 86400})
        state["n"] += 1
        if state["n"] == 1:
            return httpx.Response(503, json={"msg1": "temporary"})
        return httpx.Response(200, json={"rt_cd": "0", "output": {"stck_prpr": "100"}})

    cfg = KisConfig(app_key="k", app_secret="s", max_retries=3)
    async with KisMockClient(cfg, transport=httpx.MockTransport(handler)) as kis:
        q = await kis.get_quote("A")
        assert q.ok
        assert state["n"] == 2  # one 503, one success
