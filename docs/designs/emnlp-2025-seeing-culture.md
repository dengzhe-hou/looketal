# Seeing Culture — Style Reference

> A museum catalogue on plain white: charcoal pill buttons, a row of big exhibit counts, and a quiz card that invites you to pick the right artifact.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, and the page's `bulma.min.css`, `index.css`, `leaderboard.css`, `scb.css` and `index.html`. The page is the Nerfies/MathVista Bulma template with an SCB layer (`scb.css`) for the walkthrough. "Google Sans" is declared for the title and authors but never loads (`fonts_loaded` lists only Noto Sans 400), so those lines render in the browser's generic sans-serif (Arial in this Windows render). Bold Noto Sans is synthesised from the 400 face. The leaderboard rows are filled by script, so the table was read from its computed header and first rows.

## Overview

A white, centred, Bulma-built benchmark page. A plain white navbar carries the SEA lion logo with "Seeing Culture" on the left, eight centred text links, and a navy outlined pill linking to the video sequel on the right. The hero is centred: a 48px bold title with the logo inline, a 32px light-grey subtitle, two lines of 20px authors whose names are sky-blue links with green and pink superscripts, an affiliation line, a red bold venue with the acceptance rate in grey, and six charcoal pill buttons with white icons. Content sections run 1344px wide: a bullet summary, a six-up row of big numbers with tiny uppercase labels, a two-stage paper figure, a long justified abstract, an interactive walkthrough card with four clickable image tiles, word clouds, a script-filled sortable leaderboard, radar charts, task notes, a dated news list, a grey "Citation" band and partner logos above a #fafafa footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 82.3%, grey #bcbabb 5.6% (antialiased text), #d7dde2 3.5%, charcoal #6a6566 3.1% (buttons and title, blended), #f2efee 2.6%, #fafbfb 1.8%, #fdffff 0.7%, #fffffd 0.5%. The blue author links, red venue and logo colours are too small to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Navbar** (`nav.navbar`, 0–52px): white, no border or shadow. Brand item: logo image (max-height 32px) + bold "Seeing Culture", 16px #4a4a4a. Eight links (Benchmark … BibTeX), 16px / 400 #4a4a4a, padding 8px 12px, centred by an inline `flex-grow: 1; justify-content: center`. Right: "CMB · video benchmark" pill with 1.5px #24427c border, radius 999px, padding 2.4px 13.6px, 13.6px / 600 #24427c, external-link icon.
2. **Hero** (`section.hero > .hero-body`, padding 48px 24px; `.container.is-max-desktop` 960px at x=240).
3. **Title** (`h1.title.is-1.publication-title`, y=100): 48px / 600 / 54px, #363636, centred; a 48×32 logo image inline before the text. Margin-bottom 24px, then the subtitle's -20px pull-up.
4. **Subtitle** (`h2.subtitle.is-3`, y=162): 32px / 400 / 40px Noto Sans, #4a4a4a, centred, one line.
5. **Authors** (`.publication-authors.is-size-5`, y=233 and y=267): 20px / 400 / 30px, two centred lines; linked names #209cee (hsl(204,86%,53%), `!important`), one unlinked name in #4a4a4a; superscripts #6fbf73 (affiliation 1) and #ed4b82 (affiliation 2).
6. **Affiliations and venue** (y≈300 and y≈330): 20px #4a4a4a with the same coloured superscripts; venue "EMNLP 2025 Main Conference" bold #f41c1c followed by "(22.16% acceptance rate)" in #4a4a4a.
7. **Buttons** (`.publication-links`, y=374, 40px tall): Paper, arXiv, Code, 🤗 Dataset, Leaderboard, Explorer; each `button is-normal is-rounded is-dark` with 5px vertical margin and about 4px between pills.
8. **First section** (`section.section#what-is`, from y=479, padding 48px 24px; container 1344px at x=48): centred 32px / 600 heading at y=527, a 16px justified bullet list, then the stats row with numbers at y=775 and labels at y=835, ending at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma body) | page, navbar, hero, walkthrough card, table background |
| Charcoal | #363636 | Bulma `$grey-darker` / `is-dark` | title, section headings, stat numbers, button fill, table text |
| Text Grey | #4a4a4a | Bulma body text | subtitle, nav links, body text, stat labels, affiliations |
| Author Blue | #209cee | hsl(204,86%,53%) in `.publication-authors a` | linked author names |
| Affil Green | #6fbf73 | (inline `sup` style) | affiliation 1 markers |
| Affil Pink | #ed4b82 | (inline `sup` style) | affiliation 2 markers |
| Venue Red | #f41c1c | (inline `b` style) | "EMNLP 2025 Main Conference" |
| SCB Navy | #24427c | --scb-navy | CMB pill border and text, walkthrough stage label, tile hover border |
| SCB Line | #dbdfe6 | --scb-line | walkthrough card border, question box border, tile borders and label rules |
| SCB Soft | #f4f6fa | --scb-soft | question box, tile label strips |
| Correct Green | #2e7d4f | --scb-green | correct tile border and verdict after reveal |
| Wrong Red | #b3261e | --scb-red | "wrong" verdict text |
| Hint Grey | #6a6f7a | (literal) | walkthrough hint and source note |
| Table Rule | #000000 | `table` in leaderboard.css | 1px outer border of the leaderboard |
| Stripe | #fafafa | Bulma `.table.is-striped` | even rows and hover in the leaderboard; footer band |
| Band Grey | #f5f5f5 | Bulma `hero.is-light`, `pre` | "Citation" band, BibTeX and JSON code blocks |
| Charcoal Hover | #2f2f2f | Bulma `.button.is-dark:hover` | hero button fill on hover |
| Correct Tint | #eef7f1 | (literal, `.is-correct .tile-label`) | label strip of the correct tile after reveal |
| Row Line | #dbdbdb | Bulma `.table td` | 1px row lines in the leaderboard |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Body / UI | 'Noto Sans', sans-serif (Google Fonts, 400 only) | Noto Sans 400; bold synthesised | Noto Sans (load 600/700 weights) |
| Title / authors | 'Google Sans', sans-serif | not loaded; generic sans-serif (Arial here) | Product Sans-like: Google Sans Text or Outfit; to match the render, Arial |
| Code | Bulma monospace stack | system monospace | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 54px | #363636 |
| Subtitle | `h2.subtitle.is-3` | 32px / 400 / 40px | #4a4a4a |
| Authors, affiliations | `.publication-authors.is-size-5` | 20px / 400 / 30px | names #209cee, text #4a4a4a |
| Venue | `.paper-block b` | 20px / 700 | #f41c1c |
| Nav link | `.navbar-item` | 16px / 400 / 24px | #4a4a4a |
| Section heading | `h2.title.is-3` | 32px / 600 / 36px, margin-bottom 24px | #363636 |
| Subsection | `h3.title.is-4` | 24px / 600 / 27px | #363636 |
| Stat number | `p.title.is-3` | 32px / 600 / 36px | #363636 |
| Stat label | `p.heading` | 11px / 400 uppercase, letter-spacing 1px | #4a4a4a |
| Body | `.content` | 16px / 400 / 24px, justified | #4a4a4a |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| Table | `table.table.is-narrow` (inline 0.85rem) | 13.6px / 400 / 20.4px; th 700 | #363636 |
| Small note | `p.is-size-7` | 12px | #4a4a4a |
| Walkthrough stage | `.wt-stage` | 1.05rem = 16.8px | #24427c |
| BibTeX | `pre` | 14px / 21px | #4a4a4a on #f5f5f5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 290486px (Bulma `is-rounded`) | 1px solid transparent | none; Bulma `is-dark` hover darkens the fill to #2f2f2f |
| CMB pill | 999px | 1.5px solid #24427c | none |
| Walkthrough card | 10px, padding 20px 20px 24px | 1px solid #dbdfe6 | none |
| Question box | 8px, padding 12.8px 16px, max 720px | 1px solid #dbdfe6 | none |
| Image tiles | 8px, overflow hidden, 4:3 media | 1.5px solid #dbdfe6; hover #24427c; correct #2e7d4f; wrong tiles opacity 0.5 | none |
| Mask figures | 6px | 1px solid #dbdfe6 | none |
| Leaderboard | 0 | 1px solid #000000 outside; Bulma 1px #dbdbdb row lines | none |
| Code blocks | 0 | none | none |

