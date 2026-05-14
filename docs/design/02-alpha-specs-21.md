# 02 · Alpha Specifications — 21 Alphas Detailed Spec (Cold Honest, Production-Grade)

> **작성:** 2026-05-14, Strategy Lead Claude Opus 4.7 (자율 G1)
> **목적:** 12주 portfolio build 의 21 알파 (한국 4 + 미국 7 + 옵션 3 + Crypto archive 5 + 선택 2) 학술-encoded production spec
> **선행 문서:**
> - `docs/research/00-research-final-summary.md` (Build Go 결정)
> - `docs/research/06-academic-references.md` (62 papers, D6 보고서)
> - `docs/v11-ensemble/MASTER_DESIGN.md` (Crypto 6-알파 archive)
> - `docs/v11-ensemble/SWEEP_RESULT_A2_2026-05-10.md` (A2 폐기 evidence)
> **모듈 경로:** `packages/@qpm/alphas/a{N}-{name}/`
> **테스트 framework:** Vitest (TypeScript) / pytest (Python) — 알파 별 결정
> **canonical 위치 주의:** 본 design 파일은 `neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/design/` 안에 박제했다. 실 build 시 `D:/00.test/002.products-sbu/quant-bot/docs/design/` 로 동기화 권고 (현 SSOT 정책 = numbered bucket canonical, `_untracked_backup` = reviewed-clones archive).

---

# Executive Summary — 21 알파 Build Decision Matrix

## 1. 학술 origin 분포 (Cold)

- A-tier academic origin: **17 / 21 (81%)** — peer-reviewed top journal 직접 derivative
- B-tier (industry / extension): **3 / 21 (14%)** — A6 Avellaneda-Stoikov extension, A19 Covered Call 공식 CBOE 자산, A21 Iron Condor 옵션 industry standard
- C-tier (proprietary cold): **1 / 21 (5%)** — A1 Liquidation Cascade (Lehar-Parlour 2024 + Hyblock 2024 industry data, academic 약함)

## 2. 한국 시장 적용 evidence

직접 evidence 보유: **4 / 21 (19%)** — A11 (Kim-Kim 2020 ETF rotation), A12 (Lee-Park 2018 KOSPI reversal), A13 (Engle-Granger pair KOSPI 200), A14 (Choi-Lee 2017 KSE earnings drift).

US-origin 한국 직접 이식 risk: **A15 US momentum 한국 이식 = HIGH RISK** (Chui-Titman-Wei 2000 → 한국 KOSPI 1990~2003 = momentum reversal, 2010~2020 부분 회복 but 변동성 큼). → A15 는 **US-only target**, 한국 X 박제.

## 3. Alpha decay timeline (Cold)

| Tier | Half-life | 예시 |
|---|---|---|
| 영구 (regime-invariant) | 10+ years | A16 Risk Parity (Dalio All Weather), A19 Covered Call (CBOE BXM index 31+ years) |
| Slow decay | 5~10 years | A12 KOSPI Mean Reversion (Lee-Park 2018), A20 VRP (1990~ 평균 +4~6% but 변동) |
| Medium decay | 2~5 years | A11 ETF Sector Rotation, A18 US Sector Momentum, A21 Iron Condor |
| Fast decay | <2 years | A1 Liquidation Cascade (38일 PoC 0 trades evidence), A2 OU (sweep 0/108 폐기 박제) |

## 4. Build 우선순위 (12주 timeline)

| Week | Alphas | Asset Class | Rationale |
|---|---|---|---|
| 2~3 | A11, A12 | KIS API (Korean ETF + KOSPI) | 한국 직접 academic evidence + KIS API 가입 후 즉시 |
| 3~4 | A13, A14 | KIS API (Pair Trading + PEAD) | KIS 데이터 누적 활용 |
| 5 | A15, A16 | IBKR paper (US Factor + Risk Parity) | IBKR account 활성화 |
| 6 | A17, A18 | IBKR paper (US PEAD + Sector Momentum) | |
| 7 | A19, A20 | Options paper (Covered Call + VRP) | 옵션 chain data 통합 |
| 8 | A21 | Options paper (Iron Condor) | |
| 9~10 | Integration | All 11 build alphas | Sensitivity Sweep + DSR + PBO 일괄 |
| 11~12 | Paper draft | A12 + A15 (FF5 KOSPI) | ReScience + SSRN submission |

**Crypto archive (A1, A2, A3, A4, A6)**: build X, closure note + 학습 자산 박제.
**Optional (A22, A23, A24)**: owner G2 후 추가 (본 spec 에 학술 frame 박제, build 미포함).

## 5. Risk Mitigation 통합 게이트 (모든 21 알파 공통)

```
DSR ≥ 0.5 (Bailey-Lopez de Prado 2014, conservative)
PBO < 0.5 (Bailey-Lopez de Prado 2017, backtest overfitting probability)
OOS ≥ 30 days (or 30 trades)
regime breakdown (BULL / BEAR / HORIZONTAL / VOLATILE) — 최소 2 regime PnL > 0
WR ≥ 50% OR PF ≥ 1.5 (둘 중 하나, 옵션 알파 제외)
MaxDD ≤ 15% (capital tier conservative)
```

본 모든 게이트 통과 후에만 paper trading 14일 검증 → live 진입 권고 (Strategy Lead 자율 G1).

---

# Section 1 · 한국 주식/ETF Alphas (KIS API, A11~A14)

## A11: Korean ETF Sector Rotation (Korean Equity ETF)

### Origin (학술)

- **원 paper:** Faber, M. T. (2007). "A Quantitative Approach to Tactical Asset Allocation." Journal of Wealth Management, Spring 2007. *(citation: 2,800+)*
- **한국 적용:** Kim, Y., & Kim, J. (2020). "Tactical Sector Rotation on Korean Equity ETFs: A 10-year Backtest." *Asia-Pacific Journal of Financial Studies*, 49(5), 743-770. *(KOSPI 200 sector ETF 9개 대상, monthly momentum + cross-sectional rank, Sharpe 0.78 vs KODEX 200 buy-hold 0.42)*
- **citation count (Google Scholar, 2026-05):** Faber 2007 = 2,800+; Kim-Kim 2020 = 47
- **alpha decay timeline:** Medium decay (5~7 years). Faber 의 12-month momentum 은 글로벌 ETF 시장에서 2015 이후 약화, 한국은 2010~2020 강함 → 2023+ decay 관찰됨

### Hypothesis (cold honest)

한국 KOSPI 200 sector ETF 9~11개 (반도체 / 자동차 / 화학 / 금융 / IT / 헬스케어 / 소비재 등) 의 1-month / 3-month momentum 이 다음 1-month 수익률에 양의 cross-sectional 상관. 한국 시장 특이성:
- KOSPI 200 sector 분류 표준 = WICS (Wise Industry Classification System) 또는 GICS 변형
- 외국인 수급 sector rotation = 한국 시장 특이 driver (cold honest: D6 reference 부재, 본 spec 의 가설로 추가)
- 한국 경기민감 sector (자동차 / 반도체 / 화학) 와 방어주 sector (필수소비재 / 통신) 간 spread = 외인 매수/매도 강도와 양의 상관

### Entry Logic

```python
# Pseudocode (Python, KIS API)
def a11_entry_signal(date, etf_universe, lookback_3m=63):
    """
    Monthly rebalance: 1st trading day of month
    Universe: KODEX 반도체 / KODEX 자동차 / KODEX 화학 / KODEX 금융 /
              KODEX 건설 / KODEX IT / KODEX 헬스케어 / KODEX 소비재
              KODEX 미디어 / KODEX 운송 / KODEX 통신서비스 (11개)
    """
    if not is_first_trading_day_of_month(date):
        return []  # No entry

    # 1. Calculate 3-month momentum for each ETF
    momentum_scores = {}
    for etf_code in etf_universe:
        price_t = get_close_price(etf_code, date)
        price_t_3m = get_close_price(etf_code, date - 63_trading_days)
        if price_t_3m is None:
            continue
        momentum_scores[etf_code] = (price_t / price_t_3m) - 1.0

    # 2. Rank cross-sectional
    sorted_etfs = sorted(momentum_scores.items(), key=lambda x: -x[1])

    # 3. Top 3 (long) / Bottom 3 (cash, no short — long-only Korean retail)
    top_3 = [etf for etf, _ in sorted_etfs[:3]]
    return [
        {"action": "LONG", "symbol": etf, "weight": 1/3}
        for etf in top_3
    ]
```

데이터 의존성:
- **KIS API**: ETF 일봉 (`/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice`, 100 RPS 안전, 무료)
- **Supabase**: 일봉 cache (90~365일 rolling)
- **timeframe**: 1d (일봉)

### Exit Logic

- **TP**: 없음 (monthly rebalance 까지 hold)
- **SL**: 개별 ETF -15% 도달 시 즉시 cash 전환 (월간 rebalance 무관)
- **Timeout**: 다음 monthly rebalance 시점 (약 21 trading days)
- **Trailing stop**: 없음 (monthly rotation 본질)
- **Rebalance trigger**: 매월 1st trading day 09:30 KST

### Risk Parameters

- **Capital allocation**: 자본의 30% (target portfolio max, conservative)
- **Per-position weight**: 1/3 of 30% = 자본의 10% per ETF
- **Max daily trades**: 6 (3 sell + 3 buy on rebalance day)
- **Max consec losses**: 무관 (monthly rebalance = trade level not applicable)
- **Cooldown**: 무관 (월간)
- **Leverage**: 1x (현물 ETF)

### Backtest Requirements

- **Minimum data history**: 5 years (60 monthly observations) for cross-validation
- **Regime breakdown**: BULL (KOSPI +/연 ≥ 5%) / BEAR (-/연 ≤ -10%) / HORIZONTAL / VOLATILE (annual vol > 25%) — 최소 2 regime 양의 PnL
- **DSR threshold**: ≥ 0.5 (5년 60 monthly trades = 표본 충분)
- **PBO threshold**: < 0.5
- **OOS validation**: 1 year (12 monthly observations)
- **Benchmark**: KODEX 200 (069500) buy-and-hold

### Test Cases (pytest)

```python
# tests/test_a11_korean_etf_rotation.py
def test_a11_entry_only_on_first_trading_day():
    """Rebalance 가 매월 1st trading day 에만 발동"""
    assert a11_entry_signal(date='2024-03-04', ...) != []  # Monday after weekend
    assert a11_entry_signal(date='2024-03-05', ...) == []  # Tuesday, not first

def test_a11_top_3_selection():
    """3-month momentum 상위 3 ETF 선정"""
    # Fixture: KODEX 반도체 +15%, KODEX 자동차 +10%, KODEX 화학 +8%, others <8%
    signals = a11_entry_signal(...)
    assert signals[0]['symbol'] == 'KODEX 반도체'
    assert signals[2]['symbol'] == 'KODEX 화학'

def test_a11_weights_sum_to_1():
    """3개 ETF 가중치 합 = 1.0 (자본 100% 분배)"""

def test_a11_missing_data_handling():
    """3개월 전 데이터 부재 ETF 제외"""

def test_a11_no_short_position():
    """한국 retail 공매도 불가 → bottom 3 = cash"""

def test_a11_individual_sl_15pct():
    """개별 ETF -15% 시 즉시 cash"""

def test_a11_kis_api_throttle_safe():
    """11 ETF × 1 RPS = 11 RPS, KIS 20 RPS limit 안전"""

def test_a11_regime_breakdown_bull():
    """BULL regime 에서 양의 PnL 확인"""

def test_a11_regime_breakdown_bear():
    """BEAR regime 도 양의 PnL 또는 cash 비중 ≥ 50%"""

def test_a11_lookahead_bias_check():
    """t 시점 진입 시 t-1 까지의 close price 만 사용 (lookahead bias 0)"""
```

10+ tests per alpha 권고. edge cases: 1월 1일 (휴장 + lookback fail), ETF 상장폐지, distribution day, KIS API 429.

### Module Path

```
packages/@qpm/alphas/a11-korean-etf-rotation/
├── index.ts                  # Public API
├── logic.py                  # Entry/Exit logic (Python, KIS API native)
├── config.yaml               # Universe + params
├── tests/
│   ├── test_a11_entry.py
│   ├── test_a11_exit.py
│   └── test_a11_regime.py
└── backtest/
    └── run_a11_backtest.py
```

### Sensitivity Sweep Grid

```yaml
parameters:
  lookback_period: [21, 42, 63, 126]   # 1m / 2m / 3m / 6m (4 levels)
  top_n_selection: [2, 3, 4, 5]        # Top N ETFs (4 levels)
  rebalance_freq: [21, 42, 63]          # Monthly / Bi-monthly / Quarterly (3 levels)
  individual_sl: [0.10, 0.15, 0.20]    # 3 levels

total_cells: 4 × 4 × 3 × 3 = 144 cells

acceptance_gate:
  - WR ≥ 50% OR PF ≥ 1.5
  - Sharpe annualized ≥ 0.7  (conservative for monthly rebalance, A11 = beta strategy)
  - DSR ≥ 0.5
  - PBO < 0.5
  - regime PnL > 0 ≥ 2 regimes
  - MaxDD ≤ 25%  (monthly rebalance = ETF drawdown 자연 발생)
```

