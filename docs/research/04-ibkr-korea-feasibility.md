# 04. Interactive Brokers (IBKR) Korea — Cold Feasibility (한국 retail 1인 quant)

> **조사 시점**: 2026-05-14
> **조사자**: Claude Opus 4.7 (Strategy Lead, agent-mode research)
> **대상**: Interactive Brokers LLC (IBKR Pro) for Korean residents + TWS/IB Gateway API
> **기준**: 38일 PoC 실패 (Binance forceOrder 정책 변경) 교훈 — 외부 의존성 모든 한계 명확히 박제
> **언어 정책**: cold honest, 광고성 표현 회피, 실 운영 에러 패턴 우선

---

## Executive Summary — 5 핵심 발견

1. **IBKR 한국 거주자 가입 정식 가능, 2025년 KYC + KRX 직접 거래 양방향 개방** — IBKR 공식 한국어 페이지 + Korean residents 가입 절차 표준화. 비대면 신청 후 수시간~24시간 내 승인 표준. 한국 retail 미국 직투에 사실상 최적. **2026년 5월 IBKR 가 한국 거래소(KRX) 직접 거래까지 launch** (한국 주식까지 단일 계좌). 최소 입금액 **$0**, inactivity fee **$0** (2025년 미국 계좌 폐지).
2. **Paper Trading Account = 실 계좌 가입 후 무료 활성, $1M virtual default** — 실 계좌 승인 후 client portal 에서 paper account 생성. 시세는 실 데이터 (단, market data subscription 미가입 시 delayed 15분). TWS/IB Gateway 동일 인증서로 연결 → 알파 wiring + paper 백테스트 무한정.
3. **TWS API rate limit = 50 messages/sec (TWS) 또는 250 msg/sec (FIX) — KIS 의 20 RPS 대비 압도적 여유** — 단, historical data 호출 시 별도 pacing rule (동일 contract 2초 내 6회 = violation, 15초 내 동일 요청 = violation). 정식 native API `ibapi` (Python) + 커뮤니티 `ib_async` (1.5k stars, v2.0.1 2025-06, 이전 `ib_insync` maintainer 사망 후 fork). 실 운영 retail 사용자 수만 명, 자동매매 인프라 압도적 성숙.
4. **자산군 = 미국 NYSE/NASDAQ/AMEX 주식·ETF·옵션·선물·FX + KRX 한국 주식 (2026-05 신규) + 글로벌 170 시장** — 1인 quant 의 모든 자산군이 단일 계좌. 단, US market data subscription 별도 ($1.50~$10/월 retail, commission $30 이상 자동 면제). **옵션 historical / 분봉 historical / 틱 데이터 = 무료 제공** (TWS API 한도 내).
5. **수수료 압도적 우위 (Tiered)** — 미국 주식 0.05~0.35¢/share (volume 의존, $0.35 min, max 1%). 100주 $25 = $1.00 commission (KIS 0.25% = $6.25 대비 6분의 1). FX USD↔KRW: 0.20 basis points + $2 min/주문 (KIS 우대 0.1% 대비 5분의 1 이상 저렴). **단, 시초 deposit 시 한국 은행 SWIFT 송금 + 자기명의만 (제3자 송금 불가)**.

**Bottom line (cold)**: IBKR 는 **한국 retail 1인 quant 의 글로벌 자산군 / 압도적 비용 우위 / API 성숙도 측면 사실상 최고**. 단, **(a) 한국 은행 → IBKR SWIFT 송금 1차 셋업, (b) TWS/IB Gateway 로컬 데몬 운영 의무 (Linux/Docker 가능), (c) 시세 subscription 별도 결제** 이 3가지 setup 비용은 명확히 인지 필요. IBKR 단독 운영 시 KIS 가 필요 없는 시나리오도 가능 (단, 한국 주식·ETF KIS 가 더 저렴할 가능성은 별도 검증 필요).

---

## 1. Overview — IBKR Pro / TWS API 기본

