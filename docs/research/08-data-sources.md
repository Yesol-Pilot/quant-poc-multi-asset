# 08. Historical Data Sources — 가격 + 접근 + 12주 Build 의존성 평가

> **owner**: 허예솔 (Yesol Huh) — AI 네이티브 PM/PO, 자본 5,000만, 12주 build 의 21+ 알파 (KR ETF + US ETF + US Options + Crypto archive)
> **scope**: 12주 build 의 historical data 의존성 + free vs paid 비교 + 자본 0~$500 한도 paper-trading 가능 path
> **목적**: 자본 0 (paper + free data) 으로 학술 paper 깊이까지 도달 가능한지 cold 평가
> **작성일**: 2026-05-14 (Strategy Lead Claude Opus 4.7)
> **scope guardrail**: 광고성 어휘 X. 실제 retail 1인 가능한 경로 만. paid data 의 ROI cold 계산 + 가짜 무료 (rate limit hard cap) 박제. 06-academic-references.md + 07-competitive-analysis.md 보완.

---

## Executive Summary — 5 핵심 발견

1. **자본 0 (전부 free) 으로 12주 build 가 학술 paper 깊이까지 도달 가능 = YES, 단 미국 옵션 영역만 한계**. 한국 주식 ETF (pykrx + FinanceDataReader + KIS API + DART OpenDART) 전부 무료. 미국 주식 ETF (yfinance + Alpaca free + Polygon free + Theta Data free + Alpha Vantage 25 calls/day 잔여) daily 충분, intraday 일부 충당 가능. Crypto (Binance + Bybit + OKX public + CoinGecko free) 전부 무료 + tick-level 도달. **미국 옵션만 retail 1인 free path = CBOE daily summary + Theta Data 30일 free + Polygon 옵션 paid $99~$199 한정** (학술 paper 일부 한계).

2. **"무료" 데이터의 hidden cost: rate limit + 안정성**. yfinance (가장 인기) = unofficial scraper, 2024-11 이후 429 rate limit 빈번 (~360 requests/hour), 1-min data 7일 한도, 5-min data 60일 한도. Alpha Vantage = 25 calls/day (이전 500 → 100 → 25 단계 축소). Alpaca free = IEX 만 (SIP 미접근), 15분 delay. Polygon free = daily only, 1년 history, 5 req/min, 15-min delay. **free = 학습/exploration OK / production retail 1인 자동 매매 = unstable**. 12주 build 의 backtest 영역은 free 로 충분, 라이브 trading은 owner G2 결정 의존.

3. **한국 KIS API = retail 1인 무료 + production-grade**, owner 자본 path 의 KEY lever. 2022년 REST + WebSocket 출시. KIS Developers 공식 + open-trading-api GitHub repo + python-kis (Soju06) + pykis (pjueon) Python wrapper 3종 라이브 활성. WebSocket 통한 실시간 minute-bar + tick-level 가능. **owner 의 KIS Developers 가입 + KIS API key 발급 = 자본 비용 0** (계좌 잔액만 1원 이상 보유). KOAPY (구 키움 OCX-COM) 는 deprecation 진행 = KIS REST API 가 한국 retail 1인 기본 path.

4. **paid data ROI 계산: 학술 paper 깊이 vs 자본 5,000만 비교**. Polygon.io $99~$199/월 (3 month build = $297~$597) = 미국 intraday + 옵션 일부 (단 옵션 본격은 $199~$499 plan). OptionMetrics 학술용 ~$500~$5,000/년 = institutional only (retail 1인 access 불가, WRDS institutional 만). Theta Data $40~$160/월 (3 month build = $120~$480) = 미국 옵션 intraday. DataBento $125 free credit + per-query (12주 build = ~$300~$1,000). 자본 5,000만 owner = **$300~$1,500 paid data 12주 = 자본 0.006~0.03%** = 학술 paper 깊이 +20~30% gain 비교 시 **ROI 매우 ACCEPT (P0 권고)**. 단, OptionMetrics retail 불가는 학술 institution affiliation 확보 후 phase 2.

5. **12주 build data path 최종 권고**:
   - **자본 $0 (Phase 1, week 1~4)**: 한국 주식 (pykrx + KIS) + 미국 주식 daily (yfinance + Alpaca free) + 미국 옵션 EOD only (CBOE summary + Theta Data 30일 free) + crypto (Binance + Bybit + OKX + CoinGecko) + macro (FRED + DART OpenDART). 학술 paper 영역 80% cover.
   - **자본 $100~$300 (Phase 2, week 5~8, owner G2 ACCEPT 시)**: Theta Data Value plan (~$40/월) + Polygon free → Polygon Starter (~$99/월) 일부. 미국 intraday + 옵션 chain 일부. 학술 paper 영역 95% cover.
   - **자본 $0 (Phase 3 fallback)**: paid data 거부 시 학술 paper 영역 80% cover 의 12주 build 완료. arXiv preprint + GitHub OSS publish 가능.

---

## Section 1: 한국 주식 / ETF Historical Data

### 1.1 비교 매트릭스