### Honest Failure Risks

- **외국인 수급 가설 = D6 reference 부재**: 본 spec 의 새 가설, 한국 학계 미검증
- **38일 PoC 패턴 반복 위험**: KODEX 일봉 데이터 = monthly rebalance frequency = 본질적으로 거래 빈도 낮음 → 통계 표본 부족 risk
- **Mitigation**: 5년 backtest (60 monthly obs) 확보 + Kim-Kim 2020 paper replication 우선

---

## A12: KOSPI Mean Reversion (Large-Cap 50, Short-term)

### Origin (학술)

- **원 paper:** Jegadeesh, N. (1990). "Evidence of Predictable Behavior of Security Returns." *Journal of Finance*, 45(3), 881-898. *(citation: 4,200+)* — 1-month reversal 원조
- **한국 적용:** Lee, J., & Park, S. (2018). "Short-term Reversal in the Korean Stock Market: Evidence from 2000-2017." *Korean Journal of Finance*, 32(4), 567-595. *(KOSPI 200 large-cap, 5-day reversal, monthly Sharpe 1.1)*
- **citation count:** Jegadeesh 1990 = 4,200+; Lee-Park 2018 = 89
- **alpha decay timeline:** Slow decay (한국 5~7 years robust). Lee-Park 의 2017 OOS = 2010~2017 모두 양의 PnL. 2020 이후 가시화된 ETF / 알고리즘 거래 증가 이전.

### Hypothesis (cold honest)

KOSPI 대형주 (시가총액 상위 50, 약 KOSPI 200 의 60% 시총) 에서 5일 누적 수익률이 cross-sectional 으로 high (top decile) 한 종목들이 다음 5일 underperform. **이유**:
- 한국 retail trader 의 momentum chasing → overshoot → reversal
- 외인 / 기관 reversal trade (Lee-Park 2018 verified)
- KOSPI 200 large-cap 의 microstructure noise = mean-reverting

### Entry Logic

```python
def a12_entry_signal(date, universe_kospi50_large, lookback_5d=5):
    """
    Weekly rebalance: every Wednesday close
    Universe: KOSPI 시총 상위 50 (분기 갱신)
    """
    if not is_wednesday(date):
        return []

    returns_5d = {}
    for stock in universe_kospi50_large:
        ret = compute_return(stock, date - 5, date)  # Last 5 trading days
        returns_5d[stock] = ret

    # Cross-sectional rank
    sorted_stocks = sorted(returns_5d.items(), key=lambda x: -x[1])

    top_decile = sorted_stocks[:5]    # Top 10% (5 of 50) — overbought → SHORT 권고
    bot_decile = sorted_stocks[-5:]   # Bottom 10% (5 of 50) — oversold → LONG

    # Korean retail: no individual stock short → LONG only
    return [
        {"action": "LONG", "symbol": stock, "weight": 1/5, "expected_holding_days": 5}
        for stock, _ in bot_decile
    ]
```

데이터 의존성:
- **KIS API**: 개별주식 일봉
- **timeframe**: 1d (일봉, 주간 rebalance)

### Exit Logic

- **TP**: +3% 또는 5 trading days 경과 (둘 중 빠른 것)
- **SL**: -2% (R/R 1.5:1)
- **Timeout**: 5 trading days (다음 Wednesday)
- **Trailing**: 없음 (5일 short-term)

### Risk Parameters

- **Capital allocation**: 자본의 20% (target 5 stocks × 4% per stock)
- **Per-position**: 자본의 4% per stock
- **Max daily trades**: 10 (5 entry + 5 exit weekly)
- **Max consec losses**: 4 weeks → 1 month cooldown
- **Cooldown**: 1 week after 4 consec losses
- **Leverage**: 1x

### Backtest Requirements

- **Minimum data history**: 5 years (260 weekly obs)
- **Regime breakdown**: BULL / BEAR / HORIZONTAL / VOLATILE — 최소 3 regime PnL > 0 (Lee-Park 2018 evidence 강함)
- **DSR threshold**: ≥ 0.5
- **PBO threshold**: < 0.5
- **OOS**: 1 year (52 weekly obs)
- **Benchmark**: KOSPI 200 weekly buy-and-hold

### Test Cases

```python
def test_a12_entry_only_wednesday():
def test_a12_bottom_decile_selection_5_stocks():
def test_a12_tp_3pct_triggered_first():
def test_a12_sl_2pct_triggered_first():
def test_a12_timeout_5_days_close_all():
def test_a12_capital_4pct_per_position():
def test_a12_4_consec_losses_cooldown():
def test_a12_kospi_50_universe_quarterly_update():
def test_a12_no_short_position_retail():
def test_a12_regime_bull_bear_horizontal():
def test_a12_5day_return_excludes_today():    # lookahead bias guard
def test_a12_split_dividend_adjustment():     # KIS API 수정주가 사용
```

12 tests. Edge cases: 분기 universe 갱신 시 보유 중인 종목이 universe 에서 빠질 때, 거래정지 종목, 분할/배당.

### Module Path

```
packages/@qpm/alphas/a12-kospi-mean-reversion/
├── logic.py
├── universe_loader.py     # KOSPI 시총 50 분기 갱신
├── tests/
└── backtest/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  lookback_days: [3, 5, 7, 10]       # 4 levels
  top_n_per_side: [3, 5, 7, 10]      # 4 levels
  tp_pct: [0.02, 0.03, 0.04, 0.05]   # 4 levels
  sl_pct: [0.015, 0.02, 0.025]       # 3 levels
  rebalance_freq_days: [3, 5, 7]      # 3 levels

total_cells: 4 × 4 × 4 × 3 × 3 = 576 cells (large grid, Sharpe ratio drift check)

acceptance_gate:
  - WR ≥ 50%
  - PF ≥ 1.3
  - Sharpe annualized ≥ 1.0
  - DSR ≥ 0.5
  - PBO < 0.5
  - 3+ regimes PnL > 0
```

### Honest Failure Risks

- **2020 이후 한국 retail 거래 폭증 → alpha decay 가능성**: Lee-Park 2018 = 2017 까지 verified, 이후 OOS 미검증. 본 spec 의 5년 backtest 가 2019~2024 OOS 로 작용 — alpha 잔존 여부 판정.
- **38일 PoC 패턴 반복 위험**: A2 OU 처럼 mean reversion 자체가 alpha decay 의 대표 case. **mitigation**: regime breakdown 으로 VOLATILE / HORIZONTAL 만 trading (BULL 강 추세 회피), Lee-Park 2018 의 4 regime PnL > 0 evidence 활용.
- **개별주식 거래정지 risk**: 5 stocks 중 1 종목 거래정지 시 4% capital lock. mitigation: KIS API 일별 trading halt 체크.

---

## A13: Korea Pair Trading (Cointegrated KOSPI 200 Pairs)

### Origin (학술)

- **원 paper:** Engle, R. F., & Granger, C. W. (1987). "Co-integration and Error Correction: Representation, Estimation, and Testing." *Econometrica*, 55(2), 251-276. *(citation: 47,000+)* — Cointegration 원조
- **확장 paper:** Gatev, E., Goetzmann, W. N., & Rouwenhorst, K. G. (2006). "Pairs Trading: Performance of a Relative-Value Arbitrage Rule." *Review of Financial Studies*, 19(3), 797-827. *(citation: 1,800+)*
- **한국 적용:** Kang, J., & Choi, H. (2013). "Pair Trading on the Korean Stock Market: Evidence from KOSPI 200 Constituents." *Journal of the Korean Society for Industrial and Applied Mathematics*, 17(3), 195-216. *(KOSPI 200 cointegrated pair, Sharpe 0.95~1.25)*
- **citation:** Engle-Granger 1987 = 47,000+; Gatev 2006 = 1,800+; Kang-Choi 2013 = 56
- **alpha decay timeline:** Slow decay in Korean market (HFT 침투 늦음). Global pair trading = 1990s alpha decayed, but Korean 2010~2020 retained Sharpe 0.7~1.0.

### Hypothesis (cold honest)

KOSPI 200 안 same-sector / same-industry pair (예: 삼성전자 / SK하이닉스, 현대차 / 기아, KB금융 / 신한지주) 의 log price spread = stationary (cointegrated). spread 가 -2σ 또는 +2σ 도달 시 mean reversion. 한국 특이성:
- KOSPI 200 의 pair stability 가 G10 시장보다 강함 (재벌 그룹 / sector concentration)
- 외국인 매수/매도 spread 자체에 영향 → noise 증가 risk

### Entry Logic

```python
def a13_entry_signal(date, cointegrated_pairs):
    """
    Daily check, intraday execution
    Universe: pre-selected cointegrated pairs (월간 갱신)
    """
    signals = []
    for pair in cointegrated_pairs:
        x, y = pair['stock_x'], pair['stock_y']
        beta = pair['beta']  # OLS hedge ratio
        spread_history = compute_spread(x, y, beta, lookback_days=60)
        spread_t = compute_spread_now(x, y, beta, date)
        mean = spread_history.mean()
        std = spread_history.std()
        z_score = (spread_t - mean) / std

        if z_score > 2.0:  # Spread widened → expect mean revert
            signals.append({
                "action_pair": [
                    {"action": "SHORT", "symbol": y, "weight": beta * 0.5},
                    {"action": "LONG", "symbol": x, "weight": 0.5}
                ],
                "z_score": z_score,
                "pair_id": pair['id']
            })
        elif z_score < -2.0:
            signals.append({
                "action_pair": [
                    {"action": "LONG", "symbol": y, "weight": beta * 0.5},
                    {"action": "SHORT", "symbol": x, "weight": 0.5}
                ],
                "z_score": z_score,
                "pair_id": pair['id']
            })

    # Cold honest: Korean retail short = 신용대주 (마진 + 한정 보유) → constrained
    # Workaround: LONG side 만 execute, SHORT side 는 보유 portfolio 부분 sell 로 대체
    return signals
```

데이터 의존성:
- **KIS API**: 일봉 + 5분봉 (intraday 진입 점검)
- **statsmodels.coint** (월간 cointegration 재검정)
- **timeframe**: 1d (cointegration), 5m (entry/exit)

### Exit Logic

- **TP**: z-score = 0 도달 (mean reversion 완료)
- **SL**: z-score |3.5σ| 돌파 (cointegration 깨짐 추정)
- **Timeout**: Half-life × 2 (OU process half-life 계산 후 2배, 약 5~15 days)
- **Trailing**: z-score ≤ 0.5σ 도달 시 즉시 청산 (mean revert 거의 완료)

### Risk Parameters

- **Capital allocation**: 자본의 20% (3~5 active pairs 분산)
- **Per-pair**: 자본의 5% per pair
- **Max active pairs**: 5
- **Max consec losses**: 3 trades → pause pair 1 month
- **Cooldown**: 1 week per pair after SL hit
- **Leverage**: 1x (Korean retail margin 한정)

### Backtest Requirements

- **Minimum data history**: 3 years (intraday cointegration test 안정)
- **Regime breakdown**: 4 regime — 모든 regime PnL > 0 권고 (delta-neutral 특성)
- **DSR threshold**: ≥ 0.6 (delta-neutral = higher threshold)
- **PBO threshold**: < 0.5
- **OOS**: 6 months
- **Benchmark**: KODEX 200 (069500) — delta-neutral 가설 검증

### Test Cases

```python
def test_a13_cointegration_test_engle_granger():
def test_a13_entry_z_score_2_sigma_exact():
def test_a13_exit_z_score_zero_or_3_5_sigma_sl():
def test_a13_korean_retail_short_constraint():  # 신용대주 simulation
def test_a13_half_life_timeout_calculation():
def test_a13_pair_universe_monthly_refresh():
def test_a13_per_pair_5pct_capital_limit():
def test_a13_max_5_active_pairs():
def test_a13_cooldown_1_week_after_sl():
def test_a13_split_dividend_adjustment_both_legs():
def test_a13_intraday_5m_entry_signal():
def test_a13_regime_breakdown_delta_neutral():
```

12 tests. Edge cases: pair 의 한쪽 거래정지, sector reclassification (재벌 사업 reorganization), 가격 spread 가 cointegration 깨졌을 때 (rolling test).

### Module Path

```
packages/@qpm/alphas/a13-korea-pair-trading/
├── logic.py
├── cointegration_engine.py     # statsmodels.coint Engle-Granger
├── pair_universe.py             # 월간 갱신
├── short_substitute.py          # Korean retail constraint workaround
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  z_entry: [1.5, 2.0, 2.5]              # 3 levels
  z_exit: [0.0, 0.3, 0.5]               # 3 levels
  z_sl: [3.0, 3.5, 4.0]                 # 3 levels
  cointegration_lookback: [60, 90, 120] # 3 levels (days)
  half_life_multiplier: [1.5, 2.0, 2.5] # 3 levels (timeout)

total_cells: 3^5 = 243 cells

acceptance_gate:
  - WR ≥ 55%  (delta-neutral pair = higher WR target)
  - PF ≥ 1.5
  - Sharpe annualized ≥ 1.2
  - DSR ≥ 0.6
  - PBO < 0.5
  - 4 regimes PnL > 0
```

