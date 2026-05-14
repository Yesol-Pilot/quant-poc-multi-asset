# 한국 retail 1인 quant + Open Source publish + 학술 paper + 증권사 입사
# 법적 / 회사 compliance 심층 조사 v1

> **조사일**: 2026-05-14
> **조사자**: Strategy Lead Claude Opus 4.7 (자율 G1 research)
> **owner**: 허예솔 (Yesol-Pilot)
> **scope**: portfolio build (12주) → Open Source publish → arXiv paper → 증권사/핀테크 입사
> **자본**: 1,000~8,000만원 자기 자본
> **target 회사**: 토스증권 / 카카오페이증권 / 빗썸 / 토스뱅크 / 카카오뱅크 / 뱅크샐러드 / 뤼튼 / 에이블리 / 채널톡
> **cold honest 기준**: 광고성 좋은말 X, 회색지대 / 회사별 정책 차이 / 38일 PoC 패턴 반복 차단

---

## Executive Summary — 5 핵심 발견 (cold honest)

### 발견 1: 자기자본 자동매매 합법, 단 외부 판매/조언 시 형사처벌

자기 자본으로 자기 알고리즘으로 API 자동매매하는 행위는 자본시장법상 **투자자문업/투자일임업 미해당**. 인천지방법원 2017노1649 판결 + 금감원 유권해석 일관. 그러나 동일 코드를 **타인에게 판매/대여/리딩**하는 순간 (a) 유사투자자문업 미신고 시 1천만원 이하 과태료, (b) 개별성 있는 조언 시 미등록 투자자문업 = **3년 이하 징역 또는 1억원 이하 벌금**.

→ 결론: **GitHub Open Source 공개는 안전 boundary 안 (educational + no individualized advice)**. 단 monetization (SaaS / 구독 / paid signal) 시도 시 즉시 진입.

### 발견 2: IBKR Korea Exchange equity = 한국 거주자 **사용 불가**

IBKR가 2026.5.7 KRX equity 접속 launch 했으나 공식 정책: "**Access to equities on the Korea Exchange through Interactive Brokers is not available to residents of Korea**". 또한 외국환거래법 7-33조 4항: 거주자는 국내 투자중개업자 통해서만 외화증권 매매 가능. 2023.6 금감원: 거주자가 해외 broker 직접 사용 시 **외국환거래법 위반 소지**, 과태료 행정처분.

→ 결론: 직전 04-ibkr-korea-feasibility.md 결론 **재검증 필요**. IBKR 직접 사용 = **legal grey zone**, KIS Developers / 키움 OpenAPI+ 같은 국내 증권사 API 가 안전 대안.

### 발견 3: 한국 가상자산 양도소득세 = 2027.1.1 시행 (3번째 유예)

2024.12 소득세법 개정으로 2027.1.1 이후 양도분부터 22% (기타소득 20% + 지방소득세 2%), 250만원 기본공제 분리과세. PAPER 모드 (가상거래) = 법적 무관. LIVE 전환 시 (a) 250만원 초과 수익 22% 과세, (b) 2027 시행 시점까지 비과세 (사실상 무한 차익 보호 기간), (c) 거래소 신고 자동, 개인 신고 불필요.

→ 결론: 2026~2027 portfolio build = **세제 가장 유리한 시기**.

### 발견 4: 증권사 입사 시 개인 매매 = 사전승인 + 단일계좌 + 6개월 단기차익 반환

금융투자협회 표준내부통제기준 (강제 적용):
- 본인 실명 단일계좌만 사용 (회사 신고 1개)
- **준법감시인 사전승인 필수** (유효기간 2영업일)
- 분기별 (일반 직원) / **월별** (투자권유자문/조사분석/투자운용인력) 회사 통지
- **6개월 내 매매 시 단기매매차익 반환 의무** (자본시장법 172조)
- 자사주 / 거래제한 대상목록 매매금지

→ 결론: **PM / Data Analyst** (투자권유자문인력 아님) = 분기 통지 + 사전승인. **Quant 부서** (투자운용인력) = 월별 + 사실상 매매 어려움. **빗썸** = 임직원 전면 거래금지 (2021.7 서약서). **카카오페이증권 / 토스증권** 정책 공개 안 됨, 면접 시 직접 확인 필요.

### 발견 5: GitHub Open Source IP = 업무 무관 + 본인 자원 시 본인 소유 (저작권법 9조 + 직무발명법)

대법원 2021다236111: 업무상 저작물 인정 위해 사용자의 **명시적 또는 묵시적 기획** 필요. 단순히 직원이 만들었다는 사실만으로는 회사 소유 X. 휴일 + 본인 컴퓨터 + 회사 업무 무관 = 본인 소유. 단:
- (a) 회사 취업규칙 / 근무규정에 "사전예약승계" 조항 있을 시 권리 자동 회사 이전 (직무발명진흥법 10조)
- (b) 회사 업무 범위 (예: 이트라이브 AI R&D 가 quant 와 무관함 명시 필요)
- (c) 입사 시 회사 IP 가 GitHub 에 포함 안 됨을 lawyer-reviewed 확인 권장

→ 결론: **입사 전 GitHub repo (1인 retail quant) 유지 가능**. 단 입사 후 회사 IP / non-public 정보 commit 절대 금지. 회사별 사이드 프로젝트 정책 입사 전 명시 확인 의무.

---

# Section 1: 자기자본 API 자동 매매 합법성

## 1.1 자본시장법 핵심 조항

### 투자자문업 / 투자일임업 정의 (자본시장법 6조)
- **투자자문업**: 금융투자상품 가치 / 매매판단 관련 자문 제공 (개별성 핵심)
- **투자일임업**: 투자자로부터 매매 권한 위임받아 운용 (타인 자본)
- **유사투자자문업**: 불특정다수 대상 일방향 매매 조언 (신고 의무)

