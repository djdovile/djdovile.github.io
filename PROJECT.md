# dj_hugo

## Purpose

This project is the user's personal webpage. It appears to be an academic/personal website for Dovile Jakniunaite, built with Hugo Blox Academic CV starter. The site includes profile/CV material, publications, blog posts, teaching pages, projects, events, and slides.

## Location

Project folder:

`MyProjects/dj_hugo`

## Technology

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

The site is bilingual, with Lithuanian as the default language and English as the second language. `config/_default/languages.yaml` points Lithuanian to `content/lt` and English to `content/en`.

The Git worktree currently contains many existing changes, including deleted old single-language `content/...` paths and new `content/en/...` and `content/lt/...` paths. Treat these as existing user work. Do not revert them unless the user explicitly asks.

## Known Follow-Ups

- Confirm the preferred deployment target. `config/_default/hugo.yaml` currently uses `https://djdovile.github.io/`, matching the GitHub Pages workflow.
- Review visible mojibake/encoding issues in config and author files before publication.
- `public/`, `resources/`, `hugo_stats.json`, and `node_modules/` are generated or dependency output and are ignored; keep edits in source files.
- Test `pnpm run build` before deployment.

## Remaining Tasks To Review

- Clean or draft starter/demo Lithuanian blog posts under `content/lt/blogas/`, especially Hugo Blox examples.
- Check whether the homepage `Knygos` block should filter only book-type publications; it now renders from `content/lt/publikacijos/`, but the current filter may include non-book publications.
- Replace or draft `content/lt/events/example/` and `content/lt/slides/example/`.
- Decide whether to populate `Dėstymas` and `Projektai` now, or temporarily hide those menu items.
- Add `translationKey` values where real Lithuanian and English page pairs exist.
- Clean English author metadata later, including `slug: men`, the stray `:url`, and the typo `indentity`.
- Decide whether to disable the newsletter CTA until there is a real URL.
- Replace footer placeholder text.
- Normalize blog author metadata from `admin` or empty author lists to `me` where appropriate.
- Review legacy root files `content/_index.md` and `content/experience.md`; archive or remove them if they are no longer used.
- Align Netlify and GitHub Pages deployment notes once the preferred production route is settled.

## Working Rules

Make content and configuration changes in source files, not in `public/`. Before changing site structure, check both language folders so Lithuanian and English stay aligned where intended. Record decisions, content plans, and accepted changes in this file.
