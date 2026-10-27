# FR3D Viser Gallery — Style Reference

> A Nerfies page that hands the reader a dashboard of point-cloud replays.

**Theme:** light

Values come from the static HTML, its large inline `<style>` block, and the stock Nerfies `index.css` on top of Bulma 0.9. Bulma's full palette (turquoise `#00d1b2`, green `#48c774`, etc.) is in the stylesheet but mostly unused; the table below lists only colors the page applies. Measurements are normalized and roles interpreted.

## Overview

FR3D is the Nerfies/Bulma layout (centered `is-max-desktop` column, Google Sans title, dark rounded link buttons) extended for 3D world-model results. Its signature is the "Interactive Results" block: a row of gray tab buttons (Waymo / KITTI / nuScenes) switching between embedded Viser playback iframes, each in a 0.5em-rounded frame with a soft 1em halo shadow. Below come qualitative image grids in `#fafafa` panels, quantitative figures, acknowledgements and a restyled BibTeX card with a slate copy button. The hero is pushed down with `padding-top: 6rem`, and the venue sits in bold above the authors. A hidden GitHub-Pages notice banner (frosted slate pill fixed to the bottom) is defined but carries the `hidden` attribute.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Bulma Charcoal | `#363636` | Bulma `$grey-darker` | Titles, dark link buttons, tab text |
| Body Gray | `#4a4a4a` | Bulma `$text` | Body text (inferred from Bulma default) |
| Venue Gray | `#555555` | `.publication-venue` | Venue text (Nerfies rule) |
| Author Sky | `hsl(204, 86%, 53%)` | `.publication-authors a` | Author links (≈ `#209cee`, converted) |
| Link Blue | `#3273dc` | Bulma `$link` | Body links |
| Tab Smoke | `#f5f5f5` | (literal) | Inactive dataset tab, image-blend background |
| Tab Hover | `#e4e4e4` | (literal) | Tab hover |
| Tab Pressed | `#d3d3d3` | (literal) | Tab active press |
| Tab Selected | `#cccccc` | (literal) | Selected tab background, text `#000000` |
| Panel Paper | `#fafafa` | `.panel-style` | Qualitative grid panels, 1px `#ccc` border |
| Slate Bib | `#f1f5f9` | `.bibtex-wrapper` | BibTeX card fill, 1px `#d8e1ec` border |
| Bib Ink | `#172033` | `.static-bib` | BibTeX text |
| Copy Slate | `#475569` | `.copy-btn` | Copy button text; hover `#2563eb`, copied `#15803d` |
| Notice Ink | `#0f172a` | `.github-pages-notice` | Hidden notice banner text |
| Notice Blue | `#2563eb` / `#1d4ed8` | (literal) | Notice button and its hover |
| Frame White | `#ffffff` | (literal) | 2px border of the WebGL `#interactive` frame |

## Tokens — Typography

- **Display / authors:** `Google Sans` (Google Fonts link), sans-serif. Substitute: Product Sans, Inter.
- **Body:** `Noto Sans` per Nerfies `index.css`; Bulma falls back to `BlinkMacSystemFont, system-ui` stack. (The Google Fonts link loads only Google Sans; Noto Sans renders only if installed, inferred.)
- **Mono:** `SFMono-Regular, Consolas, "Liberation Mono", Menlo` in BibTeX.
- **Icons:** Font Awesome, Academicons, Tabler Icons outline.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`title is-1`) | 3rem | 600 (Bulma) | Google Sans, centered |
| Venue | `is-size-4` 1.5rem | bold (`<b>`) | "ICML 2026", padding 1.5rem/1rem |
| Authors | `is-size-5` 1.25rem | 400 | |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Dataset h3 | 1.5rem | 600 | |
| Tabs | 16px | 400 | |
| BibTeX heading | 1.75rem (1.5rem ≤700px) | 600 | |
| BibTeX code | 0.92rem (0.78rem ≤700px) | 400 | line-height 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px |
| Viser iframes, model-viewer, video frames | 0.5em |
| Interactive WebGL frame, thumbnails | 6px |
| Dataset tabs | 5px |
| Grid panels | 8px |
| BibTeX card | 16px |
| Copy button | 10px |

- **Shadows:** `0 0 1em 0em rgba(0,0,0,0.15)` halo on iframes and viewers; `0 0 4px #000` on the WebGL frame; copy button `0 1px 2px rgba(15,23,42,0.04)` rising to `0 4px 12px rgba(15,23,42,0.08)`.
- **Layout:** Bulma `container is-max-desktop` (960px); large frames up to 64em; side-by-side iframe column max 640px with a 384px 2x2 image grid; qualitative grids at 80% width with 6 columns and 10px gaps.

## Components