### 자기 자본 자동매매 = 셋 다 미해당

금융위 유권해석 (case 2da7fcc676):
> "고객이 직접 매매종목, 수량, 가격 및 시기를 지정하고 그 지정한 조건을 충족하는 경우 자동으로 주문만 실행해 주는 주문시스템 제공 행위는 자본시장법상 투자자문업이나 투자일임업에 해당되지 않습니다."

자기 자본 운용 자동매매:
- 자문 받는 대상 = 본인 (외부 X)
- 매매 권한 위임 = 본인 → 본인 (위임 자체 미성립)
- 불특정다수 조언 = X (본인 알고리즘)

## 1.2 인천지방법원 2017노1649 판결 (자동매매 프로그램 판매)

**핵심 판시**:
> "주식 자동매매프로그램을 판매·대여하면서 단순히 기본·권장 설정값을 제공한 경우, 개별 사용자의 투자목적·경험 등 개별성이 반영되지 않았다면 투자자문업에 해당하지 않으며, 유사투자자문업에 불과하다."

**의미**:
- 자동매매 프로그램 판매 자체 = 형사처벌 X (무죄 판결)
- 단, **불특정다수 판매 = 유사투자자문업 신고 의무** (1천만원 과태료)
- **개별 사용자 맞춤 조언 시 = 투자자문업 인가 의무** (3년 이하 징역 / 1억 벌금)

## 1.3 자기자본 15억 일임투자업 진입 장벽 — 검증

owner 가 인지한 "자기자본 15억" = **잘못된 정보**. 실제 2025 개정:
- 투자자문업 자기자본 1억 / 2억 5천만원
- 투자일임업 자기자본 14억 → **7억으로 완화** (2025 개정)

→ retail 1인 quant 는 일임투자업 등록 불요 (자기자본 운용이므로). 7억 진입 장벽은 **타인 자본 받을 때**만 적용.

## 1.4 한국 retail 자기 자본 자동매매 사례

- KIS Developers (한국투자증권 공식 GitHub) — 개인 자동매매 라이브러리 제공
- 키움 OpenAPI+ — 알고리즘 계좌 등록 가능 (KRX 등록)
- 다수 GitHub 한국 개인 quant repo (python-kis / kt_kisopenapi / eFriendPy 등)

법적 위험 0 (개인 자기자본 사용 한정).

## 1.5 IBKR / 해외 broker 자동매매 = **legal grey zone**

### IBKR Korea 정책 (2026.5.7 공식)
> "Access to equities on the Korea Exchange through Interactive Brokers is not available to residents of Korea"

### 외국환거래법 7-33조 4항
> "기관투자자 이외의 일반투자자가 외화증권을 매매하고자 하는 경우에는 투자중개업자를 통하여 외화증권의 매매를 위탁하여야 한다."

### 2023.6 금감원 공지
> "국내 거주자가 해외상장주식을 해외중개사 통해 매매하고 대금을 해외에 두면 외국환거래법 위반 소지가 있다."

### 처벌
외국환거래법 15조 위반 = 과태료 행정처분 (자진신고 시 감경).

### 권고
- 미국 주식 trading = 키움 / 한국투자증권 / 미래에셋 의 해외주식 계좌 (국내 broker 경유) 사용
- IBKR 사용 시 (a) 연간 $50,000 초과 송금 한국은행 사전 신고, (b) 매매 대금 국내 송환, (c) 외국환거래법 위반 위험 그대로 잔존
- portfolio build 단계 = **국내 broker 사용 강력 권고**, IBKR 는 비상 옵션

## 1.6 신고 / 거래세 / 양도세 (한국 주식)

- 국내 주식 retail 1인 자동매매 = 별도 신고 불요
- 거래세 0.18% (코스피) / 0.20% (코스닥) 자동 원천징수
- 양도소득세: 대주주 (10억 이상) 만 적용. retail 1인 = 비과세
- KRX 알고리즘 계좌 등록 = **HFT (고빈도)만 의무**, retail 1인 시스템트레이딩 미해당

---

# Section 2: 한국 가상자산이용자보호법 (2024.7~)

## 2.1 법 개요

- **법명**: 가상자산 이용자 보호 등에 관한 법률 (약칭: 가상자산이용자보호법)
- **시행일**: 2024.7.19
- **주요 규제**:
  - 가상자산사업자 (거래소) 인가 의무 (특금법 + 본 법)
  - 이용자 예치금 / 가상자산 분리 보호
  - 시세조종 / 부정거래 / 미공개정보 이용 금지 (자본시장법 unfair trading 과 유사 구조)
  - 위반 시 **1년 이상 징역 또는 부당이득 3~5배 벌금**

## 2.2 retail 1인 영향 범위

### 일반 retail 거래 (Upbit / Bithumb / Coinone 등) = **합법, 변동 없음**
- 개인 자기자본 매매 = 사업자 신고 의무 X (사업자 = 거래소, 개인 X)
- API 자동매매 (Upbit Open API 등) = 합법 (자기 자본 한정)

### 해외 거래소 (Binance / Bybit / OKX) = **사용 가능, 단 미신고 사업자**

금융위 공지 (2025): 미신고 가상자산사업자 리스트에 **Binance / Bybit / OKX 포함**. 단:
- **이용 자체 = retail 처벌 대상 X** (사업자 처벌 vs 이용자 처벌 구분)
- 단, (a) 외국환거래법 위반 소지 (자금 해외 보유 시), (b) 향후 정책 변경 시 차단 가능성, (c) FATCA / CRS 자동 정보교환으로 국세청 인지 가능

### 처벌 (사업자 한정)
- 미신고 사업자 영업 = 5년 이하 징역 또는 5천만원 벌금
- retail 이용자는 **직접 처벌 X**, 단 자금 회수 불가능 위험

## 2.3 crypto API 자동매매 적용

