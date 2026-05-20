"""Unit tests for packages/core/types.py — Pydantic model validation."""

import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "packages"))

from core.types import (  # noqa: E402
    AlphaSignal,
    KillSwitchLayer,
    KillSwitchTrigger,
    MarketBar,
    OrderIntent,
    OrderType,
    Side,
)


def _ts() -> datetime:
    return datetime(2026, 5, 14, tzinfo=timezone.utc)


def test_market_bar_valid() -> None:
    bar = MarketBar(
        symbol="005930", timeframe="1d", ts=_ts(),
        open=70000, high=71000, low=69500, close=70500, volume=1_000_000,
    )
    assert bar.symbol == "005930"
    assert bar.ts.tzinfo is not None


def test_market_bar_rejects_naive_ts() -> None:
    with pytest.raises(ValueError):
        MarketBar(
            symbol="X", timeframe="1d", ts=datetime(2026, 5, 14),  # naive
            open=1, high=2, low=0.5, close=1.5, volume=0,
        )


def test_market_bar_rejects_incoherent_ohlc() -> None:
    with pytest.raises(ValueError):
        MarketBar(
            symbol="X", timeframe="1d", ts=_ts(),
            open=10, high=5, low=8, close=9, volume=0,  # high < low
        )


def test_market_bar_rejects_close_outside_range() -> None:
    with pytest.raises(ValueError):
        MarketBar(
            symbol="X", timeframe="1d", ts=_ts(),
            open=10, high=12, low=9, close=15, volume=0,  # close > high
        )


def test_alpha_signal_strength_bounds() -> None:
    AlphaSignal(alpha_id="A11", symbol="X", side=Side.LONG, strength=1.0)
    with pytest.raises(ValueError):
        AlphaSignal(alpha_id="A11", symbol="X", side=Side.LONG, strength=1.5)


def test_alpha_signal_flat_must_be_zero_strength() -> None:
    AlphaSignal(alpha_id="A11", symbol="X", side=Side.FLAT, strength=0.0)
    with pytest.raises(ValueError):
        AlphaSignal(alpha_id="A11", symbol="X", side=Side.FLAT, strength=0.5)


def test_order_intent_limit_requires_price() -> None:
    OrderIntent(symbol="X", side=Side.LONG, size=1.0,
                order_type=OrderType.LIMIT, limit_price=100.0)
    with pytest.raises(ValueError):
        OrderIntent(symbol="X", side=Side.LONG, size=1.0, order_type=OrderType.LIMIT)


def test_order_intent_rejects_flat_side() -> None:
    with pytest.raises(ValueError):
        OrderIntent(symbol="X", side=Side.FLAT, size=1.0)


def test_order_intent_kill_switch_default_false() -> None:
    o = OrderIntent(symbol="X", side=Side.LONG, size=1.0)
    assert o.kill_switch_checked is False  # must be explicitly set True before live


def test_kill_switch_trigger_layers() -> None:
    trig = KillSwitchTrigger(
        layer=KillSwitchLayer.L10_ALPHA_DECAY, reason="sharpe < 0 over 14d"
    )
    assert trig.layer is KillSwitchLayer.L10_ALPHA_DECAY
    assert trig.action_taken == "alert_only"
    # all 12 layers present
    assert len(list(KillSwitchLayer)) == 12
