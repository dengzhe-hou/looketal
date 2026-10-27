# RT-Splatting Split Glass — Style Reference

> A Ref-NeRF style wipe gallery where every car window is split down the middle.

**Theme:** light

Values come from the static HTML, the page's `css/index.css` (CamP / Nerfies lineage), and Bulma 0.9 defaults. Bulma's palette inflates the raw counts, so only colors used by the page or its CSS are listed. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

RT-Splatting is built on the CamP project page (itself Nerfies-derived) and its comparison tool comes from Ref-NeRF, as the footer states. The look is the familiar white Bulma page with Google Sans title and dark pill buttons, but the content is an interactive comparison gallery: 24 `video-comparison` pairs, each a hidden `<video>` drawn into a `<canvas>` with a draggable split ("Hover or tap to move the split"). Scenes and baselines are switched with Bulma tabs: plain centered tabs for scene names (compact, hatchback, swab, van, sedan) and `is-toggle is-small` button tabs for "EnvGS vs. Ours", "Ref-GS vs. Ours" and so on. A teaser video in a 16px-radius wrapper opens the page, and the venue line "CVPR 2026 (Highlight)" is a slate `title is-4` under the main title. index.css declares a set of `--dark-*` variables (black, `#1C1C1E`, link `#3274D8`) for a `.scene-pill` selector that the current HTML does not use, so the page has no dark theme.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bulma) | Page background |
| Code Mist | `#f5f5f5` | (Bulma) | BibTeX `pre`, interpolation panel rule |
| Bulma Graphite | `#363636` | (Bulma) | Titles, dark pill buttons, active toggle tab |
| Body Gray | `#4a4a4a` | (Bulma / index.css) | Body text, `.comparison-caption` |
| Venue Slate | `#5a6268` | (inline) | "CVPR 2026 (Highlight)" |
| Author Sky | `hsl(204,86%,53%)` | (index.css) | Author links (about `#209CEE`) |
| Tab Link | `#3273dc` | (Bulma) | Active plain tab underline and text |
| Tab Hairline | `#dbdbdb` | (Bulma) | Tab borders, toggle tab outline |
| Unused Dark Set | `#000` / `#1C1C1E` / `#222` / `#404042` / `#3274D8` / `#fff` / `#eee` | `--dark-bg`, `--dark-bg-light`, `--dark-bg-hover`, `--dark-border`, `--dark-link`, `--dark-text`, `--dark-text-light` | Declared for `.scene-pill`; not used on this page |

## Tokens — Typography

- **Display:** Google Sans (title, authors, venue). Substitute: Product Sans, Inter.
- **Body:** Noto Sans. Substitute: Open Sans.

| Role | Size | Weight |
|---|---|---|
| Title (`is-1`) | 3rem | 600 |
| Venue (`title is-4`) | 1.5rem | 600 |
| Section title (`is-3` / `is-4`) | 2rem / 1.5rem | 600 |
| Authors (`is-size-5`) | 1.25rem | 400 |
| Comparison caption | 1rem, line-height 1.6, max-width 56rem | 400 |
| Hint text ("Interactive visualization...") | 1rem, `is-size-7-mobile` (0.75rem) | 400 |
| Body | 1rem | 400 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Teaser wrapper | 16px radius, overflow hidden, `margin: 1rem auto` |
| Link buttons | 290486px radius (pill) |
| Toggle tabs | Bulma `is-toggle` 4px outer corners, `is-small` 0.75rem |
| Video comparison | `font-size: 0` to remove inline gaps; canvas fills width |
| Comparison caption | `margin: 0 auto 0.9rem` |
| Container | `is-max-desktop`, 960px (Bulma `.container` rule) |

Shadows: Bulma defaults only.

## Components