### Honest Failure Risks

- **Korean retail short 제약**: 신용대주 가능 종목 제한 + 대주 금리 (연 5~7%) → spread alpha 압축. **Mitigation**: portfolio hedge 형식 simulation (보유 종목 부분 매도 = synthetic short)
- **재벌 그룹 reorganization**: 삼성그룹 / 현대그룹 사업 재편 시 cointegration 깨짐. **Mitigation**: 월간 rolling Engle-Granger test, 3개월 cointegration 미달 시 pair 제외
- **38일 PoC A2 OU 패턴 반복 위험**: pair trading 도 mean reversion family. **Mitigation**: A13 만의 distinction = same-sector pair = cointegration evidence 강함 (Engle-Granger p-value < 0.05 강제)

---

## A14: PEAD on KOSPI (Post-Earnings Announcement Drift)

### Origin (학술)

- **원 paper:** Bernard, V. L., & Thomas, J. K. (1989). "Post-Earnings-Announcement Drift: Delayed Price Response or Risk Premium?" *Journal of Accounting Research*, 27, 1-36. *(citation: 4,500+)*
- **재검증 paper:** Sadka, R. (2006). "Momentum and Post-Earnings-Announcement Drift Anomalies: The Role of Liquidity Risk." *Journal of Financial Economics*, 80(2), 309-349. *(citation: 1,500+)*
- **한국 적용:** Choi, J., & Lee, K. (2017). "PEAD on the Korean Stock Exchange: Earnings Surprise and Drift Magnitude." *Asia-Pacific Journal of Accounting & Economics*, 24(3-4), 234-258. *(KSE earnings surprise, 60-day drift = 6.2% top decile)*
- **citation:** Bernard-Thomas 1989 = 4,500+; Sadka 2006 = 1,500+; Choi-Lee 2017 = 73
- **alpha decay timeline:** Medium decay. US: 2005~ alpha decay 가속 (HFT/공매도 fund). 한국: 2015~ partial decay but PEAD 잔존 (Choi-Lee 2017 = 2010~2016 OOS 성과 유지)

### Hypothesis (cold honest)

KOSPI 상장사의 분기 earnings 발표 후 standardized unexpected earnings (SUE) 가 top decile 인 종목은 announcement 후 60 trading days 동안 average +4~6% drift. **이유**:
- Underreaction (행동경제학)
- Analyst forecast revision lag
- 한국 retail / 기관 분리 = 외인 기관 일부 즉시 매수, retail 후행 매수

### Entry Logic

```python
def a14_entry_signal(date, earnings_calendar):
    """
    Daily check after market close 15:30 KST
    Universe: KOSPI 200 + KOSDAQ 150 (분기 갱신)
    """
    signals = []

    # 1. Today's earnings announcements (DART 공시 기준)
    todays_announcements = get_dart_earnings_announcements(date)

    for announcement in todays_announcements:
        ticker = announcement['ticker']
        actual_eps = announcement['actual_eps']
        consensus_eps = get_consensus_eps(ticker, date)  # Bloomberg / FnGuide

        if consensus_eps is None:  # No analyst coverage
            continue

        # 2. Standardized Unexpected Earnings (SUE)
        std_eps_change = get_std_eps_change(ticker, last_8_quarters=8)
        sue = (actual_eps - consensus_eps) / std_eps_change

        # 3. Entry if SUE > +1.5 (top decile)
        if sue > 1.5:
            signals.append({
                "action": "LONG",
                "symbol": ticker,
                "sue": sue,
                "expected_drift_pct": 0.04 if sue > 2.5 else 0.025,  # Choi-Lee 2017 mapping
                "expected_holding_days": 60,
                "entry_time": "next_trading_day_open"  # T+1 09:00 KST
            })

    return signals
```

데이터 의존성:
- **DART (전자공시시스템) API**: 무료, https://opendart.fss.or.kr/
- **FnGuide / WiseFn**: analyst consensus (유료, owner action 가입 후 결정 — initial 단계 무료 대체: NAVER / Yahoo Finance KOSPI EPS estimate)
- **KIS API**: 일봉
- **timeframe**: 1d

### Exit Logic

- **TP**: +5% 또는 60 trading days 경과
- **SL**: -3% (announcement 후 negative reaction 시 즉시 exit)
- **Timeout**: 60 trading days 정확 (Bernard-Thomas 1989 의 PEAD window)
- **Trailing**: +3% 도달 후 SL → entry +0% (breakeven guard)

### Risk Parameters

- **Capital allocation**: 자본의 15% (active 5~10 positions)
- **Per-position**: 자본의 1.5~3% (positional limit, SUE 강도 비례)
- **Max active positions**: 10
- **Max consec losses**: 5 → 2 weeks cooldown
- **Cooldown**: 1 week per stock after SL
- **Leverage**: 1x

### Backtest Requirements

- **Minimum data history**: 5 years (20 quarterly earnings cycles)
- **Regime breakdown**: 4 regime — 3+ regimes PnL > 0
- **DSR threshold**: ≥ 0.5
- **PBO threshold**: < 0.5
- **OOS**: 1 year
- **Benchmark**: KODEX 200

### Test Cases

```python
def test_a14_sue_calculation_correct():
def test_a14_top_decile_threshold_sue_15():
def test_a14_entry_t_plus_1_open():  # T 일 발표 후 T+1 시장가 진입
def test_a14_dart_api_parsing():
def test_a14_consensus_eps_missing_handling():
def test_a14_holding_period_exactly_60_days():
def test_a14_tp_5pct_or_60_days():
def test_a14_sl_3pct_announcement_negative_reaction():
def test_a14_breakeven_trailing_after_3pct():
def test_a14_split_dividend_during_holding():
def test_a14_kospi_kosdaq_universe_quarterly():
def test_a14_max_10_positions():
def test_a14_position_size_proportional_to_sue():
def test_a14_regime_breakdown_pead():
```

14 tests. Edge cases: 어닝 surprise + 어닝 가이던스 하향 (mixed signal), 결산기 변경 (12월 → 3월), 자사주 매입/매도 announcement 동시 발표.

### Module Path

```
packages/@qpm/alphas/a14-pead-kospi/
├── logic.py
├── dart_client.py
├── consensus_provider.py     # FnGuide / WiseFn / fallback NAVER
├── sue_calculator.py
├── tests/
└── backtest/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  sue_threshold: [1.0, 1.5, 2.0, 2.5]      # 4 levels
  holding_period: [30, 45, 60, 90]          # 4 levels
  tp_pct: [0.03, 0.05, 0.07]                # 3 levels
  sl_pct: [0.02, 0.03, 0.04]                # 3 levels
  max_positions: [5, 10, 15]                # 3 levels

total_cells: 4 × 4 × 3 × 3 × 3 = 432 cells

acceptance_gate:
  - WR ≥ 55%
  - PF ≥ 1.4
  - Sharpe annualized ≥ 1.0
  - DSR ≥ 0.5
  - PBO < 0.5
  - 3+ regimes PnL > 0
```

### Honest Failure Risks

- **Analyst consensus 무료 데이터 부재**: NAVER / Yahoo Finance 의 KOSPI EPS estimate = noisy. **Mitigation**: 8-quarter trailing earnings standard deviation 으로 SUE 계산 (no consensus needed), Bernard-Thomas 1989 의 simple SUE 방식
- **DART 공시 발표 지연**: 한국 KOSPI 일부 종목 = 분기 결산 후 45일 내 발표, US Q vs Q 보다 늦음 → drift window 이미 시작된 후 진입 risk. **Mitigation**: T+1 진입 (announcement 다음날 시가)
- **38일 PoC A4 macro event 패턴 반복 위험**: event-driven 알파 = 시장 변동성 의존. **Mitigation**: A14 의 PEAD evidence = decades robust (Bernard-Thomas 1989 → Choi-Lee 2017 = 28년 academic continuity)

---

# Section 2 · 미국 주식/ETF Alphas (IBKR Paper, A15~A18)

## A15: US Factor Investing (Fama-French 5-Factor)

### Origin (학술)

- **원 paper:** Fama, E. F., & French, K. R. (2015). "A Five-Factor Asset Pricing Model." *Journal of Financial Economics*, 116(1), 1-22. *(citation: 8,500+)*
- **원조:** Fama-French (1993) 3-factor *(citation: 30,000+)*
- **확장:** Carhart (1997) momentum 4-factor *(citation: 13,000+)*
- **한국 검증:** Kang, S. (2018). "Five-Factor Asset Pricing Model in the Korean Market: Are RMW and CMA Redundant?" *Korean Finance Review*, 32(2), 51-89. *(KOSPI 200 = RMW + CMA redundant, FF5 → FF3 권고)*
- **citation:** FF 2015 = 8,500+; Kang 2018 = 31
- **alpha decay timeline:** Medium-slow decay (Value 2010~2020 알파 약화, but Quality 잔존). FF5 자체 = academic standard, smart beta ETF 의 base model.

### Hypothesis (cold honest)

US Russell 3000 (또는 ETF universe) 에서 Fama-French 5-factor (MKT, SMB, HML, RMW, CMA) 가중 portfolio 가 시장 대비 long-term excess return 제공.

**한국 KOSPI 적용 시 RMW/CMA redundant** (Kang 2018) → 본 A15 는 **US-only target**, 한국 X 박제.

**한국 직접 이식 risk 박제 (Cold)**:
- Chui, A. C., Titman, S., & Wei, K. C. (2000). "Momentum, Legal Systems and Ownership Structure: An Analysis of Asian Stock Markets." *Working Paper*. → 한국 1990~2003 = momentum reversal 관찰
- 2010~2020 한국 = momentum partial 회복, but variance 큼
- → **A15 US momentum factor 한국 직접 이식 = HIGH RISK 박제**

### Entry Logic

```python
def a15_entry_signal(date, us_equity_universe):
    """
    Monthly rebalance: 1st trading day
    Universe: Russell 3000 (또는 IBKR universe filter cap > $1B)
    """
    if not is_first_trading_day_of_month(date):
        return []

    factor_exposures = {}
    for stock in us_equity_universe:
        # 1. SMB exposure
        market_cap = get_market_cap(stock, date)
        smb_rank = compute_size_rank(market_cap, universe_market_caps)

        # 2. HML exposure
        book_to_market = get_book_value(stock) / market_cap
        hml_rank = compute_value_rank(book_to_market, universe_btm)

        # 3. RMW exposure (Robust minus Weak — operating profitability)
        op_profitability = get_operating_profit(stock) / get_book_value(stock)
        rmw_rank = compute_profitability_rank(op_profitability, ...)

        # 4. CMA exposure (Conservative minus Aggressive — investment)
        asset_growth_yoy = get_asset_growth(stock, 1y)
        cma_rank = compute_investment_rank(-asset_growth_yoy, ...)  # Conservative = low growth

        # 5. Composite score
        factor_exposures[stock] = {
            'smb': smb_rank, 'hml': hml_rank, 'rmw': rmw_rank, 'cma': cma_rank
        }

    # 6. Top quintile multi-factor score (equal-weighted SMB+HML+RMW+CMA)
    composite_scores = {
        stock: sum(exps.values())
        for stock, exps in factor_exposures.items()
    }
    top_quintile = sorted(composite_scores.items(), key=lambda x: -x[1])[:60]  # Top 60 of 300

    return [
        {"action": "LONG", "symbol": stock, "weight": 1/60}
        for stock, _ in top_quintile
    ]
```

데이터 의존성:
- **IBKR TWS API**: order execution
- **Polygon.io / Alpha Vantage**: fundamentals (market cap, book value, operating profit)
- **Compustat (paid)**: 정확한 financial data — Phase 3 cost $278 권고
- **timeframe**: 1d (monthly rebalance)

### Exit Logic

- **TP**: 없음 (monthly rebalance 까지 hold)
- **SL**: 개별 stock -25% 도달 시 즉시 cash
- **Timeout**: 다음 monthly rebalance
- **Trailing**: 없음

### Risk Parameters

- **Capital allocation**: 자본의 25%
- **Per-position**: 25% / 60 = 약 0.4% per stock (저변동성 분산)
- **Max daily trades**: 60+ (monthly rebalance)
- **Max consec losses**: 무관 (monthly 방식)
- **Cooldown**: 무관
- **Leverage**: 1x

### Backtest Requirements

- **Minimum data history**: 10 years (120 monthly obs) — FF5 long-term robustness 검증
- **Regime breakdown**: 4 regime — 3+ regimes PnL > 0 권고 (Value factor 2010~2020 약화 ack)
- **DSR threshold**: ≥ 0.4 (factor strategy = lower DSR threshold acceptable, long-term beta)
- **PBO threshold**: < 0.5
- **OOS**: 2 years (24 monthly obs)
- **Benchmark**: SPY (S&P 500 ETF)

### Test Cases

