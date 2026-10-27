# Lavender Edit Suite — Style Reference

> An image-editing gallery lit in lavender, with a slider down the middle of every picture.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

A Nerfies descendant that layers Bootstrap and several gallery widgets on top: a juxtapose.js before/after slider, a thumbnail tab gallery, a flip-card fader and an image-card slider. The brand color is a soft lavender, #8784C7 (and the near twin rgb(141, 133, 229)), used inline for feature labels and for one filled tab. A purple heart emoji prefixes the page title. The paper title switches to Lato, and section dividers are a gradient `hr` that fades from white to 35% black and back. Thirty images and no videos: this is a still-image page.

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
| Flow Lavender | `#8784C7` | `--accent` | Inline label color; one tab filled #8784C7 with white text |
| Periwinkle Label | `rgb(141, 133, 229)` | `--accent-2` | Inline color on five feature labels |
| Deep Indigo | `#5555AA` | `--accent-deep` | Single inline use (inferred: legend or highlight) |
| Mauve Tag | `#CAA6CA` | `--tag-mauve` | Single inline use (inferred: category marker) |
| Teal Tag | `#5D9EAB` | `--tag-teal` | Single inline use (inferred: category marker) |
| Interpolation Well | `#f5f5f5` | `--panel` | `.interpolation-panel` background, 10px radius |

The `hr` is `linear-gradient(to right, rgba(255,255,255,0.9), rgba(0,0,0,0.35), rgba(255,255,255,0.9))`, 2px high. Google Fonts for Akronim, Monoton, Sofia, VT323 and others are requested but no page rule uses them (inferred unused).

## Tokens — Typography

**Families.** Lato for the paper title (`.publication-title { font-family: Lato }`), Google Sans for authors, Noto Sans for body, Source Sans Pro from the Bootstrap layer, Helvetica/Arial inside juxtapose. Substitutes: Open Sans for Lato, Inter for Google Sans.

| Role | Size | Weight | Family |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem (48px), margin-top -20px | 600 | Lato |
| Paper title (`title is-2`) | 2.5rem (40px) | 600 | Google Sans |
| Section heading (`title is-3`) | 2rem (32px) | 600 | Noto Sans |
| Sub-heading (`title is-4`) | 1.5rem (24px) | 600 | Noto Sans |
| Author line (`is-size-5`) | 1.25rem (20px) | 400 | Google Sans |
| Body / abstract | 1rem (16px), line-height 1.5 | 400 | Noto Sans |
| Button label | 1rem | 400 | Noto Sans |
| BibTeX | .875em | 400 | monospace |
| Gallery caption (`#imgtext`) | 20px | 400 | inherit, white on image |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |
| --radius-none | 0 | most gallery images and tab thumbnails (radius 0 is the most frequent value) |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred). Hero bottom padding is reduced to 24px. The juxtapose embed is forced to 100% width.

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, Code, BibTex (the BibTex button jumps to the anchor). Four extra `button is-normal` (not rounded) act as gallery controls.
- **Before/after slider.** juxtapose.js: 3px handle line in currentColor (#f3f3f3), 9px x 60px controller, 8px triangular arrows; inline width splits like 54.53% / 45.47%.
- **Tab gallery.** `.tab_column` 10% wide thumbnails at opacity 0.8, full opacity on hover; caption `#imgtext` white 20px at bottom-left; close button white 35px.
- **Flip-card fader.** 1000px x 215px card, 1.5s 3D flip, 1s opacity fade between states.
- **Feature tabs.** Four 24%-wide labels in #8784C7; the active one filled #8784C7 with #FFFFFF text.
- **Gradient divider.** 2px `hr` fading at both ends, 20px bottom margin.
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and credit to the adapted source code and InfEdit; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Emoji-prefixed Lato title, Google Sans authors with numbered affiliations.
- **Link buttons.** Paper, Code, BibTex.
- **Overview figure.** Teaser image instead of video.
- **Feature gallery.** Text-driven image and video editing examples in tabs and sliders.
- **Image-comparison slider.** juxtapose before/after.
- **Method.** Uni-Inv and Uni-Edit subsections with MathJax equations.
- **Carousel.** bulma-carousel for extra results.
- **BibTeX.** End section.
- Not present: abstract heading, results table, video, 3D viewer, demo.

## Do's and Don'ts

**Do**

- Keep lavender for labels and the active tab only.
- Show every edit as a before/after slider so the reader can scrub the change.
- Use the faded gradient `hr` between major sections.

**Don't**

- Don't load display fonts you never use (several are requested here).
- Don't put rounded corners on gallery images; they are square.
- Don't add video; the page is a still-image gallery.

## Surfaces

White page, #f5f5f5 interpolation panels, white text overlaid directly on images in the tab gallery.

## Imagery

Source and edited image pairs, thumbnail strips, method equations. Images are square-cornered.

## Layout

Single centered column; overview, feature gallery, method, BibTeX. Gallery widgets run full container width.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Accent #8784C7
- Accent 2 rgb(141,133,229)
- Buttons #363636
- Slider handle #f3f3f3

**Example component prompts**

1. Create a four-tab feature selector, each tab 24% wide, label color #8784C7; the active tab filled #8784C7 with white text.
2. Create a before/after image slider at full width with a 3px light handle, a 9px x 60px grip and small triangular arrows.
3. Create a section divider: 2px hr with a horizontal gradient from rgba(255,255,255,.9) to rgba(0,0,0,.35) and back.

## Similar Pages

- InfEdit project page (credited for website code).
- Nerfies (nerfies.github.io).
- Other flow-model editing pages with juxtapose sliders.

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
  --font-display: Lato, 'Noto Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-mono: monospace;
  --radius-pill: 290486px;
  --radius-sm: 4px;
  --radius-media: 10px;
  --accent: #8784C7;
  --accent-2: rgb(141, 133, 229);
  --panel: #f5f5f5;
  --container: 1152px;
}
```

## Provenance

- URL: https://uniedit-flow.github.io/
- Paper: UniEdit-Flow: Unleashing Inversion and Editing in the Era of Flow Models (Guanlong Jiao et al.), arXiv 2504.13109.
- Venue: ICLR 2026 (per the arXiv comment). Field: image editing.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says the site was adapted from linked source code (Nerfies lineage, inferred from class names) and also refers to InfEdit's website code.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified. One CSS path (`assets/css` directory) returned an HTTP error during extraction; the named CSS files loaded.
