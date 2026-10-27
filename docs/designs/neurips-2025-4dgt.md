# 4DGT Jost Jumbotron — Style Reference

> A geometric-sans cover card in pale sea-glass gray, two-tone title, black buttons.

**Theme:** light

Values come from a locally modified `css/bootstrap-4.4.1.css` (the authors edited several Bootstrap defaults and left the originals in comments), an inline `<style>` block, and inline `style` attributes on the title, venue and citation. Jost is loaded from Google Fonts; KaTeX is loaded for math. Roles are interpreted. Rendered output was not viewed.

## Overview

4DGT (Meta Reality Labs and Zhejiang University) uses the ZJU3DV "longvolcap" template by Zhen Xu, built on a customized Bootstrap 4.4.1. Everything is set in Jost at weight 500 and 1.25em base size. The cover is a Bootstrap jumbotron recolored to `#ebf0f1`, holding a three-line h1: a gray `#6c6c6c` 800-weight "4DGT", then "Learning a" plus a copper `#c68b5b` phrase, then "Using" plus a steel-blue `#6589bf` phrase. A bold `#5a6268` h4 reads "NeurIPS 2025 (Spotlight)", followed by a hairline, author links, and near-black `#090f15` buttons with light text (arXiv, Code, 🤗 Demo Coming Soon). Below, gray-blue `#8899a5` bold captions introduce a full-width teaser video (radius 1.1em, enlarges 1.25× on hover) and a Bootstrap carousel of result videos with round translucent black controls. Each later section is a left-aligned h3 with an `hr` directly beneath, and "Click to Expand" primary buttons reveal more result grids. The citation sits in a 20px-rounded `#e9eeef` block.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#fff` | `--bg` | Page background (Bootstrap body) |
| Sea-glass Card | `#ebf0f1` | `--cover` | Jumbotron cover (Bootstrap default `#e9ecef` replaced) |
| Bootstrap Ink | `#212529` | `--text` | Body text |
| Ash Mark | `#6c6c6c` | `--mark` | "4DGT" name in the title |
| Copper Phrase | `#c68b5b` | `--title-a` | First highlighted title phrase |
| Steel Phrase | `#6589bf` | `--title-b` | Second highlighted title phrase |
| Venue Slate | `#5a6268` | `--venue` | "NeurIPS 2025 (Spotlight)" |
| Caption Mist | `#8899a5` | `--caption` | Bold teaser and carousel captions |
| Night Button | `#090f15` | `--btn` | `btn-light` link buttons (recolored) |
| Button Text | `#e2e2e2` | `--btn-text` | Button label |
| Button Hover | `#bec3c7` | `--btn-hover` | Hover fill (text turns `#212529`) |
| Bootstrap Blue | `#007bff` | `--link` | Links, "Click to Expand" primary buttons |
| Citation Panel | `#e9eeef` | `--code` | BibTeX `pre` |
| Hairline | `rgba(0,0,0,.1)` | `--line` | `hr` under section headings |
| Control Shade | `rgba(0,0,0,.5)` | `--overlay` | Carousel arrows and dots |

## Tokens — Typography

- **Family:** `Jost` (Google Fonts 300–900) for everything; the modified Bootstrap base names Source Sans Pro, overridden by the inline `body` rule.
- **Mono:** Bootstrap `code` stack, `white-space: pre-wrap`.
- **Math:** KaTeX 0.13.18.
- **Weights:** 500 body, `bolder` headings, 800 for the "4DGT" mark and `bold` venue.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Body | 1.25em | 500 | Jost |
| h1 (cover) | inline 2.0em | bold | three lines with `<br>` |
| "4DGT" mark | 1.4em of h1 | 800 | `#6c6c6c` |
| h4 venue | Bootstrap h4 (1.5rem) relative to 1.25em body (inferred) | bold | `#5a6268` |
| h3 section | 1.5em | bolder | left-aligned, `hr` below |
| h5 results header | Bootstrap h5 | bolder | 30px bottom padding |
| Citation | 0.75em | 500 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Citation `pre` | 20px |
| Teaser video | 1.1em |
| Videos, iframes, comparison canvas | 10px |
| Indicator dots | 10px (15px dots) |
| Buttons (`.btn`) | 0.5rem (modified from Bootstrap .25rem) |
| Jumbotron | 0.3rem |
| Carousel arrows | 50% (50px circles) |

- **Shadows:** none.
- **Layout:** Bootstrap `.container` (1140px at xl, inferred from Bootstrap 4 defaults); `.sm-gutters` rows with 5px padding around each video column; aspect-ratio helper classes (16:9, 4:3, 1:1, 3:2 and several custom ratios).
- **Rhythm:** h3 sections gain 30px top padding; results sections 30px bottom padding.

## Components

