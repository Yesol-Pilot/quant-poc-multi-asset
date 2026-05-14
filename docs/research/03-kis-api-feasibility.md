# 03. KIS Developers REST API — Cold Feasibility (한국 retail 1인 quant)

> **조사 시점**: 2026-05-14
> **조사자**: Claude Opus 4.7 (Strategy Lead, agent-mode research)
> **대상**: 한국투자증권 KIS Developers REST + WebSocket API
> **기준**: 38일 PoC 실패 (Binance forceOrder 정책 변경) 교훈 — 외부 의존성 모든 한계 명확히 박제
> **언어 정책**: cold honest, 광고성 표현 회피, 실 운영 에러 패턴 우선

---

## Executive Summary — 5 핵심 발견

1. **REST + WebSocket 정식 지원, Linux/Mac/Docker 운영 가능** — 국내 증권사 중 KIS와 LS증권(구 이베스트)만 OS 독립 REST 제공. 키움/대신/NH/미래에셋은 Windows COM/OCX 종속. 1인 quant 자동화 인프라 측면에서는 사실상 KIS 또는 LS 양자택일.
2. **초당 호출 제한 = 실전 20건 / 모의 5건, 토큰은 1일 1발급 원칙** — 실 운영 사례 (2025년 10월) 70 종목 분봉 수집 시 875% 초과 → 75% 실패율 보고. 동적 배치(batch size 10, delay 1.0s) 적용 후 안정화. WebSocket 동시 구독 한도도 유사 제약. `EGW00201` (초당 거래건수 초과) 가 가장 흔한 에러.
3. **모의투자 = 실 시장 데이터 동일, 그러나 REST 호출 한도가 실전보다 낮음** — owner 본인이 한국투자증권 홈페이지에서 회원가입 후 모의투자 신청 → eFriend Plus HTS에서 모의 비밀번호 발급, 그 후 KIS Developers 포털에서 모의 AppKey/Secret 별도 발급. 모의 한도가 더 낮기 때문에 파라미터 sweep / 스크리너 backtest 는 실전 계좌로 우회 권고가 정설.
4. **Historical 분봉 데이터 = 무료 일봉만 제공, 분봉/틱은 별도 유료 구매** — 백테스트 12주 build 의 가장 큰 외부 의존성 리스크. 일중 분봉(`inquire-time-itemchartprice`)은 당일/최근 일부만, 장기 분봉 backfill 불가. 일봉 + 외부 데이터 보완 설계 필수.
5. **자동매매 정식 허용 (HTS 로그인 불필요)** — 2022년 4월부터 AppKey 인증만으로 REST + WebSocket 주문 가능. 모의·실전 모두 매수/매도/정정/취소 REST API. 이는 토스증권/카카오페이증권/NH·미래에셋(공식 API 자동매매 제한적) 대비 1인 quant 의 사실상 유일한 본격 운영 선택지다.

**Bottom line (cold)**: KIS API 는 한국 retail 1인 quant 의 합리적 1순위지만, **(a) 초당 20건 throttling 을 코드 시작 시점부터 적극 설계해야 하며, (b) 분봉/틱 historical 은 KIS 외부에서 별도 확보**해야 한다. 옛 Binance forceOrder PoC 실패와 동일한 "공식 API 의 데이터 정책 변경" 리스크가 동일하게 존재 (예: 모의계좌 한도 변경, 분봉 endpoint 정책 변경 사례 기록).

---

## 1. Overview — KIS Developers API 기본

### 공식 자산
- 공식 포털: `https://apiportal.koreainvestment.com/`
- 공식 GitHub: `https://github.com/koreainvestment/open-trading-api` (1.4k stars / 726 forks / Python 90.1%, 활성 maintain)
- 24시간 ChatGPT 전용 어시스턴트 제공 (공식)
- 인증: AppKey + AppSecret → access_token (24시간 유효) → REST/WebSocket 호출