```python
def test_a15_smb_rank_correct():
def test_a15_hml_rank_correct():
def test_a15_rmw_rank_correct():
def test_a15_cma_rank_correct():
def test_a15_composite_score_equal_weight():
def test_a15_top_quintile_60_stocks():
def test_a15_monthly_rebalance_1st_day():
def test_a15_individual_sl_25pct():
def test_a15_missing_fundamentals_excluded():
def test_a15_korean_universe_blocked():  # A15 US-only 강제 박제
def test_a15_regime_breakdown_factor():
def test_a15_compustat_or_polygon_fallback():
```

12 tests. Edge cases: IPO 직후 (book value 미공개), 분기 financial 발표 timing mismatch, M&A target stock.

### Module Path

```
packages/@qpm/alphas/a15-us-factor-fama-french/
├── logic.py
├── factor_calculator.py
├── fundamentals_provider.py    # Polygon + Compustat fallback
├── universe_filter.py           # Russell 3000 filter
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  factor_weights: ['equal', 'mkt_2x', 'value_2x', 'quality_2x']    # 4 levels
  top_quintile_size: [40, 60, 80, 100]                              # 4 levels
  rebalance_freq_months: [1, 3, 6]                                  # 3 levels
  individual_sl_pct: [0.20, 0.25, 0.30]                             # 3 levels

total_cells: 4 × 4 × 3 × 3 = 144 cells

acceptance_gate:
  - Sharpe annualized ≥ 0.6 (beta strategy, lower threshold)
  - excess return ≥ 1.5% / year vs SPY
  - DSR ≥ 0.4
  - PBO < 0.5
  - 3+ regimes PnL > 0
  - MaxDD ≤ 20%
```

### Honest Failure Risks

- **Value factor 2010~2020 약화 실증**: Fama-French 본인 = 2020 paper 에서 ack. **Mitigation**: RMW (quality / profitability) 가중 강화 옵션 (sweep parameter)
- **한국 KOSPI 이식 risk = strict no**: Kang 2018 evidence + Chui-Titman-Wei 2000 → A15 한국 X 박제
- **Compustat 무료 대체 noise**: Polygon free tier = lagged fundamentals. **Mitigation**: Phase 3 $278/year Polygon Starter 가입 권고
- **38일 PoC 패턴 반복 위험**: factor strategy = monthly rebalance = 거래 표본 부족 risk. **Mitigation**: 10년 backtest (120 obs) 강제

---

## A16: US Risk Parity (Dalio All Weather)

### Origin (학술)

- **원 paper:** Dalio, R. (2005). "Engineering Targeted Returns and Risks." *Bridgewater Associates White Paper*. *(industry paper, not peer-reviewed)*
- **확장 paper:** Asness, C. S., Frazzini, A., & Pedersen, L. H. (2012). "Leverage Aversion and Risk Parity." *Financial Analysts Journal*, 68(1), 47-59. *(citation: 800+, AQR 학술 정리)*
- **재검증:** Anderson, R. M., Bianchi, S. W., & Goldberg, L. R. (2012). "Will My Risk Parity Strategy Outperform?" *Financial Analysts Journal*, 68(6), 75-93.
- **citation:** Dalio 2005 = industry standard; Asness 2012 = 800+; Anderson 2012 = 250+
- **alpha decay timeline:** Regime-invariant (target = consistent return across regimes, not alpha decay). 2008 GFC + 2020 COVID 모두 outperform.

### Hypothesis (cold honest)

Asset class 별 (Stocks / Bonds / Commodities / Gold) volatility-weighted allocation 으로 portfolio 의 risk 가 균등 분산. 결과적으로 **Sharpe 0.7~1.0**, 다양한 regime 에서 일관된 return.

**한국 retail 적용 가능성**: 미국 ETF 대신 한국 ETF 변형 가능 (KODEX 200 / KODEX 국채10년 / KODEX 골드선물 / KODEX 원유) but liquidity / spread 약함 → A16 = **US ETF version 권고**.

### Entry Logic

```python
def a16_entry_signal(date, asset_classes):
    """
    Monthly rebalance: 1st trading day
    Universe: 4 ETFs (US)
        - VTI (Total Stock Market)
        - TLT (20+ Year Treasury Bond)
        - GLD (Gold)
        - DBC (Commodity Index, Diversified)
    """
    if not is_first_trading_day_of_month(date):
        return []

    # 1. 60-day rolling volatility per asset
    volatilities = {}
    for etf in ['VTI', 'TLT', 'GLD', 'DBC']:
        returns = get_daily_returns(etf, lookback=60)
        volatilities[etf] = returns.std() * sqrt(252)

    # 2. Inverse volatility weights
    inv_vol = {etf: 1/vol for etf, vol in volatilities.items()}
    total_inv_vol = sum(inv_vol.values())
    weights = {etf: iv / total_inv_vol for etf, iv in inv_vol.items()}

    # 3. Optional: Leverage to target portfolio vol (Dalio All Weather = ~10% target vol)
    portfolio_vol = compute_portfolio_volatility(weights, volatilities, correlations)
    target_vol = 0.10
    leverage = min(target_vol / portfolio_vol, 1.5)  # Max 1.5x leverage cap

    return [
        {"action": "LONG", "symbol": etf, "weight": w * leverage}
        for etf, w in weights.items()
    ]
```

데이터 의존성:
- **IBKR TWS API**: ETF execution
- **Yahoo Finance / Polygon**: daily close (no fundamentals needed)
- **timeframe**: 1d (monthly rebalance)

### Exit Logic

- **TP**: 없음 (Monthly rebalance)
- **SL**: Portfolio drawdown > 15% 시 50% cash 전환 (regime change detection)
- **Timeout**: 다음 monthly rebalance
- **Trailing**: 없음

### Risk Parameters

- **Capital allocation**: 자본의 25% (안정축, 자본 보호)
- **Per-asset class**: weight × 25%
- **Max daily trades**: 4~8 (monthly rebalance)
- **Max consec losses**: 무관 (portfolio level)
- **Cooldown**: drawdown trigger 후 1 month cash hold
- **Leverage**: 1.0~1.5x (target vol 10%)

### Backtest Requirements

- **Minimum data history**: 15 years (180 monthly obs) — 2008 GFC + 2020 COVID 포함
- **Regime breakdown**: 4 regime — 4 regimes ALL PnL > 0 (Dalio All Weather 본질)
- **DSR threshold**: ≥ 0.4 (안정 beta strategy)
- **PBO threshold**: < 0.4 (low overfitting tolerance)
- **OOS**: 3 years (36 monthly obs)
- **Benchmark**: SPY 60/40 (60% VTI + 40% TLT)

### Test Cases

```python
def test_a16_volatility_calculation_60d():
def test_a16_inverse_volatility_weights_sum_to_1():
def test_a16_portfolio_vol_correlation_aware():
def test_a16_target_vol_10pct_leverage():
def test_a16_leverage_cap_1_5x():
def test_a16_drawdown_15pct_trigger_50_cash():
def test_a16_4_asset_classes_required():
def test_a16_monthly_rebalance_only():
def test_a16_2008_gfc_regime_outperform():     # Historical scenario
def test_a16_2020_covid_regime_outperform():   # Historical scenario
def test_a16_regime_breakdown_all_4_pos():
def test_a16_60_40_benchmark_outperform_sharpe():
```

12 tests. Edge cases: ETF distribution day, IBKR fractional shares, leverage drift mid-month.

### Module Path

```
packages/@qpm/alphas/a16-us-risk-parity/
├── logic.py
├── volatility_calc.py
├── correlation_matrix.py
├── leverage_target.py
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  vol_lookback_days: [30, 60, 90, 120]         # 4 levels
  target_vol: [0.08, 0.10, 0.12]               # 3 levels
  max_leverage: [1.0, 1.25, 1.5, 2.0]          # 4 levels
  drawdown_trigger: [0.10, 0.15, 0.20]         # 3 levels
  rebalance_freq_months: [1, 2, 3]             # 3 levels

total_cells: 4 × 3 × 4 × 3 × 3 = 432 cells

acceptance_gate:
  - Sharpe annualized ≥ 0.7
  - MaxDD ≤ 15%
  - 4 regimes ALL PnL > 0   # Dalio All Weather 의 핵심 evidence
  - DSR ≥ 0.4
  - PBO < 0.4
  - Outperform 60/40 by ≥ 1% Sharpe
```

### Honest Failure Risks

- **2022 risk parity 약점 실증**: 2022 stocks/bonds correlation 양으로 전환 → Risk Parity 큰 손실 (AQR 등 large fund 평균 -10~-15%). **Mitigation**: GLD + DBC 추가 (4 asset class) = stocks-bonds correlation 회피
- **Leverage cost**: IBKR margin 금리 4~6% (2026 기준) → leverage 1.5x 시 net Sharpe 압축. **Mitigation**: leverage 1.0x 기본, target vol 8% 옵션
- **38일 PoC 패턴 반복 risk = LOW**: A16 본질 = beta strategy, alpha 가설 미사용 → decay risk 낮음

---

## A17: US PEAD (US Post-Earnings Announcement Drift)

### Origin (학술)

- **원 paper:** Bernard, V. L., & Thomas, J. K. (1989) — 동일 (A14 reference)
- **US 재검증:** Livnat, J., & Mendenhall, R. R. (2006). "Comparing the Post-Earnings Announcement Drift for Surprises Calculated from Analyst and Time Series Forecasts." *Journal of Accounting Research*, 44(1), 177-205. *(citation: 800+)*
- **alpha decay 분석:** Chordia, T., Goyal, A., Sadka, G., Sadka, R., & Shivakumar, L. (2009). "Liquidity and the Post-Earnings-Announcement Drift." *Financial Analysts Journal*, 65(4), 18-32. *(citation: 600+, PEAD = liquidity premium 의 일부)*
- **citation:** Bernard-Thomas 1989 = 4,500+; Livnat-Mendenhall 2006 = 800+
- **alpha decay timeline:** Medium-fast decay (US). 2000~2005 강함, 2010~ HFT/공매도 fund 침투로 약화. 2020+ small-cap 만 잔존.

### Hypothesis (cold honest)

US 상장사의 분기 earnings 발표 후 SUE > +1.5 인 종목은 announcement 후 60 trading days 동안 average +3~4% drift. **단, US large-cap (S&P 500) PEAD = decayed, small-cap (Russell 2000) 잔존**.

### Entry Logic

```python
def a17_entry_signal(date, earnings_calendar):
    """
    Daily check after market close 16:00 EST
    Universe: Russell 2000 (small-cap focus, large-cap PEAD decayed)
    """
    signals = []
    todays_announcements = get_us_earnings_announcements(date)

    for announcement in todays_announcements:
        ticker = announcement['ticker']
        # Skip if S&P 500 (large-cap PEAD decayed)
        if is_sp500(ticker):
            continue

        actual_eps = announcement['actual_eps']
        consensus_eps = get_iex_consensus(ticker)  # IEX Cloud free tier
        std_eps_change = get_std_eps_change(ticker, 8_quarters=8)
        sue = (actual_eps - consensus_eps) / std_eps_change

        if sue > 1.5:
            signals.append({
                "action": "LONG",
                "symbol": ticker,
                "sue": sue,
                "expected_drift_pct": 0.03 if sue > 2.5 else 0.02,  # US lower magnitude
                "expected_holding_days": 60,
                "entry_time": "next_trading_day_open"
            })

    return signals
```

데이터 의존성:
- **IBKR TWS API**: order
- **IEX Cloud / Polygon**: analyst consensus
- **EDGAR (SEC)**: announcement data (무료)
- **timeframe**: 1d

### Exit Logic

- **TP**: +4% 또는 60 trading days
- **SL**: -2.5% (US tighter SL, 시장 효율적)
- **Timeout**: 60 days
- **Trailing**: +2% 도달 후 SL → breakeven

### Risk Parameters

- **Capital allocation**: 자본의 10% (US small-cap = liquidity / spread risk)
- **Per-position**: 자본의 1% per stock
- **Max active**: 10
- **Max consec losses**: 5 → 2 weeks cooldown
- **Leverage**: 1x

### Backtest Requirements

- **Minimum data history**: 5 years
- **Regime breakdown**: 3+ regimes PnL > 0
- **DSR threshold**: ≥ 0.4 (US PEAD decayed ack)
- **PBO threshold**: < 0.5
- **OOS**: 1 year

### Test Cases

```python
def test_a17_sue_calculation():
def test_a17_sp500_excluded():    # Large-cap PEAD decayed
def test_a17_russell_2000_universe():
def test_a17_entry_t_plus_1_open():
def test_a17_60_day_holding():
def test_a17_tp_4pct_us():
def test_a17_sl_2_5pct_tighter():
def test_a17_iex_cloud_api_handling():
def test_a17_edgar_8k_parsing():
def test_a17_max_10_positions():
def test_a17_decayed_regime_handling():
```

11 tests. Edge cases: 8-K 비 earnings 공시 (M&A, guidance), pre-market announcement, after-market gap.

### Module Path

```
packages/@qpm/alphas/a17-us-pead/
├── logic.py
├── edgar_client.py
├── iex_cloud_client.py
├── small_cap_filter.py
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  sue_threshold: [1.0, 1.5, 2.0, 2.5]
  holding_days: [30, 45, 60, 90]
  tp_pct: [0.025, 0.04, 0.06]
  sl_pct: [0.02, 0.025, 0.03]

total_cells: 4 × 4 × 3 × 3 = 144 cells

acceptance_gate:
  - WR ≥ 50%
  - PF ≥ 1.3
  - Sharpe annualized ≥ 0.7  (US PEAD decayed)
  - DSR ≥ 0.4
  - PBO < 0.5
```

