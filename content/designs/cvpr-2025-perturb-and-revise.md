# Perturb-and-Revise Slate Marquee — Style Reference

> A theatre marquee in slate blue, the venue lit in plain yellow, and a gallery of GIF reels underneath.

**Theme:** light

Measurements come from the single inline `<style>` block of the page (no external CSS besides Font Awesome 6.5.1). Hex values are literal declarations, not frequency guesses; roles are interpreted from the markup. Sizes are normalized to rem as written.

## Overview

A hand-built, framework-free page by the first author. Everything sits in a centered column on a pale `#f8f9fa` ground. The only strong colour is the full-width header: a left-to-right slate gradient (`#2c3e50` → `#4a6b8a`) carrying the white title, white author names, light-grey affiliations, a yellow "CVPR 2025" line and two translucent glass buttons. Below the header the page is a sequence of white rounded cards (abstract, GIF boxes, figures) with a soft 2px shadow, separated by section h2s in the same slate. The body is dominated by animated GIF comparisons (19 images, no `<video>`).

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Slate | `#2c3e50` | (literal) | Header gradient start; every h2 |
| Dusk Steel | `#4a6b8a` | (literal) | Header gradient end |
| Marquee Yellow | `yellow` (CSS keyword, `#ffff00`) | `.conference` | Venue line in the header |
| Signal Blue | `#3498db` | (literal) | Author hover; centre of the section-divider gradient |
| Chalk White | `#ffffff` | (literal) | Title, author names, card backgrounds, BibTeX ground |
| Fog Grey | `#e0e0e0` | (literal) | Affiliations on the header |
| Gallery Floor | `#f8f9fa` | (literal) | Page and main-container background |
| Graphite | `#333333` | (literal) | Body text |
| Abstract Ink | `#444444` | (literal) | Abstract paragraph |
| Caption Grey | `#555555` | (literal) | Figure captions |
| Hairline | `#eeeeee` | (literal) | BibTeX border |
| Footer Mist | `#f5f5f5` | (literal) | Attribution banner background (text `grey`) |
| Glass | `rgba(255,255,255,0.15)` / hover `0.25` | (literal) | Header button fill |
| Glass Edge | `rgba(255,255,255,0.3)` | (literal) | Header button border |

## Tokens — Typography

- **Everything:** system stack `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`, set on `*`. No web font is loaded.
- **Mono:** generic `monospace` for BibTeX.
- **Weights:** 500 for venue line and buttons; headings use browser-default bold.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| h1 title (header) | 2.4rem | bold (default) | 1.3 | white, margin-bottom 30px |
| Venue line | 1.3rem | 500 | 1.6 | yellow, letter-spacing 1px |
| Authors | 1.2rem | normal | 1.6 | flex row, gap 20px |
| h2 section | 1.8rem | bold (default) | 1.6 | `#2c3e50`, max-width 80% |
| Body | 1rem (browser default) | 400 | 1.6 | centered by default |
| Abstract | 1rem | 400 | 1.7 | left-aligned |
| BibTeX | 0.9rem mono | 400 | 1.4 | `pre-wrap` |
| Attribution | 0.8rem | 400 | 1.6 | letter-spacing 0.5px |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Abstract card, GIF box, figure images | 8px |
| Buttons, BibTeX block | 5px |

- **Shadows:** cards and figures `0 2px 4px rgba(0,0,0,0.1)`; main container `0 4px 8px rgba(0,0,0,0.1)`.
- **Layout:** sections max-width 1000px; GIF boxes max 800px; figures at 70% width (90% under 768px); BibTeX 80% width capped at 800px.
- **Rhythm:** header padding 40px 20px; 40px between sections; section divider is 2px tall, 80% wide, `margin: 50px auto`.

## Components