### 지원 자산군 (공식)
| 영역 | 지원 |
|---|---|
| 국내주식 (KOSPI/KOSDAQ/KONEX) | ✅ 시세 + 주문 + 잔고 |
| 국내 ETF (KODEX/TIGER/KBSTAR 등) | ✅ 일반 주식과 동일 endpoint |
| 국내 선물·옵션 (KOSPI200 선물·옵션) | ✅ 별도 `domestic-futureoption` namespace |
| 해외주식 (NYSE/NASDAQ/AMEX) | ✅ `overseas-stock` REST + WebSocket |
| 해외 선물·옵션 | ✅ `overseas-futureoption` |
| 장내채권 | ✅ 시세 + 매매 |
| ELS / 펀드 / 신주청약 | ❌ API 미지원 (HTS/MTS 만) |

### 신규성 (2022년 4월 launch)
한국 증권사 최초의 REST 기반 OpenAPI. 이전까지 OCX/COM 기반 Windows 종속에서 cross-platform 가능 환경으로 전환된 분기점이다. Linux/Mac/Docker 운영 가능 ↔ 키움 OpenAPI+(OCX, Windows 전용)와 가장 큰 차이.

---

## 2. 가입 + Paper Account 가능성 (Cold Honest)

### 일반 retail 개인 가입 절차 (실측 단계)
1. **증권 계좌 보유 필수** — 한국투자증권 위탁계좌(주식, 일반 트레이딩) 1개 이상 개설. 모바일 앱 또는 영업점.
2. **홈페이지 회원가입** — `securities.koreainvestment.com` 회원가입 + 공동인증서 또는 SMS 인증.
3. **모의투자 신청** (선택, 그러나 강력 권고) — `securities.koreainvestment.com/main/research/virtual/_static/TF07da010000.jsp` 에서 모의투자 신청 → eFriend Plus HTS 다운로드 후 모의 ID/비밀번호 활성.
4. **KIS Developers 포털 가입** — `apiportal.koreainvestment.com` 별도 회원가입 (증권 ID 와 연동). "API신청" 메뉴에서 실전 AppKey 발급.
5. **모의 AppKey 별도 발급** — 모의투자 계좌가 활성화된 상태에서만 모의용 AppKey/Secret 발급 가능. 실전과 다른 base URL(`openapivts.koreainvestment.com`) 호출.

### 소요 시간 (현실)
- 증권 계좌 개설: 10~30분 (비대면, 본인 확인서류 + 신분증)
- 홈페이지 + KIS Developers 회원가입: 15~30분
- 모의투자 신청 + eFriend HTS 설치: 30분~1시간 (Windows 필요)
- API 신청 → AppKey 발급: 즉시~수 시간 (자동)
- **총 1.5~3시간 (Windows PC 1대 필요)**

### 파생상품 모의거래 사전교육 (G2 주의)
한국투자증권 안내: "일반개인투자자가 파생상품 거래를 하기 위해서는 최저 1시간 이상의 사전교육 + 3시간 이상의 모의거래를 이수해야 한다" (시행일 2025-12-15). **현물 주식/ETF 자동매매는 영향 없음**. 그러나 KOSPI200 선물·옵션 자동매매 계획 시 4시간 사전이수 요건 존재.

### 모의계좌 정확도 (실 시장 대비)
- **시세 데이터**: 실시간 동일 (실 시장 KOSPI/KOSDAQ 데이터 그대로 송출)
- **체결 모델**: simplified — 실 호가창과 별개의 가상 체결 엔진. 슬리피지/큐 위치 모델링 안 됨. 실 시장과 fill rate 차이 존재.
- **취소/정정**: 즉시 fill 가정 → 실 운영의 race condition 검증 못함
- **장중 vs 장후**: 장 시간 외 fill 비정상 가능
- **결론**: 알파 시그널 wiring 검증용으로는 충분. **체결 모델 검증 불가능 → 슬리피지/큐 위치 PoC 는 별도 backtest 인프라 필수**.

