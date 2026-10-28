# Look et al.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23718470.svg)](https://doi.org/10.5281/zenodo.23718470)

Design research for academic pages. A reference library of paper project pages, researcher homepages and code READMEs, each with an AI-readable DESIGN.md (palette, typography, spacing, components, page modules). Site: https://looketal.com/ (English, 日本語, 简体中文).

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
| `tools/readme_pool.py` | Finds the code repository linked from each project page and keeps READMEs of at least 2.5 KB |
| `tools/readme_render.py` | Renders a README with GitHub's own HTML for screenshots and writers |
| `tools/build_site.py` | Builds the static site into `docs/` (English at the root, Japanese in `ja/`, Chinese in `zh/`) |
| `tools/i18n.py`, `tools/i18n_about.py` | Site text in English, Japanese and Simplified Chinese |
| `data/i18n/` | Japanese and Chinese mood lines and selection reasons per entry |
| `tools/assets/` | Site CSS and JS |
| `docs/` | Generated site (GitHub Pages ready) |

## Build and preview

```bash
python -I -B tools/build_site.py
python -I -B -m http.server 8765 --directory docs
```

## Site structure

- **Home**: search plus browse by venue, year, template, page module and field.
- **Browse**: filterable grid; filters live in the URL (`browse.html?conf=CVPR&module=BibTeX`).
- **Style page** (`s/<slug>.html`): specimen, palette, type samples, spacing, page modules, guidelines, similar pages; side panel with DESIGN.md (compact / extended), Tailwind v4, CSS variables and design tokens.
- **Collections**: rule-based groups with a short "look closer" note.
- **Design prompts**: prompt templates for building a page from a DESIGN.md.
- **About**: inclusion rules, method, removal policy.
- **Languages**: every page exists in English, Japanese and Simplified Chinese. DESIGN.md files stay in English so that people and coding agents read one text.

## Inclusion rules

- Project pages: pool of 907 (NeurIPS, ICML, ICLR, CVPR, ACL 2025 and 2026; ICCV 2025, ECCV 2026, SIGGRAPH 2025 and 2026, CoRL 2025, CHI 2026, EMNLP 2025; TMLR, TPAMI, JMLR and Nature-family journals 2025–2026; arXiv comments that state acceptance and link a project page; workshops excluded). 10 per venue-year, plus 10 journal papers.
- Researcher homepages: pool of 236 by three fixed rules (ACM Turing laureates 2018–2025 and first or last authors of Best, Outstanding and Test of Time papers at NeurIPS, ICML, ICLR, CVPR and ACL 2023–2025; first and last authors of ACL Outstanding Papers 2023–2025; Rumelhart Prize 2010–2025, Glushko Prize 2018–2025, CogSci Computational Modeling Prize 2020–2025 and CCN keynote speakers 2023–2025). 30 + 10 + 10 selected.
- Code READMEs: the official repositories linked from the project-page pool (647 with a README of at least 2.5 KB), in four groups (vision, learning, language, graphics/robotics/HCI); 10 per group.
- Selection: by visual design only, from screenshots, in two rounds. The reason for each pick is in `data/catalog.json` and on the style page.
- DESIGN.md files are written from the rendered page (`content/METHOD.md`) or, for READMEs, from the Markdown and GitHub's rendering (`content/METHOD_README.md`); tests in `content/TESTS.md`.

## Screenshots and removal

Each entry shows a reduced above-the-fold screenshot credited to its authors and linked to the live page. Authors can ask for removal or correction through [this form](https://github.com/dengzhe-hou/looketal/issues/new?template=removal.yml).

## License and citation

Code (`tools/`, `.github/`) is MIT (`LICENSE`). DESIGN.md files, the selection, `data/` and site text are CC BY-NC 4.0 (`LICENSE-CONTENT.md`). Screenshots belong to the pages' authors and are covered by neither. Cite as: Hou, D. (2026). Look et al.: A Design Library of Academic Web Pages for Humans and AI Agents. Zenodo. https://doi.org/10.5281/zenodo.23718470 (this DOI always points to the latest version; metadata in `CITATION.cff`).
