# CSD-VAR — Style Reference

> Cotton-candy morning: a blush header, a coral-to-sky script wordmark and a little "Decompose" machine that splits one picture into what it shows and how it is painted.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, scrolled viewport shots at y=2700, 3500 and 4400, a probe of rendered elements (hero layers, decompose widget, abstract card, section headings, carousel, gallery rows, BibTeX, footer), and the page's `css/index.css` plus two inline `<style>` blocks (about 21KB) and `index.html` over Bulma. The page builds on the Marigold / Nerfies template. Two things change after load: scrolling to the widget lets a script add `.decomposed`, which widens the decompose card from 320px to 1200px and reveals the Content and Style images; and a particles.js canvas draws white dots on a fixed layer that is invisible on the white page. The `@import` of Architects Daughter sits inside a `<style>` block after other rules, so it never applies; the handwritten labels fall back to the system cursive face.

## Overview

A light, playful Nerfies-derived page (about 5,050px tall). The header sits over a looping pastel video washed with 60% white, which reads as a pink-lilac haze. A 40px Google Sans title opens with "CSD-VAR" in the Pacifico script, clipped to a coral-to-sky gradient (#ff7e7e → #7ecbff); below are an italic gray 32px venue line ("ICCV 2025, Honolulu, Hawai'i 🌺"), sky-blue author names spaced 41.6px apart, a 40px Qualcomm logo, and four near-black pill buttons. The teaser is an interactive card: "Content" in orange and "Style" in blue, written in Pacifico above a reference image, with an orange "Decompose" button that has a moving sheen. Further down are a gray rounded abstract card, then left-aligned sections whose headings use a warm brown (#7c5c45), some with emoji: a benchmark figure, the method overview, a white 32px-radius qualitative carousel, and gallery rows on a pink-to-blue vertical gradient where "Switti" and "Infinity" tags sit in yellow on black. A plain gray BibTeX block and a #fafafa template-credit footer close the page.

## First Viewport

Color share (quantized 1440×900 shot): white #ffffff 46.8%; the blush header haze #ffedef 25.7% (plus #fff0f0 6.4%, #fcf0f2 4.7%, #fff9f8 3.8%); #b8acba 9.8% is the lilac cat reference image; the pale blue end of the decompose card is #f5fbfe 2.2%.

Anatomy in DOM order (desktop 1440px, centred; Bulma containers are forced to max-width 1350px, x=45 to 1395):

1. **Header** (`section.hero`, 0–382px): layered `.video-bg-container` (autoplay pastel video, object-fit cover) under `.video-bg-overlay` rgba(255,255,255,0.6). The declared `linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)` loses to an earlier `background: none !important`, so the video carries the color.
2. **Title** (`h1.title.is-2.publication-title`, y=16–109): Google Sans 40px/600 (only 400 loads, so the bold is synthesized), line-height 1.125, #222222, two lines. "CSD-VAR" is a `span.csd-var-gradient` in Pacifico, letter-spacing 0.03em, filled with `linear-gradient(90deg, #ff7e7e 0%, #7ecbff 100%)`. Gap 24px.
3. **Venue** (`h3.title`, y=133–169): Noto Sans 32px/600 italic, #666666, with a 🌺 emoji. Gap 24px.
4. **Authors** (`.publication-authors.author-list`, y=193–224): flex, centred, wrapping, gap 2em (41.6px); Google Sans 20.8px; names #209cee, no superscripts. Gap 24px.
5. **Affiliation logo** (`img`, y=248–288): Qualcomm wordmark, 40px tall, 218px wide. Gap 30px.
6. **Buttons** (`a.pub-btn`, y=318–365): arXiv #222222, Dataset #000000 (🤗 icon), Code #24292e, BibTeX #000000; white Noto Sans 17.6px/500, padding 10.56px 24.64px, radius 35.2px (2em), gap 8.8px between icon and label, shadow `0 2px 8px rgba(0, 0, 0, 0.04)`; hover `filter: brightness(1.1)`. The header ends at y=382.
7. **Decompose widget** (`.sketch-carousel-container`, from y≈439): at load 320px wide (centred), min-height 420px, padding 5px 24px 64px, 32px radius, background `linear-gradient(90deg, #ffeaea 0%, #fff 50%, #eaf6ff 100%)`, shadow `0 2px 8px rgba(0, 0, 0, 0.04)`; headings in Pacifico 35.2px ("Content" #f36b3b, "Style" #2a7be4, "Ref" #000000); a 250px reference image with 18px radius; below, the "Decompose" button (#f36b3b, white 19.2px, padding 12px 32px, 8px radius, 40px top margin) with a skewed white sheen sweeping across every 1.8s. It crosses the fold at y≈876.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Title Ink | #222222 | (inline `.publication-title`) | page title, arXiv button, decompose arrows, gallery sketch labels |
| Venue Gray | #666666 | Bulma subtitle color | italic venue line |
| Body Gray | #4a4a4a | Bulma body | section paragraphs, BibTeX text, footer text |
| Abstract Gray | #555555 | `.abstract-section-custom .content` | abstract text |
| Abstract Title | #333333 | `.abstract-section-custom h2.title` | "Abstract" heading |
| Brown Heading | #7c5c45 | (inline style on h2) | section headings, active carousel dot |
| Author Blue | #209cee | `hsl(204, 86%, 53%)` | author names |
| Link Blue | #3273dc | Bulma link | inline links (Switti, Infinity, email), footer links |
| Wordmark Coral | #ff7e7e | (literal gradient start) | "CSD-VAR" script gradient; content glow |
| Wordmark Sky | #7ecbff | (literal gradient end) | "CSD-VAR" script gradient; style glow |
| Content Orange | #f36b3b | `.sketch-carousel-heading-content`, `#decompose-btn` | "Content" heading, Decompose button, arrow hover |
| Style Blue | #2a7be4 | `.sketch-carousel-heading-style` | "Style" heading |
| Button Black | #000000 | `.pub-btn-hf`, `.pub-btn-bibtex` | Dataset and BibTeX buttons, gallery tag background |
| GitHub Ink | #24292e | `.pub-btn-code` | Code button |
| Widget Blush | #ffeaea → #ffffff → #eaf6ff | (literal gradient) | decompose card |
| Gallery Gradient | #f2dadc → #cde1f6 | (literal, `.gallery-row`) | showcase rows |
| Abstract Card | #f6f6f6 | (literal) | abstract card background |
| Code Well | #f5f5f5 | Bulma `pre` | BibTeX block |
| Footer Gray | #fafafa | Bulma `.footer` | footer |
| Tag Yellow | #ffff00 | (literal `yellow`) | "Switti" / "Infinity" tags on black |
| Content Border | #ffb3b3 | `.gallery-img-border-content` | 3px border on content outputs; decomposed content glow |
| Style Border | #b3d1ff | `.gallery-img-border-style` | 3px border on style outputs |
| Dot Gray | #dddddd | (inline script) | inactive carousel dots |
| Key Border | #bbbbbb | `.sketch-key-btn` | 1px border of prompt key buttons in the widget |
| Content Overlay | rgba(200,40,40,0.82) | `.overlay-content` | prompt overlay on hovered content outputs |
| Style Overlay | rgba(30,80,180,0.82) | `.overlay-style` | prompt overlay on hovered style outputs |
| Hero Haze | rgba(255,255,255,0.6) | `.video-bg-overlay` | white wash over the header video |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors / teaser | 'Google Sans', sans-serif | Google Sans 400 (600 synthesized) | Product Sans → Open Sans |
| Body / headings | 'Noto Sans', sans-serif | Noto Sans 400 (600/700 synthesized) | Noto Sans |
| Script accents | "Pacifico", cursive | Pacifico 400 | Pacifico |
| Hand labels | "Architects Daughter", cursive | not loaded; system cursive (Comic Sans MS on Windows) | Architects Daughter |
| Decompose button | Bulma button stack (BlinkMacSystemFont, -apple-system, "Segoe UI", …) | Segoe UI on Windows | Inter |
| Code | monospace | Consolas on Windows | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-2.publication-title` | 2.5rem = 40px / 600 / 1.125 | #222222; "CSD-VAR" Pacifico gradient |
| Venue | `h3.title` | 2rem = 32px / 600 italic | #666666 |
| Authors | `.author-list` | 1.3em = 20.8px / 400 | #209cee |
| Button | `.pub-btn` | 1.1em = 17.6px / 500 | #ffffff |
| Widget headings | `.sketch-carousel-heading` | 2.2em = 35.2px Pacifico | #f36b3b / #2a7be4 / #000000 |
| Abstract title | `.abstract-section-custom h2.title` | 2em = 32px / 700, centred | #333333 |
| Abstract text | `.abstract-section-custom .content` | 16px / 1.6, left | #555555 |
| Section heading | `h2.title.is-3` (inline left, brown) | 32px / 600, left | #7c5c45 |
| Body | `.content p` | 16px / 400 / 1.5 | #4a4a4a |
| Gallery tag | `.gallery-label-box` | 16px hand face | #ffff00 on #000000 |
| BibTeX | `pre` | 14px / 1.5 monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pub buttons | 35.2px (2em) | none | `0 2px 8px rgba(0, 0, 0, 0.04)` |
| Decompose card | 32px | none | `0 2px 8px rgba(0, 0, 0, 0.04)` |
| Widget images | 18px | 2px transparent; decomposed glow `0 0 16px 4px #ffb3b3aa` (content) or `0 0 16px 4px #b3e0ffaa` (style), pulsing to 32px 8px | as stated |
| Decompose button | 8px | none | none; skewed sheen `linear-gradient(120deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.5) 50%, rgba(255, 255, 255, 0) 100%)` |
| Abstract card | 18px | none | `0 2px 16px 0 rgba(60, 60, 60, 0.04)` |
| Qualitative carousel | 32px | none | `0 4px 32px 0 rgba(60, 60, 60, 0.1)` |
| Gallery row | 32px | none | `0 4px 24px 0 rgba(60, 60, 60, 0.07)` |
| Gallery images | 10px | 3px #ffb3b3 or #b3d1ff | `0 2px 8px rgba(60, 60, 60, 0.07)` |
| Carousel arrows | 50%, 48px white | none | `0 2px 8px rgba(0, 0, 0, 0.067)` |
| BibTeX `pre` | 0 | none | none |

## Layout Metrics

- **Containers**: inline CSS forces `.container`, `.container.is-max-desktop` and `.container.approach-wider` to `max-width: var(--max-width, 1350px) !important`, so containers run x=45 to 1395 at 1440. Section text and headings sit in a 1075px column at x=182; the abstract card is 950px (x=245) with an 800px text block.
- **Header**: 382px tall; title top at y=16; Bulma title margin-bottom 24px; logo 40px; buttons 47px tall.
- **Teaser**: `.teaser .hero-body` padding-bottom 48px; decompose card margin-top 25px, 320px wide at rest, `min(1200px, var(--max-width, 1400px))` once decomposed (x=120 to 1320), image cards 250px with 12px gaps.
- **Sections**: abstract card margin 56px auto; `section.section` padding 48px 24px (`.pt-0` / `.pb-4` variants 0 and 16px); heading margin-bottom 24px.
- **Qualitative carousel**: 1075px wide, `aspect-ratio: 2.2/1` (489px tall), slide images padded 18px; dots below.
- **Gallery rows**: grid 1fr 2fr 2fr, gap 2vw (28.8px), padding 2vw 1vw (28.8px 14.4px), max 1200px, 2em apart; reference image max 160px; 2×2 output grids with 1vw gaps.
- **Footer**: #fafafa, padding 16px 24px 0.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1400px | 1350px containers | 16px | 40px | gallery rows 1fr 2fr 2fr |
| ≤1400px | same | 16px | 40px | gallery gaps 0.7em; gallery images 220px |
| ≤1200px | fluid | 16px | 40px | qualitative carousel aspect 1.7/1 |
| ≤1100px | fluid | abstract 16.8px | 40px | abstract card 98vw, padding 19.2px 8px |
| ≤900px | fluid | 16px | 40px | carousel aspect 1.2/1 with 18px radius; gallery stacks; sidebar nav (if enabled) hidden |
| ≤600px | fluid | 16px | 40px | carousel aspect 1/1.2, 12px radius |

## Components

- **Script wordmark** (`.csd-var-gradient`): Pacifico at the title size, letter-spacing 0.03em, `background: linear-gradient(90deg, #ff7e7e 0%, #7ecbff 100%)` clipped to text.
- **Pub button** (`.pub-btn`): inline-flex, gap 0.5em, padding 0.6em 1.4em, 2em radius, 17.6px/500 white on a near-black that differs per button (#222222, #000000, #24292e), Font Awesome / emoji icon left, faint shadow, brightness hover.
- **Decompose widget**: blush-to-white-to-ice gradient card with Pacifico headings and arrow buttons (#222222, hover #f36b3b) that switch examples; key-word buttons (`.sketch-key-btn`, 1px #bbbbbb, 6px radius) pick prompts; the orange Decompose button expands the card and reveals the content and style images with pulsing coral and sky glows.
- **Abstract card**: #f6f6f6, 18px radius, padding 40px 35.2px 35.2px, centred 32px/700 #333333 title, left-aligned 16px/1.6 #555555 text with bold key contributions.
- **Section heading**: Noto Sans 32px/600 #7c5c45, left-aligned, sometimes led by an emoji (📈, 🖼️).
- **Qualitative carousel**: white card, 32px radius, deep soft shadow, full-bleed comparison images; 48px white round arrows with ← → glyphs; dots #dddddd with the active one #7c5c45.
- **Gallery row**: `linear-gradient(to bottom, #f2dadc, #cde1f6)`, 32px radius; a reference image with a hand-lettered "Ref" label, then two 2×2 grids of outputs with 10px radius and coral or sky 3px borders; a black tag with yellow text names the backbone; hovering an image shows the prompt over rgba(200, 40, 40, 0.82) (content) or rgba(30, 80, 180, 0.82) (style).
- **BibTeX**: Bulma `pre` (#f5f5f5, padding 17.5px 21px, 14px monospace) spanning the 1350px container, after a contact line.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Video-background header | yes | pastel looping video under a 60% white wash |
| Title / venue / authors | yes | gradient script wordmark, italic gray venue with emoji, blue names |
| Affiliation | present but non-standard | a Qualcomm logo image instead of text |
| Link buttons | yes | four near-black pills |
| Interactive teaser | yes | Decompose widget with Pacifico headings |
| Abstract | yes | gray rounded card |
| Dataset / method figures | yes | full-width figures under brown headings |
| Qualitative carousel | yes | white 32px-radius card with dots |
| Showcase gallery | yes | pink-to-blue rows with tagged 2×2 grids |
| Results tables | absent from the source | results are images |
| Sidebar navigation | present but non-standard | injected only if `config_web.json` enables it; not rendered now |
| BibTeX | yes | gray `pre` |
| Footer | yes | #fafafa Marigold / Nerfies credit |

## Adapting to Other Content

- **More authors**: the flex author list wraps at 20.8px with 41.6px gaps; past six names it forms a second centred row.
- **A results table**: put it in a white card like the qualitative carousel (32px radius, `0 4px 32px 0 rgba(60, 60, 60, 0.1)`), 16px #4a4a4a cells, header 600 #7c5c45, best values bold #f36b3b for content metrics and #2a7be4 for style metrics.
- **Long publication or news lists**: use the abstract card recipe (#f6f6f6, 18px radius) with 16px #555555 rows and 600 #7c5c45 dates.
- **More showcases**: add gallery rows; keep coral borders for content outputs and sky borders for style outputs.
- **More buttons**: add another `.pub-btn` in a near-black (#222222 or #000000); avoid colored buttons, the orange is reserved for the Decompose action.

## Do's and Don'ts

- Do pair coral/orange with content and sky/blue with style everywhere (headings, borders, glows, overlays).
- Do keep large surfaces soft: blush header, gradient cards, 18–32px radii and faint shadows.
- Do use Pacifico only for the wordmark and the widget headings.
- Do keep the buttons near-black so the pastel identity stays in the wordmark and widget.
- Don't center the section headings; after the abstract they hang left in brown.
- Don't use hard borders on cards; separation comes from radius, gradient and shadow.
- Don't rely on the hand-lettered font loading; it falls back to the system cursive.

## Surfaces

A blush video header washed with 60% white; white page; gradient cards (decompose widget horizontal blush-white-ice, gallery rows vertical pink-to-blue); a #f6f6f6 abstract card; a white floating carousel card; flat #f5f5f5 BibTeX and #fafafa footer.

## Imagery

Stylized generated images (a lilac fantasy cat, mosaic flowers and cats, hot-air balloons, seagulls in many art styles), a 25-image benchmark grid with pie charts of categories, a method diagram with token grids, and a Qualcomm logo.

## Layout

Centred header and teaser, then a centred 950px abstract card, then left-aligned sections in a 1075px column with full-width figures, carousels and gallery rows, ending with a 1350px BibTeX block.

## Agent Prompt Guide

Quick colors: ink #222222, body #4a4a4a, venue #666666, heading brown #7c5c45, authors #209cee, wordmark #ff7e7e → #7ecbff, content #f36b3b, style #2a7be4, abstract card #f6f6f6, gallery #f2dadc → #cde1f6.

1. "Build a header over a looping pastel video with a rgba(255,255,255,0.6) wash: Google Sans 40px/600 #222222 title whose acronym is in Pacifico filled with linear-gradient(90deg, #ff7e7e 0%, #7ecbff 100%); a 32px italic #666666 venue line with an emoji; flex-wrapped #209cee author names at 20.8px with 41.6px gaps; near-black pill buttons (#222222, #000000, #24292e) with white 17.6px/500 text, padding 10.56px 24.64px, radius 35.2px."
2. "Make a decompose widget: a card with linear-gradient(90deg, #ffeaea 0%, #fff 50%, #eaf6ff 100%), 32px radius, padding 5px 24px 64px; Pacifico 35.2px headings 'Content' in #f36b3b and 'Style' in #2a7be4; a 250px image with 18px radius; an orange #f36b3b button (white 19.2px, padding 12px 32px, 8px radius) with a sweeping white sheen."
3. "Create showcase rows: linear-gradient(to bottom, #f2dadc, #cde1f6), 32px radius, grid 1fr 2fr 2fr; a reference image plus two 2×2 output grids with 10px radius and 3px #ffb3b3 (content) or #b3d1ff (style) borders; small black tags with #ffff00 text; section headings 32px/600 #7c5c45 left-aligned."

## Similar Pages

- Marigold- and Nerfies-derived pages that add a playful interactive teaser.
- Style-transfer and personalization pages that color-code content versus style throughout.

## Quick Start

```css
:root {
  --ink: #222222;
  --body: #4a4a4a;
  --venue: #666666;
  --heading: #7c5c45;
  --author: #209cee;
  --content: #f36b3b;
  --style: #2a7be4;
  --wordmark: linear-gradient(90deg, #ff7e7e 0%, #7ecbff 100%);
  --widget-bg: linear-gradient(90deg, #ffeaea 0%, #fff 50%, #eaf6ff 100%);
  --gallery-bg: linear-gradient(to bottom, #f2dadc, #cde1f6);
  --abstract-bg: #f6f6f6;
  --max-width: 1350px;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --font-script: "Pacifico", cursive;
}
```

## Provenance

- **URL**: https://nqbinhcs.github.io/csd-var-page/
- **Paper**: CSD-VAR: Content-Style Decomposition in Visual Autoregressive Models (arXiv 2507.13984), Quang-Binh Nguyen, Minh Luu, Quang Nguyen, Anh Tran, Khoi Nguyen (Qualcomm AI Research).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: footer: "Website template based on Marigold, which is based on Nerfies" (CC-BY-SA 4.0); Bulma, bulma-carousel, twentytwenty, AOS, animate.css and particles.js.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, three scrolled viewport shots, a rendered-element probe, and `index.css`, the inline styles and `index.html` read directly, on 2026-10-28.
