# NOW.md

Last updated: 2026-10-12 (local `main` is 17 commits ahead of `origin`, last pushed `c634f92`; nothing pushed since)

## Status
First Lithuanian version is live on GitHub Pages (`djdovile.github.io`) as of `c634f92`. Since then 17 local commits (tags, publication types, cite.bib, sorting, Topics pages, book covers and Knygos section, preface and contents on two book pages) wait for DJ's go-ahead to push. `pnpm run check` 0 errors, 2 expected draft warnings; `cite:check` 0 errors, 2 intended warnings. One uncommitted edit is DJ's own (blank line removed in the Ambicingas front matter).

## Next action
DJ decides on the push. Then: confirm the Actions run is green and spot-check live (cover images, Knygos section on the home page, Topics pages, filter buttons, "Atnaujinta" dates, drafts hidden, Chain of Emergencies DOI link).

## Open (DJ's side)
- Replace the Ambicingas cover (only a 642x336 photo exists, soft); NATO cover (538x768) and Miniotaite cover (photo) are acceptable but not sharp.
- Restart `pnpm run dev` so "Atnaujinta" reads the new git dates (the dev server reads git once at start).
- Review drafts: blog post `vienybes-pasakojimai-ir-tvarkos-gynyba` and EN `Narrating Unity` (add volume/issue when assigned, then `python scripts/cite_bib.py --write --force giedraitytejakniunaite2026` and copy to EN).
- Connect `www.jakniunaite.lt`, then change `baseURL` in `config/_default/hugo.yaml`.
- English site hidden (`language_switcher: false`); EN pages are placeholders in places. EN home page has no Knygos section yet.
- Dedicated pages for the other chapters in Ambicingas (only DJ's two are linked).

## Optional
- Contrast check of ochre/teal on every page type and dark mode.
- `.impeccable/design.json` is older than `DESIGN.md` (`/impeccable document`).
- Run `pnpm run check` (fast) or `pnpm run check:build` before each push.
