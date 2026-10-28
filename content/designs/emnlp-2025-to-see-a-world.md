# NeuroMerging — Style Reference

> A sunburst of pastel bars blooming around one italic purple word: the results chart is the cover, and a plain academic page grows out of it.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, the page's `bulma.min.css`, `index.css` and `index.html`, and a browser probe at 1440px of the abstract text, figure caption, notes, help line and footer. The page is the Academic Project Page Template (Nerfies-derived Bulma). Google Sans does load here (`fonts_loaded`: Google Sans 400, Noto Sans 400), so the title and authors render in it. The signature graphic, a radial bar chart with "NeuroMerging" set in its centre, is a PNG (`intro_result.png`), not live markup.

## Overview

A white, centred Bulma page with no navbar. The hero opens straight at the top with a three-line 48px Google Sans title in charcoal, two lines of sky-blue author links with superscripts, two lines of affiliations, two small footnotes, "Published at EMNLP 2025." with a blue link, and five charcoal pill buttons (arXiv, Official, Presentation, Code, Citation). Directly beneath, the teaser fills 80% of the hero column: a radial bar chart whose bars, in purple, peach, mint, sage, lilac and slate pastels, fan around the method name in bold italic purple, with a legend below. A full-width #f5f5f5 band holds the Abstract in a narrow justified column. Then the colour-coded method figure (orange, gold and green dashed panels) with a 20px caption, a grey Poster band with an embedded PDF, a BibTeX section with a soft copy button and rounded code box, and a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 83.2%, pale blue-grey #ccdbdf 4.3% (light teaser bars), grey-lilac #ada7ae 3.8% (antialiased text and bars), dark slate #4f4d5b 3.7% (title, buttons and bar labels), peach #f1e8e4 2.3% (teaser bars), #f8fafa 2.0%, #fdfffe 0.6%, #fffffd 0.1%.

Anatomy in DOM order (desktop 1440px; `section.hero > .hero-body` padding 48px 24px; `.container.is-max-desktop` 960px at x=240; no navbar):

1. **Title** (`h1.title.is-1.publication-title`, y=48): Google Sans 48px / 600 / 54px, #363636, centred, three lines (162px). Margin-bottom 24px.
2. **Authors** (`.publication-authors.is-size-5`, y≈236): Google Sans 20px / 400 / 30px, two centred lines of four and five names separated by em spaces; names #209cee, superscripts (1, 2,*, 3,† …) in #4a4a4a.
3. **Affiliations** (second `.publication-authors`): 20px #4a4a4a, two lines, each institution with a leading superscript number.
4. **Footnotes** (`.eql-cntrb small`, y≈379 and y≈405): 14.58px / 400 #4a4a4a, "*Corresponding authors" and "†Work conducted while at Xiamen University Malaysia", each on its own line.
5. **Venue** (`.publication-authors .is-block`, y=440): "Published at EMNLP 2025." 20px #4a4a4a with "EMNLP 2025" as a #209cee link. Margin-top 8px.
6. **Buttons** (`.publication-links`, y=488, 40px tall): five charcoal pills about 4px apart: arXiv (Academicons), Official (PDF icon), Presentation (YouTube), Code (GitHub), Citation (paper-plane).
7. **Teaser** (`section.hero.teaser`, from y=593): `.hero-body` padding 0 24px 48px; the radial chart image renders 730×796 at x=355 (inline `max-width: 80%; border-radius: 8px`), running past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma body) | page, hero, figure section, BibTeX section |
| Charcoal | #363636 | Bulma `.title`, `is-dark` | paper title, BibTeX heading, pill button fill |
| Text Grey | #4a4a4a | Bulma body | affiliations, footnotes, venue sentence, captions, footer text |
| Author Blue | #209cee | `.publication-authors a` hsl(204,86%,53%) `!important` | author names, "EMNLP 2025" link |
| Band Ink | rgba(0,0,0,0.7) | Bulma `.hero.is-light` | Abstract and Poster headings and abstract text |
| Band Grey | #f5f5f5 | Bulma `.hero.is-light` | Abstract band, Poster band |
| Charcoal Hover | #2f2f2f | Bulma `.button.is-dark:hover` | button hover fill |
| Copy Button | #eef2f7 | `.copy-icon-btn` | BibTeX copy button fill |
| Copy Icon | #1f2937 | `.copy-icon-btn` | copy icon colour |
| Code Box | #f6f8fb | `.bibtex-box` | BibTeX box background |
| Code Border | #e5e7eb | `.bibtex-box` | 1px BibTeX box border |
| Help Grey | #7a7a7a | Bulma `.has-text-grey` | "Click anywhere on the box…" help line |
| Footer Grey | #fafafa | Bulma `.footer` | footer band |
| Footer Link | #3273dc | Bulma link | footer template link |
| Focus Blue | #2563eb | `.copy-icon-btn:focus-visible` | 2px focus outline on the copy button |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title, authors, teaser | 'Google Sans', sans-serif | Google Sans 400 (600 synthesised for the title) | Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 | Noto Sans |
| Code | Bulma `is-family-monospace` | system monospace | JetBrains Mono |
| Math | MathJax 3 | MJXTEX fonts | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 54px | #363636 |
| Authors, affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px | names #209cee, text #4a4a4a |
| Footnotes | `.eql-cntrb small` | 14.58px / 400 / 21.9px | #4a4a4a |
| Venue sentence | `.publication-authors .is-block` | 20px / 400 | #4a4a4a, link #209cee |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| Section heading | `h2.title.is-3` | 32px / 600 / 36px, margin-bottom 24px | rgba(0,0,0,0.7) in bands, #363636 on white |
| Abstract | `.hero.is-light .content p` | 16px / 400 / 24px, justified | rgba(0,0,0,0.7) |
| Figure caption | `h3.subtitle.has-text-centered` | 20px / 400 / 25px, margin-top 12px | #4a4a4a |
| Caption detail | `.content.is-size-6` | 16px / 400 / 20px, centred | #4a4a4a |
| Help line | `p.help.is-size-7` | 12px italic | #7a7a7a |
| BibTeX | `pre.bibtex-box` | 14px / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill buttons | 290486px | 1px solid transparent | none |
| Teaser image | 8px (inline) | none | none |
| Copy button | 10px, 40×40px | none | `0 0 0 1px rgba(0,0,0,.03), 0 2px 6px rgba(0,0,0,.06)`; hover `translateY(-1px)` and `0 4px 12px rgba(0,0,0,.10)`; copied state `linear-gradient(180deg, #c9f7b5 0%, #8feb77 100%)` with `0 0 0 1px rgba(16,185,129,.25), 0 6px 14px rgba(16,185,129,.35)` |
| BibTeX box | 12px, padding 17.5px 21px | 1px solid #e5e7eb | `0 1px 1px rgba(0,0,0,.02), 0 2px 8px rgba(0,0,0,.03)`; hover `0 3px 14px rgba(0,0,0,.06)` |
| Method figure | 0 | none (the dashed panel borders are drawn in the PNG) | none |
| Poster iframe | 0 | none | none |