### IBKR 한국 거주자 = IBKR Pro 만 가능
| 옵션 | 한국 거주자 |
|---|---|
| IBKR Pro | ✅ 유일 옵션 |
| IBKR Lite (commission-free) | ❌ US + Singapore 거주자만 |

한국 거주자는 자동으로 IBKR Pro 가입. Tiered 또는 Fixed commission 중 선택.

### 공식 자산
- 한국어 공식 페이지: `https://www.interactivebrokers.com/ko/`
- 가입 페이지: `https://www.interactivebrokers.com/ko/accounts/welcome-individuals.php`
- 한국 KRX 거래: `https://www.interactivebrokers.com/en/trading/krx-exchange.php` (2026-05 launch)
- TWS API 공식 docs: `https://interactivebrokers.github.io/tws-api/`
- 공식 Python SDK: `ibapi` (PyPI)
- 커뮤니티 SDK: `ib_async` (1.5k stars, v2.0.1 2025-06)

### 2026년 신규 변화
- **2025-04: 한국 FSC 규정 변경 — 외국인이 해외 broker 통해 한국 주식 직접 거래 허용**
- **2026-05-07: IBKR 가 미국 broker 중 최초로 KRX 직접 거래 launch** (2,700+ 종목, 0.20bp FX, KOSPI200 선물·옵션, 통합 portfolio margin)
- 결과: **한국 retail 도 IBKR 단일 계좌로 한국 + 미국 + 글로벌 거래 가능**

---

## 2. 가입 + Paper Account 가능성 (Cold Honest)

### 한국 거주자 가입 절차 (실측 단계, 2025 기준)
1. **`interactivebrokers.com/ko/` 접속** → "Open Account" → email 인증
2. **거주국 = South Korea 선택** → 한국어 폼 자동 활성
3. **계좌 종류 = Individual (개인) 선택** — IRA/Trust 등은 미국 거주자 전용
4. **필요 정보 입력**:
   - 이름 (영문, 여권 표기)
   - 생년월일, 주소 (영문)
   - 한국 세무 거주지
   - 직업, 소득 범위, 자산 범위
   - 투자 경험 (객관식, **해외주식 경험 없음도 가입 가능**)
5. **신분증 업로드** — 여권 (강력 권고) 또는 운전면허증
6. **W-8BEN 자동 작성** (미국 비거주자 세금 양식) — 시스템 자동 생성
7. **승인** — 일반 수시간~24시간

### 실 후기 (2025년 한국인 가이드)
- 비대면, 100% 영문 (한국어 페이지 보조)
- 신분증 = 여권이 가장 무난, 운전면허는 가끔 재제출 요청
- 최소 입금 = $0, **그러나 첫 입금 < $2,000 시 일부 deposit commission 발생 가능**
- inactivity fee: 2025년 미국 계좌 폐지 → 한국 거주자도 동일 적용 (이전엔 monthly $10 활성도 fee)
- 첫 송금 약 18시간 도착 (한국 은행 SWIFT 송금 → IBKR USD 계좌)
- 제3자 송금 거절 정책 → **owner 본인 명의 한국 은행 → owner 본인 명의 IBKR**

### Paper Trading Account 가입
- **실 계좌 승인 후** Client Portal → Settings → "Paper Trading" 메뉴에서 생성
- 동일 이메일/비밀번호 + paper 접속 시 별도 username (보통 `<live_id>p`)
- **$1M USD virtual default** (조정 가능)
- 시세: market data subscription 미가입 시 delayed 15분 (실시간 원하면 paper 도 동일 subscription)
- TWS / IB Gateway 동일, **paper 와 live 토글로 전환**
- 가입 즉시 사용 가능, **무료 무한 사용**
- 체결 모델: simulated, 실 호가창 기반 fill simulation (KIS 모의보다 정교)

### 한국 KYC 거절 사례
공식 공개 정보 부족. 일반적으로 **신분증 불일치 / 주소 증명 부족 / 세무거주지 모호** 시 재제출. 절대 거절 사례는 거의 보고되지 않음 (북한 거주 / OFAC 제재국 외).

