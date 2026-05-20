"""Smoke test for packages/core/backtest/base.py — the forward-walking loop."""

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "packages"))

from core.types import AlphaSignal, MarketBar, Side  # noqa: E402
from core.backtest.base import BaseBacktester  # noqa: E402


class BuyAndHold(BaseBacktester):
    """Goes long on the first bar, never sells. The simplest possible alpha."""

    def on_bar(self, bar: MarketBar, history: list[MarketBar]) -> AlphaSignal | None:
        if len(history) == 1:
            return AlphaSignal(alpha_id="buy_hold", symbol=bar.symbol, side=Side.LONG, strength=1.0)
        return None


class SmaCross(BaseBacktester):
    """Long when close > 5-bar SMA, flat otherwise. Exercises open/close churn."""

    def on_bar(self, bar: MarketBar, history: list[MarketBar]) -> AlphaSignal | None:
        if len(history) < 5:
            return None
        sma = sum(b.close for b in history[-5:]) / 5
        if bar.close > sma:
            return AlphaSignal(alpha_id="sma", symbol=bar.symbol, side=Side.LONG, strength=1.0)
        return AlphaSignal(alpha_id="sma", symbol=bar.symbol, side=Side.FLAT, strength=0.0)


def _make_bars(closes: list[float]) -> list[MarketBar]:
    t0 = datetime(2026, 1, 1, tzinfo=timezone.utc)
    bars = []
    for i, c in enumerate(closes):
        bars.append(
            MarketBar(
                symbol="TEST", timeframe="1d", ts=t0 + timedelta(days=i),
                open=c, high=c * 1.01, low=c * 0.99, close=c, volume=1000,
            )
        )
    return bars


def test_buy_and_hold_tracks_price() -> None:
    # price doubles 100 -> 200; buy-and-hold equity should ~double (minus 1 entry cost)
    closes = list(range(100, 201, 5))  # 100,105,...,200
    bars = _make_bars([float(c) for c in closes])
    bt = BuyAndHold(starting_equity=10_000, cost_bps=5)
    res = bt.run(bars)
    assert res.n_bars == len(bars)
    assert res.n_trades == 1  # one entry, never exits
    assert res.total_return > 0.9  # roughly doubled
    # only drawdown is the one-time entry cost (5bps) before price climbs
    assert res.max_drawdown >= -0.001
    assert res.max_drawdown <= 0.0


def test_sma_cross_runs_and_trades() -> None:
    # oscillating series forces multiple entries/exits
    closes = [100, 102, 98, 104, 96, 108, 94, 110, 92, 112, 90, 115]
    bars = _make_bars([float(c) for c in closes])
    bt = SmaCross(starting_equity=10_000, cost_bps=10)
    res = bt.run(bars)
    assert res.n_bars == len(bars)
    assert res.n_trades >= 1
    assert len(res.equity_curve) == len(bars) + 1  # +1 for starting equity
    assert isinstance(res.summary(), str)
    assert "sharpe=" in res.summary()


def test_dsr_computed_when_trials_given() -> None:
    closes = [float(c) for c in range(100, 160)]
    bars = _make_bars(closes)
    bt = BuyAndHold()
    res = bt.run(bars, n_trials=50, sr_variance=1.0)
    assert res.deflated_sharpe is not None
    assert 0.0 <= res.deflated_sharpe <= 1.0


def test_no_dsr_without_trials() -> None:
    bars = _make_bars([100.0, 101.0, 102.0])
    res = BuyAndHold().run(bars)
    assert res.deflated_sharpe is None
