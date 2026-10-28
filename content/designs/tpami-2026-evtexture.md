# EvTexture++ — Style Reference

> Morning light on a lab bench: a mint-to-cream wash, two soft blue venue chips, and a row of charcoal pills before the footage starts rolling.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `static/css/index.css` read with `index.html`. The base is the Academic Project Page Template (Bulma 0.9, bulma-carousel, bulma-slider, Font Awesome 5, Academicons). Where Bulma wins the cascade the rendered value is given: the abstract sits in a `.hero.is-light` band, so the custom `.section:not(.hero) .content.has-text-justified` size (17.28px) does not reach it and it renders at 16px rgba(0,0,0,0.7). The custom sheet also declares publication cards and venue pills (`.publication-card`, `.venue-pill`) that no element on the page uses. There is no dark mode.

## Overview

A long (9,271px) video-heavy project page. The header is a 535px band with `linear-gradient(135deg, rgba(236,248,246,0.9), rgba(247,249,252,0.95) 48%, rgba(255,248,226,0.82))` over #f7fafc, a mint-to-cream wash closed by a 1px #e5edf2 rule. It centres two pale pill chips (IEEE TPAMI 2026 in info blue, ICML 2024 in link blue), a 48px Google Sans title in deep ink #15202b, a grey subtitle that names the journal extension with "EvTexture" in teal #1f6f68 bold, sky-blue author names #209cee, notes and affiliations, and three charcoal pill buttons. A full-width carousel of 1280×720 demo videos with round white arrows and black dot pagination follows on white. The abstract sits in a #f5f5f5 band at 16px grey, justified in a 763px column. Then come the Motivation comparison figure (1344px) with a justified caption, VSR comparison figures and result tables rendered as images, a second qualitative carousel, a grey BibTeX block and a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): header wash #f3f9fa 17.9%, #f5fafb 13.4%, #faf8f1 13.2%, #faf9f5 8.6% (mint at the left, cream at the right); white #ffffff 15.9% (the Video Demos section); sky blue #88bbef 15.0% and #c3daf3 8.1% (the sky in the first demo video); slate #586a70 8.0% (title text, buttons and the trees in the video).

