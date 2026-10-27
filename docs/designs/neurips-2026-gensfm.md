# GenSfM Gallery Viewer — Style Reference

> A quiet museum catalogue with a Georgia headline and a live 3D vitrine.

**Theme:** light

Values come from `styles.css` and `results.css`. The HTML ships as an empty shell: title, authors, links and results are filled at runtime from `data/content.json`, which was read separately to recover link labels and venue. No framework. Roles are interpreted. Rendered output was not viewed.

## Overview

GenSfM (HKU, Transengram, Tencent) is a product-grade single page around an interactive three.js object explorer. The palette is near-black ink `#1b1d24`, cool gray `#656b78`, hairline `#e3e6ee`, a quiet surface `#f7f8fb`, and one indigo accent `#3656c6`. Inter (self-hosted variable font) runs everything except the h1, which is Georgia 400 at up to 64px with tight tracking. A 75px header carries a stroked SVG wordmark. Under the title come a muted subtitle, authors with indigo superscripts, and resource links as 8px-radius bordered buttons (the first one filled ink). A 16:9 film frame with a soft drop shadow plays the paper video, then a full-bleed surface band hosts the 3D gallery: dataset filter chips, a scrolling object rail, and a viewer panel with framing controls and scene toggles. Quantitative results are horizontal bar charts with the method's bar in indigo and baselines in gray.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Gallery White | `#ffffff` | `--paper` | Page background, cards |
| Graphite Ink | `#1b1d24` | `--ink` | Text, first resource button, shadow color |
| Label Gray | `#656b78` | `--muted` | Subtitle, nav, captions, metric labels |
| Hairline | `#e3e6ee` | `--line` | Borders, header rule, band rules |
| Vitrine Surface | `#f7f8fb` | `--surface` | Gallery band, film frame, viewer canvas, bar tracks |
| Indigo | `#3656c6` | `--accent` | Eyebrows, superscripts, wordmark stroke, focus, highlighted bars, button hover |
| Indigo Wash | `#eef2ff` | `--accent-soft` | Pressed framing controls and dataset tabs |
| Baseline Bar | `#b7bdca` | `--bar-muted` | Non-highlighted metric bars |
| Hover Indigo | `#8799db` | (literal) | Object option hover border |
| Citation Panel | `#f7f8fa` | (literal) | BibTeX `pre` background |
| Citation Text | `#353a46` | (literal) | BibTeX text |
| Error Clay | `#b67555` | (literal) | Viewer loading error dot |
| GT Dash | `#747e89` | (literal) | Ground-truth camera dashed legend |

## Tokens — Typography

- **Sans:** `Inter` variable (self-hosted woff2, 100–900), fallback -apple-system, Segoe UI.
- **Serif:** Georgia, "Times New Roman" (h1 only).
- **Mono:** ui-monospace, SFMono-Regular, Consolas, "Liberation Mono".
- **Weights:** 400 body, 500 headings, wordmark and highlighted rows; 600 citation title.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| h1 (serif) | `clamp(38px, 4.5vw, 64px)` | 400 | 1.12 | -0.035em, balanced |
| h2 | `clamp(30px, 3.3vw, 43px)` | 500 | 1.18 | -0.035em |
| h3 | 29px (18px in metric cards) | 500 | 1.18 | -0.025em |
| Wordmark | 23px | 500 | | -0.03em |
| Subtitle | 21px | 400 | 1.6 | max 880px |
| Body | 18px | 400 | 1.6 | |
| Authors | 18px | 400 | | superscripts 11px indigo |
| Nav, buttons, captions | 16px | 400 | | |
| Citation code | 15px (14px small screens) | 400 | 1.65 | |
| Eyebrow | 13px (12px in viewer) | 500 | | indigo |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Film frame | 16px |
| Object detail card | 14px |
| Object options, metric cards, method figure | 10px |
| Resource buttons | 8px |
| Dataset filter chips, input thumbs | 7px |
| Framing control group / buttons, citation pre | 6px / 4px, 6px |
| Status pill, protocol tag | 30px |
| Rail arrows | 50% |

- **Shadows:** film frame `0 14px 50px -36px #1b1d24`; object detail `0 8px 25px -23px #1b1d24`; selected option ring `0 0 0 2px #3656c624`. All very faint.
- **Layout:** `--page: 1240px`, shell width `min(1240px, 100% - 88px)`; results intro 780px.
- **Rhythm:** intro 63px top / 40px bottom; gallery band 62px / 65px with top and bottom hairlines.

## Components