### 한국 Upbit / Bithumb API
- 공식 Open API 제공
- 자기자본 자동매매 합법
- 임직원이 외부 GitHub 에 자체 봇 코드 공개 = 합법 (educational)

### 해외 Binance / Bybit / OKX API
- 38일 PoC 사용 사례 = PAPER 모드 (가상자본, 법적 무관)
- LIVE 전환 시:
  - (a) 한국→해외 송금 = 외국환거래법 신고 의무 (USD 5만 이상 / 연 누적)
  - (b) 미신고 사업자 이용 = 본인 책임 (정책 변경 시 자금 동결 위험)
  - (c) 2027 양도세 시행 후 = 미신고 거래소 거래 손익 신고 의무 불명확 (현 기준 자료 부족)

## 2.4 owner 38일 PoC (Binance/Bybit/OKX paper) 법적 status

**PAPER 모드 = 가상 거래 = 법적 무관 확정**:
- 실 자본 0 → 외국환거래법 위반 0
- 신고 의무 0
- 양도세 0
- GitHub 코드 공개 = 합법 (educational + open source)

**LIVE 전환 시 발생 의무**:
- (a) 외국환거래법: USD 5만 초과 송금 시 사전 신고
- (b) 2027.1.1 이후: 250만원 초과 수익 22% 양도세
- (c) 미신고 거래소 (Binance 등) 이용 시 본인 책임 분명히 (포지션 동결 위험)

## 2.5 가상자산 양도소득세 시행 시기 (cold honest)

### 현 시점 (2026-05-14) 기준 확정 정보
- **시행일**: 2027.1.1 (2024.12 소득세법 개정안 통과)
- **세율**: 기타소득세 20% + 지방소득세 2% = **22%**
- **기본공제**: 연 250만원 (250만원까지 비과세)
- **신고**: 다음해 5월 종합소득세 (분리과세)

### 4차 유예 가능성
김갑래 (자본시장연구원) 보고서 (2025): 
> "지난 3차례의 유예 이후에도 가상자산 과세 제도의 핵심 공백이 해소되지 않아 2027년 시행을 장담하기 어렵다. 제4차 과세 유예 가능성도 배제할 수 없다."

→ portfolio build (2026~2027) = 세제 유예 기간, 가장 유리한 시기 확정.

---

# Section 3: 증권사 / 핀테크 입사 시 개인 매매 compliance

## 3.1 자본시장법 63조 + 금융투자협회 표준내부통제기준

### 강제 적용 사항 (모든 증권사 / 자산운용사 동일)

1. **본인 실명 단일계좌 원칙** (63조 1항)
   - 회사에 신고한 1개 계좌만 사용
   - 외부 broker 계좌 사용 = **위반** (과태료)
   - 차명거래 (가족 명의 등) = **위반** (3 요건 모두 충족 시: 자금출연 + 매매관여 + 손익귀속)

2. **준법감시인 사전승인** (표준내부통제기준)
   - 상장 지분증권 매매 사전승인 필수
   - 유효기간 = 승인일 포함 **2영업일**
   - 매매필터링 시스템 대체 가능 (회사 선택)

3. **회사 통지 의무** (시행령 64조)
   - **월별 통지**: 투자권유자문인력 + 조사분석인력 + **투자운용인력 (quant 부서)**
   - **분기별 통지**: 그 외 임직원 (PM / Data Analyst 포함)

4. **6개월 단기매매차익 반환** (자본시장법 172조)
   - 6개월 내 매수 → 매도 차익 발생 시 = 회사에 반환 의무
   - 미공개정보 이용 무관, 무조건 반환

5. **거래제한 대상목록** (Restricted List)
   - 자사주 매매 일반적 금지
   - watch list / blackout period 종목 매매금지

6. **회전율 / 횟수 제한** (회사별 추가 통제)
   - 월간 회전율 500% 이내
   - 일일 매수 3회 이내 / 월간 30회 이내 (일반적 standard)
   - 금감원 가이드: 분기별 10회 / 연간 매입액-매도액 = 전년 근로소득 50% 이내

## 3.2 한국 증권사별 정책 (공개 정보 기준)

### 한국투자증권 / 미래에셋증권 / 삼성증권 / NH투자증권 / 키움증권 (전통 5대)
- 자본시장법 + 표준내부통제기준 그대로 적용
- 추가 정책 (공개 안 됨, 입사 후 컴플라이언스 매뉴얼 확인 필요):
  - 자사주 6개월 보유 의무
  - 외부 broker 사용 전면 금지 (사실상)
  - watch list (M&A 자문 종목 등) 매매 차단

### 토스증권 (Toss Securities)
- 자본시장법 적용 (인가받은 증권사)
- 모회사 Toss (Viva Republica) 의 fintech 특성:
  - **공개 정책 자료 없음** (검색 0건)
  - 면접 / 입사 시 직접 확인 필수
  - 추정: 표준 + 모회사 임직원 동일 정책

### 카카오페이증권
- 자본시장법 적용
- 카카오 그룹사 임직원 정책 일관 (추정)
- **공개 정책 자료 없음**

### 빗썸 (가상자산 거래소)
- **임직원 전면 거래 금지** (2021.7 서약서)
- 임직원 + 회사 빗썸 계정 이용 금지
- 근무시간 내 거래 금지 + 차명거래 금지 + 상장 가상자산 72시간 내 거래금지
- 자체 모니터링 + 내부 신고제도 + 자체 감사
- 가상자산이용자보호법 시행 (2024.7) 후 더 엄격해짐

→ **빗썸 입사 = 본인 quant portfolio 전면 보류 또는 청산 필요**. 단 GitHub 코드 (실 자본 0, educational) 는 유지 가능 (회사 정책 명시 확인 필요).

## 3.3 직군별 차이 (PM / DA / Quant)

