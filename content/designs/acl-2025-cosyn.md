# CoSyn Crimson Specimen Book — Style Reference

> A type-specimen book of synthetic documents: Crimson Text at 22px, carousels of charts, menus and business cards waiting to be enlarged.

**Theme:** light

Measurements come from `static/css/index.css` (the Nerfies stylesheet with the font swapped and an image-modal block added), two small inline `<style>` blocks and inline styles, over Bulma 0.9. Bulma's default palette inflates the extractor counts; only the neutrals and the author-link blue below are used. Roles are interpreted.

## Overview

A Nerfies skeleton where `body`, `.teaser`, `.publication-title` and `.publication-authors` are all set in **Crimson Text** at a large 22px base, so the page reads like a book even though the layout is Bulma. The hero lists eleven authors in Nerfies' info blue, two affiliations, two contact e-mails, and five dark pill buttons (Paper, arXiv, Code, CoSyn-400K, CoSyn-Point; a sixth "Tweet" button is commented out). A full-width autoplay teaser video follows, then sections titled as claims ("CoSyn can Generate Diverse Text-rich Images", "Model Trained on CoSyn-400K Achieves SOTA Performance"). Synthetic-image categories are shown in `bulma-carousel` strips of 200px-tall images with captions; clicking any `.zoomable` image opens a black 80% overlay modal. Benchmark results appear as figures with right-aligned medium-size bracketed notes. There is no venue label on the page.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Bulma Charcoal | `#363636` | Bulma `$dark` / strong | Pill buttons, titles |
| Body Graphite | `#4a4a4a` | Bulma `$text` | Paragraphs |
| Info Sky | `hsl(204, 86%, 53%)` (≈ `#209cee`, inferred conversion) | `.publication-authors a` | Author links |
| Paper | `#ffffff` | Bulma body | Page and all sections |
| Panel Grey | `#f5f5f5` | `.interpolation-panel` | Defined panel fill (template leftover) |
| Item Edge | `#bbbbbb` | `.results-carousel .item` | Defined 1px carousel-item border |
| Modal Scrim | `rgba(0,0,0,0.8)` | `.modal` | Image-zoom overlay |
| Modal Close | `#ffffff` | `.close` | 30px bold close glyph |
| Footer Ink | `#000000` | `.footer .icon-link` | 25px footer icons |
| Venue Grey | `#555555` | `.publication-venue` | Defined, unused |
| Award Rose | `#ff3860` | `.publication-awards` | Defined, unused |
| Footer Band | `#fafafa` | Bulma `.footer` default (inferred) | Footer background |

## Tokens — Typography

- **All text:** `'Crimson Text', sans-serif` (Google Fonts link `Google Sans|Noto Sans|Castoro|Crimson Text`). Substitute: Crimson Pro, EB Garamond. Note the generic fallback is `sans-serif`, so a failed load drops to a sans face.
- **Mono:** Bulma `monospace`; BibTeX `pre` at 16px inline.
- **Base:** `body { font-size: 22px }`; Bulma rem sizes stay relative to the 16px root, so titles are not scaled up with it.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title (`title is-1`) | 3rem | 600 | 1.125 | Crimson Text |
| Section title (`title is-3`) | 2rem | 600 | 1.125 | claim-style headings |
| Authors / emails (`is-size-5`) | 1.25rem | 400 | 1.5 | |
| Body | 22px | 400 | 1.5 | justified abstract |
| Result note (`subtitle`) | `medium` keyword (inline) | 400 | 1.25 | right-aligned, bracketed |
| Carousel caption | inherit | 400 | 2em on second line | 4em-tall box for two-line captions |
| BibTeX | 16px mono | 400 | | inline style |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px |
| Video wrapper, carousel item, interpolation panel | 10px |
| Interpolation images | 5px |
| Bulma controls | 4px |

- **Shadows:** none beyond Bulma focus rings.
- **Layout:** Bulma containers; content in `column is-five-fifths` (full width) and `column is-four-fifths` for prose; hero `padding-bottom: 0`; demo section `padding-top: 0`; carousel images `height: 200px; width: auto; object-fit: contain`; logo class 80px tall.

## Components

