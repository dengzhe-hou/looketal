# Multimodal Conventions — Style Reference

> A seminar handout on clean paper: a big soft headline, six charcoal tabs, and a teal-and-magenta comic strip of hands explaining blocks.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, the page's `static/css/index.css`, and `index.html` (with inline styles on the teaser caption and the video note) read directly. The page is a Nerfies template build on Bulma 0.9; the template's results carousel is still in the markup but commented out. The example video is a YouTube embed whose player shows a buffering spinner in a load-time capture.

## Overview

A short white page (about 2,900px tall) in the standard Nerfies shape. The hero centres a three-line 48px Google Sans title in #363636, two lines of eight sky-blue author links, a single affiliation line with superscripts, and a row of six dark rounded buttons (Paper, arXiv, Unimodal Study, Multimodal Study, Dataset, Viewing App) with Font Awesome and Academicons icons. The teaser is a wide three-panel figure (teal-bordered panel A, magenta-bordered panel B, gray panel C) with a centred italic Google Sans caption. Then a centred Abstract in a 763px column, a full-width light-gray band (`hero is-light`, #f5f5f5) holding "Viewing the Dataset" (justified text and a numbered list) and "Example Data Video" (a 16:9 YouTube embed with 10px radius and an italic note), a white BibTeX section and a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 78.2% plus near-whites #fafbfb 2.2%, #fdffff 0.8%, #fffffd 0.3%; cool gray #b6bdbf 5.9% and #dbe3e7 4.3% (teaser line art and gray panel), warm dark gray #5f5759 4.4% (title, buttons, caption text), pale pink-gray #f3efef 3.9% (speech bubbles in the teaser). The sky-blue links and the teaser's teal and magenta borders are too thin to form clusters.

Anatomy in DOM order (desktop 1440px; `section.hero > .hero-body` padding 48px 24px; `.container.is-max-desktop` 960px from x=240; everything centred):

1. **Title** (`h1.title.is-1.publication-title`, y=48, 162px tall): three lines, Google Sans 48px / 600 (synthetic bold; only 400 loads), line-height 1.125, #363636. Margin-bottom 24px.
2. **Authors** (`.publication-authors.is-size-5`, y=234, two lines to y≈303): eight links in Google Sans 20px / 400, #209cee (hsl(204, 86%, 53%) !important), each with a #4a4a4a superscript digit and comma.
3. **Affiliations** (second `.publication-authors`, y≈303, one line): Google Sans 20px #4a4a4a, "¹Princeton University ²University of California, San Diego ³Brown University ⁴MIT ⁵Stanford University".
4. **Buttons** (`.publication-links`, y=355, 40px tall; second Bulma column with 12px padding): six `is-dark is-rounded` buttons 4–5px apart (inline whitespace) in one row from x=284 to 1156. Hero ends at y=460.
5. **Teaser** (`section.hero.teaser`, `.hero-body` padding 0 24px 48px; image at y=460, 912×141): no radius or shadow; panels drawn in the image with teal, magenta and gray rounded borders.
6. **Teaser caption** (`p.has-text-centered`, y=616, 96px tall): Google Sans 16px / 1.5 italic (inline style), #4a4a4a, centred, margin-top 8px.

The Abstract section starts at y=760 with its heading at y=808.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (Bulma `$white`) | page background, button labels |
| Heading Gray | #363636 | (Bulma `$grey-darker`) | title, Abstract and BibTeX headings, button fill |
| Body Gray | #4a4a4a | (Bulma `$grey-dark`) | abstract text, teaser caption, affiliations, superscripts, BibTeX text |
| Sky Link | #209cee | (literal, hsl(204, 86%, 53%) !important) | author name links |
| Light Band | #f5f5f5 | (Bulma `$white-ter`, `hero.is-light`) | dataset band background, BibTeX pre |
| Band Ink | rgba(0,0,0,0.7) | (Bulma `hero.is-light` text) | headings, paragraphs, list items and note inside the light band |
| Bulma Link | #3273dc | (Bulma `$link`) | footer links, links inside paragraphs |
| Footer Gray | #fafafa | (Bulma `$white-bis`) | footer background |
| Button Hover | #2f2f2f | (Bulma `.button.is-dark:hover`) | dark button fill on hover |

