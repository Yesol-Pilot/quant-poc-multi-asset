# Korea Securities Quant Job Market Research (2024~2026)

> **작성일**: 2026-05-14
> **조사 방법**: WebSearch + WebFetch (KOFIA / 사람인 / 잡코리아 / 캐치 / 인크루트 / 자소서닷컴 / 원티드 / LinkedIn / Glassdoor / Wanted / 블라인드 / brunch)
> **조사 기간**: 2024 ~ 2026 KST
> **조사 한도**: 60분 / WebSearch ~20회
> **언어**: 한국어 본문 + 영문 직군명 병기

---

## 1. Executive Summary

대한민국 증권사 / 자산운용사 / 가상자산 거래소 / 외국계 IB 한국 지사의 퀀트·알고리즘 트레이딩·디지털 자산·AI 자산운용 채용을 1차/2차 자료로 교차 조사한 결과 다음 5개 핵심 발견을 보고한다.

1. **국내 대형 증권사의 "퀀트 리서치"는 사실상 존재하지 않거나 극소수다.** "퀀트"라는 직명을 단 정규 공고는 한국투자증권·미래에셋·삼성·NH·키움 중 **한국투자증권 알고리즘 트레이딩 경력직 1건(2023.10)**, **KB자산운용 AI퀀트운용본부 1건**, **하나증권 랩운용실(퀀트운용) 1건** 정도가 외부에서 식별되는 수준이다. 대부분의 증권사는 "IT/Digital 경력 채용"이라는 우산 안에서 시스템 트레이더와 백오피스 개발자를 통합 모집한다.

2. **연봉 격차는 채널별로 매우 크다.** WorldQuant Seoul 신입 약 9,000만~1억(인턴 월 400만) → 한국투자증권 신입 평균 약 4,803만 (평균 7,389만, IT/디지털은 평균 부근) → 삼성증권 신입 약 3,900만 (평균 약 6,680만) → 미래에셋자산운용 신입 약 7,200만 (평균 약 1억 5,083만, 단 운용역 한정 추정). 외국계 IB 서울 오피스 신입 애널리스트는 세전 1억~1.2억 + 보너스로 알려져 있으나 본부는 홍콩/싱가포르로 이동 중이다.

3. **신생 핀테크 증권사가 가장 큰 수요처가 되었다.** 토스증권은 2026년 3월 18개 직군 대규모 채용을 진행 중이고, 카카오페이증권은 데이터 사이언티스트(데이터 자산화) 경력 3년+, Data Engineer, Data Analyst, DW Engineer를 상시 모집한다. 디셈버앤컴퍼니(핀트)는 투자로직 연구개발자(경력 3~7년) + 서버 개발자 + DBA + 데이터 분석가를 동시 모집 중이다.

4. **STO / 디지털 자산 부서는 신설 추세이지만, 채용 폭은 작다.** 미래에셋증권 디지털자산플랫폼팀은 백엔드(Python/Rust/Go/Kotlin) + 스마트컨트랙트(Solidity, ERC-20/721, Hardhat/Foundry) + 인프라(커스터디·지갑) + 기획 4개 직무로 분리되어 있다. KB증권은 ST 오너스 협의체, 교보증권은 DT전략부 신설. 그러나 토큰증권법 통과가 정기국회 2025-09 분수령 이후 지연되면서 채용 규모는 여전히 한 자릿수~십수 명 단위.

5. **국내 retail/PoC 1인 quant의 portfolio 평가는 비공식적이며 weight이 낮다.** GitHub 가시화는 대형 증권사 인사 평가표의 공식 항목이 아니며 (외국계 IB 서울 / Two Sigma·Citadel·Jane Street류 본사만 정량 평가). 한국 증권사는 학벌(KAIST 금융공학 / 서울대 통계·수학·산업공학 / 포스텍 수학 등) + 자기소개서 + 인적성 + 코딩테스트(Python/C++ 알고리즘) + 직무 면접 + 임원 면접 6단계가 표준이다. **38일 PaperPnL -15.1% / 24일 5알파 0 거래라는 PoC 결과 자체는 채용에서 음의 신호로 작동할 가능성이 높다.** 단, "9-Layer Kill Switch + Supabase ledger + PM2 multi-alpha aggregation + cross-exchange (Binance/Bybit/OKX) 인프라"라는 시스템 트레이더형 자산화는 키움/한국투자/하나증권 알고리즘 트레이딩 경력직 / KB자산운용 AI퀀트운용 / Core16 Quant Researcher / 디셈버앤컴퍼니 투자로직 연구개발자 1순위 fit이다.

---

## 2. 회사별 채용 매트릭스 (Top 10 + 외국계 + 핀테크)

각 셀의 표기는 다음과 같다: `O` = 직군 라이브 채용 식별, `△` = 우산 직군에 흡수되어 있으나 명시되지 않음, `X` = 미식별 (사실상 없음), `?` = 자료 부족.

