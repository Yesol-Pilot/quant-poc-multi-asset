"""Abstract backtester — forward-walking event loop shared by every alpha.

A concrete backtester subclasses `BaseBacktester` and implements `on_bar`,
emitting `AlphaSignal`s. The base loop handles position bookkeeping, equity
tracking, and metric computation so each alpha only writes its signal logic.

This is deliberately simple (no slippage model beyond a flat bps cost, no
partial fills) for W2-W7. The W8 statistical-rigor phase swaps in a richer
execution model behind the same interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np

from core.types import AlphaSignal, MarketBar, Side
from core.backtest.metrics import (
    deflated_sharpe_ratio,
    max_drawdown,
    profit_factor,
    sharpe_ratio,
)


@dataclass
class BacktestResult:
    n_bars: int
    n_trades: int
    final_equity: float
    total_return: float
    sharpe: float
    max_drawdown: float
    profit_factor: float
    deflated_sharpe: float | None  # None unless n_trials provided
    equity_curve: list[float] = field(default_factory=list)
    period_returns: list[float] = field(default_factory=list)

    def summary(self) -> str:
        dsr = f"{self.deflated_sharpe:.3f}" if self.deflated_sharpe is not None else "n/a"
        return (
            f"bars={self.n_bars} trades={self.n_trades} "
            f"ret={self.total_return:+.2%} sharpe={self.sharpe:.2f} "
            f"maxDD={self.max_drawdown:.2%} pf={self.profit_factor:.2f} dsr={dsr}"
        )


class BaseBacktester(ABC):
    """Forward-walking, single-symbol, single-position backtester.

    Position model: at most one open position at a time (long, short, or flat).
    A signal in the same direction is ignored; the opposite direction (or FLAT)
    closes the position; a fresh direction opens. Costs are charged as
    `cost_bps` of notional per side on entry and exit.
    """

    def __init__(
        self,
        *,
        starting_equity: float = 10_000.0,
        cost_bps: float = 5.0,
        periods_per_year: int = 252,
    ) -> None:
        self.starting_equity = starting_equity
        self.cost_bps = cost_bps
        self.periods_per_year = periods_per_year

    @abstractmethod
    def on_bar(self, bar: MarketBar, history: list[MarketBar]) -> AlphaSignal | None:
        """Return a signal for this bar, or None to hold the current state.

        `history` includes all bars seen so far INCLUDING the current one (last
        element). Implementations must not peek beyond `history` — that would be
        look-ahead bias.
        """
        raise NotImplementedError

    def run(
        self,
        bars: list[MarketBar],
        *,
        n_trials: int | None = None,
        sr_variance: float | None = None,
    ) -> BacktestResult:
        """Run the event loop. If `n_trials` and `sr_variance` are given, the
        Deflated Sharpe Ratio is computed (how much of the Sharpe survives the
        multiple-testing correction across `n_trials` strategy configs)."""
        equity = self.starting_equity
        equity_curve: list[float] = [equity]
        period_returns: list[float] = []

        position: Side = Side.FLAT
        entry_price = 0.0
        n_trades = 0
        cost = self.cost_bps / 10_000.0

        history: list[MarketBar] = []
        prev_close: float | None = None

        for bar in bars:
            history.append(bar)

            # mark-to-market the open position on this bar's close
            if position is not Side.FLAT and prev_close is not None and prev_close > 0:
                ret = (bar.close - prev_close) / prev_close
                signed = ret if position is Side.LONG else -ret
                equity *= 1 + signed
                period_returns.append(signed)
            else:
                period_returns.append(0.0)

            signal = self.on_bar(bar, history)
            if signal is not None:
                desired = signal.side
                if desired is not position:
                    # close existing
                    if position is not Side.FLAT:
                        equity *= 1 - cost
                        n_trades += 1
                    # open new (if not flat)
                    if desired is not Side.FLAT:
                        equity *= 1 - cost
                        entry_price = bar.close
                        n_trades += 1
                    position = desired

            equity_curve.append(equity)
            prev_close = bar.close

        eq = np.array(equity_curve, dtype=float)
        rets = np.array(period_returns, dtype=float)
        total_return = (equity / self.starting_equity) - 1.0
        sr = sharpe_ratio(rets, periods_per_year=self.periods_per_year)
        dsr = None
        if n_trials is not None and sr_variance is not None:
            dsr = deflated_sharpe_ratio(
                rets,
                n_trials=n_trials,
                sr_variance=sr_variance,
                periods_per_year=self.periods_per_year,
            )

        return BacktestResult(
            n_bars=len(bars),
            n_trades=n_trades,
            final_equity=float(equity),
            total_return=float(total_return),
            sharpe=sr,
            max_drawdown=max_drawdown(eq),
            profit_factor=profit_factor(rets),
            deflated_sharpe=dsr,
            equity_curve=[float(x) for x in eq],
            period_returns=[float(x) for x in rets],
        )


__all__ = ["BaseBacktester", "BacktestResult"]
