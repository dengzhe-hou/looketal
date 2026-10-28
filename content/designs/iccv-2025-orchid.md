# Orchid — Style Reference

> A gallery wall in a quiet lab: plain gray type on white, then pale gray bands where color, depth and normal maps hang side by side.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `css/index.css`, inline `<style>` and `index.html`, read against the Bulma 0.9 defaults it loads (`bulma.min.css`, `bulma-carousel`, `bulma-slider`, `bulma-switch`, `twentytwenty.css`). The page is a Nerfies-template build; the footer credits Nerfies. Google Fonts is requested without weights, so only Google Sans 400 and Noto Sans 400 load and every 600 heading is a synthesized bold.

## Overview

A restrained academic page (about 6,700px tall) on white. The header is centred: a 48px Google Sans title in Bulma's dark gray #363636, an "Accepted to ICCV 2025" line at 32px, blue author links, a gray affiliation line and a single dark rounded "Paper" button with an orange-red PDF icon. A wide multi-panel teaser figure (pastel mint, green and peach panels that belong to the image itself) fills the 1296px container, captioned in one centred line with "Orchid" in small caps. Below, centred section titles in Noto Sans 32px introduce short justified paragraphs in a 763px column, alternating with full-width #f5f5f5 bands that hold carousels: triplets of color / depth / normal images with italic prompts, before/after sliders comparing depth and normal predictions (with a toggle switch), and Gaussian-splat renders. A "How does it work?" section shows the training and inference figures, then a gray BibTeX block and a #fafafa footer.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 47.6% (plus #fffdf6 4.8% and #fffeff 0.9%); the teaser figure supplies the rest: lavender gray #9d9cb0 13.1%, mint #d8eedc 11.7%, dark mauve #57435d 11.5%, pale green #f0f4ec 9.7%, #d7fdda 0.7%.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Header hero** (`section.hero` > `.hero-body`, 0–431px): padding 48px 24px; inner `.container.is-max-desktop` 960px (x=240 to 1200).
2. **Title** (`h1.title.is-1.publication-title`, y=48–156): Google Sans 48px/600 (synthesized from 400), line-height 1.125, #363636, two lines. Gap 24px.
3. **Venue line** (`h3.title`, y=180–216): "Accepted to ICCV 2025", Noto Sans 32px/600, line-height 1.125, #363636. Gap 24px (Bulma `.title` margin) then 7px.
4. **Authors** (`.publication-authors.is-size-5`, y≈247): Google Sans 20px/400, line-height 1.5; names #209cee (`hsl(204, 86%, 53%) !important`), superscript numbers in small type #4a4a4a, commas between.
5. **Affiliations** (second `.publication-authors`, y=275): Google Sans 20px #4a4a4a with superscript numbers.
6. **Button row** (`.publication-links`, y=326–366): one `a.button.is-normal.is-rounded.is-dark` "Paper": #363636 fill, white Noto Sans 16px, padding 7px 20px, fully rounded, 5px vertical margin, Font Awesome `fa-file-pdf` icon colored orangered (#ff4500) inline.
7. **Teaser** (`section.hero.teaser`, from y=431): Bulma `.container` 1344px (x=48 to 1392) with `.hero-body` padding 0 24px 48px, so the image spans x=72 to 1368 (1296px) from y=431 to 949 and crosses the fold. Its centred caption (Google Sans 16px, #4a4a4a, "Orchid" in small caps) follows at y≈957.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Title Gray | #363636 | Bulma `$grey-darker` (`.title`, `.is-dark`) | page title, venue line, section titles, Paper button fill |
| Body Gray | #4a4a4a | Bulma `$grey-dark` (body text) | paragraphs, affiliations, teaser caption, BibTeX text, footer text |
| Author Blue | #209cee | `hsl(204, 86%, 53%)` in `.publication-authors a` | author names |
| Link Blue | #3273dc | Bulma `$link` | inline links (e.g. GeoWizard), footer links ("Nerfies") |
| White | #ffffff | (page) | page background, slider nav circles, pagination dots |
| Light Band | #f5f5f5 | Bulma `.hero.is-light` | carousel bands; BibTeX `pre` background |
| Footer Gray | #fafafa | Bulma `.footer` | footer background |
| Band Text | rgba(0,0,0,0.7) | Bulma `.hero.is-light` color | italic prompts above carousel items |
| Frame Gray | #bbbbbb | (literal, `.results-carousel .twoitem`) | 1px border around carousel items |
| PDF Red | #ff4500 | (inline `color: orangered`) | PDF icon in the Paper button |
| Switch Gray | #b5b5b5 | bulma-switch default | off state of the "Show normal predictions" toggle |
| Button Hover | #2f2f2f | Bulma `.is-dark:hover` | Paper button on hover |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors / teaser caption | 'Google Sans', sans-serif | Google Sans 400 only; 600 headings are synthesized bold | Product Sans → Open Sans |
| Body / section titles | 'Noto Sans', sans-serif | Noto Sans 400 only; 600 synthesized | Noto Sans |
| Code | monospace (Bulma) | system monospace (Consolas on Windows) | — |
| Icons | Font Awesome, Academicons | loaded via kit | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 3rem = 48px / 600 / 1.125, Google Sans | #363636 |
| Venue line | `h3.title` (no size class) | 2rem = 32px / 600 / 1.125 | #363636 |
| Section title | `h2.title.is-3` | 2rem = 32px / 600 / 1.125, Noto Sans | #363636 |
| Subsection title | `h3.title` inside "How does it work?" | 24px / 600 | #363636 |
| Authors / affiliations | `.publication-authors.is-size-5` | 1.25rem = 20px / 400 / 1.5, Google Sans | #209cee names; #4a4a4a text |
| Body | `.content.has-text-justified p` | 16px / 400 / 1.5, justified | #4a4a4a |
| Teaser caption | `.teaser h4` | 16px / 400, centred; `.methodname` small-caps | #4a4a4a |
| Carousel prompt | `.captionbox i` | 16px italic, min-height 80px | rgba(0,0,0,0.7) |
| Button | `.button.is-normal` | 16px / 400 | #ffffff |
| BibTeX | `pre` | 14px / 1.5 monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Paper button (`.is-rounded`) | 290486px (fully round) | 1px transparent | none |
| Carousel comparison item (`.twoitem`) | 10px | 1px #bbbbbb | none |
| Single carousel item (`.oneitem`) | 13px | 1px #bbbbbb | none |
| Carousel arrows | 50% (bulma-carousel) | none | `0 0 12px rgba(0, 0, 0, 1)` |
| Pagination dots | 50%, 10px white | none | `0 0 4px rgba(0, 0, 0, 1)` |
| Video embed (`.publication-video`) | 10px | none | none |
| BibTeX `pre` | 0 | none | none |
| Toggle switch | pill | none | none |

## Layout Metrics

- **Header**: `.hero-body` padding 48px 24px; `.container.is-max-desktop` max 960px (x=240 to 1200); title margin-bottom 24px; header 431px tall.
- **Teaser**: Bulma `.container` max-width 1344px at ≥1408px (x=48 to 1392); `.hero-body` padding 0 24px 48px; image 1296px wide.
- **Text sections**: `section.section.pt-0` padding 0 24px 48px (`.pb-4` variants 16px bottom); `.container.is-max-desktop` 960px with `.column.is-four-fifths` → 763px text column at x=338; section title margin-bottom 24px.
- **Bands**: `section.hero.is-light.is-small.mt-4`: #f5f5f5, margin-top 16px, hero-body padding 24px; carousels show three items across at 1440 (each 438px wide, starting at x=53) with 5px side margins; 42px white round arrows sit 15px inside each edge.
- **Comparison sliders**: twentytwenty containers fixed to `aspect-ratio: 4 / 3` (horizontal) or `0.75` (vertical).
- **BibTeX**: `pre` in the 960px container, padding 17.5px 21px.
- **Footer**: #fafafa, padding 16px 24px 0, centred text.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | container 1344px; text 960px | 16px | 48px | 3 carousel items visible |
| 1216–1407px | container 1152px | 16px | 48px | same |
| 1024–1215px | container 960px | 16px | 48px | same |
| 769–1023px | 24px section padding, fluid container | 16px | 48px | columns still side by side |
| ≤768px (Bulma mobile) | 24px | 16px | 48px (Bulma `.is-1`, no override) | `.columns` stack; four-fifths column becomes full width; carousel shows fewer items (bulma-carousel breakpoints) |

## Components

- **Rounded dark button** (`a.external-link.button.is-normal.is-rounded.is-dark`): #363636 fill, white 16px Noto Sans, padding 7px 20px (Bulma rounded adds 1em side padding), fully rounded, icon span left with a colored Font Awesome glyph (orangered PDF). Hover: Bulma darkens to #2f2f2f.
- **Teaser caption**: one centred Google Sans 16px line under the figure, method name in `font-variant: small-caps`.
- **Prompt carousel** (`.results-carousel` in a `.hero.is-light` band): items are composite images (color + depth + normal grids) with 10px radius and 1px #bbbbbb border; italic quoted prompts above each in an 80px-min caption box; white round arrows with a hard black glow `0 0 12px rgba(0, 0, 0, 1)` placed 15px inside each edge; white pagination dots below.
- **Before/after slider**: jQuery twentytwenty inside carousel items; the input image on the left, prediction on the right, white handle with arrows; a bulma-switch "Show normal predictions (hides depth)" toggle (is-rtl) above flips depth vs normals.
- **Section header**: centred Noto Sans 32px/600 #363636 with 24px margin-bottom, then a justified 16px paragraph in the 763px column.
- **BibTeX**: Bulma `pre` (#f5f5f5, 14px monospace, padding 17.5px 21px) with `user-select: all`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / venue / authors / affiliations | yes | centred Nerfies header, blue names |
| Venue badge | present but non-standard | a 32px "Accepted to ICCV 2025" heading, not a badge |
| Link buttons | yes | a single dark rounded Paper button (arXiv and code buttons are commented out) |
| Teaser | yes | full-width multi-panel figure with small-caps caption |
| Overview / abstract | yes | "Overview" section, justified paragraphs |
| Result carousels | yes | three #f5f5f5 bands with image triplets and sliders |
| Before/after comparison | yes | twentytwenty sliders with a depth/normal switch |
| Method figures | yes | "How does it work?" with training and inference figures |
| Video | present but non-standard | 13 `<video>` elements inside carousels; no YouTube embed |
| Results tables | absent from the source | — |
| BibTeX | yes | gray `pre` |
| Footer | yes | #fafafa with Nerfies template credit |

## Adapting to Other Content

- **More authors**: keep them in the 20px Google Sans author line inside 960px; Bulma wraps `.author-block` spans whole, so names never break.
- **A results table**: place a Bulma `table.is-striped` in the 763px four-fifths column (16px, #4a4a4a, header 600 #363636, 1px #dbdbdb rules); bold the best value; no colored fills.
- **Long publication or news lists**: use a #f5f5f5 band with a plain `ul` in the 960px container, dates in 600 #363636, text 16px #4a4a4a, links #3273dc.
- **More media**: add another `.hero.is-light.is-small` band with a carousel; items keep the 10px radius and #bbbbbb hairline.
- **More buttons**: add more `.is-rounded.is-dark` buttons in the same row with 5px vertical margin, each with its own colored icon.

## Do's and Don'ts

- Do keep text gray (#363636 headings, #4a4a4a body) and centred headings over justified 763px paragraphs.
- Do alternate white text sections with #f5f5f5 media bands.
- Do give comparison items a 10px radius and a 1px #bbbbbb frame.
- Do let the figures carry color; the page chrome stays neutral.
- Don't add colored backgrounds or accent fills to the layout; the only color in the chrome is the author blue and the PDF icon.
- Don't widen text beyond the four-fifths column.
- Don't rely on true 600 weights; the page renders synthesized bold from 400 fonts.

## Surfaces

White page; flat #f5f5f5 bands under carousels; a #fafafa footer. No cards, no shadows on content, except the black glow on the white carousel arrows.

## Imagery

Generated image triplets (color, relative depth as warm-to-blue colormaps, surface normals in pastel RGB) of flowers, boots, alpacas, a toy elephant, Einstein and interiors; real indoor and object photos with depth and normal predictions; Gaussian-splat novel-view renders; a pastel-panelled teaser and method diagrams.

## Layout

Classic Nerfies stack: centred header in 960px, a full-width 1296px teaser, then alternating narrow text sections (763px) and full-width gray carousel bands, ending with BibTeX and a footer.

## Agent Prompt Guide

Quick colors: title #363636, body #4a4a4a, authors #209cee, links #3273dc, band #f5f5f5, footer #fafafa, frame #bbbbbb, PDF icon #ff4500.

1. "Build a Nerfies-style header: white, padding 48px 24px, centred 960px column. Title Google Sans 48px/600, line-height 1.125, #363636; a 32px/600 'Accepted to ICCV 2025' line; authors Google Sans 20px with #209cee names and superscripts; affiliations 20px #4a4a4a; one rounded #363636 'Paper' button (white 16px, padding 7px 20px) with an orangered #ff4500 PDF icon."
2. "Make a result band: full-width #f5f5f5, padding 24px, a three-across carousel of composite images (10px radius, 1px #bbbbbb border), italic rgba(0,0,0,0.7) prompts in quotes above each, white round arrows with box-shadow 0 0 12px rgba(0,0,0,1), white dots below."
3. "Create a text section: centred Noto Sans 32px/600 #363636 heading with 24px margin-bottom, then justified 16px/1.5 #4a4a4a paragraphs in a 763px column, padding 0 24px 48px."

## Similar Pages

- Nerfies-template project pages (Bulma, Google Sans titles, gray result bands with carousels).
- Pages that pair image carousels with twentytwenty before/after sliders.

## Quick Start

```css
:root {
  --title: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --link: #3273dc;
  --band: #f5f5f5;
  --footer: #fafafa;
  --frame: #bbbbbb;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --text-col: 763px;
  --item-radius: 10px;
}
```

## Provenance

- **URL**: https://orchid3d.github.io/
- **Paper**: Orchid: Image Latent Diffusion for Joint Appearance and Geometry Generation (arXiv 2501.13087), Akshay Krishnan, Xinchen Yan, Vincent Casser, Abhijit Kundu (Google DeepMind; Georgia Institute of Technology; Waymo).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: Nerfies (footer: "Website template based on Nerfies", CC-BY-SA 4.0), Bulma 0.9 with bulma-carousel, bulma-slider, bulma-switch and jQuery twentytwenty.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `index.css`, the inline style and `index.html` read directly, on 2026-10-28.
