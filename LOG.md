# LOG.md — Darbų ir sesijų žurnalas

Chronologinis atliktų darbų, sprendimų ir pakeitimų žurnalas.

---

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