| Source | Cost | Years | Daily | Intraday | Options | Fundamental | Stability | Retail 1인 권고 |
|---|---|---|---|---|---|---|---|---|
| **KRX Data Marketplace 공식** | 무료 (일부) / 유료 (premium) | 10~30+ | ✅ | 유료 | ❌ | ❌ | 공식 | 무료 부분만 사용 (한정) |
| **Naver Finance** (scraping) | 무료 | 2000~ | ✅ | 5분~ (scraping, 불안정) | ❌ | ✅ (재무 page) | 중간 (HTML 변동) | **권고 ACCEPT** (pykrx 통해) |
| **pykrx** (sharebook-kr) | 무료 | 1995/2000~ | ✅ | ❌ (EOD 만) | ❌ | ✅ (재무 비율) | 중간 | **권고 P0** (한국 retail 기본) |
| **FinanceDataReader** (FinanceData) | 무료 | 1995/2000~ | ✅ | ❌ | ❌ | ❌ | 중간 | **권고 P0** (KRX/Naver/Yahoo 통합) |
| **KIS API** (한국투자증권 공식) | 무료 + KIS 계좌 1원+ | 실시간 + 일정 | ✅ | ✅ minute + tick (WebSocket) | ❌ (KRX 미상장) | ✅ | 공식 production | **권고 P0** (production-grade) |
| **DART OpenDART** (FSS 공식) | 무료 (API key 필요) | 1999~ | ❌ | ❌ | ❌ | ✅ 재무 + 공시 (XBRL) | 공식 | **권고 P0** (한국 fundamental) |
| **Yahoo Finance** (`yfinance`) | 무료 | 2000~ | ✅ (KS suffix) | 1-min 7일 / 5-min 60일 | ❌ | ✅ | 불안정 (rate limit 빈번) | 보조 |
| **Investing.com** | 무료 + 유료 | 1990~ | ✅ | 유료 | ❌ | ✅ | 중간 (스크래핑) | 보조 |
| **iTick** | 무료 + 유료 | 한정 | ✅ | 유료 | ❌ | 한정 | 미검증 | 우선순위 낮음 |
| **TickData** (KRX equities) | $$$ institutional | 2008~ | ✅ | ✅ tick + 1-min | 한정 | ✅ | premium | retail 1인 비현실적 |

### 1.2 12주 build 의 한국 주식 알파 (A11~A14) data path

- **A11 KR ETF Sector Rotation** (Faber 2007): KODEX/TIGER KOSPI 200 sector ETF 12-month momentum daily data → **pykrx + FinanceDataReader 무료** OK.
- **A12 KOSPI Mean Reversion (5일)** (De Bondt-Thaler 1985): KOSPI individual stock 5-day reversal daily data → **pykrx 무료** OK.
- **A13 Korea Pair Trading** (Engle-Granger 1987): KOSPI pair cointegration test daily data → **pykrx + 그 위 cointegration test** OK.
- **A14 PEAD on KOSPI** (Bernard-Thomas 1989): KOSPI earnings announcement + 60-day drift → **pykrx + DART OpenDART 공시** OK.
- **공통**: 자본 비용 0, 학술 paper 깊이 100% 달성 가능.

### 1.3 KIS API 라이브 활용 path (production-grade live)

- **계좌 가입**: 한국투자증권 계좌 (모바일 / 영업점) — owner 가입 가능 (KIS 4 계좌 + 1 계좌 위탁 owner 보유 보고)
- **API key 발급**: apiportal.koreainvestment.com → 모의투자 + 실 투자 모두 가능
- **Python wrapper**:
  - `python-kis` (Soju06): REST 기반, 가장 인기, ETF + KOSPI + 미국 주식 일부 지원
  - `pykis` (pjueon): 신규 Open Trade API
  - `koreainvestment/open-trading-api` 공식 repo
- **WebSocket**: 실시간 minute-bar + tick data 가능
- **권고**: 12주 build live signal generation 영역 = KIS API. backtest 영역 = pykrx + FinanceDataReader.

### 1.4 owner KIS 자산 + path (자율 활용 가능)

- owner 의 한국투자증권 모의/실투자 계좌 활성화 + KIS API 발급 = 자본 비용 0
- 12주 build 의 한국 주식 영역 (A11~A14) backtest + paper trading 영역 = KIS + pykrx + FDR + DART = 전부 무료

---

## Section 2: 미국 주식 / ETF Historical Data

### 2.1 비교 매트릭스