### Quant 트레이딩 부서 (투자운용인력)
- 월별 통지
- 회사 내 알고리즘 운용 = 본인 알고리즘 매매와 **conflict of interest 심각**
- 실무 관행: **개인 매매 사실상 금지** (회사 정책)
- GitHub Open Source quant 코드 = 회사 알고리즘과 무관함을 lawyer-reviewed 확인 필수

### PM (Product Manager) — owner 주 target
- 분기별 통지
- 사전승인 적용 (모든 임직원)
- 회사 internal 정보 (서비스 출시 등) 인지 시 = blackout period 자동 적용
- 외부 GitHub 활동 = 회사 IP 무관 시 가능 (회사 IP 정책 명시 확인)

### Data Analyst / Data Scientist — owner 주 target
- 분기별 통지 (일반 직원과 동일)
- 단 분석 대상이 자사 서비스 사용자 거래 데이터 = 미공개정보 노출 위험
- 자사 서비스 종목 매매 사실상 불가
- 외부 GitHub 활동 가능 (회사 IP 보호 전제)

### 비교 매트릭스

| 직군 | 통지 주기 | 사전승인 | 외부 매매 | GitHub 가능 | 권고 |
|---|---|---|---|---|---|
| Quant 트레이딩 | 월별 | 필수 | 사실상 0 | 회사 검토 | quant career = 본인 quant 0 |
| 알고리즘 트레이딩 | 월별 | 필수 | 매우 제한 | 회사 검토 | 동일 |
| PM (일반) | 분기 | 필수 | 가능 (제한적) | 가능 | **owner 주 target** |
| Data Analyst | 분기 | 필수 | 가능 (제한적) | 가능 | **owner 주 target** |
| 가상자산 거래소 (빗썸) | N/A | N/A | **전면 금지** | 회사 검토 | 본인 quant 청산 필요 |

## 3.4 신고 의무 + 보유 기간 + 금지 종목

### 자본시장법 63조 신고
- 매매명세 분기/월별 통지
- 차명거래 시 직무정지 6개월 또는 과태료

### 자본시장법 172조 단기매매차익
- 6개월 내 매매 차익 = 회사 반환
- 단순 swing trade = 적용 (의도 무관)
- 미신고 계좌 사용 + 단기매매 = 이중 위반

### 자본시장법 174조 미공개정보
- 미공개 중요정보 인지 시 매매금지
- 위반 시 형사처벌 + 부당이득 반환

### 자본시장법 173조 임원 / 대주주 보유상황 보고
- 임원 / 5% 이상 주주 = 보유 변동 5영업일 내 신고
- 일반 직원은 미적용

## 3.5 GitHub Open Source quant code 유지 가능 여부

### 입사 전 자산 (현 GitHub repo)
- **유지 가능** (회사 IP 무관 시)
- 단 입사 시 회사 의무: (a) 코드 회사 업무 무관 확인, (b) 회사 비밀정보 미포함 확인, (c) 사이드 프로젝트 정책 명시

### 입사 후 maintenance
- PR review / ROADMAP update = 가능 (회사 업무시간 외 + 본인 자원)
- 단 회사 알고리즘 / 데이터 / 미공개정보 commit 절대 금지
- 회사 정책상 사이드 프로젝트 사전 신고 의무 가능 (회사별 차이)

### 외부 community 활동
- Hacker News / Twitter / Discord 활동 = 일반적 가능
- 단 회사 신원 노출 + 회사 비판 = 위험
- educational only / no individualized advice = 안전

---

# Section 4: arXiv / SSRN 학술 publish 시 사전 승인

## 4.1 이트라이브 (현 직장) 정책 — 검증 불가

### 공개 자료
- 이트라이브 publication policy = **공개 자료 0건**
- 사내 NDA / 근무규정 = owner 직접 확인 필수

### 이미 박제된 실적
NeurIPS 2026 EthicaAI Melting Pot manuscript = blind review 진행 중. 이미 (a) 본인 AI R&D 결과 외부 publish, (b) 사전 승인 받은 이력으로 추정 (구체 절차 owner 만 알 수 있음).

### 권고
- 이트라이브 NDA + 취업규칙 확인 (사이드 프로젝트 / 외부 publish 조항)
- 신규 paper (quant) publish 전 (a) 회사 IP 무관 명시, (b) 본인 자원 명시, (c) 가능 시 사내 법무팀 / HR 일조 권장

## 4.2 target 회사 publication 정책 (토스 / 카카오페이증권 / 뱅크샐러드)

### 공개 정책 자료
- 검색 0건 (모든 회사)
- 일반적으로 한국 금융회사 / 핀테크 = 보수적 (사전 승인 일반적)

### 추정 정책 (한국 IT 업계 표준)
- 회사 IP / 비밀정보 미포함 시 = 일반적 허용
- 회사 명의 사용 시 = 사내 법무팀 / 홍보팀 사전 승인 필수
- 외부 컨퍼런스 발표 = 일반적 회사 승인 (실적 reward)

### owner 권고
입사 면접 시 직접 확인 질문:
1. "사이드 프로젝트 (GitHub Open Source) 정책은?"
2. "본인 AI / quant 관련 외부 publish 가능한가?"
3. "입사 전 자산 (현 GitHub) 유지 가능 정책 명시 있는가?"

## 4.3 외국계 IB / hedge fund 한국 지사 (참고)

### Two Sigma / Citadel / Goldman / Morgan Stanley / JP Morgan
- 공통: **외부 publish 사전 승인 필수**
- 일반적 정책:
  - 입사 6개월 ~ 1년 internal review 통과
  - 회사 IP / proprietary methodology 미포함 검증
  - 본인 GitHub repo 사실상 freeze (입사 후 신규 commit 사전 승인)
- Quant strategy / alpha = **외부 공개 절대 금지** (회사 기밀)

### owner 적용
외국계 IB / hedge fund 입사 시 = **본인 quant GitHub 일시 freeze** 또는 read-only 전환 일반적.