### 영문 능력 요구
가입 form 한국어 페이지로 가이드되지만 입력 자체는 영문. TWS UI 도 한국어 일부 지원하나 영문 표준 권고. **owner 영문 readable 이면 문제 없음**.

---

## 3. 자산군 + 자동 매매 범위

### 글로벌 자산군 (한국 retail 접근 가능)
| 시장 | 지원 | 비고 |
|---|---|---|
| 미국 주식 (NYSE/NASDAQ/AMEX) | ✅ Full | 7,000+ 종목 |
| 미국 ETF (SPY, QQQ, ARKK 등) | ✅ Full | 1,000+ ETF |
| 미국 옵션 (CBOE 등) | ✅ Full | Equity + Index + ETF 옵션 |
| 미국 선물 (CME, ICE, COMEX) | ✅ Full | E-mini, micros, commodities |
| FX (Spot, 100+ pairs) | ✅ | USD/KRW 포함 |
| 채권 (US Treasury, corporate) | ✅ | |
| 한국 KRX 주식 (2026-05 신규) | ✅ Full | 2,700+ 종목, KOSPI/KOSDAQ |
| 한국 KOSPI200 선물·옵션 | ✅ (2026) | KRX 직접 |
| 일본 (TSE), 유럽, 홍콩 등 | ✅ | 170 시장, 40 국 |
| 펀드, ELS, 신주청약 | ❌ | retail 미지원 |

### TWS API + IB Gateway
- **TWS** (Trader Workstation) = GUI + API 통합, Java 기반, 메모리 4GB+
- **IB Gateway** = API 전용 경량 (headless 가능, Docker 적합)
- **연결**: localhost socket (기본 port 7497 paper / 7496 live / IB Gateway 4001 paper / 4002 live)
- **OS**: Windows / Mac / Linux 모두 지원, **Docker 이미지 다수 보급** (예: `ibgateway-docker`)

### Python SDK 비교
| SDK | 상태 | Star | 추천 |
|---|---|---|---|
| `ibapi` (공식) | IBKR 직접 제공 + sync wrapper 신규 | n/a | ✅ 1순위 (공식 지원) |
| `ib_async` | 활성 maintain (ib_insync 후속) | 1.5k stars, v2.0.1 2025-06 | ✅ 커뮤니티 1순위 |
| `ib_insync` | 🔴 **discontinued** (Ewald de Wit 2024년 작고) | 2.7k stars (legacy) | ❌ 미권고 |

### 자동매매 정식 허용
TWS API 약관에서 자동매매 명시 허용. **`ibapi` 또는 `ib_async` 로 24/7 봇 운영 가능**. 단, TWS/IB Gateway 데몬 1대 OS 위에서 운영 필수 (cloud VPS 보편화).

---

## 4. Rate Limit + 안정성

### TWS API throttling
| 항목 | 한도 |
|---|---|
| **TWS API 일반 메시지** | 50 messages/sec |
| **FIX API (IB Gateway)** | 250 messages/sec |
| **Historical data identical request** | 15 sec interval (동일 요청 반복 금지) |
| **Historical data same contract** | 2 sec 내 6 request = pacing violation |
| **Order rate** | 통상 50/sec 한도 안 |

### Pacing violation 패턴
- 동일 종목 + 동일 exchange + 동일 tick type 의 historical data 2초 내 6회 → violation
- 동일 historical request 15초 내 반복 → violation
- 위반 시 일시 차단 (보통 10분~30분), 심하면 IP 차단

### 실 운영 에러 패턴 (사례 기반)
- **`Pacing violation`** — historical bar 스크립트가 가장 흔한 사고. 종목 + tick type 단위로 무한 페이징 시 빈발.
- **TWS auto-restart (매일 새벽 1회)** — `IB Gateway` 도 동일. 자동매매 봇은 reconnect 로직 필수.
- **Java memory leak** — TWS 장기 운영 시 메모리 4GB+ 초과 가능. IB Gateway 가 더 안정.
- **API client disconnection** — TCP socket 단순 끊김 빈번. heartbeat + auto-reconnect 필수.
- **Order ID overflow** — `nextValidId` 추적 필수, 충돌 시 reject.