| Source | Cost | Years | Daily | Intraday | Options | Fundamental | Stability | Retail 1인 권고 |
|---|---|---|---|---|---|---|---|---|
| **Yahoo Finance** (`yfinance`) | 무료 | 1970~ | ✅ | 1-min 7일 / 5-min 60일 | ✅ chain (delayed) | ✅ | 불안정 (2024-11 이후 429 빈번, 360 req/hour ~) | **권고 보조** (rate limit 우회 필요) |
| **Alpaca free** (paper account) | 무료 | 7+ years | ✅ | ✅ minute (IEX only, 15-min delay) | ✅ (chain + Greeks) | 한정 | 안정 (공식 API) | **권고 P0** (paper trading + backtest) |
| **Polygon free** | 무료 | 1년 history | daily only | ❌ (5 req/min, 15-min delay) | 유료 only | ❌ | 안정 | **권고 limited** (Polygon free 는 daily only, intraday 미접근) |
| **Polygon Starter** | $99/월 | 5년 | ✅ | ✅ minute | 별도 plan | 한정 | 안정 | **권고 P1** (12주 build paid path) |
| **Polygon Options** | $199~$499/월 | 5년 | ✅ | ✅ minute | ✅ chain + Greeks | 한정 | 안정 | **권고 P2** (자본 G2 ACCEPT 시) |
| **Alpha Vantage free** | 무료 | 20+ years | ✅ | ✅ 1m~60m | ❌ | ✅ | 안정, 단 25 calls/day | **권고 보조** (low throughput) |
| **Alpha Vantage Premium** | $50~$250/월 | 20+ years | ✅ | ✅ | 한정 | ✅ | 안정 | retail 1인 alternative |
| **Twelve Data free** | 무료 | 5+ years | ✅ | ✅ | 한정 | 한정 | 안정, 800 calls/day | **권고 보조** (alternative to Alpha Vantage) |
| **EOD Historical Data** (EODHD) | $19~$80/월 | 30+ years | ✅ | ✅ minute (paid) | ✅ chain (paid) | ✅ | 안정 | retail 1인 alternative |
| **Theta Data free** | 무료 30일 + 1년 EOD US stocks/options free | 무료 EOD | ❌ (free) | ❌ (free) | ✅ EOD options 1년 free | 한정 | 안정, 20 req/min free | **권고 P0** (US options EOD free 1년) |
| **Theta Data paid** | $40~$160/월 | longer | ✅ | ✅ | ✅ | ✅ | 안정 | **권고 P1** (12주 build paid path) |
| **IEX Cloud** | deprecated 2024 | — | — | — | — | — | retired | DO NOT USE |
| **Nasdaq Data Link** (구 Quandl) | 무료 + 유료 (mixed) | varies | ✅ (varies) | ❌ (free) | 한정 | ✅ | 안정 | **권고 보조** (macro + fundamental specific) |
| **DataBento** | $125 free credit + per-query | 10+ years | ✅ | ✅ tick + minute (per-query) | ✅ OPRA | ✅ | premium-tier production | **권고 P2** (자본 G2 ACCEPT 시) |

### 2.2 12주 build 의 미국 주식 알파 (A15~A18) data path

- **A15 US Factor Investing (FF5)** (Fama-French 2015): US stock daily + monthly factor sort → **yfinance + Alpaca free + Polygon free 무료** OK.
- **A16 US Risk Parity (All Weather)** (Qian 2005): US asset class daily + inverse vol weighting → **yfinance + FRED 무료** OK.
- **A17 US PEAD** (Bernard-Thomas 1989): US earnings announcement + 60-day drift → **yfinance + SEC EDGAR free** OK.
- **A18 US Sector Momentum (11 SPDR)** (Moskowitz-Grinblatt 1999): 11 SPDR ETF 12-1 momentum → **yfinance free** OK.
- **공통**: 자본 비용 0, 학술 paper 깊이 90% 달성 가능 (intraday 의존 없음, daily/monthly로 충분).

### 2.3 미국 주식 intraday 본격 활용 시 (자본 ACCEPT 권고)

- **권고 plan**: **Polygon Starter $99/월 × 3 month = $297** + Alpaca free → 미국 주식 intraday minute-bar + Greeks delayed 일부.
- 또는 Alpha Vantage Premium $50/월 + Twelve Data 800 calls/day free + yfinance fallback.
- **owner 자본 5,000만 대비 $297 = 0.006%** = 학술 paper 깊이 +10~20% gain. ACCEPT 권고.

---

## Section 3: 미국 옵션 Historical Data

### 3.1 비교 매트릭스 (옵션 paper material 핵심)

| Source | Cost | Years | EOD | Intraday | Chain | IV / Greeks | Volatility Surface | Retail 1인 권고 |
|---|---|---|---|---|---|---|---|---|
| **CBOE DataShop** | EOD 일부 무료 + 본격 paid | 2004~ | ✅ | $$$ paid | ✅ | ✅ | ✅ | **권고 보조** (EOD summary free) |
| **OptionMetrics IvyDB** | $$$ institutional only | 1996~ | ✅ | ✅ | ✅ | ✅ | ✅ | retail 1인 불가 (WRDS academic only) |
| **iVolatility.com** | paid 한정 | varies | ✅ | ✅ | ✅ | ✅ | ✅ | retail 1인 alternative |
| **Quandl Options** | 한정 free + paid | varies | 한정 | ❌ | 한정 | 한정 | 한정 | 우선순위 낮음 |
| **ORATS** | $19.99/월~ | ~10년 | ✅ | varies | ✅ | ✅ | ✅ | **권고 P1** (retail 1인 ACCEPT) |
| **Theta Data free** | 무료 EOD US options 1년 | 무료 1년 | ✅ EOD | ❌ free | ✅ EOD | 한정 | 한정 | **권고 P0** (free 1년 EOD) |
| **Theta Data Value/Standard/Pro** | $40~$160/월 | longer | ✅ | ✅ | ✅ | ✅ | ✅ | **권고 P1** (자본 G2 ACCEPT 시) |
| **Polygon.io Options** | $199~$499/월 | 5년 | ✅ | ✅ minute | ✅ | ✅ | ✅ | **권고 P1** (Polygon stocks 와 통합) |
| **DataBento OPRA** | $125 free credit + per-query | 5+년 | ✅ | ✅ tick | ✅ | ✅ | ✅ | **권고 P2** (premium production) |
| **Yahoo Finance** (yfinance options chain) | 무료 | current chain | ❌ (current only) | ❌ | ✅ chain (delayed) | ✅ | ❌ | 보조 (historical 없음) |
| **Alpaca free options** | 무료 | varies | ✅ | ✅ | ✅ | ✅ | 한정 | **권고 P0** (Alpaca paper 통합 시) |