## Layout Metrics

- **Containers**: hero uses `.container.is-max-desktop` = 960px (x=240); content sections use Bulma `.container`, which at 1440 (widescreen ≥1408px) is 1344px (x=48). Every section is `section.section` with padding 48px 24px; inner `.column.is-four-fifths` is forced to `width: 100%` inline, so text runs the full 1344px.
- **Hero**: `.hero-body` padding 48px 24px; title at y=100 directly under the 52px navbar; buttons end at y=414; hero ends at y=479.
- **Stats row**: `columns is-multiline is-mobile` with six `is-2-desktop` columns, each 204px plus 24px gutters, margin-top 16px.
- **Walkthrough**: card full container width; question box and 2×2 tile grid capped at 720px, grid gap 12px; stage-2 block separated by a 1px #dbdfe6 rule with 22.4px margin and 19.2px padding; mask row two columns, gap 16px.
- **Figures**: images inline at 95% (radar) or full width inside centred `.content` blocks.
- **Footer**: Bulma `.footer` #fafafa, padding 48px 24px 96px; content in a centred `is-8` column.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 renders this) | 48px (container 1344px) | 16px | 48px | stats 6 across |
| 1216–1407px | container 1152px | 16px | 48px | — |
| 1024–1215px | container 960px | 16px | 48px | navbar menu shown |
| 769–1023px | 24px section padding | 16px | 48px | navbar collapses to a burger; stats 3 per row (`is-4-mobile`) |
| ≤768px | 24px | 16px | 48px | Bulma columns stack; partner logos stack vertically |
| ≤560px | 24px | 16px | 48px | walkthrough tiles and mask row → 1 column |

