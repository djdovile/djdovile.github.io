# LOG.md — Darbų ir sesijų žurnalas

Chronologinis atliktų darbų, sprendimų ir pakeitimų žurnalas.

---

## 2026-10-12 - Local work after `c634f92` (17 commits, not pushed)

- **Publication types:** `edited-book` and `report` added (LT "Sudarytas leidinys", EN "Edited volume", filter buttons, check script). "Beieškant NATO Lietuvoje" set to `edited-book` (editors Jakniūnaitė, Paulauskas).
- **cite.bib:** generator/checker `scripts/cite_bib.py` (`pnpm cite`, `cite:write`, `cite:check`); 12 new files LT+EN; damaged characters repaired, DOIs added, editors moved to `editor`.
- **Publications, projects, courses:** DJ's page edits kept; `start` on all projects, `last_taught` on past courses; lists sorted by those fields (projects by `start`, courses current A-Z then past by `last_taught`); title/label rows no longer wrap; `.filter-btn` on the filters.
- **Tags:** cleanup across posts, projects, courses, publications (status tags removed, merges, no `/` in tags). Topics pages (`layouts/tags/{taxonomy,term}.html`, frequency/A-Z toggle, type label per item, `tag_label.html`).
- **Dates:** `enableGitInfo` with front-matter `lastmod` first. "Atnaujinta" follows the last commit of the page's `index.md`; the dev server reads git once at start.
- **Book covers:** `featured.jpg` for five books (LT+EN): Georgia and NATO as supplied, Russia straightened from a photo, Ambicingas cropped from a small photo (soft), Miniotaite from a photo. Book pages show the cover beside the title (`layouts/{publikacijos,publications}/single.html`, `.book-cover` in `custom.css`). Home page: new `book-shelf` block (`layouts/_partials/hbx/blocks/book-shelf/block.html`) "Knygos" between publications and Tekstai: Georgia, Ambicingas, Russia. Typo "dešimtemtis" fixed.
- **Book page texts:** Miniotaite page carries the collection preface (from DJ's PDF; "Minionaitės" and "Lietuvių" fixed); Ambicingas page carries the contents (no page numbers, no appendices), DJ's two chapters linked with `relref`.
- **CLAUDE.md:** gotchas for sort fields, publication types, tag rules, git dates, `.filter-btn`, dev server.


---

## 2026-10-11 - Pre-push check, tags, authors, publication fixes (pushed `c634f92`)

- **Pre-push check:** `scripts/check_content.py`, run as `pnpm run check` (front matter) or `pnpm run check:build` (also builds to a temp folder: Google font links, DOI brackets, broken internal links). Reports only; exit 1 on errors. Rules: required fields and exact `status` on projects/courses/posts/publications, no `permalink`/`tech_stack`, tag hygiene, single-value DOI, `projects:` must exist, LT/EN publication twins, hidden future dates, every post has an author. `projektas`/`vykdomi`/`igyvendinti`/`kursas` tags are not required (the filter reads `status`). Documented in `CLAUDE.md`.
- **Publications:** Chain of Emergencies DOI is now a single value (was a list printing `[brackets]`); EN draft of Narrating Unity added (`draft: true`); EN Jaroszewicz "Seeing Like a Train" renamed to the LT folder name and aligned (author `me`, date, volume/issue/pages, project); EN `example-publication` deleted. Rule (in `CLAUDE.md`): a new publication in one language gets a `draft: true` twin in the other for DJ to review.
- **Tags:** missing tags added to 13 posts and the 2017 working paper per DJ's corrections; common-noun tags lowercase site-wide (names of states, regions and persons keep capitals); `Lieutos` typo, `Georgia` to `Gruzija`, `russia` to `Russia`, `Lietuvos--Rusijos` to `Lietuvos-Rusijos`.
- **Authors:** `me` on all posts (was empty or `admin`).
- **Courses:** Feminizmas date set, `dėstytas` capitalised, BA IR theory folder renamed to ASCII `tarptautiniu-santykiu-teorijos-b`; DJ's course/project list edits committed.

---

## 2026-10-11 - Session close
- Brand alignment finished and pushed (ochre `#d43d1a`, teal links, self-hosted fonts); CV-derived publications, projects and courses added; `permalink:` and `tech_stack:` removed; CLAUDE.md gotchas written.
- DJ: first version is ready; she will review content and tags herself, deploy afterwards, and change things only if bugs appear.
- Offered, not started: pre-push check script (front matter, no permalink/tech_stack, no Google fonts, internal links, DOI brackets).

---

## 2026-10-11 - Footer, links, photo, menu bar, homepage cleanup

- **Footer:** "Sukurta su Hugo ir Hugo Blox" with short links (hugo.chat promo button removed; overrides in `layouts/_partials/site_footer.html` and `components/footers/minimal.html`); row of own links (email, LinkedIn, Scholar, ORCID, ResearchGate, RSS of Tekstai `/lt/blogas/index.xml`) read from `data/authors/me.yaml`, also in the homepage column. More space between the icon row and the CC logos.
- **Language switch hidden** (header and footer) while the English site is not public; set `language_switcher: true` in `params.yaml` to bring it back.
- **Profile photo:** replaced the file with a baked-in checkerboard by the real transparent cutout, cropped square (800x800); beige backdrop behind it.
- **Menu bar:** same cream as the page (page background defined once, `#fffaf5`), hairline only, slimmer, same font sizes.
- **Homepage:** "Apie ką rašau ir kalbu" section removed (`interests: []` in the author files); the labels were not links and repeated the biography.

## 2026-10-10 (CV check) - Content added from the LT CV

Compared `Jakniunaite_CV-LT_2026.docx` with the site (not copied into the repo).
- **Publications added (3, LT + EN mirror):** 2012 "Baltic States - Three States, but No Region"; 2011 Morgenthau text; 2010 "Įvadas. Mūsų aljansas". (DJ then removed the 2012 Russian article, the 2010 "Lithuania" chapter and the 2006 review.) "Kitos" section ignored; the dataset entry (MIDAS) is linked from the Global Society page and not a separate entry.
- **Projects added (5):** INFLUENCE DN; COST CA17119; EU-PREACC; Russian identity project 2011-2012; NATO public diplomacy project 2010. (MGIMO and Baltic Sea energy security were dropped at DJ's request.) Not added: postdoc supervision and projects before 2010 (CINEFOGO, COST A24, 2005-2007 grants).
- **Courses added (6):** Socialinių mokslų tyrimų logika; Politikos mokslų teorijos; Įvadas į tarptautinę politiką; Tarptautinės bendruomenės struktūra; Lietuvos užsienio ir saugumo politika; JAV studijos. Past courses carry "Dėstytas"; level pills now include BA/PhD for all.
- **Fix:** the project filter "Vykdomi/Įgyvendinti" now reads the status field (three projects were missed because their tags did not match).
- Feminizmas now "Dėstytas"; the doctoral TST elective is deliberately not added.

## 2026-10-10 (later) - Post pages, tags, update line

- **Tekstai post pages:** new layout `layouts/blogas/single.html` (and `layouts/blog/single.html` for EN) in the Projektai/Publikacijos style: back link, optional featured image, title, muted date, content, topic tags, "Atnaujinta". Share box and reading time removed (they came from the theme's default single).
- **Tags:** no `#` prefix on any page type; post tags use the same chip style as Publikacijos.
- **"Atnaujinta":** no longer italic (all single layouts: publikacijos, projektai, destymas, teaching and their EN versions).
- Homepage introduction text considered final by DJ (2026-10-10); removed from the launch to-do list.
- **One ochre:** the darker `#a82e12` for small text was dropped (it read as a different red); `--dj-red-deep` is now an alias of `--dj-red` `#d43d1a`. If the ochre changes later, change it everywhere at once.
- **Homepage:** plain background (no gradient band), smaller name, tighter section gaps, "Daugiau" as a left-aligned teal link, Tekstai titles like publication titles. List pages (Projektai, Dėstymas, Tekstai) use the narrower publication width.
- **Status/type pills and filter chips** restyled to one quiet outline; cool grey boxes mapped to the warm shelf beige; all green removed.
- **`tech_stack` removed** (template leftover that duplicated tags); project lists and pages now show topic tags (status tags excluded).
- **CSS cleanup:** variables reduced to `--dj-paper/shelf/ink/muted/border/ochre/teal/teal-hover/measure` (merged red-deep, red-soft, shelf-strong, two measures; renamed red -> ochre, wayfinding -> teal). Keyboard focus ring is teal.
- **Publication list labels** (PDF, DOI, Projektas, Cituoti, Duomenys): muted warm grey, ochre on hover (they read as blue in teal). The Duomenys (MIDAS) icon is now `hero/circle-stack`; icon names need the `hero/` prefix.
- DJ's own edits to the Global Society entry committed.

## 2026-10-10 - Brand alignment: colours, fonts, list styling

Aligned the site with the slides and social cards (see `LIFEOS/USER/PRINCIPAL/BRAND_NOTE.md`).
- **Accent:** red `#B72818` -> ochre `#d43d1a`; deep `#a82e12` for small text. Menu hover and current page stay ochre.
- **Links, attachment/cite buttons, all other hovers:** teal `#14444b` (hover `#0f3037`); the old green `#506A52` is gone. Buttons are border-only, no fill.
- **Fonts:** Inclusive Sans for interface text, Source Serif 4 for prose. Both self-hosted (`assets/dist/font/`, italic in `static/fonts/`); no Google requests. Check builds with `hugo --minify -d <tmp>`, because the old `public/` keeps stale pages.
- **Author names** in publication lists are plain text (`layouts/_partials/page_metadata_authors.html`); the theme linked them to author pages that are not rendered.
- **List titles:** Tekstai rows now match Projektai; Publikacijos titles are ink with a quiet underline and ochre hover.
- **Global Society entry:** `doi` changed from a list to a single value, which removed the brackets from the DOI link.
- **Cleanup:** removed `permalink:` front matter from all content files (left by the retired Basic Memory experiment; not a Hugo field). `PRODUCT.md` is now untracked and gitignored (local Impeccable context only). `DESIGN.md`, `PROJECT.md`, `CLAUDE.md` updated.
- Commits: `00a8439`, `0946b00`, `7fd8469`, `ab91df5`, `0520591`. Not pushed at time of writing.

## 2026-10-10 - Global Society article added

New publication bundle `content/lt/publikacijos/giedraitytejakniunaite2026NarratingUnity/` and draft blog post `content/lt/blogas/vienybes-pasakojimai-ir-tvarkos-gynyba/` (`draft: true`). Test build passed. Committed 2026-10-10. Volume/issue/pages to fill when assigned; EN version later.

## 2026-09-17
- **Publikacijų puslapių išdėstymas (`layouts/publikacijos/single.html`, `layouts/publications/single.html`):**
  - Grąžintas `featured` iliustracijos atvaizdavimas.
  - Sudėliotas teisingas eiliškumas: Pavadinimas -> Veiksmo mygtukai (`[PDF]`, `[DOI]`, `[Projektas]`, `[Cituoti]`) -> Pilna bibliografinė informacija (autoriai, leidinys, metai) -> Projekto dėžutė -> Santrauka -> Tekstas / pastabos -> Temos / žymės -> Atnaujinimo data apačioje dešinėje.
  - „Anotacija“ pervadinta į „Santrauka“ (angl. *Abstract*).
  - Sugrąžintos žymės (`tags`), pašalinta rausva spalva ir pritaikytas neutralus, ramus akademinis stilius.
- **Projektų puslapių žymės (`tags`):**
  - Projektų puslapiuose (`layouts/projektai/single.html`, `layouts/projects/single.html`) integruotas `#Temos` žymių blokas, o projektai papildyti atitinkamomis teminėmis žymėmis (`Sienos`, `Teritorija`, `Mažosios valstybės`, `Lietuvos užsienio politika` ir kt.).
- **Teksto pločio ir antraščių suvienodinimas:**
  - CSS faile (`assets/css/custom.css`) panaikintas dirbtinis antraščių susiaurinimas (`max-width: 16ch` ir `13ch`), skaitymo plotis padidintas iki 86ch.
  - Visi sąrašai ir atskiri puslapiai (`publikacijos`, `projektai`, `destymas`, `blogas`) naudoja vienodą `max-w-4xl` konteinerio plotį ir vienodą `.page-title` antraštės stilių (šriftas, dydis, storis).
- **Tekstų (`/lt/blogas/`) sąrašo vaizdas:**
  - Sukurtas `layouts/blogas/list.html` ir `layouts/blog/list.html` šablonas su `title-date` formatu (pavadinimas + data skliausteliuose), identiškas tituliniam puslapiui.
- **Projektų (`/lt/projektai/`) sąrašo vaizdas:**
  - Sukurtas `layouts/projektai/list.html` ir `layouts/projects/list.html` su vieningu antraštės stiliumi ir greitais filtrais („Visi“, „Vykdomi“, „Įgyvendinti“).
- **Visų 4 pagrindinių kategorijų (Publikacijos, Projektai, Dėstymas, Tekstai) index puslapių tipografijos suvienodinimas:**
  - **Puslapių antraštės ir įvadai:** Visuose 4 sąrašuose antraštėms naudojama identiška `.page-title` klasė (`text-3xl lg:text-4xl font-semibold`), o paaiškinamajam tekstui / santraukai – `text-base text-neutral-600 dark:text-neutral-400 leading-relaxed`.
  - **Įrašų antraštės:** Publikacijų, projektų ir dėstymo sąrašuose įrašų pavadinimams nustatytas identiškas `text-lg font-semibold` (1.125rem) dydis ir storis.
  - **Įrašų aprašymai / metaduomenys:** Suvienodinti į `text-sm` (0.875rem), o žymės bei būsenos indikatoriai – į `text-xs`.
  - **Skiriamosios linijos ir tarpai:** Visiems sąrašams pritaikytos vienodos viršutinės ir tarpinės skiriamosios linijos (`border-stone-200` / `divide-stone-200`, naudojančios `var(--dj-border)`) bei `py-4.5` / `py-5` elementų aukščiai.
- **Verifikacija:**
  - `hugo --minify` sėkmingai sugeneravo visą svetainę (0 klaidų, 250 LT psl., 119 EN psl.).

---

## 2026-09-16 (Vakaras / Naktis)
- **Publikacijų veiksmo mygtukų įgalinimas (`page_links`):**
  - Įkeltas `{{ partial "page_links" (dict "page" . "is_list" 0) }}` į [`layouts/publikacijos/single.html`](file:///C:/Users/Vartotojas/OneDrive%20-%20Vilnius%20University/Documents/1_Projektai%20(personal)/DJwebsite/dj_hugo/layouts/publikacijos/single.html) ir [`layouts/publications/single.html`](file:///C:/Users/Vartotojas/OneDrive%20-%20Vilnius%20University/Documents/1_Projektai%20(personal)/DJwebsite/dj_hugo/layouts/publications/single.html).
  - Visi publikacijų veiksmo mygtukai (`PDF`, `Cituoti`, `DOI`, `Preprint`) dabar matomi atskirame publikacijos puslapyje.
- **`[Projektas]` / `[Project]` mygtuko integracija:**
  - Nustatyta, kad Hugo Blox numatytasis `build_links.html` projektų ieškojo tik `projects/<slug>` kelyje, todėl lietuviškame `/lt/` puslapyje `projektai/<slug>` nebuvo randamas.
  - Sukurtas perrašas [`layouts/_partials/functions/build_links.html`](file:///C:/Users/Vartotojas/OneDrive%20-%20Vilnius%20University/Documents/1_Projektai%20(personal)/DJwebsite/dj_hugo/layouts/_partials/functions/build_links.html), kuris palaiko abiejų kalbų projektų kelius.
- **Publikacijų šrifto stiliaus (bold vs. italic) sutvarkymas:**
  - Peržiūrėti visi 56 publikacijų YAML failai (`content/lt/publikacijos/` ir `content/en/publications/`).
  - Pašalintos perteklinės markdown žvaigždutės iš `name:` ir `short_name:` laukų, kurios kartu su šablono `<em>` tagu paversdavo leidinių pavadinimus paryškintais (`<strong>`). Visi leidiniai dabar atvaizduojami kursyvu (*italic*).
- **Recenzijų (`review`) taksonomija:**
  - Pridėtas `review` taksonomijos filtras į `layouts/_partials/publication_type_filters.html`, `layouts/publication_types/term.html` ir `layouts/publication_types/list.html`.
  - Priskirtas `publication_types: ["review"]` trims knygų recenzijoms (`jakniunaite2008VitkusBookReview`, `jakniunaite2005WendtoIssukis`, `jakniunaite2007KadDemokratijaVeiktu`).
- **Kompaktiškas dėstymo sąrašo šablonas:**
  - Sukurtas kompaktiškas, seminarinio stiliaus kursų sąrašas [`layouts/destymas/list.html`](file:///C:/Users/Vartotojas/OneDrive%20-%20Vilnius%20University/Documents/1_Projektai%20(personal)/DJwebsite/dj_hugo/layouts/destymas/list.html) ir [`layouts/teaching/list.html`](file:///C:/Users/Vartotojas/OneDrive%20-%20Vilnius%20University/Documents/1_Projektai%20(personal)/DJwebsite/dj_hugo/layouts/teaching/list.html).
- **Verifikacija:**
  - Paleistas `hugo --minify`, kompiliavimas praėjo sėkmingai (0 klaidų, 218 LT psl., 119 EN psl.).

---

## 2026-09-15
- **Dvipusis ryšys tarp publikacijų ir projektų:**
  - Susietos publikacijos su atitinkamais tyrimų projektais per `projects:` lauką YAML metaduomenyse.
  - Sukurtas dinaminis susijusių publikacijų sąrašo atvaizdavimas projekto puslapyje (`layouts/projektai/single.html`).
- **Naujas LMT projektas:**
  - Sukurtas naujo tyrimų projekto puslapis `content/lt/projektai/ltgalia/index.md`.
- **Dėstymo kursų atnaujinimas:**
  - Pagal `2_Destymas` programas atnaujinti visi 5 dėstomi kursai (aprašymai, tikslai, temos).
- **Blog'o nuorodų sutvarkymas:**
  - Išspręstos visos 13 neveikiančių nuorodų problemų iš `BLOG-LINK-REVIEW-2026-07-02.md`.

---

## 2026-08-25
- **Blog'o (Tekstai) migracija iš WordPress:**
  - Perkelti 55 tekstai (2012–2025 m.) iš WordPress eksporto (`hugo-export/posts/`) į `content/lt/blogas/`.
  - Atsijoti 10 juodraščių ir 4 dublikatai.
- **Pradinio puslapio tekstų vaizdas:**
  - Sukurtas `title-date` peržiūros šablonas (`layouts/_partials/views/title-date*.html`) pradžios puslapiui, pakeičiantis perteklinį straipsnių tinklelio vaizdą minimaliu sąrašu.
- **Dizaino korekcijos:**
  - Pakoreguotas pradžios puslapio Hero blokas faile `assets/css/custom.css` (paslėpti nereikalingi marketinginiai elementai, sutvarkytos etikečių ir mygtukų spalvos pagal „The Public Seminar Room“ sistemą).

---

## 2026-07-03
- **Spalvų ir tipografijos sistema:**
  - Įdiegta „The Public Seminar Room“ dizaino sistema.
  - Antrinė akcentinė spalva pakeista į ramią žalią (`#506A52` / `--dj-wayfinding`), raudona (`#B72818`) rezervuota tik aktyviems veiksmams.
  - Įdiegtas šriftų paketas `seminar` (`Source Serif 4` tekstui ir antraštėms).

---

## 2026-07-02
- **Lietuviško turinio struktūrizavimas:**
  - Sukurti lietuviški projektų, kursų ir publikacijų aplankai.
  - Išvalyti Hugo Blox demonstraciniai įrašai.