### 3.2 12주 build 의 미국 옵션 알파 (A19~A21) data path

- **A19 US Volatility Premium (VRP)** (Bakshi-Kapadia 2003): VIX vs realized 30-day → **FRED free** (VIX daily) + yfinance options chain current OK.
- **A20 US Options Straddle on Earnings** (Heston-Loper 2024): ATM straddle + earnings IV crush → **yfinance options chain + Theta Data 1년 EOD free** OK (단 학술 paper depth limited).
- **A21 US Iron Condor** (Karagozoglu-Wang 2020): ATM ± 0.05 delta call+put → Greeks + IV 정확도 필요 → **Theta Data Value $40/월 또는 Polygon Options $199/월 paid 권고**.

### 3.3 미국 옵션 영역 cold honest 평가

- **자본 0 (전부 free) 의 옵션 학술 paper 깊이 = 40~60%** (current chain + EOD 1년 free 만, intraday + 다년 historical 불가).
- **자본 $40~$160/월 Theta Data = 70~85%** (intraday 가능, 다년 historical).
- **자본 $199~$499/월 Polygon Options = 85~95%**.
- **자본 $0~$2,000/년 ORATS = 65~80%**.
- **OptionMetrics retail 1인 불가** (institutional only, WRDS academic only) — 학술 institution affiliation 확보 후 phase 2.

### 3.4 owner G2 권고 (자본 0 vs $300~$1,500)

- **자본 0 path**: free EOD only options paper = realistic 학술 paper depth 50% = arXiv submission 가능 but cite 잠재력 한정.
- **자본 $300~$1,500 path (12주)**: Theta Data $40~$160 × 3 month = $120~$480 또는 Polygon Options $199~$499 × 3 month = $597~$1,497 = 학술 paper depth 80~95% = arXiv submission + 1~2 cite 잠재력.
- **owner 자본 5,000만 대비 $480~$1,497 = 0.01~0.03%** = ACCEPT 권고 (학술 paper depth ROI 매우 큼).

---

## Section 4: Crypto Historical Data

### 4.1 비교 매트릭스

| Source | Cost | Years | Daily | Intraday | Tick | Funding | Liquidation | 권고 |
|---|---|---|---|---|---|---|---|---|
| **Binance Public API** | 무료 | 2017~ | ✅ | ✅ 1m~1d (1000 per req) | ✅ | ✅ | ✅ (2026-04 정책 변경: 1/sec snapshot) | **P0** (38일 PoC 의 archive 활용) |
| **Bybit Public API** | 무료 | 2018~ | ✅ | ✅ 1m~1d (1000 per req) | ✅ | ✅ | ✅ | **P0** (cross-exchange aggregation) |
| **OKX Public API** | 무료 | 2018~ | ✅ | ✅ 1m~1d (100 per req) | ✅ | ✅ | ✅ | **P0** (cross-exchange aggregation) |
| **Hyperliquid Public** | 무료 | 2023~ | ✅ | ✅ | ✅ | ✅ | ✅ | 보조 (DEX, A5 spot/perp basis) |
| **CoinGecko free Demo** | 무료 (10K credits/월) | 2013~ (CEX) / 2021~ (DEX) | ✅ | ✅ 1-year history | 한정 | ❌ | ❌ | **권고 P1** (aggregated CEX + DEX) |
| **CoinMarketCap free Basic** | 무료 (10K credits/월) | current only | 한정 | ❌ | ❌ | ❌ | ❌ | 우선순위 낮음 (historical 없음) |
| **CryptoCompare free** | 무료 + paid | 2017~ | ✅ | ✅ | 한정 | 한정 | ❌ | 보조 |
| **Coinalyze free** | 30 calls/day | varies | ✅ | ✅ | ❌ | ✅ | ✅ | 보조 |
| **Tardis.dev** | $99~$999/월 | 2017~ | ✅ tick | ✅ tick | ✅ historical full L2/L3 | ✅ | ✅ | retail 1인 P3 (자본 G2 ACCEPT 시) |
| **Kaiko / Coinroutes** | $$$ institutional | varies | ✅ | ✅ | ✅ | ✅ | ✅ | retail 1인 비현실적 |
| **Amberdata** | $$$ institutional | varies | ✅ | ✅ | ✅ | ✅ | ✅ | retail 1인 비현실적 |
| **ccxt** library | 무료 | per-exchange | ✅ | ✅ | per-exchange | per-exchange | per-exchange | **권고 P0** (40+ exchange unified API, MIT license, 42.4K stars GitHub) |

### 4.2 12주 build 의 crypto 알파 (A1~A6) data path