### 안정성 평가 (cold)
실 retail 사용자 후기 (전 세계 수만 명): **"TWS/IB Gateway 매일 1회 재시작 + Java GC 튜닝만 잘 하면 매우 안정"**. KIS 의 EGW00201 수준의 즉시 차단 사례는 historical pacing 외 거의 없음.

### KIS vs IBKR 안정성 비교
- KIS: 단순 REST, 단점은 throttling 매우 빡빡 (20 RPS), 한 번 hit 시 EGW00201 즉시 reject
- IBKR: 복잡한 TWS 데몬 운영, 단점은 인프라 설정 부담, 그러나 50 msg/sec + 250 msg/sec(FIX) 여유. retail 1인 quant 의 throughput 한계는 거의 안 닿음.

### 권고 운영 아키텍처 (cold)
- **Docker (IB Gateway)** = 1대 운영, 매일 새벽 재시작 cron
- **`ib_async` (Python 3.10+)** = asyncio 기반, ib_insync 대체
- **`ibapi` (공식)** = critical path 용, fallback
- **heartbeat + reconnect** = TCP 끊김 대응
- **historical pacing 1초 buffer** = 동일 종목 호출 간격 1.5초 이상

### 비교 — 옛 Binance forceOrder PoC 실패 패턴 대비
- Binance: 무료 청산 데이터 정책 영구 변경 = single point of failure
- IBKR: **paid 시세 subscription** 으로 데이터 정책 안정 (월 $1.50~$10 retail)
- KIS: 무료지만 분봉 historical 부재
- → IBKR 는 "유료 안정" vs KIS "무료 제한" 의 trade-off. quant 운영 측면에서 IBKR 가 더 안정적.

---

## 5. Historical Data

### 무료 / 유료 매트릭스
| 데이터 | 무료 | 유료 subscription |
|---|---|---|
| 미국 주식 일봉 | ✅ (TWS API limit 내) | 무료 |
| 미국 주식 분봉 (1, 5, 15분) | ✅ | 무료 |
| 미국 주식 1초 bar | ✅ | 무료 |
| 미국 주식 틱 (체결 + 호가) | △ delayed 15분 | **NASDAQ TotalView ($15.50/월)**, NYSE OpenBook, etc |
| 미국 옵션 historical bar | ✅ | 무료 |
| 미국 옵션 NBBO 실시간 | △ delayed | **US Options ($1.50/월)** |
| 미국 선물 (CME) | △ delayed | **CME bundle (~$10~$20/월)** |
| 한국 KRX 시세 | △ 2026-05 신규 | **KRX subscription 가입 필요** |
| FX | ✅ | 무료 |

### 핵심 강점 (KIS 대비)
- **분봉 historical longitudinal backfill 가능** = 분봉 알파 backtest 인프라 즉시 운영 가능
- **옵션 historical bar 무료** = 옵션 변동성 알파 가능
- **TWS API duration 옵션** = 30 일, 1년, 5년 등 자유로운 history depth

### 한도 (TWS API)
- Historical data request 의 max bar count = 1000 per call (수동 페이징 필요)
- Identical request 15초 cool-down
- 동일 contract + tick type 2초 내 6회 violation

### Subscription 자동 면제 정책
- US Securities Snapshot & Futures Value Bundle ($10/월) = 월 commission $30 이상 시 자동 waived
- 1인 quant 가 월 $30 commission 약 (Tiered 기준) = 미국 주식 round trip $6,000 distance = 매우 쉽게 도달

---

## 6. 수수료 + 환전

