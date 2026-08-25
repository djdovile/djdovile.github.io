# dj_hugo

Last updated: 2026-08-25

Purpose, commands, and architecture (tech stack, content/layout structure, build gotchas) live in `CLAUDE.md`. This file tracks project status, decisions, and next actions only — the continuity layer.

## Current State

`MyProjects/dj_hugo` is the canonical workspace for DJ's Hugo personal webpage. The older `MyHugoPage` folder should not be treated as the active source.

The site is bilingual, with Lithuanian as the default language and English as the second language. Lithuanian-first content is the current priority; English parity can follow later.

As of 2026-07-02, the worktree contains an uncommitted implementation batch: LT project/course bundles, LT homepage text, publication type filter templates, reading-time/author-card suppression, remaining Hugo Blox demo-blog deletions, and `BLOG-LINK-REVIEW-2026-07-02.md`.

Verification state: clean Hugo build into a temporary folder passed; broken demo cite warnings are gone; `/lt/destymas/`, `/lt/projektai/`, `/lt/publikacijos/`, and publication-type pages rendered expected content; no rendered reading-time labels were found.

As of 2026-07-03, the homepage color pass moved the secondary wayfinding accent away from bright blue to a quiet green (`#506A52`), kept seminar red as a scarce action/active-state marker, added `assets/css/custom.css` for restrained link, archive-row, header, focus, and profile-button styling, and updated the local design register. Verification passed with a clean Hugo build, clean Impeccable detector output, and contrast checks above WCAG AA for body, muted, link, red, and white-on-red text pairs.

As of 2026-07-03, the homepage typeset pass replaced the generic `modern` Inter pack with a local `seminar` font pack (`Source Serif 4` for prose/headings, system sans for navigation and controls). The pass also tightened homepage reading measure, heading scale, publication citation title rhythm, metadata sizing, and archive-gateway prose spacing in `assets/css/custom.css`. The design register now treats typography as a public-seminar handout system rather than a generic Hugo Blox interface.

## Theme Decision: Hugo Blox

As of 2026-08-25: evaluated whether Hugo Blox is the right theme choice, prompted by concerns about its complexity and the maintainers' history of renaming/restructuring the project (Academic 2017 → Wowchemy ~2020 → Hugo Blox 2024, each with breaking changes). Decision: **stay on Hugo Blox to finish the current Lithuanian launch** — bilingual routing, the publications pipeline, and both deploy targets already work, and rebuilding mid-launch would mean redoing that work. The complexity/churn concern is real, not overcautious.

**Revisit post-launch**: compare effort-to-rebuild against `pmichaillat/hugo-website` (github.com/pmichaillat/hugo-website) — a minimalist Hugo template built for academic personal sites, closest philosophical match to this site's own `DESIGN.md` — if Hugo Blox's weekly upgrade PRs or complexity keep costing time. Also worth a look: `minimal-academic` (github.com/jhu247/minimal-academic), `Blowfish`.

## Current Delivery Goal

Prepare and publish a complete Lithuanian version of the personal website with minimal but sufficient information.

Delivery sequence:

1. Complete and review the Lithuanian site content and current implementation batch.
2. Verify the production result through GitHub and publish it there.
3. Connect the existing `www.jakniunaite.lt` domain after the GitHub version is confirmed.

Later phase: begin a blog, add more personal/professional information, then prepare the English version.

## Minimum Lithuanian Launch Scope

The first public Lithuanian version needs:

1. A short multi-paragraph personal introduction.
2. A curated publications list: selected publications need links to files where available, short descriptions, and links to the related projects; the first launch does not require every publication.
3. Clear descriptions of the courses currently taught.
4. All existing older blog posts.
5. Descriptions of all current active projects and several most recently completed projects.

Current-course list for the first release:

- Tarptautinių santykių teorijos
- Simbolinės galios formos
- Užsienio politikos analizė
- How to Think Like a Social Scientist
- Mokslinio darbo pagrindai (Socialinių mokslų filosofijos modulis)

Profile emphasis for the first release: researcher and lecturer; an expert in international relations and security.

Research themes to foreground in the first-release introduction:

- Užsienio politikos analizė: Lietuvos ir Rusijos užsienio politika
- Vidurio ir Rytų Europos regiono saugumas
- Sienų ir mobilumo studijos
- Diskusijos apie tarptautinės tvarkos transformaciją

## Known Follow-Ups

- Confirm the GitHub publication result before connecting `www.jakniunaite.lt`. `config/_default/hugo.yaml` currently uses `https://djdovile.github.io/`, matching the GitHub Pages workflow.
- Review visible mojibake/encoding issues in config and author files before publication.
- Test `pnpm run build` before deployment.
- Post-launch: revisit the Hugo Blox theme decision (see "Theme Decision: Hugo Blox" above).

## Remaining Tasks To Review

- Complete and review the Lithuanian site as a minimally sufficient public version before publication.
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
