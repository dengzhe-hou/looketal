# SALAD Biolinum Nerfies — Style Reference

> The Nerfies layout reset in Linux Biolinum, like a motion-capture lab report typed on a LaTeX workstation.

**Theme:** light

Measurements come from the page's `static/css/index.css` (the Nerfies/Academic Project Page Template file with local edits) plus Bulma 0.9 defaults. Bulma's full palette (`#00d1b2`, `#3273dc`, `#ffdd57` …) dominates the frequency counts but almost none of it is used by this page; the colors below are the ones the markup actually references. Roles are interpreted.

## Overview

A standard Bulma hero stack (title hero, YouTube teaser, light abstract band, white overview, light video band) whose identity comes from one change: every text class (`body`, `.title`, `.subtitle`, `.content`, `.button`, `.author-block`) is switched to **Linux Biolinum**, loaded from `fonts.cdnfonts.com`, and titles drop to weight 400. That gives the page the look of a LaTeX paper set in Libertine's sans companion. Colour is Bulma's: near-black rounded buttons, `#f5f5f5` light bands, and author links in Bulma's info blue. The venue appears as plain text after the lab name. The results area is a carousel of 13 autoplaying motion-editing MP4s.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Bulma Charcoal | `#363636` | Bulma `$dark` / text strong | `is-dark` buttons; title text |
| Body Graphite | `#4a4a4a` | Bulma `$text` | Paragraph text |
| Info Sky | `hsl(204, 86%, 53%)` (≈ `#209cee`, inferred conversion) | `.publication-authors a` | Author links |
| Lab Bench | `#f5f5f5` | Bulma `hero.is-light` | Abstract and results bands |
| Paper | `#ffffff` | Bulma body | Page and overview band |
| Venue Grey | `#555555` | `.publication-venue` | Defined; venue here is inline in the affiliation block |
| Award Rose | `#ff3860` | `.publication-awards` | Defined, unused (no award) |
| Footer Ink | `#000000` | `.footer .icon-link` | Footer icons |
| Pager Black | `#000000` | `.slider-pagination .slider-page` | Carousel dots |
| Footer Band | `#fafafa` | Bulma `.footer` default (inferred) | Footer background |

## Tokens — Typography

- **All text:** `'Linux Biolinum', Arial, sans-serif` via `@import url('https://fonts.cdnfonts.com/css/linux-biolinum')`. Substitute: Linux Libertine sans, Biolinum O, or Source Sans 3.
- **Also linked but overridden:** Google Fonts `Google Sans|Noto Sans|Castoro` (the template default link stays in `<head>`).
- **Mono:** Bulma default `monospace`.
- **Weights:** titles and subtitles 400; venue bold; Bulma 600 for strong.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 3rem (Bulma) | 400 | 1.125 | Biolinum |
| Section title (`title is-3`) | 2rem (Bulma) | 400 | 1.125 | centered |
| Figure subtitle (`subtitle has-text-centered` h2) | 1.25rem (Bulma) | 400 | 1.25 | captions under each overview figure |
| Authors | 1.22rem | 400 | 1.5 | `is-size-5` overridden |
| Body / `p` / `li` | 1.12rem | 400 | 1.5 | justified in abstract |
| Buttons | 1rem | 400 | 1.5 | Biolinum |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons (`is-rounded`) | 290486px (pill) |
| YouTube frame (`.publication-video`) | 10px |
| Bulma controls | 4px |

- **Shadows:** none added; Bulma focus ring `0 0 0 .125em rgba(50,115,220,.25)` only.
- **Layout:** Bulma `container` (1152px at widescreen, 1344px at fullhd); text columns `is-four-fifths`; teaser hero-body has 0 top and 3rem bottom padding.

## Components

