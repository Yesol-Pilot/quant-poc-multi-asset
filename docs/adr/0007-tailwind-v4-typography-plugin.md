# ADR-0007 — Tailwind v4 CSS-first config + `@plugin` for typography

- Status: Accepted
- Date: 2026-05-14 (research/design wire-up)
- Decider: Strategy Lead (autonomous G1)
- Supersedes: —
- Superseded by: —

## Context

The research/design pages render long-form prose via `react-markdown`. Raw
markdown HTML (`<h2>`, `<p>`, `<ul>`, `<table>`, `<code>`) needs typographic
styling. The standard tool is `@tailwindcss/typography` (the `prose` classes).

The wrinkle: this project uses **Tailwind v4**, which moved from the v3
JavaScript config (`tailwind.config.js` with a `plugins: [require(...)]`
array) to a **CSS-first config**. There is no `tailwind.config.js`. The
`@theme` block and design tokens live in `globals.css`. So the v3 way of
registering the typography plugin does not apply.

## Decision

Register the typography plugin with Tailwind v4's `@plugin` directive directly
in `globals.css`:

```css
@import "tailwindcss";
@plugin "@tailwindcss/typography";
```

Apply `prose prose-neutral dark:prose-invert max-w-none` (plus a few
`prose-*` modifiers to align code blocks with the project's `--color-muted`
token) on the markdown container in `MarkdownBody.tsx`. Heading anchors injected
by `rehype-autolink-headings` get a `.heading-anchor` utility (hover-reveal `#`)
defined in the `@layer utilities` block.

## Consequences

- **No `tailwind.config.js`.** The whole Tailwind config — tokens, plugins,
  utilities — is in `globals.css`. One file to read, consistent with the v4
  CSS-first model already used for the OKLCH design tokens.
- **Plugin version pin.** `@tailwindcss/typography ^0.5.16` is the first line
  that reliably supports the v4 `@plugin` directive. Older 0.5.x may not.
- **`dark:prose-invert` depends on the dark class strategy.** The project's
  tokens are CSS-variable-based; `prose-invert` is wired but full dark-mode
  toggle is a W3+ concern. In light mode (current default) `prose-neutral`
  governs.
- **Risk: plugin/engine version skew.** A future Tailwind v4 minor could change
  `@plugin` resolution. Mitigated by the lockfile (pnpm-lock.yaml committed) so
  the build is reproducible until we deliberately bump.

## Alternatives considered

1. **v3-style `tailwind.config.js` with `plugins: [require('@tailwindcss/typography')]`**
   — rejected: reintroduces a JS config file that fights the v4 CSS-first model
   and the existing `@theme` setup.
2. **Hand-rolled prose CSS** (style every `<h2>/<p>/<table>` manually) —
   rejected: reinvents a well-tested plugin, high maintenance, easy to get
   inconsistent.
3. **`@plugin "@tailwindcss/typography"` in globals.css** ✅ chosen.

## References

- `apps/live-dashboard/src/app/globals.css` (`@plugin` + `.heading-anchor`)
- `apps/live-dashboard/src/components/MarkdownBody.tsx` (`prose` classes)
- Tailwind v4 `@plugin`: https://tailwindcss.com/docs/functions-and-directives#plugin
- @tailwindcss/typography: https://github.com/tailwindlabs/tailwindcss-typography
