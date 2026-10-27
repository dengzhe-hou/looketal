# Peach Serif Split Hero — Style Reference

> A physics textbook cover in sunset peach, with a bouncing-ball experiment running beside it.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the header, key-point rows, buttons, teaser video, byline, answer lines, article text, lists, table, figures and appendix, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/css/style.css` and inline `<style>` over the Distill v2 template. Positions are document coordinates at 1440px wide. The page declares Charter, which is not installed on the Windows render machine, so the render shows the default serif (Times New Roman); see Typography.

## Overview

PhyWorld uses the same Cambrian-style Distill template as several project pages but turns the header white. The split hero puts an oversized bold serif title in peach (#feae6f) on the left with an italic peach subtitle ("— A Physical Law Perspective"). Under them come a black intro sentence and six rows of line-art icons with bold run-in labels, a community link in dark blue and four butter-yellow pills. The right half is a 600px square autoplay video of a 2D physics simulator (red and blue balls in grey-framed panels). Below a full-width hairline, the Distill article opens with a ruled byline (dark green author names, plain "ICML 2025", italic "Bytedance Seed"). Two centered 24px answer lines follow, the second in orange italic, and then an embedded YouTube video. The body after that gets busier: 👉 emoji with pure-blue bold labels, a contents list with § links, a collapsible wall of embedded tweets, many figures and videos, and a small table with pale-green highlighted cells.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 60.0%, simulator near-white #fcfffc 19.3%, simulator frame grey #d9cfcb 11.6%, other near-white simulator tones 9.1%. The peach title, the black text and the colored balls are below 1% each in the quantization. The header is white; the only frame is the video's own grey panel border.

Anatomy in DOM order (y = top of element box):

1. **Title** (`.header-content h1`, inline `font-size: xxx-large`), y 50, three left-aligned lines at x 50 in a 593px column, serif 48px/700, line-height 57.6px, #feae6f. Gap 24px.
2. **Subtitle** (`.header-content h2 > i`), y 247, one line, serif 32px/700 italic, line-height 38.4px, #feae6f, starting with an em dash. Gap 16px.
3. **Intro** (`.header-container p`), y 301, 19.2px/25.6px, #000000, with a bold italic phrase ("data and model scaling"). Gap 20px.
4. **Key-point rows** (`.icon-item`), y 372 to 711, six rows 51–55px tall with about 15px between them: a 30px line-art SVG icon (16px right margin), then 16px/25.6px black text with a bold 700 run-in label and a colon; the last row ("Community") ends in an underlined #004276 link. Gap 25px.
5. **Pill buttons** (`.button-container a.button`), y 736, four pills centered under the text column: arXiv (Academicons), pdf (file-pdf), Code (GitHub), Data (🤗 emoji), each 50px tall.
6. **Teaser video** (`video.no-controls`), right column, x 745, y 120, 600×600, autoplay muted with controls hidden by CSS; four grey-framed simulator panels. Header ends at y 861, followed by a full-width 1px rgba(0,0,0,0.1) rule.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Sunset Peach | #feae6f | `.header-content h1/h2` | Title and subtitle |
| Ink | #000000 | `.header-content { color: black }` | Hero text, run-in labels, pill labels, author note |
| Article Ink | rgba(0,0,0,0.8) | Distill `d-article` | Byline, body text, lists, "The Answer:", section titles, table text |
| Caption Grey | rgba(0,0,0,0.6) | Distill `figcaption` | Figure captions |
| Appendix Grey | rgba(0,0,0,0.5) | Distill `d-appendix` | Appendix text |
| Rule Grey | rgba(0,0,0,0.1) | `hr`, `.byline`, `d-appendix` | Full-width section rules, byline bottom rule, appendix top rule |
| Butter Pill | #fff0ce | `.button-container a.button`, `.collapse-btn` | Pill fill, Display / Hide button fill |
| Amber Edge | rgba(255,193,7,0.5) | pill border | 2px pill and collapse-button border |
| Toasted Peach | #eab682 | pill hover | Pill and collapse-button hover fill (text turns white) |
| Community Blue | #004276 | link color | Underlined "Click to view the lively discussions…" link |
| Author Green | #006400 | inline `color: darkgreen` | Byline author names |
| Answer Orange | #ffa500 | inline `color: orange` | Italic answer headline |
| Label Blue | #0000ff | inline `color: blue` | 👉 "What?", "Why?", "How?", "Key Messages" labels |
| Highlight Green | #e6ffe6 | `.highlight` | Highlighted table cells |
| Table Header Grey | #f2f2f2 | `.tb-hdr` | Table header cells |
| White | #ffffff | `.header-wrapper` | Header and page background |

## Tokens — Typography

- **All text**: `body { font-family: Charter }` with no fallback and no webfont, so Charter renders only where it is installed (macOS ships it); on Windows and Linux the browser default serif renders instead (Times New Roman in this capture). Substitute: Charis SIL or "Bitstream Charter" from a webfont host, since both keep Charter's proportions; add `serif` as fallback.
- **Math**: KaTeX 0.10.2 and MathJax 3 are both loaded (KaTeX_Main and KaTeX_Math faces rendered).
- **Icons**: Font Awesome 6 (Free 900) and Academicons in the pills; line-art SVG files for the hero key points.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Title | `.header-content h1` (inline xxx-large) | 48px / 57.6px | 700 | #feae6f |
| Subtitle | `.header-content h2 i` | 32px / 38.4px italic | 700 | #feae6f |
| Intro | `.header-container p` | 19.2px / 25.6px | 400 | #000000 |
| Key point | `.icon-item div` | 16px / 25.6px | 400, label 700 | #000000 |
| Pill label | `.button-container a.button` | 16px / 25.6px | 700 | #000000 |
| Author name | `.author-link` | 20.352px / 36.8px | 400 | #006400 |
| Answer lines | `h1.text.abstract` (inline x-large) | 24px / 28.8px | 700, second line italic | rgba(0,0,0,0.8), then #ffa500 |
| Lead paragraph | `p.text` with 👉 | 21.6px / 28.8px | 400, label 700 | rgba(0,0,0,0.8), label #0000ff |
| Section title | `h2.text` | 30.528px / 38.16px | 600 | rgba(0,0,0,0.8) |
| List item | `d-article li` | 19.2px / 28.8px | 400, italic bold run-in | rgba(0,0,0,0.8) |
| Body | `d-article p` | 16.96px / 28.8px | 400 | rgba(0,0,0,0.8) |
| Caption | `figcaption` | 19.08px / 28.62px | 400 | rgba(0,0,0,0.6) |
| Table | `.data-table td/th` | 15px / 18.75px | 400, first column 700 | rgba(0,0,0,0.8) |
| Appendix | `d-appendix` | 12.8px / 21.76px | 400 | rgba(0,0,0,0.5) |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill button | 20px | 2px solid rgba(255,193,7,0.5) | none |
| Collapse button | 20px | 2px solid rgba(255,193,7,0.5) | none |
| Teaser video | 0 | none (the grey frame is in the video) | none |
| Byline | 0 | 1px rgba(0,0,0,0.1) bottom | none |
| Section rule (`hr`) | 0 | 1px rgba(0,0,0,0.1), full width, margin 60px 0 | none |
| Table | 0 | `border-spacing: 2.5px`, no cell borders | none |

## Layout Metrics

- **Header**: `.header-container` flex row at ≥600px, padding 50px, `max-width: 1600px`; `.header-content` `max-width: calc(45% - 10px)` (593px at 1440px), `.header-image` `max-width: calc(53% - 20px)` with the video at 87% of it (600px). Header height 861px.
- **Article grid**: Distill v2. At ≥1180px the text column is 704px at x 368; `.text` elements (width 150%, margin-left -20%) break out to 1056px at x 227, which is where the answer lines, the YouTube embed, the lead paragraphs, lists and figures sit.
- **YouTube embed**: `.text.video-container`, `padding-bottom: 35%`, iframe absolutely filling it (1056×642 measured with Distill's own padding).
- **Sections**: separated by full-width `hr` with 60px margins; section titles 30.5px with 16px bottom padding.
- **Tweets**: `#twitter_container`, CSS columns 250px wide with 20px gaps, toggled by the Display / Hide pill.
- **Table**: `.data-table` full text width (704px), `border-spacing: 2.5px`, cells padded 3.75px; drops to 0.8em on small screens.
- **Appendix**: margin-top 60px, padding 60px 0 48px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1180px | Distill outer 1fr | 16.96px | 48px | text 704px, breakouts 1056px |
| 1000–1179px | Distill outer 1fr | 16.96px | 48px | Distill 50px columns |
| 769–999px | Distill outer 1fr | Distill default | 48px | Distill 45px columns |
| 600–768px | 50px header padding (later ≥600px rule wins) | Distill default | 48px (inline size wins) | subtitle 27.2px, no wrap; `.text` breakouts drop to 100% |
| <600px | 16px header padding, 32px top | Distill default | 48px | header stacks; video centered at 90%; icons gain 16px bottom margin |

