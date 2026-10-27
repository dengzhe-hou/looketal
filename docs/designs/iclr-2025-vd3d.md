# VD3D Hairline Quiet — Style Reference

> A gallery catalogue: light sans captions, Palatino essays and a thin rule between every room.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide screenshots, the page's `data/assets/css/styles.css` (DreamFusion/MVDream template), inline styles, and Bootstrap 4.5.0 defaults. Color share is measured on the first 1440×900 viewport.

## Overview

A DreamFusion-family page on Bootstrap 4. Headings and author names are Source Sans Pro at weight 300, so the hero reads as thin grey-black type with bright Bootstrap-blue (#007bff) author links. The title is a single 33px line with "VD3D" in bold. A 15px affiliation key, a 22px light "ICLR 2025", and three pale #f8f9fa buttons with 24px SVG icons (Paper, Gallery, Code) complete the hero. Each section then sits in a narrow 768px column between 1px hairline rules: a 4×4 mosaic teaser video framed by a thin black border inside the frames, an Abstract in Palatino 16px, a Method figure with pastel blocks, and a three-column results layout (camera trajectory plot, reference video, generated video with a tiny 11px Palatino caption). Blue "More Results" block buttons link out to galleries. The BibTeX is a bare Bootstrap `<code>` in pink. Whitespace and the narrow measure do most of the work.

## First Viewport

Color share (1440×900, 8-color quantize): white #ffffff 69.5% (plus #fdffff 1.3%), the teaser mosaic's warm browns #7c7064 7.8% and near-black #2b2120 7.5%, pale aqua #a8bbbb 5.8%, light grey #f6f8fa 4.4% (button fills and hairlines blended), sand #e2d7cc 3.5%. Blue author links are under 1%.

Anatomy in DOM order (all centred; `.highlight-clean` wrapper with 20px top padding):

1. **Title** — `h1.text-center` inline 33px / 300 / 36.3px, #212529, "VD3D" in `<b>` (700 rendered as Source Sans Pro 400, the heaviest weight loaded), one line in a 1024px container (y=20–56). Container margin-bottom 20px.
2. **Authors** — `.authors a`, inline-block, 20px / 300, #007bff, padding 5px, superscripts in #313436; twelve names on two lines of six (y=76–156).
3. **Affiliations** — `.affiliations`, 15px / 300, #212529, four `span`s with superscript keys, margin-bottom 20px (about y=160).
4. **Venue** — `h1.text-center` inline 22px / 300, #212529, "ICLR 2025" (y=199–223). Gap 20px.
5. **Buttons** — `.buttons` (8px top and bottom margin), three `a.btn.btn-light`: 40px tall, padding 6px 12px, #f8f9fa fill and 1px #f8f9fa border, radius 4px, 16px / 400 #212529 labels, 24px SVG icon left with -12px/12px side margins (document, play triangle, GitHub). Buttons touch each other (y=243–283).
6. **Hairline** — `hr.divider`, max-width 768px, 1px rgba(0,0,0,0.1), margins 32px.
7. **Teaser** — `video.video.lazy` in a 768px container, 738×418 at x=351, y=348; a 4×4 mosaic of generated clips with a thin black grid baked in.
8. **Next hairline and "Abstract"** — h2 32px / 300 at y=837, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bootstrap `body` background | page |
| Ink | #212529 | Bootstrap `$body-color` | title, venue, section h2, paragraphs, button labels |
| Link Blue | #007bff | Bootstrap `$primary` / link color | author names, inline links, "More Results" button fill |
| Superscript Slate | #313436 | `.authors sup` | affiliation numbers after names |
| Button Mist | #f8f9fa | `.btn-light` | Paper / Gallery / Code button fill and border |
| Hairline | rgba(0,0,0,0.1) | Bootstrap `hr` border-top | dividers between sections |
| Code Pink | #e83e8c | Bootstrap `code` color | BibTeX text |
| Mosaic Umber | #7c7064 | (video) | dominant warm tone of the teaser mosaic |

## Tokens — Typography

- **Display / UI:** declared `"Source Sans Pro", Calibri, Candara, Arial, sans-serif` on body and h1–h6, weight 300, line-height 1.1 for headings. Rendered: Source Sans Pro 300 and 400 (no 700 loaded, so `<b>` renders at 400 or synthesized). Substitute: Source Sans 3.
- **Reading text:** declared `Palatino, "Palatino Linotype", "Palatino LT STD", "Book Antiqua", Georgia, serif` on `p` and `.caption`. Rendered: Palatino Linotype (system font on Windows; Palatino on macOS). Substitute: TeX Gyre Pagella.
- **Code:** Bootstrap `SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`, 14px (87.5%).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Paper title | `h1.text-center` (inline 33px) | 33px / 300 / 36.3px |
| Venue | `h1.text-center` (inline 22px) | 22px / 300 |
| Section title | `h2` | 32px / 300 / 35.2px, margin-bottom 8px |
| Authors | `.authors a` | 20px / 300 |
| Affiliations | `.affiliations` | 15px / 300 |
| Body | `p` | Palatino 16px / 300 declared (renders regular) / 24px, margin-top 4px |
| Column titles | `.compare-title p` | Palatino 16px, centred |
| Video captions | `h6.caption` (inline 11px) | Palatino 11px / 400 |
| Buttons | `.btn` | 16px / 400; `.btn-lg` 20px |
| BibTeX | `code` | 14px mono |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | radius 4px (`.btn`), 4.8px (`.btn-lg`); no shadow |
| Dividers | `hr.divider`, 1px, max-width 768px, 32px above and below |
| Rows | `.row:not(:last-child):not(.authors)` margin-bottom 16px |
| Videos, figures | square corners; any frame is inside the media |
| Shadows | none |

## Layout Metrics

- **Hero container:** `.container` with inline `max-width: 1024px`, 15px side padding (content 994px).
- **Reading column:** `.container` with inline `max-width: 768px` for every section (content 738px, x=351–1089 at 1440).
- **Hero padding:** 20px top, 0 bottom; 20px margins below title and venue blocks; buttons 8px vertical margin.
- **Sections:** hairline (32px margins) → h2 → `p` (4px top, 16px bottom margin) → media.
- **Results grid:** three `.col-xs-33` (33.33%) title cells, then rows of `.col-xs-33` (trajectory plot) + `.col-xs-64` (reference and generated videos) with an 11px caption offset 53% to sit under the third column.
- **"More Results":** `col-sm-4` centred, `btn-lg btn-search` block button, padding 12px 20px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥769px | (viewport − 768)/2 + 15px for sections | 16px | 33px | 3-column results; 4×4 teaser |
| ≤768px | 15px | 16px | 33px | `.btn-search` 16px with 4px side padding |
| 576–600px | 15px | 16px | 33px | `.citation` margins drop (template rule) |
| ≤575px | 15px | 12px Palatino | 33px | `.compare-title` and captions 12px; video compare containers gain 32px top padding |

## Components

- **Light icon button:** `a.btn.btn-light`, #f8f9fa fill and border, #212529 16px label, 4px radius, padding 6px 12px, 24px inline SVG icon pulled left (margin -12px left, 12px right); buttons sit flush with no gap; Bootstrap hover darkens the fill slightly.
- **Hairline section break:** `hr.divider`, 768px max, 1px rgba(0,0,0,0.1), 32px vertical margins, between every section.
- **Comparison row:** three equal columns with Palatino 16px column titles ("Camera Input", "Reference Trajectory Video", "Camera Controlled Generation"); left a white 3D trajectory plot video, middle and right autoplay clips; an 11px Palatino caption under the generated clip.
- **More Results button:** `btn btn-primary btn-lg btn-search`, #007bff fill, white 20px label, 4.8px radius, padding 12px 20px, centred block.
- **BibTeX:** inline Bootstrap `code` in #e83e8c with `<br>` line breaks and `&nbsp;` indents; no box or background.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | Yes | light sans, blue author links, 15px key |
| Venue line | Yes | 22px light "ICLR 2025" |
| Link buttons | Yes | three pale icon buttons |
| Teaser | Yes | 4×4 mosaic video, 738px |
| Abstract | Yes | Palatino 16px, left aligned |
| Method figure | Yes | full-width diagram after the text |
| Results comparison | Yes | three-column trajectory / reference / generated rows |
| Out-of-distribution results | Yes | same row recipe |
| Image-to-multiview results | Yes | `col-4` video triplets with 11px captions |
| Gallery links | Yes | blue "More Results" block buttons to separate gallery pages |
| Results table | No (absent from the source) | |
| BibTeX | Present but non-standard | inline pink `code`, no box |
| Footer | Yes | one line crediting DreamFusion and MVDream templates |

## Adapting to Other Content

- **More authors:** keep inline-block names at 20px with 5px padding; they wrap in centred rows; keep superscripts #313436.
- **Results table:** fit it in the 738px column, Source Sans Pro 16px, header weight 400, rows separated by 1px rgba(0,0,0,0.1) to match the hairlines; no fills.
- **Long news or publication lists:** use the template's own `.citation` recipe (bold 1em title, 12px author line, italic venue h6, small grey or sky-blue venue tag) inside the 768px column.
- **More links:** add further `btn-light` icon buttons in the same flush row; keep icons 24px monochrome SVG.
- **Wide media:** let a teaser break out to the 1024px hero container, but keep text at 738px.

## Do's and Don'ts

- Do keep headings at weight 300 and let size, not weight, build the hierarchy.
- Do set paragraphs in Palatino against light sans headings; the contrast is the look.
- Do separate every section with the same 768px hairline and 32px margins.
- Don't widen the reading column past 768px.
- Don't add color beyond Bootstrap blue for links and the gallery button.
- Don't leave BibTeX as bare pink inline code in new work; a #f8f9fa block with the same mono reads better.

## Surfaces

White page; pale #f8f9fa buttons; no bands, cards or shadows. The teaser and comparison media supply all colour.

## Imagery

A 4×4 mosaic of whimsical text-to-video results (cats, otters, astronauts), a pastel architecture diagram (lavender, green, pink blocks), white 3D camera-trajectory plots beside interior walkthrough clips, and generated videos with prompts as captions.

## Layout

Centred hero in a 1024px container, then a single 768px column of hairline-separated sections. Rendered height about 4,650px.

## Agent Prompt Guide

Quick colors: text #212529, links #007bff, superscripts #313436, button #f8f9fa, hairline rgba(0,0,0,0.1), code #e83e8c, page #ffffff.

1. "Create a hero: one-line 33px Source Sans Pro 300 title in #212529 with the acronym bold; authors as inline-block 20px / 300 #007bff links with 5px padding and #313436 superscripts; a 15px affiliation line; a 22px / 300 venue line; then flush #f8f9fa buttons with 4px radius, padding 6px 12px, 16px #212529 labels and 24px monochrome SVG icons on the left."
2. "Separate sections with a 1px rgba(0,0,0,0.1) rule, max-width 768px, 32px margins; each section a 768px container with a 32px / 300 h2 and Palatino 16px paragraphs at 24px line height."
3. "Build a comparison row: three equal columns titled in 16px Palatino (Camera Input, Reference Trajectory Video, Camera Controlled Generation), each with an autoplay video, and an 11px Palatino caption under the third column."

## Similar Pages

- DreamFusion and MVDream (stated template sources), and other Snap Research 3D/video pages built on the same template (for example AC3D, 4Real).
- Pages that mix a light sans for headings with Palatino body copy.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #212529;
  --link: #007bff;
  --sup: #313436;
  --button: #f8f9fa;
  --hairline: rgba(0, 0, 0, 0.1);
  --code: #e83e8c;
  --font-sans: "Source Sans Pro", Calibri, Candara, Arial, sans-serif;
  --font-serif: Palatino, "Palatino Linotype", "Book Antiqua", Georgia, serif;
  --title-size: 33px;
  --h2-size: 32px;
  --body-size: 16px;
  --heading-weight: 300;
  --hero-width: 1024px;
  --column: 768px;
}
```

## Provenance

- **URL:** https://snap-research.github.io/vd3d/
- **Paper:** VD3D: Taming Large Video Diffusion Transformers for 3D Camera Control (arXiv 2407.12781), Sherwin Bahmani et al.
- **Venue:** ICLR 2025 (stated on the page).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025; project page linked in the comment.
- **Template credit:** footer says the template is from DreamFusion and MVDream.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, 1440 screenshots (first viewport and tall), `data/assets/css/styles.css`, inline styles, Bootstrap 4.5.0 defaults; 2026-10-28.
