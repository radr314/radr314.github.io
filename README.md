# Randheer Vennapureddy

Source for [radr314.github.io](https://radr314.github.io), a personal
engineering notebook for projects, technical writing, and experiments.

The site uses only HTML, CSS, and a few lines of vanilla JavaScript. It has no
framework, package manager, dependency installation, or build step.

## Site structure

```text
.
├── index.html
├── projects/
│   └── index.html
├── writing/
│   └── index.html
├── about/
│   └── index.html
├── templates/
│   └── article.html.example
├── assets/
│   ├── css/main.css
│   ├── images/
│   └── js/site.js
├── 404.html
└── .nojekyll
```

## Run locally

From the repository directory, start Python's built-in static web server.

On WSL, Linux, or macOS:

```bash
python3 -m http.server 8000
```

On Windows:

```powershell
python -m http.server 8000
```

Open <http://127.0.0.1:8000>.

Available pages:

- <http://127.0.0.1:8000/>
- <http://127.0.0.1:8000/projects/>
- <http://127.0.0.1:8000/writing/>
- <http://127.0.0.1:8000/about/>

Stop the server with `Ctrl+C`.

## Write an article locally

The `drafts/` directory is ignored by Git, so articles kept there will not be
committed accidentally. Create a draft from the supplied template:

```bash
mkdir -p drafts/http-request-lifecycle
cp templates/article.html.example drafts/http-request-lifecycle/index.html
```

Edit the placeholders in the copied file, then open:

<http://127.0.0.1:8000/drafts/http-request-lifecycle/>

An article can contain ordinary HTML, code blocks, SVG, Canvas, JavaScript, or
WebGL. Put article-specific files beside its `index.html`:

```text
drafts/http-request-lifecycle/
├── index.html
├── styles.css
└── main.js
```

Uncomment the optional stylesheet or script lines in the article template only
when the article needs them.

## Publish an article

Move the finished article into `writing/`:

```bash
mv drafts/http-request-lifecycle writing/http-request-lifecycle
```

Then add its title, date, description, and link manually to
`writing/index.html`. Commit the article only when it is ready to be public.

## Add a standalone interactive page

A standalone HTML/CSS/JavaScript or WebGL experiment can use the same simple
structure:

```text
demos/attention-explorer/
├── index.html
├── styles.css
└── main.js
```

It will be available locally and on GitHub Pages at
`/demos/attention-explorer/`.
