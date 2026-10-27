# ViSAGe Headphone Gallery — Style Reference

> A listening room of square YouTube tiles, headphones on.

**Theme:** light

Values come from the static HTML, the APPT/Nerfies `static/css/index.css`, and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors the page actually uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

ViSAGe keeps the Academic Project Page Template chrome (white hero, Google Sans title, dark pill buttons, grey `hero is-light` bands) and spends its effort on an audio demo gallery. Because the results are spatial (first-order ambisonics) audio, every example is a YouTube embed (44 iframes) so viewers can listen. The embeds sit in four-across `is-one-quarter` columns, each wrapped in a square responsive box (`padding-bottom: 100%`). Each example is captioned with an `h2` "Camera Direction: (elevation, azimuth), Front Left" line. A "Guidelines for Listening Demo Videos" band tells readers to use headphones and explains the coordinate convention in `<code>`. Venue text "ICLR 2025" sits under the lab affiliation.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Listening Band | `#f5f5f5` | (Bulma `hero is-light`) | Abstract band, guideline and gallery bands, `code`/`pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, dark pill buttons |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Bulma Link | `#3273dc` | (Bulma) | Inline links |
| Code Rose | `#da1039` | (Bulma `code` color, in bulma.min.css) | Inline `<code>` for the direction convention |

## Tokens — Typography

- **Display:** Google Sans. Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.

| Role | Size | Weight |
|---|---|---|
| Title (`is-1`) | 3rem | 600 |
| Section title (`is-3`) | 2rem | 600 |
| Gallery group heading (`title is-4`) | 1.5rem | 600 |
| Example caption (`h2` inside column) | Bulma `content h2` 1.75em (inferred) | 600 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Body | 1rem | 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Link buttons | 290486px radius (pill) |
| Video tile | `position: relative; padding-bottom: 100%; height: 0; overflow: hidden` (square) |
| Iframe | `position: absolute; inset 0; width/height 100%` |
| Overview figure columns | flex column, `height: 600px`, image box 80% wide by 500px, `object-fit: contain` |
| Lists | `list-style: disc; padding-left: 1.5em` |

No custom shadows; Bulma defaults only. Container `is-max-desktop` (960px, inferred) for text; gallery uses `columns is-multiline` with `is-one-quarter`.

## Components

- **Hero:** title, three authors, "Vision and Learning Lab, Seoul National University" then "ICLR 2025".
- **Link buttons:** Paper (OpenReview PDF) and Code (GitHub). The arXiv button is commented out in the source with a `<ARXIV PAPER ID>` placeholder.
- **Overview figures:** five half-width columns pairing an image with a short explanatory paragraph.
- **Listening guide:** `hero is-small is-light` band, headphone emoji, convention in `<code>`, two-item disc list.
- **Gallery tile:** `column is-one-quarter has-text-centered`, `h2` direction caption, square YouTube embed.
- **BibTeX:** Bulma `pre`, `booktitle={ICLR}`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Stock APPT |
| Venue badge | Yes | Plain "ICLR 2025" under affiliation |
| Link buttons | Yes | Paper, Code (arXiv hidden) |
| Teaser | Yes | Overview figure with caption |
| Abstract | Yes | `hero is-light` band |
| Method figure | Yes | Overview figure set (dataset, framework, comparison) |
| Results videos | Yes | 44 YouTube embeds in 4-column grids: YT-Ambigen examples, ViSAGe results, moving objects, panoramic baselines |
| Image comparison slider / 3D / demo | No | |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do host audio demos on a player that preserves the audio track, and say "use headphones" before the gallery.
- Do label every clip with its condition (camera direction) as a heading.
- Do keep tiles square and four across so the grid reads as a matrix.
- Don't leave commented placeholder buttons in production markup.

## Surfaces

White hero; alternating `#f5f5f5` small hero bands frame the guideline and gallery groups.

## Imagery

Five static figures in the overview; everything else is embedded video with sound.

## Layout

Text in a 960px column; galleries use Bulma multiline columns at 25% width each.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f5f5f5`, title `#363636`, text `#4a4a4a`, author link `hsl(204,86%,53%)`.

1. "Build a four-across gallery: Bulma `columns is-multiline`, each `column is-one-quarter` holds an h2 caption and a square YouTube iframe wrapper with `padding-bottom: 100%`."
2. "Add a `hero is-small is-light` band titled 'Guidelines for Listening Demo Videos' with a headphones note and a disc list explaining `(elevation, azimuth)`."
3. "Place 'ICLR 2025' as a second line under the lab affiliation in the hero, no badge styling."

## Similar Pages

Audio and video-to-audio project pages built on APPT; in this collection, Sitcom-Crafter shares the template and video-heavy layout.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --title: #363636; --text: #4a4a4a;
  --link: #3273dc; --author-link: hsl(204, 86%, 53%);
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px;
}
.video-container { position: relative; padding-bottom: 100%; height: 0; overflow: hidden; }
.video-container iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
```

## Provenance

- **URL:** https://jaeyeonkim99.github.io/visage/
- **Paper:** ViSAGe: Video-to-Spatial Audio Generation (arXiv 2506.12199), Jaeyeon Kim, Heeseung Yun, Gunhee Kim.
- **Venue:** ICLR 2025 (text under affiliation).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** Academic Project Page Template adopted from Nerfies (footer).
- **Measurement method:** `extract_style.py` plus manual reading of inline styles and section markup. Rendered page not viewed.