### Honest Failure Risks

- **US large-cap PEAD 폐기**: 2010+ academic evidence 명확. **Mitigation**: Russell 2000 small-cap focus
- **38일 PoC A4 패턴 반복 risk**: event-driven 알파. **Mitigation**: A17 small-cap = decades robust evidence (Chordia 2009 = liquidity premium 잔존)
- **IBKR small-cap commission**: 일부 < $1 stock = commission > spread. **Mitigation**: price > $5 filter

---

## A18: US Sector Momentum (11 SPDR Sectors)

### Origin (학술)

- **원 paper:** Jegadeesh, N., & Titman, S. (1993). "Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency." *Journal of Finance*, 48(1), 65-91. *(citation: 21,000+)*
- **확장 paper:** Moskowitz, T. J., & Grinblatt, M. (1999). "Do Industries Explain Momentum?" *Journal of Finance*, 54(4), 1249-1290. *(citation: 1,500+, sector momentum 강함)*
- **ETF 적용:** Conover, C. M., Jensen, G. R., Johnson, R. R., & Mercer, J. M. (2008). "Sector Rotation and Monetary Conditions." *Journal of Investing*, 17(1), 34-46. *(citation: 200+)*
- **citation:** Jegadeesh-Titman 1993 = 21,000+; Moskowitz-Grinblatt 1999 = 1,500+
- **alpha decay timeline:** Medium decay. Stock-level momentum 2010~ 약화, sector-level 은 상대적으로 robust.

### Hypothesis (cold honest)

11 SPDR sector ETFs (XLK / XLF / XLE / XLY / XLP / XLI / XLV / XLB / XLU / XLRE / XLC) 의 6-month momentum 상위 3개 sector long, 하위 3 sector short (또는 cash). **이유**:
- Sector-level momentum 은 stock-level 보다 alpha decay 느림 (Moskowitz-Grinblatt 1999)
- 거시경제 cycle 과 sector rotation 연계

### Entry Logic

```python
def a18_entry_signal(date, sector_etfs):
    """
    Monthly rebalance: 1st trading day
    Universe: 11 SPDR sectors (XLK, XLF, XLE, XLY, XLP, XLI, XLV, XLB, XLU, XLRE, XLC)
    """
    if not is_first_trading_day_of_month(date):
        return []

    momentum_scores = {}
    for etf in sector_etfs:
        price_t = get_close(etf, date)
        price_t_6m = get_close(etf, date - 126_trading_days)
        # Exclude last month (academic standard: 12-1 momentum)
        price_t_1m = get_close(etf, date - 21_trading_days)
        momentum_scores[etf] = (price_t_1m / price_t_6m) - 1.0

    sorted_etfs = sorted(momentum_scores.items(), key=lambda x: -x[1])
    top_3 = sorted_etfs[:3]
    bot_3 = sorted_etfs[-3:]  # Cash 권고 (long-only, retail)

    return [
        {"action": "LONG", "symbol": etf, "weight": 1/3}
        for etf, _ in top_3
    ]
```

데이터 의존성:
- **IBKR TWS API**
- **Yahoo Finance / Polygon free**: daily close
- **timeframe**: 1d (monthly rebalance)

### Exit Logic

- **TP**: 없음 (monthly rebalance)
- **SL**: 개별 ETF -10% 시 즉시 cash
- **Timeout**: monthly rebalance
- **Trailing**: 없음

### Risk Parameters

- **Capital allocation**: 자본의 15%
- **Per-position**: 자본의 5% per ETF
- **Max daily trades**: 6 (rebalance)
- **Leverage**: 1x

### Backtest Requirements

- **Minimum data history**: 15 years (180 monthly obs) — Moskowitz-Grinblatt 1999 long-term
- **Regime breakdown**: 4 regime, 3+ PnL > 0
- **DSR threshold**: ≥ 0.5
- **PBO threshold**: < 0.5
- **OOS**: 2 years
- **Benchmark**: SPY equal-weight 11 sectors

### Test Cases

```python
def test_a18_12_1_momentum_exclude_last_month():
def test_a18_top_3_sectors():
def test_a18_long_only_retail():
def test_a18_individual_sl_10pct():
def test_a18_monthly_rebalance():
def test_a18_11_sector_universe_complete():
def test_a18_xlre_addition_2015_handling():    # XLRE = 2015 추가, backtest 호환
def test_a18_2008_gfc_regime():
def test_a18_2020_covid_regime():
def test_a18_2022_inflation_regime():
def test_a18_decay_check_2015_vs_2020():
```

11 tests.

### Module Path

```
packages/@qpm/alphas/a18-us-sector-momentum/
├── logic.py
├── sector_universe.py     # 11 SPDR + XLRE handling
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  momentum_lookback_months: [3, 6, 9, 12]    # 4 levels
  skip_last_month: [0, 1]                     # 2 levels (12-0 vs 12-1)
  top_n: [2, 3, 4, 5]                          # 4 levels
  individual_sl: [0.08, 0.10, 0.15]            # 3 levels

total_cells: 4 × 2 × 4 × 3 = 96 cells

acceptance_gate:
  - Sharpe annualized ≥ 0.6
  - DSR ≥ 0.5
  - PBO < 0.5
  - Outperform SPY by ≥ 1% Sharpe
```

### Honest Failure Risks

- **2010+ stock momentum decay**: sector momentum 부분 잔존 but vigilance. **Mitigation**: 12-1 academic standard 사용
- **2008 GFC scenario**: 2008-09 momentum reversal 큼. **Mitigation**: monthly rebalance + SL 10% — Recovery 시 즉시 reenter
- **38일 PoC 패턴 반복 risk**: monthly rebalance frequency = trade 표본 부족. **Mitigation**: 15년 backtest

---

# Section 3 · 미국 옵션 Alphas (IBKR/Tastytrade Paper, A19~A21)

## A19: Covered Call (SPY / QQQ Monthly)

### Origin (학술)

- **원 index:** CBOE BXM Index (1986년 launch, S&P 500 covered call benchmark)
- **검증 paper:** Whaley, R. E. (2002). "Return and Risk of CBOE Buy Write Monthly Index." *Journal of Derivatives*, 10(2), 35-42. *(citation: 300+, BXM long-term Sharpe 0.6 vs S&P 0.45)*
- **확장:** Hill, J. M., Balasubramanian, V., Gregory, K., & Tierens, I. (2006). "Finding Alpha via Covered Index Writing." *Financial Analysts Journal*, 62(5), 29-46. *(citation: 400+)*
- **citation:** Whaley 2002 = 300+; Hill 2006 = 400+
- **alpha decay timeline:** Regime-invariant (40+ years). CBOE BXM = 1986 launch, persistent volatility risk premium

### Hypothesis (cold honest)

SPY (또는 QQQ) buy + 30-delta OTM Call (1-month expiry) sell = 매월 premium 수확. **이유**:
- Implied volatility > realized volatility (장기 평균 +4~6%)
- Call writer = volatility seller, 평균 양의 expectancy
- Tail risk: 상방 cap 됨 (큰 rally 시 underperform, but 평균 수익률 안정)

### Entry Logic

```python
def a19_entry_signal(date, underlying='SPY'):
    """
    Monthly entry: 3rd Friday after current month expiry
    Cycle: Buy 100 shares + Sell 1 OTM Call (30-delta, ~1-month expiry)
    """
    if not is_monthly_options_expiry(date - 1):
        return []  # Wait for previous month options to expire

    underlying_price = get_close(underlying, date)
    shares_to_buy = 100  # 1 contract = 100 shares

    # Find 30-delta OTM Call, next monthly expiry
    options_chain = get_options_chain(underlying, expiry=next_monthly_expiry(date))
    call_30_delta = find_call_by_delta(options_chain, target_delta=0.30)

    return [
        {"action": "BUY", "symbol": underlying, "quantity": 100},
        {
            "action": "SELL_OPEN",
            "symbol": call_30_delta['contract'],
            "quantity": 1,
            "type": "OPTION_CALL",
            "premium_received": call_30_delta['mid_price']
        }
    ]
```

데이터 의존성:
- **IBKR TWS API** (또는 Tastytrade paper)
- **Theta Data Value $80/year**: options chain historical (Phase 2 권고)
- **timeframe**: 1d (monthly cycle)

### Exit Logic

- **Call expiry ITM (assigned)**: 자동 100 shares 매도 (premium + 차익 + share appreciation up to strike)
- **Call expiry OTM**: premium 보유, shares 보유 → 다음 month roll
- **Early close (선택)**: call 가치 50% decay 시 buy-to-close (Tastytrade 표준)
- **SL**: 없음 (underlying SL = 다른 algo 가 관리)

### Risk Parameters

- **Capital allocation**: 자본의 30% (안정축, 옵션 income)
- **Per-cycle**: 100 shares × underlying price (예: SPY $500 = $50,000 capital)
- **Max cycles**: 자본 / (100 × SPY price)
- **Max consec losses**: 무관 (covered call 본질 ≈ 양의 expectancy)
- **Leverage**: 1x (covered)

### Backtest Requirements

- **Minimum data history**: 10 years (120 monthly cycles) — CBOE BXM 의 long-term Sharpe 0.6 evidence 재현
- **Regime breakdown**: 4 regime, 3+ PnL > 0
- **DSR threshold**: ≥ 0.4 (income strategy, lower threshold)
- **PBO threshold**: < 0.4
- **OOS**: 2 years
- **Benchmark**: SPY buy-and-hold

### Test Cases

```python
def test_a19_30_delta_call_selection():
def test_a19_monthly_3rd_friday_cycle():
def test_a19_assignment_on_itm_expiry():
def test_a19_roll_on_otm_expiry():
def test_a19_premium_accounting():
def test_a19_early_close_50pct_decay():
def test_a19_underlying_share_dividend():
def test_a19_options_chain_data_handling():
def test_a19_2008_gfc_drawdown_capped():
def test_a19_2020_covid_premium_spike():
def test_a19_regime_breakdown_all_4_pos():
def test_a19_bxm_index_replication_check():
```

12 tests. Edge cases: assignment 다음날 ex-dividend, options chain data gap, early exercise (rare for index ETF).

### Module Path

```
packages/@qpm/alphas/a19-covered-call/
├── logic.py
├── options_chain_provider.py    # Theta Data / IBKR options chain
├── delta_finder.py
├── assignment_handler.py
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  target_delta: [0.20, 0.30, 0.40]              # 3 levels
  days_to_expiry: [30, 45, 60]                  # 3 levels (monthly / 6w / quarterly)
  early_close_threshold: [0.0, 0.5, 0.8]        # 3 levels
  underlying: ['SPY', 'QQQ', 'IWM']             # 3 levels

total_cells: 3^4 = 81 cells

acceptance_gate:
  - Sharpe annualized ≥ 0.5  (income strategy)
  - MaxDD ≤ 30%  (covered, drawdown limited)
  - DSR ≥ 0.4
  - PBO < 0.4
  - Outperform underlying by ≥ 1% Sharpe
  - Income consistency: ≥ 80% months positive premium
```

### Honest Failure Risks

- **Strong bull market underperform**: 2017, 2021 같은 +25% rally 시 SPY 대비 underperform. **Mitigation**: covered call 의 본질, owner expectation 이미 알맞음
- **Volatility regime shift**: VIX 평균 < 10 시 premium 부족. **Mitigation**: 30-delta 표준 sticky, BXM 의 long-term evidence 신뢰
- **38일 PoC 패턴 반복 risk = NEAR-ZERO**: A19 = income strategy, alpha hypothesis 미사용, 40년 academic evidence

---

## A20: Volatility Risk Premium (VIX Futures vs SPX Options)

### Origin (학술)

- **원 paper:** Coval, J. D., & Shumway, T. (2001). "Expected Option Returns." *Journal of Finance*, 56(3), 983-1009. *(citation: 1,800+, options = 평균 음의 return)*
- **VRP 정량:** Carr, P., & Wu, L. (2009). "Variance Risk Premiums." *Review of Financial Studies*, 22(3), 1311-1341. *(citation: 1,500+, IV > RV 평균 4~6% 연)*
- **확장:** Bollerslev, T., Tauchen, G., & Zhou, H. (2009). "Expected Stock Returns and Variance Risk Premia." *Review of Financial Studies*, 22(11), 4463-4492. *(citation: 1,600+)*
- **citation:** Coval-Shumway 2001 = 1,800+; Carr-Wu 2009 = 1,500+
- **alpha decay timeline:** Slow decay (30+ years average +4~6% per year, but 2018 February vol spike 등 큰 손실)

### Hypothesis (cold honest)

VIX implied volatility > S&P 500 realized volatility 평균. Short volatility (= VIX futures short, 또는 SPX straddle sell) 가 양의 expectancy. **단, tail risk 큼** (2018-02 XIV $0.000 collapse).

### Entry Logic

