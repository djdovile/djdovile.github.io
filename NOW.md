# NOW.md

Last updated: 2026-10-11

## Status
First version of the Lithuanian site is built and pushed (last commit `a5ecf8a`, `main`, working tree clean). DJ will now review content and tags by hand, then deploy and start using the site. No further changes planned except bugs she notices.

## Open (DJ's side)
- Review content and tags manually.
- Connect `www.jakniunaite.lt`, then change `baseURL` in `config/_default/hugo.yaml` (still `https://djdovile.github.io/`).
- Draft post `content/lt/blogas/vienybes-pasakojimai-ir-tvarkos-gynyba` is `draft: true`, awaiting her review.
- Check the Actions tab for a green deploy (not verified by Sim).
- English site hidden: to bring it back set `language_switcher: true` in `params.yaml` and restore the English menu entry.
- Global Society volume/issue not assigned yet; no MIDAS dataset entry on the site.

## Not done / optional
- Contrast check of ochre and teal on every page type and in dark mode.
- `.impeccable/design.json` has the new palette but old CSS variable names.
- Pre-push check script (`pnpm run check`) offered, not requested. Build it only if DJ says yes.
- Page background (warm cream vs slide peach/teal) left as is.
