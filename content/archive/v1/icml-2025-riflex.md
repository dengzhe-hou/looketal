# RIFLEx Highlighter Links — Style Reference

> A video wall annotated with a yellow highlighter pen.

**Theme:** light

Values come from the static HTML, its many inline styles, and a modified Nerfies `index.css` over Bulma 0.9. Bulma's unused palette is excluded. Measurements are normalized; roles are interpreted.

## Overview

RIFLEx is a Nerfies-family page built for showing long videos: 49 autoplaying, muted, looping clips in Bulma carousels and comparison grids. Its typographic signature is the link style: every `<a>` is black with a translucent yellow `rgba(255,211,30,0.4)` band covering the lower 40% of the text, like a highlighter swipe, borrowed from the CausVid / Fate-Zero lineage the footer credits. There are no dark pill buttons; arXiv and Code are plain highlighted text links with icons. The hero is compact: a 50px logo, a `title is-3` set in an `h4`, size-6 authors, then a bold blue TL;DR with the one-line fix in orange Courier. A fixed table-of-contents panel sits at the top-left of the viewport. Body text runs large (1.5rem, line-height 1.8) with key phrases picked out in blue bold.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Highlighter Yellow | `rgba(255,211,30,0.4)` | `a:after` | Underlay band on every link (top 60% to bottom) |
| Link Black | `#000000` | `a` | Link text (overrides Bulma blue) |
| TL;DR Blue | `rgb(25,100,201)` | (inline) | TL;DR sentence, "Motivation:" and other inline emphasis |
| Code Orange | `rgb(248,151,6)` | (inline) | The one-line code formula in Courier |
| Paragraph Black | `#000000` | (inline `color:black`) | Long-form paragraphs |
| Prompt Ink | `#333333` | `.prompt-text` | Prompt caption under videos |
| Prompt Overlay | `rgba(0,0,0,0.7)` | `.results-carousel .item .prompt-text` | Hover caption overlay (hidden by default) |
| TOC Paper | `#f9f9f9` | `#toc` | Fixed TOC panel fill, 1px `#ddd` border |
| Card Rule | `#bbbbbb` | `.results-carousel .item` | 1px carousel item border (Nerfies) |
| Bulma Text | `#4a4a4a` | Bulma `$text` | Default text where not overridden (inferred) |
| Title Charcoal | `#363636` | Bulma `.title` | Title color |

## Tokens — Typography

- **Display:** `Google Sans` for title and authors (Nerfies). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans` (Google Fonts link loads Google Sans and Noto Sans).
- **Code accent:** `'Courier New', Courier, monospace` for the formula `freq[k-1]=(2*np.pi)/(L*s)`.
- **Math:** MathJax 3 (`tex-mml-chtml`) is loaded.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Title (`h4.title.is-3`) | 2rem | 600 | Google Sans, line break before "Video Diffusion Transformers" |
| Authors / affiliations | `is-size-6` 1rem | 400 | Superscript affiliation numbers |
| TL;DR | 20px | bold | Blue, label "TL;DR:" in black |
| Section h2 (`title is-3`) | 2rem | 600 | |
| Sub-section h4 | 1.5rem (Bulma `is-4`, inferred) | 600 | |
| Body paragraphs | 1.5rem | 400 | line-height 1.8, justified |
| Video prompt | 18px | 400 | `#333`, centered |
| TOC | 12px | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Carousel items | 10px (Nerfies) |
| Video embed wrapper | 10px |
| Buttons | none used |
| Images | 0 (inline width 70–90%) |

- **Shadows:** TOC `0 4px 6px rgba(0,0,0,0.1)`; Bulma defaults otherwise.
- **Layout:** Bulma `container is-max-desktop` (960px); comparison rows built with inline flex and 20px or 100px gaps; images at 70% or 90% width.
- **Motion:** the highlighter band transitions its `top` over 200ms with `cubic-bezier(0, 0.8, 0.13, 1)` (a hover growth effect, inferred from the transition).

## Components

