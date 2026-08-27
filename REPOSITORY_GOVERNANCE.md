# Repository Governance Contract

Policy ID: `ng-repo-governance/1.0.0`
Last reviewed: 2026-08-27

## Identity

- Repository: `Yesol-Pilot/quant-poc-multi-asset`
- Lifecycle class: `financial-research-poc-pending-review`
- Current owner: `Yesol-Pilot`
- Intended owner: `PENDING_REVIEW`
- Canonical branch: `main`
- Visibility: `public`
- Transfer state: `PENDING_FINANCIAL_AND_IP_REVIEW`
- Production status: `POC_ONLY`

`UNKNOWN` means not independently verified and must never be reported as PASS.

## Decision boundary

This is a public multi-asset quantitative proof of concept. Public source does not establish a company trading product, financial advice, validated research, live execution authority, or ownership by NeoGenesis.

- Data providers, licenses, instruments, currencies, time zones, corporate actions, fees, taxes, liquidity, leverage, model assumptions, and benchmark methodology require explicit documentation.
- Backtests and examples may contain look-ahead, survivorship, selection, overfitting, and execution bias.
- Broker credentials, account data, positions, private strategy parameters, transactions, and live endpoints are prohibited.
- No live order, transfer, withdrawal, leverage, or irreversible account action is authorized by this repository.

## Required remediation

- [ ] Document research purpose, data sources and rights, assumptions, benchmark, supported assets, and prohibited uses.
- [ ] Run full-history secret, dependency, license, dataset-rights, numerical, public-claim, and generated-output audits.
- [ ] Add decimal precision, timezone, currency, missing-data, corporate-action, fee, slippage, leakage, walk-forward, reconciliation, sandbox, kill-switch, and rollback tests.
- [ ] Decide `TRANSFER_TO_NEOGENESISAI_RESEARCH`, `KEEP_PERSONAL_RESEARCH`, `REPLACED`, or `ARCHIVE`.
- [ ] Preserve a clear POC-only and not-financial-advice boundary while public.

## Exit criteria

Transfer requires an active company research purpose, lawful data rights, reproducible methodology, bounded non-live authority, and named owner. Otherwise the repository remains personal research or is archived.

The presence of this file alone is not investment or performance approval.
