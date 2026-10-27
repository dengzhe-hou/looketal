# Bootstrap Icon Row — Style Reference

> A 2016-era lab page: Helvetica, centered everything, and four big icons for links.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A Bootstrap 3.3.5 page in the older icon-row project template family (the `../format/app.css` layout seen on several early-2020s project pages; the exact origin is not credited, inferred). The whole `<body>` is `text-align: center`. Links are not buttons but a `nav nav-pills nav-justified` row of 60px-tall image icons (paper, YouTube, GitHub, slides) with bold `h4` labels below. Both local stylesheets `../format/app.css` and `../format/bootstrap.min.css` return 404, so the page renders on CDN Bootstrap 3 defaults plus one small inline style block for a two-column video grid. Note the title text in the HTML is cut short ("Disentanglemen").

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Bootstrap body background |
| Bootstrap Charcoal | `#333333` | `--text` | Bootstrap 3 body text |
| Pill Blue | `#337ab7` | `--link` | Bootstrap 3 link and nav-pill color |
| Pill Blue Hover | `#286090` | `--link-hover` | Bootstrap 3 hover/active shade |
| Muted Gray | `#777777` | `--muted` | Bootstrap `small` and help text |
| Code Well | `#f5f5f5` | `--bg-well` | Bootstrap `pre` background (BibTeX) |
| Rule Gray | `#dddddd` | `--border` | Bootstrap borders |
| Screen Black | `#000000` | `--media-bg` | `.video-grid video` background |

Alert colors (#3c763d, #8a6d3b, #a94442) and their pastel fills are Bootstrap 3 defaults, not used on the page.

## Tokens — Typography

**Families.** Bootstrap 3 stack: "Helvetica Neue", Helvetica, Arial, sans-serif; Menlo/monospace for code. No web fonts. Substitutes: Arial or Inter.

| Role | Size | Weight | Family |
|---|---|---|---|
| Title (`h1`) | 36px (Bootstrap 3 default) | 500 | Helvetica Neue |
| Section heading (`h3`) | 24px | 500 | Helvetica Neue |
| Author / affiliation (`.h4`) | 18px | 500 | Helvetica Neue |
| Link label (`h4 strong`) | 18px | 700 | Helvetica Neue |
| Body | 14px, line-height 1.42857143 | 400 | Helvetica Neue |
| BibTeX | 13px | 400 | Menlo, monospace |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-sm | 4px | Bootstrap 3 default (`pre`, nav-pills) |
| --radius-lg | 6px | `.video-grid video` (page-own) and Bootstrap large controls |

**Shadows.** None beyond Bootstrap's inset form shadows (`inset 0 1px 1px rgba(0,0,0,.075)`), which this page does not use.

**Layout width.** Bootstrap 3 `.container` (1170px at large breakpoint, framework default); content in `col-md-8 col-md-offset-2` (about 780px). The video grid collapses to one column below 576px.

## Components

- **Icon link row.** `ul.nav.nav-pills.nav-justified` in an 8-column centered block; each `li` holds a 60px image icon, a line break, and `h4 > strong` label (Paper, Video, Code, Supp). The Video item has no anchor in the source.
- **Video grid.** `.video-grid`: CSS grid, 2 equal columns, 12px gap, 15px top margin; each video 100% width, black background, 6px radius.
- **Venue line.** `h3.author-block.is-5` "ICLR 2026" (a commented-out CVPR 2025 line remains in source).
- **BibTeX.** Bootstrap `pre`/CodeMirror textarea with clipboard.js copy (scripts loaded), #f5f5f5 well.

## Page Modules

- **Title/author block.** Centered `h1`, authors as `.h4` spans separated by four non-breaking spaces, affiliation and equal-contribution markers on one line.
- **Link buttons.** Icon row (Paper, Video, Code, Supp), not pills.
- **Teaser / results videos.** Nine videos, many in the 2-column grid.
- **Abstract.** Centered heading, paragraph text.
- **Dataset.** "Our dataset" section with figures.
- **Results.** Visual segmentation results, rendering results for two-part and three-part objects, real-data results.
- **Method overview.** Single figure section.
- **BibTeX.** End of page.
- Not present: footer, template credit, tables, sliders, 3D viewer, demo.

## Do's and Don'ts

**Do**

- Keep everything centered and on Bootstrap defaults if you reproduce this look.
- Use recognizable 60px icons for each link with a bold label underneath.
- Set videos in a two-up grid with small radius on black.

**Don't**

- Don't reference relative stylesheets outside the project folder (they 404 here).
- Don't mix the leftover Bulma class names (`is-4`, `is-5`) expecting Bulma styling; Bulma is not loaded.
- Don't leave link items without anchors.

## Surfaces

Flat white page; black video frames; whitesmoke code well.

## Imagery

Articulated-object renderings and segmentation videos; icon images for links (paper.png, github_icon.jpg, youtube_icon.jpg, slide_icon.jpg).

## Layout

One centered column (col-md-8 offset-2), sections flow without `<section>` tags or `h2`s; headings are `h3`.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Text #333333
- Links #337ab7
- Video frames #000000
- Code well #f5f5f5

**Example component prompts**

1. Create a justified nav-pills row of four links, each a 60px icon image above a bold 18px Helvetica label, centered in a 780px column.
2. Create a two-column video grid with 12px gap, videos 100% wide on black with 6px radius, stacking to one column under 576px.
3. Create a centered Bootstrap 3 title block: 36px h1, author names in #337ab7 as 18px spans, affiliations below in the same size.

## Similar Pages

- Older Bootstrap 3 icon-row project pages (for example the mip-NeRF era layout, inferred).
- Other single-file Bootstrap 3 project pages with `format/app.css`.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #333333;
  --link: #337ab7;
  --link-hover: #286090;
  --muted: #777777;
  --bg-well: #f5f5f5;
  --font-body: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-mono: Menlo, Monaco, Consolas, monospace;
  --radius-sm: 4px;
  --radius-lg: 6px;
}
body { font-family: var(--font-body); font-size: 14px; color: var(--text); text-align: center; }
.video-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-top: 15px; }
.video-grid video { width: 100%; background: #000; border-radius: var(--radius-lg); }
```

## Provenance

- URL: https://haoai-1997.github.io/AiM/
- Paper: Articulation in Motion: Prior-free Part Mobility Analysis for Articulated Objects By Dynamic-Static Disentanglement (Hao Ai et al.), arXiv 2603.02910.
- Venue: ICLR 2026 (per the arXiv comment). Field: 3D vision.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: none on the page; no footer. Template family is inferred from structure.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified. Both local CSS files (`/format/app.css`, `/format/bootstrap.min.css`) returned HTTP 404 at extraction time, so this entry describes the page as it currently serves.