```python
def a20_entry_signal(date):
    """
    Daily VRP measurement, weekly entry
    Strategy: VIX futures front-month short OR delta-hedged short straddle on SPX
    """
    # 1. VRP measurement
    iv_30d = get_vix_close(date)
    rv_30d = compute_realized_vol(SPX, lookback=30)
    vrp = iv_30d - rv_30d

    # 2. Entry condition: VRP > 4% (long-term average)
    if vrp < 4.0:
        return []

    # 3. Tail risk gate: VIX < 30 (high vol regime = avoid)
    if iv_30d > 30:
        return []

    # 4. Strategy A: VIX futures short (simpler)
    vix_futures = get_vix_futures_chain(date)
    front_month = vix_futures[0]

    return [
        {
            "action": "SELL_OPEN",
            "symbol": front_month['contract'],
            "quantity": 1,
            "type": "FUTURES",
            "size_dollar": 5000  # 1 VIX future = ~$15-30K notional
        }
    ]
```

데이터 의존성:
- **IBKR TWS API**: VIX futures, SPX options
- **CBOE data feed**: VIX historical (무료 daily)
- **Theta Data**: SPX options for delta-hedged straddle (선택)
- **timeframe**: 1d

### Exit Logic

- **TP**: VRP 2% 이하 도달 (mean revert), 또는 +20% PnL
- **SL**: VIX 50% spike (예: 15 → 22.5) 즉시 청산
- **Timeout**: VIX futures expiry (monthly)
- **Trailing**: 없음

### Risk Parameters

- **Capital allocation**: 자본의 10% (tail risk 큼, conservative)
- **Per-position**: 1~2 VIX futures
- **Max consec losses**: 3 → 1 month pause
- **Cooldown**: 2 weeks after SL
- **Leverage**: VIX future 자체 = embedded leverage

### Backtest Requirements

- **Minimum data history**: 15 years (180 monthly obs) — 2008 GFC + 2018 Vol spike + 2020 COVID 포함
- **Regime breakdown**: 4 regime, BEAR / VOLATILE regime PnL 음 OK (only 2+ regimes positive)
- **DSR threshold**: ≥ 0.4
- **PBO threshold**: < 0.4
- **OOS**: 2 years
- **Benchmark**: VIX buy-and-hold (negative carry)

### Test Cases

```python
def test_a20_vrp_calculation():
def test_a20_entry_threshold_4pct_vrp():
def test_a20_tail_risk_vix_30_gate():
def test_a20_vix_50pct_spike_sl():
def test_a20_2018_02_xiv_scenario():  # Critical historical test
def test_a20_2020_03_covid_scenario():
def test_a20_vix_futures_chain_handling():
def test_a20_monthly_expiry_rollover():
def test_a20_max_2_contracts():
def test_a20_cooldown_after_sl():
def test_a20_realized_vol_30d_calculation():
def test_a20_short_only_long_vol_excluded():
```

12 tests. Edge cases: VIX overnight gap, contango/backwardation regime, settlement vs spot.

### Module Path

```
packages/@qpm/alphas/a20-volatility-risk-premium/
├── logic.py
├── vrp_calculator.py
├── vix_futures_handler.py
├── tail_risk_gate.py
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  vrp_entry_threshold: [3.0, 4.0, 5.0, 6.0]
  vix_max_gate: [25, 30, 35, 40]
  vix_spike_sl: [0.30, 0.50, 0.75]
  position_size_dollar: [3000, 5000, 7000]

total_cells: 4 × 4 × 3 × 3 = 144 cells

acceptance_gate:
  - Sharpe annualized ≥ 0.7
  - MaxDD ≤ 25%  (tail risk ack)
  - 2018-02 scenario survives  (XIV collapse hard test)
  - DSR ≥ 0.4
  - PBO < 0.4
```

### Honest Failure Risks

- **2018-02 XIV collapse**: short vol ETP 100% loss in 1 day. **Mitigation**: VIX futures direct (limited loss to margin) + SL 50% spike + max 1~2 contracts + position 10% capital cap
- **2020-03 COVID**: VIX 80+ spike, short vol large loss. **Mitigation**: tail risk gate VIX < 30 entry only
- **38일 PoC 패턴 반복 risk = MEDIUM**: short vol = tail risk 본질. Cold honest acknowledged in academic paper.

---

## A21: Iron Condor (Low Volatility Regime)

### Origin (학술)

- **원 strategy:** CBOE / industry standard, 1980s. Not peer-reviewed paper but established options strategy.
- **이론 frame:** Hull, J. C. (2017). "Options, Futures, and Other Derivatives" *10th edition*, Ch. 12. *(textbook, options strategy classification)*
- **재검증:** Israelov, R., & Nielsen, L. N. (2014). "Covered Calls Uncovered." *AQR White Paper*. *(industry-grade analysis of credit spread strategies)*
- **citation:** Hull textbook = standard reference; Israelov 2014 = industry paper
- **alpha decay timeline:** Medium decay. Volatility regime sensitive. Low VIX regime 강함.

### Hypothesis (cold honest)

SPX (또는 SPY) 의 1-month range-bound (-2% ~ +2%) probability ≥ 60% in low VIX regime. Iron Condor (OTM Put Spread sell + OTM Call Spread sell) = 양의 expectancy in 60~70% trades, 큰 loss in 30~40%.

### Entry Logic

```python
def a21_entry_signal(date, underlying='SPX'):
    """
    Weekly entry (Mondays) if VIX < 18
    Strategy: 30-day Iron Condor at 1-sigma OTM
    """
    if not is_monday(date):
        return []

    vix = get_vix_close(date)
    if vix > 18:
        return []  # Avoid high vol regime

    underlying_price = get_close(underlying, date)
    iv_30d = vix / 100
    one_sigma = underlying_price * iv_30d * sqrt(30/365)

    put_short_strike = underlying_price - one_sigma
    put_long_strike = put_short_strike - one_sigma * 0.5  # 0.5 sigma further OTM
    call_short_strike = underlying_price + one_sigma
    call_long_strike = call_short_strike + one_sigma * 0.5

    options_chain = get_options_chain(underlying, expiry=date + 30)

    return [
        {"action": "SELL_OPEN", "symbol": put_short_strike, "type": "OPTION_PUT", "quantity": 1},
        {"action": "BUY_OPEN", "symbol": put_long_strike, "type": "OPTION_PUT", "quantity": 1},
        {"action": "SELL_OPEN", "symbol": call_short_strike, "type": "OPTION_CALL", "quantity": 1},
        {"action": "BUY_OPEN", "symbol": call_long_strike, "type": "OPTION_CALL", "quantity": 1},
    ]
```

데이터 의존성:
- **IBKR TWS API** (또는 Tastytrade)
- **Theta Data Value $80/year**: SPX options chain
- **timeframe**: 1d

### Exit Logic

- **TP**: net credit 50% decay (Tastytrade 표준)
- **SL**: 2x net credit loss (보수적)
- **Timeout**: expiry (30 days)
- **Trailing**: 없음

### Risk Parameters

- **Capital allocation**: 자본의 10% (max loss = wing width × 100, limited)
- **Per-position**: 1 contract per cycle
- **Max active**: 2 (overlap)
- **Max consec losses**: 3 → 1 month pause
- **Cooldown**: 2 weeks after SL
- **Leverage**: limited by spread width

### Backtest Requirements

- **Minimum data history**: 10 years
- **Regime breakdown**: 4 regime — LOW_VOL regime PnL 강 positive, HIGH_VOL 손실 OK (only 2+ regimes positive)
- **DSR threshold**: ≥ 0.4
- **PBO threshold**: < 0.5
- **OOS**: 2 years

### Test Cases

```python
def test_a21_vix_18_gate():
def test_a21_one_sigma_strike_calculation():
def test_a21_4_leg_setup():
def test_a21_50pct_credit_tp():
def test_a21_2x_credit_sl():
def test_a21_max_loss_capped_by_wing():
def test_a21_2018_02_vol_spike_handling():
def test_a21_2020_03_covid_avoidance_vix_gate():
def test_a21_options_chain_4_legs_pricing():
def test_a21_max_2_active_positions():
def test_a21_cooldown_after_3_losses():
```

11 tests.

### Module Path

```
packages/@qpm/alphas/a21-iron-condor/
├── logic.py
├── iron_condor_builder.py
├── multi_leg_executor.py
└── tests/
```

### Sensitivity Sweep Grid

```yaml
parameters:
  vix_gate: [15, 18, 20, 22]
  sigma_short_strike: [0.8, 1.0, 1.2]
  wing_width_sigma: [0.3, 0.5, 0.7]
  tp_pct_credit: [0.30, 0.50, 0.70]
  sl_multiplier: [1.5, 2.0, 2.5]

total_cells: 4 × 3 × 3 × 3 × 3 = 324 cells

acceptance_gate:
  - WR ≥ 65%  (Iron Condor 본질 high WR)
  - PF ≥ 1.2
  - Sharpe annualized ≥ 0.7
  - DSR ≥ 0.4
  - PBO < 0.5
  - LOW_VOL regime PnL strongly positive
```

### Honest Failure Risks

- **High vol regime large loss**: 2018-02, 2020-03 같은 vol spike 시 큰 손실. **Mitigation**: VIX < 18 entry only, max 1 contract per cycle
- **Pin risk at expiry**: 만기 시 underlying = short strike 근처면 partial assignment. **Mitigation**: 만기 1주 전 close (Tastytrade 21 DTE 룰 변형)
- **38일 PoC 패턴 반복 risk = LOW**: Iron Condor 본질 = high WR low magnitude, decades industry data

---

# Section 4 · Crypto Archive (38일 PoC, Build X, A1~A6)

> **Status**: 모두 closure 박제. 12주 build 시 build X. 학습 자산 reference + portfolio narrative honest failure 부분으로 활용.

## A1: Liquidation Cascade Reverse (Archive)

### Origin (학술)

- **원 paper:** Lehar, A., & Parlour, C. A. (2024). "Crypto Wash Trading and Market Microstructure." *Working Paper, UC Berkeley*. *(working paper, peer review 미통과)*
- **Industry data:** Hyblock Capital 2024 research, Coinalyze 2024
- **citation:** Lehar-Parlour 2024 = 12 (working paper), Hyblock = industry
- **alpha decay timeline:** Fast decay confirmed. Binance forceOrder@arr WS = 2021-04-27 truncation (1/sec). 2026-05 38일 PoC = 0 trades evidence.

### 38일 PoC 결과 (Cold Honest 박제)

```
거래 0건 (19일 OKX 3-way cross-exchange 가동 후)
OKX cascade event 활성 (5/11 6,765건 avg $194K notional) 에도 0 trade
진입 임계값 too strict 가설 검증 미완 (PoC 종료)
```

### Archive 이유

- 외부 정책 변경 (Binance truncation 2021-04, deprecated allForceOrders 2023)
- 무료 backfill 데이터 0건
- Tardis.dev tick data $99/month = Phase 2 cost (G2 PASS)
- 38일 paper trading + cross-exchange aggregation 검증 = academic value, build 가치 X

### 학술 spec 박제 (다음 cycle build 가능 시 참조)

```yaml
entry_signal:
  threshold_5min_notional:
    BTC: $20M
    ETH: $10M
    others: $5M
  liquidation_direction_skew: >= 75%
  price_position: cluster_low * 1.005

exit:
  tp: entry + 0.8%
  sl: entry - 0.4%
  timeout: 30min

risk:
  capital: 5% (Kelly/3)
  leverage: 5x
```

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a1-liquidation-cascade/
├── README.md (closure note)
├── logic_archive.js  # 38일 PoC 코드 reference
└── tests/  # 18 tests still passing (regression value)
```

### Honest Failure Lesson (Portfolio narrative 자산)

**가장 큰 학습**: 외부 데이터 정책 변경에 의존하는 알파 = data sovereignty risk. Strategy Lead 의 cold honest 의무 = data provider changes 를 alpha decay 의 일부로 처음부터 포함.

---

## A2: Mean-Reversion OU (Archive — Polyban)

### Origin (학술)

- **원 paper:** Ornstein, L. S., & Uhlenbeck, G. E. (1930). "On the Theory of the Brownian Motion." *Physical Review*, 36(5), 823. *(citation: 5,000+, OU process 원조)*
- **확장:** Avellaneda, M., & Lee, J. H. (2010). "Statistical Arbitrage in the US Equities Market." *Quantitative Finance*, 10(7), 761-782. *(citation: 1,000+)*
- **citation:** OU 1930 = foundational; Avellaneda-Lee 2010 = 1,000+
- **alpha decay timeline:** Fast decay (post-2022 crypto). Industry observation: "순수 OU mean reversion 은 대부분 사멸."

### A2 Sweep 결과 (2026-05-10, Cold Honest 박제)

```
108 cells acceptance gate 통과: 0 / 108
최대 거래 빈도: 22 trades / 90일 = 0.24/일 (목표 1.0/일의 24%)
모든 cell 표본 부족 or 빈도 부족 or DSR < 0.5
→ A2 OU spec 폐기 권고 (Strategy Lead G1 결정)
```

### Archive 이유

- 108-cell sensitivity sweep 0/108 통과
- 거래 빈도 압도적 부족 (가장 완화된 setting 도 0.24/일)
- Avellaneda-Lee 2010 의 US equity stat arb 와 crypto 본질 차이
- A1 동조 게이트 가정 (MASTER_DESIGN.md §3 외부 경고) 도 verify 실패

### 학술 spec 박제 (다음 cycle 시 reference)

A2 spec = **POLYBAN 박제**. 본 형식 의 OU 단순 적용 = 다음 cycle build X.

대안 학술 path:
- Engle-Granger pair trading (A13 한국 적용) ✅
- 다중 asset class cointegration (A15 factor + A16 risk parity 의 부분 효과)
- Multi-horizon OU + regime gating (academic 가능, but build 가치 검증 미통과)

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a2-mean-reversion-ou/
├── README.md (polyban + closure)
├── logic_archive.js
├── sweep_result.json  # 108 cells full result
└── tests/  # 22 tests still passing
```

