# SQuadGen — Style Reference

> A clean engineering spec sheet: cool white, slate ink, one deep-teal signal, and every figure clipped into a ruled 8px card.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), a second probe of rendered elements below the fold (metric band, eyebrows, cards, flow numbers), the 1440×900 and tall screenshots, and the page's `static/css/index.css` (query `v=20260611-cdf2`) on top of Bulma. Google Sans loads only its 400 file, so every 700/800 Google Sans weight on the page is synthesised bold by Chrome.

## Overview

A modern Bulma-based project page reworked into a tidy product-style layout. Body text is Noto Sans in slate #18202a on white; headings, nav, buttons and labels are Google Sans; inline math uses Castoro. One accent family, deep teal (#0a5260 for text, #0f7c90 for links and icons), marks the "SQuadGen" brand word, the venue pill, eyebrows and metric values. The hero sits on a faint top-to-bottom wash, with a centred title, summary, teal author links and a block of dark slate buttons, then a 1360px teaser card with a large soft shadow. A four-column metrics band in cool gray follows, then sections that alternate white and #f5f7f9: a centred abstract, a two-column "why loop simplicity matters" explainer with a framed figure, three motivation cards, two idea cards with teal icon tiles, a CDF figure, a numbered four-step method flow, results figures with a colour legend and a 3D model gallery.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white and near-white family #ffffff / #f9fbfc / #fbfcfd / #f6f9f9 / #fafcfc / #fffefe together 81.6%; gray-teal #91a1a1 18.3% (the jet-coloured CDF meshes and gray wireframes inside the teaser, blended with the dark buttons). The teal accent is too small to form its own cluster.

Anatomy in DOM order (desktop 1440px, all centred):

1. **Navbar** (`nav.navbar.project-navbar`, 0–53px): #ffffff, 1px #dfe5eb bottom border, no shadow. Left "SQuadGen" (`.project-mark`) Google Sans 16px/700 #18202a at x=132; right links Abstract, Key Ideas, CDF, Method, Results, BibTeX in Google Sans 16px/400 #4a4a4a (Bulma navbar-item), padding 8px 12px, 52px tall.
2. **Hero** (`section.hero.publication-hero`, 53–1041px): `background: linear-gradient(180deg, #f8fafb 0%, #ffffff 100%)`; `.hero-body` padding-top 2.7rem = 43.2px, padding-bottom 3rem = 48px.
3. **Venue pill** (`p.venue-pill`, y=96, 194×33): "SIGGRAPH / ACM TOG 2026", Google Sans 13.12px/700 uppercase, #0a5260 on #eaf3f8, 1px #b8d7df border, radius 999px, padding 4.8px 12px. Gap 17.6px.
4. **Title** (`h1.publication-title`, y=147, two lines, max 1120px but 980px wide here): Google Sans 50.4px (clamp(2.1rem, 3.5vw, 3.25rem)) / 800 / line-height 1.04, #18202a; "SQuadGen" in `span.title-brand` #0a5260. Gap 24px.
5. **Summary** (`p.hero-summary`, y=276, max 672px): Noto Sans 17.92px/1.65, #354252, three lines. Gap 16px.
6. **Authors** (y=387): Google Sans 16px, links #0f7c90 (forced with `!important`), superscript affiliation numbers, comma separated; hover underline.
7. **Affiliations** (y=416): Google Sans 16px #5f6c7b, flex-wrapped with gap 5.6px 16px. Gap 17.6px.
8. **Buttons** (`.publication-links`, y=463 and 512, 40px tall): arXiv, Code, Data, Poster (PDF), Poster (PPTX), Slides (PPTX), Slides (PDF) on the first row, Fast-forward Video wrapping to a second row; gap 0.55rem; #1f2933 fill, no border, 6px radius, Google Sans 16px/700 white, padding 7px 16px, Font Awesome icon left.
9. **Teaser** (`figure.teaser-frame.hero-teaser-frame`, y=579, 1360×413): width min(1360px, calc(100vw − 3rem)), centred by `margin-left: 50%; transform: translateX(-50%)`; #ffffff, 1px #dfe5eb, 8px radius, padding 16px, `box-shadow: 0 22px 55px rgba(24, 32, 42, 0.11)`; image radius 4px; caption 15.2px #5f6c7b centred with a bold teal "SQuadGen".

