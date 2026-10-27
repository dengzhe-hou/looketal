# Ink Pill Inter Clean — Style Reference

> A crisp white product page: a blue announcement strip, ink-black pill buttons and every figure on a soft-shadowed card.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the announcement bar, sticky nav, hero, buttons, teaser, sections, tables, code and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `style.css` (about 11 KB) with its HTML. Positions are document coordinates at 1440px wide.

## Overview

PairCoder++ is a hand-written single page built on one small stylesheet and Inter throughout. A full-width blue gradient strip announces "🏆 Accepted to ACL 2026 (Findings)". Below it a white sticky nav holds a bold "PairCoder++" wordmark and seven grey section links. The hero is centered on white with a faint blue radial glow at the top: a solid blue "ACL 2026 · Findings" pill beside a blue uppercase subtitle, a 30.4px weight-800 title with tight tracking, three rows of author names with blue superscripts, four rows of grey affiliations, and four ink-black pill buttons with white icons. The teaser is a framed two-panel result figure (bar chart and render thumbnails) on a 14px-radius card with a soft double shadow, followed by a strip of five pale stat tiles with dark-blue numerals. Sections are separated by 1px #e2e8f0 rules and alternate white with #f6f8fb, each with a 27.2px weight-800 heading; results use ink-headed tables with green "win" cells, an interactive Chart.js explorer, tabbed galleries and a dark navy BibTeX block.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 66.9%, banner blue #2c599e 7.8% (announcement strip and teaser bars), cool grey #b1bfc7 7.3% (text anti-aliasing, figure lines), near-white #fafbfd 6.9% (hero glow), #fdfdfe 4.9%, light grey #f1f4f6 4.8% (teaser figure fills), remainder under 1.5%.

Anatomy in DOM order (y = top of element box):

