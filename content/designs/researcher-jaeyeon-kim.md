# Jaeyeon Kim — Style Reference

> A quiet seminar handout in light Roboto, where one red-highlighted question and a row of mint tags are the only raised voices.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site's `styles.css` and `index.html` read directly. The page is a small single-page app: `app.js` renders the home route into `<main>` from `content.js`, so the render is the only place the home markup exists. Roboto loads self-hosted in 300, 400, 600 and 700 and renders everywhere; body copy is weight 300, which is the defining texture.

## Overview

A 1080px shell with 28px side padding on white. A header row has "Jaeyeon Kim" in Roboto 17px/300 on the left and five 14px links on the right in grey #666666, the current page in #222222 with an underline 5px below; a 1px #dddddd rule spans the full shell under it. The hero opens with the name in Roboto 32px/600, then three light 16px paragraphs at 1.55 line height that wrap around a 270px portrait floated right. Links are a muted blue #245b96 with an underline 3px below the text. The research question sits in an inline red highlight: #ff0000 text at weight 400 on a #ffe6e6 wash with 2px corners. Five rectangular mint tags (Email, Scholar, CV, Twitter / X, LinkedIn) follow. Below, 22px/600 section headings introduce a dated News list (90px grey date column), a two-column grid of "Selected publications" cards (1px #e3e7ec border, 8px corners) with small framed thumbnails, a red-on-pink venue tag and a brown "Outstanding Paper" label, a Background prose block at 15px, a collapsible "figures" section, and a thin footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 75.0% (page), #d4d4d4 8.9%, #7d6d6b 3.3% and #f9f3f2 4.5% (portrait backdrop and clothing), #eaecec 4.6% (mint tags, header rule and anti-aliased light text), #fcfcfc 2.0%. The red question highlight and the mint tags are each under 1% but are the only saturated color.

Anatomy in DOM order (desktop 1440px; shell 1080px at x=180, content x=208–1232):

1. **Header** (`.site-header .nav-inner`, y=0–79): padding 25px 28px, 1px #dddddd bottom border across the 1080px shell. Brand "Jaeyeon Kim" Roboto 17px/300 #222222 left; nav right (x=923) with 14px/300 links, 22px gaps, #666666, current "Home" #222222 underlined with 5px offset. Gap 40px.
2. **Name** (`.hero h1`, y=119): Roboto 32px/600, line-height 1.35, #222222, left. Gap 24px.
3. **Portrait** (`figure.portrait-block`, floated right, x=962, y=186): 270px wide (351px tall), no radius, margin 0 0 20px 30px.
4. **Intro paragraphs** (`.intro p`, y=186, 351, 466): Roboto 16px/300, line-height 1.55 (24.8px), #222222, margin-bottom 16px; links #245b96 underlined 3px below; the research question as a `.coloredhl-xred` span (#ff0000 400 on #ffe6e6). Gap 21px.
5. **Social tags** (`.social-link`, y=561, 31px tall): Roboto 14px/300 #007d69 on #e5f4f1, padding 4px 10px, radius 4px, gaps 8px 18px. Hero padding-bottom 38px.
6. **News** (`h2`, y=630): Roboto 22px/600 #222222, margin-bottom 18px; rows from y=677 in a 90px + 1fr grid, gap 18px, 14px/300, date #666666, 12px between rows.
7. **Selected publications** (`h2`, y=877) with a right-aligned 14px "All publications" link at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Text | #222222 | --text | body text, name, headings, brand, current nav item, paper titles, own name |
| Muted | #666666 | --muted | inactive nav links, news dates, paper meta, contribution note, footer |
| Link Blue | #245b96 | --accent | inline links (underlined), "All publications", paper-link hover text, focus ring |
| Rule | #dddddd | --border | header bottom rule, footer top rule |
| Highlight Red | #ff0000 | --xred | text of the highlighted research question |
| Highlight Wash | #ffe6e6 | (literal) | background of the highlighted research question |
| Mint Ink | #007d69 | --social-accent | social tag text, social tag hover fill |
| Mint Wash | #e5f4f1 | (literal) | social tag background |
| Venue Red | #b30000 | --publication-accent | venue tag text in paper cards |
| Venue Tint | #fff0f0 | --publication-tint | venue tag background |
| Award Brown | #80501c | (literal) | "Outstanding Paper" label |
| Card Edge | #e3e7ec | (literal) | paper card border, paper link button border |
| Thumb Edge | #e8ebef | (literal) | thumbnail frame border |
| Authors Grey | #555555 | (literal) | author lines |
| Button Grey | #4c5768 | (literal) | Paper / Code / Project link text |
| Button Hover Edge | #acbdd4 | (literal) | paper link button border on hover |
| Scrollbar | #aeb7c2 | (literal) | thin scrollbar of the news list when it overflows |
| White | #ffffff | (literal) | page, paper cards |

