# Security Policy

> Production-grade security for an educational paper-trading repo.

## Supported Versions

This is an evolving 12-week build. Currently supported:
- `main` branch (rolling release) — security patches applied to head
- Tagged releases (`v0.x.y`) — patched only if currently maintained

## Reporting a Vulnerability

**DO NOT open public GitHub issues for security vulnerabilities.**

### How to Report

Email: **dpthf1537@gmail.com**
Subject: `[SECURITY] quant-poc-multi-asset — <short description>`

Include:
1. Type of vulnerability (e.g., credential leak, RCE, kill switch bypass)
2. Affected file(s) / commit hash
3. Steps to reproduce
4. Suggested fix (if any)

### Response

- Acknowledgement within **48 hours**
- Initial assessment within **7 days**
- Fix timeline depends on severity (Critical: 24h / High: 7d / Medium: 30d / Low: 90d)

### Disclosure

- Coordinated disclosure (we'll publish CVE if applicable)
- Reporter credited in CHANGELOG and SECURITY ADVISORIES (unless anonymity requested)
- No bug bounty program (this is a personal repo); thank-you note + public acknowledgment

---

## Threat Model

### High-priority threats

1. **Kill Switch bypass** — code paths that skip the 12-Layer Kill Switch
2. **Live mode in paper-only function** — accidentally connecting to TWS port 7496 (live) instead of 7497 (paper)
3. **Credential leak** — API keys in commits, logs, or generated reports
4. **Backtest manipulation** — silently rewriting historical data or overfitting parameters
5. **External code injection** — malicious dependencies or compromised LLM prompts in production runtime

### Medium-priority threats

6. **Supabase RLS bypass** — public API exposing internal tables
7. **Rate limit bypass** — public API endpoint exceeding documented limits
8. **Dependency vulnerabilities** — `pnpm audit` / `pip audit` findings
9. **DoS on public dashboard** — Vercel Edge rate-limit insufficient

### Low-priority threats

10. **Information disclosure in debug logs**
11. **CSRF on public API (read-only)**

---

## Active Security Controls

### 1. Kill Switch (12-Layer)

Inherited from 38-day PoC (commit `c8f4e7b`). 12 layers, each independently armed:
- L1: Order Rate Governor
- L2: Max Drawdown Halt
- L3: Correlation Killer
- L4: Exchange Health Guard
- L5: MMR Monitor
- L6: ADL Queue Monitor
- L7: Environment Guard (paper/live mode check)
- L8: Stablecoin Depeg Guard (archived)
- L9: Funding Spike Guard (archived)
- L10: **Alpha Decay Detector** (NEW)
- L11: **Regime Detector** (NEW)
- L12: **Overfit Guard** (PBO threshold) (NEW)

Tests: Each layer has 5+ dedicated test cases. `enforce_paper_only()` is a CI-blocking guard.

### 2. Credential Isolation

- **Supabase Vault**: KIS AppKey/AppSecret, IBKR account (paper only)
- **Vercel env**: Gemini API key, Supabase service role key
- **GitHub Actions secrets**: only what's needed for CI
- **`.env*` files**: in `.gitignore`, never committed

### 3. CI/CD Guards

- `pnpm audit` + `pip audit` on every PR
- ESLint security plugin
- `secrets-detector` (custom) blocks AWS keys, API keys, JWTs in diffs
- Branch protection: `main` requires 1 review + all checks pass

### 4. Disclaimer Enforcement

Every backtest result page, dashboard, and API response includes the educational-purpose disclaimer.

### 5. Audit Chain

SHA-256 audit chain (inherited from SecurPilot) for:
- All Kill Switch trigger events
- All paper trade entries/exits
- All deployment hashes

---

## Out of Scope (Not Vulnerabilities)

- Educational disclaimer is not legal advice (use a real lawyer for jurisdiction-specific compliance)
- Past backtest performance does not predict future returns (this is by design)
- Alpha decay over time (this is the central thesis of the repo)
- Documentation typos (use a regular issue/PR)

---

## Acknowledgments

Security-related contributions (responsibly disclosed) will be acknowledged here:

*No reports yet.*

---

**Maintainer**: 허예솔 (Yesol Huh) <dpthf1537@gmail.com>
**Last updated**: 2026-05-14
