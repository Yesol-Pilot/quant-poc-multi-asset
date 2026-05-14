# ADR-0001 — Use `ib_async` (NOT `ib_insync`) for IBKR integration

- Status: Accepted
- Date: 2026-05-14 (W1 D1)
- Decider: Strategy Lead (Claude Opus 4.7), with owner approval pre-W1
- Supersedes: —
- Superseded by: —

## Context

The 38-day crypto PoC closure note flagged a forthcoming IBKR integration. The
historical Python client for the IBKR TWS API is `ib_insync` (Ewald de Wit,
2017–2022). It was the de facto standard for retail Python IBKR work.

In 2024, the maintainer publicly deprecated `ib_insync` and stopped accepting
PRs. A community fork named **`ib_async`** picked up active maintenance,
fixing several long-standing bugs and adding native asyncio compatibility for
Python 3.11+.

The repo's `pyproject.toml` had to pin exactly one of these as a dependency
for the W4+ IBKR paper layer (A15~A21).

## Decision

Use **`ib_async`** (`>=2.0`). Do not use `ib_insync`.

This is enforced by:

- `pyproject.toml` declares `ib_async>=2.0` in `[project.dependencies]`.
- `tests/test_smoke.py::test_pyproject_well_formed` asserts the string
  `"ib_async"` is present in `pyproject.toml`. The same assertion is the
  reason a future PR that re-introduces `ib_insync` would fail CI.

## Consequences

- Existing `ib_insync` tutorials, code snippets, and Stack Overflow answers
  need a thin translation step. The APIs are mostly the same (the fork
  preserved compatibility intentionally), but the import path and a few async
  helpers differ.
- Long-term maintenance risk is reduced: `ib_async` is actively maintained.
- No reverse-compatibility issue, because we have zero existing IBKR code.

## Alternatives considered

1. **`ib_insync`** (deprecated, maintainer-blessed end-of-life)
2. **Raw `ibapi`** (official IBKR Python SDK, callback-style — verbose,
   no async, hard to test in isolation)
3. **`ib_async`** ✅ chosen

`ibapi` raw is a long-term option if `ib_async` ever stagnates, but the
ergonomic gap is large enough that we'd build a wrapper anyway, so we let the
community fork own that wrapper.

## References

- `ib_async`: https://github.com/ib-api-reloaded/ib_async
- `ib_insync` deprecation: https://github.com/erdewit/ib_insync (archived)
- `pyproject.toml` line where the dep lives: search for `"ib_async"`