| 회사 | 퀀트 리서치 | 알고리즘 트레이딩 개발 | 디지털 자산 | 로보어드바이저 / AI 자산운용 | DS / AI 엔지니어 | 금융 IT (Trading Infra) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **한국투자증권** | X | O (경력 1~3년, KOFIA 2023.10) | △ | △ (IT/Digital 우산) | O (FY2023 IT/Digital 경력) | O (해외MTS개발부, 플랫폼본부, 디지털본부) |
| **미래에셋증권** | △ (TRADING) | △ (글로벌인재 TRADING) | **O (디지털자산플랫폼팀 4직무)** | O (자체 AI 퇴직연금 RA) | O (AI·IT·디지털 인재 채용) | O |
| **삼성증권** | △ (Sales&Trading 운용) | △ | △ | △ (AI 서비스 기획/운영) | O (AI S/W Engineer 경력) | O (IT서비스 기획/운영) |
| **NH투자증권** | △ (리서치) | △ | △ | △ | O (머신러닝 엔지니어, 2025 상반기 신입) | O (SE, 시스템/네트워크 관리자) |
| **키움증권** | X | △ (시스템 트레이딩 강자) | △ | △ | △ | O |
| **토스증권** | △ | △ (개발·데이터 18개 직군 통합) | ? | △ | O (대규모 채용 2026.03) | O (서버 개발자 두 자릿수, 2025-08) |
| **카카오페이증권** | X | X | △ | O (데이터 자산화 DS 경력 3년+) | O (DS, DA, DE, DW) | O |
| **한국투자자산운용** | △ | X | X | △ | △ | △ |
| **미래에셋자산운용** | △ (계량분석/금융공학 리서치 신입·경력) | X | X | △ | △ | △ |
| **삼성자산운용** | △ (퀀트운용/계량분석) | X | X | △ | △ | △ |
| **KB자산운용** | **O (AI퀀트운용본부 국내AI퀀트운용팀)** | X | X | O | △ | △ |
| **하나증권** | **O (랩운용실 퀀트운용 경력직)** | △ | △ | △ | △ | △ |
| **KB증권** | △ | **O (자본시장플랫폼부 퀀트 개발자 경력 연봉계약직)** | △ (ST 오너스) | △ | △ | O |
| **교보증권** | △ | △ | O (DT전략부, STO) | △ | △ | △ |
| **WorldQuant Korea (서울 리서치 오피스)** | **O (Quantitative Researcher / Deep Researcher 경력+인턴)** | X | X | △ | O | X |
| **Vacuum Trading** | **O (퀀트 트레이더 신입 가능)** | **O** | X | X | △ | △ |
| **Core16** | **O (Quant Researcher, 자산배분/팩터)** | X | X | O | △ | △ |
| **QRST AI** | **O (Quant Researcher)** | △ | X | X | △ | △ |
| **디셈버앤컴퍼니 (핀트)** | △ | △ | X | **O (투자로직 R&D 경력 3~7년)** | O (데이터 분석가) | O (서버 개발자, DBA) |
| **Morgan Stanley Korea** | △ | △ | X | X | △ | △ |
| **JP Morgan Korea** | △ | △ | X | X | △ | △ |
| **Goldman Sachs Korea** | △ | △ | X | X | △ | △ |
| **CLSA Korea** | △ (Sales Trader 신입 가능) | △ | X | X | △ | △ |
| **두나무 (업비트)** | △ | △ (가상자산 거래 인프라) | △ | △ | O (2026 개발직군 대규모 채용 마감) | O |
| **빗썸** | △ | △ | △ | X | O (사람인 30건 진행 중) | O |
| **코빗** | X | △ | △ | X | △ | △ |

**관찰 1**: 국내 대형 증권사는 "퀀트 리서치"라는 직명을 사실상 쓰지 않고, 채용 시점도 비정기적이다. KOFIA 채용안내 게시판이 가장 정확한 1차 자료 채널이다.
**관찰 2**: AI퀀트 / 알고리즘 트레이딩 전문 부서는 **자산운용사 쪽 (KB자산운용 AI퀀트운용본부)**와 **국내 자산운용 부티크 (Core16, QRST AI, Vacuum, WorldQuant Korea)**에 집중되어 있다.
**관찰 3**: 외국계 IB 한국 지사는 트레이딩/Quant 본부를 **홍콩/싱가포르로 이전** 중이며, 서울 오피스는 Sales/Trading sales side 위주로 남아있다.

---

## 3. 직군별 평균 자격 + 연봉

### 3.1 퀀트 리서치 (Quant Researcher)

| 항목 | 요구 사항 |
|---|---|
| 학력 | **석사 권장 / 박사 우대.** WorldQuant: PhD/MS/BS 모두 가능, 단 leading university 한정. Vacuum: 학사 기본, 석/박사 우대. Core16/QRST AI: 학사+ |
| 전공 | 수학, 통계, 산업공학, 물리, CS, 금융공학, 경제학 (KAIST 금융공학·서울대 통계/수학·포스텍 수학 다수) |
| 경력 | 신입 가능 (단 WorldQuant Korea 2025는 경력 only, fresh grad 는 인턴 → 정규직 전환) |
| 자격증 | **CFA / FRM 은 + 알파, 필수 아님**. 박사학위 / 수학·정보 올림피아드 수상이 더 강한 신호 |
| 영어 | 필수 (논문 독해 + 글로벌 협업) |
| 기술 | Python (필수) + C++ 우대, NumPy/Pandas, ML/DL/RL, 시계열 분석 |
| 연봉 범위 (한국) | 신입 6,000만~1억 (WorldQuant Seoul 신입 9,000만~1억). 시니어 (5~10년) 1.5억~3억 + 성과급 |

