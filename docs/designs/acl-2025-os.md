# OS-Genesis — Style Reference

> A sunset over a marble basilica: italic serif headlines in apricot light, then a quiet Distill reading room.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the header, byline, jump cards, tables and BibTeX), the 1440×900 and full-page screenshots, and the page's `static/css/style.css` and `nav.css` read directly. The page is built on the Cambrian-1 project template over the Distill v2 article runtime. It declares `font-family: Charter` but loads no web font, and Charter is not installed on the measuring machine, so all text renders in the browser's default serif (Times New Roman on Windows); on macOS, where Charter ships with the system, the same page renders in Charter. Only Font Awesome and Academicons load.

## Overview

The page opens with a full-width 794px header on a 138° gradient that runs from black through slate lavender (#9199b1) to apricot (#feae6f) and pale butter (#fdf1cc) at the bottom right. A small apricot "More Research ⌄" dropdown sits at the top centre and an "ACL 2025 VIENNA" logo image at the top right. The header splits in two. On the left, a bold italic 52.8px "OS-Genesis" and a three-line 32px bold subtitle, both in apricot, then a 19.2px cream (#fff7d4) intro with a butter-yellow italic "manual-free", a list of four features each with a 30px line icon tinted cream and a butter-yellow bold lead word, and four cream pill buttons (#fff0ce fill, amber hairline, 20px radius, bold black labels). On the right is a 585px square illustration of robots in a sunlit basilica. Below the header the page becomes a white Distill article: a centred byline between hairlines with 16 author names at 20px and a row of six institution logos, a 21.6px abstract, a numbered component list, four light-blue jump cards with thick blue borders and line icons, a bordered "Click to jump to each section" hint, then bold 34px section headings, figures, tables with grey header cells and blue-tinted highlight cells, and a grey Courier BibTeX block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): slate lavender #8892a1 16.0% and #585f6e 12.8% (gradient mid); dark #433e42 13.7%, #191b20 10.8% and #7a7375 11.9% (the black corner and the illustration's shadows); apricot-tan #ba9f8c 11.7% and #d9c3a2 9.6% (gradient warm end and illustration gold); white #fefdf9 13.5% (the article below y=794).

Anatomy in DOM order (desktop 1440px; header container max-width 1600px with 50px padding, left column 650px at x=50, image column from x=773):

1. **Dropdown nav** (`nav.navbar`, top centre, 52px): transparent, "More Research" 16px #feae6f with a blue chevron, padding 8px 40px 8px 12px.
2. **Venue logo** (top right, x=1309, 119×26): "ACL 2025 VIENNA" image.
3. **Title** (`.header-content h1 i`, y=104): serif 52.8px (3.3em) bold italic, #feae6f, line-height 1.2, left-aligned. Gap 6px (h2 margin-top -0.75em).
4. **Subtitle** (`.header-content h2`, y=168, three lines, 115px): serif 32px bold, line-height 1.2, #feae6f. Gap 16px.
5. **Intro** (y=299): 19.2px (1.2rem) #fff7d4, two lines; "manual-free" bold italic #ffe099. Gap 19px.
6. **Feature list** (`.icon-container`, y=369–644, 15px gaps): 30px line icons (CSS-filtered to cream) with a 16px right margin, text 16px #fff7d4 line-height 1.6, lead words bold #ffe099. Gap 26px.
7. **Buttons** (y=670, 50px tall, 4px apart): arXiv, Code, Checkpoints, Data; #fff0ce, 2px rgba(255,193,7,0.5), 20px radius, padding 10px 20px, bold 16px #000000, icon left.
8. **Illustration** (`img.teaser-image`, x=773, y=121, 585×585): square image at max-width 90% of the right column, centred vertically. The header ends at y=794, so the byline's top rule shows at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Night | #000000 | (literal) | header gradient start (10%), button labels, author names |
| Dusk Lavender | #9199b1 | (literal) | header gradient middle (55%) |
| Apricot | #feae6f | (literal) | header gradient 85% stop, title, subtitle, dropdown label |
| Butter Haze | #fdf1cc | (literal) | header gradient end (100%) |
| Cream Text | #fff7d4 | (literal) | header intro and feature text |
| Butter | #ffe099 | (literal) | bold lead words and "manual-free" in the header |
| Button Cream | #fff0ce | (literal) | hero button fill |
| Button Amber | rgba(255,193,7,0.5) | (literal) | hero button border |
| Button Hover | #eab682 | (literal) | hero button hover fill (text turns white) |
| Article Ink | rgba(0,0,0,0.8) | Distill default | article body text and headings |
| Caption Grey | rgba(0,0,0,0.6) | Distill default | figure and table captions |
| Jump Blue | #508af6 | (literal) | 3px border of the jump cards |
| Jump Tint | #d6eefb | (literal) | jump card fill (hover #88c2fa) |
| Hint Blue | #007bff | (literal) | bold text in the click hint, author link hover |
| Table Header | #f2f2f2 | (literal) | `.tb-hdr` header cells |
| Highlight Teal | rgba(67,143,171,0.29) | (literal) | `.highlight` best-result cells |
| BibTeX Grey | #f9f9f9 | (literal) | BibTeX block fill |
| BibTeX Ink | #222222 | (literal) | BibTeX text |
| Hint Grey | #333333 | (literal) | click-hint text |
| Hint Border | #cccccc | (literal) | 2px click-hint border |

Declared but not visible: the template's `.highlight-green` (#e6ffe6), `.highlight-orange` (#fff2e6) and `.highlight-blue` (#e6f2ff) row tints, the takeaway cards and the storytext blockquote are in the stylesheet but unused on this page; every highlighted cell uses `.highlight`.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | `Charter` (no fallback, no web font) | browser default serif: Times New Roman on Windows, Charter on macOS | Charis SIL (a free Charter cut) |
| BibTeX | 'Courier New', Courier, monospace | Courier New | Courier Prime |
| Icons | Font Awesome 5, Academicons; feature icons are images | Font Awesome 5 Brands, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Title | `.header-content h1` | 3.3em = 52.8px / 700 italic / 1.2 | #feae6f |
| Subtitle | `.header-content h2` | 2em = 32px / 700 / 1.2, margin-top -0.75em | #feae6f |
| Intro | `.header-container p` | 1.2rem = 19.2px / 400 | #fff7d4 |
| Feature text | `.icon-item div` | 16px / 400 / 1.6; lead word 700 | #fff7d4 / #ffe099 |
| Hero button | `.button-container a.button` | 16px / 700 | #000000 |
| Author names | `.author-link` | larger = 20.35px / 400 / 2.3rem | #000000 |
| Article body | `d-article` | 16.96px / 400 / 1.7 (Distill) | rgba(0,0,0,0.8) |
| Abstract | `p.text.abstract` | 1.35rem = 21.6px / 400 | rgba(0,0,0,0.8) |
| Section heading | `h1.text` | 2em = 33.92px / 700 | rgba(0,0,0,0.8) |
| Subheading | `h2.text` | 1.8em = 30.5px / 600, 1px rgba(0,0,0,0.1) underline, 16px padding-bottom | rgba(0,0,0,0.8) |
| Caption | `figcaption` | 1.125em = 19.08px / 400, centred | rgba(0,0,0,0.6) |
| Table | `.data-table` | 15px (12px declared, scaled by Distill) / 1.25; header 700 | rgba(0,0,0,0.8) |
| Click hint | `.click-hint` | 15px | #333333 |
| BibTeX | `.bibtex` | 12.8px Courier New | #222222 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 20px | 2px rgba(255,193,7,0.5) | none |
| Jump cards | 10px | 3px #508af6 | none |
| Click hint | 5px | 2px #cccccc | 0 4px 8px rgba(0,0,0,0.1) |
| Byline | 0 | 1px rgba(0,0,0,0.1) top and bottom | none |
| Subheading | 0 | 1px rgba(0,0,0,0.1) bottom | none |
| Table cells | 0 | 1px rgba(0,0,0,0.2) under headers, 1px rgba(0,0,0,0.05) rows | none |
| BibTeX | 0 | none | none |
| Takeaway cards (declared) | 15px | none | 0 4px 8px rgba(0,0,0,0.2) |

## Layout Metrics

- **Header**: `.header-wrapper` full width; `.header-container` max-width 1600px, padding 50px, flex space-between; columns `max-width: calc(50% - 20px)`; image at max-width 90% of its column.
- **Article grid**: Distill `d-article` grid at 1440: page column from x=152, text column 704px at x=368; elements with `.text` widen to 150% (1056px) starting 140.8px left of the text column (x=227); figures 150% width with -20% margin.
- **Byline**: inside the 704px text column, padding 0 5px 10px, 1px rules above and below, 20px margin-bottom; logos 80px tall with 12–16px gaps.
- **Jump cards**: `.icon-row` flex, cards `flex: 1 1 100px`, 146×94px with 10px padding and 10px margin; hint box 60% width below.
- **Section spacing**: h1.text margin 33.92px top and bottom; h2.text 30.5px; article padding-top 32px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1180px | Distill: 152px page margin at 1440 | 16.96px | 52.8px | header two columns; `.text` and figures overhang the text column |
| 769–1179px | Distill grid narrows | 16.96px | 52.8px | — |
| 600–768px | 16px header padding (32px top) | 16px | 48px (3em); h2 27.2px, no wrap | header still two columns; aside notes hidden; `.text` back to 100% width |
| <600px | 16px | 16px | 48px | header stacks (image below text, 90% wide); jump cards two per row (45%) |

## Components

- **Sunset header**: full-width block with `linear-gradient(138deg, #000000 10%, #9199b1 55%, #feae6f 85%, #fdf1cc 100%)`, text left and illustration right.
- **Icon feature list**: rows of a 30px line-icon image (filtered to cream with `invert(87%) sepia(11%) saturate(748%) hue-rotate(340deg) brightness(110%)`) and a 16px cream paragraph whose bold lead word is #ffe099; 15px between rows.
- **Cream pill button**: #fff0ce, 2px rgba(255,193,7,0.5), 20px radius, padding 10px 20px, bold 16px black, icon or Hugging Face emoji left; hover #eab682 with white text.
- **Byline**: centred author names in 20px serif black, star superscripts for equal contribution, then a row of institution logos, all between two 1px rgba(0,0,0,0.1) rules.
- **Jump card** (`.icon-link`): #d6eefb, 3px #508af6, 10px radius, column of a line icon (1.8em tall) and a two-line label; hover #88c2fa.
- **Click hint**: centred box at 60% width, 2px #cccccc, 5px radius, 0 4px 8px rgba(0,0,0,0.1), 15px #333333 text with a bold #007bff phrase and a pointer emoji.
- **Data table** (`.data-table`): separate borders, 15px, header cells #f2f2f2 bold with 1px rgba(0,0,0,0.2) rules, best results in `.highlight` rgba(67,143,171,0.29) bold; caption below in 19.08px grey.
- **BibTeX** (`p.bibtex`): #f9f9f9, padding 2em (25.6px), 12.8px Courier New #222222.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Hero header | yes | sunset gradient, apricot italic serif title, feature list, illustration |
| Venue | present but non-standard | an "ACL 2025 VIENNA" logo image at the top right only |
| Navigation | present but non-standard | one "More Research" dropdown; no section nav |
| Link buttons | yes | four cream pills in the header |
| Authors / affiliations | yes | centred byline with institution logos instead of affiliation text |
| Abstract | yes | 21.6px paragraph at 150% text width |
| Section jump cards | yes | four blue-bordered cards plus a hint box |
| Method figures | yes | wide Distill figures with large captions |
| Results tables | yes | Distill data tables with grey headers and blue highlight cells |
| Charts | yes | five Chart.js canvases for scaling analysis |
| BibTeX | yes | grey Courier block |
| Footer | absent from the source | the page ends after BibTeX |

## Adapting to Other Content

- **More authors**: the byline wraps at 20px with 2.3rem line height; keep logos as the affiliation row, or add a 15px rgba(0,0,0,0.6) affiliation line under the names.
- **No illustration**: let the header text column run 60% wide and put a teaser figure on the right with the same 90% max-width; keep the gradient.
- **A longer results table**: keep `.data-table` with #f2f2f2 headers and the teal highlight; wrap in `.table-container` for horizontal scroll.
- **News or a publication list**: plain Distill paragraphs inside the 704px text column with bold dates, separated by 1px rgba(0,0,0,0.1) rules like the byline.
- **More link buttons**: add cream pills in the header row; they wrap in the 650px column.

## Do's and Don'ts

- Do keep the header gradient at 138° from black through lavender to apricot; it carries the identity.
- Do set the title in bold italic serif and keep apricot (#feae6f) for headline text only.
- Do use cream and butter (#fff7d4, #ffe099) for header body text and emphasis.
- Don't carry the gradient or apricot into the article; below the header everything is Distill black on white.
- Don't rely on `font-family: Charter` alone; add a fallback stack or a web font so Windows readers do not get Times New Roman.
- Don't use sharp rectangles for the hero buttons; they are 20px pills with an amber hairline.

## Surfaces

A full-bleed sunset gradient header; a white Distill article; light-blue jump cards; #f2f2f2 table headers; #f9f9f9 BibTeX.

## Imagery

A painterly AI-generated illustration of small white robots in a marble basilica under a sunburst, with glowing app icons. In the article: pipeline diagrams, GUI screenshots of mobile and web trajectories, results tables and line charts.

## Layout

Two-column hero header; then the Distill single-column article with overhanging wide blocks: byline, abstract, component list, jump cards, GUI Trajectory Data, Interaction-Driven Functional Discovery, Reverse Task Synthesis, Exploration and Reward Modeling, Mobile and Web results, scaling analysis, comparison with human data, BibTeX. About 9,150px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: gradient #000000 → #9199b1 → #feae6f → #fdf1cc, title #feae6f, header text #fff7d4, emphasis #ffe099, button #fff0ce with rgba(255,193,7,0.5), jump cards #d6eefb with #508af6, article ink rgba(0,0,0,0.8).

1. "Build a sunset header: full width, background linear-gradient(138deg, #000000 10%, #9199b1 55%, #feae6f 85%, #fdf1cc 100%), padding 50px, flex space-between. Left column max-width calc(50% - 20px): title serif 52.8px bold italic #feae6f; subtitle serif 32px bold #feae6f, line-height 1.2; intro 19.2px #fff7d4 with emphasis #ffe099. Right column: a square illustration at max-width 90%."
2. "Make cream pill buttons: background #fff0ce, 2px solid rgba(255,193,7,0.5), 20px radius, padding 10px 20px, serif 16px bold #000000, icon left; hover background #eab682 and white text."
3. "Create section jump cards: a centred flex row of cards 146px wide, padding 10px, margin 10px, background #d6eefb, 3px solid #508af6, 10px radius, a 1.8em line icon above a two-line 16.96px label; hover #88c2fa. Under it a hint box 60% wide with 2px #cccccc, 5px radius and 0 4px 8px rgba(0,0,0,0.1)."

## Similar Pages

- Cambrian-1 template pages (gradient header plus Distill article).
- GUI-agent and LLM-agent project pages with an illustrated hero and logo bylines.

## Quick Start

```css
:root {
  --night: #000000;
  --dusk: #9199b1;
  --apricot: #feae6f;
  --butter-haze: #fdf1cc;
  --cream-text: #fff7d4;
  --butter: #ffe099;
  --button-bg: #fff0ce;
  --button-border: rgba(255, 193, 7, 0.5);
  --jump-bg: #d6eefb;
  --jump-border: #508af6;
  --ink: rgba(0, 0, 0, 0.8);
  --serif: Charter, 'Bitstream Charter', 'Charis SIL', Georgia, serif;
}
body { font-family: var(--serif); }
.header-wrapper { background: linear-gradient(138deg, var(--night) 10%, var(--dusk) 55%, var(--apricot) 85%, var(--butter-haze) 100%); }
```

## Provenance

- **URL**: https://qiushisun.github.io/OS-Genesis-Home/
- **Paper**: OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis (arXiv 2412.19723), Qiushi Sun et al.
- **Venue**: ACL 2025.
- **Selection reason**: the arXiv comment states ACL 2025 camera-ready and the abstract links this page.
- **Template credit**: built on the Cambrian-1 project page template (gradient header, Distill `d-article`, jump cards, `.data-table`); no footer credit is shown.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of header and article components, the 1440×900 and full-page screenshots, and `style.css` and `nav.css` read directly, on 2026-10-28.
