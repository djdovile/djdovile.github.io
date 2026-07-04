# dj_hugo

## Purpose

This project is the user's personal webpage. It appears to be an academic/personal website for Dovile Jakniunaite, built with Hugo Blox Academic CV starter. The site includes profile/CV material, publications, blog posts, teaching pages, projects, events, and slides.

## Location

Project folder:

`MyProjects/dj_hugo`

## Technology

Reference: Hugo Blox documentation at https://hugoblox.com/docs/ and the installed Hugo Blox module templates in the local Hugo module cache should be checked when changing blocks or layout overrides.

- Static site generator: Hugo / Hugo Blox.
- Package manager: `pnpm`.
- Search indexing: Pagefind.
- Styling/tooling: Tailwind CSS via Hugo Blox.
- Deployment: GitHub Pages via `.github/workflows/deploy.yml`; Netlify is also configured in `netlify.toml`.
- Repository: this folder has its own `.git` directory.

## Key Commands

Run from `MyProjects/dj_hugo`:

- `pnpm install` - install JavaScript dependencies.
- `pnpm run dev` - start the local Hugo development server with `hugo server --disableFastRender`.
- `pnpm run build` - build the production site with Hugo minification and Pagefind indexing.
- `pnpm run pagefind` - rebuild the Pagefind search index for `public`.

## Structure

- `config/_default/` - Hugo and Hugo Blox configuration.
- `content/lt/` - Lithuanian site content.
- `content/en/` - English site content.
- `data/authors/me.yaml` - author/profile metadata.
- `assets/media/` - media processed by Hugo.
- `static/` - static files copied directly.
- `layouts/` - layout overrides and partials.
- `public/` - generated build output; avoid editing by hand.
- `update_publications.py` - helper script for publication-related updates.

## Current State

`MyProjects/dj_hugo` is the canonical workspace for DJ's Hugo personal webpage. The older `MyHugoPage` folder should not be treated as the active source.

The site is bilingual, with Lithuanian as the default language and English as the second language. Lithuanian-first content is the current priority; English parity can follow later.

As of 2026-07-02, the worktree contains an uncommitted implementation batch: LT project/course bundles, LT homepage text, publication type filter templates, reading-time/author-card suppression, remaining Hugo Blox demo-blog deletions, and `BLOG-LINK-REVIEW-2026-07-02.md`.

Verification state: clean Hugo build into a temporary folder passed; broken demo cite warnings are gone; `/lt/destymas/`, `/lt/projektai/`, `/lt/publikacijos/`, and publication-type pages rendered expected content; no rendered reading-time labels were found.

As of 2026-07-03, the homepage color pass moved the secondary wayfinding accent away from bright blue to a quiet green (`#506A52`), kept seminar red as a scarce action/active-state marker, added `assets/css/custom.css` for restrained link, archive-row, header, focus, and profile-button styling, and updated the local design register. Verification passed with a clean Hugo build, clean Impeccable detector output, and contrast checks above WCAG AA for body, muted, link, red, and white-on-red text pairs.

As of 2026-07-03, the homepage typeset pass replaced the generic `modern` Inter pack with a local `seminar` font pack (`Source Serif 4` for prose/headings, system sans for navigation and controls). The pass also tightened homepage reading measure, heading scale, publication citation title rhythm, metadata sizing, and archive-gateway prose spacing in `assets/css/custom.css`. The design register now treats typography as a public-seminar handout system rather than a generic Hugo Blox interface.

## Known Follow-Ups

- Confirm the preferred deployment target. `config/_default/hugo.yaml` currently uses `https://djdovile.github.io/`, matching the GitHub Pages workflow.
- Review visible mojibake/encoding issues in config and author files before publication.
- `public/`, `resources/`, `hugo_stats.json`, and `node_modules/` are generated or dependency output and are ignored; keep edits in source files.
- Test `pnpm run build` before deployment.

## Remaining Tasks To Review

- Review and edit the new Lithuanian project and course page wording before treating it as final public content.
- Review `BLOG-LINK-REVIEW-2026-07-02.md`; 13 checked link rows returned errors and need manual decision or later replacement.
- Replace or draft `content/lt/events/example/` and `content/lt/slides/example/`.
- Add English project/course pages later if bilingual parity is desired.
- Add `translationKey` values where real Lithuanian and English page pairs exist.
- Clean English homepage placeholder text and English author metadata later, including `slug: men`, the stray `:url`, and the typo `indentity`.
- Normalize blog author metadata from `admin` or empty author lists to `me` where appropriate.
- Review legacy root files `content/_index.md` and `content/experience.md`; archive or remove them if they are no longer used.
- Align Netlify and GitHub Pages deployment notes once the preferred production route is settled.

## Working Rules

Make content and configuration changes in source files, not in `public/`. Before changing site structure, check both language folders so Lithuanian and English stay aligned where intended. Record decisions, content plans, and accepted changes in this file.
