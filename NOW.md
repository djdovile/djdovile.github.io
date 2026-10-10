# NOW.md

Last updated: 2026-09-16 (late night)

## Current Focus
Lietuviškos svetainės versijos (`/lt/`) paleidimo paruošimas ir publikacijų/projektų/dėstymo struktūros užbaigimas.

---

## What Was Just Done (2026-09-17)
1. **Publikacijų atskiro puslapio patobulinimai (`single.html`):**
   - Grąžintas `featured` viršelio / iliustracijos atvaizdavimas puslapio viršuje.
   - Pakeistas eiliškumas: Pavadinimas -> Veiksmo mygtukai (`[PDF]`, `[DOI]`, `[Projektas]` ir kt.) -> Pilna straipsnio bibliografinė informacija (sąrašo formatu) -> Susijusio projekto blokas -> Santrauka -> Tekstas -> Žymės (temos) -> Atnaujinimo data apačioje dešinėje.
   - Pakeistas sekcijos pavadinimas iš „Anotacija“ į **„Santrauka“** (angl. *Abstract*).
   - Sugrąžintos žymės (`#tag`) su ramia neutralia estetika (pašalintas rausvumas).
2. **Projektų puslapių žymės (`tags`):**
   - Projektų puslapiuose (`layouts/projektai/single.html` ir `layouts/projects/single.html`) integruotas teminių žymių (`#Temos`) blokas, susietas su bendra taksonomijų sistema (visi 7 projektai papildyti teminėmis žymėmis).
3. **Vienodas teksto plotis, antraščių ir turinio tipografija:**
   - Panaikinti dirbtiniai siauri `max-width: 16ch` apribojimai antraštėms CSS faile (`assets/css/custom.css`).
   - Visi 4 pagrindiniai sąrašai (Publikacijos, Projektai, Dėstymas, Tekstai) ir atskiri puslapiai suvienodinti į patogų `max-w-4xl` plotį su bendra `.page-title` antraštės klase (`text-3xl lg:text-4xl font-semibold`).
   - Suvienodintas įvadinių tekstų dydis (`text-base leading-relaxed`), įrašų pavadinimai (`text-lg font-semibold`), aprašymai/metaduomenys (`text-sm`) bei skiriamosios linijos ir tarpai.
4. **Tekstų (`/lt/blogas/`) ir Projektų (`/lt/projektai/`) išdėstymas:**
   - `/lt/blogas/` pervestas į `title-date` formatą (kaip tituliniame puslapyje: pavadinimas + data skliausteliuose).
   - `/lt/projektai/` atnaujintas į švarų sąrašą su filtrų mygtukais („Visi“, „Vykdomi“, „Įgyvendinti“).

---

## Active State & Context
- **Repozitorija:** `MyProjects/dj_hugo`
- **Pagrindinė kalba:** Lietuvių (`/lt/`), antroji: Anglų (`/en/`)
- **Stiliai:** `assets/css/custom.css` („The Public Seminar Room“ dizaino sistema)
- **Kompiliavimas:** `hugo --minify` veikia be klaidų (218 LT psl., 119 EN psl.)

---

## Immediate Next Steps (Prioritetai)
1. **Peržiūrėti bendrą svetainės vaizdą naršyklėje (`pnpm run dev`):**
   - Įvertinti pradinį puslapį (`/lt/`), dėstymo puslapį (`/lt/destymas/`), projektų sąrašą (`/lt/projektai/`) ir publikacijas (`/lt/publikacijos/`).
2. **Paveikslėlių/iliustracijų parinkimas:**
   - Parinkti ir pritaikyti iliustracijas dėstymo ir projektų puslapiams pagal seminaro/akademinę estetiką.
3. **Domeno pajungimas:**
   - Patvirtinus galutinį lietuviškos versijos vaizdą, nukreipti `www.jakniunaite.lt` į GitHub Pages / Netlify ir atnaujinti `baseURL` faile `config/_default/hugo.yaml`.

---

## Brand alignment: done so far (2026-10-10, later session)

Applied option B: accent red `#B72818` -> ochre `#d43d1a` (`params.yaml`, `--dj-ochre` in `custom.css`, one ochre for fills and text); nav/interface font -> Inclusive Sans (`data/fonts/seminar.yaml`, with sans fallback via `:root:root` in `custom.css`). `hugo --minify` builds clean; not yet checked in the browser. Next: review the green `#506A52` (`--dj-wayfinding*`), then check contrast of the new ochre on every page type.

## Handoff from another session (2026-10-10): brand alignment

DJ is aligning colours and fonts across the site, slides and social cards. Start from `LIFEOS/USER/PRINCIPAL/BRAND_NOTE.md` (palette, card options, what the site already uses). Facts: the site uses Source Serif 4 and a quiet green `#506A52`, with red as a scarce marker and Hugo Blox primary `#B72818`; slides (`base-dj`, `base-dj-bold`) use peach `#fef2e8`, teal `#14444b`, ochre `#d43d1a`, harvest orange `#f9cd9e`, indigo `#261763`; DJ chose Source Serif 4 and Inclusive Sans as fonts. Open: whether the site red becomes the ochre. Also pending review here: new publication `content/lt/publikacijos/giedraitytejakniunaite2026NarratingUnity/` and draft blog `content/lt/blogas/vienybes-pasakojimai-ir-tvarkos-gynyba/` (`draft: true`); both uncommitted. When the decision is made, update `BRAND_NOTE.md` and the card templates in `PRINCIPAL/BRAND/social-card-templates/`.