Declared but not visible on the home route: `--publication-hover` #850000, `--publication-border` #efd6d6, the topic filter colors (#3153b4, #623e99) and blog callout colors, which belong to the Research and Blog routes.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif (self-hosted `assets/fonts/roboto.css`) | Roboto 300, 400, 600, 700 | Inter (at 300) |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Brand | `.brand` | 17px / 300 | #222222 |
| Nav link | `#main-nav a` | 14px / 300 | #666666 (current #222222, underlined) |
| Name | `.hero h1` | 32px / 600 / 1.35 | #222222 |
| Section heading | `h2` | 22px / 600 / 1.35 | #222222 |
| Intro | `.intro p` | 16px / 300 / 1.55 | #222222 |
| Question highlight | `.coloredhl-xred` | 16px / 400, padding 0.08em 0.2em | #ff0000 on #ffe6e6 |
| Social tag | `.social-link` | 14px / 300 | #007d69 |
| News row | `.news-list li` | 14px / 300 / 1.65 | #222222; date #666666 |
| Paper title | `.paper-row h3` | 16px / 700 / 1.4 | #222222 |
| Paper meta | `.paper-meta` | 12px / 300 | #666666 |
| Venue tag | `.venue` | 11px / 300 | #b30000 on #fff0f0 |
| Award label | `.research-section .award-tag` | 15px / 600 | #80501c |
| Authors | `.authors` | 13px / 300; own name 700 #222222 | #555555 |
| Paper link | `.paper-links a` | 11px / 300 | #4c5768 |
| Background prose | `.background-section` | 15px / 300 / 1.65 | #222222 |
| Footer | `.footer` | 13px / 300 | #666666 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Social tag | 4px | none | none |
| Question highlight | 2px | none | none |
| Paper card | 8px | 1px #e3e7ec | none |
| Thumbnail frame | 5px | 1px #e8ebef, 4px padding | none |
| Venue tag | 4px | none | none |
| Paper link button | 4px | 1px #e3e7ec (hover #acbdd4) | none |
| Portrait | 0 | none | none |
| Header and footer | 0 | 1px #dddddd (bottom / top) | none |

## Layout Metrics

- **Shell**: `.shell` max-width 1080px, padding-inline 28px, centred; content 1024px from x=208 at 1440.
- **Header**: flex, space-between, padding-block 25px (79px tall), nav gap 8px 22px.
- **Hero**: `display: flow-root`, padding-block 40px 38px; portrait float 270px with margin 0 0 20px 30px; h1 margin-bottom 24px; social row margin-top 20px, clears the float.
- **Home sections**: grid with 40px gap; h2 margin-bottom 18px.
- **News**: grid columns 90px + 1fr, gap 18px, 12px between rows; `.news-scroll` caps at 10rem with a thin #aeb7c2 scrollbar when long.
- **Paper grid**: at ≥900px two columns with 14px gap; each card a grid of 105px visual + 1fr, gap 14px, padding 16px; visual 105×96 with object-fit contain.
- **Footer**: shell, flex space-between, margin-top 40px, padding-block 22px.
- **Page height**: 2,077px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥900px | 28px inside a 1080px shell | 16px | 32px | papers in two columns, 105×96 visual |
| 651–899px | 28px | 16px | 32px | papers in one column, 145×110 visual, cards align centre |
| ≤650px | 20px | 16px | 28px | header stacks (nav under brand, 14px gap); portrait 34% (max 200px); news date column 78px; visual 115×100 |
| ≤450px | 20px | 16px | 28px | paper card stacks visual (full width, 140px tall) over text |

## Components

- **Mint tag link** (`.social-link`): inline-block, Roboto 14px/300, #007d69 on #e5f4f1, padding 4px 10px, radius 4px, no icon; hover and focus: #ffffff text on #007d69, 140ms.
- **Question highlight**: inline span, #ff0000 at weight 400 on #ffe6e6, padding 0.08em 0.2em, radius 2px, `box-decoration-break: clone` so each wrapped line gets its own wash.
- **Underlined link**: #245b96, underline offset 3px in prose and news; elsewhere underline only on hover.
- **News row**: two-column grid, 90px date in #666666 and a 14px/300 sentence with underlined links.
- **Paper card** (`.paper-row`): #ffffff, 1px #e3e7ec, radius 8px, padding 16px; left a 105×96 thumbnail frame (1px #e8ebef, radius 5px, padding 4px, contain); right a meta line (venue tag 11px #b30000 on #fff0f0 with 2px 6px padding and 4px radius, then an optional 15px/600 #80501c award label), a 16px/700 title, 13px #555555 authors with the owner bold, then small 11px buttons (1px #e3e7ec, radius 4px, padding 2px 8px, #4c5768; hover #245b96 with #acbdd4 border).
- **Disclosure section**: `<details>` with a #666666 ▸ marker at 18px that rotates 90° when open, beside a 22px/600 summary heading.
- **Footer**: name left and "Email" right in 13px #666666 above nothing else, 1px #dddddd top rule.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header nav | yes | text brand and five grey links, current underlined |
| Name, intro and portrait | yes | 32px/600 name, light 16px paragraphs, floated photo |
| Research question highlight | yes | red text on pink wash |
| Social links | yes | mint rectangular tags |
| News | yes | dated grid list |
| Selected publications | yes | two-column card grid with venue tags |
| Award tags | yes | brown 15px/600 label beside the venue tag |
| Background | yes | 15px prose block with underlined links |
| Figure gallery | yes | collapsed `<details>` "Click here if you think my figures are pretty" |
| Footer | yes | name and email on a hairline |
| Blog / CV / Research list | present but non-standard | separate hash routes, not on the home view |

