# Hear You in Silence — Style Reference

> A lamplit study after dark: espresso-brown walls, a peach italic title like a whispered aside, and then the lights come up on warm paper.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's single inline `<style>` block and markup read directly. The page is a dark header band over a light article, so the theme is "both" in the sense of two fixed zones, not a toggle. Every `.section-block` is set to opacity 0 and translateY(30px) by a script and fades in when 10% of it enters the viewport, so blocks below the fold are invisible in a load-time capture.

## Overview

A long single-column research page (about 18,200px tall) in two moods. The top 948px is a dark brown header (`.header-wrapper`) with a 135° gradient from #2d2a26 through #4a453e to #3d3833 and two faint radial glows, one terracotta and one sage. Inside it, a 1200px two-column grid: the italic Cormorant Garamond title "Hear You in Silence" in peach #e8b4a0 and a white DM Sans subtitle span both columns; the left column holds a 2×2 grid of translucent contribution cards and a row of buttons (two filled terracotta, two ghost); the right column holds the teaser figure on a white rounded card with a deep shadow and an expanded BibTeX panel in a darkened well with mint-green code. Below, a light beige author band (#f0eeea) carries centred author names with colored symbol markers, a terracotta "CHI 2026 🏅 Honorable Mention Award" pill and colored affiliation lines. The article is a 900px column on #faf9f7: justified muted abstract paragraphs, a large figure, a Research Questions callout with a terracotta left bar, then white rounded section blocks (Video Preview, Design Space, Strategies, System, Evaluation, Implications) with serif headings underlined by a short terracotta bar, sage gradient "Key Insight" boxes, a strategy table with a dark header row, stat cards and quote cards. The page ends with two beige appendix bands (Links, BibTeX). There is no footer element.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): brown header family #574c43 17.2%, #4d443d 13.6%, #434039 13.2%, #2d2a26 12.4%, #4d4c44 11.9%, #39352f 9.8%, #857b73 7.4% (translucent cards and buttons over the gradient), together about 85%; light #efedec 14.4% (the white teaser image). Terracotta buttons and peach headings are too small to form clusters. The beige author band starts at y=948, just below the fold.

Anatomy in DOM order (desktop 1440px; `.header-wrapper` padding 80px 20px 60px; `.header-container` max 1200px at x=120, grid 1fr 1fr with gap 20px 60px, so each column is 570px):

1. **Title** (`.header-titles h1 em`, y=80, 54px tall): "Hear You in Silence", Cormorant Garamond 44.8px (2.8rem) / 500 italic, line-height 1.2, letter-spacing -0.896px (-0.02em), #e8b4a0, left aligned. h1 margin-bottom 20px.
2. **Subtitle** (`.header-titles h2`, y=154, 28px tall): the full paper title in DM Sans 17.6px / 400, line-height 1.6, white at opacity 0.85. `.header-titles` margin-bottom 20px plus the 20px row gap: next row at y=222.
3. **Contribution cards** (`.icon-container`, left column, y=222): 2×2 grid, 275px cards with 20px gaps, first row 230px tall, second row from y=472. Each card: Font Awesome solid icon 32px white at 0.8 opacity, then a 13.6px peach #e8b4a0 600 heading and 13.6px / 20.4px white body at 0.9 opacity. Container margin-bottom 40px plus `.header-main-row` margin-bottom 40px.
4. **Buttons** (`.button-container`, y=761, 56px tall): arXiv and Paper filled #c97c5d; Presentation and Demo ghost; gap 10px. Icon (academicons arXiv, FA file-pdf, FA YouTube) to the left of the label.
5. **Studio links** (y=839): "Studio for Narrative Spaces" (FA globe icon) and "@studiofornarrativespaces" (FA Instagram icon), 16px white at 0.9 opacity, 8px side margins.
6. **Teaser** (`.teaser-image`, right column, y=222, 570×348): radius 16px, box-shadow 0 30px 60px rgba(0,0,0,0.4).
7. **BibTeX panel** (`.header-bibtex.expanded`, y=598 to 888): rgba(0,0,0,0.3) well, radius 12px, margin-top 20px; 48px toggle row "❝ BibTeX ⌃" in 14.4px / 500 white, padding 12px 20px; code in Monaco/Menlo 12px / 19.2px #a8e6cf on #2d2a26, padding 15px 20px, bottom radius 12px; "Copy" button absolute at 10px from the bottom right. Header ends at 888 + 60px padding = 948.