Teal, magenta and gray panel borders belong to the teaser image.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display (hero, teaser) | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | Google Sans 400 only; 600 synthesized | Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400; bold synthesized | Open Sans |
| Code | Bulma monospace | system monospace (Consolas on Windows) | Source Code Pro |
| Icons | Font Awesome (local CSS and JS), Academicons | FA as injected SVG; Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | Google Sans 48px / 600 / 1.125 | #363636 |
| Authors | `.publication-authors a` | Google Sans 20px / 400 / 1.5 | #209cee |
| Affiliations | `.publication-authors` | Google Sans 20px / 400 | #4a4a4a |
| Button | `.button.is-dark` | Noto Sans 16px / 400 | white |
| Teaser caption | `.teaser p` | Google Sans 16px italic / 1.5 | #4a4a4a |
| Section heading | `h2.title.is-3` | Noto Sans 32px / 600 / 1.125, centred | #363636 (white sections), rgba(0,0,0,0.7) (light band) |
| BibTeX heading | `h2.title` | 28px / 600, left aligned | #363636 |
| Body | `.content.has-text-justified p` | Noto Sans 16px / 1.5, justified | #4a4a4a or rgba(0,0,0,0.7) in the band |
| List | `.content ol`, `ul` | 16px, indent 32px, 4px between items | rgba(0,0,0,0.7) |
| Video note | inline-styled `p` | 14px italic / 1.5, centred | rgba(0,0,0,0.7) |
| BibTeX | `pre` | 14px / 1.5 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 290486px | 1px transparent | none |
| Teaser image | 0 | none | none |
| Video embed | 10px (`.publication-video`, !important), overflow hidden | none | none |
| BibTeX pre | 0 | none | none |
| Light band | 0 | none | none |

## Layout Metrics

- **Container**: `.container.is-max-desktop` 960px at ≥1024px (x=240 at 1440).
- **Hero**: `.hero-body` padding 48px 24px, 460px tall.
- **Teaser**: `.teaser .hero-body` padding-top 0, bottom 48px, sides 24px, so the figure is 912px wide from x=264; section 300px tall.
- **Abstract and band sections**: Bulma `.section` padding 48px 24px; content in `.column.is-four-fifths` (787px with 12px padding, text 763px from x=338).
- **Light band**: `section.section.hero.is-light`, full width, #f5f5f5, 1063px tall here, holding two four-fifths columns stacked.
- **Video**: 16:9 `.publication-video`, 763×429, radius 10px; note 8px below.
- **BibTeX**: `.container.is-max-desktop.content`, pre padding 17.5px 21px at full 960px.
- **Footer**: padding 48px 24px 96px; inner `.column.is-8` 888px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1024px | 960px container, 24px section padding | 16px | 48px | four-fifths text columns (763px) |
| 769–1023px | fluid container | 16px | 48px | four-fifths columns of the fluid width |
| ≤768px | 24px | 16px | 48px | Bulma columns stack full width; buttons wrap |

## Components

