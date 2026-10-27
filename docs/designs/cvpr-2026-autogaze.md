# AutoGaze Style Reference

> A linen-bound field journal with brass page tabs.

**Theme:** light

Measurements come from the Clarity template stylesheet (assets/stylesheets/main_free.css) as customized by the authors, the page HTML, and computed styles plus one reduced screenshot in a rendered browser tab. Values are normalized to hex; roles are interpreted from where they are applied.

## Overview

AutoGaze is a blog-style long read rather than a Bulma landing page. It runs on Shikun Liu's Clarity template: Figtree throughout at a light 300 weight, warm graphite text (#353535), generous viewport-relative side gutters, and almost no colour. The authors added a warm parchment layer: the header fades from #f1e6d2 to white, key claims sit in a cream highlight box with a brass outline (#fdf4e9 fill, #e1b76e border), and carousel arrows pick up the same brass. Links are black with a hairline underline that thickens and turns walnut (#775223) on hover. Link "buttons" are small uppercase chips on a 5% black wash.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Graphite Smoke | #353535 | (literal) | Body text, headings, chip labels |
| Ink Link | #000000 | --link-brown | Inline links, 0.5px underline |
| Walnut | #775223 | --link-brown-hover | Link hover |
| Parchment | #f1e6d2 | --gradient-start | Header gradient top (to #ffffff) |
| Cream Note | #fdf4e9 | (literal) | Highlight box fill, carousel arrow hover |
| Brass Edge | #e1b76e | (literal) | Highlight box border, carousel arrow border, lightbox close hover |
| Deep Brass | #d4a054 | (literal) | Carousel arrow hover border |
| Chip Wash | rgba(0,0,0,0.05) | (inline) | Link chip background |
| Pebble | #ececec | (literal) | Chip base, inline code, table stripe |
| Paper Grey | #f6f6f6 | (literal) | Section band, gradient fade edges |
| Footer Haze | #fafafa | (literal) | Footer, code blocks |
| Dot Grey | #c6c6c6 | (literal) | Carousel dots, table top rule, code-chip border |
| Caption Grey | #666667 | (literal) | Table headers, inline code text |
| Moss | #47804e | (literal) | Bold accent in template text styles |

The template's original green link (#598864, hover #7baa86) is overridden by the --link-brown variables.

## Tokens · Typography

- **Primary**: Figtree (Google Fonts via @import), weights 300 to 900 loaded.
- **Mono**: Fira Code for code blocks and inline code chips.
- **Highlighting**: highlight.js "foundation" theme for the Quickstart code.

| Role | Size (desktop) | Weight | Notes |
|---|---|---|---|
| Paper title (h1) | 37px measured | 500 | #353535, centred |
| .title (template) | 35px | 500 | widest breakpoint |
| h1 in body | 32px | 700 | line-height 1.2 |
| Section h2 | 18px to 22px | 600 to 700 | measured 18px at about 1,000px wide |
| h3 | 18px | 700 | |
| Body / lists | 18px | 300 | line-height 1.6 |
| Author names | 20px | 300 | black links |
| Link chip | 11.7px | 500 to 600 | uppercase, letter-spacing 1px |
| Table header | 15px | 600 | #666667 |
| Code | 18px Fira Code | 300 | |

Sizes step down at narrower breakpoints (body 13px to 20px across six media queries).

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Highlight box | 16px |
| Link chips, inline code chips | 10px |
| Inline code span | 5px |
| Carousel arrows, dots | 50% |

- **Shadows**: one, on the image lightbox, `0 8px 32px rgba(0,0,0,0.4)`.
- **Layout**: content max-width 1200px; side padding grows with viewport, from 9vw to 27vw (`padding-left: 27vw` at the widest step). Vertical rhythm in vh units (h1 padding 1.75vh, sections 3 to 4vh).

## Components