Below the fold: author band (`.byline`, 948 to 1256, padding 40px 20px): author names 16px / 500 #2d2a26 at y=988; the award pill at y=1047; affiliation lines at y=1125 and below.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Espresso | #2d2a26 | --color-text | body text, article headings, header gradient start, strategy-table header row fill, BibTeX code background |
| Walnut | #4a453e | (literal) | header gradient midpoint (50%) |
| Umber | #3d3833 | (literal) | header gradient end (100%) |
| Warm Paper | #faf9f7 | --color-bg | page background behind the article |
| Linen | #f0eeea | --color-bg-alt | author band, appendix bands, stat cards, even table rows, Research Questions gradient start |
| Stone | #e8e4df | (literal) | Research Questions gradient end |
| White | #ffffff | (literal) | section blocks, table, limitation cards, feedback cards; header text and button labels |
| Muted Taupe | #6b6560 | --color-text-muted | abstract paragraphs, figure captions, blockquotes |
| Terracotta | #c97c5d | --color-accent | arXiv/Paper buttons, award pill, h1 underline bar, Research Questions and blockquote left bars, stat numbers, author hover |
| Peach | #e8b4a0 | --color-accent-light | header title, contribution-card headings, user chat bubbles |
| Rust | #a65d40 | --color-accent-dark | Research Questions heading, hover fill of filled buttons and award pill |
| Sage | #7b9e89 | --color-silence | Key Insight gradient end, positive feedback-card bar, "Copied" button state |
| Pale Sage | #a8c5b3 | --color-silence-light | Key Insight gradient start, agent chat bubbles |
| Sand Rule | #d8d4cf | --color-border | table row dividers, `hr`, neutral card borders |
| Mint Code | #a8e6cf | (literal) | BibTeX code text |
| Affiliation set | #087321, #4285f4, #c41e3a, #7d0ca3, #e67e22 | (inline styles) | per-institution symbols and affiliation names (HKU green, Columbia blue, Renmin red, CityU purple, GDUT orange) |

