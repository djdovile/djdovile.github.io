---
title: ""
summary: ""
date: ""
type: "landing"
sections:
  - block: "resume-biography-3"
    content:
      username: "me"
      text: "///"
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
      title: "Kas čia?"
      subtitle: ""
      text: |-
        Puslapio aprašymas

    design:
      columns: "1"
    ce: "section-06ab342f"
    As: "section-de4f07f9"
  - block: "collection"
    content:
      title: "Knygos"
      filters:
        folders:
          - "publikacijos"
        featured_only: false
        type: book
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
          - "publikacijos"
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
      title: "Tekstai"
      subtitle: ""
      text: ""
      page_type: "blogas"
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
      view: "article-grid"
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
