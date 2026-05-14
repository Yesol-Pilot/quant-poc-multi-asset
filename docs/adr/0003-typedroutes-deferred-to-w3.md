# ADR-0003 — Defer Next.js `typedRoutes` to W3+

- Status: Accepted
- Date: 2026-05-14 (W1 D5)
- Decider: Strategy Lead (Claude Opus 4.7), autonomous G1
- Supersedes: —
- Superseded by: (W3+ ADR when typedRoutes is re-enabled)

## Context

Next.js 15 ships an experimental `typedRoutes` mode that statically types the
`href` prop of `<Link>` against the project's actual route table. Enabling
it gives compile-time errors for typos and dead links.

The W1 landing page (`apps/live-dashboard/src/app/page.tsx`) renders a "Documentation"
grid of placeholder Links:

```tsx
{[
  { href: '#', label: 'Research (16 reports)', note: 'Coming W2' },
  { href: '#', label: 'Design Specs (4)',     note: 'Coming W2' },
  { href: '#', label: 'Papers (SSRN/ReScience)', note: 'Coming W12' },
  { href: '#', label: 'Blog', note: 'Coming W2' },
].map((l) => (
  <Link href={l.href} ...>
```

With `experimental.typedRoutes: true`, the build fails with:

> `./src/app/page.tsx:124:15
> Type error: Type 'string' is not assignable to type 'UrlObject | RouteImpl<string>'.`

because TypeScript can't prove `l.href` (`string` from the array) is a valid
route. The first Vercel deploy that got far enough to compile (`dpl_J1d...`,
commit `188a4ad`) failed on this exact error.

The placeholder hrefs *will* be replaced by real route strings as W2 (research
hub), W3 (dashboard wire-up), W11 (public API) land, but for W1 they're
intentional `#` anchors so the cards render without 404s.

## Decision

Disable `typedRoutes` for W1. Add an explicit comment in `next.config.ts`
describing when to re-enable.

```ts
// typedRoutes intentionally disabled for W1 scaffold:
// - Landing page has placeholder `href: '#'` strings in a .map() that
//   can't satisfy the RouteImpl<string> constraint.
// - Re-enable in W3+ once /dashboard has real typed routes wired.
```

Re-enable trigger: when the landing page's documentation grid points to real
routes (e.g. `/research`, `/design`, `/papers`, `/blog`) and the only `'#'`
placeholders remaining are removed.

## Consequences

- W1 build is green without ergonomic gymnastics (no `as Route` casts
  scattered through the page).
- Typo'd `<Link href="/abuot">` won't fail the build during W1~W2. The
  consequence is small because we have only 5 routes (`/`, `/about`,
  `/disclaimer`, `/dashboard`, plus `/not-found`).
- W3 ADR will document the re-enable and any cast hatches needed for
  dynamic alpha pages (`/alphas/[id]`).

## Alternatives considered

1. **Cast each placeholder `href` to `Route`** — works but litters the
   landing page with `as Route` and trains contributors to defeat the type
   system. Rejected.
2. **Lift placeholders to a constant typed as `Route[]`** — cleaner cast,
   but still adds friction for a 4-week-long temporary state. Rejected.
3. **Switch placeholders from `<Link>` to `<a href="#">`** — defeats client
   navigation for the eventual real links and creates a second migration
   later. Rejected.
4. **Disable for W1, re-enable in W3+ ADR** ✅ chosen.

## References

- Build failure: `dpl_J1dTG4cxG7TU3hjujxNTE9marn97` (commit `188a4ad`).
- Next.js docs (typedRoutes is stable in 15.5+, moved out of `experimental`):
  https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes
- `next.config.ts` carries the disable + re-enable comment in source.