## Layout Metrics

- **Hero**: `.hero-body` padding 48px 24px; `.container.is-max-desktop` 960px at x=240; the title starts at y=48 because there is no navbar. Hero section 0–593px.
- **Teaser**: `section.hero.teaser > .hero-body` padding 0 24px 48px; image at 80% of the 960px column (730px wide, 796px tall).
- **Abstract band**: `section.section.hero.is-light` padding 48px 24px, #f5f5f5; `.column.is-four-fifths` inside the 960px container gives a 763px justified column at x=338; band 540px tall.
- **Method figure**: `section.hero.is-small.mt-5.mb-5` (24px margins, Bulma is-small body padding 24px); Bulma container 1344px; image 1230px wide; caption 12px below.
- **Poster band**: `section.hero.is-small.is-light`, padding 24px, iframe 100% × 550px (1344px wide).
- **BibTeX**: `section.section` padding 48px 24px, 960px container; heading row with the copy button 8px to the right; help line margin 4px 0 12px.
- **Footer**: Bulma `.footer` #fafafa, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 renders this) | hero 960px column; figure container 1344px | 16px | 48px | — |
| 1216–1407px | figure container 1152px | 16px | 48px | — |
| 1024–1215px | figure container 960px | 16px | 48px | — |
| 769–1023px | 24px section padding | 16px | 48px | `is-max-desktop` container becomes fluid with 24px padding |
| ≤768px | 24px | 16px | 48px (Bulma `is-1` does not shrink) | Bulma columns stack; four-fifths column full width |

## Components

- **Charcoal pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, #ffffff 16px / 400 Noto Sans, padding 7px 20px, 40px tall, radius 290486px, leading Font Awesome or Academicons icon in a 24px `.icon` span; hover #2f2f2f.
- **Signature teaser**: a radial bar chart image at 80% of the hero column with 8px corners; method bars in a saturated purple, baselines in pastel peach, mint, sage, lilac and slate; the method name sits in the centre in bold italic purple; legend in two rows underneath. No frame or shadow.
- **Grey abstract band**: full-width #f5f5f5, 48px padding, a centred 32px / 600 "Abstract" heading in rgba(0,0,0,0.7), then a 763px column of 16px justified text; the method name in bold italic.
- **Figure with caption**: full-width method figure, then a centred 20px `h3.subtitle` lead sentence and a 16px caption block with line-height 20px.
- **Copy button** (`.copy-icon-btn`): 40×40px, #eef2f7, radius 10px, #1f2937 22px copy icon, ring-and-drop shadow; hover lifts 1px; after copying it turns into a green gradient with a check icon.
- **BibTeX box** (`pre.bibtex-box`): #f6f8fb, 1px #e5e7eb, radius 12px, padding 17.5px 21px, wrapping text, two-layer whisper shadow.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | absent from the source | page starts with the title |
| Title / authors / affiliations | yes | centred Google Sans, blue linked names |
| Footnotes | yes | two small lines for corresponding and visiting authors |
| Venue | yes | sentence "Published at EMNLP 2025." with a blue link |
| Link buttons | yes | five charcoal pills including Presentation and Citation |
| Teaser | yes | radial bar chart image with centred method name |
| Abstract | yes | grey full-width band, narrow justified column |
| Method figure | yes | colour-coded diagram with centred caption |
| Results tables | absent from the source | results appear only in the teaser chart and the paper |
| Poster | yes | grey band with an embedded PDF viewer |
| BibTeX | yes | heading with a copy icon button and a rounded code box |
| Footer | yes | #fafafa, template credit, visitor map |

