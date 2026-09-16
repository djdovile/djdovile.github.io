# NOW.md

Last updated: 2026-09-16 (late night)

## Current Focus
Lietuviškos svetainės versijos (`/lt/`) paleidimo paruošimas ir publikacijų/projektų/dėstymo struktūros užbaigimas.

---

## What Was Just Done (2026-09-16)
1. **Publikacijų veiksmo mygtukai (Action Buttons):**
   - Įjungti `[PDF]`, `[Cituoti]`, `[DOI]`, `[Preprint]` ir `[Projektas]` mygtukai atskiruose publikacijų puslapiuose (`layouts/publikacijos/single.html` ir `layouts/publications/single.html`).
   - Sukurtas `layouts/_partials/functions/build_links.html` perrašas, kad `[Projektas]` / `[Project]` mygtukas automatiškai atpažintų lietuviškus `/projektai/` kelius.
2. **Publikacijų šriftų pataisymas:**
   - Sutvarkyti visi 56 publikacijų YAML failai – pašalintos markdown žvaigždutės (`*`), kurios vertė leidinių pavadinimus paryškintais (**bold**). Dabar visi leidiniai atvaizduojami tvarkingu kursyvu (*italics*).
3. **Recenzijų taksonomija (`review`):**
   - Sukurtas `Recenzijos` / `Reviews` filtras publikacijų sąrašuose ir priskirtas atitinkamoms publikacijoms.
4. **Kompaktiškas dėstymo sąrašas:**
   - Sukurtas kompaktiškas kursų sąrašo šablonas (`layouts/destymas/list.html` ir `layouts/teaching/list.html`).

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