## Components

- **Split hero**: white, flex row, text column 45% and media column 53%, vertically centered. Title and subtitle in peach serif; everything else black.
- **Icon key-point row**: flex row, 30px line-art SVG icon with 16px right margin, then a 16px/25.6px line beginning with a bold label and a colon; italic emphasis for law names.
- **Butter pill**: `a.button`, #fff0ce fill, 2px solid rgba(255,193,7,0.5) border, 20px radius, padding 10px 20px, margin 5px 2px, 16px/700 black label with icon left; hover #eab682 fill, white text, 0.3s transition. The same recipe is reused for the "Display / Hide" `.collapse-btn` inside a section title.
- **Ruled byline**: centered, author names in #006400 20.352px with superscript stars and em-space separators, then plain "ICML 2025", italic "Bytedance Seed" and a small black note, closed by a 1px rgba(0,0,0,0.1) rule.
- **Answer headline pair**: two centered 24px/700 lines, a plain "The Answer:" in rgba(0,0,0,0.8) and an italic statement in #ffa500, at breakout width.
- **Emoji lead paragraph**: 👉 then a bold #0000ff label ("What?") and two spaces, then 21.6px body text.
- **Highlighted result table**: `.data-table`, 15px serif, tabular numbers centered, first column right-aligned and bold, `.tb-hdr` header cells on #f2f2f2, winning cells on #e6ffe6.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Split hero with title, summary, media | yes | white header, peach serif title, square simulator video |
| Key points | yes | six icon rows with bold run-in labels |
| Link buttons | yes | four butter pills |
| Authors, venue, affiliation | present but non-standard | below the hero in a ruled Distill byline |
| Headline answer | yes | centered 24px pair, second line orange italic |
| Video abstract | yes | embedded YouTube at breakout width |
| Contents | yes | ordered list of § anchor links |
| Social proof | yes | collapsible multi-column wall of embedded tweets |
| Figures and videos | yes | Distill figures with "Figure N:" captions, many inline videos |
| Results table | yes | compact serif table with green highlights |
| Navigation bar | absent from the source | none |
| BibTeX and references | yes | Distill appendix |

