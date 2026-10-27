# Oxblood Book Page — Style Reference

> A quiet monograph page: one serif column, oxblood ink for the links, and a table that blushes only at its own row.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the title block, gist, comparison table, BibTeX block and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's single hand-written `style.css` with its HTML. Positions are document coordinates at 1440px wide.

## Overview

GuideDog is a hand-built single-column page with no framework and no JavaScript beyond analytics. Everything is set in Crimson Pro on an off-white paper (#fdfdfc) carrying a barely visible two-layer dot grain. The title block is left-aligned in a 700px column: a tiny tracked uppercase venue line, a 30.4px semibold three-line title, authors in 18.88px with linked names in oxblood (#7a1f1f), italic grey affiliations, and a row of five plain text links separated by middle dots. A one-paragraph gist follows with a 2px oxblood rule on its left. Figures break out of the column to 780px or 920px. Below the teaser, a four-cell stat strip between two hairlines sets semibold lining numerals over italic grey labels, and an 860px comparison table uses only horizontal rules, with the "ours" row tinted 6% oxblood. Section headings are small (19.52px semibold) and each carries a short oxblood tick before it. It reads like a printed book page.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): paper #fcfcfb 71.9%, mauve-grey #a0899a 9.9% (the teaser photo and text anti-aliasing), warm rule grey #e2e1db 9.0% (paper grain and the teaser's light areas), white #fefefe 4.9%, cream #fffdeb 2.2% (teaser speech bubbles), remainder under 1.5%. There is no band or hero fill; the teaser image supplies the only strong colors (a navy title bar, pink and sky-blue callouts) at the bottom of the fold.

Anatomy in DOM order (y = top of element box, column x 370–1070):

1. **Venue line** (`p.venue`), y 64, "ACL 2026 MAIN", 12.48px/400, uppercase, letter-spacing 1.5px (0.12em), #555555, left. Gap 12px.
2. **Title** (`h1`), y 97, three forced lines (`br.title-br`), 30.4px/600, line-height 38px, #1a1a1a, left. Gap 10px.
3. **Authors** (`p.authors`), y 221, two lines at 18.88px/400, line-height 29.3px, #333333; linked names #7a1f1f with no underline; symbol superscripts (♣ ♢ ♡ ♠, *, †) at 0.7em. Gap 5px.
4. **Affiliations** (`p.affiliations`), y 285, 16.8px/400 italic, #555555, items joined by " · ". Gap 3px.
5. **Note** (`p.note`), y 316, "*Equal contribution · †Work done…", 14.72px/400, #555555. Gap 17px.
6. **Links** (`p.links`), y 357, "PDF · arXiv · Code · Data · BibTeX", 17.28px/400, links #7a1f1f with a 1px underline at 30% oxblood, word-spacing 0.25em, no icons. Gap 39px.
7. **Gist** (`p.gist`), y 425, 203px tall, 18.4px/400, line-height 28.5px, #2a2a2a, 2px solid #7a1f1f left border, 16px left padding; bold product names. Gap 32px.
8. **Teaser** (`figure.teaser.medium`), y 660, 780px wide centered (x 330), image 577px tall; italic caption below with a bold italic run-in "The task." The fold cuts the image.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Ink | #1a1a1a | `--ink` | Body text, title, section headings, table text, stat numerals, BibTeX text, table header bottom rule |
| Paper | #fdfdfc | `--paper` | Page background (under a dot grain of rgba(26,26,26,0.018) and 0.012) |
| Oxblood | #7a1f1f | `--link` (`--accent-oxblood`) | Author name links, link row, inline links, gist left rule, h2 tick, S1/S2/S3 labels in the standards box |
| Link Underline | rgba(122,31,31,0.3) | `color-mix(--link 30%)` | 1px bottom border under links; becomes solid #7a1f1f on hover |
| Author Grey | #333333 | `.authors` | Unlinked author names |
| Muted | #555555 | `--muted` | Venue line, affiliations, note line, figure captions, stat labels |
| Gist Ink | #2a2a2a | `.gist` | Gist paragraph text |
| Rule | #e5e3de | `--rule` | Stat-strip hairlines, table row rules, takeaway rule, footer top border |
| Ours Tint | #f5f0ef | `color-mix(--link 6%)` over paper | "GuideDog (ours)" table row background |
| Standards Fill | #f8f4f4 | `color-mix(--link 4%, --paper)` | Standards callout background |
| Standards Border | #c09e9b | `color-mix(--link 35%, --rule)` | Standards callout border, "ours" row bottom rule |
| Code Wash | #f5f4f0 | `--code-bg` | BibTeX `pre` background |
| Footer Grey | #777777 | `footer` | Footer text |

Declared but not visible: `--accent-royal` #1e3a8a, `--accent-yonsei` #003876 and `--accent-pure-royal` #4169e1 are alternative link colors in `:root`; only oxblood is wired to `--link`.

## Tokens — Typography

- **All text**: declared `"Crimson Pro", Georgia, "Times New Roman", serif` from Google Fonts (400, 400 italic, 600). Rendered: Crimson Pro 400, 400i, 600 (`fonts_loaded`). Body uses `font-feature-settings: "onum", "kern", "liga"` (oldstyle figures); the stat strip and table switch to `"lnum", "tnum"`. Substitute: EB Garamond (similar narrow old-style proportions; Georgia is wider).
- **Mono**: `"SFMono-Regular", ui-monospace, Menlo, Consolas, monospace` for the BibTeX block (system font, not loaded).

| Role | Selector | Size / line-height | Weight / style | Color |
|---|---|---|---|---|
| Venue eyebrow | `.title-block .venue` | 12.48px (0.78rem) / 20.6px, uppercase, 0.12em tracking | 400 | #555555 |
| Paper title | `h1` | 30.4px (1.9rem) / 38px | 600 | #1a1a1a |
| Section heading | `section > h2` | 19.52px (1.22rem) / 32.2px, -0.01em | 600 | #1a1a1a |
| Authors | `.title-block .authors` | 18.88px (1.18rem) / 29.3px | 400 | #333333, links #7a1f1f |
| Gist | `.gist` | 18.4px (1.15rem) / 28.5px | 400 | #2a2a2a |
| Body | `body, p` | 19px / 31.35px (1.65) | 400 | #1a1a1a |
| Link row | `.title-block .links` | 17.28px (1.08rem) / 28.5px | 400 | #7a1f1f |
| Affiliations | `.title-block .affiliations` | 16.8px (1.05rem) / 27.7px | 400 italic | #555555 |
| Takeaway | `.takeaway` | 16.8px (1.05rem) | 400 italic | #1a1a1a |
| Stat numeral | `.stats .num` | 24.8px (1.55rem) | 600, lining tabular | #1a1a1a |
| Table body | `table.comparison td` | 15.2px (0.95rem) / 22px | 400 | #1a1a1a |
| Table header | `table.comparison th` | 14.72px (0.92rem) / 21.3px | 600 | #1a1a1a |
| Caption | `figcaption` | 15.2px (0.95rem) / 23.6px | 400 italic | #555555 |
| Note | `.title-block .note` | 14.72px (0.92rem) / 24.3px | 400 | #555555 |
| Stat label | `.stats .lbl` | 13.76px (0.86rem) / 1.4 | 400 italic | #555555 |
| BibTeX | `pre` | 12.8px (0.8rem) / 19.2px | 400 | #1a1a1a |
| Footer | `footer` | 12.8px (0.8rem) / 21.1px | 400 | #777777 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Gist | 0 | 2px solid #7a1f1f left only | none |
| Links | 0 | 1px bottom rgba(122,31,31,0.3); hover #7a1f1f | none |
| Stat strip (`ul.stats`) | 0 | 1px #e5e3de top and bottom | none |
| Table header cells | 0 | 1px solid #1a1a1a bottom | none |
| Table body cells | 0 | 1px solid #e5e3de bottom | none |
| Standards callout | 3px | 1px solid #c09e9b | none |
| BibTeX `pre` | 2px | none | none |
| Footer | 0 | 1px #e5e3de top | none |
| Images | 0 | none | none |

No shadows anywhere; the only rounding is 2–3px.

## Layout Metrics

- **Column**: `main.page` max-width 740px, centered, padding 64px 20px 96px, so text runs x 370–1070 (700px).
- **Breakout figures**: `figure.medium` max-width 780px and `figure.wide` max-width 920px, centered on the viewport with `margin-left: 50%; transform: translateX(-50%)`; their captions stay at 740px max. Figure margin 32px top and bottom.
- **Comparison table**: `.table-wrap` max-width 860px, same breakout trick (x 290–1150), margin 16px top, 38.4px bottom; cells padded 11.2px, header bottom padding 8.8px.
- **Stat strip**: 4-column grid, gap 12px, padding 16px 0, margin 24px 0 32px.
- **Section rhythm**: h2 margin 41.6px top, 11.2px bottom; paragraphs 16px bottom. Title block bottom margin 40px; gist margin 24px 0 32px.
- **Footer**: margin-top 64px, padding-top 19.2px. Rendered height about 5,910px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >920px | 20px inside a 740px column | 19px | 30.4px | figures and table break out to 780/860/920px |
| 641–920px | 20px | 19px | 30.4px | `figure.wide` (≤920) then table (≤860) and `figure.medium` (≤780) fall back to column width |
| ≤640px | 17.6px (padding 40px 17.6px 64px) | 17px | 24px (1.5rem), title line breaks removed | h2 17.6px; stats 2×2 grid; table scrolls horizontally with a sticky first column and a right-edge fade mask; BibTeX 11.5px |

## Components

- **Venue eyebrow**: `p.venue` Crimson Pro 12.48px/400, uppercase, letter-spacing 0.12em, #555555, margin-bottom 12.8px. No pill, no fill.
- **Text link row**: links separated by literal " · ", 17.28px, #7a1f1f, padding 0.15em 0.05em, 1px bottom border rgba(122,31,31,0.3) turning solid #7a1f1f on hover; word-spacing 0.25em. No icons, no buttons.
- **Gist**: a single paragraph at 18.4px/1.55 #2a2a2a with a 2px #7a1f1f left border and 16px left padding; product names bold 600.
- **Section heading with tick**: `h2` 19.52px/600, letter-spacing -0.01em, preceded by a `::before` 0.7em × 1px #7a1f1f line at 85% opacity, 0.55em right margin.
- **Stat strip**: `ul.stats` 4-column grid between 1px #e5e3de hairlines; each cell centered, numeral 24.8px/600 lining tabular #1a1a1a, label 13.76px italic #555555 below with 3.2px gap.
- **Comparison table**: full-width collapse table, 15.2px, no vertical rules, no header fill; header 14.72px/600 with a 1px #1a1a1a rule; rows ruled 1px #e5e3de; the "ours" row (`tr.ours`) has #f5f0ef fill and a #c09e9b bottom rule with bold values.
- **Standards callout**: `div.standards-box` #f8f4f4 fill, 1px solid #c09e9b border, 3px radius, padding 14.4px 17.6px 9.6px; each line 15.2px with an oxblood 600 label ("S1") of min-width 1.7em.
- **Takeaway**: italic 16.8px #1a1a1a paragraph with a 1px #e5e3de top rule and 14.4px top padding.
- **BibTeX**: `pre` #f5f4f0, 2px radius, padding 16px 17.6px, monospace 12.8px/1.5.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue line | yes | tracked uppercase 12.48px grey text, no badge |
| Title and authors | yes | left-aligned, symbol-keyed affiliations in italic |
| Link buttons | present but non-standard | dot-separated oxblood text links, no buttons or icons |
| TL;DR / gist | yes | left-ruled paragraph replacing an abstract |
| Abstract | absent from the source | the gist stands in for it |
| Teaser figure | yes | 780px breakout image, italic caption with run-in label |
| Stat strip | yes | four numerals between hairlines |
| Comparison table | yes | rule-only HTML table, own row tinted |
| Callout box | yes | standards box with oxblood labels |
| Method / data figures | yes | 920px and 780px breakout figures |
| Findings and takeaway | yes | paragraphs plus an italic ruled takeaway |
| BibTeX | yes | warm-grey `pre` |
| Navigation, videos | absent from the source | none |
| Footer | yes | 12.8px grey line above a hairline |

## Adapting to Other Content

- **More authors**: keep the inline paragraph with symbol superscripts and a manual `<br>` every four or five names; switch symbols to numbers past four affiliations. Do not center.
- **A results table**: reuse `table.comparison` at 860px breakout, best values bold 600, the proposed method row as `tr.ours` with #f5f0ef fill. Never add vertical rules or a header fill.
- **More links**: extend the dot-separated text row; no icons.
- **Videos**: place them in `figure.medium` at 780px with an italic caption; no rounded frames.
- **Long publication lists or news**: plain paragraphs with an italic grey date or venue (16.8px #555555) and oxblood title links; separate groups with an h2 and its tick.
- **More numbers**: the stat strip holds four cells per row at desktop and two on phones; keep labels lowercase italic.

## Do's and Don'ts

- Do keep everything in one serif family and one accent, #7a1f1f.
- Do use oldstyle figures in prose and lining tabular figures in stats and tables.
- Do let figures and the table break out of the 700px text column while captions stay narrow.
- Do mark sections with the small oxblood tick, not with rules or bands.
- Don't center the title block or use buttons, pills, icons or shadows.
- Don't fill table headers or add zebra striping; only the "ours" row gets a tint.
- Don't enlarge section headings; they sit barely above body size by design.

## Surfaces

One surface: off-white paper #fdfdfc with a faint 3px and 7px dot grain. Tinted insets are limited to the standards callout (#f8f4f4), the "ours" table row (#f5f0ef) and the BibTeX block (#f5f4f0). No cards, no shadows.

## Imagery

Brightly colored paper figures (navy title bars, pink and sky-blue speech callouts, cartoon BLV user icon) over street photographs; a world map of locations; an annotated example frame; QA examples. Images sit unframed with italic captions; their saturation is the page's only loud color.

## Layout

A single left-aligned 700px reading column centered in the viewport, with figures and the table breaking out symmetrically to 780–920px. The rhythm is text, figure, numbers, table, callout, figures, findings, citation, footer, in one vertical flow with no grid beyond the stat strip.

## Agent Prompt Guide

Quick colors: ink #1a1a1a, paper #fdfdfc, accent #7a1f1f, muted #555555, rules #e5e3de, code #f5f4f0, ours-row #f5f0ef.

1. "Build a left-aligned title block in a 700px column on #fdfdfc: an uppercase 12.48px Crimson Pro venue line in #555555 with 0.12em tracking; a 30.4px/38px weight-600 #1a1a1a title; authors at 18.88px #333333 with linked names in #7a1f1f; italic 16.8px #555555 affiliations; then 'PDF · arXiv · Code · Data · BibTeX' as 17.28px #7a1f1f links with a 1px rgba(122,31,31,0.3) underline that turns solid on hover."
2. "Add a stat strip: a 4-column grid between 1px #e5e3de top and bottom rules, 16px vertical padding; each cell centered with a 24.8px weight-600 lining tabular numeral in #1a1a1a and a 13.76px italic #555555 label beneath."
3. "Add a comparison table 860px wide, centered beyond the text column: Crimson Pro 15.2px, cells padded 11.2px, header 14.72px/600 with a 1px #1a1a1a bottom rule, body rows ruled 1px #e5e3de, no vertical lines; the proposed row filled #f5f0ef with a #c09e9b bottom rule and bold values."

## Similar Pages

- Tufte-style and "academic book page" templates (single serif column, sidenote restraint).
- Hand-written minimal project pages that avoid the Nerfies template entirely.

## Quick Start

```css
:root {
  --ink: #1a1a1a;
  --paper: #fdfdfc;
  --muted: #555555;
  --rule: #e5e3de;
  --code-bg: #f5f4f0;
  --link: #7a1f1f;
  --ours: #f5f0ef;
  --font: "Crimson Pro", Georgia, "Times New Roman", serif;
  --font-mono: "SFMono-Regular", ui-monospace, Menlo, Consolas, monospace;
  --body-size: 19px;
  --body-lh: 1.65;
  --title-size: 1.9rem;
  --h2-size: 1.22rem;
  --column: 740px;
}
body { background: var(--paper); color: var(--ink); font: var(--body-size)/var(--body-lh) var(--font); font-feature-settings: "onum", "kern", "liga"; }
```

## Provenance

- **URL**: https://jun297.github.io/GuideDog/
- **Paper**: GuideDog: A Real-World Egocentric Multimodal Dataset for Blind and Low-Vision Accessibility-Aware Guidance (arXiv 2503.12844), Junhyeok Kim et al. (Yonsei University and others).
- **Venue**: ACL 2026 Main.
- **Selection reason**: existing verified entry (entries.json); arXiv 2503.12844 comment "ACL 2026 Main". Chosen for its book-page reading: narrow serif column, oxblood links, ruled gist, italic stat labels and a restrained comparison table with its own row highlighted.
- **Template credit**: none; the footer says the page source is on GitHub and free to fork.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, the first-viewport screenshot and scaled full-page capture, `style.css` and `index.html`. Date 2026-10-28.
