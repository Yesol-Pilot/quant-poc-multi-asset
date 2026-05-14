# Architecture Decision Records

This directory captures the decisions that shape `quant-poc-multi-asset`.
The format is loosely based on Michael Nygard's
[ADR template](https://github.com/joelparkerhenderson/architecture-decision-record).

## Index

| #  | Date       | Status   | Decision                                  |
|----|------------|----------|-------------------------------------------|
| [0001](./0001-ib_async-not-ib_insync.md) | 2026-05-14 | Accepted | Use `ib_async` (NOT `ib_insync`) for IBKR |
| [0002](./0002-npx-pnpm-for-vercel.md)    | 2026-05-14 | Accepted | Pin pnpm via `npx --yes pnpm@9.15.0` in Vercel build |
| [0003](./0003-typedroutes-deferred-to-w3.md) | 2026-05-14 | Accepted | Defer Next.js `typedRoutes` to W3+ |

## When to write a new ADR

Write one whenever you'd want to grep for the *why* of a decision six months
from now. Specifically:

- A non-obvious dependency choice (which IBKR client? which option-pricing lib?)
- A build / deploy pattern that took more than one attempt to land
- A feature deferral with a re-enable trigger
- A kill-switch invariant or capital allocation rule
- An academic methodology choice (DSR vs deflated PSR, PBO vs CSCV)

The cost of writing a one-page ADR is much smaller than the cost of
discovering, six weeks later, that no one remembers why the build fails when
they revert that "obviously unnecessary" config change.
