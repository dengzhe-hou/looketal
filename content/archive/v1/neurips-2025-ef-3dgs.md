# EF-3DGS — Style Reference

> A stock Nerfies sheet turned into a wall of side-by-side video loops.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9 plus Nerfies `index.css`, a partial Bootstrap file, Juxtapose and small gallery stylesheets) and roles are interpreted from selectors and one rendered look. Bulma's unused palette (`#00d1b2`, `#ffdd57`, `#3298dc`) appears in frequency counts but not on the page and is excluded. One linked stylesheet (`image_card_fader.css`) returns 404.

## Overview

EF-3DGS is an almost untouched Nerfies page whose personality comes from content density: 26 autoplaying, muted, looping `<video>` elements laid out in Bulma `is-half` columns (28 half columns on the page), plus 11 Juxtapose before/after sliders for comparisons. Chrome is minimal: white background, Google Sans title, Noto Sans body, one dark pill button (arXiv), and centered `title is-3` section headings. The only page-specific colors are two inline text colors used as a legend for trajectory plots.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page and hero background |
| Bulma Ink | `#363636` | (Bulma `$grey-darker`) | Titles, dark button fill |
| Body Graphite | `#4a4a4a` | (Bulma `$grey-dark`) | Body text |
| Bulma Link Blue | `#3273dc` | (Bulma `$link`) | Author and inline links |
| Smoke | `#f5f5f5` | — | `pre` background, `.interpolation-panel` |
| Card Edge | `#bbb` | — | 1px border on `.results-carousel .item` |
| Venue Grey | `#555` | — | `.publication-venue` (template rule; no venue rendered) |
| Trajectory Red | `rgb(214, 39, 40)` | inline | Text legend for "estimated" pose trajectories |
| Trajectory Green | `rgb(0, 127, 0)` | inline | Text legend for "ground truth" trajectories |
| Juxtapose Label | `#000` @ .7 alpha | — | Slider label chips |

## Tokens — Typography

- **Title family:** Google Sans (Google Fonts link `Google Sans|Noto Sans|Castoro`) on `.publication-title`, `.title`. Substitute: Product Sans, Inter.
- **Body family:** Noto Sans. Substitute: Open Sans.
- **Weights:** 400 body, 600 Bulma titles, 700 bold emphasis.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`.title.is-1`) | 3rem | 600 | Google Sans, `#363636` |
| Section title (`.title.is-3`) | 2rem | 600 | Centered |
| Authors (`.is-size-5`) | 1.25rem | 400 | Links `#3273dc` |
| Body | 1rem | 400 | line-height 1.5 |
| Juxtapose label | 1em | 400 | White on translucent black |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link button (`is-rounded`) | 290486px (pill) |
| Carousel item, interpolation panel | 10px |
| Bulma default controls | 4px |

- **Shadows:** none page-specific; Bulma focus ring `0 0 0 .125em rgba(50,115,220,.25)` only.
- **Layout width:** `.container.is-max-desktop` (Bulma 960px, inferred) for text; video grids use `is-full-width` containers with `max-width: 1440px` from Nerfies CSS.

## Components

- **Link button:** `.button.is-normal.is-rounded.is-dark` fill `#363636`, white text, pill radius, academicons arXiv glyph. Only one button (arXiv).
- **Video tile:** `<video autoplay controls muted loop height="100%">` inside `.column.is-half`, with a caption line underneath.
- **Before/after slider:** Juxtapose (`div.jx-slider`), handle and labels in white `#f3f3f3` on black at alpha .7.
- **Section heading:** `h2.title.is-3.has-text-centered`.
- **BibTeX:** Bulma `pre` on `#f5f5f5`; content reads "To be updated".

## Page Modules

- **Title/author block:** Google Sans title, eight authors with superscripts, one affiliation (University of Science and Technology of China).
- **Venue badge:** none rendered; NeurIPS 2025 does not appear on the page.
- **Link buttons:** arXiv only; no Code/Data/Demo buttons in the hero.
- **Teaser:** figure of event stream versus discrete frames, then a four-up row of comparison videos.
- **Abstract:** centered `is-four-fifths` column, justified text.
- **Method figure:** "Framework" image.
- **Results:** "Comparisons" (Tanks and Temples, EvReal-DAVIS) as dense video grids and Juxtapose sliders; "Camera Pose Estimation" trajectory videos with red/green text legend.
- **BibTeX:** placeholder.
- **Not present:** results tables, 3D viewer, HF demo, acknowledgements.

## Do's and Don'ts

- Do let paired videos carry the page; keep them muted, looping and the same height.
- Do use plain colored words as a legend when plots use red and green lines.
- Don't add color to chrome; everything except media is grey on white.
- Don't leave linked CSS files missing (one 404 here).
- Don't rely on red/green alone for meaning; add labels for color-blind readers.

## Surfaces

Flat white throughout. Light grey `#f5f5f5` appears only in code and the template's interpolation panel. Media tiles carry no shadows.

## Imagery

Rendered novel-view videos of indoor and outdoor scenes, event-camera visualizations, trajectory plots. Media is the dominant visual element.

## Layout

Centered single column for text; two-column (`is-half`) and four-up grids for video comparisons, separated by `.section` blocks with centered headings.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, body `#4a4a4a`, link `#3273dc`, code bg `#f5f5f5`, legend red `rgb(214,39,40)`, legend green `rgb(0,127,0)`.

1. "Make a Nerfies-style hero: Google Sans 3rem title in `#363636`, Noto Sans author line with `#3273dc` links, and a single dark pill arXiv button (`#363636`, radius 290486px)."
2. "Build a two-column grid of autoplaying muted looping videos (Bulma `column is-half`), each with a centered caption, under a centered `title is-3` heading."
3. "Add a Juxtapose before/after slider with white handle and black 70% alpha labels, full column width."

## Similar Pages

Classic Nerfies derivatives for 3D Gaussian Splatting and NeRF papers, e.g. PlanarGS and GOATex in this batch.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --link: #3273dc;
  --code-bg: #f5f5f5;
  --card-border: #bbb;
  --legend-est: rgb(214, 39, 40);
  --legend-gt: rgb(0, 127, 0);
  --radius-card: 10px;
  --radius-pill: 290486px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL:** https://lbh666.github.io/ef-3dgs/
- **Paper:** EF-3DGS: Event-Aided Free-Trajectory 3D Gaussian Splatting (arXiv 2410.15392), Bohao Liao et al., USTC.
- **Venue:** NeurIPS 2025 per arXiv comment; the page itself shows no venue line.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says "The template is borrowed from Nerfies".
- **Measurement method:** `extract_style.py` counts, manual reading of HTML and local CSS (`index.css`, `tab_gallery.css`, `image_card_slider.css`, `juxtapose.css`), one rendered screenshot of the hero. Video playback and slider interaction not exercised.
