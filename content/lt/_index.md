---
title: ""
summary: ""
date: ""
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "me"
      text: |-
        Esu VU Tarptautinių santykių ir politikos mokslų instituto profesorė ir šio instituto Tarptautinių santykių katedros vedėja.

        Mano tyrimų temos apima sienas ir teritoriją, Rusijos politiką, Lietuvos užsienio ir saugumo politiką, de facto valstybes, pripažinimo ir simbolinės galios klausimus.

        Dėstau apie tarptautinių santykių teorijas, užsienio politikos analizę, simbolinės galios formas ir socialinių mokslų tyrimo mąstyseną.
      button:
        text: "Oficialus VU TSPMI puslapis"
        url: "https://www.tspmi.vu.lt/zmogus/dovile-jakniunaite/"
      headings:
        about: "Trumpai"
        education: ""
        interests: "Apie ką rašau ir kalbu"
    design:
      background:
        gradient_mesh:
          enable: false
      name:
        size: "sm"
      avatar:
        size: "small"
        shape: "circle"
    ce: "section-9a744d1c"
    As: "section-0b57de8f"

  - block: "markdown"
    content:
      title: "Kur toliau?"
      subtitle: ""
      text: |-
        Šis puslapis veikia kaip mano akademinių darbų ir viešų tekstų archyvas. Jei ieškote konkrečios informacijos, pradėkite nuo vienos iš šių krypčių:

        - [Publikacijos](/lt/publikacijos/) - straipsniai, knygos, knygų skyriai ir bibliografiniai įrašai.
        - [Projektai](/lt/projektai/) - tyrimų projektai ir temos, prie kurių dirbu ar dirbau.
        - [Dėstymas](/lt/destymas/) - kursai, dėstymo temos ir būsimi mokymų keliai.
        - [Tekstai](/lt/blogas/) - komentarai, interviu, tinklaraščio įrašai ir vieši pasisakymai.
    design:
      columns: "1"
    ce: "section-archive-gateway"
    As: "section-archive-gateway"

  - block: "collection"
    content:
      title: "Knygos"
      filters:
        folders:
          - "publikacijos"
        featured_only: false
        publication_type: book
    design:
      view: "citation"
      show_read_time: false
    ce: "section-papers"
    id: "papers"
    As: "section-513d1eef"
  - block: "collection"
    content:
      title: "Naujausios publikacijos"
      text: "Naujausios publikacijos"
      filters:
        folders:
          - "publikacijos"
        exclude_featured: false
    design:
      view: "citation"
      show_read_time: false
    ce: "section-d82bf061"
    As: "section-ee8c5be4"
  - block: "collection"
    content:
      title: "Tekstai"
      subtitle: ""
      text: "Komentarai, interviu ir kiti vieši tekstai apie tarptautinę politiką, saugumą ir viešąjį gyvenimą."
      page_type: "blogas"
      count: 10
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: "desc"
      sort_by: "Date"
      sort_ascending: false
    design:
      view: "title-date"
      show_date: true
      show_read_time: false
      spacing:
        padding:
          - 0
          - 0
          - 0
          - 0
    ce: "section-news"
    id: "news"
    As: "section-ef6c376a"
---