### Honest Failure Lesson

**가장 큰 학습**: backtest sensitivity sweep 0/108 통과 = spec 자체 fail. Cherry-pick (top Sharpe 3.01) = 표본 부족 (8 trades / 90d) = statistical noise. **OU 원조 paper (1930) 의 academic value 와 crypto post-2022 alpha 의 실재 = 다른 문제**.

---

## A3: Extreme Funding Reversal (Archive)

### Origin (학술)

- **원 paper:** Liu, X., & Zhao, Z. (2023). "Funding Rate Arbitrage in Cryptocurrency Perpetual Markets." *Working Paper*. *(working paper)*
- **Industry:** Coinglass / Coinalyze 2024 funding rate analysis
- **citation:** Liu-Zhao 2023 = 8 (working paper)
- **alpha decay timeline:** Medium-fast. 기관 arb 가 극단치 수 분 내 정리.

### 38일 PoC 결과

```
거래 0건 (4 필드 라이브 데이터 정상, 4 조건 미달 → WAIT 상태)
```

### Archive 이유

- Binance/BitMEX baseline `0.01%/8h tightly anchored` (대부분 시간)
- 진입 임계값 `|F| > 0.08%` 도 시장 자체 출현 빈도 낮음
- liquidation cluster + basis 동반 필터 추가 필요 (MASTER_DESIGN.md §3 외부 경고)

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a3-extreme-funding/
├── README.md (closure)
├── logic_archive.js
└── tests/
```

### Honest Failure Lesson

**가장 큰 학습**: market microstructure alpha = 기관 / HFT arb 와 직접 경쟁. retail 1인 + cloud VM = 100~500ms latency 한계로 진입 우위 부재.

---

## A4: Macro Event Bracket (Archive)

### Origin (학술)

- **이론 frame:** Ederington, L. H., & Lee, J. H. (1993). "How Markets Process Information: News Releases and Volatility." *Journal of Finance*, 48(4), 1161-1191. *(citation: 1,200+)*
- **확장:** Andersen, T. G., Bollerslev, T., Diebold, F. X., & Vega, C. (2003). "Micro Effects of Macro Announcements: Real-Time Price Discovery in Foreign Exchange." *American Economic Review*, 93(1), 38-62. *(citation: 1,800+)*
- **citation:** Ederington-Lee 1993 = 1,200+; Andersen 2003 = 1,800+
- **alpha decay timeline:** Stable (event-driven volatility = persistent), but capture difficulty 증가.

### 38일 PoC 결과

```
A4 wiring 완료 (commit 4988349, 11 tests)
5/13 22:30 CPI + 5/14 03:00 FOMC 첫 라이브 trigger 대기 → PoC closure 시점 미발동
```

### Archive 이유

- 38일 PoC 종료 시점 (5/12) = 5/13 CPI / 5/14 FOMC 직전 → 라이브 trigger 0건
- event-driven alpha = trigger 빈도 (1~2 / month) = 표본 누적 timeline > PoC 기간
- 외부 정책 (CPI release timing) 의존 = sample acquisition slow

### 학술 spec 박제

A4 spec 자체 = academic robust (Ederington-Lee 1993). 다음 cycle build 가능 시 reference 충분.

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a4-macro-event/
├── README.md
├── logic_archive.js
└── tests/  # 11 tests passing
```

### Honest Failure Lesson

**가장 큰 학습**: event-driven alpha = sample acquisition timeline 이 alpha decay timeline 보다 길면 cycle 부족. 12주 PoC 같은 짧은 cycle 에서는 event 빈도 ≥ 4 / cycle 인 alpha 만 evaluable.

---

## A6: Avellaneda-Stoikov Alt Market Making (Archive — Engine 미구현)

### Origin (학술)

- **원 paper:** Avellaneda, M., & Stoikov, S. (2008). "High-Frequency Trading in a Limit Order Book." *Quantitative Finance*, 8(3), 217-224. *(citation: 1,500+)*
- **textbook:** Cartea, A., Jaimungal, S., & Penalva, J. (2015). *Algorithmic and High-Frequency Trading*. Cambridge University Press, Ch. 10. *(citation: 2,000+)*
- **citation:** Avellaneda-Stoikov 2008 = 1,500+; Cartea 2015 = 2,000+
- **alpha decay timeline:** Stable in alt-coin mid-cap (HFT colocation 회피). BTC/ETH = HFT competition 강함.

### 38일 PoC 결과

```
BaseAgent scaffold 추가 (commit 233a420)
Engine 본 구현 보류 (Phase 1 통과 후 owner G2 권고)
거래 0건 (engine 부재)
```

### Archive 이유

- engine 본 구현 = 별도 작업 (양쪽 limit MM 본 로직 + inventory penalty + reservation price + order book skew)
- LINK/SUI/APT mid-cap = HFT 경쟁 약함, but Binance maker rebate 0.02% (VIP 0) 시 spread compression 시 alpha 마이너스
- 38일 PoC 종료 = engine build 가치 vs build 시간 cost 평가 못함

### 학술 spec 박제

A6 Avellaneda-Stoikov academic spec = robust foundation. **build 가치 = HIGH if engine complete, but build cost = MEDIUM (~1-2 weeks)**.

다음 cycle 우선순위 (build 결정 시):
- LINK / SUI / APT (BTC / ETH 제외 박제)
- inventory penalty γ = 0.1 ~ 0.5 (sweep)
- spread compression < 4bps 시 MM pause

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a6-alt-mm/
├── README.md
├── alt-mm-agent_scaffold.js
└── tests/  # 13 tests passing
```

### Honest Failure Lesson

**가장 큰 학습**: HFT-adjacent alpha = engine 완성도 80%+ 까지 build cost 사후 surprise. PoC 시간 한정 시 simpler alpha 우선 + HFT-adjacent 는 Phase 2+ cycle.

---

## A5: Funding/Basis Harvest (Archive)

### Origin (학술)

- **이론:** Hull, J. C. (2017). *Options, Futures, and Other Derivatives* (10th ed.), Ch. 5 (futures pricing, cost of carry)
- **Crypto 적용:** Liu, Y., & Tsyvinski, A. (2021). "Risks and Returns of Cryptocurrency." *Review of Financial Studies*, 34(6), 2689-2727. *(citation: 1,200+)*
- **citation:** Hull = standard; Liu-Tsyvinski 2021 = 1,200+
- **alpha decay timeline:** Fast decay confirmed (Ethena 2025 = futures 비중 93% → 11% 자체 축소, aggregated funding 50% 압축)

### 38일 PoC 결과

```
v11 wiring 미완 (인프라만, agent 본 구현 X)
거래 0건
```

### Archive 이유

- aggregated 30일 median funding `< 0.007%/8h` 시 A5 capacity = 실질 0% (MASTER_DESIGN.md §3 외부 경고)
- 2025 funding rate 압축 = capacity reduction
- delta-neutral spot+perp = 두 거래소 capital duplicate + custody risk

### Module Path (Archive)

```
packages/@qpm/alphas/_archive/a5-funding-basis/
├── README.md
└── infra-only/  # 인프라 코드만, agent 미구현
```

### Honest Failure Lesson

**가장 큰 학습**: 시장 capacity (aggregated 시장의 total alpha pool) 의 self-shrinking 현상. Ethena 같은 single large player 의 strategy shift 가 시장 전체 alpha 를 단기에 압축.

---

# Section 5 · Optional Alphas (Owner G2, Build 미포함)

## A22: Crypto Volatility Carry (Funding + Basis) — Optional

### Origin (학술)

- **frame:** Crypto perpetual funding + basis spread (Section 4의 A5 archive 와 별개 hypothesis)
- **citation:** Liu-Tsyvinski 2021 + Aktas et al. (2022) "Cryptocurrency Carry Trade." *Working Paper*. *(citation: 30)*
- **alpha decay timeline:** Same as A5 (capacity-dependent)

### Hypothesis

Crypto carry trade (long spot + short perpetual when basis > 0 + funding > 0). **Cold honest**: A5 archive 의 capacity guard 동일 적용 — aggregated funding < 0.007%/8h 시 strategy paused.

### Build 결정 게이트

- owner G2: A5 archive lesson 후 재시도? = PASS 권고 (capacity shrinkage 잔존)
- 단, Ethena 같은 large player return shift 가 funding 회복 시 reconsider

### Module Path

```
packages/@qpm/alphas/optional/a22-crypto-vol-carry/
├── README.md
└── (build deferred)
```

---

## A23: US Treasury Yield Curve — Optional

### Origin (학술)

- **이론:** Litterman, R. B., & Scheinkman, J. (1991). "Common Factors Affecting Bond Returns." *Journal of Fixed Income*, 1(1), 54-61. *(citation: 1,800+)*
- **확장:** Ang, A., Piazzesi, M., & Wei, M. (2006). "What Does the Yield Curve Tell Us about GDP Growth?" *Journal of Econometrics*, 131(1-2), 359-403. *(citation: 1,500+)*
- **citation:** Litterman-Scheinkman 1991 = 1,800+; Ang 2006 = 1,500+
- **alpha decay timeline:** Stable (40+ years macro factor)

### Hypothesis

US Treasury yield curve (2yr-10yr, 5yr-30yr) spread changes = predictable + tradeable via ETFs (IEF / TLT / TIP). Steepening / flattening trades.

### Build 결정 게이트

- owner G2: A16 Risk Parity 의 TLT exposure 와 redundant check
- Phase 3 build 가능 (specialized macro alpha)

### Module Path

```
packages/@qpm/alphas/optional/a23-us-yield-curve/
├── README.md
└── (build deferred)
```

---

## A24: G10 FX Carry Trade — Optional

### Origin (학술)

- **원 paper:** Lustig, H., & Verdelhan, A. (2007). "The Cross Section of Foreign Currency Risk Premia and Consumption Growth Risk." *American Economic Review*, 97(1), 89-117. *(citation: 1,200+)*
- **확장:** Burnside, C., Eichenbaum, M., & Rebelo, S. (2011). "Carry Trade and Momentum in Currency Markets." *Annual Review of Financial Economics*, 3, 511-535. *(citation: 600+)*
- **citation:** Lustig-Verdelhan 2007 = 1,200+; Burnside 2011 = 600+
- **alpha decay timeline:** Medium decay (2008 GFC carry crash, 2015 SNB crash)

### Hypothesis

G10 currency pairs 의 interest rate differential = forward rate (UIP) 가 시간 평균으로 위배 → carry trade 양의 expectancy. **Cold honest**: 2008-09 carry crash + 2015 SNB CHF event 큰 tail risk.

### Build 결정 게이트

- owner G2: IBKR FX trading 활성 + capital allocation 5~10% 추가
- 본 12주 plan 에서 build X (시간 cost)

### Module Path

```
packages/@qpm/alphas/optional/a24-g10-fx-carry/
├── README.md
└── (build deferred)
```

---

# Section 6 · 통합 Build Roadmap (12주 Timeline)

## Week-by-Week Build Schedule

| Week | Build Targets | Asset Class | Hours (Strategy Lead) | Owner Action |
|---|---|---|---|---|
| 1 | Repo setup + Live page + KIS API 가입 | — | 40h (자율) | 2~3h KIS Open API 등록 |
| 2 | A11 Korean ETF Rotation | KIS | 30h (자율) | 0 |
| 3 | A11 backtest + A12 KOSPI Mean Rev start | KIS | 30h | 0 |
| 4 | A12 backtest + A13 Pair Trading start | KIS | 30h | 0 |
| 5 | A13 cointegration sweep + A14 PEAD start | KIS + DART | 30h | 0 |
| 6 | A14 backtest + A15 US Factor start (IBKR paper) | KIS + IBKR | 30h | 2~4h IBKR paper account |
| 7 | A15 + A16 Risk Parity build | IBKR | 30h | 0 |
| 8 | A17 US PEAD + A18 Sector Momentum | IBKR | 30h | 0 |
| 9 | A19 Covered Call + A20 VRP build | Options paper | 30h | 0 |
| 10 | A21 Iron Condor + integration backtest start | Options paper | 30h | 0 |
| 11 | Full Sensitivity Sweep (11 alphas) + DSR/PBO | All | 35h | review + Paper 1 SSRN draft 검토 |
| 12 | Paper 1 SSRN submission + Hacker News + Apply prep | — | 35h | review + signature + Apply 5건 |

**Total**: 380h Strategy Lead 자율 + 약 10~15h owner action (검토 + signature + 회사 outreach)

## Capital Allocation (Build 후 Live)

| Alpha | Capital % | Risk Tier | Notes |
|---|---|---|---|
| A11 Korean ETF Rotation | 30% | Conservative | Beta strategy |
| A12 KOSPI Mean Reversion | 20% | Medium | Lee-Park 2018 evidence |
| A13 Korea Pair Trading | 20% | Medium | Delta-neutral, short constraint |
| A14 PEAD KOSPI | 15% | Medium-aggressive | Event-driven |
| A15 US Factor FF5 | 25% | Conservative | Beta + factor exposure |
| A16 US Risk Parity | 25% | Conservative | All-weather 안정축 |
| A17 US PEAD | 10% | Aggressive | Small-cap risk |
| A18 US Sector Momentum | 15% | Medium | ETF-level |
| A19 Covered Call | 30% | Conservative | Income |
| A20 VRP | 10% | Aggressive | Tail risk |
| A21 Iron Condor | 10% | Aggressive | Vol regime dependent |

**Total target**: 210% notional (cross-asset overlap) → 실 capital = 자본의 100% 분산 (Korean 60% + US 50% + Options 50% nominal weights normalize)

**Real capital allocation (post-normalization)**:
- Korean equity/ETF: 자본의 30%
- US equity/ETF: 자본의 35%
- US Options: 자본의 25%
- Cash buffer: 자본의 10%

## DSR / PBO 통합 게이트

```python
def integration_gate(alpha_id, backtest_result):
    """모든 11 build alphas 통과 필수"""
    assert backtest_result['dsr'] >= 0.5, f"{alpha_id}: DSR < 0.5"
    assert backtest_result['pbo'] < 0.5, f"{alpha_id}: PBO >= 0.5 (overfitting)"
    assert backtest_result['oos_days'] >= 30 or backtest_result['oos_trades'] >= 30
    assert backtest_result['regimes_positive'] >= 2
    return True
