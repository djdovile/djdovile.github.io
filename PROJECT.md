# dj_hugo

Last updated: 2026-10-11

Purpose, commands, and architecture (tech stack, content/layout structure, build gotchas) live in `CLAUDE.md`. This file tracks project status, decisions, and next actions only — the continuity layer.

## Current State

This repo (`1_Projektai (personal)/DJwebsite/dj_hugo`) is the canonical workspace for DJ's Hugo personal webpage. The older `MyHugoPage` folder is not the active source.

**Status 2026-10-11:** the first Lithuanian version is built and pushed to `main` (GitHub Pages at `djdovile.github.io`). DJ is reviewing content and tags by hand before deploying for real; further changes only for bugs. The English site and language switch are hidden for now. Open: connect `www.jakniunaite.lt` and change `baseURL`; review the draft post `vienybes-pasakojimai-ir-tvarkos-gynyba`; contrast check of ochre/teal and dark mode. Current short status is in `NOW.md`. A pre-push consistency check exists (`pnpm run check`, see `CLAUDE.md`); first version pushed 2026-10-11.

The site is bilingual, with Lithuanian as the default language and English as the second language. Lithuanian-first content is the current priority; English parity can follow later.

As of 2026-07-02, the worktree contains an uncommitted implementation batch: LT project/course bundles, LT homepage text, publication type filter templates, reading-time/author-card suppression, remaining Hugo Blox demo-blog deletions, and `BLOG-LINK-REVIEW-2026-07-02.md`.

Verification state: clean Hugo build into a temporary folder passed; broken demo cite warnings are gone; `/lt/destymas/`, `/lt/projektai/`, `/lt/publikacijos/`, and publication-type pages rendered expected content; no rendered reading-time labels were found.

As of 2026-07-03, the homepage color pass moved the secondary wayfinding accent away from bright blue to a quiet green (`#506A52`), kept seminar red as a scarce action/active-state marker, added `assets/css/custom.css` for restrained link, archive-row, header, focus, and profile-button styling, and updated the local design register. Verification passed with a clean Hugo build, clean Impeccable detector output, and contrast checks above WCAG AA for body, muted, link, red, and white-on-red text pairs.

As of 2026-07-03, the homepage typeset pass replaced the generic `modern` Inter pack with a local `seminar` font pack (`Source Serif 4` for prose/headings, system sans for navigation and controls). The pass also tightened homepage reading measure, heading scale, publication citation title rhythm, metadata sizing, and archive-gateway prose spacing in `assets/css/custom.css`. The design register now treats typography as a public-seminar handout system rather than a generic Hugo Blox interface.

