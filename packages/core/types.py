"""Canonical data structures shared across alphas, connectors, and backtests.

Every alpha emits `AlphaSignal`s. The execution layer turns approved signals
into `OrderIntent`s. The kill switch emits `KillSwitchTrigger`s. Market data
arrives as `MarketBar`s. Keeping these in one place means the KIS connector,
the IBKR connector, the backtester, and the live runner all speak the same
vocabulary — no per-module ad-hoc dicts.

Pydantic v2 for validation (the project already depends on pydantic>=2.10).
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


class Side(str, Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"


class AssetClass(str, Enum):
    KOREAN_EQUITY = "korean_equity"
    US_EQUITY = "us_equity"
    US_OPTION = "us_option"
    CRYPTO = "crypto"  # archive only


class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"


class KillSwitchLayer(str, Enum):
    """The 12 kill-switch layers. L1-L9 inherited from the 38-day crypto PoC,
    L10-L12 added for the multi-asset rebuild."""

    L1_ORDER_RATE = "L1_order_rate"
    L2_MAX_DRAWDOWN = "L2_max_drawdown"
    L3_CORRELATION = "L3_correlation"
    L4_EXCHANGE_HEALTH = "L4_exchange_health"
    L5_MMR = "L5_mmr"
    L6_ADL_QUEUE = "L6_adl_queue"
    L7_ENV_GUARD = "L7_env_guard"
    L8_STABLECOIN_DEPEG = "L8_stablecoin_depeg"
    L9_FUNDING_SPIKE = "L9_funding_spike"
    L10_ALPHA_DECAY = "L10_alpha_decay"
    L11_REGIME = "L11_regime"
    L12_OVERFIT = "L12_overfit"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class MarketBar(BaseModel):
    """A single OHLCV bar. Timeframe is a string like '1m', '5m', '1h', '1d'."""

    symbol: str
    timeframe: str
    ts: datetime  # bar open time, tz-aware UTC
    open: float = Field(gt=0)
    high: float = Field(gt=0)
    low: float = Field(gt=0)
    close: float = Field(gt=0)
    volume: float = Field(ge=0)

    @field_validator("ts")
    @classmethod
    def _tz_aware(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError("MarketBar.ts must be timezone-aware (UTC)")
        return v.astimezone(timezone.utc)

    @model_validator(mode="after")
    def _ohlc_coherent(self) -> "MarketBar":
        if self.high < self.low:
            raise ValueError(f"high {self.high} < low {self.low}")
        if not (self.low <= self.open <= self.high):
            raise ValueError("open outside [low, high]")
        if not (self.low <= self.close <= self.high):
            raise ValueError("close outside [low, high]")
        return self


class AlphaSignal(BaseModel):
    """Emitted by an alpha when it wants a position. `strength` in [0, 1] is the
    alpha's conviction; the position sizer converts it (with risk limits) into a
    concrete size. `side=FLAT` with strength 0 means 'close any open position'."""

    alpha_id: str
    symbol: str
    side: Side
    strength: float = Field(ge=0.0, le=1.0)
    ts: datetime = Field(default_factory=_utcnow)
    timeframe: str = "1d"
    reason: str = ""
    metadata: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _flat_zero_strength(self) -> "AlphaSignal":
        if self.side is Side.FLAT and self.strength != 0.0:
            raise ValueError("FLAT signal must have strength 0.0")
        return self


class OrderIntent(BaseModel):
    """What the execution layer should attempt. `kill_switch_checked` MUST be
    True before a live runner submits; the runner asserts this to guarantee no
    order bypasses the 12-layer gate. Paper/backtest runners may set it via the
    simulated kill switch."""

    symbol: str
    side: Side
    size: float = Field(gt=0)
    order_type: OrderType = OrderType.MARKET
    limit_price: float | None = None
    reduce_only: bool = False
    alpha_id: str = ""
    kill_switch_checked: bool = False
    ts: datetime = Field(default_factory=_utcnow)

    @model_validator(mode="after")
    def _limit_needs_price(self) -> "OrderIntent":
        if self.order_type is OrderType.LIMIT and self.limit_price is None:
            raise ValueError("LIMIT order requires limit_price")
        if self.side is Side.FLAT:
            raise ValueError("OrderIntent side cannot be FLAT (use reduce_only)")
        return self


class KillSwitchTrigger(BaseModel):
    """A kill-switch fire event. `halt_until` (if set) blocks new entries until
    that time. `action_taken` records what the orchestrator did (cancel_all,
    close_positions, block_entries, alert_only)."""

    layer: KillSwitchLayer
    reason: str
    ts: datetime = Field(default_factory=_utcnow)
    alpha_id: str | None = None
    symbol: str | None = None
    action_taken: str = "alert_only"
    halt_until: datetime | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


__all__ = [
    "Side",
    "AssetClass",
    "OrderType",
    "KillSwitchLayer",
    "MarketBar",
    "AlphaSignal",
    "OrderIntent",
    "KillSwitchTrigger",
]