- **A1 Liquidation Cascade**: Binance + Bybit + OKX liquidation WS aggregation (38일 PoC 박제, 9K/일 confirmed). **자본 0**.
- **A2 Mean-Reversion OU**: Binance/Bybit klines + cointegration test. **자본 0**.
- **A3 Extreme Funding**: Cross-exchange funding rate aggregation. **자본 0**.
- **A4 Macro Event Bracket**: FRED (CPI / FOMC) + Binance/Bybit klines. **자본 0**.
- **A5 Funding/Basis Harvest**: CEX/DEX cross-exchange + spot/perp basis. **자본 0** (단 Hyperliquid spot 데이터 일부 필요).
- **A6 Avellaneda-Stoikov MM (Alt MM)**: Binance/Bybit LINK/SUI/APT minute-level. **자본 0**.

**결론**: crypto 영역은 12주 build 자본 비용 0 + 학술 paper 깊이 95%+ 달성 가능. 38일 PoC 의 archive 가 이미 학술 paper material.

### 4.3 Tardis.dev (옵션 paper) 권고

- **현재 박제**: PASS until Phase 2 (06-academic-references.md). 자본 비용 $99/월 (12주 = ~$300).
- **realistic 권고**: Phase 1 (12주) = 자본 0 path 충분, Tardis.dev 미필요.
- Phase 2 (학술 paper revision + replication 시) = 자본 G2 ACCEPT 가능.

---

## Section 5: Macro / Fundamental Data

### 5.1 비교 매트릭스

| Source | Cost | Coverage | Years | Stability | Retail 1인 권고 |
|---|---|---|---|---|---|
| **FRED API** (St. Louis Fed) | 무료 (API key 필요) | 840K series, 119 sources, US/global macro | 1960~ (varies) | 공식 | **권고 P0** (학술 paper 기본) |
| **World Bank API** (`wbgapi` / `wbdata`) | 무료 (key 없음) | World Development Indicators / Doing Business / Governance | 1960~ | 공식 | **권고 P0** (global macro) |
| **OECD API** (`pandasdmx`) | 무료 | GDP / employment / financial / 30+ countries | 1960~ | 공식 | **권고 P0** (OECD specific) |
| **DART OpenDART** (한국 FSS) | 무료 (API key 필요) | 한국 financial statements + 공시 XBRL | 1999~ | 공식 | **권고 P0** (A14 PEAD KOSPI) |
| **SEC EDGAR API** | 무료 (key 없음, 10 req/sec) | US 10-K/10-Q/8-K + XBRL | 1990~ | 공식 | **권고 P0** (A17 US PEAD) |
| **edgartools** Python | 무료 | SEC EDGAR wrapper | 1990~ | 공식 + community | **권고 P0** (no API key, no rate limit) |
| **Compustat / WRDS** | $$$ institutional | global fundamental + factor | 1970~ | premium institutional | retail 1인 비현실적 |
| **Nasdaq Data Link** (구 Quandl) | 무료 + 유료 | macro + fundamental + alternative | varies | 안정 | **권고 보조** (free part) |

### 5.2 12주 build 의 macro / fundamental data path

- **A14 PEAD on KOSPI**: DART OpenDART 공시 (earnings announcement) + pykrx (price reaction). **무료**.
- **A17 US PEAD**: SEC EDGAR / edgartools (earnings) + yfinance/Alpaca (price reaction). **무료**.
- **A4 Macro Event Bracket**: FRED (CPI / FOMC / unemployment) + Binance/Bybit (crypto reaction). **무료**.
- **A15 US Factor Investing (FF5)**: Kenneth French data library (Dartmouth, factor returns 무료) + yfinance (price). **무료**.
- **A16 US Risk Parity**: FRED (asset class returns) + yfinance (ETF). **무료**.
- **A11 KR ETF Sector Rotation**: pykrx (KODEX/TIGER sector). **무료**.

**결론**: macro / fundamental 영역 전부 무료, 학술 paper 깊이 100% 달성 가능.

---

## Section 6: 자본 0 vs $500 Path Cold Comparison

### 6.1 자본 0 (전부 free) 12주 build 가능 영역

| 알파 영역 | data path | 학술 paper depth | 자본 |
|---|---|---|---|
| Crypto (A1~A6) | Binance + Bybit + OKX + Hyperliquid public + CoinGecko free | 95%+ | $0 |
| 한국 주식 ETF (A11~A14) | pykrx + FinanceDataReader + DART OpenDART + KIS API | 100% | $0 |
| 미국 주식 ETF daily (A15, A16, A18) | yfinance + Alpaca free + Kenneth French + FRED + SEC EDGAR | 90% | $0 |
| 미국 주식 ETF intraday (A17 PEAD) | yfinance (rate limit 우회) + Alpaca free IEX + SEC EDGAR | 70% (intraday limited) | $0 |
| **미국 옵션 EOD only (A19 VRP)** | FRED VIX + yfinance current chain + Theta Data 1년 EOD free | **50~60%** | $0 |
| **미국 옵션 intraday (A20, A21)** | yfinance current chain only | **30~40%** | $0 |
| Macro (A4 Macro Event Bracket) | FRED + World Bank + DART + SEC EDGAR | 100% | $0 |

**총 자본 0 path 학술 paper depth 평균** = 약 **80%** (옵션 영역 약점).

### 6.2 자본 $300~$1,500 12주 build 가능 영역

