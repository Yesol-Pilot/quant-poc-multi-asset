# Substack Issue 01 — Draft

> Status: draft (Week 1, 2026-05-14). Owner review required before publish.
> Target send: Week 2 (5/21~5/27), once newsletter is live and 50+ initial subs confirmed.
> Audience: dual-track (Korean retail learners + English research/dev followers). Single newsletter, both languages stacked. English first, then full Korean translation below.

---

## Subject line candidates

Pick one before send. Drafted three so the A/B story can run in Week 2~3 issues.

1. `We published a −15.1% trading loss before we published any wins.` (recommended)
2. `Why "honest failure first" is a hiring signal, not a confession.`
3. `A 12-week, single-developer, multi-asset quant build — in public.`

Preview text (all variants): *Crypto PoC closed at −15.1%. The lessons, the rebuild plan, and what an open-source weekly looks like when you publish the loss before the win.*

---

## English body

Subject: *We published a −15.1% trading loss before we published any wins.*

---

Hi —

This is Issue 01 of **`quant-poc-multi-asset`**, a 12-week weekly. If you signed up after reading the GitHub README, the LinkedIn launch post, or the Hacker News thread, welcome. If you signed up by mistake, the unsubscribe link is at the bottom and nobody will be offended.

I'm going to do something unfashionable for an Issue 01: I'm not going to pitch the new project. I'm going to talk about the *closed* one.

### What just ended

From 2026-04-05 to 2026-05-12, I ran a 38-day proof-of-concept that paper-traded six crypto perpetuals strategies across Binance, Bybit, and OKX. The headline numbers:

- 191 paper trades
- 37.7% win rate
- **−15.1% paper PnL**
- 0 of 108 sensitivity-sweep cells passed the acceptance gate on the flagship mean-reversion alpha (A2)
- 0 trades on the next-generation alphas (A1, A3~A6) over the final 19 days

I closed it. I closed it the same day I confirmed the sweep had zero passes. I `pm2 stop`-ed every runner, I wrote a closure note, and I started writing the post-mortem you'll see in the **research backbone** of the new repo.

Most people I know would have sandbagged this. They would have kept one alpha running, called it "in iteration," and waited for a green week before they talked about it. I'm not doing that, and the reason I'm not doing that is the point of this newsletter.

### Honest failure is the artifact

The crypto PoC produced one durable thing: a 9-layer kill switch that traces real production wiring across three exchanges, with shadow logs, supabase audit trails, and cross-exchange aggregation that handled Binance's April 27 policy change without losing a beat. That code is real. It is the only thing I trust from the entire 38 days. Everything else — every alpha, every backtest — was a hypothesis the market rejected.

If I had hidden the −15.1%, that kill switch would have looked like a victory lap on a winning bot. Instead, it gets to be what it actually is: the load-bearing safety mechanism for the rebuild.

In `quant-poc-multi-asset`, the closed PoC isn't an embarrassment buried in a footnote. It's the first paper, the load-bearing reason every alpha now ships with a Deflated Sharpe Ratio, a Probability of Backtest Overfitting estimate, and a published sensitivity sweep before it touches paper money in the new repo.

### What's getting rebuilt (in public, weekly)

Twelve weeks. One developer. Four asset classes:

- 🇰🇷 **Korean equities** via KIS Developers (mock API; live is blocked at the CI level)
- 🇺🇸 **US equities & ETFs** via IBKR paper (port 7497; the live port 7496 is a CI guard violation)
- 📈 **US options** via IBKR paper — covered call, VRP, iron condor
- ₿ **Crypto** — archived. Read-only. The post-mortem corpus.

Eleven new alphas, A11~A21. Every one shipped with a public backtest run id, a sensitivity grid, and a kill-switch invariant test in CI.

Two papers:

- **SSRN.** A case study on the closed PoC. Working title: *One-person, multi-strategy, honest failure: a 38-day crypto perpetuals retrospective.*
- **ReScience.** A replication of a public-source Korean factor paper (Fama-French five-factor on KOSPI 200). Code, data lineage, plots, all open.

The arXiv preprints for the EthicaAI and WhyLab manuscripts are on hold while their double-blind reviews complete. The quant rebuild does not depend on those, and pretending otherwise would be cute. So I'm waiting.

### What this newsletter will be

Once a week, Monday morning Seoul time. Three things every issue:

1. **One number that moved.** Paper PnL, kill-switch fires, test count, star count, doc word count. One number, with the context.
2. **One thing I learned the hard way.** Always specific. No "embrace failure" mush.
3. **One link.** A research paper, a code change, a backtest run id, or — sometimes — a quiet brag about a Lighthouse score.

There is no upsell. There is no course. There is no Discord with a paywall. If at some point one of those exists, it will be because the project earned it, not because the newsletter needed a flywheel.

If you got value from this, the most useful thing you can do is forward it to one person who would rather read about a closed strategy than a launched one.

— Yesol (허예솔)

GitHub: <https://github.com/Yesol-Pilot/quant-poc-multi-asset>
Site: <https://quant.heoyesol.kr>
Career stuff lives separately at <https://heoyesol.kr> on purpose.

---

## 한국어 본문

제목: *수익 글을 쓰기 전에, 손실 −15.1%부터 공개합니다.*

---

안녕하세요.

**`quant-poc-multi-asset`** 뉴스레터 첫 호입니다. GitHub README, LinkedIn 글, Hacker News 스레드 어느 경로로 오셨든 환영합니다. 실수로 구독하셨다면 맨 아래 구독 취소 링크가 있으니 부담 없이 눌러주세요.

첫 호에 어울리지 않는 이야기를 먼저 하겠습니다. 새로 시작한 프로젝트가 아니라, **막 끝낸** 프로젝트 이야기입니다.

