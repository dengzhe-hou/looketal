# InfiniteYou — Style Reference

> A darkroom contact sheet that never stops scrolling: one face, recrafted a hundred ways, drifting past in endless rows on charcoal.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, scrolled viewport shots at y=2200, 3500 and 4800, a probe of rendered elements (rules, carousel rows, inset thumbnails, abstract, figures, footer), and the page's own `src/index.css`, `src/carousel.css` and `index.html` over Bulma (a Nerfies-derived build). No web font loads at all (`fonts_loaded` is empty): the Google Fonts stylesheet is linked as `./src/css` and never applies, so "Noto Sans" and "Google Sans" fall back to the system sans (Arial on Windows), and the title's `bradley hand, cursive` renders as Bradley Hand on macOS but Comic Sans MS on Windows, which is what the screenshot shows. The photo rows scroll continuously by CSS animation, so their horizontal position in any screenshot is arbitrary.

## Overview

A dark, image-led page (about 6,600px tall) on charcoal #202020 with off-white text #f5f5f5. The header is centred: a 48px handwritten-style title, a row of six author names in 22px plain sans separated by wide spaces, "ByteDance Intelligent Creation", and a bold "ICCV 2025 (Highlight)" with "Highlight" in red #f44336, then five dark gray (#363636) rounded Bulma buttons with icons. A thin translucent white rule spans the page, a one-line tagline follows, and then the signature module: six full-width rows of 200px portrait photos that scroll endlessly (alternating directions, 40s per loop, pausing on hover), each row with an 80px white-framed identity thumbnail pinned at its top-left and 140px charcoal fades at both ends. After a second rule, the text sections (Abstract, Comparison, Plug-and-Play, Disclaimer and Licenses, Acknowledgments, BibTeX) are Nerfies-style: centred 24px headings, justified 16px text in a 763px column, and 960px figures. A #303030 BibTeX block and a centred footer close the page.

## First Viewport

Color share (quantized 1440×900 shot): charcoal #202020 53.3% (plus #20201f 3.1%, #202021 2.7%, #1d2021 1.5%); the photo rows supply warm dark brown #433a38 15.8%, sand gray #9d9d8d 14.6%, near-black #1a1414 5.9% and #2d201c 3.0%.

Anatomy in DOM order (desktop 1440px, centred, `.container.is-max-desktop` 960px at x=240):