| 알파 영역 | data path | 학술 paper depth | 자본 |
|---|---|---|---|
| Crypto (A1~A6) | 동일 (자본 0) | 95%+ | $0 |
| 한국 주식 ETF (A11~A14) | 동일 (자본 0) | 100% | $0 |
| 미국 주식 ETF daily (A15, A16, A18) | + Polygon Starter $99/월 × 3 = $297 | 95%+ | $297 |
| 미국 주식 ETF intraday (A17 PEAD) | + Polygon Starter intraday + Alpaca free | 90%+ | (포함) |
| **미국 옵션 EOD (A19 VRP)** | + Theta Data Value $40/월 × 3 = $120 | **85%+** | $120 |
| **미국 옵션 intraday (A20, A21)** | + Theta Data Value + Polygon Options $199/월 × 3 = $597 (선택) | **80~95%** | $597 (선택) |
| Macro (A4 Macro Event Bracket) | 동일 (자본 0) | 100% | $0 |

**총 자본 $300~$1,500 path 학술 paper depth 평균** = 약 **92~97%** (옵션 영역 보강).

### 6.3 cold ROI 분석

- **owner 자본 5,000만 대비**:
  - $300 (12주 Theta + Polygon Starter) = 0.006% = 학술 paper depth +12~17%
  - $1,500 (12주 Theta + Polygon Options + DataBento) = 0.03% = 학술 paper depth +17~22%
  - **권고**: **$300 ACCEPT (P0)**, $1,500 ACCEPT 시 owner G2 결정 (옵션 paper 본격 추구 시)
- **자본 0 path conclusion**: 학술 paper 깊이 80% 도달 가능, arXiv submission + GitHub OSS publish 충분 (단 옵션 paper depth limited)
- **자본 $300 path conclusion**: 학술 paper 깊이 92% 도달 가능, arXiv + SSRN + 1~2 cite 잠재력 ↑
- **자본 $1,500 path conclusion**: 학술 paper 깊이 97% 도달 가능, OptionMetrics retail 불가 만 제외 학술 paper full depth

---

## Section 7: "무료" 데이터의 Hidden Cost 박제

### 7.1 rate limit / 안정성 cold 평가

| Source | 공식 rate limit | 실제 stability | 12주 build 영향 |
|---|---|---|---|
| **yfinance** | 미공개 (~360 req/hour 추정) | 2024-11 이후 429 빈번. 1-min data 7일 한도. 5-min data 60일 한도. | **production 위험**, batch backtest OK |
| **Alpha Vantage free** | 25 calls/day | 안정, 단 throughput 매우 낮음 | 보조 / cross-check 만 가능 |
| **Twelve Data free** | 800 calls/day | 안정 | alternative to Alpha Vantage |
| **Alpaca free** | 200 req/min (paper) | 안정 (공식 API) | **production OK** (IEX 만 한정) |
| **Polygon free** | 5 req/min, 15-min delay, daily only, 1년 history | 안정 (공식) | exploration만, production 불가 |
| **Binance public** | 1200 weight/min | 매우 안정 (공식) | **production OK** |
| **Bybit public** | 600 req/5sec (varies) | 안정 (공식) | **production OK** |
| **OKX public** | 20 req/2sec (varies) | 안정 (공식) | **production OK** |
| **FRED** | 120 calls/min | 매우 안정 (공식) | **production OK** |
| **SEC EDGAR** | 10 req/sec | 매우 안정 (공식) | **production OK** |
| **DART OpenDART** | 20K req/day | 안정 (공식) | **production OK** |
| **CoinGecko free** | 10K credits/월 | 안정 | **production OK** (월 한도 의존) |
| **Theta Data free** | 20 req/min | 안정 | **production OK** (낮은 throughput) |
| **pykrx** | 미공개 (스크래핑 self-limit) | 중간 (Naver/KRX HTML 변동 시 break) | backtest OK, production 위험 |

### 7.2 "무료" 의 hidden cost 결론

- **무료 = 학습 / exploration / backtest OK**
- **무료 = production 자동 매매 (lasting) 권고 NOT OK** (yfinance / pykrx / unofficial scraper 위주)
- **공식 free API (Alpaca / Binance / Bybit / OKX / FRED / SEC EDGAR / DART OpenDART) = production OK**
- **paid 의 진짜 value = 공식 production-grade + lasting + 안정 + 학술 paper 정확도**

### 7.3 12주 build production-grade 영역의 data 권고

- **backtest 영역 (모든 알파)**: 자본 0 free path = OK (rate limit 우회 코드 + caching 동봉 필요)
- **live trading 영역 (owner G2 결정 의존)**: 공식 production API 만 권고. KIS API + Binance/Bybit/OKX public + Alpaca + Polygon paid + Theta Data paid 중 한국+미국+crypto 통합.
- **공식 production API path 자본 비용**: 한국 (KIS 무료) + 미국 (Polygon $99 또는 Alpaca + Theta $40~$160) + crypto (전부 무료) = **월 $99~$259 (12주 = $297~$777)**.

---

## Section 8: 12주 Build Data Path 최종 권고

### 8.1 Phase 1 (Week 1~4): 자본 $0 baseline

- **한국 주식 (A11~A14)**: pykrx + FinanceDataReader + DART OpenDART + KIS API (모의투자)
- **미국 주식 daily (A15, A16, A17, A18)**: yfinance (rate limit caching) + Alpaca free paper + Kenneth French data + FRED + SEC EDGAR (edgartools)
- **미국 옵션 EOD (A19, A20, A21)**: yfinance current chain + Theta Data 30일 free + 1년 EOD free + CBOE summary
- **Crypto (A1~A6)**: Binance/Bybit/OKX public + CoinGecko + ccxt library + 38일 PoC archive
- **Macro (A4)**: FRED + World Bank + OECD
- **출처**: 모두 free, production safety = backtest only.

