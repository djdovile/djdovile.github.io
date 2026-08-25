---
title: ""
summary: ""
date: "2026-06-07"
type: "landing"

sections:

  - block: "resume-biography-3"
    content:
      username: "me.en"
      text: "...en"
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
        size: "small"
        shape: "circle"
    ce: "section-9a744d1c"
    As: "section-0b57de8f"

  - block: "markdown"
    content:
      title: "About this page"
      subtitle: ""
      text: |-
        Use this area to speak to your mission.
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
      show_read_time: false
      columns: 2
    ce: "section-papers"
    id: "papers"
    As: "section-513d1eef"

  - block: "collection"
    content:
      title: "Recent Publications"
      text: ""
      filters:
        folders:
          - "publications"
        exclude_featured: false
    design:
      view: "citation"
      show_read_time: false
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
      show_read_time: false
    ce: "section-talks"
    id: "talks"
    As: "section-e67064d6"
    
  - block: "collection"
    content:
      title: "Posts"
      subtitle: ""
      text: ""
      page_type: "blog"
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