- **Hero:** title, five authors, `h3.title.is-4` venue in `#5a6268`, pill buttons Paper (arXiv PDF), Code (GitHub), Dataset (Google Drive).
- **Teaser:** autoplay, muted, looping `teaser.mp4` with controls, inside the 16px wrapper, caption container below.
- **Scene tabs:** `.tabs-widget > .tabs.is-centered > ul.is-marginless`, one tab per scene; matching `.tabs-content` children toggled by script.
- **Baseline toggle:** `.tabs.is-centered.is-toggle.is-small` button group above each comparison.
- **Video comparison:** hidden `video.video` (loop, muted, `preload="none"`) plus a `<canvas>` split view with a hover/drag divider.
- **Scene Editing:** same tab widget, each tab an editing operation compared with the original.
- **Citation:** Bulma `pre`.
- **Footer:** credits CamP and Ref-NeRF.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Stock Nerfies hero |
| Venue badge | Yes | Slate `title is-4` "CVPR 2026 (Highlight)" |
| Link buttons | Yes | Paper, Code, Dataset |
| Teaser video | Yes | 16px-radius wrapper |
| Abstract | Yes | Justified |
| Method figure | Yes | Single figure |
| Results videos | Yes | 25 videos in static HTML |
| Image/video comparison slider | Yes | 24 canvas split comparisons (Ref-NeRF tool) |
| Interactive 3D / HF demo | No | |
| BibTeX | Yes | "Citation" section, Bulma pre |
| Acknowledgements | No | |

## Do's and Don'ts

- Do let the comparison tool carry the page; keep chrome stock.
- Do group comparisons by scene with plain tabs and by baseline with small toggle tabs.
- Do lazy-load comparison videos (`preload="none"`).
- Don't leave unused theme variables suggesting a dark mode that does not exist.

## Surfaces

White throughout; no `hero is-light` bands. The media themselves provide contrast.

## Imagery

Rendered driving-scene videos with reflective glass; one static method figure.

## Layout

960px column; comparisons span the column; captions capped at 56rem and centered.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, text `#4a4a4a`, venue `#5a6268`, author link `hsl(204,86%,53%)`, tab `#3273dc`, hairline `#dbdbdb`.

1. "Build a split-view video comparison: a hidden looping muted video drawn to a full-width canvas, with a vertical divider that follows hover or touch; caption below in `#4a4a4a`, line-height 1.6, max 56rem."
2. "Above each comparison add a Bulma `tabs is-centered is-toggle is-small` group with options like 'EnvGS vs. Ours' and 'Ref-GS vs. Ours'."
3. "Put the venue under the title as a Google Sans `title is-4` in `#5a6268`: 'CVPR 2026 (Highlight)'."

## Similar Pages

CamP and Ref-NeRF project pages (named in the footer); within this collection, Reflection Separation also centers on comparison sliders, built differently.

## Quick Start

```css
:root {
  --bg: #ffffff; --title: #363636; --text: #4a4a4a; --venue: #5a6268;
  --author-link: hsl(204, 86%, 53%); --tab: #3273dc; --hairline: #dbdbdb;
  --font-display: "Google Sans", sans-serif; --font-body: "Noto Sans", sans-serif;
  --radius-pill: 290486px; --radius-teaser: 16px;
}
.video-comparison { font-size: 0; }
.comparison-caption { max-width: 56rem; margin: 0 auto 0.9rem; color: var(--text); line-height: 1.6; }
```

## Provenance

- **URL:** https://sjj118.github.io/RT-Splatting/
- **Paper:** RT-Splatting: Joint Reflection-Transmission Modeling with Gaussian Splatting (arXiv 2605.18263), Ji Shi et al.
- **Venue:** CVPR 2026 Highlight (stated on page and in the arXiv comment).
- **Selection reason:** arXiv comment states acceptance at CVPR 2026 (Highlight) and links this page.
- **Template credit:** based on the CamP project page; video comparison tool modified from Ref-NeRF (footer).
- **Measurement method:** `extract_style.py` plus manual reading of css/index.css and markup. The extractor's interactive-3D flag came from the word "Splatting", not a viewer. Rendered page not viewed.
