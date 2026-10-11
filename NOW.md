# NOW.md

Last updated: 2026-10-11 (after push `c634f92`)

## Status
First Lithuanian version is on `main` and deploying to GitHub Pages (`djdovile.github.io`). DJ is reviewing content and tags by hand before real use; further changes only for bugs. Local `pnpm run check` reports 0 errors, 2 expected warnings.

## Open (DJ's side)
- Confirm the Actions run for `c634f92` is green (Sim cannot see it).
- After deploy, spot-check: Chain of Emergencies DOI link (no brackets), new Feminizmas and BA theory course pages, drafts hidden.
- Review drafts: blog post `vienybes-pasakojimai-ir-tvarkos-gynyba` and EN `Narrating Unity` (`draft: true`).
- Connect `www.jakniunaite.lt`, then change `baseURL` in `config/_default/hugo.yaml`.
- English site hidden: `language_switcher: true` in `params.yaml` + restore English menu entry when ready. EN pages link to a non-existent `/en/blogas/index.xml` (footer RSS).
- Global Society volume/issue not assigned yet; no MIDAS dataset entry on the site.

## Optional
- Contrast check of ochre/teal on every page type and dark mode.
- `.impeccable/design.json` still has old CSS variable names.
- Run `pnpm run check` (fast) or `pnpm run check:build` before each push.
