"""Backtest evaluation metrics, with emphasis on overfitting-aware statistics.

The 38-day crypto PoC failed in part because a flagship alpha looked good on a
single backtest but collapsed under a 108-cell sensitivity sweep (0/108 passed).
The lesson baked into this module: never report a raw Sharpe without also
reporting the Deflated Sharpe Ratio (how much of that Sharpe survives the
multiple-testing correction) and, where a strategy grid exists, the Probability
of Backtest Overfitting.

References
----------
- Bailey, D. H., & López de Prado, M. (2014). "The Deflated Sharpe Ratio:
  Correcting for Selection Bias, Backtest Overfitting, and Non-Normality."
  Journal of Portfolio Management, 40(5), 94-107.
- Bailey, D. H., Borwein, J., López de Prado, M., & Zhu, Q. J. (2017). "The
  Probability of Backtest Overfitting." Journal of Computational Finance,
  20(4), 39-69. (CSCV method.)
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from itertools import combinations

import numpy as np
from scipy import stats

# Euler-Mascheroni constant, used in the expected-maximum-Sharpe estimator.
_EULER_MASCHERONI = 0.5772156649015329


def sharpe_ratio(
    returns: np.ndarray,
    periods_per_year: int = 252,
    risk_free: float = 0.0,
) -> float:
    """Annualized Sharpe ratio of a per-period return series.

    `returns` are simple per-period returns (not log). `risk_free` is per-period.
    Returns 0.0 for a degenerate (zero-variance or empty) series rather than
    raising — callers iterate over many alphas and a flat one shouldn't crash
    the sweep.
    """
    r = np.asarray(returns, dtype=float)
    if r.size < 2:
        return 0.0
    excess = r - risk_free
    sd = excess.std(ddof=1)
    if sd == 0 or not np.isfinite(sd):
        return 0.0
    return float(excess.mean() / sd * math.sqrt(periods_per_year))


def max_drawdown(equity_curve: np.ndarray) -> float:
    """Maximum drawdown as a negative fraction (e.g. -0.151 for -15.1%).

    `equity_curve` is a cumulative equity series (not returns). Returns 0.0 for
    an empty/single-point series.
    """
    eq = np.asarray(equity_curve, dtype=float)
    if eq.size < 2:
        return 0.0
    running_max = np.maximum.accumulate(eq)
    # guard against zero/negative equity in the denominator
    safe = np.where(running_max == 0, np.nan, running_max)
    drawdowns = (eq - running_max) / safe
    dd = np.nanmin(drawdowns)
    return float(dd) if np.isfinite(dd) else 0.0


def profit_factor(returns: np.ndarray) -> float:
    """Gross profit / gross loss. inf if there are no losing periods, 0.0 if no
    winning periods."""
    r = np.asarray(returns, dtype=float)
    gains = r[r > 0].sum()
    losses = -r[r < 0].sum()
    if losses == 0:
        return float("inf") if gains > 0 else 0.0
    return float(gains / losses)


def probabilistic_sharpe_ratio(
    returns: np.ndarray,
    sr_benchmark: float = 0.0,
    periods_per_year: int = 252,
) -> float:
    """Probabilistic Sharpe Ratio (PSR): P(true SR > sr_benchmark) given the
    observed track record, correcting for skew and kurtosis of the returns.

    Returns a probability in [0, 1]. `sr_benchmark` is expressed in the SAME
    annualization as the output of `sharpe_ratio`.
    """
    r = np.asarray(returns, dtype=float)
    n = r.size
    if n < 3:
        return 0.0
    sr_ann = sharpe_ratio(r, periods_per_year=periods_per_year)
    # convert annualized SRs to per-period for the PSR formula
    sr = sr_ann / math.sqrt(periods_per_year)
    sr_b = sr_benchmark / math.sqrt(periods_per_year)
    skew = float(stats.skew(r, bias=False)) if r.std() > 0 else 0.0
    kurt = float(stats.kurtosis(r, fisher=False, bias=False)) if r.std() > 0 else 3.0
    denom = math.sqrt(max(1e-12, 1 - skew * sr + (kurt - 1) / 4 * sr**2))
    psr = stats.norm.cdf((sr - sr_b) * math.sqrt(n - 1) / denom)
    return float(psr)


def expected_max_sharpe(
    n_trials: int,
    sr_variance: float,
) -> float:
    """Expected maximum Sharpe ratio under the null (all strategies have true
    SR = 0), given `n_trials` independent backtests whose estimated SRs have
    variance `sr_variance`. This is the SR* benchmark in the Deflated Sharpe
    Ratio.

    Bailey & López de Prado (2014), eq. for E[max SR].
    """
    if n_trials < 1:
        return 0.0
    if n_trials == 1:
        return 0.0
    sigma = math.sqrt(max(0.0, sr_variance))
    z1 = stats.norm.ppf(1 - 1.0 / n_trials)
    z2 = stats.norm.ppf(1 - 1.0 / (n_trials * math.e))
    return float(sigma * ((1 - _EULER_MASCHERONI) * z1 + _EULER_MASCHERONI * z2))


def deflated_sharpe_ratio(
    returns: np.ndarray,
    n_trials: int,
    sr_variance: float,
    periods_per_year: int = 252,
) -> float:
    """Deflated Sharpe Ratio (DSR): the PSR evaluated against the expected
    maximum Sharpe from `n_trials` independent trials, instead of against 0.

    A DSR > 0.95 means the observed Sharpe is unlikely to be a false positive
    arising from having tried `n_trials` strategies. `sr_variance` is the
    variance of the (annualized) SR estimates across the trials.

    Returns a probability in [0, 1].
    """
    sr_star_ann = expected_max_sharpe(n_trials, sr_variance)
    return probabilistic_sharpe_ratio(
        returns, sr_benchmark=sr_star_ann, periods_per_year=periods_per_year
    )


@dataclass
class PBOResult:
    pbo: float  # probability of backtest overfitting in [0, 1]
    n_splits: int  # number of IS/OOS combinations evaluated
    logits: list[float]  # logit of OOS relative rank for each split's IS-best


def probability_of_backtest_overfitting(
    returns_matrix: np.ndarray,
    n_partitions: int = 10,
) -> PBOResult:
    """CSCV Probability of Backtest Overfitting.

    Parameters
    ----------
    returns_matrix : np.ndarray, shape (T, N)
        T per-period observations for N strategy configurations.
    n_partitions : int
        Number of disjoint, contiguous, equal-size time blocks S (must be even).
        The matrix is split into S blocks; every way of choosing S/2 blocks as
        in-sample (the rest as out-of-sample) is evaluated.

    Method
    ------
    For each combination C(S, S/2):
      1. Build IS from the chosen blocks, OOS from the rest.
      2. Pick the config with the best IS Sharpe.
      3. Find that config's *relative rank* in OOS (0=worst, 1=best).
      4. logit = ln(rank / (1 - rank)).
    PBO = fraction of combinations where logit <= 0 (i.e. the IS-best config
    landed in the bottom half OOS — the signature of overfitting).

    Returns a `PBOResult`. A PBO near 0 is good (IS winners keep winning OOS);
    PBO >= 0.5 means the backtest selection is no better than random OOS.
    """
    M = np.asarray(returns_matrix, dtype=float)
    if M.ndim != 2:
        raise ValueError("returns_matrix must be 2D (T observations x N configs)")
    T, N = M.shape
    if N < 2:
        raise ValueError("need at least 2 strategy configurations")
    if n_partitions % 2 != 0:
        raise ValueError("n_partitions must be even")
    if T < n_partitions:
        raise ValueError(f"need at least {n_partitions} observations, got {T}")

    # Split rows into S contiguous, (near) equal blocks.
    block_idx = np.array_split(np.arange(T), n_partitions)
    s = n_partitions
    half = s // 2

    logits: list[float] = []
    for is_blocks in combinations(range(s), half):
        is_set = set(is_blocks)
        is_rows = np.concatenate([block_idx[b] for b in range(s) if b in is_set])
        oos_rows = np.concatenate([block_idx[b] for b in range(s) if b not in is_set])

        is_sr = np.array([sharpe_ratio(M[is_rows, j]) for j in range(N)])
        oos_sr = np.array([sharpe_ratio(M[oos_rows, j]) for j in range(N)])

        best_is = int(np.argmax(is_sr))
        # relative rank of the IS-best config among OOS Sharpes
        order = np.argsort(oos_sr)  # ascending
        rank_pos = int(np.where(order == best_is)[0][0])  # 0..N-1
        rel_rank = (rank_pos + 1) / (N + 1)  # in (0,1), avoids 0 and 1
        logit = math.log(rel_rank / (1 - rel_rank))
        logits.append(logit)

    pbo = float(np.mean([1.0 if lg <= 0 else 0.0 for lg in logits])) if logits else 0.0
    return PBOResult(pbo=pbo, n_splits=len(logits), logits=logits)


__all__ = [
    "sharpe_ratio",
    "max_drawdown",
    "profit_factor",
    "probabilistic_sharpe_ratio",
    "expected_max_sharpe",
    "deflated_sharpe_ratio",
    "probability_of_backtest_overfitting",
    "PBOResult",
]