토스 / 카카오페이 / 뱅크샐러드 같은 **핀테크 본업 = relatively lenient** (회사 자체 quant trading 부서 없으므로 conflict 0). 이게 owner profile 와 가장 적합.

---

# Section 5: GitHub Open Source IP 정책

## 5.1 현 직장 (이트라이브) IP 정책

### 한국 직무발명진흥법
- 직무발명: 직무 관련 + 회사 업무 범위 = 회사 IP
- 휴일 + 본인 자원 + 회사 업무 무관 = **본인 IP** (직무발명 미해당)

### 저작권법 9조 — 업무상저작물
- 사용자 기획 + 직원이 업무로 창작 = 회사 저작권
- 컴퓨터 프로그램 = 공표 불요, 업무로 창작 시 회사 소유

### 대법원 2021다236111 (2021.9.9)
> "프로그램 개발이 직원의 주 직무가 아닌 경우 + 회사의 명시/묵시적 기획 부족 = 직원의 저작권 인정"

**owner 적용**:
- 이트라이브 직무 = CTS 콘텐츠그룹 파트장 + AI R&D TF 리드
- AI R&D = quant 와 관련 가능성 회색
- quant 코드 작성 시점이 **휴일 / 퇴근 후 + 본인 컴퓨터** 명시 권장
- 회사 업무 무관 명시 (예: GitHub repo README 에 "Personal project, no affiliation with any employer" 명시)

### 회사 IP 가 GitHub Open Source 에 포함되지 않는지 확인 절차
1. 모든 코드 = 본인 작성 (회사 PC / 회사 네트워크 사용 0)
2. 회사 데이터 / 비밀정보 = 0건 commit
3. 회사 알고리즘 / methodology = 0건 차용
4. 사용 라이브러리 = 공개 (open source license 명시)
5. owner identity 명시 = Yesol-Pilot, 회사 소속 별도 표기 X

## 5.2 target 회사 입사 후 GitHub 정책

### 입사 전 자산 (1인 retail quant portfolio) 유지
- **일반적 가능** (회사 정책상 explicit prohibition 없을 시)
- 단 입사 시점 snapshot 회사에 명시 권고 (입사 후 신규 commit 가 회사 IP 와 conflict 없도록)

### 입사 후 maintenance (PR review, ROADMAP update)
- **일반적 가능** (회사 업무시간 외)
- 신규 feature commit 시 = 회사 사이드 프로젝트 정책 확인 의무

### 회사별 차이
- 보수 (한국투자증권 / 미래에셋 / 삼성 등 전통 5대): 사전 신고 의무 일반적
- 핀테크 (토스 / 카카오페이 / 뱅크샐러드): 상대적 유연 (구체 정책 비공개)
- 가상자산 (빗썸): 가장 엄격 (전면 거래 금지 + 사이드 프로젝트 검토 일반적)

---

# Section 6: Paper Trading + Open Source quant code 법적 status

## 6.1 Paper Trading 자체 법적 status

### IBKR paper account
- 가상 자본 = 법적 무관 확정
- 자기 자본 0, 외국환거래법 미적용
- API 키 / 코드 = 공개 가능 (proprietary X)

### KIS Developers 모의투자
- 한국투자증권 공식 sandbox
- 가상 자본 = 동등
- 코드 공개 가능

### GitHub repo 에 paper trading 결과만 공개 = **법적 안전 확정**

owner 38일 PoC (Binance / Bybit / OKX paper) = 실 자본 0, 법적 위험 0, GitHub 공개 가능.

## 6.2 Open Source quant code 한국 법적 status

### 자기자본 운용 알고리즘 외부 공개 = **일임투자업 무관**
- 일임투자업 = 타인 자본 운용
- 자기자본 운용 알고리즘 공개 = educational, 타인이 운용 시 그 사용자의 자기자본 운용
- 자본시장법 미적용

### "투자 자문" 으로 분류되지 않는 안전 boundary
| 행위 | 분류 | 위험 |
|---|---|---|
| 알고리즘 코드 GitHub 공개 | educational | 0 |
| README 에 "백테스트 결과 X%" 공개 | educational | 0 |
| README 에 "실 자본 운용 결과 X%" 공개 | educational + 본인 사례 | 0 |
| Discord / Telegram 에서 코드 사용법 안내 | 무료 community support | 0 |
| 개별 사용자에게 "이 종목 사세요" 답변 | 투자자문업 (미등록) | 3년 / 1억 |
| 유료 구독 + 매매 신호 발신 | 투자자문업 / 유사투자자문업 | 신고 / 인가 의무 |
| 자동매매 봇 SaaS 판매 + 백테스트 결과 광고 | 유사투자자문업 | 신고 의무 |

### "Educational purpose only" disclaimer
- 강력 권고 (lawsuit defense)
- 모범 사례:

```
DISCLAIMER

This software is provided for educational and research purposes only.
It is not financial advice. The author makes no representations as to
accuracy, completeness, suitability, or validity of any information
on this repository and will not be liable for any errors or omissions
in this information or any losses, injuries, or damages arising from
its use.

Trading financial markets involves substantial risk of loss. Past
performance is not indicative of future results. By using this
software, you acknowledge that you have read this disclaimer and
agree to be solely responsible for any trades and decisions made.

This software is not registered with the Korean Financial Services
Commission (FSC) as an investment advisor or investment management
service. Any use of this software is at your own risk.
```

## 6.3 외부 contributor / fork 사용자가 실 자본 운용 시 책임

### MIT License 책임 차단
- MIT License = "AS IS" 명시, 저자 책임 면제
- 사용자가 실 자본 손실 시 = 본인 책임
- 한국 법원도 일반적 license 면책 조항 인정 (단 절대 보장 X)

