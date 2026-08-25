# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Current status, delivery goals, and open follow-ups live in `PROJECT.md` — this file covers only durable technical/architecture facts.

Dovilė Jakniūnaitė's personal academic website — a Hugo Blox (Academic CV starter) static site, bilingual (Lithuanian default, English second). Deployed via GitHub Pages (`.github/workflows/deploy.yml`) with Netlify configured as an alternate (`netlify.toml`). Lithuanian-first launch is the current priority; English parity is a deliberate later layer, so LT and EN content trees are not expected to mirror each other yet.

## Commands

Run from repo root (`pnpm` is the package manager):

- `pnpm install` — install JS dependencies.
- `pnpm run dev` — local dev server (`hugo server --disableFastRender`).
- `pnpm run build` — production build: `hugo --minify` then Pagefind indexing.
- `pnpm run pagefind` — rebuild the Pagefind search index over `public/` (build output must exist first).

There is no lint/test suite. Verification is a clean `pnpm run build` plus manual checks against `DESIGN.md`/`PRODUCT.md` intent (see Working Notes below).

`update_publications.py` is a standalone helper for reconciling imported publication data (type mapping, auto-tagging, summary extraction) — not part of the build pipeline; a related CI job is `.github/workflows/import-publications.yml`.

## Architecture

- **Content is bilingual by directory, and the two languages use different URL/folder vocab, not just different locales.** LT: `content/lt/{authors,blogas,destymas,events,projektai,publikacijos,slides}`. EN: `content/en/{authors,blog,events,projects,publications,slides}`. `defaultContentLanguage: lt`, `defaultContentLanguageInSubdir: true` (`config/_default/languages.yaml`, `hugo.yaml`). When adding a page type, check whether it needs both trees or is LT-only for now.
- **Layout overrides are per-language-slug**, not shared: `layouts/publications/list.html` (EN) vs `layouts/publikacijos/list.html` (LT) vs `layouts/publication_types/{list,term}.html`. Editing one does not affect the other — this is a common source of "why didn't my change show up" on the LT vs EN site.
- **Hugo Blox is pulled in as Hugo Modules**, not vendored: `config/_default/module.yaml` imports `github.com/HugoBlox/kit/modules/{blox,slides}` and `.../integrations/netlify`, then mounts `hugo-blox/blox/*` into `layouts/_partials/blox/`. Local `layouts/` and `assets/` are also self-mounted, meaning repo-root `layouts/`/`assets/` override module defaults of the same path. `go.mod`/`go.sum` exist only to pin these Hugo Modules, not for any Go code in this repo.
- **Design intent lives in three docs, read them before visual/structural changes**: `PRODUCT.md` (audience, brand personality, anti-references), `DESIGN.md` (color/type/component system — "The Public Seminar Room" — plus explicit Do/Don't rules like the Accent Rarity Rule and No Ghost Card Rule), `PROJECT.md` (current delivery goal, launch scope, known follow-ups, working rules). `PROJECT.md`'s "Working Rules" section is the operating contract for this repo: make changes in source files (never `public/`), check both language folders before structural changes, and record decisions/content plans back into `PROJECT.md`.
- **Custom styling lives in `assets/css/custom.css`**, layered on top of Hugo Blox's Tailwind v4 output — it's where the seminar-room palette/typography deviations from the stock template are implemented (see `data/fonts/seminar.yaml` for the custom font pack).
- **`.impeccable/`** holds a generated design-consistency snapshot (`design.json` + `critique/`/`live/`) used to verify visual/contrast changes against the design system — check it exists and consider regenerating after visual changes, but it's tooling output, not something to hand-edit.
- **Generated/dependency output — never hand-edit**: `public/` (build output), `resources/` (Hugo asset cache), `hugo_stats.json`, `node_modules/`.
- Author/profile metadata: `data/authors/me.yaml` (LT) and `data/authors/me.en.yaml` (EN).
- i18n UI strings (nav labels, etc., distinct from content): `i18n/lt.yaml`, `i18n/en.yaml`.

## Known repo-specific gotchas

- `baseURL` in `config/_default/hugo.yaml` currently points at `https://djdovile.github.io/`, matching the GitHub Pages workflow — this needs to change when `www.jakniunaite.lt` is connected (see `PROJECT.md` Known Follow-Ups).
- Some LT/EN content and author metadata still has known placeholder/encoding issues (mojibake, stray `:url`, `slug: men`, typo `indentity`) — see `PROJECT.md` for the current list rather than assuming everything is clean.