- **Cover jumbotron.** `#ebf0f1`, centered, 0.3rem radius, title, venue, `hr`, authors, buttons.
- **Two-tone title.** Plain text interleaved with two colored phrases (copper and steel) that name the method and the data.
- **Link buttons.** `btn btn-large btn-light` recolored to `#090f15` with `#e2e2e2` text, 1.5rem side padding, 0.5rem radius; hover `#bec3c7`.
- **Teaser.** Autoplay video at 16:9 with `zoom-element` (scale 1.25 on hover, 0.2s).
- **Carousel.** Bootstrap carousel; 50px round `rgba(0,0,0,.5)` prev/next controls 25px from the edges; 15px dot indicators placed bottom-right.
- **Expand sections.** h5 with a blue `btn-primary` "Click to Expand" toggling a Bootstrap collapse of more video grids.
- **Citation block.** `#e9eeef`, 1.5em padding, 20px radius, 0.75em text.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Jumbotron cover, two-tone title |
| Venue badge | Bold slate h4 "NeurIPS 2025 (Spotlight)" | |
| Link buttons | arXiv, Code, 🤗 Demo (Coming Soon) | Near-black buttons |
| Teaser | Full-width zooming video | |
| Abstract | Justified paragraph in cover (inferred from `text-align: justify` blocks) | |
| Method figure | Pipeline JPG under h3 + hr | |
| Results videos | Carousel and collapsible grids (ADT, HOT3D, Nymeria) | |
| Comparisons | "Baseline Comparisons & Ablations" with comparison canvases | 10px radius |
| Math | KaTeX | |
| HF demo | Button only, marked coming soon | |
| BibTeX | "Citation" block | |
| Acknowledgements | Footer thanks (template author, discussion, Project Aria) | |

## Do's and Don'ts

- Do color exactly two title phrases, one warm and one cool.
- Do keep every section heading left-aligned with an `hr` directly under it.
- Do round videos at 10px and the teaser slightly more.
- Don't use Bootstrap's stock light button; this template inverts it to near-black.
- Don't add shadows; the page relies on the gray cover and rounded media.

## Surfaces

White page, sea-glass `#ebf0f1` cover, `#e9eeef` citation panel.

## Imagery

Egocentric and multi-view reconstruction videos (Aria datasets) in 16:9, comparison canvases, one pipeline diagram.

## Layout

Bootstrap container with 12-column rows; video grids use `col-md-4`, `col-md-6` or `col-md-12` with 5px gutters.

## Agent Prompt Guide

**Quick colors:** bg `#fff`, cover `#ebf0f1`, text `#212529`, mark `#6c6c6c`, copper `#c68b5b`, steel `#6589bf`, venue `#5a6268`, caption `#8899a5`, button `#090f15`, code `#e9eeef`.

1. "Create a centered cover card `#ebf0f1` with 0.3rem radius: a Jost h1 with a gray 800-weight project name, then two lines where one phrase is `#c68b5b` and another `#6589bf`, and a bold `#5a6268` 'NeurIPS 2025 (Spotlight)' line."
2. "Make link buttons `#090f15` with `#e2e2e2` text, 0.5rem radius, 1.5rem horizontal padding; hover fill `#bec3c7` with `#212529` text."
3. "Add a section heading: left-aligned Jost h3 at 1.5em bolder, an `hr` with zero top margin, then a full-width 10px-rounded video."

## Similar Pages

ZJU3DV project pages built from the same longvolcap template (e.g. Zhen Xu's EasyVolcap and LongVolCap pages).

## Quick Start

```css
:root {
  --bg: #ffffff; --cover: #ebf0f1; --text: #212529;
  --mark: #6c6c6c; --title-a: #c68b5b; --title-b: #6589bf;
  --venue: #5a6268; --caption: #8899a5;
  --btn: #090f15; --btn-text: #e2e2e2; --btn-hover: #bec3c7;
  --link: #007bff; --code: #e9eeef;
  --font: 'Jost', Helvetica, Arial, sans-serif;
  --radius-media: 10px; --radius-code: 20px; --radius-btn: 0.5rem;
}
body { font-family: var(--font); font-weight: 500; font-size: 1.25em; }
```

## Provenance

- **URL:** https://4dgt.github.io/
- **Paper:** 4DGT: Learning a 4D Gaussian Transformer Using Real-World Monocular Videos (arXiv 2506.08015), Zhen Xu et al., Meta Reality Labs and Zhejiang University.
- **Venue:** NeurIPS 2025 Spotlight
- **Selection reason:** arXiv comment states NeurIPS 2025 (Spotlight) acceptance and links this page.
- **Template credit:** footer thanks Zhen Xu for the template, linked to `zju3dv/zju3dv.github.io/tree/master/longvolcap`; built on a locally modified Bootstrap 4.4.1.
- **Measurement method:** static HTML (inline styles and style block), the modified Bootstrap file fetched and searched for edited rules, and `extract_style.py` frequencies. Not viewed in a browser; container width and h4 size are inferred from Bootstrap defaults.