As of 2026-08-25: `content/lt/blogas` (Tekstai) migrated from the WordPress export at `hugo-export/posts/` — went from 18 posts to 55, covering 2012 through 2025. `EN/content/en/blog` was not touched (still only has the original posts; English isn't in scope for the LT launch). Deliberately excluded from the migration:

- **10 posts marked `draft: true` in the WP export** — never actually published on the old site. Worth a look if there's ever a reason to revisit: `pirmas` (2012, a short reflective photo post), `5 keliavimo traukiniu privalumai` (2012, travel), `Miestas, į kurį sugrįšiu` (2013, NYC), `Россия все активнее...` (2014, RU-language Delfi.ru interview), `Gražinos Miniotaitės knyga` (2014, empty stub), `Ar bus nauja Lietuvos užsienio politika?` (2014, one-line stub, no real content), `testinis` (2015, a WordPress pricing-table test post — not real content), `Apie karinę Lietuvos strategiją` (2016, RU-language interview), `po 2016 Seimo rinkimų` (2016, FB repost), `Žodžiai` (2017, year-in-words piece).
- **4 export files that duplicate a post already published under a different (shorter) slug** — verified by matching title and date, not re-added.

All of today's changes are pushed to GitHub `main` and confirmed live on `djdovile.github.io` (deploy workflow runs all green, spot-checked both a 2012 and a 2025 post return 200). `www.jakniunaite.lt` is not yet connected — still pending the domain step below.

Also today: the LT homepage "Tekstai" and EN homepage "Posts" blocks were switched from the citation/article-grid views to a new minimal `title-date` view (`layouts/_partials/views/title-date*.html`) — plain title + muted `(date)`, no author line or summary, since the citation view read as clutter for a single-author commentary list.

**Session close, 2026-09-16**:
- Cleaned and fixed bold vs. italics across all 56 publication YAML files (removed markdown asterisks causing nested strong tags; all publication venues now italicized).
- Added `review` taxonomy / filter for book reviews in Lithuanian (`Recenzijos`) and English (`Reviews`).
- Created compact teaching overview layout in `layouts/destymas/list.html` and `layouts/teaching/list.html`.
- Implemented single publication layout with project context and enabled `[Projektas]` / `[Project]` button in publication action links via overridden `layouts/_partials/functions/build_links.html`.
- Build verified with `hugo --minify` (0 errors).

**Homepage navigation decision, 2026-09-18**: the Lithuanian homepage has no hero CTA. The VU TSPMI profile is an inline institutional-verification link at the end of the biography; “Kur toliau?” immediately below remains the first explicit prompt for navigating the site archive.

As of 2026-10-10, brand alignment with the slides and social cards (`LIFEOS/USER/PRINCIPAL/BRAND_NOTE.md`): accent red `#B72818` became ochre `#d43d1a` (one ochre for fills and text, as in the slides; a darker shade was tried and dropped); links, attachment/cite buttons and all hover states are teal `#14444b` (the old green `#506A52` is gone; buttons are border-only, no fill); menu hover and current page stay ochre. Interface font is now Inclusive Sans; Source Serif 4 stays for prose. Both fonts are self-hosted (no Google requests; checked with a clean build into a temporary folder). Author names in publication lists are plain text (`layouts/_partials/page_metadata_authors.html` overrides the theme, which linked each name to a non-rendered author page and fell back to the publications list). `DESIGN.md` updated to match. Not yet checked: contrast of the new ochre/teal on every page type; `.impeccable/design.json` still holds the old palette and needs regenerating.

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
4. ~~All existing older blog posts.~~ Done 2026-08-25: 55 of the ~65 WordPress-export posts are live (2012-2025); the remainder are 10 genuine WP drafts and 4 duplicates, deliberately excluded (see Current State above).
5. Descriptions of all current active projects and several most recently completed projects.

Current-course list for the first release:

- Tarptautinių santykių teorijos (MA)
- Simbolinės galios formos (MA)
- Užsienio politikos analizė (MA)
- How to Think Like a Social Scientist (BA)
- Feminizmas: tekstai ir praktika (BA)

Profile emphasis for the first release: researcher and lecturer; an expert in international relations and security.

Research themes to foreground in the first-release introduction:

- Užsienio politikos analizė: Lietuvos ir Rusijos užsienio politika
- Vidurio ir Rytų Europos regiono saugumas
- Sienų ir mobilumo studijos
- Diskusijos apie tarptautinės tvarkos transformaciją

## Known Follow-Ups

- ~~Confirm the GitHub publication result before connecting `www.jakniunaite.lt`.~~ Confirmed 2026-08-25: GitHub Pages deploy is green and live at `djdovile.github.io`. `config/_default/hugo.yaml` still points there (`https://djdovile.github.io/`); update to the real domain when it's connected.
- Review visible mojibake/encoding issues in config and author files before publication.
- Test `pnpm run build` before deployment.
- Post-launch: revisit the Hugo Blox theme decision (see "Theme Decision: Hugo Blox" above).
- Pixel-verify the 2026-08-25 (evening) homepage hero CSS pass — see Current State session-close note above. Uncommitted until confirmed.
- C: drive is down to ~467 MB free — free up space (blocked a one-time Playwright screenshot install; will block bigger things eventually).

## Remaining Tasks To Review

- Complete and review the Lithuanian site as a minimally sufficient public version before publication.
- ~~Review `BLOG-LINK-REVIEW-2026-07-02.md`; 13 checked link rows returned errors and need manual decision or later replacement.~~ Done 2026-09-15: all 13 broken/outdated link rows across 5 blog posts fixed/archived/cleaned, with author/footnote notes added where appropriate.
- ~~Update course descriptions according to actual syllabi in `2_Destymas`.~~ Done 2026-09-15: all 5 courses updated with descriptions, objectives, and topics ("Simbolinės galios formos" and "Feminizmas: tekstai ir praktika" titles corrected).
- ~~Link publications and projects bidirectionally (Option A+C).~~ Done 2026-09-15: added `projects:` mapping across publications, created single page layouts (`layouts/publikacijos/single.html`, `layouts/projektai/single.html` and EN mirrors) rendering linked projects on publication pages and dynamically listing all associated publications on project pages.
- ~~Fix bold publication venue formatting across all publications.~~ Done 2026-09-16: removed stray markdown asterisks from `name:` and `short_name:` fields across all 56 publication files in LT and EN trees, fixing double-emphasis that caused publication titles/venues to render in bold instead of clean italics, plus fixed residual character encoding issues.
- ~~Add new LMT research project `LTgalia`.~~ Done 2026-09-15: `content/lt/projektai/ltgalia/index.md` created.
- ~~Replace or draft `content/lt/events/example/` and `content/lt/slides/example/`.~~ Done 2026-08-25: removed both (Hugo Blox demo placeholders). LT `/events/` and `/slides/` are now empty sections; add real content or unlink from nav later.
- ~~The same Hugo Blox demo placeholders exist under `content/en/`.~~ Done 2026-08-25: removed both. EN `/events/` and `/slides/` are now empty sections too.
- Add English project/course pages later if bilingual parity is desired.
- Add `translationKey` values where real Lithuanian and English page pairs exist.
- Clean English homepage placeholder text and English author metadata later, including `slug: men`, the stray `:url`, and the typo `indentity`.
- Normalize blog author metadata from `admin` or empty author lists to `me` where appropriate.
- Review legacy root files `content/_index.md` and `content/experience.md`; archive or remove them if they are no longer used.
- Align Netlify and GitHub Pages deployment notes once the preferred production route is settled.

## Working Rules

Make content and configuration changes in source files, not in `public/`. Before changing site structure, check both language folders so Lithuanian and English stay aligned where intended. Record decisions, content plans, and accepted changes in this file.
