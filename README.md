# quant-poc-multi-asset

> **AI-Native Multi-Asset Quant Portfolio: Honest Failure Report from a 1-Person Builder**
>
> 38-day Crypto PoC → 12-week 4-asset-class portfolio. Production-grade. Open Source. Academic-rigorous.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/build-pending-lightgrey.svg)](#)
[![Tests](https://img.shields.io/badge/tests-0%2F1000-lightgrey.svg)](#)
[![Coverage](https://img.shields.io/badge/coverage-0%25-lightgrey.svg)](#)
[![Stars](https://img.shields.io/github/stars/Yesol-Pilot/quant-poc-multi-asset?style=social)](https://github.com/Yesol-Pilot/quant-poc-multi-asset)
[![Discord](https://img.shields.io/badge/Discord-pending-7289DA?logo=discord&logoColor=white)](#)

**English** | [한국어](#한국어)

---

## 🎯 What This Is

A **1-person, AI-native, multi-asset quant portfolio** built across 12 weeks (2026-05-14 ~ 2026-08-05). Open source from day 1.

**Asset coverage**:
- 🇰🇷 **Korean equities** (KIS Developers API, 4 alphas: Sector Rotation / Mean Reversion / Pair Trading / PEAD)
- 🇺🇸 **US equities & ETFs** (IBKR paper, 4 alphas: Factor Investing / Risk Parity / PEAD / Sector Momentum)
- 📈 **US options** (paper, 3 alphas: Covered Call / Volatility Risk Premium / Iron Condor)
- ₿ **Crypto** (38-day PoC archive — Liquidation Cascade / OU Mean-Reversion / Extreme Funding / Macro Event / Alt-coin MM)

**Production-grade primitives** (carried over from the 38-day PoC):
- **9-Layer Kill Switch** + 3 new layers (Alpha Decay / Regime / Overfit guards)
- **Deflated Sharpe Ratio (DSR)** + **Probability of Backtest Overfitting (PBO)**
- **Sensitivity Sweep** harness (108~576 cells per alpha)
- **Multi-agent orchestration** (Claude + Codex + Gemini)
- **Cross-exchange aggregation** archive (Binance + Bybit + OKX)

## 🚨 Why "Honest Failure"?

Most retail quant content is cherry-picked marketing. This repo publishes **the cold honest results, including the 38-day PoC that returned -15.1% on paper trading with 37.7% win rate across 191 trades**. We carry these lessons forward openly.

Academic references throughout (López de Prado / Fama-French / Black-Litterman / Avellaneda-Stoikov / Bailey et al. / Lakonishok / Jegadeesh-Titman). 300+ peer-reviewed citations across [Research](docs/research/) and [Design](docs/design/) docs.

## 📚 Documentation

- **[Research Phase](docs/research/)** — 16 cold-honest reports (~65,000 words, 300+ refs)
- **[Design Phase](docs/design/)** — 3 detailed specs (~41,500 words)
  - `01-architecture-spec.md` — System + Database + API contract
  - `02-alpha-specs-21.md` — 21 alphas, academic + code
  - `03-12week-daily-plan-and-milestones.md` — 84-day daily plan
- **[ROADMAP](ROADMAP.md)** — Week 1~12 milestones (live updated)
- **[ARCHITECTURE](ARCHITECTURE.md)** — System overview
- **[Live Dashboard](https://heoyesol.kr/quant)** *(deploying)* — Real-time paper trading metrics

## 🚀 Quick Start (5 minutes)

```bash
# Clone
git clone https://github.com/Yesol-Pilot/quant-poc-multi-asset
cd quant-poc-multi-asset

# Install
pnpm install              # Node.js workspaces
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]     # Python packages

# Run sample backtest (A12 KOSPI Mean Reversion, daily-bar)
pnpm backtest:a12

# Start live dashboard locally
pnpm dev
# → http://localhost:3000
```

Full instructions: [docs/getting-started.md](docs/getting-started.md) *(coming Week 1)*

## ⚠️ Disclaimer (Educational Purpose Only)

This is an **educational and research artifact**. **NOT financial advice. NOT investment recommendation. NOT a fiduciary product**. The author is not a registered investment advisor under Korean Financial Investment Services and Capital Markets Act (자본시장법) or US Investment Advisers Act. Use at your own risk. Past hypothetical paper-trading results do not guarantee future returns.

Korean readers: 자본시장법 + 자기자본 운용 가이드 준수. 본 코드를 활용한 외부 자금 운용 / 자문 / 리딩은 미등록 투자자문업 위반 (3년 이하 징역 또는 1억원 벌금).

See [DISCLAIMER.md](DISCLAIMER.md) for full statement.

## 🏗️ Status

| Week | Phase | Status |
|---|---|---|
| W1 (5/14~) | Setup + GitHub public + Live page scaffold | 🟢 in progress |
| W2~3 | KIS API integration + A11/A12 build | ⏳ pending |
| W4~6 | A13/A14 + IBKR paper + A15~A17 | ⏳ |
| W7~8 | Options (A19~A21) + integration | ⏳ |
| W9~10 | DSR/PBO + Sensitivity Sweep + Paper 1 draft | ⏳ |
| W11~12 | SSRN + ReScience submission + Hacker News launch | ⏳ |

Live progress: [ROADMAP.md](ROADMAP.md) (auto-updated weekly).

## 📜 License

MIT. See [LICENSE](LICENSE).

## 🙏 Acknowledgments

Built on the shoulders of the global quant academic community. Key academic references (full list in [docs/research/06-academic-references.md](docs/research/06-academic-references.md)):
- **Marcos López de Prado** (Cornell / ADIA Lab) — DSR, PBO, ML in Finance
- **Eugene Fama & Kenneth French** (Chicago Booth) — 5-factor model
- **Fischer Black & Robert Litterman** (Goldman Sachs) — Bayesian asset allocation
- **Marco Avellaneda & Sasha Stoikov** (NYU) — HFT market making
- **Ernest Chan** (QTS Capital) — Algorithmic Trading practitioner

---

## 한국어

### 이게 뭐냐

**1인 AI 네이티브 멀티 자산군 quant portfolio** — 12주 build (2026-05-14 ~ 2026-08-05). 첫날부터 오픈 소스. 학술적으로 엄격하게.

**자산군**:
- 🇰🇷 한국 주식 / ETF (KIS Developers API, 4 알파)
- 🇺🇸 미국 주식 / ETF (IBKR paper, 4 알파)
- 📈 미국 옵션 (paper, 3 알파)
- ₿ Crypto (38일 PoC 아카이브, 5 알파)

### Honest Failure 의 의미

대다수 retail quant 콘텐츠는 cherry-pick 마케팅. 본 repo 는 **38일 PoC 가 페이퍼 트레이딩에서 -15.1% / WR 37.7% / 191 trades** 라는 cold honest 결과 그대로 publish. 이 학습을 열린 마음으로 다음 phase 에 적용.

### 면책 사항 (교육 목적)

본 repo 는 **교육 + 연구 산출물**이며 투자 자문 / 추천 / 수익 보장이 아닙니다. 자본시장법 / 자본시장과금융투자업에관한법률 등 한국 규제 준수.

### 라이센스

MIT. 자세한 내용은 [LICENSE](LICENSE).

---

---

## About

Built by **[Yesol Heo](https://heoyesol.kr)** as part of **[Neo Genesis](https://neogenesis.app)** ([Q139569680](https://www.wikidata.org/wiki/Q139569680)) — a 1-person AI-native operating company running 11 SBUs under one autonomous AI orchestrator.

- 🌐 **[neogenesis.app](https://neogenesis.app)** — main site (11 live SBUs)
- 🤗 **[neogenesislab](https://huggingface.co/neogenesislab)** — 9 open datasets (CC-BY-4.0)
- 📚 Wikidata: **[Q139569680](https://www.wikidata.org/wiki/Q139569680)** (organization) · **[Q139569708](https://www.wikidata.org/wiki/Q139569708)** (founder)
- 💼 GitHub: **[@Yesol-Pilot](https://github.com/Yesol-Pilot)** · Portfolio: **[heoyesol.kr](https://heoyesol.kr)**


**Maintained by [Yesol Huh (허예솔)](https://github.com/yesol-pilot)**
[GitHub](https://github.com/yesol-pilot) · [Live Dashboard](https://heoyesol.kr/quant)

*This site focuses on the project. For author identity / career inquiries, see [heoyesol.kr](https://heoyesol.kr) (separate main site).*
