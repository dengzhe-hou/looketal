# Five-Letter Spectrum — Style Reference

> A plain Nerfies page that spends its whole color budget on one word.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

The leanest page in the batch: two images, one video, four sections (Abstract, Exemplary Visual Results, Method Overview, BibTeX). Its `index.css` is the unmodified Nerfies file. The single design decision is in the title: the five letters of "Color" in "Color3D" each get their own inline color, red #e63946 followed by four Dracula-theme hues (#f1fa8c yellow, #8be9fd cyan, #50fa7b green, #bd93f9 purple). Everything else is Bulma default. Only Paper and Code buttons are present.

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
| Letter C Red | `#e63946` | `--c1` | Title letter C |
| Letter o Lemon | `#f1fa8c` | `--c2` | Title letter o (Dracula yellow) |
| Letter l Cyan | `#8be9fd` | `--c3` | Title letter l (Dracula cyan) |
| Letter o Mint | `#50fa7b` | `--c4` | Title letter o (Dracula green) |
| Letter r Lilac | `#bd93f9` | `--c5` | Title letter r (Dracula purple) |

The pale yellow #f1fa8c and cyan #8be9fd have low contrast on white; they read as decoration, not text color.

## Tokens — Typography

**Families.** Google Sans for title and authors, Noto Sans for body (stock Nerfies). Substitutes: Inter.

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

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-pill | 290486px | `is-rounded` link buttons |
| --radius-sm | 4px | Bulma default controls, tags |
| --radius-md | 6px | Bulma boxes, cards |
| --radius-media | 10px | `.publication-video`, carousel items |

**Shadows.** Shadows are almost absent. The only framework shadow that appears in practice is Bulma's card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`; focus rings use `0 0 0 .125em rgba(50,115,220,.25)`.

**Layout width.** Bulma `.container` caps at 1152px (widescreen) and 1344px (fullhd); text columns usually sit in `column is-four-fifths` or `is-two-thirds` inside it, so prose runs about 750-920px wide (inferred).

## Components

- **Link button (Paper / arXiv / Code ...).** `a.external-link.button.is-normal.is-rounded.is-dark`: fill #363636, white label, pill radius 290486px, Font Awesome or Academicons glyph in a `span.icon` before a `span` label, 5px vertical margin from `.link-block a`. Labels: Paper, Code.
- **Spectrum title.** `title is-1 publication-title` with five `span style="color:..."` letters, then plain "3D: Controllable and Consistent 3D Colorization ..." in #363636.
- **Results carousel.** Template `.results-carousel .item`: 1px #bbb border, 10px radius, `font-size: 0`.
- **Interpolation panel.** Template class present in CSS (#f5f5f5, 10px radius), not a visible module (inferred).
- **BibTeX block.** `section#BibTeX` with `h2.title` "BibTeX" above a Bulma `pre > code`; background #f5f5f5, text #4a4a4a, padding 1.25em 1.5em, no border, left-aligned monospace.
- **Footer.** Bulma `footer.footer` on #fafafa (Bulma default, inferred), centered small text with the CC BY-SA 4.0 license sentence and thanks to the Nerfies authors; `.footer .icon-link` 25px black.

## Page Modules

- **Title/author block.** Spectrum-lettered title, Google Sans authors.
- **Link buttons.** Paper, Code (no arXiv button).
- **Teaser video.** One video in `.hero.teaser`.
- **Abstract.** Standard.
- **Exemplary visual results.** Carousel of colorized 3D scenes.
- **Method overview.** One figure.
- **BibTeX.** End section.
- Not present: results table, slider, demo. The extractor flagged an interactive 3D module, but no 3D viewer script is loaded; treat the flag as a false positive.

## Do's and Don'ts

**Do**

- If you color a word letter by letter, keep the rest of the page neutral.
- Keep the stock Nerfies spacing for short pages.

**Don't**

- Don't use #f1fa8c or #8be9fd for body text on white.
- Don't add extra accents; the title already carries the palette.

## Surfaces

White page and whitesmoke BibTeX well only.

## Imagery

Before and after colorized 3D scene renders, a method diagram.

## Layout

Header, teaser, abstract, results carousel, method, BibTeX in one centered column.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Title letters #e63946 #f1fa8c #8be9fd #50fa7b #bd93f9
- Headings #363636
- Buttons #363636

**Example component prompts**

1. Create a 48px Google Sans title where the letters C, o, l, o, r are colored #e63946, #f1fa8c, #8be9fd, #50fa7b, #bd93f9 and the rest is #363636.
2. Create a results carousel tile with 1px #bbbbbb border and 10px radius containing a 3D render.
3. Create two dark pill buttons (Paper, Code) centered under the author list.

## Similar Pages

- Nerfies (nerfies.github.io).
- Other single-accent Nerfies clones in 3D editing.

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
  --c1: #e63946;
  --c2: #f1fa8c;
  --c3: #8be9fd;
  --c4: #50fa7b;
  --c5: #bd93f9;
  --container: 1152px;
}
```

## Provenance

- URL: https://yecongwan.github.io/Color3D/
- Paper: Color3D: Controllable and Consistent 3D Colorization with Personalized Colorizer (Yecong Wan et al.), arXiv 2510.10152.
- Venue: ICLR 2026 (per the arXiv comment). Field: 3D vision.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer thanks the Nerfies authors for the template; CC BY-SA 4.0.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