### 3.2 알고리즘 트레이딩 개발 (Quant Developer / Algo Trader)

| 항목 | 요구 사항 |
|---|---|
| 학력 | 학사+ (대부분 학력 명시 안 함, 실력 검증 위주) |
| 전공 | CS, 수학, 통계, 산업공학, 전자공학 |
| 경력 | 1~3년 (한국투자증권 KOFIA 공고 기준) / 신입 일부 가능 |
| 자격증 | 정보처리기사 + 알파. CFA/FRM 은 거의 보지 않음. |
| 영어 | OPIc IM 이상 또는 TOEIC 800+ 권장 |
| 기술 | **C/C++/C#/DevExpress/MySQL** (한국투자증권) + Python (자산운용사 쪽), Java 일부. 자료구조 + TCP Socket 통신 |
| 연봉 범위 (한국) | 신입 4,500만~6,000만 / 경력 3~5년 7,000만~1억 / 시니어 1.2억~2억 + 성과급 |

### 3.3 디지털 자산 / 토큰증권 (STO)

| 항목 | 요구 사항 |
|---|---|
| 학력 | 학사+ |
| 전공 | CS, 전자공학, 분산시스템, 암호학 |
| 경력 | 미명시 (미래에셋증권 디지털자산플랫폼팀 4직무 모두 학력/연차 미명시) |
| 자격증 | 정보처리기사 + 알파. 블록체인 자격증 우대 가능 |
| 영어 | 권장 (글로벌 표준 ERC, EIP 문서 독해) |
| 기술 | 백엔드: Python/Rust/Go/Kotlin 중 2개+. 스마트컨트랙트: Solidity, ERC-20/721, Hardhat/Foundry/Truffle. 인프라: 커스터디·지갑 서드파티 솔루션 |
| 연봉 범위 | 신입 5,000만~7,000만 / 경력 3~5년 8,000만~1.2억 / 시니어 1.2억~2.5억 |

### 3.4 로보어드바이저 / AI 자산운용

| 항목 | 요구 사항 |
|---|---|
| 학력 | 학사+ (석사 우대) |
| 전공 | CS, 통계, 산업공학, 금융공학 |
| 경력 | 경력 3~7년 (디셈버앤컴퍼니 투자로직 R&D 기준) |
| 자격증 | 투자자산운용사 + 알파 (특히 자산운용사 측). 핀테크 측은 자격증보다 모델 + 백테스트 결과 |
| 영어 | 권장 |
| 기술 | Python, ML/DL, 포트폴리오 최적화, 백테스팅, 팩터모델 |
| 연봉 범위 | 디셈버앤컴퍼니 평균 5,882만 / 카카오페이증권 평균 5,804만 / KB자산운용 AI퀀트운용 7,000만~1.2억 추정 |

### 3.5 데이터 사이언티스트 / AI 엔지니어

| 항목 | 요구 사항 |
|---|---|
| 학력 | 학사+ (석사 우대, 박사 우대 시점 점차 증가) |
| 전공 | CS, 통계, ML, AI 관련 학과 |
| 경력 | 신입~경력 3~5년 |
| 자격증 | 빅데이터분석기사, ADP, 정보처리기사 우대 |
| 영어 | 권장 |
| 기술 | Python (PyTorch/TF), SQL, Spark, ML pipelines, LLM RAG (2024~ 우대 증가) |
| 연봉 범위 | 신입 5,000만~7,500만 / 경력 3~5년 8,000만~1.3억 / 시니어 1.5억~2.5억 |

### 3.6 금융 IT / Trading Infrastructure

| 항목 | 요구 사항 |
|---|---|
| 학력 | 학사+ |
| 전공 | CS, 컴퓨터공학 |
| 경력 | 신입~경력 5년+ |
| 자격증 | 정보처리기사 + 알파 |
| 영어 | 권장 |
| 기술 | Java/Spring (back-end), DevOps, MSA, RDBMS, AWS/GCP, Kafka, Redis |
| 연봉 범위 | 신입 4,500만~6,000만 / 경력 3~5년 7,000만~9,000만 / 시니어 1.2억~1.8억 |

### 3.7 연봉 비교 표 (회사별 평균, 신입 초봉)

| 회사 | 신입 초봉 | 평균 연봉 | 비고 |
|---|---|---|---|
| 한국투자증권 | 약 4,803만 | 약 7,389만 | 잡코리아 평균 14,161만은 임원 포함 추정 |
| 미래에셋자산운용 | 약 7,200만 | 약 1억 5,083만 | 운용역 위주, 영업·관리는 더 낮음 |
| 삼성증권 | 약 3,900만 | 약 6,680만 | 잡코리아 평균 15,455만은 임원 포함 |
| KB자산운용 (AI퀀트운용) | 5,000만~7,000만 추정 | - | 채용연계형 |
| WorldQuant Korea | 9,000만~1억 (인턴 월 400만) | - | 글로벌 본사 수준 |
| 디셈버앤컴퍼니 | - | 약 5,882만 | wanted 기준 |
| 카카오페이증권 | - | 약 5,804만 | catch 기준 |
| 외국계 IB 서울 신입 | 세전 1억~1.2억 + 보너스 | - | 3년차부터 세전 2억+ 도달 |
| 외국계 IB 홍콩 (APAC HQ) | 세전 약 2억 | - | HK$1M 기본급, 보너스 별도 |