- **Dark pill link button.** Bulma `button is-normal is-rounded is-dark`: `#363636` fill, white text, icon left. Labels: arXiv, ICML Paper.
- **Dataset tab bar.** `nav ul` flex row, 10px gap, buttons stretch equally, min-height 50px, padding 10px 20px, `#f5f5f5` fill, 5px radius; hover scales 1.05 to `#e4e4e4`; selected tab `#cccccc` with black text. ARIA `tablist` / `tab` roles are set.
- **Viser frame.** `iframe` 100% wide, aspect 5/4 (side layout) or 32/18 (large), 0.5em radius, no border, 1em halo shadow.
- **Image grid panel.** `#fafafa`, 1px `#ccc` border, 8px radius, 20px padding; 1x6 or 2x6 CSS grid.
- **BibTeX card.** `#f1f5f9` with 1px `#d8e1ec` border and 16px radius; pre padded 38px 150px 38px 40px to leave room for the white copy button at top-right.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Nerfies centered hero, padding-top 6rem |
| Venue badge | Bold text "ICML 2026" | No chip |
| Link buttons | arXiv, ICML Paper | Dark rounded Bulma buttons; extractor also flags a code link elsewhere on the page |
| Teaser | `hero teaser` section | Figure under the hero |
| Abstract | Yes | Bulma `content has-text-justified` |
| Method figure | "Method Overview" | Centered image |
| Interactive 3D | Yes, 3 Viser playback iframes plus model-viewer scripts | Tabbed by dataset |
| Results | Qualitative grids, quantitative and zero-shot figures, static vs. dynamic | Images, no HTML tables |
| Carousel | Bulma carousel script loaded | |
| BibTeX | Yes | Restyled slate card with copy button |
| Acknowledgements | Yes | Plain section |

## Do's and Don'ts

- Do give every interactive embed the same 0.5em radius and 1em soft halo.
- Do keep tabs neutral gray; the selection state is darker gray, not a color.
- Do keep Bulma's charcoal dark buttons for external links.
- Don't introduce Bulma's turquoise primary; the page never uses it.
- Don't show the GitHub-Pages notice in a reproduction; it ships hidden.

## Surfaces

White page and white footer, `#fafafa` panels for image grids, slate `#f1f5f9` BibTeX card. No dark sections.

## Imagery

Point-cloud replays (Viser), driving-scene image grids from Waymo, KITTI and nuScenes, multiply-blended images on `#f5f5f5`.

## Layout

Single 960px Bulma column; the interactive area breaks wider (up to 64em frames). Side-by-side iframe-plus-grid row uses flex with 1vw gaps and stacks under 768px.

## Agent Prompt Guide

**Quick colors:** text `#4a4a4a`, title `#363636`, tab `#f5f5f5`/`#cccccc`, panel `#fafafa`, bib `#f1f5f9`, link `#3273dc`.

1. "Make a dataset tab bar: equal-width flex buttons with 10px gaps, min-height 50px, `#f5f5f5` fill, `#363636` 16px text, 5px radius; hover `#e4e4e4` and scale 1.05; selected `#cccccc` with black text."
2. "Embed a 3D viewer iframe at 100% width, aspect-ratio 32/18, max 64em, border-radius 0.5em, no border, shadow `0 0 1em 0 rgba(0,0,0,0.15)`."
3. "Build a BibTeX card: `#f1f5f9` fill, 1px `#d8e1ec` border, 16px radius, mono 0.92rem `#172033` text, and a white copy button at top-right with 10px radius and `#475569` 600 text that turns `#2563eb` on hover."

## Similar Pages

CUT3R's project page (credited as a source) and other Nerfies derivatives with embedded Viser viewers; T3-Video and DPLM-2.1 in this collection share the Nerfies base.

## Quick Start

```css
:root {
  --text: #4a4a4a; --title: #363636; --link: #3273dc; --venue: #555555;
  --author: hsl(204, 86%, 53%);
  --tab: #f5f5f5; --tab-hover: #e4e4e4; --tab-active: #cccccc;
  --panel: #fafafa; --panel-line: #cccccc;
  --bib-bg: #f1f5f9; --bib-line: #d8e1ec; --bib-ink: #172033;
  --frame-radius: 0.5em; --frame-shadow: 0 0 1em 0 rgba(0,0,0,0.15);
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", system-ui, sans-serif;
  --container: 960px;
}
```

## Provenance

- **URL:** https://fr3d-wm.github.io/
- **Paper:** Future Dynamic 3D Reconstruction: Toward 3D World Modeling with Disentangled Ego-Motion (arXiv 2606.18250), Nils Morbitzer et al.
- **Venue:** ICML 2026 (shown in bold in the hero).
- **Selection reason:** arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit:** footer says the site "was adapted from CUT3R and Nerfies" (CC BY-SA 4.0).
- **Measurement method:** `extract_style.py` on static HTML and CSS, plus manual reading of the inline style block and `index.css`. Bulma framework colors were excluded unless the markup uses them. Rendered page not viewed; the Viser embeds were not loaded.
