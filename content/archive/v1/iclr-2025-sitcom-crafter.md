# Sitcom-Crafter Torus Stage — Style Reference

> A stock-template stage set where three colored toruses name the cast.

**Theme:** light

Values come from the static HTML, the Academic Project Page Template's `static/css/index.css`, and Bulma 0.9 defaults. Bulma's full palette inflates the raw counts, so only colors the page markup or index.css actually uses are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

Sitcom-Crafter uses the Academic Project Page Template (APPT) almost untouched: white hero, Google Sans title, Noto Sans body, dark pill buttons, `hero is-light` grey bands for carousels, and a CC BY-SA footer. Its one bespoke touch is in the teaser caption, which color-codes the three motion types to match the toruses in the teaser video: Human Locomotion in copper `#C36D3E`, Human-Scene Interaction in muted violet `#795DA1`, Human-Human Interaction in slate `#545F6C`. The page is video-heavy (21 `<video>` tags) with two Bulma carousels. The venue is shown as a plain "( ICLR 2025 )" heading under the title.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Carousel Mist | `#f5f5f5` | (Bulma `hero is-light`) | Carousel bands, BibTeX `pre` |
| Bulma Graphite | `#363636` | (Bulma) | Titles, `is-dark` button fill |
| Body Gray | `#4a4a4a` | (Bulma) | Body text |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Bulma Link | `#3273dc` | (Bulma) | Other links |
| Venue Gray | `#555` | (index.css `.publication-venue`) | Defined venue style |
| Award Rose | `#ff3860` | (index.css `.publication-awards`) | Defined award style (unused here) |
| Locomotion Copper | `#C36D3E` | (inline) | Motion-type label 1 |
| Interaction Violet | `#795DA1` | (inline) | Motion-type label 2 |
| Duet Slate | `#545F6C` | (inline) | Motion-type label 3 |
| Pager Black | `#000000` | (index.css) | Carousel pagination dots |

## Tokens — Typography

- **Display:** Google Sans (title, authors, teaser). Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.
- **Mono:** Bulma `monospace` for BibTeX.

| Role | Size | Weight |
|---|---|---|
| Title (`title is-1`) | 3rem | 600 |
| Venue line | Bulma heading inside hero (size not set inline) | 600 |
| Section title (`is-3`) | 2rem | 600 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Affiliations (`is-size-6`) | 1rem | 400 |
| Body / captions | 1rem | 400 |
| Equal-contribution note (`.eql-cntrb`) | smaller | 400 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px (pill) |
| Video embed (`.publication-video`) | 10px |
| Bulma defaults | 4px |

Carousel items use `padding: 20px` and no border (this page's index.css overrides the APPT default 1px `#bbb` border). Shadows are Bulma defaults only. Container `is-max-desktop` (960px, Bulma default, inferred); teaser hero body has `padding-top: 0; padding-bottom: 3rem`.

## Components

- **Hero:** title, "( ICLR 2025 )" line, authors with links, affiliations, three dark pill buttons.
- **Link buttons:** `button is-normal is-rounded is-dark`, icons from Font Awesome and Academicons: Paper (arXiv PDF), arXiv, Code.
- **Teaser:** `hero teaser` with autoplay video and a caption carrying the three colored labels.
- **Results carousel:** `results-carousel` of videos inside `hero is-light` bands, black pagination dots.
- **BibTeX:** `section` with `pre` on `#f5f5f5`.
- **Footer:** APPT credit line plus CC BY-SA 4.0 license.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Stock APPT hero |
| Venue badge | Yes | Plain text heading "( ICLR 2025 )" |
| Link buttons | Yes | Paper, arXiv, Code; dark pills |
| Teaser video | Yes | Autoplay video with color-coded caption |
| Abstract | Yes | `is-four-fifths`, justified |
| Method figure | Yes | "System Overview" |
| Results videos | Yes | "Motion Comparisons", "Long Plot Generations", "Ablations"; 21 videos, 2 carousels |
| Image comparison slider / 3D / demo | No | |
| BibTeX | Yes | Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do tie caption colors to the colors used inside the video (the torus legend).
- Do keep carousels on light grey bands so videos read as a separate layer.
- Don't add new accent colors outside the three motion labels.
- Don't use bordered carousel cards here; this page pads them instead.

## Surfaces

White hero and text sections, `#f5f5f5` `hero is-light` bands for carousels.

## Imagery

Video-first: teaser video plus result clips in carousels and grids. Two still images.

## Layout

Centered 960px column, `columns is-centered` with `is-four-fifths` text.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f5f5f5`, title `#363636`, text `#4a4a4a`, author link `hsl(204,86%,53%)`, labels `#C36D3E` `#795DA1` `#545F6C`.

1. "Write a teaser caption where three category names are bold and colored `#C36D3E`, `#795DA1` and `#545F6C` to match a legend in the video."
2. "Make a Bulma results carousel inside a `hero is-light` band, items padded 20px with no border, black pagination dots."
3. "Add a hero with a 3rem Google Sans title, a centered '( ICLR 2025 )' line, and three dark rounded pill buttons for Paper, arXiv and Code."

## Similar Pages

Any APPT page; in this collection AIF and PR-IQA use the same template.

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --title: #363636; --text: #4a4a4a;
  --link: #3273dc; --author-link: hsl(204, 86%, 53%);
  --label-locomotion: #C36D3E; --label-scene: #795DA1; --label-human: #545F6C;
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px; --radius-video: 10px;
}
```

## Provenance

- **URL:** https://windvchen.github.io/Sitcom-Crafter/
- **Paper:** Sitcom-Crafter: A Plot-Driven Human Motion Generation System in 3D Scenes (arXiv 2410.10790), Jianqi Chen et al.
- **Venue:** ICLR 2025 (shown as "( ICLR 2025 )").
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** Academic Project Page Template (eliahuhorwitz), credited in the footer.
- **Measurement method:** `extract_style.py` plus manual reading of index.css and inline styles. Rendered page not viewed.