Strategy badges use paired tints: #e8f4ec / #2d5a3d (Reflective), #e8f0f8 / #2d4a6d (Facilitative), #f8e8f4 / #6d2d5a (Empathic), #f8f0e8 / #6d4a2d (Holding), #f0f0f0 / #4d4d4d (Immediate).

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Cormorant Garamond', Georgia, serif | Cormorant Garamond 500, 500 italic, 600, 700 (Google Fonts) | EB Garamond |
| Body | 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif | DM Sans 400, 400 italic, 500, 600, 700 | Inter |
| Code | 'Monaco', 'Menlo', monospace | system monospace (Consolas on Windows) | JetBrains Mono |
| Icons | Font Awesome 6.5.1, Academicons | FA 6 Free 900, FA 6 Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Header title | `.header-titles h1 em` | 44.8px / 500 italic / 1.2, letter-spacing -0.02em | #e8b4a0 |
| Header subtitle | `.header-titles h2` | 17.6px / 400 / 1.6 | white at 0.85 |
| Card heading | `.icon-item strong` | 13.6px / 600 / 1.5 | #e8b4a0 |
| Card body | `.icon-item div` | 13.6px / 400 / 1.5 | white at 0.9 |
| Button | `.button` | 14.4px / 500 | white |
| Section heading | `.article h1` | 35.2px / 600 / 1.7 (59.84px) | #2d2a26 |
| Subsection | `.article h3` | 24px / 600 / 1.7 | #2d2a26 |
| Callout heading | `.research-questions h4` | 19.2px / 700 Cormorant | #a65d40 |
| Insight heading | `.highlight-box h4` | 20.8px Cormorant | white |
| Body | `body` | 16px / 400 / 1.7 (27.2px) | #2d2a26 |
| Abstract | `.abstract` | 16.8px / 400 / 1.7, justified | #6b6560 |
| Authors | `.author-link` | 16px / 500 | #2d2a26 |
| Affiliations | `.affiliation-link` | 15.2px / 400 | inline institution color |
| Award pill | `.venue-badge` | 16px / 600 | white |
| Caption | `figcaption` | 14.4px / 400 / 1.7, left aligned | #6b6560 |
| Blockquote | `blockquote` | 17.6px italic / 1.7 | #6b6560; cite 14.4px #c97c5d |
| Stat number | `.result-value` | 40px / 700 Cormorant | #c97c5d |
| Table | `.strategy-table` | 14.4px; th 600 | th white on #2d2a26 |
| BibTeX (header) | `.header-bibtex .bibtex` | 12px / 1.6 | #a8e6cf |
| BibTeX (appendix) | `.bibtex` | 13.6px / 1.6 | #a8e6cf |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Contribution cards | 12px | 1px rgba(255,255,255,0.1) | none; hover fill rgba(255,255,255,0.08), translateY(-2px) |
| Buttons | 8px | ghost 1px rgba(255,255,255,0.2); filled 1px #c97c5d | none; hover translateY(-2px) |
| Teaser image | 16px | none | 0 30px 60px rgba(0,0,0,0.4) |
| Header BibTeX well | 12px (code 0 0 12px 12px) | none | none |
| Copy button | 6px | 1px rgba(255,255,255,0.2) | none |
| Award pill | 30px | none | none; hover scale(1.02) |
| Section blocks | 16px | none | 0 4px 30px rgba(0,0,0,0.06) |
| Figure images | 12px | none | 0 10px 40px rgba(0,0,0,0.1); hover scale(1.02) and 0 15px 50px rgba(0,0,0,0.15) |
| Video container | 12px | none | 0 10px 40px rgba(0,0,0,0.15) |
| Research Questions | 12px | 4px left #c97c5d | none |
| Limitation cards | 8px | 4px left #c97c5d | 0 2px 10px rgba(0,0,0,0.05) |
| Feedback cards | 12px | 4px left #7b9e89 (positive) or #c97c5d (negative) | 0 4px 15px rgba(0,0,0,0.08) |
| Strategy table | 12px, overflow hidden | row dividers 1px #d8d4cf | 0 4px 20px rgba(0,0,0,0.08) |
| Strategy badges | 20px | none | none |
| Section h1 underline | 2px | 60×3px #c97c5d bar at bottom left | none |

## Layout Metrics