## Components

- **Charcoal pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, #ffffff 16px / 400 Noto Sans, padding 7px 20px, height 40px, radius 290486px, 1px transparent border; leading 1em inline SVG icon (`.svg-icon`, fill currentColor) or emoji. Hover: Bulma darkens to #2f2f2f.
- **Outline pill link** (navbar CMB): 1.5px #24427c border, radius 999px, padding 2.4px 13.6px, 13.6px / 600 #24427c, external-link icon at 0.7rem.
- **Stat block**: number `p.title.is-3` 32px / 600 #363636 centred, then `p.heading` 11px uppercase with 1px tracking in #4a4a4a; six across, no card or divider.
- **Walkthrough quiz card** (`.walkthrough`): white, 1px #dbdfe6, radius 10px; stage label 16.8px #24427c with bold "Stage 1"; question box #f4f6fa with 1px #dbdfe6, radius 8px, 600 weight, centred; four `button.wt-tile` tiles (1.5px #dbdfe6, radius 8px) each with a #f4f6fa label strip (bold letter, 14.72px) over a 4:3 cover image; hover border #24427c (120ms). After a click the correct tile's border turns #2e7d4f with a #eef7f1 label, the others drop to 50% opacity, and stage 2 reveals mask images.
- **Leaderboard** (`table.table.is-striped.is-narrow.is-hoverable`): 13.6px, 1px black outer border, Bulma 1px #dbdbdb row lines, even rows #fafafa, cells padding 3.4px 6.8px, sortable number headers (underline on hover), medal emoji after leaders.
- **News list**: bullet items with a bold bracketed date `[2026-09]` lead, 16px #4a4a4a.
- **Citation band** (`section.hero.is-light.is-small`): full-width #f5f5f5 strip with a centred 40px `title is-2` "Citation", then a #f5f5f5 `pre` with the BibTeX.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | white, centred text links, logo left, navy outline pill right |
| Title / subtitle / authors | yes | centred; blue author links with green and pink superscripts |
| Venue | yes | red bold inline text with grey acceptance rate |
| Link buttons | yes | six charcoal rounded buttons with white icons |
| Summary bullets | yes | justified bullet list with bold leads |
| Stats row | yes | six big numbers with tiny uppercase labels |
| Overview figure | yes | full-width two-stage paper figure |
| Abstract | yes | justified 16px block across 1344px (dense) |
| Interactive example | yes | two-stage quiz card with clickable image tiles |
| Dataset samples, word clouds | yes | centred images with short captions |
| Leaderboard | yes | Bulma striped narrow table with black frame, script-filled and sortable |
| Qualitative results | yes | figure with caption |
| Task definition / submission | yes | h3 sections with a JSON `pre` block |
| News | yes | dated bullet list |
| BibTeX | yes | grey hero band title + grey `pre` |
| Partner logos | yes | SMU and ITB logos at 17em and 12em height |
| Footer | yes | #fafafa, template credit, visitor map |
| Video | absent from the source | — |

## Adapting to Other Content

