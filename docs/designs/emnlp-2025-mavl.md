# MAVL — Style Reference

> A clean personal portfolio that opens one paper like a folder: Inter type, a blue name in the corner, and four cobalt pills under a soft grey wash.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, and the author's site-wide `style.css` (custom properties, navbar, footer), the page-level `paper-detail.css` and the inline styles of `papers/paper1.html`. The paper page lives inside the author's personal site, so the navbar and footer are the site's own. The statistics table is styled entirely by inline `style` attributes, which the render confirms.

## Overview

A modern, Inter-set page inside a personal site. A fixed 70px white navbar with a soft shadow shows "Woohyun Cho" in bold cobalt on the left and Home, About, Publications, Contact on the right. The paper header is a band with a barely visible 135deg grey-to-white gradient and a 1px bottom rule; inside, a centred 40px / 700 dark slate title on two lines, a grey author line with the site owner bolded, a cobalt "EMNLP 2025" and four cobalt pill buttons with white Font Awesome icons. Below, a 900px column holds sections whose 32px / 700 headings are underlined by a 2px grey rule: a justified 18px grey abstract with monospace-bold method names, figures set on #f9fafb padded cards with soft shadows and italic grey captions, an inline-styled statistics table with dashed row lines, and a citation box with a cobalt copy button. A dark slate footer closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 48.7%, header wash #fafbfc 11.8%, #fefefe 10.4%, #fcfdfd 10.3%, slate-blue #bbc3d4 9.9% (antialiased title, text and the cobalt buttons blended), #fbfcfc 8.4%, #fffffd 0.5%, #fffeff 0.1%. The gradient from #f9fafb to #ffffff breaks into several near-white clusters.

Anatomy in DOM order (desktop 1440px):