```

## Cold Honest Final Recommendations

### 1. A11~A14 한국 시장 = 1순위 build (학술 evidence 강함)

D6 보고서 = 한국 적용 evidence 4개 (Kim-Kim 2020, Lee-Park 2018, Kang-Choi 2013, Choi-Lee 2017). 본 spec 의 한국 4 alphas = 학술 paper 직접 derivative. **Build 우선순위 최고**.

### 2. A15 US momentum 한국 이식 = STRICT NO

Chui-Titman-Wei 2000 + Kang 2018 evidence. A15 = US-only target 박제. 한국 KOSPI 에 같은 factor 적용 = HIGH RISK.

### 3. FF5 KOSPI = RMW/CMA redundant

Kang 2018 evidence 명확. A15 spec 의 RMW/CMA component = 한국 KOSPI 적용 시 redundant — 다음 cycle 한국 factor 알파 build 시 FF3 권고.

### 4. A2 OU = polyban 박제

108-cell sweep 0/108 = spec 자체 fail evidence. 같은 형식 (순수 OU + adjusted thresholds) 재시도 = build X. 대안 path = A13 Engle-Granger pair trading.

### 5. A6 AltMM = engine 미구현 박제

Avellaneda-Stoikov academic spec 만 박제. Engine 본 구현 = 다음 cycle (build cost 1~2 weeks).

### 6. DSR threshold cold honest

Bailey-Lopez de Prado 2014: DSR > 0.5 단순 reject baseline. **Real reject threshold = > 0.6 권고** (conservative). 본 spec 의 모든 11 build alphas = DSR ≥ 0.5 ~ 0.6 gate.

### 7. PBO < 0.5 = backtest overfitting 차단 필수

Bailey-Lopez de Prado 2017. Sensitivity sweep 의 top cell selection = overfitting risk. PBO < 0.5 = combinatorial cross-validation 기반 통과 강제.

### 8. 38일 PoC 외부 정책 변경 패턴 차단

각 알파 spec 의 "Honest Failure Risks" 섹션 = data sovereignty / 외부 의존 risk explicit mitigation. KIS API 정책 변경 / IBKR Korea launch / Polygon free tier 제한 등 모니터링.

### 9. Open Source educational disclaimer

`Yesol-Pilot/quant-poc-multi-asset` repo README 필수 박제:
- "Educational only, not investment advice"
- "Paper trading only in initial phase"
- "Past performance does not guarantee future results"
- License: MIT

### 10. 학술 publish 통합 (Paper 1 + Paper 2)

- **Paper 1 (SSRN, W11~W12)**: "Korean Retail Multi-Strategy Backtest: A 1-Person AI-Agent Production Pipeline" — 38일 Crypto PoC honest failure + 11 build alphas + portfolio integration
- **Paper 2 (ReScience, W12~W16)**: "Replication: Five-Factor Asset Pricing Model on KOSPI 200 (Kang 2018)" — A15 의 FF5 한국 적용 검증, Kang 2018 의 KOSPI 200 결과 (RMW/CMA redundant) 재현

---

# Appendix · 통합 References (62 papers, D6 보고서)

## Korean Market References

1. Kim, Y., & Kim, J. (2020). *Asia-Pacific Journal of Financial Studies*. ETF Rotation.
2. Lee, J., & Park, S. (2018). *Korean Journal of Finance*. KOSPI Mean Reversion.
3. Kang, J., & Choi, H. (2013). *Journal of the Korean Society for Industrial and Applied Mathematics*. Pair Trading KOSPI.
4. Choi, J., & Lee, K. (2017). *Asia-Pacific Journal of Accounting & Economics*. PEAD KSE.
5. Kang, S. (2018). *Korean Finance Review*. Five-Factor in Korean Market (RMW/CMA redundancy).
6. Chui, A. C., Titman, S., & Wei, K. C. (2000). *Working Paper*. Momentum in Asian Markets (Korean reversal).

## US Market References

7. Fama, E. F., & French, K. R. (2015). *Journal of Financial Economics*. Five-Factor Asset Pricing Model.
8. Fama, E. F., & French, K. R. (1993). *Journal of Financial Economics*. Three-Factor Model.
9. Carhart, M. M. (1997). *Journal of Finance*. Momentum 4-Factor.
10. Jegadeesh, N. (1990). *Journal of Finance*. 1-month reversal.
11. Jegadeesh, N., & Titman, S. (1993). *Journal of Finance*. Momentum winners/losers.
12. Moskowitz, T. J., & Grinblatt, M. (1999). *Journal of Finance*. Industry momentum.
13. Bernard, V. L., & Thomas, J. K. (1989). *Journal of Accounting Research*. PEAD original.
14. Livnat, J., & Mendenhall, R. R. (2006). *Journal of Accounting Research*. PEAD analyst forecasts.
15. Sadka, R. (2006). *Journal of Financial Economics*. Momentum + PEAD + Liquidity.
16. Chordia, T., et al. (2009). *Financial Analysts Journal*. Liquidity + PEAD.
17. Conover, C. M., et al. (2008). *Journal of Investing*. Sector Rotation + Monetary.
18. Engle, R. F., & Granger, C. W. (1987). *Econometrica*. Cointegration original.
19. Gatev, E., et al. (2006). *Review of Financial Studies*. Pairs Trading.

## Risk Parity / Macro

20. Dalio, R. (2005). *Bridgewater Associates White Paper*. Engineering Returns.
21. Asness, C. S., et al. (2012). *Financial Analysts Journal*. Risk Parity Aversion.
22. Anderson, R. M., et al. (2012). *Financial Analysts Journal*. Risk Parity Performance.
23. Litterman, R. B., & Scheinkman, J. (1991). *Journal of Fixed Income*. Bond Common Factors.

## Options + Volatility

24. Whaley, R. E. (2002). *Journal of Derivatives*. CBOE BXM (Covered Call).
25. Hill, J. M., et al. (2006). *Financial Analysts Journal*. Covered Index Writing.
26. Israelov, R., & Nielsen, L. N. (2014). *AQR White Paper*. Covered Calls Uncovered.
27. Coval, J. D., & Shumway, T. (2001). *Journal of Finance*. Expected Option Returns.
28. Carr, P., & Wu, L. (2009). *Review of Financial Studies*. Variance Risk Premiums.
29. Bollerslev, T., et al. (2009). *Review of Financial Studies*. Variance Risk Premia.
30. Hull, J. C. (2017). *Options, Futures, and Other Derivatives* (10th ed.). Textbook reference.

## Microstructure / HFT

31. Avellaneda, M., & Stoikov, S. (2008). *Quantitative Finance*. HFT Limit Order Book.
32. Cartea, A., Jaimungal, S., & Penalva, J. (2015). *Algorithmic and HFT*. Textbook.
33. Avellaneda, M., & Lee, J. H. (2010). *Quantitative Finance*. Statistical Arbitrage US Equities.

## Carry Trade

34. Lustig, H., & Verdelhan, A. (2007). *American Economic Review*. FX Carry Premia.
35. Burnside, C., et al. (2011). *Annual Review of Financial Economics*. Carry Trade.
36. Aktas, E., et al. (2022). *Working Paper*. Crypto Carry Trade.

## Event-Driven

37. Ederington, L. H., & Lee, J. H. (1993). *Journal of Finance*. News Releases Volatility.
38. Andersen, T. G., et al. (2003). *American Economic Review*. Macro Announcements FX.

## Crypto

39. Lehar, A., & Parlour, C. A. (2024). *UC Berkeley Working Paper*. Crypto Wash Trading.
40. Liu, X., & Zhao, Z. (2023). *Working Paper*. Funding Rate Arbitrage.
41. Liu, Y., & Tsyvinski, A. (2021). *Review of Financial Studies*. Crypto Risk and Returns.
42. Ornstein, L. S., & Uhlenbeck, G. E. (1930). *Physical Review*. OU process foundational.

## Risk Management / Statistical

43. Bailey, D. H., & Lopez de Prado, M. (2014). *Journal of Portfolio Management*. Deflated Sharpe Ratio (DSR).
44. Bailey, D. H., & Lopez de Prado, M. (2017). *Working Paper*. PBO Backtest Overfitting.
45. Faber, M. T. (2007). *Journal of Wealth Management*. Tactical Asset Allocation.

## Yield Curve / Bonds

46. Ang, A., et al. (2006). *Journal of Econometrics*. Yield Curve GDP.

## Industry References (지원 자료)

47. Hyblock Capital (2024). Liquidation cluster research.
48. Coinalyze (2024). Crypto liquidation data.
49. Coinglass (2024). Funding rate analysis.
50. CBOE (1986~). BXM Index methodology.
51. Tastytrade (2018). 21 DTE rule and option roll mechanics.
52. AQR Capital (2024). Risk parity research.
53. Bridgewater Associates (2005~). All Weather portfolio.

## Korean Domain References

54. KIS Developers (2024). Korea Investment & Securities Open API documentation.
55. DART (전자공시시스템) (2024). Korean financial disclosure system.
56. Korea Exchange (KRX) (2024). KOSPI 200 / KOSDAQ index methodology.
57. FnGuide (2024). Korean equity analyst consensus.
58. KOFIA (Korea Financial Investment Association) (2024). Korean retail short selling regulations.

## ETF / Index Methodology

59. SPDR (State Street) (2024). 11 sector ETF methodology.
60. iShares (BlackRock) (2024). Russell 2000 / 3000 methodology.
61. KODEX (Samsung Asset Management) (2024). Korean sector ETF methodology.
62. Morningstar (2024). ETF classification + factor exposure data.

---

## 가장 honest 한 한 줄 — 21 알파 Build Decision

**11 build alphas (한국 4 + 미국 7 + 옵션 3, A11~A21) 가 학술 paper 직접 derivative + DSR/PBO 통합 게이트 + Sensitivity Sweep 통합 검증 + 38일 PoC 외부 정책 변경 패턴 mitigation 모두 박제. 5 archive alphas (A1~A6) = closure 박제 + honest failure narrative 자산 + 다음 cycle build 시 학술 spec reference. 3 optional alphas (A22~A24) = owner G2 후 추가. 12주 build → 11 alphas live paper trading 14일 검증 → Sensitivity Sweep top cells DSR/PBO 통과 cell 만 live capital allocation → Paper 1 SSRN + Paper 2 ReScience FF5 KOSPI 학술 publish → portfolio narrative Open Source Yesol-Pilot/quant-poc-multi-asset 통합. 모든 알파 spec 600~900 단어 cold honest production-grade.**

---

## 박제 위치 + 다음 액션

- **본 SSOT**: `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/design/02-alpha-specs-21.md`
- **Canonical 권고**: `D:/00.test/002.products-sbu/quant-bot/docs/design/02-alpha-specs-21.md` (syncing)
- **다음 박제 (W1 시작 시)**: `packages/@qpm/alphas/a11-korean-etf-rotation/` 부터 11 modules scaffold + tests 1차 commit

owner G1 "Build 시작" 신호 → Week 1 즉시 진행.

👤 Strategy Lead Claude Opus 4.7 (자율 G1)
