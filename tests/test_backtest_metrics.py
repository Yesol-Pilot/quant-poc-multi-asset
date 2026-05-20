"""Unit tests for packages/core/backtest/metrics.py.

These pin the academically-significant statistics (DSR, PBO) to known
behaviors so a future refactor can't silently break the overfitting guards.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

REPO_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(REPO_ROOT / "packages"))

from core.backtest.metrics import (  # noqa: E402
    deflated_sharpe_ratio,
    expected_max_sharpe,
    max_drawdown,
    probabilistic_sharpe_ratio,
    probability_of_backtest_overfitting,
    profit_factor,
    sharpe_ratio,
)

RNG = np.random.default_rng(42)


def test_sharpe_zero_for_degenerate() -> None:
    assert sharpe_ratio(np.array([])) == 0.0
    assert sharpe_ratio(np.array([0.01])) == 0.0
    assert sharpe_ratio(np.array([0.01, 0.01, 0.01])) == 0.0  # zero variance


def test_sharpe_positive_for_trending_up() -> None:
    rets = np.full(252, 0.001) + RNG.normal(0, 0.0001, 252)
    assert sharpe_ratio(rets) > 0


def test_max_drawdown_known_curve() -> None:
    # peak 100 -> trough 85 = -15% drawdown (the project's narrative anchor)
    eq = np.array([100, 110, 93.5, 100, 105])  # 110 -> 93.5 = -15%
    dd = max_drawdown(eq)
    assert dd == pytest.approx(-0.15, abs=1e-9)


def test_max_drawdown_monotonic_up_is_zero() -> None:
    assert max_drawdown(np.array([100, 101, 102, 103])) == 0.0


def test_profit_factor() -> None:
    assert profit_factor(np.array([1.0, -0.5, 2.0, -0.5])) == pytest.approx(3.0)
    assert profit_factor(np.array([1.0, 2.0])) == float("inf")
    assert profit_factor(np.array([-1.0, -2.0])) == 0.0


def test_psr_in_unit_interval() -> None:
    rets = RNG.normal(0.001, 0.01, 500)
    psr = probabilistic_sharpe_ratio(rets, sr_benchmark=0.0)
    assert 0.0 <= psr <= 1.0


def test_expected_max_sharpe_increases_with_trials() -> None:
    # More trials => higher expected max Sharpe under the null.
    e10 = expected_max_sharpe(10, sr_variance=1.0)
    e100 = expected_max_sharpe(100, sr_variance=1.0)
    e1000 = expected_max_sharpe(1000, sr_variance=1.0)
    assert e10 < e100 < e1000
    assert expected_max_sharpe(1, sr_variance=1.0) == 0.0


def test_dsr_lower_than_psr_when_many_trials() -> None:
    # The whole point of DSR: trying many strategies should DEFLATE the
    # confidence relative to the naive PSR (which assumes a single trial).
    rets = RNG.normal(0.0015, 0.01, 500)
    psr = probabilistic_sharpe_ratio(rets, sr_benchmark=0.0)
    dsr = deflated_sharpe_ratio(rets, n_trials=1000, sr_variance=1.0)
    assert dsr <= psr


def test_pbo_low_for_genuinely_good_strategy() -> None:
    # One config has a real positive drift, the rest are noise. The good one
    # should keep winning OOS => low PBO.
    T, N = 240, 8
    M = RNG.normal(0, 0.01, (T, N))
    M[:, 0] += 0.003  # config 0 has real edge across the whole period
    res = probability_of_backtest_overfitting(M, n_partitions=8)
    assert 0.0 <= res.pbo <= 1.0
    assert res.pbo < 0.5  # genuine edge => not overfit
    assert res.n_splits == 70  # C(8,4) = 70


def test_pbo_high_for_pure_noise() -> None:
    # All configs are noise; IS winner is random => OOS rank ~ uniform =>
    # PBO should hover around 0.5 (no better than chance).
    T, N = 240, 10
    M = RNG.normal(0, 0.01, (T, N))
    res = probability_of_backtest_overfitting(M, n_partitions=8)
    assert res.pbo > 0.2  # pure noise should not look like a robust edge


def test_pbo_rejects_odd_partitions() -> None:
    with pytest.raises(ValueError):
        probability_of_backtest_overfitting(RNG.normal(0, 1, (100, 3)), n_partitions=7)
