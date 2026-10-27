# AIF Red Venue Plain — Style Reference

> The bare template, four figures, and a venue line printed in red.

**Theme:** light

Values come from the static HTML, the Academic Project Page Template `static/css/index.css`, and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors the page uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

The AIF page is the Academic Project Page Template with almost nothing changed, which makes it a good reference for the template's baseline look. A white hero holds the Google Sans title, four linked authors, and a bold "CVPR 2026" line forced to red with `color: red !important`. Three dark pill buttons follow. The abstract sits in the template's grey `hero is-light` band. Then come four short `section is-small` blocks (Key Idea, Method Overview, Quantitative Results, Visualization), each a centered `title is-3`, one figure, and a justified paragraph. The only CSS addition is `.blend-img-background { mix-blend-mode: multiply }` on the teaser so its white background melts into the page. A StatCounter tracker sits in the footer area.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Abstract Band | `#f5f5f5` | (Bulma `hero is-light`) | Abstract band, BibTeX `pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, `is-dark` buttons |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (APPT index.css) | Author links (about `#209CEE`) |
| Bulma Link | `#3273dc` | (Bulma) | Footer links |
| Venue Red | `red` (`#FF0000`) | (inline, `!important`) | "CVPR 2026" |
| Footer Fog | `#fafafa` | (Bulma `.footer`) | Footer background |

## Tokens — Typography

- **Display:** Google Sans (title, authors). Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.
- **Mono:** Bulma `monospace` for BibTeX.

| Role | Size | Weight |
|---|---|---|
| Title (`is-1`) | 3rem | 600 |
| Venue (`is-size-4`, `<strong>`) | 1.5rem | 700 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Section title (`is-3`) | 2rem | 600 |
| Body | 1rem | 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link buttons | 290486px radius (pill) |
| Bulma controls | 4px radius |
| Section rhythm | `section is-small` (Bulma 3rem 1.5rem padding) |
| Footer | `padding: 3rem 1.5rem 6rem` (Bulma) |
| Container | `is-max-desktop`, 960px (Bulma `.container` rule) |

Shadows: none beyond Bulma defaults.

## Components

- **Hero:** title, authors, `strong` venue in red at `is-size-4`.
- **Link buttons:** `button is-normal is-rounded is-dark`: Paper (arXiv PDF), arXiv (abs, Academicons), Code (GitHub, Font Awesome).
- **Abstract band:** `section hero is-light`, `is-four-fifths` column, justified text.
- **Figure section:** `section is-small`, centered `title is-3`, `center-image` figure, `.level-set has-text-justified` paragraph.
- **BibTeX:** Bulma `pre`, `booktitle={CVPR}`.
- **Footer:** APPT credit, CC BY-SA 4.0 notice, StatCounter image.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Stock APPT |
| Venue badge | Yes | Bold red "CVPR 2026" text |
| Link buttons | Yes | Paper, arXiv, Code |
| Teaser figure | Yes | "Key Idea" figure with multiply blend |
| Abstract | Yes | Grey band |
| Method figure | Yes | "Method Overview" pipeline image |
| Results | Yes | "Quantitative Results" as an image (`vqa.png`); "Visualization" figure |
| Image comparison slider / 3D / demo | No | |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do use `mix-blend-mode: multiply` on white-background figures that sit on white.
- Do keep each result section to one figure and one paragraph.
- Don't stack more accent colors; the red venue is the only one.
- Don't rely on `!important` inline colors if you also theme the page.

## Surfaces

White hero and sections, one `#f5f5f5` abstract band, `#fafafa` footer.

## Imagery

Four static PNGs (teaser, pipeline, VQA results, visualization) plus a tracker image.

## Layout

One centered 960px column with `is-four-fifths` text width.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f5f5f5`, title `#363636`, text `#4a4a4a`, author link `hsl(204,86%,53%)`, venue `#FF0000`, footer `#fafafa`.

1. "Make an APPT hero: 3rem Google Sans title, authors at 1.25rem in `hsl(204,86%,53%)`, then a bold 1.5rem 'CVPR 2026' line in red, then three dark pill buttons."
2. "Create a `section is-small` with a centered 2rem title, a centered figure using `mix-blend-mode: multiply`, and a justified paragraph below."
3. "Place the abstract in a `hero is-light` band (`#f5f5f5`) inside a four-fifths column."

## Similar Pages

Sitcom-Crafter and Atlas Gaussians in this collection use the same template with small additions.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --footer: #fafafa;
  --title: #363636; --text: #4a4a4a; --link: #3273dc;
  --author-link: hsl(204, 86%, 53%); --venue: #FF0000;
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px; --column: 960px;
}
.blend-img-background { mix-blend-mode: multiply; }
```

## Provenance

- **URL:** https://cxliu0.github.io/AIF/
- **Paper:** Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow (arXiv 2604.15809), Chengxin Liu et al.
- **Venue:** CVPR 2026 (red text in hero).
- **Selection reason:** arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit:** Academic Project Page Template (eliahuhorwitz), credited in the footer.
- **Measurement method:** `extract_style.py` plus manual reading of index.css additions and inline styles. Rendered page not viewed.