### 막 끝난 것

2026-04-05 ~ 2026-05-12, 38일 동안 Binance · Bybit · OKX에서 6개 무기한선물 전략을 페이퍼로 돌렸습니다. 결과는 이렇습니다.

- 모의 거래 191건
- 승률 37.7%
- **−15.1% 페이퍼 손익**
- 핵심 평균회귀 알파(A2) 108개 셀 sensitivity sweep 중 **0개 통과**
- 차세대 알파(A1, A3~A6) 마지막 19일간 거래 **0건**

그래서 종결했습니다. sweep 0/108을 확인한 그 날, 모든 PM2 러너를 정지시키고 종결 노트를 쓰고, 곧 공개할 **research backbone**의 첫 포스트모템 초고를 시작했습니다.

대부분은 이렇게 안 합니다. 알파 하나만 살려두고 "iterating 중"이라 부르며 다음 녹색 주를 기다리겠죠. 저는 그렇게 안 합니다. 그 이유가 이 뉴스레터의 핵심입니다.

### 정직한 실패가 자산

38일 PoC가 남긴 단 하나의 견고한 산출물은 9-layer kill switch입니다. 세 거래소를 가로지르는 실제 프로덕션 배선, 새도우 로그, Supabase 감사 추적, 그리고 Binance 4월 27일 정책 변경을 흡수한 cross-exchange aggregation. 이 코드는 진짜입니다. 38일 통틀어 제가 신뢰하는 유일한 산출물입니다. 다른 모든 것 — 알파, 백테스트 — 은 시장이 기각한 가설이었습니다.

만약 −15.1%를 숨겼다면, kill switch는 "잘 나가는 봇의 승리 표식"처럼 보였을 겁니다. 공개했기에 본래 모습 그대로 — **재건의 안전 장치**로 — 자리 잡습니다.

`quant-poc-multi-asset`에서 종결된 PoC는 각주에 묻힌 부끄러움이 아니라, 모든 신규 알파가 페이퍼 머니에 손대기 전 **Deflated Sharpe Ratio, Probability of Backtest Overfitting, 공개된 sensitivity sweep**을 의무 출판하는 이유 — 즉 첫 번째 논문의 토대입니다.

### 무엇을 다시 짓는가 (공개, 매주)

12주. 한 명의 개발자. 4개 자산군.

- 🇰🇷 **한국 주식** — KIS Developers (모의 API. 실거래는 CI에서 차단)
- 🇺🇸 **미국 주식 & ETF** — IBKR paper (포트 7497. 실거래 포트 7496은 CI 가드 위반)
- 📈 **미국 옵션** — IBKR paper — covered call, VRP, iron condor
- ₿ **크립토** — 아카이브. 읽기 전용. 포스트모템 코퍼스

신규 알파 11개, A11~A21. 모두 공개 backtest run id, sensitivity 그리드, CI의 kill-switch invariant 테스트와 함께 출시합니다.

논문 2건:

- **SSRN.** 종결된 PoC 사례 연구. 가제: *1인 멀티스트래티지, 정직한 실패 — 38일 크립토 무기한선물 회고.*
- **ReScience.** 공개 소스 한국 팩터 논문 재현 (Fama-French 5-factor on KOSPI 200). 코드·데이터 계보·그래프 전부 공개.

EthicaAI / WhyLab 원고의 arXiv preprint는 더블 블라인드 심사 중이라 hold 입니다. 퀀트 재건은 이 두 논문에 의존하지 않습니다. 그 사실을 숨기는 게 더 어색하기에, 솔직히 기다리는 중입니다.

### 이 뉴스레터의 형식

매주 월요일 오전, 한국 시간 기준. 매 호 세 가지:

1. **움직인 숫자 하나.** 페이퍼 PnL, kill-switch 발동, 테스트 수, GitHub 스타, 문서 단어 수. 숫자 하나와 맥락.
2. **어렵게 배운 것 하나.** 항상 구체적으로. "실패를 받아들이자" 같은 죽 같은 문장 없음.
3. **링크 하나.** 논문, 코드 변경, backtest run id, 또는 가끔은 — Lighthouse 점수 자랑 한 줄.

업셀 없습니다. 강의 없습니다. 유료 디스코드 없습니다. 어느 시점에 그런 게 생긴다면, 그건 뉴스레터의 플라이휠이 필요해서가 아니라 프로젝트가 그것을 벌었기 때문일 겁니다.

도움이 되셨다면, "출시된 전략"보다 "종결된 전략"이 더 궁금한 사람 한 명에게 전달해 주세요. 그게 가장 큰 도움입니다.

— Yesol (허예솔)

GitHub: <https://github.com/Yesol-Pilot/quant-poc-multi-asset>
사이트: <https://quant.heoyesol.kr>
커리어 관련 글은 의도적으로 <https://heoyesol.kr>(별도 메인 사이트)에 분리되어 있습니다.

---

## Owner action checklist (before send)

- [ ] Substack publication name decided (suggestion: `quant-poc-multi-asset weekly`)
- [ ] Domain mapping: <https://quant.heoyesol.kr/blog> redirects to Substack publication
- [ ] Substack -> Twitter cross-post connector enabled
- [ ] Owner profile bios (`docs/marketing/profile-bios.md`) live on Substack profile
- [ ] First-issue preview rendered in Substack draft view (mobile + desktop)
- [ ] Disclaimer link in footer points to <https://quant.heoyesol.kr/disclaimer>
- [ ] Spam-check: avoid `100% return`, `guaranteed`, `risk-free` in subject / preview — none of these appear in current draft; verify before send