- **Header**: `.header-wrapper` padding 80px 20px 60px; `.header-container` max-width 1200px (x=120 to 1320 at 1440), grid 1fr 1fr, gap 20px row / 60px column. Title block spans both columns. Rendered header height 948px.
- **Header gradient**: `background: linear-gradient(135deg, #2d2a26 0%, #4a453e 50%, #3d3833 100%)`, with `::before` overlay `radial-gradient(circle at 20% 80%, rgba(201, 124, 93, 0.15) 0%, transparent 50%), radial-gradient(circle at 80% 20%, rgba(123, 158, 137, 0.15) 0%, transparent 50%)`.
- **Contribution grid**: 2 columns, gap 20px, card padding 20px, icon-to-text gap 15px.
- **Author band**: padding 40px 20px, centred, inner max 1200px; paragraphs margin-bottom 15px; award pill margin 15px 0; affiliation rows margin-top 20px and 10px.
- **Article**: `.article` max-width 900px, padding 60px 20px, so text runs 860px from x=290. Section blocks fill 860px with 50px padding (inner text 760px from x=340), margin 40px 0.
- **Figures**: margin 40px 0, image max-width 100% (860px at top level, 760px inside blocks); caption 15px below with 20px side padding.
- **Grids**: stat cards `repeat(auto-fit, minmax(250px, 1fr))` gap 25px (two 368px cards per row in a block); feedback cards minmax(280px, 1fr) gap 20px; pacing demo cards flex with gap 30px.
- **Appendix bands**: #f0eeea, padding 50px 20px, inner max 900px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px (base) | header 20px, article 20px + 50px block padding | 16px | 44.8px | header 2 columns, contribution cards 2×2 |
| ≤900px | same | 16px | 44.8px | header 1 column (gap 30px 20px); contribution cards 1 column; block padding 30px 20px |
| ≤768px | header 40px 15px 30px; article 30px 15px | 15px, line-height 1.6 | 32px; subtitle 16px | buttons stack full width (padding 14px 20px, 15.2px); authors and affiliations one per line; section h1 28.8px; h3 20.8px; paragraphs left aligned; block padding 25px 15px, radius 12px; stat cards 2 columns; feedback 1 column |
| ≤480px | header 30px 10px 20px; article 20px 10px | 15px | 25.6px; subtitle 14.4px | section h1 24px; h3 17.6px; stat cards 1 column; block padding 18px 10px |

## Components

