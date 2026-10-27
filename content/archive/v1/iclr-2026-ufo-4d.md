# Blueprint Tile Deck — Style Reference

> Engineering review boards: pale blue tiles, navy tabs, one pair of photos turned into motion.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A Nerfies base reworked into a card layout: every `section > .container` becomes a rounded tile filled #f8fafd with 16px radius and 2rem 2.5rem padding, separated by 1px #cccccc rules capped at 960px. The brand ink is a steel blue #0d6fb0, used in weight 800 for the method name and as the fill of small uppercase toggle buttons that hover to navy #053a5c. Comparison grids (input plus five methods) are hidden behind those toggles. Input images pulse between two frames with a 2s fade loop to show the two-image input.

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
| Blueprint Wash | `#f8fafd` | `--tile` | Section tile background (16px radius) |
| Steel Blue | `#0d6fb0` | `--brand` | Method name (weight 800) and `.title-btn` fill |
| Midnight Navy | `#053a5c` | `--brand-dark` | `.title-btn` hover fill and active-state text/border |
| Divider Gray | `#cccccc` | `--rule` | `hr` 1px, max-width 960px |

The page keeps Bulma's #3298dc for author links; the steel blue is reserved for the method name and toggles.

## Tokens — Typography

**Families.** Google Sans for title, authors, venue, method headers and toggle buttons; Noto Sans for body. Substitutes: Inter for Google Sans.

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
| Toggle button | 0.65rem, uppercase, letter-spacing 0.8px | 700 | Google Sans |
| Comparison column header | 0.9rem | 700 | Google Sans |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |
| --radius-tile | 16px | section tiles |

**Shadows.** Presentation video uses `0 4px 10px rgba(0,0,0,0.05)`; toggle hover uses `0 2px 5px rgba(0,0,0,0.15)`. Tiles themselves are flat.

**Layout width.** Hero padding `3rem 1.5rem 1rem`; sections `1rem 1.5rem`; tiles padded `2rem 2.5rem` (1.5rem under 768px); rules max 960px.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, arXiv, Code.
- **Section tile.** `section.section > .container`: #f8fafd, radius 16px, padding 2rem 2.5rem.
- **Title toggle button.** `.title-btn`: fill #0d6fb0, white 0.65rem uppercase Google Sans 700, letter-spacing 0.8px, radius 4px, padding 2px 8px, height 22px, chevron icon that rotates 180deg; hover #053a5c; active white with #053a5c text and border.
- **Comparison grid.** `.method-comparison-grid`: CSS grid `1fr repeat(5, 1fr)`, 6px gap; hidden until toggled, then fades in from translateY(-5px).
- **Pulsing input.** Two stacked frames, second runs `tenPercentFade` 2s linear infinite; 1px #dbdbdb border, 4px radius.
- **Copy button.** Absolutely placed at top 8px right 8px over the BibTeX block, background #f8fafd, transparent border.
- **Affiliation logos.** 16px-high logos after author names.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and credit to Nerfies and "Gemini's help"; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Google Sans title, nowrap author blocks, affiliation logos.
- **Link buttons.** Paper, arXiv, Code.
- **Teaser / presentation video.** Full-width video with 10px radius and faint shadow.
- **How it works.** Method explanation in a tile.
- **4D interpolation.** Expandable grid of interpolation results.
- **Qualitative comparison.** Expandable six-column grid (input + five methods).
- **BibTeX.** Tile with copy button.
- Not present: abstract heading, results table, slider, 3D viewer, demo.

## Do's and Don'ts

**Do**

- Wrap each section in the pale #f8fafd tile with 16px radius.
- Hide large comparison grids behind small labeled toggles.
- Reserve #0d6fb0 for the method name and controls.

**Don't**

- Don't add shadows to tiles; they stay flat.
- Don't use the steel blue for body links.
- Don't show all comparison grids expanded on load.

## Surfaces

White page with pale blue-white tiles; white pulsing-input wrappers inside tiles.

## Imagery

Two-frame input pairs, reconstructed point clouds and novel-view renders, comparison grids across five methods.

## Layout

Stacked tiles in a single column, each with heading, toggle, and grid. Header outside tiles.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Tile #f8fafd
- Brand #0d6fb0
- Brand hover #053a5c
- Rule #cccccc

**Example component prompts**

1. Create a section tile: background #f8fafd, 16px radius, padding 2rem 2.5rem, containing a Google Sans 2rem heading and a figure.
2. Create a toggle chip: 22px tall, fill #0d6fb0, white 0.65rem uppercase Google Sans 700 label with letter-spacing 0.8px, chevron rotating on open, hover #053a5c.
3. Create a six-column comparison grid (input + five methods) with 6px gaps and bold 0.9rem column headers.

## Similar Pages

- Nerfies (nerfies.github.io).
- Other feedforward 4D reconstruction pages with method comparison grids.

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
  --tile: #f8fafd;
  --brand: #0d6fb0;
  --brand-dark: #053a5c;
  --rule: #cccccc;
  --radius-tile: 16px;
  --container: 1152px;
}
```

## Provenance

- URL: https://ufo-4d.github.io/
- Paper: UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images (Junhwa Hur et al.), arXiv 2602.24290.
- Venue: ICLR 2026 (per the arXiv comment). Field: 4D reconstruction.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says the source is based on the Nerfies project page and Gemini's help; CC BY-SA 4.0.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