## Adapting to Other Content

- **More authors**: they already live in the byline; keep #006400 names separated by em spaces and break lines with `<br>` at about six names.
- **A larger results table**: keep `.data-table` with 2.5px spacing and no borders; bold the first column, put headers on #f2f2f2 and winners on #e6ffe6; let it scroll horizontally in `.table-container` rather than shrinking below 12px.
- **News**: a short 👉-led paragraph list under the answer pair, label in #0000ff bold, date first.
- **Long publication lists**: use the contents-list pattern (ordered list, bold § links with a colon and a one-line description).
- **Calmer body**: to tame the busy lower page, drop the pure-blue labels to rgba(0,0,0,0.8) bold and keep orange only for the one answer line.
- **Missing simulator video**: any square teaser works at 600px in the right column; keep it unframed so the white header stays open.

## Do's and Don'ts

- Do keep the title and subtitle in #feae6f serif and everything else in the hero black.
- Do give every key point a line icon and a bold run-in label.
- Do put authors and venue below the hero in the Distill byline, not in it.
- Do ship a webfont or a serif fallback for Charter; the declared stack has none.
- Don't add a background color to the header; its whiteness lets the peach title carry the identity.
- Don't multiply accent colors in the body; the source already mixes peach, orange, pure blue and dark green.
- Don't let emoji headings replace real section titles for long sections.

