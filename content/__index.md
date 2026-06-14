---
title: ""
summary: ""
date: "2026-06-07"
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "me"
      text: "tyrėja"
      button:
        text: "..."
        url: null
      headings:
        about: ""
        education: ""
        interests: ""
    design:
      background:
        gradient_mesh:
          enable: false
      name:
        size: "sm"
      avatar:
        size: "medium"
        shape: "circle"
    ce: "section-9a744d1c"
    As: "section-0b57de8f"
  - block: "markdown"
    content:
      title: "Mano tyrimai"
      subtitle: ""
      text: |-
        Use this area to speak to your mission. I'm a research scientist in the Moonshot team at DeepMind. I blog about machine learning, deep learning, and moonshots.

        I apply a range of qualitative and quantitative methods to comprehensively investigate the role of science and technology in the economy.

        Please reach out to collaborate 
    design:
      columns: "1"
    ce: "section-06ab342f"
    As: "section-de4f07f9"
  - block: "collection"
    content:
      title: "Featured Publications"
      filters:
        folders:
          - "publications"
        featured_only: true
    design:
      view: "article-grid"
      columns: 2
    ce: "section-papers"
    id: "papers"
    As: "section-513d1eef"
  - block: "collection"
    content:
      title: "Naujausios publikacijos"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: false
    design:
      view: "citation"
    ce: "section-d82bf061"
    As: "section-ee8c5be4"
  - block: "collection"
    content:
      title: "Pasisakymai"
      filters:
        folders:
          - "events"
    design:
      view: "card"
    ce: "section-talks"
    id: "talks"
    As: "section-e67064d6"
  - block: "collection"
    content:
      title: "Įrašai"
      subtitle: ""
      text: ""
      page_type: "lt/blog"
      count: 5
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
      sort_ascending: true
    design:
      view: "compact"
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