1. **Navbar** (`nav.navbar`, fixed, 0–70px): #ffffff with `box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px 0 rgba(0,0,0,0.06)`; `.nav-container` max 1200px (x=120), padding 16px 20px, flex space-between. Logo "Woohyun Cho" 24px / 700 #2563eb at x=140; links 16px / 500 #1f2937, 32px apart, hover #2563eb.
2. **Paper header** (`section.paper-header`, y=80 to 468): margin-top 80px (clears the fixed bar, leaving a 10px white strip), padding 60px 0, background `linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-primary) 100%)` = #f9fafb → #ffffff, 1px #e5e7eb bottom border. Content max 900px, centred.
3. **Title** (`h1.paper-title`, y=140): 40px / 700, line-height 52px (1.3), #1f2937, centred, two lines. Margin-bottom 16px.
4. **Authors** (`p.paper-authors`, y=260): 18px / 400, line-height 28.8px, #6b7280, centred; "Woohyun Cho" in `strong`. Margin-bottom 8px.
5. **Venue** (`p.paper-venue`, y=297): "EMNLP 2025", 18px / 600 #2563eb. Margin-bottom 32px.
6. **Buttons** (`.paper-links`, y=358, 50px tall): Paper, Code, 🤗 Data, BibTeX; flex, gap 16px, centred.
7. **Content** (`section.paper-content`, from y=468, padding 60px 0): first `.paper-section` (900px max, padding 0 20px, so text 860px at x=290); "Abstract" heading at y=528 with its 2px rule, abstract text from y=613 running past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cobalt | #2563eb | --primary-color | navbar logo, venue line, pill buttons, copy-citation button, nav link hover |
| Deep Blue | #1e40af | --secondary-color | button hover fill |
| Slate | #1f2937 | --text-primary | title, section headings, nav links, section text, footer background |
| Grey | #6b7280 | --text-secondary | authors, abstract text, figure captions, inline method names |
| Paper | #ffffff | --bg-primary | page, navbar, content section, gradient end |
| Wash | #f9fafb | --bg-secondary | header gradient start, figure cards, citation box, audio/demo panels |
| Rule | #e5e7eb | --border-color | header bottom border, 2px heading underlines, table header rules and dashed row lines |
| Table Head | #f3f4f6 | (inline style) | statistics table header row |
| Footer Text | #ffffff | `.footer` | footer copyright on #1f2937 |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| UI / text | 'Inter', -apple-system, BlinkMacSystemFont, sans-serif | Inter 400, 500, 600, 700 | Inter |
| Code / citation | browser monospace; `'Courier New', monospace` in `.citation-box pre` | system monospace, Courier New | JetBrains Mono |
| Icons | Font Awesome 6 | Font Awesome 6 Free 900, Brands 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.paper-title` | 2.5rem = 40px / 700 / 1.3 | #1f2937 |
| Authors | `.paper-authors` | 1.125rem = 18px / 400 / 1.6 | #6b7280; own name 700 |
| Venue | `.paper-venue` | 18px / 600 | #2563eb |
| Nav logo | `.nav-logo` | 1.5rem = 24px / 700 | #2563eb |
| Nav link | `.nav-link` | 16px / 500 | #1f2937 |
| Button | `.paper-link-btn` | 16px / 500 | #ffffff |
| Section heading | `.section-heading` | 2rem = 32px / 700 / 1.6, padding-bottom 8px, 2px bottom border | #1f2937 |
| Subsection | `.subsection-heading` | 1.5rem = 24px / 600, margin 32px 0 16px | #1f2937 |
| Abstract | `.abstract-text` | 18px / 400 / 1.8 = 32.4px, justified | #6b7280 |
| Section text | `.section-text` | 1.0625rem = 17px / 400 / 1.7 | #1f2937 |
| Inline method name | `code` in abstract | monospace 18px / 700 | #6b7280 |
| Caption | `.figure-caption` | 0.9rem = 14.4px italic | #6b7280 |
| Table | inline `font-size: 0.95em` | 15.2px; th 700; first column 500 | #1f2937 |
| Citation | `.citation-box pre` | Courier New 0.9rem = 14.4px / 1.4 | #1f2937 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Navbar | 0 | none | `0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px 0 rgba(0,0,0,0.06)` (--shadow) |
| Pill buttons | 30px | none | none; hover `translateY(-2px)` + --shadow, fill #1e40af |
| Figure card (`.figure-container img`) | 8px, padding 16px | none | --shadow, background #f9fafb |
| Video container | 8px | none | --shadow |
| Citation box | 8px, padding 24px | none | none |
| Copy-citation button | 6px, padding 8px 16px | none | none |
| Audio / demo panels | 8px, padding 24px / 32px | none | demo button hover `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05)` (--shadow-lg) |
| Section heading rule | 0 | 2px solid #e5e7eb bottom | none |
| Table | 0 | th 2px solid #e5e7eb top and bottom; td 1px dashed #e5e7eb bottom | none |

## Layout Metrics

- **Site container**: `.container` max 1200px, padding 0 20px (x=120 at 1440).
- **Header**: margin-top 80px under the 70px fixed navbar; padding 60px 0; title block max 900px centred (x=270).
- **Sections**: `.paper-section` max 900px, margin 0 auto 60px, padding 0 20px, so text runs 860px from x=290. From "Method: SylAVL-CoT" onwards the sections are nested one level deeper in the markup and render 820px wide at x=310.
- **Content band**: `.paper-content` padding 60px 0, white.
- **Figures**: `.figure-container` margin 32px 0, centred; images max 100% with 16px padding on a #f9fafb card; caption 16px below.
- **Table**: inline width 90% (774px), margin 32px auto, caption 600 above with 16px gap, cells padding 12px.
- **Results grid / audio samples**: auto-fit grids (min 350px / 300px), gap 32px.
- **Footer**: #1f2937, padding 32px 0, centred white text; rendered 90px tall.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px (1440 renders this) | 20px inside 1200px / 900px | 18px abstract, 17px text | 40px | nav links inline |
| ≤768px | 20px | same | 28px (1.75rem); h2 24px; h3 20px | hamburger menu; buttons padding 8px 16px at 14.4px, gap 8px; results and audio grids 1 column; copy button static and full width |

## Components

- **Cobalt pill button** (`.paper-link-btn`): inline-flex, gap 8px, padding 12px 24px, 50px tall, radius 30px, #2563eb fill, #ffffff 16px / 500 Inter, leading Font Awesome icon (file, GitHub, quote) or emoji. Hover: fill #1e40af, translateY(-2px), --shadow; transition 0.3s.
- **Personal-site navbar**: fixed white bar, 70px, soft two-layer shadow; bold cobalt name as the logo; 16px / 500 slate links 32px apart.
- **Section heading**: 32px / 700 #1f2937 with an 8px bottom padding and a 2px #e5e7eb rule spanning the column; 24px gap to content.
- **Figure card**: image with 16px #f9fafb padding, 8px radius and --shadow, centred; italic 14.4px #6b7280 caption beginning "Figure N:" in bold italic.
- **Statistics table**: 90% width, caption 600 above; header row #f3f4f6 with 2px #e5e7eb rules top and bottom; body rows separated by 1px dashed #e5e7eb; first column 500; numbers centred; no vertical lines.
- **Citation box**: #f9fafb, radius 8px, padding 24px, Courier New 14.4px; a cobalt "Copy" button absolutely placed 16px from the top-right corner (6px radius, 14px / 500 white), hover #1e40af.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Site navbar | yes | fixed white bar with the author's name as logo |
| Title / authors / venue | yes | centred, grey authors with bold owner, cobalt venue |
| Affiliations | absent from the source | no affiliation line on the page |
| Link buttons | yes | four cobalt pills with icons |
| Abstract | yes | 18px justified grey text with monospace method names |
| Figures | yes | padded grey cards with soft shadow and italic captions |
| Statistics table | yes | inline-styled minimal table with dashed rows |
| Method / results | yes | headings with rules, figures |
| Citation | yes | grey box with a cobalt copy button |
| Footer | yes | dark slate band with a white copyright line |
| Video / audio demos | present but non-standard | styles exist in `paper-detail.css` (video container, audio samples, demo button) but this paper page does not use them |

## Adapting to Other Content

- **More authors and affiliations**: keep the 18px #6b7280 author line, add a 15.2px #6b7280 affiliation line below it, and keep the owner's name in 700.
- **A results table**: copy the statistics-table recipe (header #f3f4f6, 2px #e5e7eb rules, dashed 1px rows, 12px cell padding) and mark the best value 700 #1f2937; cobalt only for links.
- **Audio or video demos**: use the declared `.audio-samples` grid (#f9fafb panels, 8px radius, 24px padding) and the 16:9 `.video-container` with 8px radius and --shadow.
- **News or publication lists**: these belong to the site's Publications page; on a paper page, link back through the navbar rather than adding a list.
- **A teaser image in the header**: place it as a figure card at the top of the content band (900px column), not inside the gradient header.

## Do's and Don'ts

- Do use one blue (#2563eb) for the logo, venue, buttons and the copy action.
- Do underline every section heading with the 2px #e5e7eb rule.
- Do set figures on #f9fafb cards with 16px padding, 8px radius and the soft shadow.
- Do keep the paper page inside the personal-site chrome (navbar and dark footer).
- Don't add colour fills to table cells; the header grey and dashed rules are enough.
- Don't use the deep blue #1e40af except for hover states.
- Don't widen the reading column past 900px.

## Surfaces

White page and navbar; a #f9fafb → #ffffff 135deg wash behind the paper header; #f9fafb figure cards and citation box; #f3f4f6 table header; #1f2937 footer. Shadows are the soft Tailwind-like --shadow pair.

## Imagery

Paper figures with frames from animated films (Frozen, Trolls, Coco), multilingual lyric snippets with flag icons, colour-highlighted alignment tables and bar charts, each on a pale grey padded card. Icons from Font Awesome.

## Layout

Fixed site navbar, a centred gradient header, then a single 900px column of sections separated by 60px margins and heading rules, and a dark footer. About 7,200px tall.

## Agent Prompt Guide

Quick colors: cobalt #2563eb, deep blue #1e40af, slate #1f2937, grey #6b7280, wash #f9fafb, rule #e5e7eb, table head #f3f4f6.

1. "Build a paper header inside a personal site: fixed 70px white navbar with box-shadow 0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px 0 rgba(0,0,0,0.06), logo 24px / 700 #2563eb, links 16px / 500 #1f2937 32px apart. Below it a band with background linear-gradient(135deg, #f9fafb 0%, #ffffff 100%), padding 60px 0, 1px #e5e7eb bottom border; centred 900px block: Inter 40px / 700 #1f2937 title (line-height 1.3), 18px #6b7280 authors, 18px / 600 #2563eb venue, then pills."
2. "Make cobalt pills: padding 12px 24px, radius 30px, #2563eb fill, #ffffff 16px / 500 Inter, 8px gap to a leading icon, 16px between pills; hover background #1e40af, translateY(-2px), box-shadow 0 1px 3px 0 rgba(0,0,0,0.1), 0 1px 2px 0 rgba(0,0,0,0.06)."
3. "Create a section: max-width 900px, padding 0 20px, margin-bottom 60px; heading 32px / 700 #1f2937 with padding-bottom 8px and a 2px solid #e5e7eb bottom border; abstract 18px #6b7280, line-height 1.8, justified; figures as images with 16px #f9fafb padding, radius 8px and the soft shadow, captions 14.4px italic #6b7280."

## Similar Pages

- Paper pages generated inside a personal academic site, sharing its navbar and footer.
- Tailwind-palette pages (slate, grey, blue-600) written in plain CSS custom properties.

## Quick Start

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #1e40af;
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --border-color: #e5e7eb;
  --table-head: #f3f4f6;
  --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --font: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --column: 900px;
  --radius-pill: 30px;
  --radius-card: 8px;
}
```

## Provenance

- **URL**: https://k1064190.github.io/papers/paper1.html
- **Paper**: MAVL: A Multilingual Audio-Video Lyrics Dataset for Animated Song Translation (arXiv 2505.18614), Woohyun Cho, Youngmin Kim, Sunghyun Lee, Youngjae Yu.
- **Venue**: EMNLP 2025.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: none stated; a hand-written personal site (`style.css`, `paper-detail.css`); footer reads "© 2025 Woohyun Cho. All rights reserved."
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and `style.css`, `paper-detail.css` and `papers/paper1.html` read directly, on 2026-10-28.