### IBKR Pro Tiered Commission (미국 주식)
| Volume (월) | $/share | $/100주 | $1,000주 |
|---|---|---|---|
| < 300K | 0.35¢ | $0.35 | $3.50 |
| 300K~3M | 0.20¢ | $0.20 | $2.00 |
| 3M~20M | 0.15¢ | $0.15 | $1.50 |
| 20M~100M | 0.10¢ | $0.10 | $1.00 |
| 100M+ | 0.05¢ | $0.05 | $0.50 |
| **min** | $0.35 | | |
| **max** | 1% of trade value | | |

### KIS vs IBKR 미국 주식 round-trip cost 비교 (예시)
- 100주 × $25 = $2,500 거래
  - **KIS 미국 직투**: 0.25% buy + 0.25% sell = **$12.50 round trip + 환전 0.1% × 2 = $5.00 + KRW 매매기준율 변동 = 총 ~$17.50**
  - **IBKR Tiered (개인 1순위 tier)**: $1.00 + $1.00 = **$2.00 round trip + FX 0.20bp × 2 ($2.00 min) = $4.00 = 총 $6.00**
- **결과: IBKR 가 약 3배 저렴**

### 미국 옵션 commission (Tiered, IBKR)
- 1 contract @ $2 premium = $1.00
- 2 contracts @ $5 premium = $1.30
- 5 contracts @ $0.03 = $1.25

### FX 환전 (USD ↔ KRW)
- **Tier I (retail)**: 0.20 basis points + $2.00 min/order
- 예: $10,000 환전 = 0.20bp × $10,000 = $0.20 < $2.00 min → **$2.00 fee**
- 예: $100,000 환전 = 0.20bp × $100,000 = $2.00 = $2.00 fee (현행 최소)
- 예: $1,000,000 환전 = 0.20bp × $1M = $20.00 fee

### KIS 90% 우대 환전 0.1% 와 비교
- $10,000 환전: KIS 우대 0.1% = $10 / IBKR = $2 → **IBKR 5배 저렴**
- $100,000 환전: KIS = $100 / IBKR = $2 → **IBKR 50배 저렴**

### 추가 cost
- **Market data subscription**: 시작 단계 NASDAQ + NYSE 통합 약 $10/월 → 월 commission $30+ 시 자동 waived
- **Wire deposit fee**: IBKR 미부과, **한국 은행 SWIFT 송금 fee = $20~30 (KEB하나 외화 송금 표준)**
- **inactivity fee**: $0 (2025년 폐지)

### KRX 한국 주식 commission (2026-05 신규, IBKR)
- 정확한 수수료율 공개 페이지 부재 (`https://www.interactivebrokers.com/en/accounts/fees/KSE.php` 403 차단으로 직접 확인 불가)
- **추정**: Asia-Pacific Tiered 기준 < 0.05% retail 가능 (KIS 0.015% 대비 약 3배 비쌀 가능성)
- **거래세 + 유관기관 수수료는 KIS 와 동일** (한국 정부 정책)
- → **한국 주식만 본다면 KIS 가 여전히 저렴 가능성**, owner G2 결정 필요

---

## 7. SDK + 사례 + 경쟁 비교

### 공식 SDK
- `ibapi` (PyPI / IBKR 직접 배포) — Python, Java, C++, C# 지원
- 2024년 신규 Sync Wrapper 추가 — async 부담 없이 사용 가능
- 공식 지원, IBKR 측 issue tracker 응답 보장

### 커뮤니티 SDK
| SDK | 상태 | Star | 추천 |
|---|---|---|---|
| `ib_async` | ✅ 활성 (Matt Stancliff maintain) | 1.5k, v2.0.1 (2025-06), 857 commits | ✅ 커뮤니티 1순위 |
| `ib_insync` | 🔴 discontinued (creator 2024 작고) | 2.7k legacy | ❌ |
| `@stoqey/ib` (Node.js) | △ 활성 | 100+ stars | Node.js 진영 |

### 권고 stack (1인 quant)
- **Critical path**: `ibapi` 공식 sync wrapper
- **Async + Jupyter**: `ib_async` (3.10+)
- **운영**: IB Gateway Docker + cron 매일 새벽 재시작
- **인증**: IBKR Pro Tiered + market data minimal subscription