1. **Navbar** (`nav.navbar`, 0–52px): empty #202020 bar (only a burger that is hidden on desktop), so the page opens with 52px of blank charcoal.
2. **Hero** (`section.hero` > `.hero-body`, 52–484px): padding 48px 24px, background #202020.
3. **Title** (`h1.title.is-1.publication-title`, y=100–214): 48px, line-height 1.125, weight 200 declared, #f5f5f5, two lines; the text is a `span` set in `bradley hand, cursive`. Gap 24px.
4. **Authors** (`.publication-authors`, inline 22px, y=238–271): six names in #f5f5f5, each followed by four non-breaking spaces instead of commas; no superscripts. Hover underlines.
5. **Affiliation** (y=271–304): "ByteDance Intelligent Creation", 22px #f5f5f5, margin-bottom 15px.
6. **Venue** (y=319–352): bold 22px "ICCV 2025 (Highlight)", "Highlight" in a `<font color="#F44336">`. Margin-bottom 10px.
7. **Buttons** (`.publication-links`, y=379–419): Paper, Code, Model, ComfyUI, Demo; Bulma `.button.is-rounded.is-dark`: #363636 fill, white 16px, padding 7px 20px, fully round, 5px vertical margins, 4px apart; icons are inline Font Awesome SVGs or 18px SVG images on a #f5f5f5 square.
8. **Rule** (`hr` inline style, y=481): 0.7px tall, `background-color: rgba(255, 255, 255, 0.665)`, width 100% (x=12 to 1428), margin-top -15px, margin-bottom 24px.
9. **Tagline** (`.teaser .is-size-5`, y≈505): "Create Infinite Photographs of You with Diffusion Transformers (DiTs) like FLUX!", 20px #f5f5f5, centred.
10. **Photo rows** (`.carousel-container` ×6, from y=572): each 1372×274 at x=34; first row at 572, second at 845; 200px-wide portraits (4px radius, 3px apart) in an endless strip; an 80px identity thumbnail in a 1px #ffffff frame with 5px radius at 20px,20px of each row. The first row fills the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Charcoal | #202020 | --main-background-color | html, body, navbar, hero bodies, containers, footer, carousel edge fades |
| Off-White | #f5f5f5 | --main-color | title, headings, authors, body text, links, footer, icon backplates |
| Button Gray | #363636 | Bulma `.is-dark` | rounded link buttons |
| Code Gray | #303030 | (literal, `.bib-tex`) | BibTeX block background |
| Highlight Red | #f44336 | (inline `<font color>`) | "Highlight" in the venue line |
| Rule White | rgba(255,255,255,0.665) | (inline `hr`) | the two full-width hairlines |
| Frame White | #ffffff | (literal, `.carousel-float`) | 1px frame of the identity thumbnails; button text |
| Hidden Light Band | #f5f5f5 | Bulma `.hero.is-light` | declared on the photo-row section but fully covered by #202020 inner `.hero-body` and `.container`, so it never shows |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title | `bradley hand, cursive` (inline span); `.publication-title` sets Georgia 200 underneath | no web font; Bradley Hand on macOS, Comic Sans MS on Windows | Caveat |
| Authors / teaser | 'Google Sans', sans-serif | not loaded; system sans (Arial on Windows, Helvetica on macOS) | Arial |
| Body / headings | 'Noto Sans', sans-serif | not loaded; system sans | Arial |
| Code | monospace | Consolas on Windows | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title > span` | 48px / 200 declared / 1.125, cursive | #f5f5f5 |
| Authors, affiliation, venue | `.publication-authors` (inline 22px) | 22px / 400 (venue bold) / 1.5 | #f5f5f5; "Highlight" #f44336 |
| Tagline | `.teaser .is-size-5` | 20px / 400 | #f5f5f5 |
| Section heading | `h2.title.is-4` | 24px / 400 / 1.125, centred | #f5f5f5 |
| Body | `.content.has-text-justified` | 16px / 400 / 1.5, justified | #f5f5f5 |
| Button | `.button.is-normal` | 16px / 400 | #ffffff |
| BibTeX | `pre.bib-tex` | 14px / 1.5 monospace | #f5f5f5 |
| Footer | `footer.footer` | 16px, centred | #f5f5f5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px (fully round) | 1px transparent | none |
| Portrait tiles (`.carousel img`) | 4px | none | none |
| Identity thumbnail (`.carousel-float`) | 5px | 1px #ffffff | none |
| Row edge fades | — | — | `linear-gradient(270deg, rgba(32, 32, 32, 0), rgba(32, 32, 32, 1))` on the left and `linear-gradient(90deg, rgba(32, 32, 32, 0), rgba(32, 32, 32, 1))` on the right, each 140px wide |
| Figures in sections | 0 | none | none |
| BibTeX `pre` | 4px | none | none |
| Rules | 0 | 0.7px rgba(255,255,255,0.665) fill | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop` 960px (x=240 to 1200) for the header, figures and BibTeX; text in `.column.is-four-fifths` → 763px at x=338.
- **Header**: navbar 52px; `.hero-body` padding 48px 24px; title margin-bottom 24px; affiliation margin-bottom 15px; venue margin-bottom 10px; buttons 40px tall with 5px vertical margins.
- **Photo rows**: section `.hero.is-light.is-small` (padding 24px) holding six `.carousel-container`s of 1372px × 274px stacked with no gap (y=572, 845, 1119, 1393, 1666, 1940); tiles 200px wide, `margin-right: 3px`; the strip is duplicated so `translateX(-50%)` loops seamlessly; `scroll-left` and `scroll-right` both run 40s linear infinite; hover pauses.
- **Sections**: `section.section` padding 48px 24px with margin-top -15px; heading margin-bottom 24px; figures 960px wide (e.g. the method figure 960×822 at y=2652).
- **Second rule**: at y=2219, x=34 to 1406, margin 5px 0 24px.
- **Footer**: padding 48px 24px 96px, margin-top -10px, text in an 8-of-12 column, centred.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | 24px; text column 763px | 16px | 48px | six photo rows full width |
| 1024–1215px | 24px | 16px | 48px | same; `.is-max-desktop` stays 960px |
| 769–1023px | 24px | 16px | 48px | containers become fluid |
| ≤768px | 24px | 16px | 48px (no override) | Bulma columns stack; navbar burger appears; photo rows keep 200px tiles and scroll |

## Components

