# Surfboard Zoom Bench — Style Reference

> A side-by-side test bench where every result has a magnifier and a slider.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A Nerfies clone (with DC2 credited too) built for close visual inspection. Results use twentytwenty before/after sliders, a jQuery magnifier with a 130px lens, a three-column grid, and a gigapixel image section. Fixed inline widths of 300px and 467px size the comparison panes, so the layout is tuned for desktop. Small gray tab buttons (#f1f1f1, 8px radius, hover/active #666 with white text) switch between scenes. A surfer emoji prefixes the title, the venue sits as an `h2` "ICLR 2026", and the link row is the full set: Paper, arXiv, Video, Code, Data.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page and section background |
| Whitesmoke Well | `#f5f5f5` | `--bg-well` | Bulma `pre` (BibTeX) and `hero is-light` fill |
| Graphite Heading | `#363636` | `--text-strong` | Bulma `.title` color; also the `is-dark` button fill |
| Body Slate | `#4a4a4a` | `--text` | Bulma body copy |
| Byline Gray | `#555555` | `--venue` | `.publication-venue` (bold) |
| Author Sky | `#3298dc` | `--author-link` | `.publication-authors a`, written as hsl(204, 86%, 53%) |
| Bulma Link Blue | `#3273dc` | `--link` | Default anchor color in body text |
| Hairline Gray | `#dbdbdb` | `--border` | Bulma input and table borders |
| Carousel Rim | `#bbbbbb` | `--frame` | 1px border on `.results-carousel .item` |
| Tab Fog | `#f1f1f1` | `--tab` | `.btn` scene-switch button fill |
| Tab Iron | `#666666` | `--tab-active` | `.btn:hover` and `.active` fill with white text |

No brand accent beyond Bulma defaults; the page's own colors are only the two tab grays.

## Tokens — Typography

**Families.** Google Sans for title and authors, Noto Sans for body (stock Nerfies). Tab buttons 18px. Substitutes: Inter.

| Role | Size | Weight | Family |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem (48px) | 600 | Google Sans |
| Paper title (`title is-2`) | 2.5rem (40px) | 600 | Google Sans |
| Section heading (`title is-3`) | 2rem (32px) | 600 | Noto Sans |
| Sub-heading (`title is-4`) | 1.5rem (24px) | 600 | Noto Sans |
| Author line (`is-size-5`) | 1.25rem (20px) | 400 | Google Sans |
| Body / abstract | 1rem (16px), line-height 1.5 | 400 | Noto Sans |
| Button label | 1rem | 400 | Noto Sans |
| BibTeX | .875em | 400 | monospace |
| Scene tab button | 18px | 400 | Noto Sans |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |
| --radius-tab | 8px | scene tab buttons |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred). Comparison panes are fixed at 300px or 467px with 20px right margins; label rows use manual right margins of 335-360px (inferred desktop-only).

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, arXiv, Video, Code, Data.
- **Scene tab button.** `.btn`: no border, padding 10px 16px, #f1f1f1, 18px, radius 8px; hover/active #666 with white text.
- **Before/after slider.** twentytwenty container, default white handle.
- **Magnifier.** `jquery.magnify` with `.magnify-lens` 130px x 130px.
- **Three-up grid.** `.grid-container` CSS grid, 3 equal columns, 10px gap.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and credit to nerfies and DC2; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Emoji-prefixed title, venue `h2`.
- **Link buttons.** Paper, arXiv, Video, Code, Data.
- **Teaser.** Teaser section with figure/video.
- **Abstract and video.** Abstract, then a dedicated Video section.
- **Overview.** Method figure.
- **Results.** Gigapixel image, image fitting comparison, quantitative comparison, subjective comparison, signed distance function.
- **Image-comparison slider and magnifier.** Used across the results.
- **BibTeX.** End section.
- Not present: results table (quantitative comparison is an image, inferred), HF demo. The extractor flagged interactive 3D, but only zoom and slider scripts load; treat it as zoom inspection, not a 3D viewer.

## Do's and Don'ts

**Do**

- Give readers a magnifier and a slider when the claim is about fine surface detail.
- Use simple gray tabs to switch scenes in place.

**Don't**

- Don't hard-code pixel widths if the page must work on phones.
- Don't load three copies of jQuery (2.2.4, 3.2.1, 3.5.1 are all included here).

## Surfaces

White page; light gray tab buttons; whitesmoke BibTeX well.

## Imagery

Gaussian-splat renders, surface normal and depth maps, gigapixel crops, SDF visualizations.

## Layout

Header, teaser, abstract, video, overview, a long results section with sub-headings, BibTeX.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Tab #f1f1f1
- Tab active #666666
- Buttons #363636
- Headings #363636

**Example component prompts**

1. Create a row of scene tabs: borderless, 10px 16px padding, #f1f1f1 fill, 18px text, 8px radius; hover and active fill #666666 with white text.
2. Create a before/after slider pair at 467px wide each with 20px gap, captions above.
3. Create an image magnifier with a 130px square lens over a high-resolution render.

## Similar Pages

- Nerfies (nerfies.github.io).
- DC2 project page (credited).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-well: #f5f5f5;
  --text-strong: #363636;
  --text: #4a4a4a;
  --venue: #555555;
  --author-link: #3298dc;
  --link: #3273dc;
  --border: #dbdbdb;
  --frame: #bbbbbb;
  --font-display: 'Google Sans', 'Noto Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-mono: monospace;
  --radius-pill: 290486px;
  --radius-sm: 4px;
  --radius-media: 10px;
  --tab: #f1f1f1;
  --tab-active: #666666;
  --radius-tab: 8px;
  --container: 1152px;
}
```

## Provenance

- URL: https://hebing-sjtu.github.io/SurfSplat-website/
- Paper: SurfSplat: Conquering Feedforward 2D Gaussian Splatting with Surface Continuity Priors (Bing He et al.), arXiv 2602.02000.
- Venue: ICLR 2026 (per the arXiv comment). Field: Gaussian splatting.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says the template was borrowed from nerfies and DC2; CC BY-SA 4.0.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