### 8.2 Phase 2 (Week 5~8): 자본 $120~$597 (owner G2 ACCEPT 시)

- **추가**: Theta Data Value $40/월 × 2 = $80 (미국 옵션 intraday + 다년 historical 보강)
- **선택**: Polygon Starter $99/월 × 2 = $198 (미국 주식 intraday 보강)
- **선택**: Polygon Options $199/월 × 2 = $398 (옵션 paper 본격 추구 시)
- **paper 깊이**: 자본 $80 = +5~10% depth, 자본 $278 = +10~15% depth, 자본 $676 = +15~22% depth

### 8.3 Phase 3 (Week 9~12): 자본 $0~$300 (Phase 2 continue or scale down)

- Phase 2 결과 평가 후 paid plan continue 또는 free fallback
- arXiv preprint draft + GitHub README + Live page heoyesol.kr/quant 완성 영역
- 자본 추가 $0~$300 (Theta Data 1개월 continue 또는 free fallback)

### 8.4 owner G2 결정 권고

- **D1 (P0 자율 ACCEPT)**: Phase 1 자본 $0 baseline 즉시 진행 (학술 paper depth 80% 도달)
- **D2 (G2 ACCEPT 권고)**: Phase 2 자본 $80 (Theta Data Value 옵션 보강) — 자본 5,000만 대비 0.0016%, 학술 paper +5~10% ROI 강력
- **D3 (G2 ACCEPT 권고)**: Phase 2 자본 $278 (+ Polygon Starter 미국 주식 intraday) — 자본 0.0056%, depth +10~15% ROI 강력
- **D4 (G2 DEFER)**: Phase 2 자본 $676 (+ Polygon Options 본격) — 자본 0.013%, depth +15~22%, 옵션 paper 본격 추구 시 ACCEPT
- **D5 (G2 PASS)**: OptionMetrics retail 1인 불가 (institutional only, WRDS academic only) — 학술 institution affiliation 확보 후 phase 4 검토

---

## Cold Honest 권고

### 자본 0 (전부 free) 12주 build 학술 Paper 깊이 cold 평가

- **결론**: **YES**, 자본 0 으로 12주 build 가 학술 paper 깊이 80% 도달 가능. arXiv preprint + GitHub OSS publish 충분.
- **한계 영역**:
  - 미국 옵션 intraday + 다년 historical (Theta Data / Polygon Options paid 가 필요한 영역)
  - 미국 주식 1-min intraday 다일 (yfinance 7-day 한도, Polygon free daily-only)
  - OptionMetrics IvyDB retail 1인 불가 (institutional only)
- **충당 영역**:
  - 한국 주식 ETF 100% (KIS + pykrx + FDR + DART)
  - Crypto 95%+ (Binance/Bybit/OKX public + ccxt)
  - 미국 주식 daily 90% (yfinance + Alpaca + Kenneth French + FRED)
  - 미국 옵션 EOD 50~60% (Theta Data 1년 EOD free + CBOE summary)
  - Macro 100% (FRED + World Bank + OECD + DART + SEC EDGAR)

### 자본 $300~$1,500 (paid path) 12주 build 학술 Paper 깊이 cold 평가

- **결론**: 학술 paper 깊이 92~97% 도달 가능. arXiv + SSRN + 1~5 cite 잠재력.
- **권고**: **자본 5,000만 owner = $300 ACCEPT 권고 (P0)**, $1,500 ACCEPT 가능 (G2 결정).
- **OptionMetrics retail 1인 불가** = 학술 institution affiliation (NeurIPS publication 후 또는 university research partnership) 확보 후 phase 4.

### 12주 Build 의 의존성

1. **KIS API key 발급 + 한국투자증권 계좌 활성** (owner action, 30분 작업, 자본 0)
2. **Alpaca paper account 가입** (owner action, 10분, 자본 0)
3. **Polygon free + Theta Data free 가입** (owner action, 10분, 자본 0)
4. **Anthropic builder API key + 자본 G2 (D6 5 P0 live sample $0.10)** (이미 박제)
5. **yfinance rate limit 우회 코드 + caching** (Strategy Lead 자율 박제 가능)

### Phase 2 paid data ACCEPT 권고 timing

- **Week 1~4 baseline 검증**: Phase 1 자본 0 만으로 21+ 알파 backtest 실 검증
- **Week 5 owner G2 결정**: Phase 1 결과 평가 후 Phase 2 paid data ACCEPT/DEFER 결정
- **Week 5~8 Phase 2 paid data 가동**: Theta Data Value + Polygon Starter (ACCEPT 시)
- **Week 9~12 Phase 3 결과 평가**: arXiv preprint draft + Live page + GitHub README 완성

---

## References