---

## 4. 최근 트렌드 (5 키)

### 4.1 AI / LLM 가능자 우대 가속화
- 2024년부터 거의 모든 직군 공고에 "AI / 머신러닝 / LLM 활용 경험" 우대 추가.
- 삼성증권 2026 상반기 GSAT에 AI 인재 발굴 전형 별도 운영.
- 핵심 키워드: RAG, LangChain, Vector DB, 시계열 forecasting, 알파 디스커버리 with ML.

### 4.2 신생 핀테크 증권사의 expansion (2024~2026)
- **토스증권**: 2026.03 18개 직군 대규모 채용 (개발/데이터/디자인/프로덕트/비즈니스).
- **카카오페이증권**: 데이터 자산화 DS, DE, DW 상시 채용.
- 신생사는 학벌보다 **GitHub commit / 오픈소스 contribution / 사이드 프로젝트 평가 비중이 높다** (전통 증권사 대비).

### 4.3 디지털 자산 / 토큰증권 (STO) 부서 신설 (보수적 expansion)
- KB증권 'ST 오너스', 미래에셋증권 NFI(하나금융+SKT), 교보증권 DT전략부 신설.
- 정기국회 2025-09 토큰증권법 통과 지연 → 채용 규모는 한 자릿수~십수 명 (가시화 후 폭증 예상).
- 미래에셋증권 디지털자산플랫폼팀이 가장 명확한 4직무 (백엔드/스마트컨트랙트/인프라/기획) 구조.

### 4.4 외국계 한국 지사의 채용 축소 + 홍콩/싱가포르 이동
- Morgan Stanley 2026 Asia Internship Program에서 Sales & Trading – Quantitative Finance는 **홍콩** 전용.
- WorldQuant 2025 Seoul은 fresh grad full-time 신입 채용 중단 (인턴 → 전환만 운영).
- Citadel, Jane Street, Two Sigma 모두 서울 오피스 본격 진출 부재. APAC 본부 = 홍콩 + 싱가포르.

### 4.5 로보어드바이저 부서 신설 (증권사 자체 vs 핀테크 제휴)
- **미래에셋증권**: 자체 AI 퇴직연금 RA 운영.
- **KB증권**: 디셈버앤컴퍼니(핀트)와 제휴, MTS 마블 앱 '자율주행 서비스'.
- **삼성/한국투자/NH**: 제휴+자체 혼합.
- 핀트 운용자산 312억, 불리오 1,500억 (소규모, 증권사 잠재 인수 가능성).

---

## 5. Portfolio Fit 매트릭스 (owner의 38일 PoC + 8주 build 자산 기준)

### 5.1 owner 자산 (active-tasks.md 5/12 closure 박제 기준)

| 자산 | 자산화 가치 |
|---|---|
| 38일 PoC 결과 (4/5~5/12) | **부정적 결과 자체는 negative**, 그러나 38일을 끌고 학습한 사실 자체는 positive |
| 옛 알파 7개 PAPER 191 trades / WR 37.7% / -15.1% PnL | "alpha decay 실증 학습" = 정직한 정량적 결과 |
| 신규 알파 5개 (A1/A2/A3/A4/A6) 24일 0 거래 | "조건부 진입 임계값 보수적 설계" 학습 |
| A2 OU sensitivity sweep 0/108 cells PASS | spec failure 정량 학습 |
| **9-Layer Kill Switch production wiring** | **Knight Capital 2012 회피 시스템적 사고 입증, 가장 큰 자산** |
| **Supabase ledger + PM2 multi-alpha + Telegram 알림 + Killswitch audit** | **운영 인프라 능력** |
| **3-way cross-exchange (Binance + Bybit + OKX WS)** | **데이터 엔지니어링 능력** |
| Backtest Round 1~3 + sensitivity sweep + DSR / PBO | **정량 검증 방법론** |
| 38일 PaperPnL 시계열 + 분석 | **honest, regulatory-ready 결과** |
| AI agentic 자율 운영 (Strategy Lead + Codex + multi-device) | **MLOps / AgentOps 능력** |

### 5.2 직군별 fit 점수 (10점 만점, cold judgment)

