# LARP Oral Ember — Style Reference

> A Nerfies page with a red Oral stamp and ember-orange key sentences.

**Theme:** light

Values come from the static HTML, the Nerfies `static/css/index.css`, a small inline `<style>` block, and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors the page markup or its CSS uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

LARP keeps the Nerfies skeleton (Google Sans title, Noto Sans body, dark pill buttons, `is-max-desktop` column) and adds a little personality. The title carries two emoji ("Tokenizing Videos 🎬 ... Prior 🚀"). Under the authors, "ICLR 2025 (Oral)" is set bold in pure red with a legacy `<font color="#ff0000">` tag. The "🔥 Highlights" section sits on a flat `#f0f0f0` band and uses three emoji-led bullets (🌟, 🚀, and a third), where the key clause of each is colored ember orange `rgb(241,122,30)`. The method figure uses a red/purple arrow legend (`#CC0000`, `#6600CC`) explained in its caption. Results are a figure for SOTA numbers and two 600px-tall autoplay loops for UCF101 generation and Kinetics-600 prediction. Font Awesome 7 is loaded from cdnjs in addition to the bundled FA build.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Highlight Band | `#f0f0f0` | (inline) | "Highlights" section background |
| Code Mist | `#f5f5f5` | (Bulma) | BibTeX `pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, dark pill buttons |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Oral Red | `#ff0000` | (`<font color>`) | "ICLR 2025 (Oral)" |
| Ember Orange | `rgb(241,122,30)` | (inline) | Key clauses in Highlights |
| Arrow Red | `#CC0000` | (inline) | Caption legend "red" (first round) |
| Arrow Purple | `#6600CC` | (inline) | Caption legend "purple" (second round) |

## Tokens — Typography

- **Display:** Google Sans. Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.
- **Icons:** Font Awesome (bundled plus 7.0.1 CDN), Academicons.

| Role | Size | Weight |
|---|---|---|
| Title (`is-1`) | 3rem; 2rem with line-height 1.2 under 768px (inline style block) | 600 |
| Venue line | inherits author block size, `<b>` | 700 |
| Teaser caption (`h2.subtitle`) | 1.25rem | 400 |
| Section title (`is-3`) | 2rem | 600 |
| Highlights bullets | 20px (inline) | 400, lead phrase bold |
| Body | 1rem | 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link buttons | 290486px radius (pill) |
| Result carousels (template) | 10px radius, 1px `#bbb` border |
| Result videos | `display: block; margin: 0 auto; height: 600px; width: auto` |
| `#compGenTable` rules (no matching element in HTML) | width 100%, collapsed borders, cells padding 1%, bold, centered |
| Container | `is-max-desktop` (960px, Bulma `.container` rule) |

Shadows: Bulma defaults only.

## Components

- **Hero:** emoji title, five authors, affiliation, red bold "ICLR 2025 (Oral)".
- **Link buttons:** Paper (arXiv PDF), arXiv (abs), Code; `is-dark is-rounded` with FA and Academicons glyphs.
- **Teaser:** figure with a justified `h2.subtitle` caption starting "(a) LARP is a video tokenizer...".
- **Video section:** a single player video (`mmist.mp4` with controls).
- **Highlights band:** `#f0f0f0` section, three 20px emoji bullets with orange key clauses.
- **Method figure:** caption with colored arrow words.
- **Visualization:** two autoplay loops, 600px tall.
- **Footer:** "Credits for this awesome template goes to Nerfies website."

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Nerfies hero with emoji title |
| Venue badge | Yes | Red bold text "ICLR 2025 (Oral)" |
| Link buttons | Yes | Paper, arXiv, Code |
| Teaser figure | Yes | Static figure with justified caption |
| Abstract | Yes | Justified |
| Video | Yes | One native video with controls |
| Method figure | Yes | "Method Overview" |
| Results | Yes | "SOTA Results" figure; "UCF101 Class-conditional Generation", "Kinetics-600 Frame Prediction" loops |
| Image comparison slider / 3D / demo | No | Select-box CSS exists (`#selectObject`, `#selectState`) without matching controls in the HTML |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do color only the key clause of each highlight, not the whole bullet.
- Do mark Oral status in the hero in a single strong red.
- Don't use emoji in more than the title and highlight bullets.
- Don't keep `<font>` tags; use a class for the venue color.

## Surfaces

White page with one flat `#f0f0f0` band for Highlights.

## Imagery

Teaser and method figures, one result figure, two tall looping videos, one narrated video.

## Layout

Centered 960px column; `columns is-centered` with `is-four-fifths` and `is-12` columns.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f0f0f0`, title `#363636`, text `#4a4a4a`, oral `#ff0000`, ember `rgb(241,122,30)`, legend `#CC0000` / `#6600CC`.

1. "Create a Highlights section on `#f0f0f0`: 'title is-3' heading with a 🔥, three 20px bullets each starting with an emoji and a bold phrase, the key clause colored `rgb(241,122,30)`."
2. "Under the author list, add a bold venue line 'ICLR 2025 (Oral)' in `#ff0000`."
3. "Show two result loops centered at a fixed 600px height with autoplay, muted, loop and playsinline."

## Similar Pages

Nerfies-derived pages in this collection (SeTok, PIG); the Oral stamp and orange highlight clauses set it apart.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f0f0f0; --title: #363636; --text: #4a4a4a;
  --author-link: hsl(204, 86%, 53%);
  --oral: #ff0000; --ember: rgb(241, 122, 30);
  --legend-1: #CC0000; --legend-2: #6600CC;
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px;
}
```

## Provenance

- **URL:** https://hywang66.github.io/larp/
- **Paper:** LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior (arXiv 2410.21264), Hanyu Wang et al.
- **Venue:** ICLR 2025, marked Oral on the page.
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** Nerfies (footer).
- **Measurement method:** `extract_style.py` plus manual reading of index.css, the inline style block and inline attributes. Rendered page not viewed.
