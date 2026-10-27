# Clean Data Sage Report — Style Reference

> A quiet lab report on sage paper: forest-green ink, numbered section tabs, and soft moss cards that never raise their voice.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's single minified stylesheet, /backdoor/style.css. No web fonts load (`document.fonts` is empty), so everything renders in Arial.

## Overview

The page is a single 1160px column on a pale sage ground (#f5f6f1), set entirely in Arial and colored in one deep forest green (#173e3c). A thin nav line reads "JUNHOO LEE / RESEARCH" on the left and "DaR · 2026" on the right in letterspaced 13px caps above a hairline. The hero is left-aligned: a pale green venue pill, an uppercase eyebrow, a 78px bold title with very tight tracking (-0.06em), a 35px regular subtitle, a gray-green dek, authors and four pill links (the first filled green). Each section below starts with a 1px sage rule and a numbered eyebrow ("01 / THE QUESTION", "02 / THE MECHANISM"), then a 35px bold heading. The overview figure sits in a white 22px-radius card, the mechanism is three moss-tinted step cards, and results are a hairline table with the DaR rows tinted and bold. No images in the hero, no shadows, no second accent.

## First Viewport

Color share of the 1440×900 viewport: #f5f6f1 82% (page ground), #e4e9e3 5% (venue pill and text antialiasing), #647e7a 5% (green-gray text mass), #f9f9f4, #f6f6f1, #f5f6f0 together 8% (ground variants). The fold is a near-monochrome sage page with dark green type and one filled green button.

Anatomy in DOM order (content x 172–1268):

1. **Nav** `nav`: padding 8px 0 23px, 1px #c7d3ca bottom border, Arial 13px/400, letter-spacing .08em, #173e3c; "JUNHOO LEE / RESEARCH" left, "DaR · 2026" right. Gap 76px (header padding-top).
2. **Venue pill** `span.badge`: "The Fortieth Annual Conference on Neural Information Processing Systems", 12px, #e4ece0 fill, radius 30px, padding 7px 13px. Gap 12px.
3. **Eyebrow** `p.eyebrow`: "DAR / RESEARCH PROJECT", 12px uppercase, letter-spacing .14em, #586f68. Gap 24px.
4. **Title** `h1.title`: Arial 78px/700 (clamp 40px, 6.7vw, 78px), line-height 1.06, letter-spacing -0.06em, #173e3c, left, max-width 1030px (two lines). Gap 24px.
5. **Subtitle** `p.subtitle`: 35px/400 (clamp 23px, 3vw, 35px), line-height 1.25, letter-spacing -0.03em, #173e3c. Gap 21px.
6. **Dek** `p.dek`: 21px/400, line-height 1.7, #506962, max-width 790px. Gap 29px.
7. **Authors** `.authors`: 16px #173e3c, asterisks for equal contribution; **affiliation** 14px #63766f directly below (two lines). Gap 24px.
8. **Links** `.links`: Read the paper ↗ (filled #173e3c, white text), LaTeX source ↓, Explore results, Cite this work; 44px tall pills, 10px apart. Header padding-bottom 42px.
9. **Section rule** at y 778: 1px #cad6cc, then "01 / THE QUESTION" eyebrow and the first h2 at the fold edge.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Sage Paper | #f5f6f1 | (literal) | page background |
| Forest Ink | #173e3c | (literal) | body text, title, headings, nav, filled button and selected tab fill, DaR rows text |
| Eyebrow Green | #586f68 | (literal) | uppercase eyebrows |
| Dek Green | #506962 | (literal) | hero dek |
| Affiliation Green | #63766f | (literal) | affiliation line |
| Caption Green | #62746e | (literal) | figure captions |
| Muted Green | #65766e | (literal) | table note, footer |
| Header Cell | #5c7168 | (literal) | table header text |
| Abstract Text | #435f56 | (literal) | abstract paragraph |
| Card Num | #597269 | (literal) | monospace step labels in cards |
| Pill Border | #b5c9bf | (literal) | outline link pills, buttons |
| Venue Pill | #e4ece0 | (literal) | venue badge fill |
| Moss Card | #e9efe5 | (literal) | mechanism step cards |
| Code Wash | #e7eee4 | (literal) | BibTeX block |
| Code Text | #244b41 | (literal) | BibTeX text |
| Ours Row | #e2ecdf | (literal) | DaR rows in the results table |
| Section Rule | #cad6cc | (literal) | section top borders |
| Nav Rule | #c7d3ca | (literal) | nav bottom border |
| Table Rule | #cbd6cd | (literal) | table row borders |
| Figure Border | #d9e1d9 | (literal) | 1px border of the white figure card |
| Card White | #ffffff | (literal) | figure card fill, filled-pill label |

Declared but not visible: #ae502e (a rust focus outline, `a:focus-visible, button:focus-visible`) appears only on keyboard focus.

## Tokens — Typography

- **Family**: declared `Arial, sans-serif`; renders Arial (no web fonts loaded). Substitute: Helvetica Neue, or Arimo for metric-compatible rendering.
- **Mono**: `monospace` (system default) for card step labels and BibTeX.

| Role | Selector | Size at 1440 (clamp) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `.title` | 78px (40px, 6.7vw, 78px); 43px ≤650px | 700 | 1.06 | -0.06em |
| Section title | `h2` | 35px (29px ≤650px) | 700 | 1.2 | -0.035em |
| Subtitle | `.subtitle` | 35px (23px, 3vw, 35px) | 400 | 1.25 | -0.03em |
| Lead | `.lead` | 25px (21px ≤650px) | 400 | 1.5 | 0 |
| Step title | `h3` | 21px | 700 | 1.35 | 0 |
| Dek | `.dek` | 21px | 400 | 1.7 | 0 |
| Body | `body` | 17px | 400 | 1.7 | 0 |
| Authors, table cells, abstract | `.authors`, `td`, `.abstract` | 16px | 400 | 1.7 | 0 |
| Card text | `.card p` | 15px | 400 | 1.7 | 0 |
| Pills, affiliation, captions, notes | `.links a`, `.affiliation`, `figcaption`, `.note` | 14px | 400 | 1.7 | 0 |
| Nav | `nav` | 13px | 400 | 1.7 | .08em |
| Table header | `th` | 13px | 700 | 1.7 | 0 |
| Eyebrow, venue pill | `.eyebrow`, `.badge` | 12px (eyebrow uppercase) | 400 | 1.7 | .14em / 0 |
| Card label, BibTeX | `.card .num`, `pre` | 12px / 13px mono | 400 | 1.7 | 0 |

## Tokens — Spacing & Shapes

- **Radius**: 30px for link pills and the venue pill; 28px for buttons and tabs; 22px for the figure card; 18px for step cards; 15px for BibTeX (figure card drops to 15px ≤650px).
- **Shadows**: none.
- **Borders**: 1px #b5c9bf on pills and buttons; 1px #d9e1d9 on the figure card; 1px #cad6cc between sections; 1px #cbd6cd under table rows; 1px #c7d3ca under the nav.

## Layout Metrics

- **Container**: `.wrap` max-width 1160px, padding 30px 32px, centered: content 1096px wide at 1440 (x 172–1268). Paragraphs cap at 860px, the lead at 880px, the dek at 790px.
- **Header**: padding 76px 0 42px.
- **Sections**: padding 48px 0 with a 1px #cad6cc top border; eyebrow, then h2 (margin 10px 0 25px).
- **Figure card**: full content width, padding 25px, margin 20px 0 45px.
- **Mechanism cards**: grid 3 × 1fr, gap 18px, padding 25px; label 25px above the heading.
- **Table**: full width, cells 15px 12px.
- **Footer**: padding 35px 0.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >650px | 32px | 17px | 6.7vw, max 78px | cards 3 across |
| ≤650px | 18px | 17px | 43px | header padding 45px 0 25px; sections 30px; cards 1 across; figure padding 13px; h2 29px; lead 21px; nav 11px; table cells 10px 8px at 13px |

## Components

- **Filled pill** `.links a:first-child`: padding 9px 19px, radius 30px, 1px #b5c9bf border, #173e3c fill, #ffffff Arial 14px, trailing "↗".
- **Outline pill** `.links a`: same size, transparent, #173e3c text, trailing "↓" on downloads; no hover change declared.
- **Venue pill** `.badge`: #e4ece0, radius 30px, padding 7px 13px, 12px #173e3c.
- **Numbered eyebrow** `.eyebrow`: 12px uppercase, letter-spacing .14em, #586f68, format "NN / LABEL".
- **Figure card** `figure`: #ffffff, 1px #d9e1d9 border, radius 22px, padding 25px; caption 14px #62746e, 18px above.
- **Step card** `.card`: #e9efe5, radius 18px, padding 25px; label 12px monospace #597269 ("01 / DISCOVER"), 25px gap; h3 21px/700; text 15px.
- **Results table**: 16px cells with 15px 12px padding and 1px #cbd6cd bottom borders; header 13px/700 #5c7168; proposed rows `tr.ours` #e2ecdf fill and bold; note below 14px #65766e.
- **Copy button**: 1px #b5c9bf border, radius 28px, padding 10px 17px, transparent, 17px text; `aria-selected` state fills #173e3c with #ffffff text.
- **BibTeX** `pre`: #e7eee4, radius 15px, padding 25px, 13px monospace #244b41, wrapped.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | text-only line with a hairline: site name left, project tag right |
| Venue badge | yes | pale green pill above the eyebrow |
| Title block | yes | left-aligned bold title, regular subtitle, gray-green dek |
| Authors / affiliations | yes | plain 16px line and 14px affiliation |
| Link buttons | yes | four pills, first filled |
| Teaser | absent from the source | the first figure follows section 01 |
| Method figure | yes | white rounded card with caption |
| Step cards | yes | three moss cards with monospace labels |
| Results table | yes | hairline table with tinted bold rows |
| Abstract | yes | placed late, under "IN THE PAPER" |
| BibTeX | yes | sage code block with Copy button |
| Footer | yes | 13px muted line |

## Adapting to Other Content

- **More authors**: keep a single wrapping 16px line with superscript markers and move affiliations to the 14px #63766f line; the left-aligned layout absorbs two or three lines without change.
- **Teaser video or image**: place it in the white figure card (radius 22px, 25px padding, 1px #d9e1d9) directly after the header, before section 01.
- **Long publication list**: one row per paper separated by 1px #cbd6cd, title 16px #173e3c, venue 14px #65766e; group under a numbered eyebrow.
- **News**: a section with eyebrow "NN / NEWS", dates in 12px monospace #597269 (the card label style) before 16px text.
- **More results**: repeat the table pattern; tint and bold only the proposed rows with #e2ecdf.

## Do's and Don'ts

- Do keep a single ink color (#173e3c) for all text weights; vary only gray-greens for secondary text.
- Do prefix every section with a numbered uppercase eyebrow and a 1px #cad6cc rule.
- Do keep the hero text-only and left-aligned.
- Do use tight negative tracking on the title (-0.06em) and h2 (-0.035em).
- Don't add shadows or gradients; surfaces are flat tints of sage.
- Don't introduce a second accent; rust #ae502e is for focus only.
- Don't center headings or widen paragraphs beyond 860px.

## Surfaces

Sage #f5f6f1 page; white #ffffff figure card; moss #e9efe5 step cards; #e2ecdf table highlight; #e7eee4 code; #e4ece0 venue pill. All flat.

## Imagery

One method overview diagram (pipeline with images, clustering plot and network sketches) in a white card. No photos or video.

## Layout

One left-aligned column in a 1160px wrapper: text hero, then ruled sections with numbered eyebrows, a 3-card grid, a table and BibTeX. About 4,400px tall.

## Agent Prompt Guide

Quick colors: ground #f5f6f1, ink #173e3c, eyebrow #586f68, muted #65766e, pill border #b5c9bf, rule #cad6cc, card #e9efe5, highlight #e2ecdf, figure card #ffffff with #d9e1d9 border.

1. "Build a hero on #f5f6f1 in Arial: venue pill 12px on #e4ece0, radius 30px, padding 7px 13px; eyebrow 12px uppercase, letter-spacing .14em, #586f68; title 78px/700, line-height 1.06, letter-spacing -0.06em, #173e3c; subtitle 35px/400, letter-spacing -0.03em; dek 21px #506962."
2. "Build link pills: padding 9px 19px, radius 30px, 1px solid #b5c9bf, Arial 14px #173e3c, 10px gap; the first one filled #173e3c with #ffffff text and a trailing ↗."
3. "Build a mechanism row: 3-column grid with 18px gap; each card #e9efe5, radius 18px, padding 25px; label 12px monospace #597269 like '01 / DISCOVER', 25px below it an h3 21px/700 #173e3c, then 15px text."

## Similar Pages

- Personal-site research pages with one ink color, numbered section eyebrows and a text-only hero.
- Minimal report-style project pages built on system fonts.

## Quick Start

```css
:root {
  --ground: #f5f6f1;
  --ink: #173e3c;
  --eyebrow: #586f68;
  --dek: #506962;
  --muted: #65766e;
  --pill-border: #b5c9bf;
  --badge: #e4ece0;
  --card: #e9efe5;
  --code-bg: #e7eee4;
  --code-ink: #244b41;
  --ours: #e2ecdf;
  --rule: #cad6cc;
  --figure-border: #d9e1d9;
  --font: Arial, sans-serif;
  --wrap: 1160px;
}
body { background: var(--ground); color: var(--ink); font: 17px/1.7 var(--font); }
```

## Provenance

- **URL**: https://junhoo.me/backdoor
- **Paper**: Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse (arXiv 2610.21208), Junhoo Lee, Baekseung Kim, Seungyeon Kim, Nojun Kwak.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and the abstract links this page.
- **Template credit**: part of the author's personal site; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, empty fonts_loaded, color share), the 1440 screenshot and tall capture, and style.css read directly. Captured 2026-10-28.