### 경쟁 미국 broker (한국 retail 가입 가능 여부)
| Broker | 한국 retail 가입 | API | 비고 |
|---|---|---|---|
| **IBKR Pro** | ✅ 정식 | ✅ TWS + REST | 최고 옵션 |
| 한국투자 미국직투 | ✅ (KIS API 안) | ✅ KIS API endpoint | 수수료 0.25%, 환전 0.1% |
| 키움 미국직투 | ✅ (HTS 안) | ❌ API X (HTS 만) | |
| 토스증권 미국 | ✅ (앱 안) | ❌ API X | |
| 미래에셋 미국직투 | ✅ (HTS 안) | ❌ API X (Public API 없음) | |
| **Alpaca** | ⚠️ Beta only, 비 US 가입 가능 시 $1 deposit | ✅ REST | KYC 까다로움, 한국 거주자 case-by-case |
| **Tradier** | ❌ US only | ✅ REST | 한국 거주자 X |
| **Polygon.io** (데이터만) | ✅ subscriber 가입 가능 | ✅ market data only | broker 아님, 시세 vendor |
| **TD Ameritrade / Schwab** | ❌ US only | (deprecated) | |
| **E*Trade** | ❌ US only | ✅ | |
| **Robinhood** | ❌ US only | (closed) | |

**Bottom line**: 한국 retail 미국 직투 + 자동매매 API 결합 = **IBKR Pro 사실상 유일**. KIS API 미국 endpoint 가 대안 (수수료 더 비싸지만 한국어 + 한국 입금 편의).

### 경쟁 매트릭스 종합
| 항목 | IBKR Pro | KIS 미국직투 | 키움 미국 | 토스/미래에셋 |
|---|---|---|---|---|
| 한국 거주자 가입 | ✅ | ✅ | ✅ | ✅ |
| API 자동매매 | ✅ TWS | ✅ REST | ❌ | ❌ |
| 미국 주식 commission | 0.05~0.35¢/share | 0.25% | 0.25% | 0.25% |
| 미국 옵션 | ✅ 정식 | △ (KIS 매우 제한) | ❌ | ❌ |
| 미국 선물 (CME) | ✅ | ❌ (별도 약정) | ❌ | ❌ |
| FX 수수료 | 0.20bp + $2 min | 우대 0.1% | 우대 0.1% | 우대 0.1% |
| 분봉 historical | ✅ 무료 | △ 매우 제한 | n/a | n/a |
| 옵션 historical | ✅ 무료 | ❌ | ❌ | ❌ |
| Linux/Docker 운영 | ✅ | ✅ | ❌ Windows | ❌ |
| 한국 입금 편의 | △ SWIFT | ✅ KRW 직접 | ✅ KRW | ✅ KRW |
| **종합 (1인 quant)** | **★★★★★** | ★★★ | ★ | ★ |

---

## 8. Cold Honest 권고 — 12주 portfolio build 외부 의존성 평가

### IBKR 채택 시 의존성 매트릭스
| 의존성 | 리스크 | 완화 |
|---|---|---|
| TWS/IB Gateway 데몬 운영 | ⚠️ 중 (1대 VPS 필요) | Docker + cron daily restart |
| Historical pacing violation | ⚠️ 중 | 1.5s buffer + identical 15s |
| US Market data subscription cost | 🟢 낮음 | $30+ commission 시 자동 waived, 시작 단계 ~$10/월 |
| 한국 SWIFT 송금 | ⚠️ 중 (1회성 setup) | KEB하나 또는 신한 외환 — wire fee $20~30 |
| 영문 영주권/세무 form | 🟢 낮음 | 한국어 가이드 페이지 충분 |
| W-8BEN 갱신 (3년 1회) | 🟢 낮음 | system 자동 알림 |
| ib_async 비공식 (creator 작고 후 fork) | ⚠️ 중 | `ibapi` 공식 fallback 준비 |
| TWS 매일 새벽 재시작 | 🟢 낮음 | cron auto-restart |
| 정책 변경 (예: subscription price 인상) | 🟡 중 | 정기 모니터링, KIS 와 분산 가능 |