### 영문/외국인 retail 가입
공식 KIS Developers 포털은 한국어 only. 외국인 retail 도 한국 증권 계좌 보유 시 가입 가능하지만 절차는 한국어. **owner 한국 거주 한국어 native 가정 시 문제 없음**.

---

## 3. 자산군 + 자동매매 범위

### 한국 주식
- KOSPI/KOSDAQ/KONEX 전 종목 시세 + 주문 가능
- REST 매수/매도/정정/취소 (POST), 잔고/체결내역 조회 (GET)
- 일중분봉(`inquire-time-itemchartprice`) + 일봉(`inquire-daily-itemchartprice`)
- WebSocket 실시간 체결가/호가/잔고 알림

### 한국 ETF
- 일반 주식과 동일 endpoint. KODEX 200, TIGER S&P500 등 모두 거래 가능.

### 한국 선물·옵션
- KOSPI200 선물·옵션 시세 + 주문 가능
- 사전교육 이수 필수 (2025-12-15 시행)
- 별도 위탁 약정 필요

### 미국 직투 (NYSE/NASDAQ/AMEX)
- `overseas-stock` namespace REST + WebSocket
- 매수/매도/예약주문 가능
- 일중분봉 + 일봉 + 실시간 체결가 (overseas WebSocket 별도 토큰)
- **단가 통화: USD, 자동환전 옵션 지원** (통합증거금)

### 자동매매 정식 허용
한국투자증권은 KIS Developers 약관에서 자동매매를 명시적으로 허용한다. AppKey 인증만으로 HTS 로그인 없이 24/7 봇 운영 가능. 이는 키움 OpenAPI+(OCX 라 Windows HTS 로그인 필수)와 큰 차이.

### 단점
- **알고리즘 거래소 등록(Algo) 미요구** = 자동매매 규제 부담은 거의 없으나, 비정상 대량 주문 시 증권사 측 fraud detection 차단 사례 보고.
- **시장조성 (MM) 불가** — retail 계좌는 메이커 리베이트/티커 협상 없음.
- **체결 우선순위** — retail 큐는 기관/외인 큐와 동일하지만 코로케이션 없음. HFT 성격 알파 불가능.

---

## 4. Rate Limit + 안정성

### 공식 throttling
| 항목 | 실전 | 모의 |
|---|---|---|
| 초당 REST 호출 | 20 건 | 5 건 |
| 토큰 발급 | 1분당 1회 + 1일 1발급 원칙 | 동일 |
| Access token 유효 | 24시간 | 24시간 |
| WebSocket 동시 구독 | 41 (실전) / 별도 (모의) | 더 낮음 |

### 실 운영 에러 패턴 (사례 기반)
- **`EGW00201` (초당 거래건수 초과)** — 가장 흔한 에러. 70 종목 분봉 일괄 수집 시 875% 초과 → 75% 실패율 보고된 사례 존재 (tgparkk.github.io 2025-10).
- **`'No close frame received'` WebSocket 끊김** — HTS ID 검증 실패 시 발생. 다중 계좌 동시 연결 시 빈번.
- **token 재발급 spam → 일시 접근 제한** — refresh 로직 무한 루프 시 IP 차단 보고.
- **장 시작 9:00:00 ~ 9:00:30 buffer** — 동시접속 폭주 시 KIS 측 5xx 응답. 봇은 9:00:30 부터 시작 권고.
- **장 중 패치/배포 공지** — KIS 측 임시 서비스 중단 (공지사항 모니터링 필수).

### 안정성 평가 (cold)
실 retail 사용자 후기 종합: "**single 종목 거래 봇은 매우 안정적, 다종목/고빈도는 throttling 적극 설계 필요**". GitHub 의 youhogeon/finance.kis_api (Java) 와 Soju06/python-kis (Python, 274 stars, v2.1.6 2025-10) 모두 자동 retry + rate limiter (Guava 또는 asyncio semaphore) 내장.

