# Twitter / X — Pinned Tweet Draft

> Status: draft (Week 1, 2026-05-14). Owner posts after the GitHub repo crosses 5 stars (organic, not solicited) so the pinned tweet has at least some social-proof anchor.
> Target post window: Week 2 D2~D3.
> Account: `@yesolhuh` (or final handle decided in Week 1 setup).

---

## Recommended pinned tweet (single)

```
38-day crypto PoC: 191 trades, 37.7% WR, −15.1% PnL.
0 of 108 sensitivity-sweep cells passed on the flagship alpha.

I closed it the same day I confirmed it.

Now rebuilding across 4 asset classes — KR equities (KIS), US equities, US options, crypto archive — in public, 12 weeks, MIT.

🧵 ↓

github.com/Yesol-Pilot/quant-poc-multi-asset
```

**Character budget:** ~275 / 280 — fits, but leave room for the handle.
**Why pinned:** This tweet is the entire positioning in one breath. Honest number first, decision next, what's getting built last.

---

## Thread (reply chain, 5 tweets after the pin)

### 2/5 — kill switch is the artifact

```
The PoC's only durable artifact: a 9-layer kill switch that ran across Binance + Bybit + OKX and absorbed Binance's April 27 policy change without losing a beat.

If I'd hidden the −15.1%, that kill switch would look like a victory lap. By publishing the loss, it gets to be what it is: the load-bearing safety layer for the rebuild.
```

### 3/5 — what gets rebuilt

```
A11~A21, eleven new alphas:

🇰🇷 KR equities (KIS mock): sector rotation, mean reversion, pair, PEAD
🇺🇸 US equities/ETFs (IBKR paper): factor, risk parity, PEAD, sector momentum
📈 US options (IBKR paper): covered call, VRP, iron condor
₿ crypto: archived, read-only, the post-mortem corpus

Every alpha ships with DSR, PBO, and a published sensitivity sweep before paper money.
```

### 4/5 — what gets published

```
Two papers, both public-source:

- SSRN — "1-person, multi-strategy, honest failure": 38-day crypto retrospective
- ReScience — FF5 replication on KOSPI 200

arXiv preprints (EthicaAI, WhyLab) are on hold while double-blind review completes. The quant rebuild does not depend on them, so I wait.
```

### 5/5 — how to follow

```
Weekly Monday 08:00 KST:

⭐ github.com/Yesol-Pilot/quant-poc-multi-asset (commits + ROADMAP)
🌐 quant.heoyesol.kr (live paper dashboard, scaffolding W2~3)
📨 Substack (link Week 2, after first issue ships)

No upsell. No course. No paywall. If those ever exist, it's because the project earned it.
```

---

## Alternative single-tweet hook variants

For A/B testing in later weeks (not pinned):

### Variant A — research credibility hook

```
I published a −15.1% paper PnL before publishing a single paper.

Reason: the 9-layer kill switch built during that loss is the only thing I trust from the 38 days, and it only gets to be load-bearing if the loss is on the record.

12-week, multi-asset, open rebuild → github.com/Yesol-Pilot/quant-poc-multi-asset
```

### Variant B — methodology hook

```
Every new alpha in this repo ships with three numbers before it touches paper money:

- Deflated Sharpe Ratio
- Probability of Backtest Overfitting
- Sensitivity sweep grid (all cells, including the failures)

If those three don't pass CI, the alpha doesn't merge.

github.com/Yesol-Pilot/quant-poc-multi-asset
```

### Variant C — Korean retail hook (post in 한국어 thread later)

```
38일 크립토 PoC, 191건 모의 거래, 승률 37.7%, 누적 −15.1%.

108개 sensitivity sweep 셀 중 통과 0건 확인한 날 봇을 종결했습니다.

이제 한국 주식·미국 주식·미국 옵션·크립토 아카이브 — 4개 자산군에서 다시 짓습니다. 12주, 오픈소스, MIT.

🧵 ↓ github.com/Yesol-Pilot/quant-poc-multi-asset
```

---

## Pre-publish checklist

- [ ] Twitter handle confirmed in bio (see `profile-bios.md`)
- [ ] Repo open, README displays −15.1% hero on first visit
- [ ] `https://quant.heoyesol.kr` live (or explicitly "scaffolding" page)
- [ ] Pinned-thread length verified <280 chars per tweet (Twitter counts t.co URLs as 23 chars regardless of length)
- [ ] No financial-advice language (no "buy", "sell", "guaranteed", "profit")
- [ ] No solicitation of clients / funds / DMs
- [ ] Disclaimer mention or `/disclaimer` link visible on linked surfaces

---

## Notes

- Don't tag accounts in the pin. Organic growth, no notification spam.
- If first 24h impressions <2k, don't delete; let it ride. Substack issue 01 in Week 2 will recirculate the same hook with more context.
- Avoid responding to "lol you lost money" QTs in the first 48h. Engagement-baiting noise. Respond only to substantive technical questions.