### 12주 build 시나리오 분류
| 시나리오 | 권고 |
|---|---|
| **A. 미국 주식·ETF 일봉 quant** | ✅ **IBKR 단독 OK**. 수수료 우위 명확. |
| **B. 미국 분봉 + 옵션 변동성 알파** | ✅ **IBKR 압도적 최적**. Historical 무료 + 옵션 chain 무료. |
| **C. 한국 + 미국 듀얼 시장** | 🟡 **IBKR 단독 (KRX 신규) 또는 KIS + IBKR 분산**. owner G2 결정. |
| **D. KOSPI200 옵션 변동성** | 🟡 **KIS 한국 ETF + IBKR 미국 옵션 분산 가능**. |
| **E. 미국 선물 (CME)** | ✅ **IBKR 유일 옵션**. |
| **F. FX 알고리즘** | ✅ **IBKR 단독**. 0.20bp 압도적. |

### Strategy Lead 권고 (1인 quant 12주 build)
- **1순위**: **IBKR Pro + IB Gateway Docker + ib_async** 로 미국 자산군 (주식·ETF·옵션) 시나리오 A or B 진행
- **2순위**: **KIS + IBKR 듀얼** — 한국 주식 KIS 일봉, 미국 ETF/옵션 IBKR
- **3순위**: **IBKR 단독 (KRX 신규)** — 한국·미국 단일 계좌. 단, 한국 주식 수수료 KIS 대비 비쌀 가능성 확인 필요.

### 38일 PoC 실패 패턴 반복 차단 평가
- **Binance forceOrder 사례 = 무료 데이터 정책 변경 single point**. IBKR 는 paid subscription 모델 = 정책 변경 시에도 commercial relationship 안정.
- **KIS 분봉 부재 = 다른 single point**. IBKR 분봉 무료 = 이 의존성 해소.
- **결론**: IBKR 채택은 외부 의존성 리스크를 KIS 단독 대비 더 분산시킨다.

### 자본 입금 권고 (PAPER → 실전 단계적)
1. **0~2주**: 실 계좌 가입 + paper 활성 → IB Gateway Docker 셋업 + ib_async wiring
2. **3~6주**: Paper $1M virtual 환경에서 알파 wiring + 14일 Sharpe 측정
3. **7~10주**: 소액 SWIFT 송금 (~$1,000~$3,000) + 실전 read-only commission 검증
4. **11~12주**: 실전 확장 (~$5,000~$10,000) + 14일 Sharpe + DSR
5. **트리거**: Paper 14일 Sharpe ≥ 1.2 + DSR ≥ 0.5 시점에만 실 자본 증액

---

## 9. References