1. **Announcement bar** (`.accepted-bar`), y 0, full width, 42px tall, `linear-gradient(90deg, #1450b0, #1f6feb)`, Inter 14.72px/600 white, centered, padding 9px 16px, with a 🏆 emoji. Scrolls away.
2. **Sticky nav** (`nav.topnav`), y 42, 1440×51, rgba(255,255,255,0.85) with saturate(180%) blur(10px), 1px #e2e8f0 bottom border; inner row 1080px max (x 180–1260), padding 11px 24px, space-between.
3. **Wordmark** (`a.brand`), x 204, "PairCoder++", Inter 16.8px/800 #10202e. **Nav links** right, Inter 14.4px/500 #43586a, gap 22px, hover #1f6feb. Gap to hero content 62px.
4. **Venue row** (`p.venue`), y 155: a solid pill (`.acl-badge`, Inter 11.84px/700, white on #1f6feb, padding 3px 11px, radius 999px) then "CODE-DRIVEN MULTIMODAL & STRUCTURED-ARTIFACT GENERATION" in Inter 12.48px/600 uppercase, letter-spacing 0.04em, #1f6feb. Gap 14px.
5. **Title** (`h1.title`), y 195, max-width 1000px, two lines, Inter 30.4px/800, line-height 38px, letter-spacing -0.67px (-0.022em), #10202e, centered. Gap 24px.
6. **Authors** (`.authors`), y 295, flex-wrap centered in 720px, gap 6px 22px, Inter 16.64px/400 #10202e, line-height 1.3; numeric superscripts 0.62em/600 #1f6feb. Three rows. Gap 14px.
7. **Affiliations** (`.affil`), max-width 760px, Inter 14.08px #43586a, line-height 1.85, superscripts #1f6feb, items joined by " · ", four rows. Gap 22px.
8. **Buttons** (`.buttons`), y 532, four pills 47px tall, gap 12px: "Paper", "Code", "arXiv", "Cite", Inter 14.88px/600 white on #10202e, padding 11px 20px, 16px white icons on the left, shadow 0 1px 2px rgba(16,32,46,0.06), 0 8px 24px rgba(16,32,46,0.06). Hero bottom padding 30px; teaser section top padding 34px.
9. **Teaser** (`section.teaser figure`), y 642, image 1032×605 at x 204: white, 1px #e2e8f0 border, radius 14px, same soft shadow. The fold falls inside it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| White | #ffffff | `--bg` | Page, nav glass base, cards, table wrapper, explorer, figure backgrounds |
| Alt Band | #f6f8fb | `--bg-alt` | `.block.alt` sections (Framework, Gallery), stat tiles, segmented track, family rows in the grid |
| Ink | #10202e | `--ink` | Title, headings, authors, wordmark, button fill, table header row fill |
| Ink Hover | #000000 | `.btn:hover` | Button fill on hover |
| Ink Soft | #43586a | `--ink-soft` | Nav links, affiliations, leads, card text, captions, footer, inactive tabs |
| Line | #e2e8f0 | `--line` | Nav bottom border, section top rules, figure and card borders, table row rules, tab borders |
| Brand Blue | #1f6feb | `--brand` | Venue pill, subtitle, superscripts, links, active tab and segment, card icon squares, nav hover |
| Brand Dark | #1450b0 | `--brand-dark` | Stat numerals, left stop of the announcement gradient |
| Win Fill | #e2f2e4 | `--win-bg` | Winning cells in the results table, copied state of the copy button |
| Win Ink | #13662a | `--win-ink` | Text in winning cells |
| Improve Cell | #dcf0df | `td.cell.imp` | Improved cells in the full results grid |
| Regress Cell | #fbe2e2 | `td.cell.reg` | Regressed cells in the full results grid |
| Code Chip | #eef2f7 | `code` | Inline code background |
| Bib Navy | #0d1b27 | `pre.bib` | BibTeX block background |
| Bib Text | #e6edf3 | `pre.bib` | BibTeX text |
| Row Hover | #f3f7fc | `tbody tr:hover td` | Results table row hover |

## Tokens — Typography

- **All text**: declared `"Inter", system-ui, -apple-system, Segoe UI, Roboto, sans-serif`. Rendered: Inter 400, 500, 600, 700, 800 (`fonts_loaded`). Substitute: Roboto (close metrics, slightly narrower).
- **Mono**: `"JetBrains Mono", ui-monospace, Menlo, monospace` for inline code, numeric table columns and BibTeX; rendered JetBrains Mono 400 and 500.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `.title` | 30.4px / 38px, -0.022em | 800 | #10202e |
| Section heading | `.block h2` | 27.2px / 44.9px, -0.015em | 800 | #10202e |
| Stat numeral | `.stat .num` | 24px, -0.01em | 800 | #1450b0 |
| Abstract | `#abstract p` | 16.8px / 1.65 | 400 | #10202e |
| Wordmark | `.brand` | 16.8px | 800 | #10202e |
| Authors | `.authors` | 16.64px / 1.3 | 400 | #10202e |
| Card title | `.card h3` | 16.64px / 27.5px | 700 | #10202e |
| Lead | `.lead` | 16.32px | 400 | #43586a |
| Body | `body` | 16px / 26.4px | 400 | #10202e |
| Button | `.btn` | 14.88px | 600 | #ffffff |
| Banner | `.accepted-bar` | 14.72px, 0.01em | 600 (strong 800) | #ffffff |
| Results table | `table.results` | 14.72px (numbers 13.44px mono) | 400, header 600 | #10202e, header #ffffff |
| Nav link, caption | `.nav-links a`, `figcaption` | 14.4px | 500 / 400 | #43586a |
| Affiliations | `.affil` | 14.08px / 1.85 | 400 | #43586a |
| Venue subtitle | `.venue` | 12.48px, uppercase, 0.04em | 600 | #1f6feb |
| Venue pill | `.acl-badge` | 11.84px, 0.03em | 700 | #ffffff |
| Stat label | `.stat .lbl` | 13.12px | 400 | #43586a |
| Grid table | `table.pc-grid` | 12.8px (cells 11.84px mono) | 400 | #10202e |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons (`.btn`) | 999px | none | `--shadow`: 0 1px 2px rgba(16,32,46,0.06), 0 8px 24px rgba(16,32,46,0.06) |
| Venue pill, tabs, segmented control, copy button | 999px | tabs and copy 1px #e2e8f0 | none |
| Figures, cards, table wrapper, explorer, BibTeX | 14px (`--radius`) | 1px #e2e8f0 (BibTeX none) | `--shadow` |
| Stat tile | 14px | 1px #e2e8f0 | none |
| Card icon square | 9px | none | none |
| Inline code | 5px | none | none |
| Select inputs | 9px | 1px #e2e8f0; focus #1f6feb with 3px rgba(31,111,235,0.15) ring | none |

## Layout Metrics

- **Container**: `.container` max-width 1080px, padding 0 24px, so content spans x 204–1236 (1032px). `.narrow` reduces it to 820px (772px of text) for the Abstract.
- **Hero**: padding 62px 0 30px; title max 1000px; authors max 720px; affiliations max 760px; button gap 12px.
- **Teaser**: section padding 34px 0 8px; figure full container width; caption 14.4px #43586a, 12px above.
- **Stats**: section padding 26px 0; five equal tiles, gap 14px, tile padding 18px 14px.
- **Sections** (`.block`): padding 60px 0, 1px #e2e8f0 top rule; h2 margin-bottom 14px; lead max-width 780px, 28px below; wide figures 34px below.
- **Cards**: three columns, gap 18px, padding 22px. **Two-column figures**: gap 24px, 36px above.
- **Explorer**: white card, padding 22px; chart box 420px tall.
- Rendered height about 8,540px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >880px | 24px inside a 1080px container | 16px | 30.4px | five stat tiles, three cards, two-column figures |
| ≤880px | 24px | 16px | 27.2px (1.7rem) | nav links hidden (wordmark only); stats 2 per row; cards and two-column figures stack |

## Components

- **Announcement bar**: full-width `linear-gradient(90deg, #1450b0, #1f6feb)`, white Inter 14.72px/600 centered, padding 9px 16px, emoji prefix, bold (800) key phrase.
- **Ink pill button**: inline-flex, gap 8px, #10202e fill, white Inter 14.88px/600, padding 11px 20px, radius 999px, 16px white icon on the left, `--shadow`; hover fill #000000 and translateY(-1px).
- **Venue pill + kicker**: `.acl-badge` solid #1f6feb pill (11.84px/700 white, padding 3px 11px) followed 10px later by an uppercase 12.48px/600 #1f6feb line.
- **Framed figure**: image width 100%, white, 1px #e2e8f0 border, 14px radius, `--shadow`; caption 14.4px #43586a with a bold lead sentence.
- **Stat tile**: #f6f8fb, 1px #e2e8f0, 14px radius, padding 18px 14px, centered; numeral 24px/800 #1450b0, label 13.12px #43586a, 4px gap.
- **Feature card**: white, 1px #e2e8f0, 14px radius, padding 22px, `--shadow`; 32px #1f6feb icon square (9px radius, white glyph), 16.64px/700 title, 14.88px #43586a text.
- **Results table**: in a white 14px-radius wrapper with `--shadow`; header row #10202e with white 600 text, sticky; cells padded 10px 14px with 1px #e2e8f0 rules; numeric columns JetBrains Mono 13.44px; winning cells #e2f2e4 with #13662a 600 text; row hover #f3f7fc.
- **Tabs and segmented control**: pills, 1px #e2e8f0 border, #43586a 600 text; active #1f6feb fill, white text; segmented track #f6f8fb with 3px padding.
- **BibTeX**: `pre.bib` #0d1b27, #e6edf3 JetBrains Mono 13.76px/1.6, 14px radius, padding 20px 22px, `--shadow`; a white pill "Copy" button below that turns #e2f2e4 when done.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Announcement bar | yes | blue gradient strip with trophy emoji |
| Sticky nav | yes | white glass, bold wordmark, grey links |
| Venue badge | yes | blue pill plus uppercase subtitle |
| Title, authors, affiliations | yes | centered, numeric blue superscripts |
| Link buttons | yes | four ink-black pills with icons |
| Teaser figure | yes | framed two-panel result figure |
| Stat strip | yes | five pale tiles with dark-blue numerals |
| Abstract | yes | 820px narrow column, 16.8px |
| Method figure and cards | yes | framed figure plus three icon cards on the alt band |
| Results table | yes | ink header, green win cells |
| Interactive explorer | yes | Chart.js chart, segmented control, selects, heat-colored full grid |
| Qualitative gallery | yes | tabbed image panels |
| BibTeX | yes | dark navy block with copy button |
| Videos | absent from the source | none |
| Footer | yes | centered 14.4px #43586a text above a rule |

## Adapting to Other Content

- **More authors**: the 720px flex-wrap list absorbs them; use `.break` elements to control rows and keep blue numeric superscripts.
- **Fewer stats**: the tile grid is fixed at five columns; with three or four numbers set `repeat(n, 1fr)` and keep tile styling.
- **Videos**: put them in the same framed card (14px radius, 1px #e2e8f0, `--shadow`) at full container width or in the two-column grid.
- **Long publication lists or news**: a white card list with 14px radius, a bold 16.64px title, #43586a meta line and #1f6feb links; separate years with an h2 on alternating bands.
- **More links**: add ink pills to the centered row; reserve no other button colors.
- **Comparisons with losses**: reuse the grid's #dcf0df improve, #fbe2e2 regress and #f7f8fa missing cell fills.

## Do's and Don'ts

- Do keep Inter everywhere, with 800 for title, headings, wordmark and numerals.
- Do frame every figure, table and code block with 14px radius, a 1px #e2e8f0 border and the soft double shadow.
- Do alternate white and #f6f8fb section bands, each opened by a 1px #e2e8f0 rule.
- Do make action buttons ink pills; use #1f6feb only for small accents, pills and active states.
- Don't color the hero background beyond the faint 10% blue radial glow.
- Don't use serif type or italic display styles.
- Don't put text directly on the blue except in the announcement bar and pills.

## Surfaces

White page with a blue gradient strip on top, a faint radial glow (rgba(31,111,235,0.1)) behind the hero, alternating #f6f8fb bands, white cards and frames with soft shadows, #f6f8fb stat tiles, a #10202e table header row and a #0d1b27 BibTeX block.

## Imagery

Paper figures throughout: a two-panel teaser with horizontal bar charts (blue, green, red, gold and purple domain groups) and rendered artifact thumbnails (3D surfaces, spirals, TikZ, CAD rings, SVG icons); a cartoon Driver/Navigator framework diagram; qualitative galleries of target, reference and generated renders. All framed on white.

## Layout

A 1080px container with a centered hero and left-aligned section content; the abstract narrows to 820px. Content is full-width figures, a five-tile stat strip, three-card grids and two-column figure pairs, with horizontally scrollable tables. Sections stack as full-bleed bands.

## Agent Prompt Guide

Quick colors: page #ffffff, band #f6f8fb, ink #10202e, soft ink #43586a, line #e2e8f0, blue #1f6feb, dark blue #1450b0, win #e2f2e4 / #13662a, BibTeX #0d1b27.

1. "Build a centered hero on white with a radial-gradient(1100px 380px at 50% -120px, rgba(31,111,235,0.1), transparent 70%) glow: a #1f6feb pill reading 'ACL 2026 · Findings' (Inter 11.84px/700 white, padding 3px 11px) followed by an uppercase 12.48px/600 #1f6feb subtitle; 14px below, an Inter 30.4px weight-800 #10202e title with -0.022em tracking; authors 16.64px #10202e with #1f6feb superscripts; affiliations 14.08px #43586a at line-height 1.85."
2. "Add four pill buttons 12px apart: #10202e fill, white Inter 14.88px/600, padding 11px 20px, radius 999px, a 16px white icon on the left, shadow 0 1px 2px rgba(16,32,46,0.06), 0 8px 24px rgba(16,32,46,0.06); hover fill #000000 and lift 1px."
3. "Add a stat strip of five equal tiles with 14px gaps: background #f6f8fb, 1px #e2e8f0 border, 14px radius, padding 18px 14px, centered numeral Inter 24px/800 #1450b0 over a 13.12px #43586a label."

## Similar Pages

- Modern SaaS-style research pages with an announcement strip and ink pill buttons.
- Project pages that add an interactive Chart.js results explorer under a static table.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-alt: #f6f8fb;
  --ink: #10202e;
  --ink-soft: #43586a;
  --line: #e2e8f0;
  --brand: #1f6feb;
  --brand-dark: #1450b0;
  --win-bg: #e2f2e4;
  --win-ink: #13662a;
  --max: 1080px;
  --radius: 14px;
  --shadow: 0 1px 2px rgba(16, 32, 46, .06), 0 8px 24px rgba(16, 32, 46, .06);
  --font: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, Menlo, monospace;
}
.accepted-bar { background: linear-gradient(90deg, #1450b0, #1f6feb); color: #fff; }
```

## Provenance

- **URL**: https://yisuanwang.github.io/PairCoder/
- **Paper**: PairCoder++: Pair Programming as a Universal Paradigm for Verified Code-Driven Multimodal and Structured-Artifact Generation (arXiv 2607.01883), Junhao Chen et al. (Tsinghua University and others).
- **Venue**: ACL 2026 (Findings, per the page's banner and badge).
- **Selection reason**: arXiv 2607.01883 comment states acceptance at ACL 2026; project page linked in the comment. Chosen as a clean modern template made its own: announcement bar, well-set hero, framed two-panel teaser, stat-tile strip and a comfortable abstract measure.
- **Template credit**: none stated; custom stylesheet.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, the first-viewport screenshot and scaled full-page capture, `style.css` and `index.html`. Date 2026-10-28.