- **Header.** 75px tall, white at 97% opacity, bottom hairline, wordmark with a 30px stroked SVG in indigo, 16px gray nav with 30px gaps.
- **Resource link.** 1px hairline border, 10px 20px padding, 8px radius, 16px text. The first link (arXiv) is ink-filled with white text. Hover turns any link indigo with white text. Labels: arXiv, Code, Models, Explore results.
- **Film frame.** 16:9, hairline border, 16px radius, surface background, `object-fit: contain`, caption row with an indigo "Explore in 3D ↓" link.
- **3D explorer.** Object rail of 10px-radius cards (selected: indigo border plus 2px translucent ring), detail card with a viewer canvas on surface gray, segmented framing controls, checkbox toggles with `accent-color: #3656c6`.
- **Metric bar chart.** White 10px cards; each row has label and tabular value above a surface-gray track; GenSfM's row is indigo text and fill, baselines `#b7bdca`.
- **Citation.** `#f7f8fa` pre, hairline border, 6px radius, 24px 26px padding.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes (JS-rendered) | Georgia h1, Inter authors, indigo superscripts |
| Venue badge | `paper-status` pill (indigo text, hairline border, 30px radius), filled from JSON "NeurIPS 2026" (inferred) | |
| Link buttons | arXiv, Code, Models (HF), Explore results | Bordered 8px buttons |
| Teaser | Paper film in framed 16:9 player | |
| Interactive 3D | three.js object explorer with dataset filters | |
| Abstract / contributions | Overview section "From four views to 3D." | |
| Method figure | "How it works" | 10px radius |
| Results | Bar-chart cards with dataset tabs, expandable full table | |
| Sliders / HF Space | No | |
| BibTeX | Citation section | Light panel |
| Acknowledgements | No | |

## Do's and Don'ts

- Do reserve indigo for the method's own data and the interactive state.
- Do keep the headline serif and everything else Inter.
- Do place the 3D explorer on a full-bleed surface band framed by hairlines.
- Don't use heavy shadows; offsets of -23 to -36px keep them barely visible.
- Don't color baselines; they stay `#b7bdca`.

## Surfaces

White page, `#f7f8fb` band and viewer, white cards on the band, `#f7f8fa` code panel.

## Imagery

A narrated paper video, a method figure, input-view thumbnails with per-view colored borders, and live 3D renders in canvas.

## Layout

1240px shell with 44px side gutters; centered intro; gallery splits into a viewer panel and an input panel separated by a hairline.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, surface `#f7f8fb`, ink `#1b1d24`, muted `#656b78`, line `#e3e6ee`, accent `#3656c6`, accent-soft `#eef2ff`, baseline `#b7bdca`.

1. "Center a Georgia 400 h1 at `clamp(38px,4.5vw,64px)` with -0.035em tracking, a 21px `#656b78` subtitle, then bordered 8px-radius links where the first is filled `#1b1d24`; hover fills `#3656c6`."
2. "Make a 16:9 video frame: 1px `#e3e6ee` border, 16px radius, `#f7f8fb` background, shadow `0 14px 50px -36px #1b1d24`."
3. "Build a horizontal bar metric card: white, 10px radius; rows with 14px labels and tabular values; tracks `#f7f8fb`; our bar `#3656c6`, others `#b7bdca`."

## Similar Pages

Polished single-product research pages with a hosted 3D viewer, such as AEON and 4DGT in this collection.

## Quick Start

```css
:root {
  --paper: #ffffff; --ink: #1b1d24; --muted: #656b78; --line: #e3e6ee;
  --accent: #3656c6; --accent-soft: #eef2ff; --surface: #f7f8fb; --bar-muted: #b7bdca;
  --sans: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --serif: Georgia, 'Times New Roman', serif;
  --mono: ui-monospace, SFMono-Regular, Consolas, monospace;
  --page: 1240px; --radius-btn: 8px; --radius-card: 10px; --radius-film: 16px;
}
body { font: 400 18px/1.6 var(--sans); color: var(--ink); background: var(--paper); }
```

## Provenance

- **URL:** https://dotb1ue.github.io/GenSfm/
- **Paper:** Generative Structure from Motion with Native 3D Diffusion (GenSfM, arXiv 2610.35522), Haobin Duan et al., HKU, Transengram, Tencent.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** none; custom page.
- **Measurement method:** static HTML shell, two stylesheets, and `data/content.json` (for authors, venue and resource labels) read directly. The extractor reported no arXiv link because links are injected by JavaScript. Not viewed in a browser.