### 권고 throttling 아키텍처
- **Guava RateLimiter or asyncio Semaphore** = 15 RPS (20 RPS limit 의 75%, safety margin)
- **EGW00201 감지 후 자동 1초 retry**
- **Token 캐시: 1 access_token / 24h, refresh 만료 1시간 전 사전 발급**
- **WebSocket 다중 계좌 분산** (한 계좌 41 구독 한도 회피)
- **장 시작 30초 buffer**

### 비교 — 옛 Binance forceOrder PoC 실패 패턴 대비
- Binance 는 무료 청산 데이터 정책 영구 변경 (1/sec snapshot) → 데이터 부족으로 알파 fail
- KIS 는 **무료 분봉 historical 데이터 자체가 처음부터 제한적** (당일 위주). 이를 모르고 12주 build 시작하면 동일 패턴 반복 위험.

---

## 5. Historical OHLCV 데이터

### 무료 제공 범위
| 데이터 | 무료 제공 | 한도 |
|---|---|---|
| 한국 주식 일봉 | ✅ 무제한 (`inquire-daily-itemchartprice`) | 100개 row/호출, 페이징 |
| 한국 주식 일중분봉 (1분~30분) | ✅ 당일 + 일부 과거 | 매우 제한적 |
| 한국 주식 틱 (체결가) | ❌ 별도 유료 구매 |
| 미국 직투 일봉 | ✅ 무제한 (`overseas-price/v1/quotations/dailyprice`) | 100개 row/호출 |
| 미국 직투 분봉 | ✅ 당일 + 일부 | 제한적 |
| 미국 직투 틱 | ❌ 별도 유료 |
| 한국 ETF 일봉 | ✅ 일반 주식 endpoint | 동일 |
| 옵션 historical | ❌ 별도 유료 |

### 핵심 한계
- **분봉/틱 longitudinal backfill 부재** — 한국 증권사 retail API 공통 한계. 분봉 시계열 기반 알파 (예: VWAP 회귀, intraday momentum) backtest 는 외부 데이터 (KOREA Stock Exchange의 데이터마트, FnGuide, 또는 데이터 vendor 유료) 필수.
- **호출 횟수 자체는 무제한** — 단, 초당 20건/모의 5건 throttling 으로 실 효 throughput 제약. 5000 종목 일봉 1년치 = 약 1주일 분량 호출 시간.

### 12주 portfolio build 시 영향
- **일봉/주봉 알파** = 100% 가능 (모멘텀, 평균회귀, 페어트레이딩, 듀얼모멘텀 등)
- **분봉 알파** = backfill 인프라 외부 의존성 추가 필요 (Kiwoom MoneyMarket 데이터, FnGuide DataGuide, 또는 owner 본인의 KIS 데이터 매일 누적 수집 → 12주 → 약 2.5개월 데이터 확보)
- **틱/호가창 알파** = 사실상 불가능 (KIS retail 범위 밖)

---

## 6. 수수료 + 환전

### 한국 주식 거래 수수료 (한국투자증권 retail)
- **온라인 매매**: 0.014989% (KIS API 자체 = 한국투자증권 온라인 동일)
- **거래세**: 코스피 0.15% (매도 시), 코스닥 0.18%
- **유관기관 수수료**: 0.0036396% (한국거래소 + 예탁결제원 등)
- **소형주/뱅키스/이벤트별** 추가 우대 가능

### 미국 직투 수수료
- **0.25% (매수/매도 각각)** = 한국 retail 표준
- **최소 수수료**: 보통 USD 0.01/주
- **신규/휴면 고객 3개월 면제 이벤트** 상시 진행