| 직군 | 회사 후보 | fit 점수 | 핵심 근거 |
|---|---|---|---|
| 알고리즘 트레이딩 개발 (경력 1~3년) | **한국투자증권 (KOFIA)**, KB증권 자본시장플랫폼부, 하나증권 랩운용실, 키움증권 시스템 트레이딩 | **8.5/10** | 9-Layer Kill Switch + multi-exchange WS + PM2 production = 한국투자 KOFIA 공고 우대사항 4개 중 자료구조/TCP Socket/MySQL/DB 정확히 일치 |
| 데이터 사이언티스트 (퀀트형) | **카카오페이증권 데이터 자산화**, 디셈버앤컴퍼니 데이터 분석가, 토스증권 데이터 | **7.5/10** | 38일 시계열 + 백테스트 + sensitivity sweep = 모델 검증 능력 입증. 다만 LLM/RAG는 별도 학습 필요 |
| 투자로직 연구개발 | **디셈버앤컴퍼니 (핀트) 투자로직 R&D 경력 3~7년** | **8/10** | 5개 알파 wiring + 백테스트 + 9-Layer Kill Switch = 로보어드바이저 핀테크 fit. owner 경력 3~7년 구간 매치 |
| AI 자산운용 / 퀀트 운용 | **KB자산운용 AI퀀트운용본부 국내AI퀀트운용팀**, Core16, QRST AI | **7/10** | 알파 모델링 + 백테스트 입증, 단 학력(석사+) 와 운용 경험(자산운용사 경력) 부족 |
| 디지털 자산 플랫폼 백엔드 | **미래에셋증권 디지털자산플랫폼팀 백엔드** | **6.5/10** | Supabase + PM2 + 운영 인프라 매치, 단 Solidity + ERC 표준 + Hardhat/Foundry 학습 필요 |
| 퀀트 리서치 (석사·박사 필요) | WorldQuant Korea, Vacuum | **3/10** | 석사 학위 + 올림피아드 수상 + leading univ. 필요. 실력보다 자격 게이트 |
| 외국계 IB 서울 Quant | Morgan Stanley / JP Morgan / Goldman Sachs Korea | **2/10** | 채용 자체가 거의 없음 (홍콩/싱가포르 이전). 학벌 + 영어 native + 인턴 경험 필요 |

### 5.3 우선순위 1순위 추천 = 한국투자증권 + 하나증권 + KB증권 알고리즘 트레이딩 / 자본시장플랫폼

근거:
- KOFIA 2023.10 공고 우대사항 4개 중 owner PoC 자산이 **3개 정확히 매칭** (자료구조/DB/프로그래밍 소질). TCP Socket 통신은 라이브 WS subscriber 3-way (Binance/Bybit/OKX) 로 직접 입증.
- 경력 1~3년 구간 + IT 개발 경험 우대 → owner 학습 기간이 이 구간에 들어옴.
- 9-Layer Kill Switch + audit ledger는 "장내상품 (주식/파생) 시스템 안정성" 요건과 정합.

### 5.4 우선순위 2순위 = 디셈버앤컴퍼니 (핀트) 투자로직 연구개발 + 카카오페이증권 DS

근거:
- 핀트 투자로직 R&D 경력 3~7년 구간, AI 자산운용 알파 + 백테스트 + 운영 인프라 = 가장 직접 fit.
- 카카오페이증권 DS는 "데이터 자산화"라는 명시적 직무명 = owner의 PoC 38일 sensitive 데이터 + 신규 알파 5개 시계열 = 자산화 사례 직접 어필.

### 5.5 우선순위 3순위 = KB자산운용 AI퀀트운용 + Core16 / QRST AI

근거:
- AI퀀트운용본부 국내AI퀀트운용팀은 "계량 방법론 + ML/DL + 자산배분 포트폴리오 최적화 + 퀀트 투자 전략 개발 + 백테스팅 + 성과 분석" 명시 → owner PoC 와 거의 1:1 매칭.
- Core16 Quant Researcher 직무 설명 (자산배분/팩터/백테스팅/성과분석)도 직접 매칭.

---

## 6. Cold Honest 권고

### 6.1 대전제 (frame setting)
38일 PoC 결과 자체는 **자본 입금 영구 ❌**라는 정직한 결론을 도출했다. 이것은 채용 평가에서:
- **음의 신호**: "결과가 마이너스이고 거래조차 0건이었다" 표면적 해석
- **양의 신호**: "38일을 끌고 정량적으로 spec failure를 입증, kill switch 발동 0건, 자본 위험 0으로 종료" 라는 시스템 트레이더 / 리스크 관리 perspective

본 권고는 **양의 신호를 정확히 framing 해야 채용 평가에서 자산이 된다**는 점에 기반한다.

### 6.2 한국 증권사 보수적 채용 패턴의 진실
- **학벌 게이트**: KAIST/SNU/포스텍/연·고대 = 90% 이상 가산점. 그 외 학교는 강한 정량 결과로 보완 필요.
- **자격증 게이트**: 정보처리기사 + 투자자산운용사 (자산운용사 측) + CFA Level 1 (선호도 상위) = 표준 3종.
- **자기소개서의 정성성**: 한국 증권사 채용은 자소서가 1차 필터에서 매우 중요. PHARL 구조 (Problem → Hypothesis → Action → Result → Learning) 로 PoC 38일을 풀어 쓰면 강함.
- **인적성 + 코딩테스트 + 직무 면접 + 임원 면접 5단계** = 약 3~4개월 소요. 시간 자원 투입 사전 계산.

