# LangSplatV2 Nerfies Widescreen — Style Reference

> The standard Nerfies handout, widened, with a red "Accepted" line typed in by hand.

**Theme:** light

Values come from Bulma (`bulma.min.css`, plus unused `bulma-carousel` and `bulma-slider`) and the stock Nerfies `static/css/index.css`. The Bulma palette dominates frequency counts; only colors visible in the markup are kept. Roles are interpreted. Rendered output was not viewed.

## Overview

LangSplatV2 (Harvard, UCAS, Tsinghua, JHU, MIT-IBM, UMass) uses the Nerfies template almost unchanged. Two small departures: the hero container is `is-max-widescreen` instead of `is-max-desktop`, and the acceptance note is written with a legacy `<font color="red"><b>Accepted to NeurIPS 2025</b></font>` tag. A centered Bulma navbar offers a "More Research" dropdown linking LangSplat and 4D LangSplat. Four dark rounded buttons follow (arXiv, Video, Code, Hugging Face). The body is a YouTube embed in a 10px-rounded 16:9 frame, a justified abstract, and two results sub-sections built from static figures (several set inline to 70% width), then a BibTeX block. No tables, no carousels, no sliders in use.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page and navbar |
| Bulma Ink | `#363636` | `--text-strong` | Titles |
| Body Graphite | `#4a4a4a` | `--text` | Body text |
| Author Sky | `hsl(204, 86%, 53%)` | `--author-link` | Author links (`!important`) |
| Acceptance Red | `red` (`#ff0000`) | `--venue` | `<font color="red">` acceptance line |
| Button Night | `#363636` | `--btn-dark` | `is-dark` rounded buttons (Bulma dark) |
| Code Mist | `#f5f5f5` | `--surface` | BibTeX `pre` |
| Footer Fog | `#fafafa` | `--footer` | Bulma footer background |
| Bulma Link | `#3273dc` | `--link` | Default links and navbar dropdown hover (Bulma 0.9, inferred) |
| Carousel Border | `#bbbbbb` | (template) | Defined for `.results-carousel .item`, unused here |

## Tokens — Typography

- **Display:** `Google Sans` (title, authors, teaser). Substitute: Product Sans, Inter. Google Fonts usually falls back because the family is not openly served.
- **Body:** `Noto Sans`. Substitute: Open Sans.
- **Mono:** Bulma `monospace`.
- **Weights:** 400 body, 600 Bulma titles, 700 acceptance line (`<b>`).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Authors, affiliations, acceptance (`is-size-5`) | 1.25rem | 400 (700 acceptance) | 1.5 |
| Section h2 (`title is-3`) | 2rem | 600 | 1.125 |
| Sub-section h3 (`title is-4`) | 1.5rem | 600 | 1.125 |
| BibTeX heading (`title`) | 2rem | 600 | 1.125 |
| Body | 1rem | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px |
| YouTube frame (`.publication-video`) | 10px |
| `pre` | 4px |

- **Shadows:** Bulma navbar dropdown shadow only (`0 8px 8px rgba(10,10,10,.1)`, Bulma default, inferred).
- **Layout:** hero `container is-max-widescreen` (1152px at widescreen); body sections `is-max-desktop` (960px); abstract and video in a four-fifths column.
- **Section rhythm:** Bulma `.section` 3rem 1.5rem; figures wrapped in `.hero-body` blocks adding 3rem 1.5rem around each image.

## Components

- **Navbar.** Bulma navbar centered via inline `flex-grow: 1; justify-content: center`, hoverable "More Research" dropdown.
- **Acceptance line.** Third `is-size-5 publication-authors` block, bold red text, no badge.
- **Link buttons.** `external-link button is-normal is-rounded is-dark`: dark pills with Academicons arXiv, Font Awesome YouTube, GitHub, and a `fa-smile` icon standing in for Hugging Face.
- **Video embed.** `.publication-video` 56.25% padding-bottom wrapper, 10px radius, YouTube iframe.
- **Figures.** Centered images at inline `width: 70%` inside `.hero-body`, interleaved with justified paragraphs.
- **BibTeX.** Bulma `pre > code` on `#f5f5f5`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered, Google Sans, superscript affiliations, equal-contribution note |
| Venue badge | Red bold text "Accepted to NeurIPS 2025" | |
| Link buttons | arXiv, Video (YouTube), Code, Hugging Face (paper page) | Dark pills |
| Teaser | YouTube video | 10px rounded frame |
| Abstract | Yes | Justified, four-fifths column |
| Method / results figures | Speed plots and open-vocabulary query visualizations | 70% or full width |
| Tables / sliders / carousel / 3D | No (carousel and slider CSS loaded but unused) | |
| BibTeX | Yes | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep the three stacked `is-size-5` lines (authors, affiliations, acceptance) centered.
- Do round the video frame at 10px to match the template.
- Do use a real HF logo if adapting; the smile icon is a stand-in.
- Don't use the `<font>` tag in new work; set the red with a class.
- Don't mix `is-max-widescreen` and `is-max-desktop` unless the wider hero is intended.

## Surfaces

White page, `#f5f5f5` code, `#fafafa` footer.

## Imagery

Paper figures as PNG (speed charts, dimension comparison, localization and segmentation grids) and one YouTube video.

## Layout

Single centered column. Hero wider (widescreen container) than the body (desktop container).

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, body `#4a4a4a`, author links `hsl(204,86%,53%)`, acceptance `red`, buttons `#363636`, code `#f5f5f5`.

1. "Build a Nerfies hero in a widescreen container: Google Sans 3rem/600 title, 1.25rem author line with blue links, affiliation line, and a bold red 'Accepted to NeurIPS 2025' line."
2. "Add four dark Bulma `is-rounded` buttons with icons: arXiv, Video, Code, Hugging Face."
3. "Embed a YouTube video in a 16:9 wrapper (padding-bottom 56.25%) with 10px radius inside a four-fifths column."

## Similar Pages

Nerfies and its forks, including the authors' own LangSplat and 4D LangSplat pages (linked from the navbar), V2W and KungfuBot in this collection.

## Quick Start

```css
:root {
  --bg: #ffffff; --text-strong: #363636; --text: #4a4a4a;
  --author-link: hsl(204, 86%, 53%); --venue: #ff0000;
  --btn-dark: #363636; --surface: #f5f5f5; --footer: #fafafa;
  --font-display: 'Google Sans', 'Inter', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-pill: 290486px; --radius-video: 10px; --radius-code: 4px;
  --container-hero: 1152px; --container-body: 960px;
}
```

## Provenance

- **URL:** https://langsplat-v2.github.io/
- **Paper:** LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS (arXiv 2507.07136), Wanhua Li et al.
- **Venue:** NeurIPS 2025
- **Selection reason:** arXiv comment states NeurIPS 2025 acceptance and links this page.
- **Template credit:** Nerfies; the footer source thanks the Nerfies authors (part of the footer is commented out, so the visible credit is not confirmed).
- **Measurement method:** static HTML and `index.css` parsed with `extract_style.py`; Bulma defaults filtered by reading markup. The extractor's `interactive_3d` and `carousel` flags are false positives from loaded but unused assets. Not viewed in a browser.
