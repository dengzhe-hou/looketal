# V2W Nerfies Classic — Style Reference

> A clean lab handout pinned under a dark-red conference stamp.

**Theme:** light

Measurements below come from the page's static HTML and linked CSS (declaration frequency counts), then filtered by reading the markup to keep only values the page actually uses. Bulma's unused palette (turquoise `#00d1b2`, green `#48c774`, info `#3298dc`) is excluded. Roles are interpreted, not declared by the authors.

## Overview

The V2W page is a near-stock instance of the Nerfies template on Bulma 0.9. Everything is centered in a `is-max-desktop` container (Bulma caps it at 960px on desktop), the title is set in Google Sans at Bulma's `is-1` size (3rem), and a single dark-red `NeurIPS 2026` line sits under it in bold. There is one rounded dark pill button (arXiv), a full-width static teaser PNG, a justified abstract in a four-fifths column, a method figure, two qualitative case figures and a BibTeX block. No video, no carousel, no tables. The only additions to the template are a shared `<project-navbar>` web component (dropdown linking the author's other project pages) and the dark-red venue color.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page and navbar background |
| Bulma Ink | `#363636` | `--text-strong` | Titles (`.title`) |
| Body Graphite | `#4a4a4a` | `--text` | Body copy, navbar items |
| Oxblood Stamp | `#8b0000` | `--venue` | `.publication-conference` "NeurIPS 2026" line |
| Author Sky | `hsl(204, 86%, 53%)` | `--author-link` | Author name links (forced `!important`) |
| Bulma Link Blue | `#3273dc` | `--link` | Default links, navbar chevron, focus outline |
| Button Night | `#363636` | `--btn-dark` | `is-dark` rounded link buttons (Bulma dark) |
| Code Mist | `#f5f5f5` | `--surface` | `pre` BibTeX background, current-nav pill |
| Hairline | `#dbdbdb` | `--line` | Navbar dropdown top border |
| Footer Fog | `#fafafa` | `--footer` | Bulma `.footer` background, nav hover |
| Muted Label | `#777777` | `--muted` | Navbar "current" tag text |

## Tokens — Typography

- **Display:** `Google Sans`, sans-serif (title, authors, teaser). Substitute: Product Sans, or `Inter` if unavailable (Google Sans is not openly served; the Google Fonts request often falls back).
- **Body:** `Noto Sans`, sans-serif. Substitute: Open Sans.
- **Mono:** Bulma default `monospace` for BibTeX.
- **Weights:** 400 body, 600 Bulma titles, 700 venue line (`has-text-weight-bold`).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem (2rem under 768px) | 600 | 1.125 |
| Venue line (`is-size-4`) | 1.5rem | 700 | 1.5 |
| Authors / affiliations (`is-size-5`) | 1.25rem | 400 | 1.5 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Sub-heading (`title is-4`) | 1.5rem | 600 | 1.125 |
| Body | 1rem | 400 | 1.5 |
| Navbar item | .875rem | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px (full pill) |
| `pre` code block | 4px (Bulma) |
| Navbar dropdown | 0 0 6px 6px |
| Navbar current tag | 4px |

- **Shadows:** only the navbar dropdown (`0 8px 8px rgba(10,10,10,.1)`); content is flat.
- **Layout max-width:** `container is-max-desktop` (960px at desktop breakpoint, inferred from Bulma 0.9 defaults); abstract column is four-fifths of that.
- **Section rhythm:** Bulma `.section` padding 3rem 1.5rem; teaser hero-body has `padding-top: 0; padding-bottom: 3rem`.

## Components

- **Venue line.** `div.is-size-4.has-text-weight-bold.publication-conference`, color `#8b0000`, centered under the title, followed by a `<br>`.
- **Author block.** Inline-block spans, superscript affiliation numbers, links in `hsl(204,86%,53%)` with underline on hover. Affiliations on separate lines below.
- **Link button.** `a.external-link.button.is-normal.is-rounded.is-dark`: dark pill, white text, Academicons `ai-arxiv` icon, 5px vertical margin. Only arXiv is shown; no Code button at time of capture.
- **Project navbar.** Custom element, centered flex row, min-height 3.25rem, white background, `<details>` dropdown with a 2px `#3273dc` chevron.
- **Figures.** `img.project-figure` full width; case figures at 90% width (100% on mobile), case sub-heading margin-top 3rem.
- **Footer.** Bulma footer with a single 25px black PDF icon and the CC BY-SA licence plus Nerfies credit.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered, Google Sans, superscript affiliations |
| Venue badge | Yes | Bold dark-red text line, not a pill |
| Link buttons | arXiv only | Dark rounded Bulma buttons |
| Teaser | Static PNG (1616×797) | Full container width, no caption |
| Abstract | Yes | Justified, four-fifths column, centered heading |
| Method figure | Yes | One wide PNG with a lead paragraph |
| Results | Qualitative case figures | Two tall PNGs under `title is-4` sub-heads |
| Tables / videos / sliders / 3D / HF demo | No | |
| BibTeX | Yes | Bulma `pre` on `#f5f5f5` |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep the whole page in one centered 960px column.
- Do let the venue be colored text, not a badge.
- Do use dark pill buttons with icon plus short label.
- Don't introduce card shadows or colored section bands; the template is flat white.
- Don't mix the template's turquoise primary into content; it is never used.

## Surfaces

Two surfaces only: white page and `#f5f5f5` for code. The footer uses Bulma's `#fafafa`.

## Imagery

Wide, white-background diagram PNGs with explicit width/height and `loading="lazy"`. No rounded corners on figures.

## Layout

Single column, centered hero, sections stacked with 3rem padding. Mobile drops the title to 2rem and widens case figures to 100%.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, body `#4a4a4a`, venue `#8b0000`, author links `hsl(204,86%,53%)`, buttons `#363636`, code `#f5f5f5`.

1. "Build a centered hero: Google Sans title at 3rem weight 600 in `#363636`, a bold 1.5rem `#8b0000` venue line, then 1.25rem author spans with blue links and superscript numbers."
2. "Add a row of fully rounded dark buttons (`#363636`, white text, icon left), 5px vertical margin, centered."
3. "Make a BibTeX section: `h2` 'BibTeX' left-aligned at 2rem/600, `pre` with `#f5f5f5` background and 4px radius."

## Similar Pages

Nerfies (nerfies.github.io) and the many 2022–2026 project pages forked from it, e.g. KungfuBot and LangSplatV2 in this collection.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text-strong: #363636;
  --text: #4a4a4a;
  --venue: #8b0000;
  --author-link: hsl(204, 86%, 53%);
  --link: #3273dc;
  --surface: #f5f5f5;
  --line: #dbdbdb;
  --font-display: 'Google Sans', 'Inter', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-pill: 290486px;
  --radius-code: 4px;
  --container: 960px;
}
```

## Provenance

- **URL:** https://fangzhou2000.github.io/projects/v2w/
- **Paper:** From Views to Worlds: Active Exploration over 3D Worlds for Vision-Language Models (arXiv 2610.24676), Qijian Tian et al.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** Nerfies (footer credit), Bulma CSS, shared `../fleg/` assets from the author's earlier project page.
- **Measurement method:** static HTML plus four linked stylesheets parsed with `extract_style.py`; framework defaults filtered by reading markup. The rendered page was not viewed, so container width and font fallback are inferred from Bulma 0.9 defaults.