- **Book-face hero.** Crimson Text title, eleven linked authors with `*` and numeric superscripts, affiliation line, a line of two `mailto:` e-mail links.
- **Pill button.** `external-link button is-normal is-rounded is-dark`, `#363636`, white label with icon; five buttons covering paper PDF, arXiv, GitHub code and two Hugging Face datasets.
- **Teaser video.** Autoplay, loop, muted, playsinline MP4 at 100% width directly under the hero, with a one-line caption.
- **Image carousel strip.** `bulma-carousel` of `.item-1.image-container` cards: caption above, 200px-tall `.zoomable` image; repeated per category (charts, documents, and more).
- **Zoom modal.** Fixed full-screen flex overlay `rgba(0,0,0,0.8)`, image at 80% max, white 30px close mark top-right; image hover transition 0.2s.
- **Result figure with note.** Benchmark chart followed by a right-aligned `subtitle` in `font-size: medium` explaining the metric in brackets.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Crimson Text, with contact e-mails |
| Venue badge | No | Page shows no venue; BibTeX is an arXiv `@article` |
| Link buttons | Paper, arXiv, Code, CoSyn-400K, CoSyn-Point | Dark pills |
| Teaser video | Yes | Autoplay MP4 |
| Abstract | Yes | White section |
| Method figure | "Code Guided Synthetic Data Generation" | |
| Results | Benchmark figures with notes; pointing-data results with a second video | |
| Carousels | Three image carousels with zoom | |
| Tables / sliders / 3D / HF Space | No (the extractor's 3D flag is a false positive from template class names) | |
| BibTeX | Yes | 16px `pre` |
| Footer | Icon links and a credit to the Nerfies repository; icons from flaticon | |

## Do's and Don'ts

- Do set the body font once and repeat it on `.publication-title` and `.publication-authors`, which Bulma otherwise overrides.
- Do give carousel images a fixed height with `object-fit: contain` so mixed document shapes line up.
- Do offer click-to-zoom for dense text-rich images.
- Don't rely on the `sans-serif` fallback after a serif face; use `serif` as the fallback.
- Don't omit the venue if the paper is accepted; this page never mentions ACL 2025.

## Surfaces

All-white sections (no `is-light` bands), Bulma default footer, black modal scrim.

## Imagery

33 images: synthetic charts, documents, diagrams and tables in carousels, benchmark charts, method figure; four videos including the teaser and pointing demo.

## Layout

Centered Bulma column stack; carousels run full container width; result notes right-aligned under figures.

## Agent Prompt Guide

**Quick colors:** page `#ffffff`, text `#4a4a4a`, title/buttons `#363636`, author links `hsl(204,86%,53%)`, modal `rgba(0,0,0,0.8)`.

1. "Set a Bulma project page in Crimson Text: `body { font-size: 22px }`, title and authors in Crimson Text, author links in `hsl(204, 86%, 53%)`, five dark rounded `is-dark` pill buttons."
2. "Build an image carousel strip: each item a caption above a 200px-tall `object-fit: contain` image with class `zoomable`; clicking opens a fixed `rgba(0,0,0,0.8)` overlay showing the image at up to 80% with a white 30px close mark."
3. "Under a benchmark chart, add a right-aligned bracketed note in `font-size: medium` explaining the metric and evaluation setting."

## Similar Pages

SALAD (CVPR 2025, Linux Biolinum) and WoW-Bench (ACL 2026 Findings, stock fonts) in this collection are the same Nerfies skeleton with different type.

## Quick Start

```css
:root {
  --dark: #363636; --text: #4a4a4a; --page: #ffffff;
  --author-link: hsl(204, 86%, 53%); --scrim: rgba(0, 0, 0, 0.8);
  --font: 'Crimson Text', Georgia, serif;
  --fs-body: 22px; --radius-pill: 290486px; --radius-item: 10px;
}
body, .teaser, .publication-title, .publication-authors { font-family: var(--font); }
body { font-size: var(--fs-body); }
.carousel img { height: 200px; width: auto; object-fit: contain; }
```

## Provenance

- **URL:** https://yueyang.ai/cosyn/ (yueyang1996.github.io/cosyn redirects here)
- **Paper:** Scaling Text-Rich Image Understanding via Code-Guided Synthetic Multimodal Data Generation (arXiv 2502.14846), Yue Yang, Ajay Patel et al. (University of Pennsylvania, Allen Institute for AI).
- **Venue:** ACL 2025, per the arXiv comment; the page itself shows no venue.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and links the project page.
- **Template credit:** footer says the site was developed by referencing the Nerfies repository; icons from flaticon.com.
- **Measurement method:** `extract_style.py`, then manual reading of `index.css`, inline styles and the HTML. The Quick Start fallback `Georgia, serif` is my recommendation; the page itself falls back to `sans-serif`. The rendered page was not viewed.