### 환전 (USD ↔ KRW)
- **표준 환전 스프레드**: 매매기준율 ± 1% (즉 1.0%)
- **한국투자증권 우대**: 90% 우대 → 스프레드 **0.1%** (해외주식 거래 신청 시)
- **자동환전 (통합증거금)**: USD 잔고 부족 시 KRW 잔고 자동 차감 후 환전 → 미국 주식 매수
- **우대 기간**: 해외주식 거래 신청일로부터 12개월 자동 연장

### 옛 PoC 대비 cost 평가
- Binance taker 수수료 0.04% vs KIS 한국 주식 0.015% + 거래세 0.15% (매도만) → KIS 가 비싸지만 **세금 포함 후 net 비교 시 미국 주식은 IBKR 이 훨씬 저렴**.
- 미국 직투 0.25% (편도) = round trip 0.5% → quant strategy 의 alpha 가 0.5% 이상 명확하지 않으면 KIS 미국 직투는 비효율.

---

## 7. SDK + 사례 + 경쟁 비교

### 공식 SDK (한국투자증권 / koreainvestment GitHub)
- `koreainvestment/open-trading-api` — **1.4k stars, 726 forks**, Python 90.1%
- examples_llm/ — 단일 API 함수 (LLM 친화)
- examples_user/ — 상품별 통합 자동매매 예제
- 모의/실전 별도 AppKey 분리 설정 지원
- strategy_builder, backtester, MCP 통합 도구 포함
- 한국어 + 일부 영문 주석

### 비공식 (커뮤니티) Python SDK
| Repo | Star | 활성 | 특징 |
|---|---|---|---|
| `Soju06/python-kis` | 274 | v2.1.6 (2025-10), 304 commits | 타입 힌트 완벽, WebSocket 자동 재연결, 국내·해외 unified API |
| `koreainvestment/open-trading-api` | 1.4k | active | 공식, 폭넓은 예제 |
| `softyoungha/kis-client` | 소형 | 2024 | 경량 wrapper |
| `youhogeon/finance.kis_api` | 소형 | Java | Java 진영 |
| `devngho/kt_kisopenapi` | 소형 | Kotlin/Java | mobile, JVM |
| `seokhoonj/kisopenapi` | 소형 | R | 통계 분석 |

### 권고 stack
- **신규 1인 quant**: 공식 `koreainvestment/open-trading-api` + Python 3.11+
- **타입 힌트 + 자동완성 선호**: `Soju06/python-kis` (한국·해외 unified)
- **Java/Spring**: `youhogeon/finance.kis_api` + Guava RateLimiter 패턴

### 경쟁 API 비교 매트릭스 (한국 증권사)

| 항목 | KIS (한국투자) | 키움 OpenAPI+ | LS증권 (구 이베스트) | NH투자 | 토스/카카오페이 |
|---|---|---|---|---|---|
| **API 방식** | REST + WS | OCX (Windows COM) | REST + WS | 부분 REST | 미공개 (없음) |
| **OS** | 모두 (Linux/Mac/Docker) | Windows only | 모두 | Windows 중심 | n/a |
| **자동매매 허용** | ✅ 공식 | ✅ 공식 (HTS 로그인 필요) | ✅ | △ 제한적 | ❌ |
| **모의투자 API** | ✅ 별도 AppKey | ✅ | ✅ | △ | ❌ |
| **수수료 (한국주식 온라인)** | 0.015% | 0.015% (이벤트시 0.011%) | 0.015% (전통 강자) | 0.015% | 0.015% (단 거래세 동일) |
| **미국주식 API** | ✅ 정식 | ❌ (OpenAPI+ 미국 미지원) | △ | ❌ | ❌ |
| **launch 시점** | 2022-04 (한국 최초 REST) | 2007 | 2024-? (후발) | 2014 | 없음 |
| **자료 + 커뮤니티** | ★★★★★ | ★★★★ | ★★ | ★★ | n/a |
| **1인 quant 적합성** | **★★★★★** | ★★★★ (Windows 종속만 OK 시) | ★★★ | ★★ | ★ |
| **Linux/Mac 운영** | ✅ | ❌ | ✅ | ❌ | n/a |
| **공식 GitHub** | 1.4k stars | 없음 (외부 wrapper 의존) | 신규 | 없음 | n/a |

