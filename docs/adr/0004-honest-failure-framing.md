# ADR-0004 — Lead with the −15.1% failure, not a launch pitch

- Status: Accepted
- Date: 2026-05-14 (W1 D1, framing locked in design v2.0)
- Decider: Owner + Strategy Lead
- Supersedes: the W1 D1 v1.0 "career portfolio" framing (rejected mid-W1)
- Superseded by: —

## Context

The project follows a closed 38-day crypto PoC that returned −15.1% paper PnL
(191 trades, 37.7% win rate, 0/108 sensitivity-sweep cells passing on the
flagship alpha). There were two ways to present the new repo:

1. **Hide the failure.** Open with the rebuild plan, mention the PoC only as
   "prior experience," lead the live site with aspirational metrics.
2. **Lead with the failure.** Make −15.1% the hero number on the landing page,
   the first line of the README, the subject of the first SSRN paper.

A first draft of the site briefly drifted toward a third option — a
career-portfolio framing that pitched the maintainer for hire. The owner
rejected this explicitly: "여기서 내 이력을 팔고 홍보할 필요는 없어" (no need
to sell my résumé here). See ADR-0005-adjacent note: the site is project-only;
career inquiries redirect to heoyesol.kr.

## Decision

Lead with the failure. Specifically:

- The landing page hero is the literal string `−15.1%` styled in the
  `.honest-failure` danger color.
- The README opens with the PoC outcome before the rebuild plan.
- The first planned paper (SSRN, W9-W12) is titled around "honest failure":
  a 1-person multi-strategy retrospective.
- The live site is **project-only**. It does not pitch the maintainer. Career
  inquiries are redirected to `heoyesol.kr` (a separate site).

## Consequences

- **Credibility compounds.** The 9-layer kill switch built during the PoC reads
  as a load-bearing safety mechanism (because the loss is on the record), not a
  victory lap on a winning bot.
- **Differentiation.** The quant-content landscape is saturated with "I made N%
  last month." "Here is the sweep that failed and the bot I closed" is rare and
  memorable — it is the marketing hook for every channel (Substack, Twitter,
  LinkedIn, HN).
- **Constraint.** Every future metric must be reported honestly, including
  paper-trade drawdowns and failed alphas. We cannot quietly drop a losing
  alpha; we archive it with a post-mortem. This is enforced socially (the brand
  is "honest"), and technically (DSR/PBO must accompany every Sharpe — see
  ADR-0006 and packages/core/backtest/metrics.py).
- **Risk.** Leading with a loss can read as weakness to a shallow reader. We
  accept this; the target audience (researchers, quant-curious builders,
  Korean retail learners) values the transparency.

## Alternatives considered

1. Hide the failure (option 1) — rejected: makes the kill switch look like a
   brag and forfeits the differentiation.
2. Career-portfolio framing (the drift) — rejected by owner: conflates the
   project with a job hunt and pollutes the project's neutrality.
3. **Honest failure, project-only** ✅ chosen.

## References

- `apps/live-dashboard/src/app/page.tsx` (hero `−15.1%`)
- `apps/live-dashboard/src/app/about/page.tsx` ("What this site is not")
- `README.md` opening section
- docs/design/04-live-page-product-spec.md (v2.0, Persona set without "Recruiter")
