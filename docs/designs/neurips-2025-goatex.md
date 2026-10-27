# GOATex — Style Reference

> A Nerfies gallery wall of 56 captioned texture turntables.

**Theme:** light

Measurements are normalized from static HTML/CSS (Bulma 0.9, unmodified Nerfies `index.css`, and a 139-character inline `<style>` for tabs) and roles are interpreted from selectors and one rendered look. Bulma's palette (`#00d1b2`, `#ffdd57`, `#3298dc`) appears in frequency counts but not on the page and is excluded.

## Overview

GOATex keeps Nerfies chrome (Google Sans title, Noto Sans body, `#3273dc` author links) but turns the body into a dense media gallery: 58 `<video>` elements, most inside `column is-one-third` cells (52 one-third columns) with a fixed-height caption box under each. Captions are the text prompts used to texture each mesh, set very small (0.6rem in 39 places, 0.7rem in 17). A centered Bulma tab strip switches the qualitative video between scenes (House, Bus, …), with the active tab on `#eee` and bold `#333`. The hero has no link buttons at all: title, "NeurIPS 2025", authors, affiliations, then the teaser figure.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | — | Page background |
| Bulma Ink | `#363636` | (Bulma `$grey-darker`) | Titles |
| Body Graphite | `#4a4a4a` | (Bulma `$grey-dark`) | Body text, captions |
| Bulma Link Blue | `#3273dc` | (Bulma `$link`) | Author links |
| Tab Fog | `#eee` | inline style | Active tab background |
| Tab Charcoal | `#333` | inline style | Active tab label |
| Divider Grey | `#ccc` | inline attr | Inline borders between gallery rows (3 uses) |
| Smoke | `#f5f5f5` | — | `.hero.is-light` band, `pre` |
| Card Edge | `#bbb` | — | Template carousel item border |

## Tokens — Typography

- **Title family:** Google Sans. Substitute: Product Sans, Inter.
- **Body family:** Noto Sans. Substitute: Open Sans.
- **Weights:** 600 titles, 700 active tab, 400 body and captions.

| Level | Size | Weight | Notes |
|---|---|---|---|
| Paper title (`h1.title.is-1`) | 3rem | 600 | Single line at desktop |
| Gallery headings (`h1`) | 2rem–2.5rem (inferred) | 600 | "Detailed Views for Teaser Objects", "…Texturing Results" |
| Section title (`.title.is-3`) | 2rem | 600 | Abstract, prompt-conditioning sections |
| Sub-heading (`.title.is-5`) | 1.25rem | 600 | 17 uses |
| Venue line | font-size `x-large` (inline) | 400 | "NeurIPS 2025" |
| Authors | `large` (inline) | 400 | Blue links |
| Video caption | 0.6rem / 0.7rem | 400 | Box height 6em, flex-centered |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Active tab | 4px |
| Carousel items, interpolation panel | 10px |
| Video tiles | 0 (unframed) |

- **Shadows:** none.
- **Caption box:** `height: 6em; display: flex; align-items: center; justify-content: center`.
- **Layout width:** `.container.is-max-desktop` (Bulma 960px, inferred) for text; galleries use `columns is-multiline` with one-third cells.

## Components

- **Captioned video tile:** `column is-one-third` → `<video>` (object-fit cover, 100% width) → `.video-caption` prompt text.
- **Scene tabs:** Bulma `.tabs.is-centered`; JS `changeVideo()` swaps the source; active `#eee` / `#333` / 700 / 4px.
- **Prompt pair block:** "Outer Prompt" / "Inner Prompt" captions under paired renders in the conditioning sections.
- **Section heading:** centered `title is-3`.
- **BibTeX:** Bulma `pre` on `#f5f5f5`.

## Page Modules

- **Title/author block:** four authors (KRAFTON, NC AI, UC Berkeley, Seoul National University), equal-contribution note.
- **Venue badge:** plain text "NeurIPS 2025".
- **Link buttons:** none rendered (no Paper, arXiv or Code buttons in the hero).
- **Teaser:** composite figure of exterior and cut-away interior textures with highlighted prompt phrases.
- **Gallery:** "Detailed Views for Teaser Objects" and "Geometry & Occlusion Aware 3D Mesh Texturing Results" video grids.
- **Abstract.**
- **Method demonstrations:** "Separate Prompt Conditioning for Inner and Outer Surfaces" with three numbered cases (multiple interior styles, exterior prompt removal, interior prompt addition).
- **BibTeX.**
- **Not present:** results tables, comparison slider, HF demo, acknowledgements.

## Do's and Don'ts

- Do give every generated asset its prompt as a caption.
- Do use a uniform caption box height so grids stay aligned.
- Don't drop caption text below 0.7rem if it carries meaning; 0.6rem is hard to read.
- Don't ship without Paper/Code buttons; readers expect them in the hero.
- Don't leave the template `<title>` fragment ("Tab Highlight Example") in the document head.

## Surfaces

White page, unframed media tiles, grey tabs as the only control surface.

## Imagery

Textured 3D meshes (houses, buses, wardrobes, theaters) rendered as rotating videos, often in exterior/interior pairs.

## Layout

Hero, teaser, then long three-column galleries separated by large centered headings and thin `#ccc` dividers.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, text `#4a4a4a`, link `#3273dc`, tab active `#eee`/`#333`, divider `#ccc`.

1. "Build a three-column video gallery (Bulma `columns is-multiline`, `column is-one-third`) where each autoplaying looped video is followed by a 6em-tall centered caption in 0.7rem Noto Sans."
2. "Add centered Bulma tabs that swap a video source; active tab `#eee` background, `#333` bold label, 4px radius."
3. "Make a minimal Nerfies hero with a Google Sans title, an x-large 'NeurIPS 2025' line and blue author links, without buttons."

## Similar Pages

COOPERA, PlanarGS and EF-3DGS (same Nerfies CSS); EF-3DGS also leans on dense video grids.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --title: #363636;
  --text: #4a4a4a;
  --link: #3273dc;
  --tab-active-bg: #eee;
  --tab-active-fg: #333;
  --divider: #ccc;
  --caption-size: 0.7rem;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
.tabs ul li.is-active a { background: var(--tab-active-bg); color: var(--tab-active-fg); font-weight: bold; border-radius: 4px; }
```

## Provenance

- **URL:** https://goatex3d.github.io/
- **Paper:** GOATex: Geometry & Occlusion-Aware Texturing (arXiv 2511.23051), Hyunjin Kim et al.
- **Venue:** NeurIPS 2025, stated on the page and in the arXiv comment.
- **Selection reason:** arXiv comment states acceptance at NeurIPS 2025 and links the project page.
- **Template credit:** footer keeps the Nerfies licence text and links to the Nerfies source repository (`github.com/nerfies/nerfies.github.io`); the extractor did not flag it.
- **Measurement method:** `extract_style.py` counts, manual reading of HTML, inline styles and `index.css`, one rendered screenshot of the hero. Gallery heading sizes are inferred; video playback and tabs were not exercised.