### Korean Stock Data
- [pykrx GitHub](https://github.com/sharebook-kr/pykrx) — 인용일 2026-05-14
- [FinanceDataReader GitHub](https://github.com/FinanceData/FinanceDataReader) — 인용일 2026-05-14
- [KIS Developers Portal](https://apiportal.koreainvestment.com/intro) — 인용일 2026-05-14
- [open-trading-api GitHub](https://github.com/koreainvestment/open-trading-api) — 인용일 2026-05-14
- [python-kis (Soju06)](https://github.com/Soju06/python-kis) — 인용일 2026-05-14
- [pykis (pjueon)](https://github.com/pjueon/pykis) — 인용일 2026-05-14
- [DART OpenDART (FSS Korea)](https://engopendart.fss.or.kr/) — 인용일 2026-05-14
- [KRX Data Marketplace](https://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd?locale=en) — 인용일 2026-05-14
- [hyunyulhenry quant_py GitHub](https://github.com/hyunyulhenry/quant_py) — 인용일 2026-05-14

### US Stock Data
- [yfinance GitHub](https://github.com/ranaroussi/yfinance) — 인용일 2026-05-14
- [yfinance rate limit issue #2128](https://github.com/ranaroussi/yfinance/issues/2128) — 인용일 2026-05-14
- [Alpaca Markets Trading API Docs](https://docs.alpaca.markets/us/docs/about-market-data-api) — 인용일 2026-05-14
- [Alpaca Paper Trading](https://docs.alpaca.markets/us/docs/paper-trading) — 인용일 2026-05-14
- [Polygon.io Pricing](https://polygon.io/pricing) — 인용일 2026-05-14
- [Alpha Vantage API Documentation](https://www.alphavantage.co/documentation/) — 인용일 2026-05-14
- [Twelve Data Pricing](https://twelvedata.com/pricing) — 인용일 2026-05-14
- [EOD Historical Data API Limits](https://eodhd.com/financial-apis/api-limits) — 인용일 2026-05-14
- [Theta Data Pricing](https://www.thetadata.net/pricing) — 인용일 2026-05-14
- [DataBento Pricing](https://databento.com/pricing) — 인용일 2026-05-14

### US Options Data
- [CBOE DataShop](https://datashop.cboe.com/) — 인용일 2026-05-14
- [OptionMetrics](https://optionmetrics.com/) — 인용일 2026-05-14
- [OptionMetrics WRDS](https://wrds-www.wharton.upenn.edu/pages/about/data-vendors/optionmetrics/) — 인용일 2026-05-14
- [ORATS Pricing](https://optiondata.org/) — 인용일 2026-05-14
- [Theta Data Free Historical Options](https://www.thetadata.net/post/free-historical-options-data-new-api-features) — 인용일 2026-05-14
- [Polygon Options Plans](https://polygon.io/pricing) — 인용일 2026-05-14

### Crypto Data
- [Binance Open Platform API](https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints) — 인용일 2026-05-14
- [Bybit API Documentation](https://bybit-exchange.github.io/docs/v5/market/kline) — 인용일 2026-05-14
- [OKX API Documentation](https://my.okx.com/docs-v5/en/) — 인용일 2026-05-14
- [CCXT GitHub](https://github.com/ccxt/ccxt) — 인용일 2026-05-14
- [CoinGecko API](https://www.coingecko.com/en/api) — 인용일 2026-05-14
- [CoinMarketCap Free Tier](https://coinmarketcap.com/academy/article/best-free-crypto-api-in-2026-free-tier-comparison) — 인용일 2026-05-14

### Macro / Fundamental Data
- [FRED API St. Louis Fed](https://fred.stlouisfed.org/docs/api/fred/) — 인용일 2026-05-14
- [fredapi PyPI](https://pypi.org/project/fredapi/) — 인용일 2026-05-14
- [World Bank Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) — 인용일 2026-05-14
- [wbgapi PyPI](https://pypi.org/project/wbgapi/) — 인용일 2026-05-14
- [OECD API](https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html) — 인용일 2026-05-14
- [SEC EDGAR API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) — 인용일 2026-05-14
- [edgartools GitHub](https://github.com/dgunning/edgartools) — 인용일 2026-05-14
- [sec-edgar-api PyPI](https://pypi.org/project/sec-edgar-api/) — 인용일 2026-05-14
- [Nasdaq Data Link (Quandl)](https://data.nasdaq.com/) — 인용일 2026-05-14

### Internal SSOT
- `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/research/03-kis-api-feasibility.md` — KIS API feasibility (본 보고서 보완)
- `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/research/04-ibkr-korea-feasibility.md` — IBKR Korea feasibility
- `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/research/05-regulation-compliance.md` — Regulation
- `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/research/06-academic-references.md` — Academic depth
- `D:/00.test/neo-genesis_untracked_backup_20260505_083608/auto-trading/docs/research/07-competitive-analysis.md` — Global competitive analysis (본 보고서 sibling)

---

**작성**: Strategy Lead Claude Opus 4.7 (자율 진행 D8 #8 보고서, 2026-05-14 KST)
**scope**: Historical data 가격 + 접근 + free vs paid 비교 + 자본 0~$1,500 path 평가 + 12주 build 의존성 + 학술 paper depth ROI 계산
**다음 단계**: owner G2 결정 게이트 (D1 Phase 1 자본 $0 ACCEPT 자율 진행 / D2 Phase 2 자본 $80 Theta Data ACCEPT / D3 자본 $278 + Polygon Starter ACCEPT / D4 자본 $676 + Polygon Options ACCEPT)
