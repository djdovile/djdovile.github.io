---
title: Teaching
summary: 
type: landing

#  cascade:
#  - target:
#      path: '{/teachings/*/**}'
#    type: docs
#    params:
#      show_breadcrumb: true

sections:
  - block: collection
    content:
      title: my teaching
      text: I enjoy teaching
      filters:
        folders: teaching
    design:
      view: article-grid
      fill_image: false
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: false
---


```
sections:
  - block: collection
    id: courses
    content:
      title: Courses
      filters:
        tag: Course
        kinds:
          - section
    design:
      view: article-grid
      show_read_time: false
      show_date: false
      show_read_more: false
      columns: 1
      ```