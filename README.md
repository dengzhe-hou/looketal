# Look et al.

Design research for academic pages. A reference library of paper project pages and researcher homepages, each with an AI-readable DESIGN.md (palette, typography, spacing, components, page modules), structured after [Refero Styles](https://styles.refero.design/).

## Layout

| Path | What it is |
|---|---|
| `content/designs/*.md` | One DESIGN.md per page (source of truth) |
| `data/catalog.json` | One record per included page (build input) |
| `data/raw/` | Candidate pool and collection records |
| `content/shots/` | Screenshots (1200×750 and 640×400 webp) |
| `content/archive/v1/` | First-version DESIGN.md files, kept for comparison |
| `data/entries.json` | Normalized entry list, written by the build |
| `tools/computed_style.py` | Reads computed styles, loaded fonts and first-viewport anatomy from the rendered page (headless Chrome) |
| `tools/snap.py` | Screenshots |
| `tools/lint_design.py` | Structure and color-consistency check for DESIGN.md files |
| `tools/check_links.py` | Link check (run weekly by a GitHub Action) |
| `tools/extract_style.py` | Declaration counts from a page's static HTML and linked CSS |
| `tools/build_site.py` | Builds the static site into `docs/` |
| `tools/assets/` | Site CSS and JS |
| `docs/` | Generated site (GitHub Pages ready) |

## Build and preview

```bash
python -I -B tools/build_site.py
python -I -B -m http.server 8765 --directory docs
```

## Site structure (after Refero)

- **Home**: search plus browse by venue, year, template, page module and field.
- **Browse**: filterable grid; filters live in the URL (`browse.html?conf=CVPR&module=BibTeX`).
- **Style page** (`s/<slug>.html`): specimen, palette, type samples, spacing, page modules, guidelines, similar pages; side panel with DESIGN.md (compact / extended), Tailwind v4, CSS variables and design tokens.
- **Collections**: rule-based groups with a short "look closer" note.
- **Design prompts**: prompt templates for building a page from a DESIGN.md.
- **About**: inclusion rules, method, removal policy.

## Inclusion rules

- Pool: 505 paper project pages (NeurIPS, ICML, ICLR, CVPR, ACL 2025 and 2026; arXiv comments that state acceptance and link a project page; workshops excluded) and 138 researcher homepages (ACM Turing laureates 2018–2025 and first or last authors of Best, Outstanding and Test of Time papers at the same venues, 2023–2025).
- Selection: by visual design only, from screenshots, in two rounds; 10 per venue-year and 30 researchers. The reason for each pick is in `data/catalog.json` and on the style page.
- DESIGN.md files are written from the rendered page; see `content/METHOD.md` and the tests in `content/TESTS.md`.

## Screenshots and removal

Each entry shows a reduced above-the-fold screenshot credited to its authors and linked to the live page. Authors can ask for removal or correction through [this form](https://github.com/dengzhe-hou/looketal/issues/new?template=removal.yml).