## Adapting to Other Content

- **A results table**: put it in a white `section.section` after the method figure inside the 960px container; Bulma `table is-striped is-fullwidth` at 16px, best values bold #363636; leave colour to the charts.
- **A different teaser**: keep the 80%-width centred image with 8px radius; a single strong data graphic works better here than a photo collage.
- **More authors**: keep two or three centred 20px lines separated by em spaces, with footnote lines at 14.58px.
- **Video**: use the template's `.publication-video` (16:9, radius 10px) in its own section between the teaser and the abstract.
- **News**: a short list in the 763px column of a white section, dates bold, at 16px.

## Do's and Don'ts

- Do let the teaser chart carry the identity; a memorable data graphic at the top replaces a photo or diagram.
- Do keep the hero entirely centred and the buttons charcoal pills.
- Do alternate a full-width #f5f5f5 band for the abstract and poster with white sections.
- Do give the BibTeX a copy button with the soft #eef2f7 fill.
- Don't add a navbar; the page opens directly on the title.
- Don't introduce new accents in HTML; colour lives in the figures (purple and pastels, orange/gold/green panels).
- Don't frame the figures; they sit on white.

## Surfaces

White page, #f5f5f5 bands (Abstract, Poster), a #f6f8fb rounded BibTeX box with a hairline border, #fafafa footer. The only gradient is the green copied-state of the copy button.

## Imagery

A radial bar chart in pastel colours with a saturated purple series and the method name centred in bold italic purple; a method diagram drawn with dashed panels in burnt orange, gold and green with labelled headers, neuron illustrations and vector sketches; an embedded PDF poster.

## Layout

Centred 960px hero, an 80%-width teaser, a full-width grey abstract band, a full-container method figure, a grey poster band and a 960px BibTeX section. About 4,200px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, charcoal #363636, text #4a4a4a, author blue #209cee, band #f5f5f5, code #f6f8fb with #e5e7eb border, copy button #eef2f7 / #1f2937, footer #fafafa.

1. "Build a centred hero with no navbar (padding 48px 24px, 960px column): Google Sans 48px / 600 #363636 title; 20px author lines with #209cee names and #4a4a4a superscripts separated by em spaces; affiliations at 20px; 14.58px footnotes; 'Published at …' with a #209cee link; charcoal pill buttons (#363636, #ffffff 16px Noto Sans, padding 7px 20px, 40px tall, fully rounded, icon on the left)."
2. "Below the buttons, place one signature results chart image at 80% of the column with an 8px radius and no frame, followed by a full-width #f5f5f5 band (padding 48px 24px) containing a centred 32px / 600 rgba(0,0,0,0.7) 'Abstract' heading and a 763px column of 16px justified text."
3. "Make a BibTeX block: 32px / 600 #363636 heading with a 40×40px copy button (#eef2f7, radius 10px, #1f2937 icon, box-shadow 0 0 0 1px rgba(0,0,0,.03), 0 2px 6px rgba(0,0,0,.06)); a 12px italic #7a7a7a help line; a pre with #f6f8fb background, 1px #e5e7eb border, radius 12px, padding 17.5px 21px."

## Similar Pages

- Academic Project Page Template pages whose teaser is a single data chart.
- Model-merging and multi-task papers that summarise results as a radial or polar bar chart.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --charcoal: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --band: #f5f5f5;
  --band-ink: rgba(0, 0, 0, 0.7);
  --code-bg: #f6f8fb;
  --code-border: #e5e7eb;
  --copy-bg: #eef2f7;
  --copy-ink: #1f2937;
  --footer: #fafafa;
  --font-title: "Google Sans", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --hero-column: 960px;
  --radius-code: 12px;
}
```

## Provenance

- **URL**: https://ZzzitaoFang.github.io/projects/NeuroMerging/
- **Paper**: To See a World in a Spark of Neuron: Disentangling Multi-task Interference for Training-free Model Merging (arXiv 2503.05320), Zitao Fang, Guodong Du, Shuyang Yu, Yifei Guo, Yiwei Zhang, Yiyao Cao, Jing Li, Ho-Kin Tang, Sim Kuan Goh.
- **Venue**: EMNLP 2025.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: footer says the page was built using the Academic Project Page Template (adapted from Nerfies).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, a browser probe at 1440px, and `bulma.min.css`, `index.css` and `index.html` read directly, on 2026-10-28.