- **Hero title block.** Centered `title is-1 publication-title` in Biolinum 400, six authors as linked `author-block`s in Info Sky, then "Visual Media Lab, KAIST" and a line break before "CVPR 2025".
- **Link button.** `external-link button is-normal is-rounded is-dark`: `#363636` pill, white text, Font Awesome / academicons icon in a `span.icon`. Two buttons: Paper (arXiv PDF), Code (GitHub).
- **YouTube teaser.** 16:9 responsive wrapper (`padding-bottom: 56.25%`), 10px radius, iframe absolutely positioned.
- **Overview figures.** Three method images (VAE, denoiser, editing) each followed by a centered subtitle caption "(a) … (b) … (c) …".
- **Video carousel.** `bulma-carousel` with `.item` cards (5px margin, 20px padding, `font-size: 0`), each a caption `<p>` above an autoplay/muted/loop MP4.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Biolinum 400 title, blue author links |
| Venue badge | Text only | "CVPR 2025" on the affiliation line |
| Link buttons | Paper, Code | Dark pills |
| Teaser video | YouTube embed | 10px rounded 16:9 frame |
| Abstract | Yes | `hero is-light` band, justified |
| Method figure | Three-part overview | White band, centered captions |
| Results | 13 MP4s (word swap, prompt refinement, attention re-weighting, mirroring) | Carousel on light band |
| Tables / sliders / 3D / HF demo | No | |
| BibTeX | No | Not present on the page |
| Acknowledgements | No | Footer only |

## Do's and Don'ts

- Do apply the custom font to every Bulma text class, not just `body`, or Bulma will fall back to its system stack.
- Do keep titles at weight 400; the lighter title is the page's signature.
- Do alternate `is-light` and white heroes to pace sections.
- Don't introduce Bulma's turquoise primary; the page never uses it.
- Don't rely on BibTeX being present when cloning this layout; add it if needed.

## Surfaces

White and `#f5f5f5` full-width bands; no cards or shadows. Footer uses Bulma's default footer band.

## Imagery

One YouTube video, three PNG method diagrams, 13 MP4 motion renders in a carousel.

## Layout

Single centered column inside Bulma containers; all content centered except the justified abstract. Carousel shows several items per slide (bulma-carousel defaults).

## Agent Prompt Guide

**Quick colors:** page `#ffffff`, band `#f5f5f5`, text `#4a4a4a`, title `#363636`, buttons `#363636`, author links `hsl(204,86%,53%)`.

1. "Set a Bulma project title in Linux Biolinum at weight 400, 3rem, with author links in `hsl(204, 86%, 53%)` that underline on hover and authors at 1.22rem."
2. "Make dark pill link buttons: Bulma `button is-normal is-rounded is-dark`, `#363636` fill, white Biolinum label with a leading icon."
3. "Build a video carousel item: 5px margin, 20px padding, a short caption paragraph (e.g. 'Word swap (a): inplace → forward') above an autoplaying muted looping MP4."

## Similar Pages

Nerfies-derived pages in this collection, especially WoW-Bench (stock Nerfies fonts) and CoSyn (Nerfies with Crimson Text), which show the same skeleton with a different font swap.

## Quick Start

```css
@import url('https://fonts.cdnfonts.com/css/linux-biolinum');
:root {
  --dark: #363636; --text: #4a4a4a; --band: #f5f5f5; --page: #ffffff;
  --author-link: hsl(204, 86%, 53%);
  --font: 'Linux Biolinum', Arial, sans-serif;
  --fs-body: 1.12rem; --fs-authors: 1.22rem;
  --radius-pill: 290486px; --radius-video: 10px;
}
body, .title, .subtitle, .content, .button, .author-block { font-family: var(--font); }
.title, .subtitle { font-weight: 400; }
```

## Provenance

- **URL:** https://seokhyeonhong.github.io/projects/salad/
- **Paper:** SALAD: Skeleton-aware Latent Diffusion for Text-driven Motion Generation and Editing (arXiv 2503.13836), Seokhyeon Hong et al., Visual Media Lab, KAIST.
- **Venue:** CVPR 2025.
- **Selection reason:** the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit:** footer credits the Academic Project Page Template (eliahuhorwitz), adopted from Nerfies.
- **Measurement method:** `extract_style.py` on static HTML and four CSS files, then manual reading of `index.css` and the HTML to drop unused Bulma palette entries. The rendered page was not viewed, so the Biolinum web font loading from cdnfonts is assumed, not observed. The `hsl()` to hex conversion is mine.