- **Marquee header.** Full-bleed `linear-gradient(to right, #2c3e50, #4a6b8a)`, centered, padding 40px 20px, 40px bottom margin.
- **Glass button (`.button`).** Inline-flex, padding 8px 20px, `rgba(255,255,255,0.15)` fill, 1px `rgba(255,255,255,0.3)` border, 5px radius, white 500 text, Font Awesome icon plus `&ensp;` before the label. Hover raises fill to 0.25. Two buttons: Paper (arXiv abs), Code.
- **Abstract card.** White, 25px padding, 8px radius, 2px shadow, left-aligned `#444` text at line-height 1.7.
- **GIF box.** White card, 8px radius, `overflow: hidden`, image full-width; hover lifts it `translateY(-5px)` over 0.3s.
- **Figure section.** Image at 70% width with 8px radius and shadow, caption below in `#555` capped at 70%.
- **Section divider.** 2px bar, `linear-gradient(to right, transparent, #3498db, transparent)`.
- **BibTeX.** White `pre` with 1px `#eee` border, 5px radius, 20px padding.
- **Attribution banner.** `#f5f5f5` band, grey 0.8rem text, 50px padding.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | White on slate gradient, four linked authors with superscript affiliations |
| Venue badge | Yes, as text | Yellow 1.3rem "CVPR 2025" line, not a pill |
| Link buttons | Paper, Code | Glass buttons on the header |
| Teaser | 3D object editing GIF row directly after the abstract | GIF boxes |
| Abstract | Yes | White card |
| Method figure | "Method Overview" and "Parameter Perturbation" | 70%-width figures with captions |
| Results | Object, scene, Objaverse, fashion and real-scene editing | GIF grids (single column) and one still figure |
| Tables / video / sliders / 3D / HF demo | No | |
| BibTeX | Yes | White bordered `pre` |
| Acknowledgements | No | Footer credits only the template |

## Do's and Don'ts

- Do keep the gradient confined to the header; the body stays pale grey and white.
- Do put every visual inside a white 8px card with the same 2px shadow.
- Do use one blue (`#3498db`) only for hover and the divider.
- Don't add more saturated colours; yellow is reserved for the venue.
- Don't set text in a web font; the page relies on the system stack.

## Surfaces

Slate gradient header, `#f8f9fa` page, white cards, `#f5f5f5` footer band. No dark mode.

## Imagery

Animated GIF before/after strips (`assets/split_gifs/comp_partNN.gif`) and four static PNG/JPG figures. No embedded video.

## Layout

Single centered column (1000px max) with text centered by default; the abstract and BibTeX switch to left alignment. Only one breakpoint (768px) widens figures to 90%.

## Agent Prompt Guide

**Quick colors:** header `#2c3e50`→`#4a6b8a`, venue `yellow`, page `#f8f9fa`, card `#ffffff`, text `#333333`, h2 `#2c3e50`, hover `#3498db`.

1. "Build a full-width header with `linear-gradient(to right, #2c3e50, #4a6b8a)`, 40px 20px padding, a 2.4rem white title, white author links that turn `#3498db` on hover, `#e0e0e0` affiliations, and a 1.3rem/500 yellow venue line with 1px tracking."
2. "Make glass buttons: padding 8px 20px, `rgba(255,255,255,0.15)` fill, 1px `rgba(255,255,255,0.3)` border, 5px radius, white 500 text with a leading Font Awesome icon."
3. "Create a GIF card: white, 8px radius, `0 2px 4px rgba(0,0,0,0.1)` shadow, max-width 800px, image fills the card, hover lifts 5px."

## Similar Pages

Other single-file, gradient-header project pages; SALAD (CVPR 2025) in this batch covers the same venue with a Bulma/Nerfies build instead.

## Quick Start

```css
:root {
  --slate: #2c3e50; --steel: #4a6b8a; --venue: yellow; --blue: #3498db;
  --page: #f8f9fa; --card: #ffffff; --text: #333333; --abstract: #444444;
  --caption: #555555; --hair: #eeeeee; --footer: #f5f5f5;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --radius-card: 8px; --radius-btn: 5px;
  --shadow-card: 0 2px 4px rgba(0,0,0,0.1);
  --max: 1000px;
}
header { background: linear-gradient(to right, var(--slate), var(--steel)); color: #fff; }
```

## Provenance

- **URL:** https://susunghong.github.io/Perturb-and-Revise (redirects to the trailing-slash URL)
- **Paper:** Perturb-and-Revise: Flexible 3D Editing with Generative Trajectories (arXiv 2412.05279), Susung Hong, Johanna Karras, Ricardo Martin-Brualla, Ira Kemelmacher-Shlizerman (University of Washington, Google Research).
- **Venue:** CVPR 2025, shown on the page as a yellow text line.
- **Selection reason:** the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit:** the footer says the template was originally made by Susung Hong for this project. No third-party framework.
- **Measurement method:** static HTML fetched with curl and parsed with `extract_style.py`; every value above is read from the inline stylesheet. The rendered page was not viewed. The page's BibTeX cites `arXiv:2408.00760` with year 2024, which does not match the paper's arXiv ID 2412.05279.