### 추가 안전망
- DISCLAIMER 영구 README 상단 배치
- "NOT FINANCIAL ADVICE" badge / warning
- repo 설명에 "educational purpose only" 명시
- 한국어 disclaimer 추가 (한국 사용자 대상)

### 모범 사례 (Open Source 트레이딩 봇)
- NautilusTrader: "algorithmic trading software only, not broker/dealer/exchange"
- QuantConnect Lean: MIT + DISCLAIMER
- Hummingbot: Apache 2.0 + DISCLAIMER + KYC 안내
- Jesse: MIT + risk warning

owner 채택: **MIT + 한국어/영문 DISCLAIMER + educational badge**.

---

# Section 7: Cold Honest 권고 (위험 매트릭스)

## 7.1 Portfolio Build 단계 (paper only, 12주, 2026.5~2026.8)

| 위험 | severity | 발생 확률 | 대응 |
|---|---|---|---|
| 자본시장법 위반 (자기자본 자동매매) | LOW | 0% | 합법 확인됨 |
| 외국환거래법 위반 (IBKR 직접 사용) | MEDIUM | LIVE 시 가능 | **KIS / 키움 국내 broker 우선 사용** |
| 가상자산 미신고 거래소 (Binance) | LOW | PAPER = 0% | LIVE 시 정책 변경 risk |
| 회사 (이트라이브) IP 침해 | LOW | 0~10% | 회사 PC / 데이터 사용 0 |
| 회사 사이드 프로젝트 정책 위반 | UNKNOWN | UNKNOWN | **owner 직접 NDA / 취업규칙 확인 필수** |
| arXiv publish 회사 승인 누락 | UNKNOWN | UNKNOWN | NeurIPS 2026 절차 재확인 권장 |

**진행 권고**: portfolio build PAPER 단계 = **법적 위험 0** (회사 정책 확인 전제). 진행 OK.

## 7.2 Publish 단계 (arXiv / Hacker News, 2026.8~2026.10)

| 위험 | severity | 발생 확률 | 대응 |
|---|---|---|---|
| 회사 (이트라이브) publication 사전 승인 누락 | HIGH | UNKNOWN | **사전 승인 절차 명시 확인 필수** |
| 회사 IP 본의 아닌 노출 | MEDIUM | 5~10% | 코드 / 데이터 사전 review |
| 자본시장법 유사투자자문업 진입 | LOW | 0% (educational + no advice) | DISCLAIMER 영구 배치 |
| Hacker News virality → 채용 영향 | LOW | 긍정 효과 가능 | 회사 명시 표기 신중 |
| 외부 community 활동 (Discord 등) 회사 정책 위반 | UNKNOWN | UNKNOWN | 사전 신고 권장 |

**진행 권고**: publish 단계 = **이트라이브 사전 승인 절차 확정 후 진행**. 절차 불확실 시 publish 보류 권장.

## 7.3 입사 후 단계 (토스 / 카카오페이 / 뱅크샐러드 등, 2027+)

| 위험 | severity | 발생 확률 | 대응 |
|---|---|---|---|
| 자본시장법 63조 (단일계좌 / 사전승인) | HIGH | 100% (적용 의무) | 입사 시 본인 quant 계좌 정리 |
| 자본시장법 172조 (6개월 단기차익 반환) | HIGH | 가능 | 6개월 이상 보유 또는 매매 중단 |
| 회사 watch list / blackout 위반 | HIGH | 가능 | 회사 매뉴얼 숙지 |
| 미공개정보 이용 (회사 데이터 분석 → 본인 매매) | CRITICAL | 100% 위험 | 자사 / 자사 서비스 종목 매매 0 |
| GitHub repo 유지 정책 위반 | MEDIUM | UNKNOWN | 입사 시 양해각서 권장 |
| 입사 후 신규 commit 정책 위반 | MEDIUM | UNKNOWN | 사이드 프로젝트 사전 신고 |
| 빗썸 입사 시 본인 crypto holdings | CRITICAL | 100% (전면 금지) | **빗썸 입사 = crypto 전면 청산** |

**진행 권고**: 입사 시 회사별 정책 명시 확인 + 본인 quant portfolio **transition plan** 사전 수립.

---

# Section 8: Owner Action Items

## 8.1 필수 (Portfolio Build 진행 전, 2026.5 ~ 2026.6)

1. **이트라이브 NDA / 취업규칙 확인** (owner 직접):
   - [ ] 사이드 프로젝트 / 외부 publish 조항 확인
   - [ ] AI R&D TF 결과 외부 publish 절차 확인
   - [ ] 회사 IP / 비밀정보 boundary 명시 확인

2. **본인 GitHub repo (현재 Yesol-Pilot/quant-bot 등) 가시화 확인**:
   - [ ] README 에 "Personal project, no employer affiliation" 명시
   - [ ] DISCLAIMER 영구 추가 (educational only, no financial advice)
   - [ ] MIT License 명시
   - [ ] 회사 데이터 / 코드 / 비밀정보 commit history 0건 검증

3. **38일 PoC 코드 정리** (master archive):
   - [ ] PAPER 모드만 사용 명시
   - [ ] 실 자본 0, educational only 명시
   - [ ] Binance / Bybit / OKX API 키 = 본인 명의 (회사 명의 X) 확인

## 8.2 권고 (Portfolio Build 중, 2026.5 ~ 2026.8)

4. **국내 broker 우선 사용**:
   - [ ] KIS Developers (한국투자증권) 또는 키움 OpenAPI+ 사용
   - [ ] IBKR 사용 시 외국환거래법 7-33조 4항 위반 위험 인지
   - [ ] 미국 주식 = 키움 / 한국투자 의 해외주식 계좌 (국내 경유)

5. **PAPER → LIVE 전환 시 cold check**:
   - [ ] 자본 1억 미만 = retail 1인 자기자본 운용 안전 boundary
   - [ ] 자본 1억 이상 = 대주주 양도세 검토
   - [ ] 외환 송금 USD 5만 초과 시 한국은행 사전 신고
   - [ ] 미신고 거래소 (Binance) 자금 = 본인 책임 명시

