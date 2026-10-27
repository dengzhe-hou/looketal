# PlanarGS — Style Reference

> Minimal Nerfies: one looping indoor fly-through and four dark pills.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9 and the unmodified Nerfies `index.css`) and roles are interpreted from selectors and one rendered look. Bulma's palette (`#00d1b2`, `#ffdd57`, `#3298dc`) appears in frequency counts but not on the page and is excluded.

## Overview

PlanarGS is the shortest page in this batch: hero, teaser video, Abstract, Method, "Comparsion" (sic), BibTeX. It uses the Nerfies template unchanged. The hero shows a three-line Google Sans title, blue author links with superscripts and †/* marks, a small affiliation line (Shanghai Jiao Tong University, Monash University), a contribution note, and a venue line "NeurIPS 2025" set in `is-size-4` through a misspelled class `publication-veneu`, so the template's venue rule does not apply. Four dark pill buttons follow. The teaser is a single autoplaying, muted, looping indoor reconstruction video.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page background |
| Bulma Ink | `#363636` | (Bulma `$grey-darker`) | Title, dark pill buttons |
| Body Graphite | `#4a4a4a` | (Bulma `$grey-dark`) | Body text, venue line |
| Bulma Link Blue | `#3273dc` | (Bulma `$link`) | Author links |
| Smoke | `#f5f5f5` | — | `pre` background, template interpolation panel |
| Card Edge | `#bbb` | — | `.results-carousel .item` border (template rule) |
| Footer Icon | `#000` | — | `.footer .icon-link` |

## Tokens — Typography

- **Title family:** Google Sans. Substitute: Product Sans, Inter.
- **Body family:** Noto Sans. Substitute: Open Sans.
- **Weights:** 600 titles, 400 body.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`.title.is-1`) | 3rem | 600 | Three lines at 800px viewport |
| Venue line (`.is-size-4`) | 1.5rem | 400 | Plain text |
| Authors (`.is-size-5`) | 1.25rem | 400 | Blue links |
| Affiliation / notes | `<sup>`/small text | 400 | — |
| Section title (`.title.is-3`) | 2rem | 600 | Centered |
| Body | 1rem | 400 | Justified |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Carousel items, interpolation panel | 10px |
| Bulma controls | 4px |

- **Shadows:** none.
- **Layout width:** `.container.is-max-desktop` (Bulma 960px, inferred); text in `is-four-fifths` columns.

## Components

- **Link button:** `.button.is-normal.is-rounded.is-dark`, `#363636`, white text, Font Awesome / academicons glyphs. Labels: Paper, arXiv, Code, Video.
- **Teaser video:** `<video id="teaser" autoplay muted loop playsinline controls height="100%">` in `section.hero.teaser`.
- **Section heading:** `h2.title.is-3`, centered.
- **BibTeX:** Bulma `pre` on `#f5f5f5`.

## Page Modules

- **Title/author block:** five authors with superscripts, affiliations, equal-contribution and corresponding-author notes.
- **Venue badge:** plain "NeurIPS 2025" line (`is-size-4`).
- **Link buttons:** Paper, arXiv, Code, Video.
- **Teaser:** looping indoor Gaussian-splat fly-through video.
- **Abstract**, **Method** figure, **Comparison** figures.
- **BibTeX** with OpenReview URL.
- **Footer:** "We thank Nerfies for providing the template."
- **Not present:** results tables, image-comparison slider, interactive viewer, HF demo, acknowledgements section. The template's teaser subtitle ("Nerfies turns selfie videos…") remains only inside an HTML comment.

## Do's and Don'ts

- Do keep the page short when the paper's contribution is visible in one video.
- Do put the venue directly above the buttons.
- Don't misspell class names (`publication-veneu`); styling silently drops.
- Don't add color; the style is grey, white and one link blue.
- Don't leave typos in section headings ("Comparsion").

## Surfaces

Single white surface; no light bands rendered in the hero area.

## Imagery

Indoor scene reconstructions (rooms, furniture planes), one teaser video, static method and comparison figures.

## Layout

Centered column, hero then full-width teaser video, then three short sections.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, text `#4a4a4a`, link `#3273dc`, code bg `#f5f5f5`.

1. "Make a Nerfies hero with a 3rem Google Sans title, Noto Sans author line with `#3273dc` links and superscripts, a 1.5rem 'NeurIPS 2025' line, and four dark pill buttons (Paper, arXiv, Code, Video)."
2. "Add a full-width teaser `<video autoplay muted loop playsinline controls>` directly below the hero, no frame or shadow."
3. "Create three sections (Abstract, Method, Comparison) with centered `title is-3` headings and four-fifths-width text."

## Similar Pages

COOPERA, GOATex and EF-3DGS in this batch (same Nerfies CSS).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --link: #3273dc;
  --code-bg: #f5f5f5;
  --radius-pill: 290486px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL:** https://planargs.github.io/
- **Paper:** PlanarGS: High-Fidelity Indoor 3D Gaussian Splatting Guided by Vision-Language Planar Priors (arXiv 2510.23930), Xirui Jin et al., Shanghai Jiao Tong University / Monash University.
- **Venue:** NeurIPS 2025, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer "We thank Nerfies for providing the template."
- **Measurement method:** `extract_style.py` counts, manual reading of HTML and `index.css`, one rendered screenshot of the hero. The extractor's `interactive_3d` flag was not confirmed by any viewer element in the markup.