**Cold conclusion**: 한국 retail 1인 quant 에 대해 **KIS 가 사실상 압도적 1순위**, **LS증권이 신규 2순위 옵션** (후발이라 자료 부족), **키움은 Windows 운영 OK 시 차순위**. 토스/카카오페이는 API 자체 부재.

---

## 8. Cold Honest 권고 — 12주 portfolio build 외부 의존성 평가

### KIS 채택 시 의존성 매트릭스
| 의존성 | 리스크 | 완화 |
|---|---|---|
| 초당 20건 throttling | ⚠️ 중 (다종목 시 즉시 hit) | Guava RateLimiter 15 RPS + 동적 batch |
| 분봉 historical 부재 | 🔴 높음 (분봉 알파 시 12주 내 backfill 불가) | 일봉 위주 알파 OR 외부 데이터 vendor OR 매일 누적 수집 |
| 모의 한도 더 낮음 | ⚠️ 중 (sweep 시 실전 강제) | 실전 계좌로 read-only 시세 sweep 운영 |
| 토큰 1일 1발급 정책 | 🟢 낮음 | refresh 만료 1시간 전 사전 발급, 단일 token 캐시 |
| 모의 체결 모델 단순화 | 🔴 높음 (슬리피지 검증 불가) | 별도 backtest 인프라 + paper → 소액 실전 단계적 |
| WebSocket 41 구독 한도 | ⚠️ 중 (전종목 모니터링 불가) | 멀티 계좌 또는 핵심 종목 화이트리스트 |
| 미국 직투 수수료 0.5% RT | 🔴 높음 (alpha < 0.5% 무의미) | 미국 직투는 IBKR 권고 (영역 04 참조) |
| KIS 정책 변경 (분봉 endpoint 등) | ⚠️ 중 (Binance 패턴 반복) | API 변경 공지 모니터링 + alpha 결합 분산 |

### 12주 build 시나리오 분류
| 시나리오 | 권고 |
|---|---|
| **A. 한국 주식 일봉 모멘텀/평균회귀 1인 quant** | ✅ **KIS 단독 OK**. 외부 의존성 최소. 12주 충분. |
| **B. 한국 분봉 momentum/microstructure** | 🔴 **외부 데이터 추가 필수**. KIS 분봉 부재. 12주 backfill 시 데이터만으로 4주 소요. |
| **C. 한국 + 미국 ETF 듀얼모멘텀** | 🟡 **KIS + IBKR 듀얼 권고**. 한국 일봉 KIS, 미국 ETF IBKR (수수료/환전 우위). |
| **D. KOSPI200 옵션 변동성 알파** | 🟡 **KIS 옵션 endpoint 가능, 그러나 사전교육 4시간 + 옵션 historical 유료**. |
| **E. 한국·미국 양시장 펀더멘털 quant** | 🟡 **KIS + IBKR + 외부 fundamentals (FnGuide, Compustat 등)**. |

### Strategy Lead 권고 (1인 quant 12주 build)
- **1순위 선택**: **시나리오 A** (한국 주식 일봉 + ETF), KIS 단독, **외부 의존성 최소화 안전**. 38일 PoC 의 "외부 정책 변경 single point of failure" 반복 방지에 최적.
- **2순위 선택**: **시나리오 C** (KIS 한국 + IBKR 미국 ETF), 분산 + 미국 직투 비용 최적화. 단, IBKR 가입 추가 필요 (영역 04 참조).
- **금기**: 시나리오 B (분봉) 단독 진행. 분봉 데이터 backfill 인프라 별도 4~6주 추가 필요 → 12주 build 못 끝남.

