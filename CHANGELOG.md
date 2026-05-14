# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

Week 1 (5/14 ~ 5/20) — Setup phase.

### Added
- Initial directory structure
- LICENSE (MIT)
- DISCLAIMER (Korean + English)
- README v0 (Korean + English)
- .gitignore (Node.js + Python + Vercel + Supabase)
- ROADMAP.md (12-week milestone tracking)
- ARCHITECTURE.md (high-level system overview)
- CONTRIBUTING.md
- SECURITY.md (threat model + Kill Switch reuse)
- CODE_OF_CONDUCT.md (Contributor Covenant v2.1)
- CHANGELOG.md (this file)

### Referenced
- 16 Research reports from `docs/research/` (linked from README)
- 3 Design specs from `docs/design/` (linked from ARCHITECTURE.md)

---

## Pre-history

This project is a **continuation of a 38-day Crypto PoC** (2026-04-05 ~ 2026-05-12) that resulted in:
- 191 paper trades, 37.7% win rate, -15.1% paper PnL
- Production-grade 9-Layer Kill Switch (commit `c8f4e7b`)
- Cross-exchange aggregation (Binance + Bybit + OKX, commits `c8f4e7b` ~ `4849d84`)
- Honest closure (2026-05-12) and pivot to **12-week multi-asset rebuild**

That PoC's lessons inform every alpha and Kill Switch layer in this repo.

For full PoC retrospective: see [docs/research/07-competitive-analysis.md](docs/research/07-competitive-analysis.md) and the upcoming **Paper 1 (SSRN)**.

---

[Unreleased]: https://github.com/Yesol-Pilot/quant-poc-multi-asset/compare/v0.0.0...HEAD
