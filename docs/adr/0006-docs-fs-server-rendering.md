# ADR-0006 — Render docs/ markdown via fs at build time, not a CMS

- Status: Accepted
- Date: 2026-05-14 (research/design wire-up)
- Decider: Strategy Lead (autonomous G1)
- Supersedes: —
- Superseded by: —

## Context

The project has 21 long-form documents (17 research reports + 4 design specs,
~65,000 words) living as markdown in `docs/research/` and `docs/design/`. They
needed to become real, indexable, deep-linked pages on the live site
(`/research/[slug]`, `/design/[slug]`).

Options for sourcing the content into Next.js:

1. **A headless CMS** (Contentful, Sanity, Notion API). Content lives off-repo.
2. **MDX with per-file imports.** Each doc becomes a `.mdx` module imported by
   a route. Requires converting the markdown to MDX and wiring imports.
3. **Filesystem read at build time.** A server-only util reads `docs/**/*.md`
   from the repo, parses title/description, and `react-markdown` renders the
   body. Content stays in the repo as plain markdown.

## Decision

Filesystem read at build time. `apps/live-dashboard/src/lib/docs.ts` uses
`node:fs` to read the markdown from two levels up (`../../docs` relative to the
app's `process.cwd()`), and the `[slug]` routes use `generateStaticParams` +
`dynamicParams = false` to prerender exactly the docs that exist (404 for
anything else). Rendering is `react-markdown` + `remark-gfm` + `rehype-slug` +
`rehype-autolink-headings`.

## Consequences

- **Single source of truth.** The markdown in `docs/` is what GitHub shows AND
  what the site renders. No sync step, no CMS drift, no second copy to keep
  current. A doc edit is a git commit, reviewed like code.
- **Zero runtime cost.** Pages are SSG (prerendered at build). No CMS API calls,
  no runtime fs access, no database. Hosting cost stays at Vercel-static $0.
- **Slug = filename.** `docs/research/03-kis-api-feasibility.md` →
  `/research/03-kis-api-feasibility`. Stable, predictable, no slug field to
  manage.
- **Coupling to repo layout.** `docs.ts` resolves `../../docs` from the app dir.
  If the monorepo layout changes (app moves), this path must update. Mitigated
  by a single constant + an empty-state UI that says "build context did not
  include docs/" rather than crashing.
- **No draft workflow.** Every markdown file in `docs/research|design` is
  published. Drafts must live elsewhere (e.g. `docs/_drafts/`, excluded by the
  reader's directory scan) until ready. Acceptable: the project's content is
  deliberately public-first.
- **Large-page performance.** The biggest doc (~12K words) renders to ~378 KB
  and scores Lighthouse Performance 88 (vs 99 on the hero). Acceptable for a
  deep-link doc page; W3+ may add a ToC sidebar / pagination if it matters.

## Alternatives considered

1. Headless CMS — rejected: off-repo content, sync drift, runtime cost, a second
   system to secure.
2. MDX per-file imports — rejected: requires md→mdx conversion + import wiring
   for 21 files, and we don't need JSX-in-markdown for these documents.
3. **fs read at build time** ✅ chosen.

## References

- `apps/live-dashboard/src/lib/docs.ts`
- `apps/live-dashboard/src/components/MarkdownBody.tsx`
- `apps/live-dashboard/src/app/research/[slug]/page.tsx`
- `apps/live-dashboard/src/app/sitemap.ts` (consumes getDocList for slugs)