The metrics band starts at y=1041, just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| White | #ffffff | (literal) | page, navbar, odd sections, cards, figure frames, footer |
| Ink | #18202a | --ink | body text, title, section h2, card h3 |
| Muted | #5f6c7b | --muted | affiliations, metric labels, captions, card text, footer |
| Line | #dfe5eb | --line | navbar and footer rules, metric dividers, all card and figure borders, BibTeX border |
| Soft | #f5f7f9 | --soft | metrics band, even sections |
| Soft Blue | #eaf3f8 | --soft-blue | venue pill fill |
| Pill Border | #b8d7df | (literal) | venue pill border, strong motivation card border |
| Teal | #0f7c90 | --accent | author links, body links, idea icon tiles, flow arrows |
| Deep Teal | #0a5260 | --accent-dark | brand word in title, venue pill text, eyebrows, metric values, formula titles, button hover fill, table highlights |
| Summary Slate | #354252 | (literal) | hero summary |
| Body Slate | #273340 | (literal) | abstract body, CDF copy |
| Button Slate | #1f2933 | (literal) | link buttons, "More results" button |
| Flow Slate | #26323f | (literal) | numbered method circles |
| Nav Gray | #4a4a4a | (Bulma default) | navbar links |
| Bulma Heading | #363636 | (Bulma default) | the "Simple loops make quad meshes editable" h2, which sits outside `.section-heading` |
| Hero Wash | #f8fafb | (literal) | top stop of the hero gradient |
| Code Well | #f7f9fb / #1e2935 | (literal) | BibTeX `pre` fill / text |
| Card Tint | #f8fcfd / #fbfcfd | (literal) | strong motivation card fill / idea figure well |
| Legend | #2274c7, #d97913, #d14f9a | (literal) | result legend swatches (blue, orange, pink) |
| Viewer Dark | #1a1a1a / #2f2f2f / #111111 / #bdbdbd | (literal) | 3D gallery card fill / border / label strip / label text |
| Lightbox Scrim | rgba(12, 18, 24, 0.82) | (literal) | figure lightbox overlay |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings / UI | 'Google Sans', sans-serif | Google Sans 400 only; 700/800 synthesised | Product Sans is unavailable; use Outfit 700–800 |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 | Noto Sans |
| Math inline | 'Castoro', serif | Castoro 400 | Source Serif 4 |
| Math display | MathJax SVG | rendered as SVG paths | — |
| Code | Bulma `monospace` | system monospace (Consolas on Windows) | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.publication-title` | clamp(2.1rem, 3.5vw, 3.25rem) → 50.4px / 800 / 1.04 | #18202a, brand #0a5260 |
| Section heading | `.section-heading .title.is-3` | 32px / 800 / 36px | #18202a |
| Side heading | `.title.is-3` outside `.section-heading` | 32px / 600 Noto Sans / 36px | #363636 |
| Metric value | `.metric-value` | 2rem = 32px / 800 / 1.1 | #0a5260 |
| Metric label | `.metric-label` | 0.92rem = 14.72px / 1.45 | #5f6c7b |
| Eyebrow | `.eyebrow` | 0.82rem = 13.12px / 800 uppercase, letter-spacing 0 | #0a5260 |
| Card heading | `.idea-card h3`, `.flow-step h3` | 1.1rem = 17.6px / 800 (motivation cards 1.08rem) | #18202a |
| Body | `body` | 16px / 400 / 1.65 | #18202a |
| Abstract body | `.publication-body` | 1.05rem = 16.8px | #273340 |
| Hero summary | `.hero-summary` | 1.12rem = 17.92px / 1.65 | #354252 |
| Venue pill | `.venue-pill` | 0.82rem = 13.12px / 700 uppercase | #0a5260 |
| Button | `.publication-links .button` | 16px / 700 | #ffffff |
| Caption | `.teaser-frame figcaption` | 0.95rem = 15.2px / 1.5 | #5f6c7b |
| BibTeX | `pre` | 0.9rem = 14.4px / 1.65 | #1e2935 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser frame | 8px, padding 16px | 1px #dfe5eb | `0 22px 55px rgba(24, 32, 42, 0.11)` |
| Section figures (why-loop, CDF, method, detail, result) | 8px, padding 0.75–0.9rem | 1px #dfe5eb | none |
| Idea, motivation, flow, case-study cards, legend, formula panel | 8px | 1px #dfe5eb (strong card #b8d7df) | none |
| Images inside frames | 4px | none | none |
| Idea figure well | 6px, 240px tall, padding 0.75rem | 1px #dfe5eb, fill #fbfcfd | none |
| Buttons, idea icon tiles (38px) | 6px | none | none |
| Venue pill | 999px | 1px #b8d7df | none |
| Flow numbers | 50%, 32px | none | none |
| BibTeX pre | 8px | 1px #dfe5eb | none |
| Lightbox image | 8px | none | `0 28px 80px rgba(0, 0, 0, 0.35)` over rgba(12, 18, 24, 0.82) |

## Layout Metrics

- **Containers**: Bulma `.container` (max 1344px at this width, 24px side margins) holds the navbar and footer; section content uses a 1152px column (x=144) and centred text blocks narrow to 960px (x=240) for the abstract and section headings. Hero text: `.hero-intro` max 980px; title max 1120px; summary max 42rem = 672px.
- **Hero**: padding 43.2px top, 48px bottom inside the 53px navbar; teaser margin-top 1.7rem = 27.2px, width 1360px at 1440.
- **Metrics band**: 4 columns of 288px inside the 1152px column, each `min-height: 7rem; padding: 1.2rem 1rem` (renders 19.2px 16px, 122px tall), divided by 1px #dfe5eb verticals including a left edge; 1px rules top and bottom.
- **Sections**: padding 4.8rem = 76.8px top and bottom, 24px sides; backgrounds alternate #ffffff and #f5f7f9 by `nth-of-type(even)`; section heading margin-bottom 2rem.
- **Grids**: why-loop explainer is a Bulma columns split (text 352px, figure about 760px); motivation cards 3 columns, gap 1rem; idea cards 2 columns (556px each); method flow `grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr`, gap 0.8rem; 3D gallery 4 columns, gap 0.6rem, width min(96vw, 1600px).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | 24px | 16px | 3.5vw → 42.6–50.4px | 4-column metrics, 3 motivation cards, horizontal flow |
| ≤1023px | 24px | 16px | 3.5vw, floor 33.6px | navbar burger; metrics 2×2; flow stacks with arrows rotated 90°; legend wraps; motivation cards 1 column; dataset copy 1 column |
| ≤900px | 24px | 16px | 33.6px | 3D gallery 2 columns |
| ≤640px | 24px | 16px | 2.25rem = 36px | hero padding 40px; summary 16px; buttons two per row; metrics 1 column; sections 54.4px padding |

## Components

- **Venue pill** (`.venue-pill`): inline-flex, min-height 2rem, padding 0.3rem 0.75rem, 1px #b8d7df, radius 999px, #eaf3f8, Google Sans 13.12px/700 uppercase #0a5260.
- **Dark link button** (`.publication-links .button.is-dark`): #1f2933, no border, radius 6px, padding 7px 16px, 40px tall, Google Sans 16px/700 white, Font Awesome or Academicons icon left. Hover fill #0a5260.
- **Metrics band** (`.metrics-band`): #f5f7f9 strip with 1px #dfe5eb rules; four left-aligned cells, value Google Sans 32px/800 #0a5260 ("Representation", "Editability Metric", "Large Dataset", "10x Fewer Charts"), label 14.72px #5f6c7b.
- **Eyebrow** (`.eyebrow`): Google Sans 13.12px/800 uppercase #0a5260, no letter-spacing, 5.6px above the h2.
- **Idea card** (`.idea-card`): #ffffff, 1px #dfe5eb, 8px radius, padding 16px 18.4px 20px; a 240px figure well (#fbfcfd, 6px radius) on top, a 38px #0f7c90 icon tile (6px radius, white icon), 17.6px/800 heading, #5f6c7b text.
- **Motivation card** (`.metric-motivation-card`): min-height 13rem, padding 1.15rem 1.2rem, white, 1px #dfe5eb, 8px radius; the middle "strong" card uses #f8fcfd fill and #b8d7df border.
- **Method flow** (`.method-flow`): four white 8px cards (min-height 13rem, padding 1.2rem) with a 32px #26323f number circle (Google Sans 800 white), separated by teal #0f7c90 arrow icons.
- **Result legend** (`.result-legend`): white 8px card, padding 1rem, centred row of 12px round swatches #2274c7, #d97913, #d14f9a with 14.4px #5f6c7b labels.
- **3D gallery card** (`.cdf-card`): square, #1a1a1a, 1px #2f2f2f, 8px radius, `<model-viewer>` inside, monospace 10.88px #bdbdbd label on #111111.
- **Lightbox**: clicking any figure opens it over rgba(12, 18, 24, 0.82), image radius 8px with the large black shadow, round translucent close button.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | white Bulma navbar with hairline, brand left, Google Sans links right |
| Venue badge | yes | pale-blue teal pill |
| Title / authors / affiliations | yes | centred, teal brand word, teal author links, muted affiliations |
| TL;DR / summary | yes | 17.92px slate summary under the title |
| Link buttons | yes | eight dark slate 6px buttons with icons |
| Teaser | yes | 1360px white card, 16px padding, large soft shadow |
| Stats | yes | four-column metrics band with teal values |
| Abstract | yes | centred heading, justified 16.8px body |
| Explainer / key ideas | yes | two-column text + framed figure; three motivation cards; two idea cards |
| Method | yes | framed figure and numbered four-step flow |
| Results | yes | framed figures, legend card, case study, 3D model gallery with pagination |
| Results tables | present but non-standard | styled `.results-table` wrapper exists in the CSS; results are mainly figures |
| Video | present but non-standard | "Fast-forward Video" link button only |
| BibTeX | yes | #f7f9fb pre with 8px radius and hairline |
| Footer | yes | white, 1px top rule, muted "SQuadGen Project Page, 2026" |

## Adapting to Other Content

- **More authors**: keep teal 16px Google Sans links with superscripts in one centred line; at more than eight names let them wrap within the 980px hero column, affiliations staying a single #5f6c7b flex row.
- **A results table**: use the existing `.results-table-wrapper` (white, 1px #dfe5eb, 8px radius); th Google Sans 14.4px #18202a, 1px #dfe5eb cell rules, best values `<strong>` in #0a5260.
- **More metrics**: keep the band at four cells per row (288px each at 1440); a fifth metric goes in a second band row rather than squeezing the cells.
- **Long publication or news lists**: put each entry in an 8px white card with 1px #dfe5eb, a 13.12px/800 uppercase #0a5260 eyebrow date, and #5f6c7b text, stacked with 1rem gaps inside a #f5f7f9 section.

## Do's and Don'ts

- Do keep teal for identity only: brand word, pill, eyebrows, metric values, links and icon tiles.
- Do put every figure in a white 8px card with a 1px #dfe5eb border; only the teaser gets a shadow.
- Do alternate #ffffff and #f5f7f9 section bands at 76.8px vertical padding.
- Do use dark slate #1f2933 for all link buttons, turning #0a5260 on hover.
- Don't use colored section backgrounds or gradients beyond the faint hero wash.
- Don't add letter-spacing to eyebrows; they are uppercase at 0 tracking.
- Don't round cards beyond 8px or buttons beyond 6px.

## Surfaces

White page and cards, cool gray #f5f7f9 bands for the metrics strip and every second section, a faint `linear-gradient(180deg, #f8fafb 0%, #ffffff 100%)` behind the hero, #f7f9fb BibTeX well, and dark #1a1a1a cards only inside the 3D model gallery.

## Imagery

Technical renderings of quad meshes: jet-coloured distance fields on CAD parts and characters, gray wireframe meshes, and diagrams of face loops with teal highlights. Figures are wide and light, always inside white 8px frames with 4px-rounded images; the 3D gallery shows interactive models on dark tiles.

## Layout

Centred hero with a full-width 1360px teaser, a 1152px content column below, and centred 960px text blocks for the abstract and section intros. Sections alternate white and gray at 76.8px padding, using two-column splits, three- and two-card rows, and a horizontal four-step flow. About 11,500px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, band #f5f7f9, ink #18202a, muted #5f6c7b, line #dfe5eb, accent #0a5260 (link #0f7c90), pill #eaf3f8 / #b8d7df, buttons #1f2933.

1. "Build a centred hero on linear-gradient(180deg, #f8fafb 0%, #ffffff 100%): a pill (#eaf3f8, 1px #b8d7df, radius 999px, padding 0.3rem 0.75rem, Google Sans 13.12px/700 uppercase #0a5260), a Google Sans title at 50.4px/800, line-height 1.04, #18202a with the method name in #0a5260, a 17.92px #354252 summary capped at 672px, and #0f7c90 author links."
2. "Make link buttons: #1f2933, no border, radius 6px, padding 7px 16px, Google Sans 16px/700 white with a left icon, gap 0.55rem, centred and wrapping; hover background #0a5260."
3. "Create a metrics band: full-width #f5f7f9 strip with 1px #dfe5eb top and bottom rules, four 288px cells separated by 1px #dfe5eb verticals, padding 1.2rem 1rem, value Google Sans 32px/800 #0a5260, label 14.72px #5f6c7b."

## Similar Pages

- Bulma "Nerfies"-template project pages that have been restyled with a custom accent, metrics band and card system.
- Geometry-processing project pages that put every figure in a ruled white card on alternating gray bands.

## Quick Start

```css
:root {
  --ink: #18202a;
  --muted: #5f6c7b;
  --line: #dfe5eb;
  --soft: #f5f7f9;
  --soft-blue: #eaf3f8;
  --accent: #0f7c90;
  --accent-dark: #0a5260;
  --button: #1f2933;
  --font-head: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-card: 8px;
  --radius-button: 6px;
  --shadow-teaser: 0 22px 55px rgba(24, 32, 42, 0.11);
  --section-pad: 4.8rem;
}
```

## Provenance

- **URL**: https://microsoft.github.io/SQuadGen/ (youkang-kong.github.io/squadgen/ meta-refreshes here)
- **Paper**: SQuadGen: Generating Simple Quad Layouts via Chart Distance Fields (arXiv 2604.27329), Youkang Kong, Yang Liu, Yue Dong, Xin Tong, Heung-Yeung Shum.
- **Venue**: SIGGRAPH 2026 (ACM TOG, Journal Track).
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 (Journal Track) without an explicit acceptance word and links the project page.
- **Template credit**: built on the Bulma-based Nerfies project-page template (Bulma, bulma-carousel, bulma-slider, Font Awesome, Academicons), heavily restyled in `index.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), an additional computed-style probe of below-the-fold elements, the 1440×900 and tall screenshots, and `index.css` and `index.html` read directly, on 2026-10-28.