- **Highlighter link.** `a { color:#000; position:relative }` plus an `a:after` pseudo-element spanning -0.1em past each side, from 60% height to the baseline, filled `rgba(255,211,30,0.4)`.
- **Text link block.** `span.link-block > a.external-link` with an Academicons or Font Awesome icon and a label (arXiv, Code), separated by `&nbsp;&nbsp;`; no button chrome.
- **TL;DR line.** 20px bold blue sentence with a black "TL;DR:" label and an inline orange Courier code snippet.
- **Video carousel item.** Nerfies results-carousel item (1px `#bbb` border, 10px radius) holding an autoplay loop video with controls and a centered 18px prompt caption below.
- **Fixed TOC.** `#toc` fixed at 10px/10px, 300px wide, `#f9f9f9` with 1px `#ddd` border and soft shadow, 12px text, z-index 9999.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Logo (max 50px), Google Sans title, size-6 authors |
| Venue badge | No | The page does not mention ICML |
| Link buttons | arXiv, Code | Highlighted text links, not buttons |
| Teaser | `hero teaser` video | Autoplay loop |
| TL;DR | Yes | Blue bold with orange code |
| Overview / method | "Overview" with Motivation paragraphs and figures | 1.5rem justified text |
| Results | Training-free 2x temporal extrapolation, fine-tuned extrapolation, spatial and joint extrapolation, comparisons | 49 videos in carousels and flex grids |
| Video embed | One YouTube iframe | Nerfies 16:9 wrapper |
| Tables / sliders / 3D | No | |
| BibTeX | Yes | Nerfies pre block |
| Acknowledgements | No | Footer credits CausVid and Fate/Zero |

## Do's and Don'ts

- Do mark every link with the yellow highlighter band instead of color.
- Do set one TL;DR in blue bold right under the hero, with the key code in orange mono.
- Do let videos autoplay muted and loop, each with its prompt beneath.
- Don't add dark Bulma pill buttons; this page's links are text.
- Don't shrink body text to Bulma's 1rem; the page reads at 1.5rem.

## Surfaces

All white. The only tinted surface is the fixed `#f9f9f9` TOC panel.

## Imagery

Generated long videos (129 to 261 frames at 24 fps per the copy) and a few method figures.

## Layout

Single 960px Bulma column with full-width carousels; comparison sections use inline flex columns with large gaps.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, link `#000000` on `rgba(255,211,30,0.4)`, emphasis `rgb(25,100,201)`, code `rgb(248,151,6)`, caption `#333333`, TOC `#f9f9f9`.

1. "Style all links black with a highlighter underlay: an `:after` pseudo-element from top 60% to bottom, extending 0.1em on each side, filled `rgba(255,211,30,0.4)`, transitioning `top` over 200ms."
2. "Write a TL;DR line at 20px bold in `rgb(25,100,201)` with a black 'TL;DR:' label and an inline Courier New snippet in `rgb(248,151,6)`."
3. "Build a video carousel item with a 1px `#bbb` border and 10px radius containing a muted autoplay loop video and an 18px `#333` centered prompt caption below it."

## Similar Pages

CausVid and Fate/Zero project pages (credited); T3-Video in this collection is another Nerfies-based video-generation page.

## Quick Start

```css
:root {
  --link: #000000; --highlighter: rgba(255,211,30,0.4);
  --emphasis: rgb(25,100,201); --code-accent: rgb(248,151,6);
  --caption: #333333; --toc-bg: #f9f9f9; --toc-line: #dddddd;
  --font-display: "Google Sans", "Inter", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --container: 960px;
}
a { color: var(--link); position: relative; }
a::after { content: ""; position: absolute; top: 60%; left: -0.1em; right: -0.1em; bottom: 0;
  background: var(--highlighter); transition: top 200ms cubic-bezier(0, 0.8, 0.13, 1); }
```

## Provenance

- **URL:** https://riflex-video.github.io/
- **Paper:** RIFLEx: A Free Lunch for Length Extrapolation in Video Diffusion Transformers (arXiv 2502.15894), Min Zhao et al.
- **Venue:** ICML 2025, per the arXiv comment. The page itself shows no venue.
- **Selection reason:** arXiv comment states acceptance at ICML 2025 and links this project page.
- **Template credit:** footer says the template "is borrowed from CausVid and Fate/Zero"; the stylesheet is a modified Nerfies `index.css`.
- **Measurement method:** `extract_style.py` plus manual reading of inline styles and `index.css`; a commented-out "两列对比" section was excluded. Rendered page not viewed; the TOC's position over content and the highlighter hover are inferred from CSS.
