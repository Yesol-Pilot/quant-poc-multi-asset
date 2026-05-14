# ADR-0002 — Pin pnpm via `npx --yes pnpm@9.15.0` in Vercel build

- Status: Accepted
- Date: 2026-05-14 (W1 D5)
- Decider: Strategy Lead (Claude Opus 4.7), autonomous G1
- Supersedes: —
- Superseded by: —

## Context

The first 4 Vercel production builds for this repo all failed at
`ERR_PNPM_UNSUPPORTED_ENGINE` (commits `109493c`, `3885148`, `4643615`,
`188a4ad`).

The repo declares `engines.pnpm >=9.0.0` and `packageManager: pnpm@9.15.0`
in the root `package.json`. The dashboard lives at `apps/live-dashboard/`
(monorepo `rootDirectory`).

The build failures revealed three layered problems:

1. **Vercel reads `package.json` at `rootDirectory`, not the repo root**, for
   framework + engine detection. `apps/live-dashboard/package.json` had no
   `engines` and no `packageManager`. Without those signals, Vercel selected
   pnpm 6.35.1 (its oldest bundled default).
2. **Vercel's bundled pnpm 6 fails `engines.pnpm >=9.0.0`** (which the root
   `package.json` does declare). The build stops before the `installCommand`
   gets to run a workaround.
3. **Even `npm install -g pnpm@9.15.0` inside `installCommand` did not help**.
   The global install succeeded ("added 1 package in 1s"), but the next
   `pnpm install` line resolved to the system pnpm 6 because
   `/usr/local/bin/pnpm` outranks npm's global bin on Vercel's PATH.

## Decision

Use `npx --yes pnpm@9.15.0 …` as a one-shot bypass in both `installCommand`
and `buildCommand`:

```json
{
  "installCommand": "cd ../.. && npx --yes pnpm@9.15.0 install --frozen-lockfile=false",
  "buildCommand":   "cd ../.. && npx --yes pnpm@9.15.0 --filter @qpm/live-dashboard build"
}
```

`npx` resolves a fresh pnpm 9.15.0 from npm cache and invokes it directly,
ignoring whatever pnpm exists on the system PATH.

## Consequences

- Each build pays a small startup cost (~1s) for npx to resolve pnpm. Vercel
  caches `~/.npm`, so the actual pnpm tarball is only downloaded once per
  build cache lifetime.
- We do not depend on `corepack`. Corepack's signature verification has had
  TUF key-rotation issues on Node 22.12 (observed locally on
  `desktop-home`, `Error: Cannot find matching keyid`), which would have
  been a latent build risk if we'd relied on it.
- We do not depend on `apps/live-dashboard/package.json` carrying its own
  `engines.pnpm` / `packageManager` field. The single source of truth is the
  pinned version in `vercel.json`.
- Upgrading pnpm later is a one-line `vercel.json` edit, not a corepack dance.

## Alternatives considered

1. **Add `engines.pnpm` + `packageManager` to `apps/live-dashboard/package.json`** —
   would have let Vercel auto-detect pnpm 9. Rejected because it duplicates
   the root manifest and adds two more places that can drift.
2. **`corepack enable && corepack prepare pnpm@9.15.0 --activate`** —
   the "blessed" Node-built-in path. Rejected because:
   - the TUF signature failure observed on the developer's Node 22.12.0 suggests
     fragility in the wild,
   - Vercel's documentation defers to whatever pnpm it has shipped, which
     means relying on corepack on Vercel is poorly tested.
3. **Use Vercel project-dashboard `installCommand` instead of `vercel.json`** —
   rejected because Vercel-dashboard settings live outside source control,
   and we want the entire build contract checked into git.
4. **`npx --yes pnpm@9.15.0`** ✅ chosen — bypasses all of the above with
   one well-understood mechanism.

## References

- Failed build IDs that proved the layered chain:
  `dpl_Ce5o4eA7ZEGnfCz187eLWTh2bYp9`, `dpl_5oHnkH8RjFJhXQdVvexMh9m4kGjQ`,
  `dpl_BRRAHYzqHReHNENnUiT3rk5vuaGB`, `dpl_J1dTG4cxG7TU3hjujxNTE9marn97`.
- First green build: `dpl_J1dTG4cxG7TU3hjujxNTE9marn97`'s successor for commit
  `0e7e308`, then `0a759ff` after the CI-guard parity fix.
- Vercel docs on framework auto-detection (rootDirectory):
  https://vercel.com/docs/projects/project-configuration#rootdirectory
- pnpm corepack signature bug (observed local Node 22.12): the error string
  was `Cannot find matching keyid` with TUF cert payload.