Anatomy in DOM order (desktop 1440px, everything centred; the header's `.container.is-max-desktop` is 960px at x=240):

1. **Header band** (`section.hero.publication-header`, 0–535px): gradient above, `.hero-body` padding 64px 24px 52px, 1px #e5edf2 bottom border.
2. **Venue chips** (`.publication-badges`, y=64, 32px tall, gap 12.8px): "IEEE TPAMI 2026" (`tag is-info is-light`: #1d72aa on #eef6fc) and "ICML 2024" (`tag is-link is-light`: #2160c4 on #eef3fc); Google Sans 15.68px/700, padding 0 18.4px, radius 999px; margin-bottom 17.6px.
3. **Title** (`h1.publication-title.is-1`, y=114, 104px tall): Google Sans 48px/600, line-height 1.08, #15202b, two lines; margin-bottom 24px.
4. **Subtitle** (`p.publication-subtitle`, y=236): Google Sans 17.92px/400, line-height 1.55, #4d5b67, max-width 780px, two lines, "EvTexture" 700 #1f6f68; margin -4.8px auto 20px.
5. **Authors** (y=312): Google Sans 20px, line-height 30px; linked names #209cee (hsl(204,86%,53%), underline on hover), unlinked names #20242a, comma-separated with superscripts.
6. **Notes** (y=347 and below): "†Corresponding author" and the affiliations line, each a 20px `.publication-authors` block in #20242a.
7. **Buttons** (y=425, 40px tall): TPAMI (file icon), ICML (arXiv glyph), Code (GitHub icon); Bulma `is-rounded is-dark` pills with 5px vertical margins. The band ends at y=535.
8. **Video Demos** (`section.hero.is-small`, white, from y=535): h2 "Video Demos" at y=559 (24px hero-body padding), Noto Sans 32px/600 #363636; 24px below, a carousel (x=48–1392) whose current item holds a 1280×720 video starting at y=644.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Header Base | #f7fafc | (literal) | header band background under the gradient |
| Mint Wash | rgba(236,248,246,0.9) | (literal) | header gradient start |
| Mid Wash | rgba(247,249,252,0.95) | (literal) | header gradient middle (48%) |
| Cream Wash | rgba(255,248,226,0.82) | (literal) | header gradient end |
| Header Rule | #e5edf2 | (literal) | header bottom border |
| Title Ink | #15202b | (literal) | paper title |
| Body Ink | #20242a | (body) | body text, unlinked authors, notes, affiliations, justified captions |
| Subtitle Grey | #4d5b67 | (literal) | header subtitle |
| Teal | #1f6f68 | (literal) | "EvTexture" name in the subtitle |
| Author Blue | #209cee | hsl(204, 86%, 53%) | linked author names |
| Link Blue | #2563a9 | (literal) | footer and body links |
| Info Chip Text | #1d72aa | (Bulma `is-info is-light`) | TPAMI chip text |
| Info Chip Fill | #eef6fc | (Bulma `is-info is-light`) | TPAMI chip background |
| Link Chip Text | #2160c4 | (Bulma `is-link is-light`) | ICML chip text |
| Link Chip Fill | #eef3fc | (Bulma `is-link is-light`) | ICML chip background |
| Charcoal | #363636 | (Bulma `is-dark`, `.title`) | button fill, section h2 on white |
| White | #ffffff | (literal) | Video Demos and figure section backgrounds, button text, carousel arrow buttons |
| Light Grey | #f5f5f5 | (Bulma `hero is-light`, `pre`) | Abstract band, BibTeX background |
| Abstract Ink | rgba(0,0,0,0.7) | (Bulma `.hero.is-light`) | abstract h2 and text |
| Caption Grey | #4a4a4a | (Bulma `.subtitle`, `pre`) | carousel captions, BibTeX text |
| Dot Black | #000000 | (literal) | carousel pagination dots, video letterbox |
| Footer Grey | #fafafa | (Bulma `.footer`) | footer background |
| Control Shadow | rgba(50,50,50,0.1) | (bulma-carousel) | carousel arrow and dot shadows |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / header text | 'Google Sans', sans-serif | Google Sans 400; 600/700 synthesised | Outfit |
| Body / headings | 'Noto Sans', sans-serif | Noto Sans 400; 600 synthesised | Open Sans |
| Code | monospace | system monospace (Consolas on Windows) | IBM Plex Mono |
| Icons | Font Awesome 5 (SVG), Academicons | inline SVG; Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 1.08 | #15202b |
| Venue chip | `.publication-badges .tag` | Google Sans 15.68px / 700 / 1.5 | #1d72aa or #2160c4 |
| Subtitle | `.publication-subtitle` | Google Sans 17.92px / 400 / 1.55 | #4d5b67 |
| Authors / notes | `.publication-authors` | Google Sans 20px / 400 / 1.5 | #209cee links, #20242a text |
| Section title | `h2.title.is-3` | Noto Sans 32px / 600 / 1.125, centred | #363636 (abstract rgba(0,0,0,0.7)) |
| Abstract | `.hero.is-light .content.has-text-justified` | 16px / 400 / 1.5, justified | rgba(0,0,0,0.7) |
| Figure caption | `.section:not(.hero) .content.has-text-justified` | 17.28px / 400 / 1.65, justified | #20242a |
| Carousel caption | `.results-carousel .subtitle` | 17.28px / 400 / 1.45, centred | #4a4a4a |
| Button | `.button.is-rounded.is-dark` | Noto Sans 16px / 400 | #ffffff |
| BibTeX | `pre` | 14px / 1.5 | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue chips | 999px | none | none |
| Pill buttons | 290486px (Bulma `is-rounded`) | 1px transparent | none |
| Carousel arrows | fully round, 42px | 1px #ffffff | 0 2px 5px rgba(50,50,50,0.1) |
| Pagination dots | fully round, 10px (active scaled 1.4) | none | 0 2px 5px rgba(50,50,50,0.1) |
| Header band | 0 | 1px #e5edf2 bottom | none |
| Videos and figures | 0 | none | none |
| BibTeX `pre` | 0 | none | none |

## Layout Metrics

- **Containers**: header text in `.container.is-max-desktop` (960px at x=240); figures, carousels and captions in `.container` (1344px at x=48, Bulma's ≥1408px width); the abstract in a 4/5 column (763px text at x=338).
- **Header**: 535px tall; hero-body padding 64px 24px 52px; chips→title 17.6px, title→subtitle 24px − 4.8px, subtitle→authors 20px; buttons have 5px vertical margins.
- **Sections**: `.section` padding 56px 24px (3.5rem); `hero is-small` bands (Video Demos, Abstract) use 24px (Video Demos) and 56px 24px (Abstract) as rendered.
- **Carousel**: items 1334px with 20px padding and 5px margin; demo videos render 1280×720; arrows 42px at the container edges; dots 10px with 6px gaps below.
- **Figures**: `.figure-image` full 1344px width, 16px below; result-table images full width with a 760px minimum (horizontal scroll when narrower).
- **BibTeX**: 960px, padding 17.5px 21px.
- **Footer**: padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (incl. 1440) | `.container` 1344px | 16px | 48px | header text 960px |
| 1216–1407px | `.container` 1152px | 16px | 48px | — |
| 1024–1215px | `.container` 960px | 16px | 48px | — |
| 769–1023px | fluid with 24px section padding | 16px | 48px | carousel shows one item at full width |
| ≤768px | 24px | 16px | 32.8px (`2.05rem !important`) | header padding-top 48px; subtitle 16px; Bulma columns stack; result-table images min 680px |

## Components

- **Venue chip** (`.publication-badges .tag`): Bulma light tag, Google Sans 15.68px/700, min-height 32px, padding 0 18.4px, radius 999px; info variant #1d72aa on #eef6fc, link variant #2160c4 on #eef3fc; 12.8px apart.
- **Pill button** (`.external-link.button.is-rounded.is-dark`): #363636 fill, white Noto Sans 16px, padding 7px 20px, fully rounded, 40px tall, 24px white icon box on the left (file, Academicons arXiv, GitHub); Bulma hover darkens the fill.
- **Subtitle with name**: centred 17.92px #4d5b67 sentence, max 780px, with the earlier method name in 700 #1f6f68.
- **Video carousel** (`.results-carousel`, bulma-carousel): one 16:9 video per view, 42px white round arrows with soft shadow at the left and right edges, black 10px dots below (active scaled to 14px).
- **Comparison figure**: one full-width image (crops, PSNR labels, error maps, a red dashed divider drawn in the image) followed by a justified 17.28px caption, line-height 1.65.
- **Grey abstract band**: `hero is-light` #f5f5f5 with 56px vertical padding, centred 32px title and a justified 16px rgba(0,0,0,0.7) paragraph in a 763px column.
- **BibTeX**: #f5f5f5 `pre`, 14px #4a4a4a, padding 17.5px 21px.
- **Footer**: #fafafa, centred credit with #2563a9 links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue badges | yes | two light-blue pill chips above the title |
| Title / subtitle / authors / affiliations | yes | centred on a mint-to-cream gradient band |
| Link buttons | yes | three charcoal pills with white icons |
| Teaser / demo videos | yes | full-width video carousel with arrows and dots |
| Abstract | yes | grey band, justified small text |
| Motivation figure | yes | full-width comparison image with justified caption |
| Results tables | present but non-standard | tables are images inside `.result-table` wrappers |
| Qualitative carousel | yes | second carousel with centred grey captions |
| Publication cards | absent from the source | declared in CSS (`.publication-card`, `.venue-pill`) but not used |
| BibTeX | yes | grey `pre` |
| Footer | yes | #fafafa with template credit |
| Navigation bar | absent from the source | — |

## Adapting to Other Content

- **More venues**: add `.tag` chips to the badge row (light Bulma colors, 999px radius, 12.8px gap); keep them pale, never filled.
- **More authors**: authors wrap within 960px at 20px; keep the corresponding-author note and affiliations as separate centred lines.
- **An HTML results table**: put it in a 1344px `.container` on white; header 16px/600 #363636 with a 1px #e5edf2 bottom rule, body 16px #20242a tabular numerals, best values bold; caption below at 17.28px, line-height 1.65, justified.
- **A longer abstract**: keep the grey `hero is-light` band but raise the text to 17.28px with 1.65 line-height (the size the custom sheet intends for body text) so it does not read small.
- **Related publications**: the unused `.publication-card` recipe fits here: white, 1px #dfe7ee, radius 8px, padding 21.6px, shadow 0 12px 30px rgba(24,39,75,0.06), with a #1f6f68 (journal) or #315f9d (conference) venue pill.

## Do's and Don'ts

- Do keep the header wash subtle: the mint-to-cream gradient at 82–95% alpha over #f7fafc.
- Do show venues as pale chips and links as charcoal pills; the two never swap styles.
- Do give videos and figures the full 1344px container width.
- Do use teal #1f6f68 only for the method's own name.
- Don't fill sections with color; besides the header only the abstract band (#f5f5f5) is tinted.
- Don't add borders or radii to figures and videos.
- Don't leave long text at 16px rgba(0,0,0,0.7) in the grey band if it runs past ten lines; prefer the 17.28px caption style.

## Surfaces

A mint-to-cream gradient header with a hairline bottom rule, white sections for videos and figures, one #f5f5f5 band for the abstract, a #f5f5f5 BibTeX block and a #fafafa footer.

## Imagery

Real-world driving and street videos at 1280×720 (blue sky, trees, cars), comparison figures with zoomed crops, PSNR labels and blue error maps, event-stream visualisations in magenta, and result tables saved as images. Media have square corners.

## Layout

Centred. A 960px text column in the header, then full 1344px media sections: video carousel → abstract band (763px column) → Motivation → comparisons and result tables → qualitative carousel → BibTeX (960px) → footer. Sections are separated by background changes and 56px padding.

## Agent Prompt Guide

Quick colors: header base #f7fafc with a mint-to-cream wash, title #15202b, subtitle #4d5b67, author links #209cee, method name #1f6f68, buttons #363636, abstract band #f5f5f5, body #20242a, header rule #e5edf2.

1. "Build a header band with background linear-gradient(135deg, rgba(236,248,246,0.9), rgba(247,249,252,0.95) 48%, rgba(255,248,226,0.82)), #f7fafc, padding 64px 24px 52px and a 1px #e5edf2 bottom border. Centre two venue chips (Google Sans 15.68px/700, radius 999px, padding 0 18.4px, #1d72aa on #eef6fc and #2160c4 on #eef3fc), then a Google Sans 48px/600 title with line-height 1.08 in #15202b, a 17.92px #4d5b67 subtitle (max 780px), 20px authors in #209cee, and #363636 pill buttons with white icons."
2. "Make a full-width video carousel in a 1344px container: one 16:9 video per slide, 42px round white arrows with box-shadow 0 2px 5px rgba(50,50,50,0.1) at the edges, and 10px black dots below with the active one scaled 1.4."
3. "Add an abstract band: background #f5f5f5, padding 56px 24px, a centred Noto Sans 32px/600 'Abstract' title 24px above a justified paragraph in a 763px column."

## Similar Pages

- Academic Project Page Template pages with a custom gradient header, venue chips and a video carousel.
- Journal-extension project pages that present both the conference and journal versions in the header.

## Quick Start

```css
:root {
  --header-base: #f7fafc;
  --header-wash: linear-gradient(135deg, rgba(236, 248, 246, 0.9), rgba(247, 249, 252, 0.95) 48%, rgba(255, 248, 226, 0.82));
  --header-rule: #e5edf2;
  --title: #15202b;
  --ink: #20242a;
  --subtitle: #4d5b67;
  --teal: #1f6f68;
  --author: #209cee;
  --link: #2563a9;
  --button: #363636;
  --band: #f5f5f5;
  --font-title: "Google Sans", sans-serif;
  --font-body: "Noto Sans", sans-serif;
  --text-width: 960px;
  --media-width: 1344px;
  --section-pad: 56px 24px;
}
```

## Provenance

- **URL**: https://dachunkai.github.io/evtexture-project-page/
- **Paper**: EvTexture++: Event-Driven Texture Enhancement for Video Super-Resolution, Dachun Kai, Jiayao Lu, Yueyi Zhang, Xiaoyan Sun (University of Science and Technology of China; Midea Group); journal extension of the ICML 2024 paper EvTexture.
- **Venue**: IEEE TPAMI 2026 (vol. 48, no. 6).
- **Selection reason**: found in an arXiv cs.CV listing scan; the arXiv comment reads "IEEE TPAMI 2026 ... Project page: ...", and the journal-ref gives TPAMI vol. 48, no. 6; curl returned 200 text/html.
- **Template credit**: footer reads "This page was built using the Academic Project Page Template", adopted from Nerfies; Bulma 0.9 with bulma-carousel and bulma-slider.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the header band, chips, authors, sections, carousel, pagination, figures, captions, BibTeX and footer, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