- **Dark pill button** (`a.external-link.button.is-normal.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, 40px tall, radius 290486px, icon on the left in a 24px `.icon` span (FA file-pdf, Academicons arXiv, FA GitHub ×2, FA database, FA hand-pointer). Hover #2f2f2f.
- **Teaser with italic caption**: full-width unframed image, then a centred Google Sans 16px italic caption starting "Figure 1." 8px below.
- **Section heading**: centred Noto Sans 32px / 600, #363636 on white or rgba(0,0,0,0.7) on the light band, 24px margin-bottom.
- **Light band** (`hero is-light`): full-bleed #f5f5f5 strip with no border, separating the dataset instructions and video from the white sections.
- **Numbered instructions**: Bulma `.content ol` with a nested `ul`, 16px, 32px indent, 4px item spacing.
- **Video embed** (`.publication-video`): 16:9, radius 10px, overflow hidden; an italic 14px centred note below.
- **BibTeX**: left-aligned 28px heading, #f5f5f5 pre, 14px monospace, padding 17.5px 21px, horizontal scroll for long author lines.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / authors / affiliations | yes | Google Sans hero, sky-blue links |
| Venue | absent from the source | no venue line in the hero; CHI '26 appears only in the BibTeX |
| Link buttons | yes | six dark Bulma pills in one row |
| Teaser + caption | yes | three-panel figure, italic centred caption |
| Abstract | yes | 763px justified column |
| Dataset viewer instructions | yes | gray band with numbered list |
| Video | yes | YouTube embed with 10px radius, in the gray band |
| Results carousel | present but non-standard | template carousel is commented out in the markup |
| Results tables | absent from the source | none |
| BibTeX | yes | gray pre |
| Footer | yes | #fafafa with license and source-code credit |

## Adapting to Other Content

- **More authors**: keep the Google Sans 20px line of #209cee links; at 960px about six names fit per line. Put all affiliations on one 20px #4a4a4a line with superscripts, wrapping if needed.
- **A results table**: Bulma `.table` inside a four-fifths column (763px), 16px Noto Sans, header 600 #363636, Bulma 1px rules; put it in a `hero is-light` band if it belongs with the dataset material.
- **Long publication or news lists**: a `.content ul` in the 763px column, 16px, 4px spacing, dates bold.
- **A venue or award line**: add a Google Sans 20px #4a4a4a line under the affiliations; the template's unused `.publication-awards` rule gives bold #ff3860 if an award must stand out.
- **More media**: alternate white `.section` blocks and #f5f5f5 `hero is-light` bands to group related material.

## Do's and Don'ts

- Do keep the hero in Google Sans and the body in Noto Sans.
- Do use the full-width #f5f5f5 band to set off supplementary material.
- Do keep figures unframed and captions italic and centred.
- Do keep author links #209cee and buttons #363636.
- Don't add colors to the chrome; teal and magenta stay inside the figure.
- Don't widen the abstract beyond the four-fifths column.
- Don't leave a template carousel visible without content.

## Surfaces

White page, one full-width #f5f5f5 band for the dataset section, #f5f5f5 BibTeX block, #fafafa footer. No shadows anywhere; the only rounded element is the 10px video.

## Imagery

A line-drawn three-panel teaser of hands gesturing at block grids with monospace speech bubbles (green and red highlights), outlined in teal, magenta and gray, plus a small 3D red-green target tower. The example video is a gray 3D viewer with a hand model, form fields and burned-in captions.

## Layout

Centred 960px hero, full-width teaser at 912px, then 763px reading columns for text and video, with one full-bleed gray band in the middle. The page is short: four sections after the teaser.

## Agent Prompt Guide

Quick colors: background #ffffff, headings and buttons #363636, body #4a4a4a, author links #209cee, band #f5f5f5 with rgba(0,0,0,0.7) text, footer #fafafa.

1. "Build a centred hero in a 960px column with 48px 24px padding: title Google Sans 48px / 600, line-height 1.125, #363636; authors Google Sans 20px #209cee links with #4a4a4a superscripts; affiliations one 20px #4a4a4a line; six buttons with #363636 fill, white 16px Noto Sans, padding 7px 20px, fully rounded, icons left."
2. "Add a teaser section with padding 0 24px 48px: full-width unframed figure, then a centred Google Sans 16px italic #4a4a4a caption starting 'Figure 1.' 8px below."
3. "Make a full-width #f5f5f5 band (Bulma hero is-light, section padding 48px 24px) with a 763px centred column: 32px / 600 heading in rgba(0,0,0,0.7), justified 16px text, a numbered list indented 32px, then a 16:9 video embed with radius 10px and a 14px italic centred note."

## Similar Pages

- Nerfies-template project pages with a single gray hero-is-light band for supplementary material.
- Cognitive-science and HCI pages with dataset viewer instructions and a replay video.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --heading: #363636;
  --text: #4a4a4a;
  --author-link: #209cee;
  --link: #3273dc;
  --band-bg: #f5f5f5;
  --band-text: rgba(0, 0, 0, 0.7);
  --footer-bg: #fafafa;
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --container: 960px;
  --text-column: 763px;
  --video-radius: 10px;
}
```

## Provenance

- **URL**: https://multimodal-conventions.github.io/
- **Paper**: Gesturing Toward Abstraction: Multimodal Convention Formation in Collaborative Physical Tasks (arXiv 2602.08914), Kiyosu Maeda, William P. McCarthy, Ching-Yi Tsai, Jeffrey Mu, Haoliang Wang, Robert D. Hawkins, Judith E. Fan, Parastoo Abtahi.
- **Venue**: CHI 2026.
- **Selection reason**: the arXiv comment states acceptance at CHI 2026; the project page is linked in the paper body (arXiv HTML).
- **Template credit**: Nerfies template on Bulma 0.9; footer states a Creative Commons license and links the source code.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of the teaser caption, light band, list, video and footer, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
