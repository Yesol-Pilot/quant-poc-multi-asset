"""Pydantic models for the KIS OpenAPI request/response payloads we use.

Only the fields the project actually reads are modeled; KIS responses carry
many more. `extra="ignore"` keeps us forward-compatible when KIS adds fields.

Endpoint reference (mock domain openapivts.koreainvestment.com:29443):
- POST /oauth2/tokenP                                  -> TokenResponse
- GET  /uapi/domestic-stock/v1/quotations/inquire-price -> QuoteResponse
- POST /uapi/domestic-stock/v1/trading/order-cash       -> OrderResponse
"""

from __future__ import annotations

from datetime import datetime, timezone

from pydantic import BaseModel, ConfigDict, Field


class TokenResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    access_token: str
    token_type: str = "Bearer"
    expires_in: int = 86400  # seconds; KIS tokens last ~24h
    access_token_token_expired: str = ""  # KIS returns a string timestamp too

    issued_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def is_expired(self, *, skew_s: int = 60) -> bool:
        """True if the token is past (expiry - skew). The skew margin forces a
        refresh slightly early so an in-flight request never uses a token that
        expires mid-call."""
        age = (datetime.now(timezone.utc) - self.issued_at).total_seconds()
        return age >= (self.expires_in - skew_s)


class QuoteOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    # KIS field names (Korean API uses abbreviated codes); mapped to readable names.
    stck_prpr: str = "0"        # 현재가 (current price)
    stck_oprc: str = "0"        # 시가 (open)
    stck_hgpr: str = "0"        # 고가 (high)
    stck_lwpr: str = "0"        # 저가 (low)
    acml_vol: str = "0"         # 누적 거래량 (volume)
    prdy_ctrt: str = "0"        # 전일 대비율 (pct change)

    @property
    def price(self) -> float:
        return float(self.stck_prpr or 0)

    @property
    def open(self) -> float:
        return float(self.stck_oprc or 0)

    @property
    def high(self) -> float:
        return float(self.stck_hgpr or 0)

    @property
    def low(self) -> float:
        return float(self.stck_lwpr or 0)

    @property
    def volume(self) -> float:
        return float(self.acml_vol or 0)


class QuoteResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rt_cd: str = "0"            # 0 = success
    msg_cd: str = ""
    msg1: str = ""
    output: QuoteOutput = Field(default_factory=QuoteOutput)

    @property
    def ok(self) -> bool:
        return self.rt_cd == "0"


class OrderRequest(BaseModel):
    """Cash order. `ORD_DVSN` 00=지정가(limit), 01=시장가(market)."""

    model_config = ConfigDict(extra="ignore")

    CANO: str                  # account number (8 digits)
    ACNT_PRDT_CD: str = "01"   # product code
    PDNO: str                  # symbol (e.g. "005930")
    ORD_DVSN: str = "01"       # 01 = market
    ORD_QTY: str               # quantity (string per KIS spec)
    ORD_UNPR: str = "0"        # price (0 for market)


class OrderResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    rt_cd: str = "0"
    msg_cd: str = ""
    msg1: str = ""
    output: dict = Field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return self.rt_cd == "0"

    @property
    def order_no(self) -> str:
        return str(self.output.get("ODNO", "")) if self.output else ""


__all__ = [
    "TokenResponse",
    "QuoteOutput",
    "QuoteResponse",
    "OrderRequest",
    "OrderResponse",
]