## Surfaces

White throughout. Butter pills are the only filled controls. Full-width hairlines (rgba(0,0,0,0.1)) separate sections, and table cells take #f2f2f2 or #e6ffe6. The Distill appendix closes the page under a hairline.

## Imagery

Flat 2D physics-simulation videos (red, blue and grey balls, ramps and boxes in grey frames), line-art SVG icons in the hero, plots and diagrams in the body, a YouTube video abstract and embedded tweets.

## Layout

A split hero (45/53) above a Distill article: 704px text with 1056px breakouts for figures, videos and lead paragraphs. Rendered height about 25,200px at 1440px, the longest page in this set, mostly from videos and the tweet wall.

## Agent Prompt Guide

Quick colors: title #feae6f, hero text #000000, article text rgba(0,0,0,0.8), captions rgba(0,0,0,0.6), rules rgba(0,0,0,0.1), pills #fff0ce with rgba(255,193,7,0.5) border and #eab682 hover, authors #006400, answer #ffa500, table header #f2f2f2, highlight #e6ffe6.

1. "Build a split hero on white: flex row with 50px padding, max-width 1600px. Left column at calc(45% - 10px): serif (Charter, fallback serif) 48px/700 title in #feae6f, line-height 57.6px; italic 32px/700 #feae6f subtitle starting with an em dash; 19.2px #000000 intro. Right column at calc(53% - 20px): a square autoplay muted video at 87% width with controls hidden."
2. "Add icon key points: flex rows with a 30px line-art icon and 16px right margin, then 16px/25.6px black text starting with a bold label and a colon. Below, centered pills: #fff0ce fill, 2px solid rgba(255,193,7,0.5) border, 20px radius, padding 10px 20px, 16px/700 black label with icon left; hover #eab682 fill and white text."
3. "Create a results table: serif 15px, `border-spacing: 2.5px`, no borders, cells padded 3.75px, numbers centered with tabular figures, first column right-aligned bold, header cells on #f2f2f2, best cells on #e6ffe6, text rgba(0,0,0,0.8)."

## Similar Pages

- Cambrian-style Distill pages with a split hero, icon key points and butter pills (CellFlux uses the same skeleton with a dark gradient).
- Distill-template long reads with embedded video abstracts.

## Quick Start

```css
:root {
  --title: #feae6f;
  --ink: #000000;
  --article: rgba(0, 0, 0, 0.8);
  --caption: rgba(0, 0, 0, 0.6);
  --rule: rgba(0, 0, 0, 0.1);
  --pill: #fff0ce;
  --pill-border: rgba(255, 193, 7, 0.5);
  --pill-hover: #eab682;
  --community-link: #004276;
  --author: #006400;
  --answer: #ffa500;
  --label: #0000ff;
  --table-head: #f2f2f2;
  --table-win: #e6ffe6;
  --font: Charter, 'Charis SIL', serif;
  --text-col: 704px;
  --wide-col: 1056px;
  --radius-pill: 20px;
}
```

## Provenance

- **URL**: https://phyworld.github.io/
- **Paper**: How Far is Video Generation from World Model: A Physical Law Perspective (arXiv 2411.02385), Bingyi Kang, Yang Yue et al. (Bytedance Seed).
- **Venue**: ICML 2025.
- **Selection reason**: the arXiv 2411.02385 comment states acceptance at ICML 2025 and the abstract links the page. Chosen for the split hero with an oversized peach serif title, icon-labelled summary bullets and the physics-simulation teaser; the body below is busier, with emoji headings and mixed styles.
- **Template credit**: Distill v2 template with Cambrian-style header and pill rules in `static/css/style.css`; no explicit credit line.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share, targeted computed-style probes of the header, byline, answer lines, lists, captions, rules, table highlights and appendix, the first-viewport screenshot and scaled full-page capture, `style.css`, the inline `<style>` and the HTML. Date 2026-10-28.