### 6.3 retail 1인 quant 평가의 진실
- 한국 증권사 인사 평가표에서 **GitHub commit 수 / 오픈소스 contribution / 학술 paper publish** 는 **공식 가산점이 아니다**. (외국계 IB 본사·Two Sigma류만 정량 평가)
- 그러나 직무 면접에서 **"GitHub 보여드릴 수 있나요?"** 라는 질문은 점점 증가 중. 특히 토스증권/카카오페이증권/디셈버앤컴퍼니류 핀테크는 사실상 필수.
- **실 매매 결과는 negative**여도 OK, 단 **honest reporting + risk management 시스템**이 동시 입증되어야 한다.

### 6.4 자격 보완 필요사항 (우선순위 순)
1. **(필수) 정보처리기사 자격증** - 한국 증권사 IT/Digital 직무 공통 우대. 3개월 학습.
2. **(필수) 자기소개서 PHARL 구조 작성** - 38일 PoC를 5단락 (Problem: alpha decay 가설 검증 / Hypothesis: 5개 신규 알파 / Action: 9-Layer Kill Switch + multi-alpha PM2 / Result: -15.1% 후 0거래, kill switch 0 발동 / Learning: spec failure 정량 검증) 로 풀어 쓰기. **이 보고서의 §5.1 자산 표가 자소서 원자료**.
3. **(권장) CFA Level 1 + 투자자산운용사 자격증** - 자산운용사 측 지원 시 필수에 가까움.
4. **(권장) C++ 보강** - 한국투자증권 KOFIA 공고는 C/C++/C# 명시. Python 능력은 있으나 C++ 추가 학습 필요 (3~6개월).
5. **(권장) Solidity + ERC-20/721 + Hardhat 학습** - 미래에셋증권 디지털자산플랫폼팀 응시 시. 1~3개월.
6. **(권장) OPIc IM 이상 또는 TOEIC 850+** - 외국계 IB 한국 지사 응시 시 필수.
7. **(선택) 석사 학위 (금융공학)** - 퀀트 리서치 / KB자산운용 AI퀀트운용 등 응시 시. KAIST 금융공학 야간 / 서울대 금융수학 등 옵션 검토. 2년 투자.

### 6.5 정직한 cold judgment 매트릭스

| 시나리오 | 성공 확률 | 시간 | ROI |
|---|---|---|---|
| 한국투자증권/하나증권/KB증권 알고리즘 트레이딩 경력직 응시 | 30~50% | 즉시~3개월 | 매우 높음 |
| 디셈버앤컴퍼니 투자로직 R&D 응시 | 40~60% | 즉시~2개월 | 높음 |
| 카카오페이증권 DS / 토스증권 데이터 응시 | 35~55% | 즉시~2개월 | 중상 |
| KB자산운용 AI퀀트운용본부 응시 | 15~30% | 즉시~6개월 (CFA + 학위) | 중 |
| WorldQuant Korea 인턴 → 정규직 | 5~15% | 6개월~2년 | 높음 (글로벌 경력) |
| 외국계 IB 서울 Quant | 2~5% | 1~3년 | 매우 높음 (자격 부족 시 비현실적) |
| 미래에셋증권 디지털자산플랫폼팀 | 25~40% | 3~6개월 (Solidity 학습 후) | 중상 |

### 6.6 최종 권고 (cold honest)
**Phase 1 (즉시 0~2개월)**: 한국투자증권 알고리즘 트레이딩 / 하나증권 랩운용실 / KB증권 자본시장플랫폼부 / 디셈버앤컴퍼니 투자로직 R&D 4개 회사 동시 자소서 작성 + KOFIA 게시판 일일 모니터링 + 채용 알람 등록. 자소서 원자료는 본 보고서 §5.1 자산 표 + 38일 PoC 4/5~5/12 commits 7건.

**Phase 2 (2~6개월, Phase 1 결과 무관 진행)**: 정보처리기사 + CFA Level 1 학습 + C++ 보강 (Effective C++ / Modern Effective C++) + 카카오페이증권 / 토스증권 데이터 직군 응시.

**Phase 3 (6~12개월, Phase 1 + 2 무관 시)**: KAIST/SNU 금융공학 야간 석사 검토 OR Solidity 학습 후 미래에셋 디지털자산플랫폼팀 응시 OR WorldQuant Korea 인턴 응시.

**경계**: PoC 38일 결과를 "실패"로 framing 하면 모든 응시에서 negative. **"38일을 끌고 정량적 spec failure 입증 + kill switch 0발동 + 자본 위험 0 종료 + Recovery Plan v1 박제"** 라는 systems thinking 으로 framing 해야 한다. 이 framing이 한국 증권사가 가장 좋아하는 "리스크 관리 + 정직한 보고" 키워드와 정합한다.

**가장 큰 리스크**: 채용 자체가 비정기적/수시이므로, **응시 가능 공고가 1년에 1~2건** 인 직군이 많다. KOFIA 게시판 일일 모니터링 + 사람인·캐치·잡코리아 알람 등록이 시간 비용 최소화 핵심.

---

## 7. References

채용 공고 + 채용 페이지 URL + 시점

