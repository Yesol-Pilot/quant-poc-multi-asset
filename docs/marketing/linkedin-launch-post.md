# LinkedIn — Launch Post Draft

> Status: draft (Week 1, 2026-05-14). Owner posts in Week 2 D3 after Substack issue 01 + Twitter pin are live, so the LinkedIn post has cross-references.
> Account: <https://www.linkedin.com/in/yesolhuh> (or final handle).
> Post length budget: LinkedIn favors 1,300~1,900 char posts with 5~9 line breaks. Below is one English variant (~1,800 chars) and one Korean variant (~1,400 chars). Pick by week, post both is fine.

---

## English variant (post first)

I'm launching a 12-week public build of a multi-asset quant research stack. The unusual part of the launch isn't the project — it's that I'm leading with the failure that preceded it.

From 2026-04-05 to 2026-05-12, I ran a 38-day proof-of-concept on six crypto perpetuals strategies across three exchanges. Results:

➤ 191 paper trades
➤ 37.7% win rate
➤ −15.1% paper PnL
➤ 0 of 108 sensitivity-sweep cells passed the acceptance gate on the flagship mean-reversion alpha
➤ 0 trades on the next-generation alphas over the final 19 days

I closed it the same day I confirmed the sweep had zero passes. Then I started writing the public retrospective.

The new repo — `quant-poc-multi-asset` — is the rebuild. Four asset classes (Korean equities via KIS Developers mock, US equities and ETFs via IBKR paper, US options, archived crypto layer). Eleven new alphas (A11~A21). Every one ships with a Deflated Sharpe Ratio, a Probability of Backtest Overfitting estimate, and a published sensitivity sweep before it sees paper money.

Two papers planned:
• SSRN — "One-person, multi-strategy, honest failure": a case study on the closed PoC
• ReScience — replication of a public-source Korean factor paper (FF5 on KOSPI 200)

The arXiv preprints for two unrelated manuscripts (EthicaAI, WhyLab) are on hold while their double-blind reviews complete. The quant rebuild does not depend on them, so I wait. Honestly.

Why the radical openness? Two reasons.

One — the 38-day PoC produced a 9-layer kill switch that runs across Binance, Bybit, and OKX. That code is real. By publishing the −15.1%, the kill switch gets to be what it actually is (the load-bearing safety layer for the rebuild) instead of a victory lap on a winning bot.

Two — the field needs more publish-the-loss work. There is plenty of "I made N percent last month" content. There is very little "here is the sensitivity sweep that failed and here is what I closed."

MIT license. Open weekly progress. No upsell, no course, no paywalled Discord.

GitHub: https://github.com/Yesol-Pilot/quant-poc-multi-asset
Live site (scaffolding W2~3): https://quant.heoyesol.kr

— Yesol Huh

---

## Korean variant (post 2~3 days later, separate post)

`quant-poc-multi-asset` 12주 공개 빌드를 시작합니다. 시작 포스트에 이례적인 건 프로젝트 자체가 아니라, 그것을 앞두고 종결한 실험을 먼저 공개한다는 점입니다.

2026-04-05 ~ 2026-05-12, 38일간 3개 거래소(Binance, Bybit, OKX)에서 6개 크립토 무기한선물 전략을 페이퍼로 돌렸습니다. 결과:

➤ 모의 거래 191건
➤ 승률 37.7%
➤ 누적 손익 −15.1%
➤ 핵심 평균회귀 알파 sensitivity sweep — 108개 셀 중 통과 0개
➤ 차세대 알파 마지막 19일간 거래 0건

sweep 0/108을 확인한 그 날, 봇을 정지시키고 공개 회고를 쓰기 시작했습니다.

신규 저장소 `quant-poc-multi-asset`은 그 재건입니다. 4개 자산군 — 한국 주식(KIS Developers 모의), 미국 주식·ETF (IBKR paper), 미국 옵션, 아카이브된 크립토. 신규 알파 11개 (A11~A21). 모두 페이퍼 머니에 손대기 전 Deflated Sharpe Ratio, Probability of Backtest Overfitting, 공개 sensitivity sweep을 의무 출판합니다.

논문 2건:
• SSRN — "1인 멀티스트래티지, 정직한 실패": 종결된 PoC 사례 연구
• ReScience — 공개 소스 한국 팩터 논문 재현 (KOSPI 200 FF5)

비관련 원고 두 건(EthicaAI, WhyLab)의 arXiv preprint은 더블 블라인드 심사 중이라 hold 입니다. 퀀트 재건은 두 논문에 의존하지 않습니다.

왜 이렇게 급진적으로 공개하는가? 두 가지.

하나 — PoC 38일이 남긴 9-layer kill switch는 진짜 코드입니다. −15.1%를 공개해야, 이 kill switch가 "수익봇의 승리 표식"이 아니라 본래 모습 — 재건의 안전 장치 — 로 자리 잡습니다.

둘 — "이번 달 N% 수익" 콘텐츠는 충분합니다. "통과 못한 sweep, 그리고 종결한 봇" 콘텐츠가 부족합니다.

라이선스 MIT. 매주 공개 진행. 업셀·강의·유료 디스코드 없음.

GitHub: https://github.com/Yesol-Pilot/quant-poc-multi-asset
라이브 사이트 (스캐폴딩, W2~3): https://quant.heoyesol.kr

— Yesol Huh (허예솔)

---

## Pre-publish checklist

- [ ] Profile headline in LinkedIn matches `profile-bios.md`
- [ ] Pinned post on Twitter is live (LinkedIn audience often cross-checks)
- [ ] Substack issue 01 has shipped at least 24h prior
- [ ] `/disclaimer` link works on quant.heoyesol.kr
- [ ] Post visibility: Public, Anyone (NOT Connections-only)
- [ ] Tags: `#OpenSource` `#QuantFinance` `#KoreanFinTech` `#FailFast` (max 3~4, avoid spam-tier)
- [ ] No client solicitation language
- [ ] If LinkedIn restricts inline links: pin the GitHub URL as first comment instead

---

## Engagement playbook (first 48h)

- Reply to every substantive comment within 4h during waking hours
- Do not edit the post within first 6h (LinkedIn algorithm penalizes early edits)
- If someone asks "is this a job pitch?": link to <https://heoyesol.kr> and clarify this project is separate
- If someone asks for portfolio access / API key: politely link to /disclaimer
- If a Korean fintech engineer comments substantively: invite to GitHub Discussions (not DM)