- **More authors**: keep `author-block` spans at 20px centred, break lines with `<br>` every four names, and keep the colour-coded superscript per affiliation.
- **A teaser figure**: put it in a `section.section` right after the hero, full container width (1344px) or at 95% inline, centred caption at 16px #4a4a4a.
- **More stats**: extend the stats row in multiples of six on desktop (`is-2-desktop`); never box them.
- **Long abstracts**: the page sets the abstract at 1344px justified; for readability, a `.column.is-four-fifths` without the inline width override gives 1075px.
- **News or publication lists**: use the bracketed-date bullet pattern; bold the date only.
- **Additional benchmarks**: link them with the navy outline pill, as the navbar does for CMB.

## Do's and Don'ts

- Do centre the hero and keep its buttons charcoal pills with white icons.
- Do colour-code affiliations with the #6fbf73 / #ed4b82 superscripts.
- Do present dataset size as large 32px numbers with 11px uppercase labels.
- Do keep interactive cards on white with 1px #dbdfe6 borders and #f4f6fa label strips.
- Don't add shadows; borders are hairlines and buttons are flat.
- Don't introduce further accent colours beyond the author blue, venue red and SCB navy.
- Don't rely on Google Sans loading; plan for the generic sans fallback or load a real face.

## Surfaces

White page with three tints: #f4f6fa inside the walkthrough card, #f5f5f5 for the Citation band and code blocks, #fafafa for zebra rows and the footer. No gradients.

## Imagery

Paper figures with serif labels (the two-stage task diagram), real photographs of Southeast Asian cultural artifacts in 4:3 tiles and grids, segmentation-mask overlays, word clouds and radar charts, plus partner university logos. Icons are inline SVG sprites in white on the buttons.

## Layout

Centred 960px hero, then full-width 1344px sections stacked with 48px padding each, all headings centred; one full-bleed grey band before the BibTeX. About 7,450px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, charcoal #363636, text #4a4a4a, author links #209cee, superscripts #6fbf73 / #ed4b82, venue #f41c1c, navy #24427c, line #dbdfe6, soft #f4f6fa, correct #2e7d4f.

1. "Build a centred hero (container 960px, padding 48px 24px): 48px / 600 #363636 title with a small logo inline, 32px / 400 #4a4a4a subtitle, 20px author lines with #209cee links and coloured superscripts (#6fbf73, #ed4b82), a bold #f41c1c venue, then pill buttons: #363636 fill, #ffffff 16px text, padding 7px 20px, height 40px, fully rounded, 1em white SVG icon on the left."
2. "Make a stats row: six equal columns, each a centred 32px / 600 #363636 number above an 11px uppercase #4a4a4a label with 1px letter-spacing; no borders or cards."
3. "Create a quiz card: white, 1px #dbdfe6 border, 10px radius, padding 20px; a 16.8px #24427c stage label; a #f4f6fa question box (1px #dbdfe6, 8px radius, 600 weight, max 720px); a 2×2 grid (gap 12px) of image tiles with 1.5px #dbdfe6 borders, 8px radius, a #f4f6fa label strip, 4:3 images; hover border #24427c; on reveal the correct tile gets a #2e7d4f border and others fade to 50%."

## Similar Pages

- Nerfies and MathVista derived Bulma pages with centred heroes and dark rounded buttons.
- Dataset benchmark pages that lead with a big-number stats row.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --charcoal: #363636;
  --text: #4a4a4a;
  --author: #209cee;
  --affil-1: #6fbf73;
  --affil-2: #ed4b82;
  --venue: #f41c1c;
  --scb-navy: #24427c;
  --scb-green: #2e7d4f;
  --scb-red: #b3261e;
  --scb-line: #dbdfe6;
  --scb-soft: #f4f6fa;
  --band: #f5f5f5;
  --stripe: #fafafa;
  --font-body: "Noto Sans", sans-serif;
  --font-title: "Google Sans", Arial, sans-serif;
  --container: 1344px;
  --hero-container: 960px;
}
```

## Provenance

- **URL**: https://seeingculture-benchmark.github.io/
- **Paper**: Seeing Culture: A Benchmark for Visual Reasoning and Grounding (arXiv 2509.16517), Burak Satar, Zhixin Ma, Patrick A. Irawan, Wilfried A. Mulyawan, Jing Jiang, Ee-Peng Lim, Chong-Wah Ngo.
- **Venue**: EMNLP 2025 Main Conference.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: footer says the site is adapted from Nerfies and MathVista (CC BY-SA 4.0); `scb.css` adds the walkthrough styles.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and `bulma.min.css`, `index.css`, `leaderboard.css`, `scb.css` and `index.html` read directly, on 2026-10-28.