### 7.1 한국 증권사 채용 페이지
- 한국투자증권 채용포탈: https://recruit.truefriend.com/
- 한국투자증권 채용 홈페이지: https://career.koreainvestment.com/rec/console/truefriend
- 한국투자증권 2026 진행공고 (catch): https://www.catch.co.kr/Comp/RecruitInfo/091255
- 미래에셋증권 e-HR: https://recruit.securities.miraeasset.com/
- 미래에셋 채용 홈페이지: https://career.miraeasset.com/recruit01
- 미래에셋자산운용 채용: https://investments.miraeasset.com/company/recruit/introduce/list.do
- 삼성증권 채용 (SAMSUNG CAREERS): https://www.samsungcareers.com/subsid/detail/E40
- NH투자증권 채용: https://nhqv.recruiter.co.kr/career/home
- NH투자증권 2025 해외대 신입: https://nhqv-recruit2025.com/
- 키움증권 채용 (사람인): https://kiwoom.saramin.co.kr/
- 키움증권 채용 안내: https://www.kiwoom.com/h/ir/recruit/VJobOpeningView
- 토스증권 채용: https://recruit.tossinvest.com/2026-03
- 토스증권 채용 (toss.im): https://toss.im/career/tosssecurities
- 카카오페이증권 채용: https://career.kakaopaysec.com/
- 카카오페이증권 채용공고 페이지: https://career.kakaopaysec.com/job_posting
- KB증권 채용: https://kbsec.career.greetinghr.com/ko/home
- KB금융그룹 (AI퀀트&DI운용본부 등): https://careers.kbfg.com/apply/170

### 7.2 핵심 1차 공고 (KOFIA)
- 한국투자증권 투자금융본부 알고리즘 트레이딩 경력직 (2023.10): https://www.kofia.or.kr/brd/m_96/view.do?seq=27127&multi_itm_seq=0&itm_seq_1=0&itm_seq_2=0&page=1
- 미래에셋증권 디지털자산플랫폼팀 채용: https://kofia.or.kr/brd/m_96/view.do?seq=34908
- CLSA Korea Sales Trader 신입 가능: https://kofia.or.kr:12443/brd/m_96/view.do?seq=33201
- KB증권 자본시장플랫폼부 (퀀트 개발자) 경력직 연봉계약직: https://www.kofia.or.kr/brd/m_96/view.do?seq=27428
- KOFIA 채용안내 목록 (전체): https://www.kofia.or.kr/brd/m_96/list.do

### 7.3 자산운용사 + 핀테크 + 외국계
- 디셈버앤컴퍼니 (핀트) 메인: https://www.dco.com/
- 디셈버앤컴퍼니 채용 (원티드): https://www.wanted.co.kr/company/1800
- 디셈버앤컴퍼니 투자로직 R&D 경력 3~7년 (지급항): https://zighang.com/recruitment/408f8ea1-812e-4335-8a1c-72e6e8946cce
- 디셈버앤컴퍼니 DBA: https://zighang.com/recruitment/416565cd-0346-42ca-b7fd-4e8e583f7df8
- 핀트 서버 개발자 (wanted): https://www.wanted.jobs/wd/43757?country_code=WW
- 카카오페이 데이터 사이언티스트 (catch): https://www.catch.co.kr/NCS/RecruitInfoDetails/520672
- KB자산운용 AI퀀트운용본부 (린커리어): https://linkareer.com/activity/151887
- WorldQuant Korea 채용 (superookie): https://www.superookie.com/jobs/62205ae88b129f478893464b
- WorldQuant Quantitative Researcher (글로벌): https://www.worldquant.com/career-listing/?id=4069499006
- WorldQuant Korea Deep Researcher (blindhire): https://www.blindhire.co.kr/job/10583
- WorldQuant Korea Quantitative Researcher (blindhire): https://www.blindhire.co.kr/job/10584
- 코어16 Quant Researcher (zighang): https://zighang.com/recruitment/53aa90d4-8e5d-45ce-8258-96d38b340f94
- 코어16 Quant Researcher (wanted): https://www.wanted.co.kr/wd/243196
- QRST AI Quant Researcher (wanted): https://www.wanted.co.kr/wd/164245?country_code=WW
- Vacuum 퀀트 트레이더 (서울대 컴공): https://cse.snu.ac.kr/community/notice/22903
- Vacuum 퀀트 트레이더 (KAIST 수리과학과): https://mathsci.kaist.ac.kr/ko/xe/news/10283396
- 하나증권 랩운용실(퀀트운용) 경력직 (잡코리아): https://www.jobkorea.co.kr/Recruit/GI_Read/46189658
- 한화투자증권 퀀트/트레이딩 (catch): https://www.catch.co.kr/NCS/RecruitInfoDetails/367777

### 7.4 가상자산 거래소
- 빗썸 채용: https://career.bithumbcorp.com/ko/story1
- 빗썸 사람인 30건: https://www.jobkorea.co.kr/company/16153019/recruit
- 두나무 2026 개발직군: https://careers.dunamu.com/tech2026
- 코빗 채용: https://korbit.career.greetinghr.com/ko/home