### 자본 입금 권고 (PAPER → 실전 단계적)
1. **0~4주**: 모의계좌 + 실전 read-only AppKey (시세만), 일봉 알파 wiring + paper 매매
2. **5~8주**: 소액 실전 (100~300만원), KIS 실 fill 검증, 슬리피지 측정
3. **9~12주**: 실전 확장 (300만~1000만원), 14일 Sharpe + DSR 측정
4. **트리거**: 14일 paper Sharpe ≥ 1.2 + DSR ≥ 0.5 시점에만 실 자본 증액

---

## 9. References

- KIS Developers 공식 포털 — `https://apiportal.koreainvestment.com/` (인용 2026-05-14)
- 이용안내 — `https://apiportal.koreainvestment.com/howto-use` (인용 2026-05-14)
- 공식 GitHub — `https://github.com/koreainvestment/open-trading-api` (1.4k stars, Python 90.1%, 인용 2026-05-14)
- Soju06/python-kis — `https://github.com/Soju06/python-kis` (v2.1.6 2025-10, 274 stars, 인용 2026-05-14)
- 초당 20건 제한 실 운영 사례 — `https://tgparkk.github.io/robotrader/2025/10/09/robotrader-1-70stocks-problem.html` (875% 초과 → 75% 실패, 인용 2026-05-14)
- 쓰로틀링 구현 사례 — `https://hky035.github.io/web/kis-api-throttling/` (Guava RateLimiter, EGW00201, 인용 2026-05-14)
- 모의투자 안내 — `https://securities.koreainvestment.com/main/research/virtual/_static/TF07da010000.jsp` (인용 2026-05-14)
- 한국투자증권 수수료 — `https://securities.koreainvestment.com/main/customer/guide/_static/TF04ae010000.jsp` (인용 2026-05-14)
- 환전 우대 90% — `https://attention99.com/entry/한국투자증권-미국-주식-수수료` (인용 2026-05-14)
- 증권사 별 API 비교 — `https://mg.jnomy.com/whatis-diff-stock-open-api` (인용 2026-05-14)
- 퀀티랩 블로그 — `https://blog.quantylab.com/htsapi.html` (인용 2026-05-14)
- 한국 알고리즘 트레이딩 위키북 — `https://wikidocs.net/book/7845` (인용 2026-05-14)
- LS증권 OPEN API — `https://openapi.ls-sec.co.kr/intro` (인용 2026-05-14)

---

## owner Action Items

- [ ] **한국투자증권 위탁계좌 (주식 일반) 개설** — 모바일 앱 비대면 약 10~30분 (기존 보유 시 skip)
- [ ] **한국투자증권 홈페이지 회원가입 + 모의투자 신청** — `securities.koreainvestment.com` → 모의 ID/비밀번호 발급 — 30분~1시간 (Windows + eFriend Plus HTS 다운로드 필요)
- [ ] **KIS Developers 포털 회원가입** — `apiportal.koreainvestment.com` → API신청 → 실전 AppKey + Secret 발급 — 15~30분
- [ ] **모의 AppKey 별도 발급** — 모의투자 활성 후 KIS Developers 포털에서 모의용 AppKey 추가 발급 — 15분
- [ ] **CREDENTIAL_BIBLE.md 박제** — 실전/모의 AppKey, AppSecret, base URL 2개 (`openapi.koreainvestment.com:9443` 실전, `openapivts.koreainvestment.com:29443` 모의) 등록
- [ ] **(선택) 미국 직투 신청** — 한국투자증권 미국주식 거래 신청 → 환전우대 90% + KIS API 해외주식 endpoint 활성 — 30분

**총 예상 시간**: **2~3시간** (Windows PC 1대, 신분증, 공동인증서 또는 휴대폰 본인인증)

---

> **다음 보고서**: `04-ibkr-korea-feasibility.md` (Interactive Brokers Korea 동일 cold honest 평가)
> **상위 SSOT**: `01-korea-securities-job-market.md`, `02-owner-asset-inventory.md`
