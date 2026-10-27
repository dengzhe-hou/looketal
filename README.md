# Look et al.

Design research for academic pages. A reference library of paper project pages and researcher homepages, each with an AI-readable DESIGN.md (palette, typography, spacing, components, page modules), structured after [Refero Styles](https://styles.refero.design/).

## Layout

| Path | What it is |
|---|---|
| `content/designs/*.md` | One DESIGN.md per page (source of truth) |
| `data/raw/workflow_*.json` | Collection and extraction records: queries, selection notes, per-page metadata |
| `data/entries.json` | Normalized entry list, written by the build |
| `tools/extract_style.py` | Measures colors, fonts, sizes, radii and widths from a page's static HTML and linked CSS |
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

## Inclusion rules (v0)

- Project pages: NeurIPS, ICML, ICLR, CVPR, ACL 2025 and 2026, 10 per venue-year, taken in arXiv relevance order from comments that state acceptance and link a project page; page must load; workshops excluded.
- Researcher homepages: ACM Turing laureates 2018–2025 (computing/AI) with a personal page, then first and last authors of Best/Outstanding Paper awards at the same venues in 2024–2025 with a personal page.

No screenshots are stored. Cards show a synthetic specimen built from measured tokens and link back to the original page.