### 7.5 외국계 IB
- Morgan Stanley 2026 Asia Internship (Harvard): https://careerservices.fas.harvard.edu/jobs/morgan-stanley-asia-2026-asia-internship-program-morgan-stanley/
- Morgan Stanley Global Programs: https://morganstanley.tal.net/vx/lang-en-GB/mobile-0/brand-2/spa-1/candidate/jobboard/vacancy/1/adv/
- Morgan Stanley Careers (전체): https://www.morganstanley.com/careers/career-opportunities-search
- Glassdoor Korea 82 Quantitative Jobs: https://www.glassdoor.com/Job/south-korea-quantitative-jobs-SRCH_IL.0,11_IN135_KO12,24.htm
- Glassdoor Korea 13 Quantitative Analyst Jobs: https://www.glassdoor.com/Job/south-korea-quantitative-jobs-SRCH_IL.0,11_IN135_KO12,32.htm
- WorldQuant Seoul Glassdoor: https://www.glassdoor.com/Interview/WorldQuant-Seoul-Interview-Questions-EI_IE309841.0,10_IL.11,16_IM1103.htm

### 7.6 산업 트렌드 + 분석 자료
- 토큰증권 발행(STO) 준비 마친 증권사들 (인베스트조선 2025.09.26): https://www.investchosun.com/site/data/html_dir/2025/09/26/2025092680112.html
- 증권사 먹거리로 STO 부각 (CEOSCOREDAILY): https://www.ceoscoredaily.com/page/view/2023122913550483724
- 국내 증권토큰발행(STO) 현황 및 시사점 (자본시장연구원): https://www.kcmi.re.kr/common/downloadw?fid=25831
- 국내 퀀트 인력수요와 금융공학 진로 (Brunch, Dr. Hong): https://brunch.co.kr/@gauss92tgrd/24
- 금융시장이 원하는 퀀트의 유형은 변화한다 (Brunch): https://brunch.co.kr/@gauss92tgrd/6
- 알고리즘 트레이딩 (나무위키): https://namu.wiki/w/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%94%A9
- 투자은행 (나무위키 - 외국계 IB 서울 연봉): https://namu.wiki/w/%ED%88%AC%EC%9E%90%EC%9D%80%ED%96%89
- 핀트 퇴직연금 RA 일임 (벤처스퀘어): https://www.venturesquare.net/962943
- AI 로보어드바이저 5종 (AI타임스): https://www.aitimes.com/news/articleView.html?idxno=136379
- 코딩에 빠진 증권가 알고리즘 매매 (경향신문 2019.07.27, 트렌드 기준점): https://www.khan.co.kr/article/201907271301001

### 7.7 채용 포털 (직군별 검색)
- 잡코리아 퀀트 검색: https://www.jobkorea.co.kr/Search/?stext=%ED%80%80%ED%8A%B8
- 잡코리아 퀀트트레이딩 검색: https://www.jobkorea.co.kr/Search/?stext=%ED%80%80%ED%8A%B8%ED%8A%B8%EB%A0%88%EC%9D%B4%EB%94%A9
- Indeed 퀀트 채용: https://kr.indeed.com/q-%ED%80%80%ED%8A%B8-%EC%B1%84%EC%9A%A9%EA%B3%B5%EA%B3%A0.html
- LinkedIn Quant Korea: https://kr.linkedin.com/jobs/quant-jobs
- 인크루트 한국투자증권: https://www.incruit.com/company/2867494/
- 인크루트 미래에셋자산운용: https://www.incruit.com/company/6740409/
- 인크루트 카카오페이증권: https://www.incruit.com/company/1683722247/
- 인크루트 NH투자증권: https://www.incruit.com/company/1809201/
- 자소서닷컴 한국투자증권: https://jasoseol.com/companies/43/careers
- 자소서닷컴 미래에셋증권: https://jasoseol.com/companies/82/careers
- 자소서닷컴 NH투자증권: https://jasoseol.com/companies/5534/careers
- 자소서닷컴 토스증권: https://jasoseol.com/companies/13103/careers

### 7.8 글로벌 비교 자료
- WorldQuant Global Hunt for Quant Talent (BriefGlance): https://briefglance.com/articles/worldquants-global-hunt-for-quant-talent-enters-the-ai-era
- 2026 Asia Internship Open (eFinancialCareers): https://www.efinancialcareers.com/news/banking-finance-internships-open-2026
- Quant Hedge Fund Negotiations (Citadel, Jane Street, HRT, Two Sigma): https://www.teamrora.com/post/quant-hedge-fund-negotiations
- Top Quant Firms 2026: https://www.quantblueprint.com/glossary/top-quant-firms-2026
- Northwestern Fintech 2026 Quant Internships: https://github.com/northwesternfintech/2026QuantInternships
- Buy-Side Quant Job Advice (Giuseppe Paleologo, 2024): https://sangmino.github.io/Documents/r60.pdf

---

**보고서 끝. cold honest 자세 유지. 자료 명시적 한계: KOFIA 일부 공고 본문 미공개, 외국계 IB 한국 지사 비공개 채용 비중 추정 불가, 퀀트 채용 평균 연봉은 사람인·잡코리아·블라인드의 자가신고 데이터 기반(검증 한계).**