- **Rounded dark button** (`a.external-link.button.is-normal.is-rounded.is-dark`): #363636, white 16px, padding 7px 20px, fully round, leading 18px icon (Font Awesome SVG, or an SVG logo on a #f5f5f5 square for Model / ComfyUI / Demo).
- **Endless photo row** (`.carousel-container` > `.carousel.carousel-scroll-left|right`): overflow hidden; `display: inline-flex; width: max-content`; 200px portrait images with 4px radius and 3px gaps; 140px charcoal fades at both ends via `::before` / `::after`; an absolutely positioned `.carousel-float` (left 20px, top 20px, 1px #ffffff border, 5px radius) shows the 80px source identity photo; hover pauses the animation.
- **Hairline rule**: inline `hr` 0.7px tall, rgba(255,255,255,0.665), full width.
- **Section**: centred `h2.title.is-4` 24px/400 #f5f5f5, then justified 16px text in 763px with bold method names, then a 960px figure.
- **BibTeX** (`pre.bib-tex`): #303030, 4px radius, padding 20px 24px, 14px monospace #f5f5f5; a 30px copy button absolutely positioned 30px from the top-right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | present but non-standard | empty 52px charcoal bar on desktop |
| Title / authors / affiliation | yes | centred, cursive title, plain 22px names without superscripts |
| Venue line | yes | bold 22px text with red "Highlight" |
| Link buttons | yes | five #363636 rounded Bulma buttons |
| Teaser | present but non-standard | six endlessly scrolling photo rows with identity insets instead of a figure |
| Abstract | yes | centred heading, justified text |
| Comparison / plug-and-play figures | yes | 960px figures |
| Disclaimer, acknowledgments | yes | text sections |
| Video | absent from the source | — |
| Results tables | absent from the source | comparisons are shown as figures |
| BibTeX | yes | #303030 block with copy button |
| Footer | yes | centred source-code line on charcoal |

## Adapting to Other Content

- **More authors**: keep the 22px names separated by wide spaces; at more than seven they wrap to a second line inside 960px, and affiliations stay on their own 22px line.
- **A results table**: place it in the 960px container on #202020 with 16px #f5f5f5 text, 1px rgba(255,255,255,0.665) rules like the page hairlines, header bold; best values bold rather than colored (red #f44336 is reserved for the Highlight label).
- **Long publication or news lists**: centred 24px heading, then rows of 16px #f5f5f5 text in the 763px column with bold dates.
- **More image rows**: add `.carousel-container`s; alternate `carousel-scroll-left` and `carousel-scroll-right` and keep the 80px framed identity inset.
- **Font fallback**: link the Google Fonts stylesheet correctly (or self-host) if the intended Noto Sans / Google Sans look matters; as served, everything renders in the system sans.

## Do's and Don'ts

- Do keep the page charcoal #202020 with #f5f5f5 type; the photos supply all the color.
- Do let the photo wall run full width with soft charcoal fades at the edges.
- Do frame identity references with a 1px white border and 5px radius.
- Do keep buttons quiet (#363636) so they do not compete with the images.
- Don't rely on the cursive title face being the same everywhere; it changes between macOS and Windows.
- Don't add colored backgrounds or cards behind sections.
- Don't use red for anything except the Highlight label.

## Surfaces

Flat charcoal everywhere (page, navbar, hero, rows, footer); the only lighter surfaces are #363636 buttons and the #303030 BibTeX block; two translucent white hairlines divide the header, the photo wall and the text.

## Imagery

Dense rows of photorealistic generated portraits (women and men across settings: fields, cars, space stations, cities, sports, history) all preserving one identity per row, plus comparison grids against other identity methods and plug-and-play examples with ControlNet- and LoRA-style variations.

## Layout

A centred 960px header, a full-width photo wall (six 274px rows), then narrow Nerfies-style text sections with 960px figures, ending in BibTeX and a footer.

## Agent Prompt Guide

Quick colors: background #202020, text #f5f5f5, buttons #363636, code #303030, highlight #f44336, rules rgba(255,255,255,0.665), inset frame #ffffff.

1. "Build a dark centred header on #202020: a 48px title in a handwritten face (#f5f5f5, line-height 1.125), 22px author names separated by wide spaces, a 22px affiliation, a bold 22px 'ICCV 2025 (Highlight)' with 'Highlight' in #f44336, and fully rounded #363636 buttons (white 16px, padding 7px 20px, 18px icons)."
2. "Make an endless photo wall: full-width rows 274px tall, each an inline-flex strip of 200px portraits (4px radius, 3px gaps) duplicated and animated translateX(0 → -50%) over 40s linear infinite, alternating direction per row, paused on hover; 140px edge fades linear-gradient(90deg, rgba(32,32,32,0), rgba(32,32,32,1)); an 80px source photo pinned at 20px,20px with a 1px #ffffff border and 5px radius."
3. "Create text sections: a full-width 0.7px rgba(255,255,255,0.665) hairline, centred 24px/400 #f5f5f5 headings, justified 16px/1.5 #f5f5f5 paragraphs in a 763px column, 960px figures, and a BibTeX block (#303030, 4px radius, padding 20px 24px, 14px monospace)."

## Similar Pages

- Nerfies-template pages recolored to a dark theme.
- Identity and portrait generation pages that open with an auto-scrolling sample wall.

## Quick Start

```css
:root {
  --main-color: #f5f5f5;
  --main-background-color: #202020;
  --button: #363636;
  --code-bg: #303030;
  --highlight: #f44336;
  --rule: rgba(255, 255, 255, 0.665);
  --font-title: "Bradley Hand", cursive;
  --font-body: 'Noto Sans', Arial, sans-serif;
  --container: 960px;
  --tile-width: 200px;
  --row-loop: 40s;
}
```

## Provenance

- **URL**: https://bytedance.github.io/InfiniteYou/
- **Paper**: InfiniteYou: Flexible Photo Recrafting While Preserving Your Identity (arXiv 2503.16418), Liming Jiang, Qing Yan, Yumin Jia, Zichuan Liu, Hao Kang, Xin Lu (ByteDance Intelligent Creation).
- **Venue**: ICCV 2025 (Highlight, as stated on the page).
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: none stated on the page; the structure, Bulma classes and `index.css` come from the Nerfies template, recolored dark, with a custom `carousel.css` for the photo rows.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, three scrolled viewport shots, a rendered-element probe, and `index.css`, `carousel.css` and `index.html` read directly, on 2026-10-28.