- **Link chip**: `.button.icon`, background rgba(0,0,0,.05) over #ececec, 10px radius, padding 0.75em 1em, Figtree 0.7em bold uppercase with icon; hover opacity 0.8. Labels: Paper, Code, Models/Data/Benchmark, Demo.
- **Highlight box**: `p.text.highlight-box`, #fdf4e9 fill, 1px #e1b76e border, 16px radius, padding 1em 2em.
- **Flickity carousel**: white 90% arrow buttons, 35px circle, 1px #e1b76e border; hover #fdf4e9 fill and #d4a054 border; grey #c6c6c6 dots.
- **Image comparison**: `img-comparison-slider` web component (CDN), divider and handle set to #000000 or #ffffff by CSS variable.
- **Results table**: Figtree 18px, header 15px/600 #666667, #c6c6c6 2px top rule, alternate rows #ececec.
- **Code block**: Fira Code on #fafafa, padding 1.5vh 1.5vw.
- **Footer**: #fafafa band with Clarity credit.

## Page Modules

- **Title/author block**: three-line centred title, 13 authors with symbol superscripts, affiliations (UC Berkeley, MIT, Clarifai, NVIDIA), equal-contribution notes; header on the parchment gradient.
- **Link chips**: Paper, Code, Models/Data/Benchmark (Hugging Face), Demo.
- **Quickstart**: pip-and-Python code block (unusual for a project page).
- **Teaser video**: autoplay video near the top.
- **Method figure**: Architecture and Training, Training Pipeline.
- **Qualitative results**: gaze visualizations in Flickity carousels (moving patches, OOD videos, camera motion).
- **Image-comparison slider**: img-comparison-slider component.
- **Efficiency results**: "How many patches do we need?", "What speedups do we get?" carousels.
- **Benchmark**: HLVid dataset section and one HTML results table.
- **Math**: MathJax rendering.
- **BibTeX**.

## Do's and Don'ts

- Do keep text at #353535 and weight 300; the softness is the look.
- Do reserve brass (#e1b76e) and cream (#fdf4e9) for emphasis surfaces and carousel controls.
- Do keep links black with a thin underline; walnut only on hover.
- Don't use filled colour buttons; link chips are a 5% black wash with uppercase micro type.
- Don't fix side gutters in px; they scale with the viewport.

## Surfaces

White page, parchment-to-white header gradient, #f6f6f6 bands, #fafafa footer and code, one cream highlight surface.

## Imagery

Video frames with gaze-patch overlays, efficiency plots, architecture diagrams. Images run full container width and open in a lightbox.

## Layout

Single reading column with wide gutters, article-like. Rendered height about 10,000px, the longest in this batch.

## Agent Prompt Guide

Quick colors: text #353535, link #000000 / hover #775223, highlight #fdf4e9 with #e1b76e border, chip rgba(0,0,0,.05), band #f6f6f6, footer #fafafa.

1. "Create a key-finding callout: paragraph in Figtree 18px/300 #353535, background #fdf4e9, 1px solid #e1b76e border, 16px radius, padding 1em 2em, auto horizontal margins."
2. "Build link chips: inline-flex, background rgba(0,0,0,.05), 10px radius, padding .75em 1em, Figtree 0.7em bold uppercase, letter-spacing 1px, #353535, icon left; hover opacity .8."
3. "Style carousel arrows: 35px circles, rgba(255,255,255,.9) fill, 1px #e1b76e border; hover fill #fdf4e9 and border #d4a054."

## Similar Pages

- Clarity template pages by Shikun Liu.
- Long-form, blog-style research pages with a single wide reading column.

## Quick Start

```css
:root {
  --text: #353535;
  --link: #000000;
  --link-hover: #775223;
  --gradient-start: #f1e6d2;
  --gradient-end: #ffffff;
  --highlight-bg: #fdf4e9;
  --highlight-border: #e1b76e;
  --highlight-border-hover: #d4a054;
  --chip-bg: rgba(0, 0, 0, 0.05);
  --band: #f6f6f6;
  --code-bg: #fafafa;
  --rule: #c6c6c6;
  --font-sans: 'Figtree', sans-serif;
  --font-mono: 'Fira Code', monospace;
}
```

## Provenance

- **URL**: https://autogaze.github.io/
- **Paper**: Attend Before Attention: Efficient and Scalable Video Understanding via Autoregressive Gazing (arXiv 2603.12254), Baifeng Shi et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states CVPR 2026 acceptance and links this page.
- **Template credit**: footer reads that the site is built on the Clarity Template designed by Shikun Liu.
- **Measurement method**: extract_style.py on static HTML/CSS, the customized main_free.css read directly, computed styles and one reduced screenshot in a browser tab on 2026-10-27. Responsive sizes come from the stylesheet's media queries; measured values are at about 1,000px viewport.
