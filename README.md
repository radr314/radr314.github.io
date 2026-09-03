# Randheer Vennapureddy

Source for [radr314.github.io](https://radr314.github.io), a personal engineering notebook for projects, technical writing, and experiments.

## Site structure

- `/` contains the introduction.
- `/projects/` lists active and completed projects.
- `/writing/` lists published articles.
- `/about/` contains a short biography and contact links.
- `_posts/` contains writing published from the main branch.
- `_drafts/` can be created locally for unpublished work.
- `assets/writing/<article-slug>/` holds article-specific JavaScript, CSS, data, images, or WebGL shaders.

## Run locally

Install Ruby, Jekyll, and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve --livereload --drafts
```

Open <http://127.0.0.1:4000>.

Available pages:

- <http://127.0.0.1:4000/>
- <http://127.0.0.1:4000/projects/>
- <http://127.0.0.1:4000/writing/>
- <http://127.0.0.1:4000/about/>

## Start a draft

Create `_drafts/article-title.md` locally:

```markdown
---
layout: article
title: "Article title"
description: "A one-sentence description."
topics:
  - Systems
project: http-engine
---

Article content begins here.
```

Drafts appear locally because the preview command includes `--drafts`. Do not push `_drafts` to this public repository if the content should remain private.

To publish, move the file to `_posts/YYYY-MM-DD-article-title.md`, commit it, and merge it into `main`.

## Add an interactive page

A standalone HTML/CSS/JavaScript or WebGL experiment can live at:

```text
demos/attention-explorer/
├── index.html
├── styles.css
└── main.js
```

It will be served at `/demos/attention-explorer/`. To place an interactive visualization inside an article, add its stylesheet and module to the article front matter:

```yaml
styles:
  - /assets/writing/attention-explorer/styles.css
scripts:
  - /assets/writing/attention-explorer/main.js
```