6. **paper publish 사전 준비**:
   - [ ] arXiv 업로드 전 이트라이브 publication review 절차 확인
   - [ ] NeurIPS 2026 EthicaAI 사례 참고
   - [ ] 본인 자원 / 본인 시간 명시 (직무발명 미해당 증거)

## 8.3 옵션 (입사 시점, 2027+)

7. **target 회사 면접 시 명시 질문**:
   - [ ] "사이드 프로젝트 / GitHub 정책은?"
   - [ ] "본인 quant Open Source repo 유지 가능?"
   - [ ] "외부 paper publish 절차는?"
   - [ ] "watch list / blackout period 규정은?"

8. **빗썸 / crypto 거래소 입사 시**:
   - [ ] **본인 crypto holdings 전면 청산** (입사 전 완료)
   - [ ] GitHub repo 회사 검토 후 유지 가능 여부 확인
   - [ ] 본인 quant 알고리즘 = 회사 알고리즘과 conflict 0 명시

9. **증권사 (토스증권 / 카카오페이증권) 입사 시**:
   - [ ] 단일계좌 신고 절차 진행
   - [ ] 사전승인 시스템 / 매매필터링 시스템 숙지
   - [ ] 본인 quant repo = freeze 또는 maintenance mode 전환 결정

10. **외국계 IB / hedge fund 한국 지사 입사 시 (참고)**:
    - [ ] 본인 GitHub repo = **freeze 일반적**
    - [ ] Open Source quant 자산 = 입사 전 stable release 마무리
    - [ ] 입사 후 신규 quant 활동 = 회사 알고리즘과 차별화 필요

---

# Section 9: References (URL + 인용일)

## 한국 법령 (2026-05-14 인용)

