# FIPER — Style Reference

> Lato on Bootstrap, a quiet lab report with one lavender TL;DR strip.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bootstrap 5.3.2 from jsDelivr plus the page's `css/app.css`, which descends from the Ref-NeRF/ReconFusion page style) and roles are interpreted from selectors and one rendered look. Bootstrap's button and table variables (`#0d6efd`, `#6c757d` etc.) dominate frequency counts but are not visible on the page and are excluded.

## Overview

FIPER is a narrow, text-forward Bootstrap page. Every content row is `col-md-8 offset-md-2` (nine of them), so the reading column is two-thirds of the container, left-aligned headings in Lato light, and justified paragraphs. The title is an `h2` with only "FIPER:" in bold. Authors are blue `#1772d0` Lato links at `min(3vw, 15px)` that turn orange `#f09228` on hover, which is the Jon-Barron-lineage link pair. Two dark Bulma-style pill buttons (arXiv, Code) are hand-copied into `app.css`. The one color block is a lavender `#d0d5ec` rounded TL;DR strip after the abstract. BibTeX lives in a read-only `<textarea class="form-control">`.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page background |
| Ink Black | `#000000` | — | Headings, TL;DR text |
| Barron Blue | `#1772d0` | — | Links, author names |
| Tangerine Hover | `#f09228` | — | Link hover and focus |
| Lavender Strip | `#d0d5ec` | inline | TL;DR banner background |
| Charcoal Button | `#363636` | — | arXiv / Code pill fill |
| Highlight Cream | `#ffffd0` | — | `span.highlight` background (rule present) |
| Bootstrap Body | `#212529` (inferred, Bootstrap default) | `--bs-body-color` | Paragraph text |

## Tokens — Typography

- **Family:** Lato (`'Lato', Verdana, Helvetica, sans-serif`) for `h2`–`h6` and links; Noto Sans for buttons. Lato is referenced but not loaded from Google Fonts in the static HTML, so rendering falls back to Verdana where Lato is not installed (inferred).
- **Weights:** 300 for Bootstrap headings, 700 for the bold "FIPER:" prefix and `<b>` terms, 400 body.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Title (`h2`) | calc(1.325rem + .9vw) → 2rem | 300 + bold prefix | Centered |
| Section (`h3`) | calc(1.3rem + .6vw) → 1.75rem | 300 | Left-aligned |
| Authors / affiliations | calc(min(3vw, 15px)) | 400 | Inline styles |
| Links | 15px | 400 | Lato |
| Body | 1rem | 400 | Justified (`text-justify`) |
| Button | 15px (inline) | inherit | Width 80px / 190px inline |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| TL;DR strip (`.rounded`) | 0.375rem (Bootstrap `--bs-border-radius`, inferred) |
| Scene pills (unused here) | 5px |

- **Shadows:** none.
- **Layout width:** outer `.container-lg` with inline `max-width: 1500px`; content in `col-md-8 offset-md-2` rows inside Bootstrap `.container` (960px at lg, 1140px at xl; Bootstrap defaults, inferred).
- **Button metrics:** height 2.5em, padding calc(.5em − 1px) calc(1em + .25em).

## Components

- **Link button:** copied Bulma `.button.is-dark.is-rounded`: `#363636` fill, white text and icon, pill radius, fixed inline widths.
- **Author list:** `ul.list-inline` with no wrapping (`white-space: nowrap`), Barron Blue links, Unicode superscript digits.
- **TL;DR strip:** `col-md-8 offset-md-2 rounded`, background `#d0d5ec`, `h6` centered with bold "TL;DR".
- **Section header:** `h3` left-aligned, Lato light, no rule or ornament.
- **BibTeX:** Bootstrap `textarea.form-control` (readonly), CodeMirror CSS loaded.
- **3D title hover:** `.title3d` stacked text-shadow ramp (`#222525` → `#d0d0d0`) defined in CSS; not used on this title.

## Page Modules

- **Title/author block:** centered `h2` title, five authors, three affiliations (NYCU, Johns Hopkins, Academia Sinica) on one line.
- **Venue badge:** none; NeurIPS 2025 appears only inside the BibTeX entry.
- **Link buttons:** arXiv, Code.
- **Teaser:** none above the fold; the abstract follows the buttons directly.
- **Abstract:** left `h3`, justified paragraph, then the lavender TL;DR.
- **Method figures:** comparison of representations, full formulation, SR + compression pipeline.
- **Results:** visual SR comparison (4×) and RD-curve plots as images; no HTML tables.
- **BibTeX:** textarea.
- **Not present:** video, image-comparison slider, HF demo, acknowledgements. A Gaussian-splat carousel script (`js/splats.js`) is imported, but no viewer was visible in the render.

## Do's and Don'ts

- Do keep the reading column at two-thirds width with left-aligned headings.
- Do use the blue/orange link pair for every hyperlink.
- Do reserve color fills for a single TL;DR callout.
- Don't center section headings; only the title is centered.
- Don't mix in Bootstrap primary blue `#0d6efd`; the page never shows it.
- Don't rely on Lato being present; load it or pick a matching fallback.

## Surfaces

One white surface. The TL;DR strip is the only tinted block; the textarea uses Bootstrap's default form border.

## Imagery

Paper figures exported as wide PNGs: architecture comparisons, equation figure, qualitative zoom crops, rate-distortion plots.

## Layout

Stacked Bootstrap rows, each a centered 8/12 column. No grid of media, no carousel in use.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#000000`, link `#1772d0`, hover `#f09228`, callout `#d0d5ec`, button `#363636`.

1. "Build a Bootstrap 5 paper header: centered h2 title with a bold acronym prefix, a nowrap inline author list in Lato with `#1772d0` links that turn `#f09228` on hover, and two dark pill buttons (`#363636`, radius 290486px)."
2. "Add a TL;DR callout: an 8/12 centered column with `#d0d5ec` background, small rounded corners, centered h6 text with bold 'TL;DR:' label."
3. "Create a BibTeX area as a readonly Bootstrap textarea under a left-aligned Lato h3."

## Similar Pages

Ref-NeRF, ReconFusion and Michaël Gharbi's page lineage (credited in the footer); Jon Barron-style link colors.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --link: #1772d0;
  --link-hover: #f09228;
  --callout: #d0d5ec;
  --button: #363636;
  --highlight: #ffffd0;
  --radius-pill: 290486px;
  --font: 'Lato', Verdana, Helvetica, sans-serif;
  --font-button: 'Noto Sans', sans-serif;
}
a { color: var(--link); text-decoration: none; }
a:hover, a:focus { color: var(--link-hover); }
```

## Provenance

- **URL:** https://jayisaking.github.io/FIPER/
- **Paper:** FIPER: Factorized Features for Robust Image Super-Resolution and Compression (arXiv 2410.18083), Yang-Che Sun et al., NYCU / JHU / Academia Sinica.
- **Venue:** NeurIPS 2025 per arXiv comment and the BibTeX (`Conference on Neural Information Processing Systems`, 2025); no venue badge on the page.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer says the template was borrowed from Michaël Gharbi, Ref-NeRF and ReconFusion.
- **Measurement method:** `extract_style.py` counts, manual reading of HTML and `css/app.css`, one rendered screenshot. Bootstrap defaults marked inferred; the splat carousel was not exercised.