## Adapting to Other Content

- **Long publication lists**: keep the two-column card grid on the home view for six to eight papers and link the rest from "All publications"; on a full list switch to one column and add the topic filter tabs the stylesheet already defines.
- **Papers without figures**: use `.without-figure` so the text spans both card columns; do not insert placeholder art.
- **More news**: wrap in `.news-scroll` (max-height 10rem) rather than letting the list push publications below the fold.
- **More awards**: one brown 15px/600 label per card, after the venue tag; never more than one.
- **Talks or teaching**: reuse the news grid with a 90px date column.

## Do's and Don'ts

- Do keep body text at Roboto 300; headings jump straight to 600.
- Do let exactly one phrase per page carry the red highlight.
- Do keep tags rectangular with 4px corners; nothing on the page is a pill.
- Don't add shadows; cards are outlined with #e3e7ec only.
- Don't use the mint color anywhere but the social tags.
- Don't round the portrait.

## Surfaces

White throughout. Cards are separated from the page only by 1px #e3e7ec outlines; the only washes are the mint tags, the pink question highlight and the venue tags.

## Imagery

A studio portrait on a pale backdrop, and small paper thumbnails that are mostly plots and figure crops (loss curves, sudoku grids, a dark heatmap) shown contained inside framed 105×96 boxes.

## Layout

Header, hero (name, intro wrapped round the portrait, tags), News, Selected publications grid, Background, collapsible figures, footer. About 2,077px tall at 1440.

## Agent Prompt Guide

Quick colors: text #222222, muted #666666, links #245b96, rule #dddddd, highlight #ff0000 on #ffe6e6, tag #007d69 on #e5f4f1, venue #b30000 on #fff0f0, award #80501c, card edge #e3e7ec, page #ffffff.

1. "Build a hero: shell max-width 1080px with 28px padding; name Roboto 32px/600 #222222, margin-bottom 24px; a 270px portrait floated right with margin 0 0 20px 30px; intro paragraphs Roboto 16px/300, line-height 1.55, #222222, links #245b96 underlined 3px below; wrap the key research question in a span with color #ff0000, font-weight 400, background #ffe6e6, padding 0.08em 0.2em, radius 2px."
2. "Make social tags: inline-block links, Roboto 14px/300, color #007d69, background #e5f4f1, padding 4px 10px, radius 4px, gaps 8px 18px; hover #ffffff on #007d69."
3. "Create a selected-publication card grid: two columns with 14px gap; each card #ffffff, 1px solid #e3e7ec, radius 8px, padding 16px, a grid of a 105×96 thumbnail frame (1px #e8ebef, radius 5px, padding 4px, contain) and text; meta line with an 11px #b30000 venue tag on #fff0f0 (radius 4px, padding 2px 6px) and an optional 15px/600 #80501c award label; title 16px/700 #222222; authors 13px #555555 with the owner in 700; 11px link buttons with 1px #e3e7ec border, radius 4px, color #4c5768."

## Similar Pages

- Minimal hand-built academic SPAs with a top text nav and light-weight sans body.
- Theory-leaning ML student pages that foreground a single research question.

## Quick Start

```css
:root {
  --text: #222222;
  --muted: #666666;
  --border: #dddddd;
  --accent: #245b96;
  --xred: #ff0000;
  --social-accent: #007d69;
  --publication-accent: #b30000;
  --publication-tint: #fff0f0;
}
body { margin: 0; background: #ffffff; color: var(--text); font: 300 16px/1.65 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
.shell { max-width: 1080px; padding-inline: 28px; margin-inline: auto; }
h1 { font-size: 32px; font-weight: 600; } h2 { font-size: 22px; font-weight: 600; }
a { color: var(--accent); text-decoration: none; }
.social-link { padding: 4px 10px; border-radius: 4px; color: var(--social-accent); background: #e5f4f1; }
.paper-row { border: 1px solid #e3e7ec; border-radius: 8px; padding: 16px; background: #ffffff; }
```

## Provenance

- **URL**: https://jaeyeonkim01.github.io/
- **Person**: Jaeyeon Kim (diffusion models).
- **Venue / award**: ICML 2025 Outstanding Paper, "Train for the Worst, Plan for the Best".
- **Selection reason**: Rule B (first author); announcement https://icml.cc/virtual/2025/awards_detail. Homepage from the Semantic Scholar author profile.
- **Template credit**: none; a hand-built hash-routed single-page site.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `styles.css` and the `index.html` shell read directly, on 2026-10-28.