1. [자본시장과 금융투자업에 관한 법률 (자본시장법)](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=94370) — 국가법령정보센터
2. [자본시장과 금융투자업에 관한 법률 시행령 64조](http://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%9E%90%EB%B3%B8%EC%8B%9C%EC%9E%A5%EA%B3%BC%20%EA%B8%88%EC%9C%B5%ED%88%AC%EC%9E%90%EC%97%85%EC%97%90%20%EA%B4%80%ED%95%9C%20%EB%B2%95%EB%A5%A0%20%EC%8B%9C%ED%96%89%EB%A0%B9/%EC%A0%9C64%EC%A1%B0) — 국가법령정보센터
3. [가상자산 이용자 보호 등에 관한 법률](https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=261099) — 국가법령정보센터
4. [특정 금융거래정보의 보고 및 이용 등에 관한 법률 (특금법)](https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=21013) — 김·장 법률사무소
5. [저작권법 9조 (업무상저작물)](https://casenote.kr/%EB%B2%95%EB%A0%B9/%EC%A0%80%EC%9E%91%EA%B6%8C%EB%B2%95/%EC%A0%9C9%EC%A1%B0) — CaseNote
6. [대법원 2021다236111 (업무상저작물 판단)](https://casenote.kr/%EB%8C%80%EB%B2%95%EC%9B%90/2021%EB%8B%A4236111) — CaseNote
7. [발명진흥법 / 직무발명제도](https://www.kipa.org/ip-job/intro/intro02.jsp) — 한국발명진흥회

## 금융위원회 / 금융감독원 (2026-05-14 인용)

8. [금융투자업자 임직원의 자기매매 위반에 대한 가이드라인 (2023.1.18)](https://www.fsc.go.kr/no010101/79303) — 금융위원회 보도자료
9. [가상자산이용자보호법 시행 안내 (2024.7.18)](https://www.fsc.go.kr/no010101/82682) — 금융위원회 보도자료
10. [유사투자자문업자의 불건전영업행위 규율 자본시장법 시행 (2024)](https://www.korea.kr/briefing/pressReleaseView.do?newsId=156645610) — 대한민국 정책브리핑
11. [미신고 가상자산사업자에 대한 이용 및 거래 주의 안내](https://fsc.go.kr/no010101/78323) — 금융위원회
12. [금융위원회·금융감독원 - 투자일임의 적용 범위 유권해석](https://casenote.kr/%EA%B8%88%EC%9C%B5%EC%9C%84%EC%9B%90%ED%9A%8C%C2%B7%EA%B8%88%EC%9C%B5%EA%B0%90%EB%8F%85%EC%9B%90/2da7fcc676) — CaseNote
13. [금융위원회·금융감독원 - 자본시장법 제63조 위반 여부](https://casenote.kr/%EA%B8%88%EC%9C%B5%EC%9C%B0%EC%9B%90%ED%9A%8C%C2%B7%EA%B8%88%EC%9C%B5%EA%B0%90%EB%8F%85%EC%9B%90/ef51273d5d) — CaseNote

## 금융투자협회 (KOFIA)

14. [금융투자회사 표준내부통제기준](https://law.kofia.or.kr/service/law/lawFullScreenContent.do?seq=150&historySeq=437) — 금융투자협회 법규정보시스템
15. [금융투자회사의 컴플라이언스 매뉴얼 (공통·증권·선물편)](https://law.kofia.or.kr/service/law/lawFullScreenContent.do?seq=284&historySeq=780) — 금융투자협회
16. [증권회사임직원의주식등의매매거래에관한내부통제기준표준안](https://law.kofia.or.kr/service/law/lawFullScreenContent.do?seq=234&historySeq=617) — 금융투자협회

## 판례

17. [인천지방법원 2017노1649 (자동매매 프로그램 판매)](https://albup.co.kr/page/judgement_detail.php?com_idx=25092) — 판례검색
18. [주식 자동매매 프로그램 판매 투자자문업 해당 여부](https://albup.co.kr/page/judgement_detail.php?com_idx=8304) — 판례검색
19. [컴퓨터프로그램 업무상저작물 판단 (대법원 2021.9.9)](https://www.scourt.go.kr/portal/news/NewsViewAction.work?seqnum=7950&gubun=4) — 대법원

## 한국 broker / 증권사 자료

20. [KIS Developers (한국투자증권 Open API)](https://apiportal.koreainvestment.com/intro)
21. [한국투자증권 Open Trading API GitHub](https://github.com/koreainvestment/open-trading-api)
22. [키움증권 Open API+ 개발가이드](https://download.kiwoom.com/web/openapi/kiwoom_openapi_plus_devguide_ver_1.1.pdf)
23. [한국투자증권 Open API 파이썬 자동매매 (TG Programming Blog)](https://tgparkk.github.io/stock/2025/03/08/auto-stock-1-init.html)

## IBKR / 해외 broker

24. [IBKR Available Countries](https://www.interactivebrokers.com/en/accounts/open-account-country-list.php)
25. [Is Interactive Brokers Legal in Korea?](https://tradersunion.com/brokers/forex/view/interactive_brokers/is-regulated-in-korea/)
26. [IBKR Korea Stock Exchange Fees](https://www.interactivebrokers.com/en/accounts/fees/KSE.php)
27. [IBKR Korea Equities Launch (2026.5.7)](https://www.interactivebrokers.com/en/general/about/mediaRelations/5-7-26.php)

## 가상자산 / 양도세

28. [가상자산 과세 유예 2027년 시행 (KDI 경제교육)](https://eiec.kdi.re.kr/policy/domesticView.do?ac=0000200097)
29. [거주자의 가상자산소득 과세 개요 (국세청)](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=40370&cntntsId=238935)
30. [가상자산이용자보호법 본격 시행 주요 내용](https://m.boannews.com/html/detail.html?idx=131600)
31. [Korea's Digital Asset Basic Act (Pebblous)](https://blog.pebblous.ai/report/korea-digital-asset-basic-law-2026/en/)

## 빗썸 / 가상자산 거래소 임직원 정책

32. [빗썸 임직원 내부거래 금지 (2021.7)](https://news.mt.co.kr/mtview.php?no=2021070208365644719) — 머니투데이
33. [빗썸 임직원 내부거래 금지 서약서](https://www.bloter.net/newsView/blt202107020005) — 블로터

## 외국환거래법

34. [외국환거래 위반사례집 (2019.11)](https://exchange.kfb.or.kr/data/foreign_exchange_breach.pdf) — 한국은행
35. [외국환거래법규 위반 10대 유형 (Citibank)](https://www.citibank.co.kr/download/cms/ir/CONSUMER_INFO/cs_consumer_foreign_180427.pdf)
36. [한국은행 외환거래별 신고 안내](https://www.bok.or.kr/portal/main/contents.do?menuNo=200405)

## Open Source Trading Engines

37. [NautilusTrader](https://nautilustrader.io/) — algorithmic trading software disclaimer 모범
38. [QuantConnect Lean GitHub](https://github.com/QuantConnect/Lean)
39. [Hummingbot](https://hummingbot.org/)
40. [Jesse Trade](https://jesse.trade/)

## 직무발명 / 저작권

41. [직무발명제도 공식사이트 (한국발명진흥회)](https://www.kipa.org/ip-job/intro/intro02.jsp)
42. [업무상 저작물 성립 요건 (카산 법무법인)](http://kasanlaw.com/bbs/board.php?bo_table=sub04_2&wr_id=690)
43. [직원이 창작한 저작물 회사 소유 여부 (Platum)](https://platum.kr/archives/172495)

## 학술 publish 정책

44. [arXiv About](https://info.arxiv.org/about/index.html)
45. [Open Access and University IP Policies (Authors Alliance)](https://www.authorsalliance.org/2023/08/18/open-access-and-university-ip-policies-in-the-united-states/)

---

## Document Status

- **작성 완료**: 2026-05-14
- **작성자**: Strategy Lead Claude Opus 4.7 (autonomous G1 research)
- **검증 단계**: cold honest 1차 완료, owner G2 review 대기
- **다음 갱신 트리거**:
  1. 이트라이브 NDA / 취업규칙 확인 후 (Section 4.1 + 5.1 갱신)
  2. target 회사 면접 / 입사 시 (Section 3.2 갱신)
  3. 가상자산 양도세 시행 변동 시 (Section 2.5 갱신)
  4. 자본시장법 / 가상자산법 개정 시 (전체 갱신)
- **rollback**: git history 보존, ssotRevision propagate 별도

## Cold Honest Closing Note

이 조사는 **공개 정보 기반** 이며 lawyer-reviewed 법률 자문 **아님**. 38일 quant-bot PoC 가 정책 변경 (Binance forceOrder 1/sec)으로 실패한 패턴 재현 방지 목적의 사전 리스크 박제. 

**owner G2 결정 필요한 사항 5건**:
1. portfolio build PAPER 단계 진행 (법적 위험 0)
2. publish 단계 진행 (이트라이브 사전 승인 절차 확인 후)
3. IBKR 사용 여부 결정 (외국환거래법 위반 risk vs benefit)
4. crypto LIVE 전환 시점 (2027.1.1 양도세 시행 전 vs 후)
5. target 회사 우선순위 (핀테크 = relatively lenient / 가상자산 = 엄격)

**owner 직접 확인 필수 사항 3건**:
1. 이트라이브 NDA / 취업규칙 (사이드 프로젝트 / 외부 publish 조항)
2. NeurIPS 2026 EthicaAI publish 시 절차 재확인 (quant paper 동일 적용 가능 검증)
3. target 회사 (토스 / 카카오페이 / 뱅크샐러드) 면접 시 사이드 프로젝트 정책 명시 질문

👤 Claude Opus 4.7 (Strategy Lead, autonomous research mode)