- **Contribution card** (`.icon-item`): flex row, gap 15px, padding 20px, background rgba(255,255,255,0.05), 1px rgba(255,255,255,0.1) border, radius 12px. Left: FA solid icon at 32px, white, opacity 0.8. Right: heading 13.6px / 600 #e8b4a0 (display block, 4px below), body 13.6px / 1.5 white at 0.9. Hover: background rgba(255,255,255,0.08), translateY(-2px), 0.3s cubic-bezier(0.4, 0, 0.2, 1).
- **Filled button** (`.button.paper-link`): inline-flex, gap 8px, padding 12px 24px, #c97c5d fill and 1px border, radius 8px, white 14.4px / 500, icon 17.6px on the left. Hover: #a65d40, translateY(-2px).
- **Ghost button** (`.button`): same geometry, background rgba(255,255,255,0.1), border 1px rgba(255,255,255,0.2). Hover: background rgba(255,255,255,0.2), translateY(-2px).
- **Header BibTeX** (`.header-bibtex`): rgba(0,0,0,0.3) container, radius 12px, collapsible; toggle row with a quote-left icon, "BibTeX" and a right-aligned chevron that rotates 180° when expanded; code #a8e6cf on #2d2a26 in 12px Monaco/Menlo, max-height 300px; Copy button rgba(255,255,255,0.15), 1px rgba(255,255,255,0.2) border, 6px radius, 12.8px, turns #7b9e89 with "Copied!" for 2s.
- **Award pill** (`.venue-badge`): inline-block, #c97c5d, white 16px / 600, padding 8px 20px, radius 30px, margin 15px 0. Hover #a65d40, scale(1.02).
- **Author line**: names as `.author-link` 16px / 500 #2d2a26 with 8px side margins and superscript colored symbols (♠ ♣ ♦ ♥ ▲); hover #c97c5d. Affiliations repeat the symbol and set the name in the same institution color, separated by em spaces.
- **Section block** (`.section-block`): white, radius 16px, padding 50px, margin 40px 0, shadow 0 4px 30px rgba(0,0,0,0.06); fades in from translateY(30px) over 0.6s.
- **Section heading** (`.article h1`): Cormorant Garamond 35.2px / 600 #2d2a26, padding-bottom 15px, margin-bottom 30px, with a 60×3px #c97c5d bar (radius 2px) at bottom left.
- **Research Questions callout** (`.research-questions`): background linear-gradient(135deg, #f0eeea 0%, #e8e4df 100%), 4px left #c97c5d bar, radius 12px, padding 25px 30px; heading Cormorant 19.2px / 700 #a65d40; RQ paragraphs left aligned with bold "RQ1:" leads.
- **Key Insight box** (`.highlight-box`): background linear-gradient(135deg, #a8c5b3 0%, #7b9e89 100%), white text, radius 12px, padding 25px; Cormorant heading 20.8px.
- **Stat card** (`.result-card`): #f0eeea, radius 12px, padding 25px, centred; number Cormorant 40px / 700 #c97c5d; label 14.4px #6b6560. Hover translateY(-5px), shadow 0 10px 30px rgba(0,0,0,0.1).
- **Strategy table**: white, radius 12px, shadow 0 4px 20px rgba(0,0,0,0.08); header cells white 600 on #2d2a26, padding 15px; body cells padding 12px 15px, 1px #d8d4cf dividers, even rows #f0eeea; strategy names as tinted pills (radius 20px, 12.8px / 600, padding 4px 12px).
- **Blockquote**: 4px left #c97c5d, padding-left 25px, 17.6px italic #6b6560; cite 14.4px #c97c5d upright.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title / subtitle | yes | peach italic serif short title above a white sans full title, left aligned on the dark band |
| Contribution highlights | yes | 2×2 translucent cards with FA icons beside the button row |
| Link buttons | yes | two filled terracotta + two ghost buttons |
| Teaser | yes | in the header right column, white image card with deep shadow |
| BibTeX | yes | expanded panel under the teaser, repeated in a beige appendix band at the bottom |
| Authors / affiliations | yes | separate beige band below the header, colored symbol markers |
| Venue / award | yes | terracotta pill "CHI 2026 🏅 Honorable Mention Award" in the author band |
| Abstract | present but non-standard | no heading; two muted justified paragraphs around Figure 1 |
| Research questions | yes | gradient callout with terracotta bar |
| Video | yes | "Video Preview" block with a 760px video, 12px radius |
| Results | yes | stat cards, a strategy table, feedback quote cards |
| Table of contents / nav bar | absent from the source | none |
| Footer | absent from the source | page ends with the BibTeX appendix band |

## Adapting to Other Content

- **More authors**: keep one centred 16px / 500 line in the beige band and let it wrap within 1200px; give each new institution its own symbol and color, applied to both the superscript and the affiliation name.
- **A results table**: reuse the strategy table: white, 12px radius, header row white 600 on #2d2a26 at 14.4px, 12px 15px cells, #d8d4cf dividers, even rows #f0eeea; best values in #c97c5d 600.
- **More stats**: add `.result-card`s; at 1440 a 760px block fits two 368px cards per row (minmax 250px), numbers 40px Cormorant #c97c5d.
- **Long publication or news lists**: use the limitation-card pattern (white, 8px radius, 4px #c97c5d left bar, padding 20px, 15px apart) with the date as a 16px / 600 #a65d40 lead.
- **More contributions in the header**: keep the 2-column grid of 275px cards; beyond four, move extras into a section block rather than lengthening the dark band.

## Do's and Don'ts

- Do keep the two-zone structure: dark brown header for identity, warm paper below for reading.
- Do set display text in Cormorant Garamond and everything else in DM Sans.
- Do reserve terracotta #c97c5d for actions and bars, peach #e8b4a0 for text on dark, and sage #7b9e89 for "silence" and insight content.
- Do give every section heading the 60×3px terracotta underline bar.
- Don't put white section blocks on the dark band, or translucent cards on the light page.
- Don't use pure black; the darkest value is #2d2a26.
- Don't center body paragraphs; the article justifies them at desktop and left-aligns them below 768px.

## Surfaces

Dark band: 135° brown gradient with a terracotta glow at (20%, 80%) and a sage glow at (80%, 20%), carrying translucent white cards (5% fill, 10% border) and a 30% black BibTeX well. Light zone: #faf9f7 page, #f0eeea bands and stat cards, white section blocks with soft 6% shadows, gradient callouts in beige and sage.

## Imagery

A single dense, colorful teaser (chat interface screenshots, a cartoon robot and two illustrated users, numbered strategy callouts) appears twice: in the header at 570px and as Figure 1 at 860px. Later figures are analysis diagrams and system screenshots with 12px radii and soft shadows. Icons are Font Awesome solids and brands, white on dark.

## Layout

A 1200px two-column header (text and cards left, teaser and BibTeX right), then a full-width beige author band, then a 900px article column of white blocks spaced 80px apart (40px margins), then full-width beige appendix bands. All sections stack in one column below the header.

## Agent Prompt Guide

Quick colors: header gradient #2d2a26 → #4a453e → #3d3833, page #faf9f7, band #f0eeea, text #2d2a26, muted #6b6560, accent #c97c5d, accent text on dark #e8b4a0, accent dark #a65d40, sage #7b9e89, code #a8e6cf.

1. "Build a dark header: background linear-gradient(135deg, #2d2a26 0%, #4a453e 50%, #3d3833 100%), padding 80px 20px 60px, a 1200px grid of two 1fr columns with gap 20px 60px. Title in Cormorant Garamond 44.8px / 500 italic, letter-spacing -0.02em, color #e8b4a0; subtitle DM Sans 17.6px white at 0.85 opacity. Teaser in the right column with radius 16px and shadow 0 30px 60px rgba(0,0,0,0.4)."
2. "Make contribution cards and buttons: cards in a 2-column grid, gap 20px, padding 20px, background rgba(255,255,255,0.05), border 1px rgba(255,255,255,0.1), radius 12px, a 32px white icon at 0.8 opacity, heading 13.6px / 600 #e8b4a0, body 13.6px white. Buttons padding 12px 24px, radius 8px, 14.4px / 500 white; primary #c97c5d (hover #a65d40), secondary rgba(255,255,255,0.1) with 1px rgba(255,255,255,0.2) border."
3. "Create a content block: white, radius 16px, padding 50px, shadow 0 4px 30px rgba(0,0,0,0.06), inside a 900px column on #faf9f7. Heading Cormorant Garamond 35.2px / 600 #2d2a26 with a 60×3px #c97c5d bar under it. Callout: linear-gradient(135deg, #f0eeea 0%, #e8e4df 100%), 4px left #c97c5d, radius 12px, padding 25px 30px, heading 19.2px / 700 #a65d40."

## Similar Pages

- Hand-built HCI project pages with a dark hero band that holds both the teaser and the BibTeX, followed by a light article.
- Pages pairing a Garamond-style italic display face with a geometric sans body.

## Quick Start

```css
:root {
  --color-bg: #faf9f7;
  --color-bg-alt: #f0eeea;
  --color-text: #2d2a26;
  --color-text-muted: #6b6560;
  --color-accent: #c97c5d;
  --color-accent-light: #e8b4a0;
  --color-accent-dark: #a65d40;
  --color-silence: #7b9e89;
  --color-silence-light: #a8c5b3;
  --color-border: #d8d4cf;
  --code: #a8e6cf;
  --header-bg: linear-gradient(135deg, #2d2a26 0%, #4a453e 50%, #3d3833 100%);
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --max-width: 1200px;
  --article-width: 900px;
  --radius-block: 16px;
  --radius-card: 12px;
  --radius-button: 8px;
}
```

## Provenance

- **URL**: https://zhihanjiang.com/pacing/
- **Paper**: Hear You in Silence: Designing for Active Listening in Human Interaction with Conversational Agents Using Context-Aware Pacing (arXiv 2602.06134), Zhihan Jiang, Qianhui Chen, Chu Zhang, Yanheng Li, RAY LC.
- **Venue**: CHI 2026, Honorable Mention Award (as shown on the page).
- **Selection reason**: the arXiv comment states acceptance at CHI 2026 (conditionally accepted); the project page is linked in the paper body (arXiv HTML).
- **Template credit**: none stated; a custom single-file page with inline CSS, Google Fonts, Font Awesome 6.5.1 and Academicons.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted computed-style probes of header, cards, author band, section blocks and callouts, the 1440×900 and full-page screenshots, and the inline stylesheet and markup read directly, on 2026-10-28.