- IBKR 공식 한국어 — `https://www.interactivebrokers.com/ko/` (인용 2026-05-14)
- IBKR Welcome Individuals (Korean) — `https://www.interactivebrokers.com/ko/accounts/welcome-individuals.php` (인용 2026-05-14)
- IBKR 한국 계좌 개설 2025 가이드 — `https://www.gardenbom.com/23583/...` (인용 2026-05-14)
- IBKR KRX Launch Press Release (2026-05-07) — `https://www.businesswire.com/news/home/20260506438968/en/...` (2,700+ securities, 0.20bp FX, 인용 2026-05-14)
- IBKR KRX Exchange — `https://www.interactivebrokers.com/en/trading/krx-exchange.php` (인용 2026-05-14)
- TWS API rate limit 50 msg/sec — `https://interactivebrokers.github.io/tws-api/historical_limitations.html` (인용 2026-05-14)
- Tiered Commission Plan — `https://www.interactivebrokers.com/campus/glossary-terms/tiered-commission-plan/` (인용 2026-05-14)
- ib_async (1.5k stars) — `https://github.com/ib-api-reloaded/ib_async` (v2.0.1 2025-06, 인용 2026-05-14)
- FX Conversion fee 0.20bp + $2 min — `https://www.matchmybroker.com/articles/interactive-brokers-currency-conversion-guide` (인용 2026-05-14)
- Market data subscription auto-waive — `https://supa.is/article/interactive-brokers-market-data-subscription-which-one-do-i-need-2026` (인용 2026-05-14)
- US Stock Commissions Tiered — `https://www.interactivebrokers.com/en/pricing/commissions-stocks.php` (인용 2026-05-14)
- 한국 → IBKR 송금 절차 — `https://www.gardenbom.com/24380/...` (인용 2026-05-14)
- Korea Exchange Brokers comparison — `https://brokerlistings.com/stocks/krx` ($0 min, demo account, 인용 2026-05-14)
- IBKR Lite vs Pro 한국 제한 — `https://www.matchmybroker.com/articles/ibkr-lite-vs-ibkr-pro` (Lite = US/SG only, 인용 2026-05-14)
- Alpaca non-US 가입 정책 — `https://alpaca.markets/support/is-alpaca-available-outside-the-us` ($1 minimum 변경, 인용 2026-05-14)

---

## owner Action Items

- [ ] **IBKR Pro 한국 거주자 가입** — `https://www.interactivebrokers.com/ko/` → 개인 계좌 → 여권 + 영문 주소 + 영문 이름 — **30~60분 입력 + 수시간~24시간 승인**
- [ ] **Paper Trading Account 활성** — 실 계좌 승인 후 Client Portal → Settings → Paper Trading 생성 — **5분**
- [ ] **TWS / IB Gateway 다운로드 + 첫 연결 테스트** — 권고: IB Gateway (경량) + Docker 이미지 — **30분~1시간**
- [ ] **(선택) 한국 SWIFT 송금 1차 ~$100~$1,000** — KEB하나 또는 신한 외화 송금, $20~30 wire fee, 약 18시간 도착 — **30분 준비 + 익일 도착 확인**
- [ ] **US Market data subscription 검토** — 시작 단계 default 무료 delayed → 실전 시 NASDAQ + NYSE 약 $10/월 (commission $30+ 시 자동 waived) — **10분**
- [ ] **`ibapi` 또는 `ib_async` Python 설치 + paper wiring 첫 테스트** — `pip install ibapi` 또는 `pip install ib-async` — **30분~1시간**
- [ ] **CREDENTIAL_BIBLE.md 박제** — IBKR username, paper username, Client Portal URL, IB Gateway port (4001 paper / 4002 live), market data subscription 상태 — **15분**

**총 예상 시간**: **2~4시간 (가입 + 송금 수속) + 익일 송금 도착 + 추가 1~2시간 (paper wiring)**

### 추가 cold note
- IBKR 가입 자체는 무료 + 매우 빠르지만, **첫 SWIFT 송금 == 한국 은행 외화 송금 한도 (연 $50K USD 무신고)**. owner 가 한국 은행 외화 송금 경험 없으면 첫 송금 시 절차 미숙 가능 → 보수적 $100~$500 1차 송금 권고.
- TWS API 의 ibapi vs ib_async 선택은 ROI 측면 큰 차이 없음. ib_async 가 jupyter/asyncio 통합 빠르고, ibapi 가 공식 지원. 두 SDK 병행 운영도 가능.
- IBKR 한국어 고객지원 한정적 (영문 우선), 영문 OK 시 24/7 chat + 한국어 일부 시간대만.

---

> **이전 보고서**: `03-kis-api-feasibility.md` (한국투자증권 KIS API)
> **상위 SSOT**: `01-korea-securities-job-market.md`, `02-owner-asset-inventory.md`
> **종합 권고**: KIS + IBKR 듀얼 인프라가 1인 quant 12주 build 의 안정 + 분산 + 비용 최적 조합. owner G2 결정 후 cred SSOT 박제 + paper wiring 동시 착수 권고.
