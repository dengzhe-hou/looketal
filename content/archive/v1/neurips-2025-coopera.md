# COOPERA — Style Reference

> Stock Nerfies with a Spotlight banner and a household-robot storyboard.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9 and the unmodified Nerfies `index.css`) and roles are interpreted from selectors and one rendered look. Bulma's palette (`#00d1b2`, `#ffdd57`, `#3298dc`) appears in frequency counts but not on the page and is excluded. Several template blocks (Poster, a second video carousel, extra buttons) are present only inside HTML comments.

## Overview

COOPERA keeps the Nerfies template nearly verbatim: Google Sans title, Noto Sans body, `#363636` dark pill buttons, `#3273dc` author links, a `#f5f5f5` light band for the abstract. Its one structural edit is a venue line written as an `h2` with `<font size="+2.5">` reading "NeurIPS 2025 (Spotlight)" placed between the title and the authors. Below the buttons, a wide storyboard teaser of simulated household scenes is followed by a bold "TL;DR:" subtitle, an embedded YouTube video, and a series of centered sections with figures and carousels.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page background |
| Bulma Ink | `#363636` | (Bulma `$grey-darker`) | Titles, dark pill buttons |
| Body Graphite | `#4a4a4a` | (Bulma `$grey-dark`) | Body and subtitle text |
| Bulma Link Blue | `#3273dc` | (Bulma `$link`) | Author names |
| Smoke Band | `#f5f5f5` | (Bulma `$white-ter`) | `.hero.is-light` abstract band, `pre` |
| Carousel Dot | `#000000` | — | `.slider-pagination .slider-page` background |
| Footer Icon | `#000` | — | `.footer .icon-link` |

## Tokens — Typography

- **Title family:** Google Sans (Google Fonts `Google Sans|Noto Sans|Castoro`). Substitute: Product Sans, Inter.
- **Body family:** Noto Sans. Substitute: Open Sans.
- **Weights:** 600 Bulma titles, 700 for the bold "TL;DR:" label, 400 body.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`.title.is-1`) | 3rem | 600 | Google Sans, two lines |
| Venue line (`h2 > font size=+2.5`) | about 1.5rem (inferred from render) | 400 | Plain text above authors |
| Section title (`.title.is-3`) | 2rem | 600 | Centered |
| Sub-section (`.title.is-4`) | 1.5rem | 600 | "Simulated Humans", "Human-Robot Collaboration" |
| Authors (`.is-size-5`) | 1.25rem | 400 | Blue links, †/* marks |
| TL;DR subtitle | 1.25rem | 400 + 700 label | Centered |
| Body | 1rem | 400 | Justified abstract |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px (pill) |
| Carousel/video frames | 10px (`.publication-video` iframe `!important`) |
| Bulma controls | 4px |

- **Shadows:** none beyond Bulma focus rings.
- **Section margins:** inline `margin-top: 25px; margin-bottom: 25px` on the light band.
- **Layout width:** `.container.is-max-desktop` (Bulma 960px, inferred); text in `is-four-fifths` columns (8 instances).

## Components

- **Link button:** `.button.is-normal.is-rounded.is-dark`, `#363636`, white label and icon. Rendered: arXiv, Code (Paper and Supplementary markup exists but did not render in the view checked).
- **Venue line:** unstyled `h2` with legacy `<font>` sizing; no chip.
- **TL;DR subtitle:** `h2.subtitle.has-text-centered` with bold label.
- **Video embed:** YouTube iframe, width 100%, height 400px.
- **Carousel:** `bulma-carousel` with black pagination dots.
- **BibTeX:** Bulma `pre` on `#f5f5f5`.

## Page Modules

- **Title/author block:** centered title, venue line, five authors (Oxford / Meta affiliations with †, * marks), equal-advising note.
- **Venue badge:** text "NeurIPS 2025 (Spotlight)".
- **Link buttons:** arXiv, Code.
- **Teaser:** wide storyboard figure of a simulated human, robot, and multi-day timeline.
- **TL;DR** under the teaser.
- **Video:** YouTube embed.
- **Abstract:** `#f5f5f5` light band.
- **Method figures:** Framework Overview, Simulating Humans, Instantiating COOPERA with an Assistive Agent.
- **Results:** Qualitative Results with two sub-carousels (Simulated Humans, Human-Robot Collaboration).
- **BibTeX.**
- **Not present (live):** results tables, image-comparison slider, 3D viewer, HF demo; Poster section is commented out.

## Do's and Don'ts

- Do keep the Nerfies defaults intact if the content is a storyboard-heavy robotics paper.
- Do put the Spotlight designation directly under the title.
- Don't use `<font>` tags for sizing; a `.publication-venue` class does the same job.
- Don't leave template placeholder sections in comments if they reference unrelated videos.
- Don't add accent colors; this style has none.

## Surfaces

White page; one `#f5f5f5` band for the abstract; media carry no borders or shadows.

## Imagery

Simulator screenshots of homes and robots composed into storyboard figures with speech bubbles and timeline labels; YouTube overview video.

## Layout

Centered column; full-width teaser figure; sections stacked with centered `title is-3` headings and four-fifths text columns.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, titles `#363636`, text `#4a4a4a`, links `#3273dc`, band `#f5f5f5`.

1. "Build a Nerfies hero: Google Sans 3rem title, a plain 'NeurIPS 2025 (Spotlight)' line, blue `#3273dc` author links in Noto Sans, and dark pill buttons (`#363636`) for arXiv and Code."
2. "Add a centered TL;DR subtitle (1.25rem, `#4a4a4a`) with a bold 'TL;DR:' label beneath a full-width storyboard image."
3. "Place the abstract in a Bulma `hero is-light` band (`#f5f5f5`) with a centered `title is-3` heading and justified text."

## Similar Pages

PlanarGS, GOATex and EF-3DGS in this batch use the same unmodified Nerfies CSS.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --link: #3273dc;
  --band: #f5f5f5;
  --radius-pill: 290486px;
  --radius-media: 10px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
```

## Provenance

- **URL:** https://dannymcy.github.io/coopera/
- **Paper:** COOPERA: Continual Open-Ended Human-Robot Assistance (arXiv 2510.23495), Chenyang Ma et al., University of Oxford.
- **Venue:** NeurIPS 2025 Spotlight, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 (Spotlight) and links the project page.
- **Template credit:** no footer credit found in static text; the CSS and markup are the Nerfies template (identified from `index.css` rules such as `.publication-awards #ff3860` and class names).
- **Measurement method:** `extract_style.py` counts, manual reading of HTML and `index.css`, one rendered screenshot of the hero. The venue font size is estimated from the render.
