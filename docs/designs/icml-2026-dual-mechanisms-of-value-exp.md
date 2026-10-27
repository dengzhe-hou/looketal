# Value Mechanisms — Style Reference

> A well-set technical memo: one narrow column of charcoal text, a quiet contents rail and a single violet thread for links.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `assets/site.css` and `assets/page-toc.css`. No web font is loaded: the stack starts with "Noto Sans", which this test machine lacks, so the render falls back to Arial. On a system with Noto Sans installed the same sizes apply in Noto Sans.

## Overview

A minimal documentation-style page with no framework. A 48px white top bar carries only the short brand "Value Mechanisms". On wide screens a fixed 184px contents rail sits at the left, with a small bold "Contents" label and plain links; the current section gets a 2px violet left rule and a pale gray fill. The paper itself is a 660px reading column centred on the page. The hero is centred: a bold 41.6px two-line title in charcoal (#303039), a 21px subtitle, authors with violet links for those who have pages, a gray affiliation and notes line, a bold "ICML 2026" line and five pill buttons (four filled charcoal, one outlined). Everything after is left-aligned prose at 16px/1.65 with 24px bold section headings, thin #ececf0 rules between sections, inline diagrams with 13.5px gray captions, small numeric tables with a pale gray header row and a gray-boxed BibTeX block. The only color is violet #6552a3.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 86.6%; near-whites #f5f6f6 / #fdfdfd / #feffff / #fffffd 4.3% (active contents row, hairlines); #bfbec2 4.5% and #e0e0e2 2.5% (anti-aliased text); #77767d 2.1% (text and buttons). The violet links are too small to form a cluster.

Anatomy in DOM order (desktop 1440px):

1. **Top bar** (`header.topbar`, 0–49px, sticky): white, 1px #ecedf1 bottom rule; inner row max-width 1000px, padding 0 20px, min-height 48px. "Value Mechanisms" 14px/600 #303039 at x=240.
2. **Contents rail** (`.page-toc nav`, fixed, top 88px, left calc(50% - 568px) = 152px, width 184px): "Contents" 12px/600 #303039 with 14px left padding, 12px gap; links 13px #62626e, padding 7px 12px, 2px transparent left border; current link 600 #303039 on #f2f3f6 with a 2px #6552a3 left border.
3. **Title** (`h1`, y=101, two lines, 100px tall): 41.6px/700, line-height 1.2, `text-wrap: balance`, #303039, centred in the 660px column (x=390–1050). Gap 18px.
4. **Subtitle** (`.paper-subtitle`, y=219): 21px/500, line-height 1.4, #303039. Gap 24px.
5. **Authors** (`.authors`, y=272): 17px, line-height 1.7, #303039; linked names #6552a3; superscript markers at 0.66em. Gap 4px.
6. **Affiliation** (y=305): 14.5px #62626e. Gap 6px.
7. **Notes** (y=335): 13px #62626e, line-height 1.55. Gap 22px.
8. **Venue line** (y=377): "ICML 2026", 19px/700 #303039. Gap 22px.
9. **Buttons** (`.links`, y=431, 36px tall): Paper, arXiv, Code, Proceedings filled; BibTeX outlined; gap 8px, centred. Gap 64px.
10. **TL;DR** (y=531): left-aligned 24px/700 heading, then a 16px paragraph; "What is this paper about?" follows 30px later and runs past the fold.

No teaser figure: the first figure appears in the Method section at about y=1200.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Charcoal | #303039 | --text | body text, title, headings, filled button fill and border, outline button text, brand |
| Button Hover | #444450 | (literal) | filled button hover fill |
| Slate Gray | #62626e | --muted | affiliation, notes, captions, table header text, inactive contents links |
| Violet | #6552a3 | --primary | links (author names, figure references, Copy/Download), active contents rule, focus outline |
| Hairline | #dcdde3 | --border | BibTeX block border, collapsed contents panel border |
| Mist | #f5f5f7 | --surface | table header row, BibTeX block, outline button hover |
| Active Row | #f2f3f6 | (literal) | current contents link background |
| Hover Row | #f7f7f9 | (literal) | contents link hover background |
| Rule | #ececf0 | (literal) | section divider lines, table row lines |
| Top-bar Rule | #ecedf1 | (literal) | top bar bottom border |
| White | #ffffff | (literal) | page, top bar, outline button fill |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text | "Noto Sans", "Helvetica Neue", Arial, sans-serif | no web font loaded; Arial in this render (Noto Sans where installed) | Noto Sans (load it from Google Fonts to fix the fallback) |
| Code | ui-monospace, "SF Mono", Menlo, Consolas, monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | clamp(1.7rem, 4vw, 2.6rem) → 41.6px / 700 / 1.2, balanced | #303039 |
| Subtitle | `.paper-subtitle` | 21px / 500 / 1.4 | #303039 |
| Section heading | `h2` | 24px / 700 / 1.3 | #303039 |
| Subsection | `h3` | 18px / 600 / 1.4, margin 30px 0 10px | #303039 |
| Body | `body` | 16px / 400 / 1.65 | #303039 |
| Authors | `.authors` | 17px / 1.7 | #303039, links #6552a3 |
| Affiliation | `.affiliation` | 14.5px | #62626e |
| Notes | `.notes` | 13px / 1.55 | #62626e |
| Venue line | `.venue-line` | 19px / 700 | #303039 |
| Button | `.button` | 14px / 500 / 1.2 | #ffffff (outline: #303039) |
| Caption | `figcaption`, `.caption`, `.note` | 13.5px / 1.55 | #62626e |
| Table body | `table` | 14px tabular-nums | #303039 |
| Table header | `thead th` | 13px / 600 | #62626e |
| Table caption | `caption` | 15px / 600, left | #303039 |
| Contents links | `.page-toc nav a` | 13px / 1.5 (active 600) | #62626e (active #303039) |
| Brand | `.brand` | 14px / 600 | #303039 |
| BibTeX | `pre` | 13px / 1.65, pre-wrap | #303039 |

`strong` and `b` are set to 600, not bold.

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 999px | 1px #303039 | none |
| BibTeX block | 0 | 1px #dcdde3 | none |
| Contents active row | 0 | 2px #6552a3 left | none |
| Tables | 0 | 1px #ececf0 row lines | none |
| Figures | 0 | none | none |

The page has no rounded containers other than the buttons and no shadows anywhere.

## Layout Metrics

- **Containers**: `main { max-width: 1000px; margin: 0 auto; padding: 0 20px 36px }`; each `main > section` is capped at `--reading-width: 660px` and centred (x=390–1050 at 1440). The hero inner block is also capped at 660px from 1200px up.
- **Hero**: `.hero-inner { padding: 52px 0 28px; text-align: center }`; TL;DR starts 64px below the buttons.
- **Sections**: padding 44px 0 8px; a 1px #ececf0 rule is drawn 20px below each section's top edge, so headings sit 24px under the rule.
- **Paragraphs**: margin 0 0 14px; h2 margin-bottom 14px.
- **Figures**: full column (660px) by default; `.compact` 500px, `.medium` 550px, geometry diagram 360px; the method pipeline is split into two crops at 560px and 440px. Margin 24px auto; captions 10px below.
- **Tables**: full column, cells padding 9px 10px, right-aligned numbers; the diversity table has min-width 560px inside a horizontal scroller.
- **Contents rail**: fixed at top 88px, 184px wide, starting at calc(50% - 568px).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 20px; column 660px | 16px | 41.6px | fixed left contents rail |
| 761–1199px | 20px | 16px | 4vw (30–41.6px) | rail collapses into a "Contents" disclosure in the top bar showing the current section; panel drops down with a #dcdde3 border |
| ≤760px | 20px | 16px | 4vw | hero top padding 36px; subtitle 19px |
| ≤600px | 20px | 16px | 27.2px floor | current-section label hidden in the top bar |
| ≤480px | 18px | 16px | 28px | h2 22px; subtitle 18px; authors 15px; buttons padding 8px 13px; tables 12px |

## Components

- **Filled pill button** (`.button`): inline-flex, min-height 36px, padding 8px 16px, 1px #303039 border, radius 999px, #303039 fill, white 14px/500 text, no icons. Hover: #444450 fill, no underline.
- **Outline pill button** (`.button.secondary`): same shape, white fill, #303039 text and border; hover #f5f5f7 fill. Used only for BibTeX.
- **Contents rail** (`.page-toc`): 184px column; "Contents" label 12px/600; links 13px #62626e with 2px transparent left border; hover #303039 on #f7f7f9; current section 600 #303039 on #f2f3f6 with 2px #6552a3 left border. Below 1200px it becomes a `<details>` in the top bar with a chevron and the current section name after a "/".
- **Section divider**: absolute 1px #ececf0 line across the column, 20px above each section heading area.
- **Figure** (`.figure`): image at full width, click to zoom (cursor zoom-in), caption 13.5px #62626e with violet "Figure N." links.
- **Data table**: caption 15px/600 left; header row #f5f5f7 with 13px/600 #62626e text, bottom-aligned; body 14px tabular figures, right-aligned, 1px #ececf0 row lines; scale notes in 12px.
- **BibTeX block**: heading row with h2 and right-aligned "Copy" / "Download" text buttons (13px #6552a3); `pre` padding 18px, #f5f5f7, 1px #dcdde3, 13px mono, wrapping.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top bar | yes | white sticky bar with a short brand name |
| Contents sidebar | yes | fixed left rail, violet active rule; dropdown on narrower screens |
| Title / subtitle | yes | centred, balanced bold title and 21px subtitle |
| Authors / affiliation / notes | yes | centred; violet links on linked authors |
| Venue line | yes | plain bold text, no badge |
| Link buttons | yes | four charcoal pills and one outlined pill, text only |
| TL;DR / plain summary | yes | left-aligned h2 + paragraph inside the hero |
| Teaser | absent from the source | first figure is in the Method section |
| Method figures | yes | inline diagrams with gray captions |
| Results tables | yes | two small numeric tables with gray header rows |
| BibTeX | yes | gray box with Copy and Download text actions |
| Footer | absent from the source | the page ends after BibTeX |

## Adapting to Other Content

- **More authors**: authors are inline-block spans with nowrap, so a long list wraps by name inside the 660px column; keep 17px and add affiliations as a second 14.5px line.
- **A teaser figure**: place it after the buttons and before TL;DR at full column width with a 13.5px caption; do not widen beyond 660px.
- **Larger results tables**: keep the table style and wrap it in `.table-scroll` with a min-width; bold best values at 600 #303039 rather than adding color.
- **Long publication or news lists**: plain list items at 16px with dates in 13px #62626e; separate groups with the same 1px #ececf0 rule as sections.
- **Many sections**: the contents rail scales with no changes; keep link labels short (two or three words).

## Do's and Don'ts

- Do keep one reading column at 660px; nothing but the contents rail sits outside it.
- Do limit color to violet #6552a3 for links and the active contents rule.
- Do keep buttons as text-only charcoal pills with one outlined secondary.
- Don't add cards, shadows or rounded boxes; the BibTeX box is square.
- Don't add icons to buttons or headings.
- Don't centre body text; only the hero block is centred.

## Surfaces

White everywhere; #f5f5f7 only for table headers and the BibTeX box; #f2f3f6 for the active contents row. Separation comes from 1px rules (#ececf0, #ecedf1, #dcdde3).

## Imagery

Clean vector-style diagrams: a two-panel data pipeline with chat bubbles, a geometric plot of shared and unique axes with colored dashed regions, and result charts. Images sit directly on white with no frames.

## Layout

Sticky top bar, fixed left contents rail, and a single 660px column: centred hero with TL;DR, then six sections (Method, Shared components, Value steering, Response diversity, Instruction compliance, BibTeX) separated by hairlines. Page height about 8,650px at 1440 wide.

## Agent Prompt Guide

Quick colors: text #303039, muted #62626e, link #6552a3, rule #ececf0, border #dcdde3, surface #f5f5f7, active row #f2f3f6, page #ffffff.

1. "Build a centred paper header in a 660px column: padding 52px 0 28px; title 41.6px/700, line-height 1.2, text-wrap balance, #303039; subtitle 21px/500; authors 17px with links in #6552a3; affiliation 14.5px #62626e; notes 13px #62626e; venue line 19px/700; then a centred row of pill buttons with 8px gaps."
2. "Make pill buttons: min-height 36px, padding 8px 16px, radius 999px, 1px solid #303039, background #303039, white 14px/500 text, no icons; hover background #444450. Secondary: white background, #303039 text; hover #f5f5f7."
3. "Create a fixed contents rail: 184px wide at top 88px; label 'Contents' 12px/600 #303039 with 14px left padding; links 13px #62626e, padding 7px 12px, 2px transparent left border; active link 600 #303039 on #f2f3f6 with a 2px #6552a3 left border."

## Similar Pages

- Documentation-style single-column research pages with a left table of contents (Distill-like reading pages without the custom typography).
- Interpretability paper pages that favour prose and inline figures over hero media.

## Quick Start

```css
:root {
  --text: #303039;
  --muted: #62626e;
  --primary: #6552a3;
  --border: #dcdde3;
  --surface: #f5f5f7;
  --rule: #ececf0;
  --active: #f2f3f6;
  --reading-width: 660px;
  --font-sans: "Noto Sans", "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
body { font: 16px/1.65 var(--font-sans); color: var(--text); background: #fff; }
```

## Provenance

- **URL**: https://holi-lab.github.io/ValueMechanism/
- **Paper**: Dual Mechanisms of Value Expression: Intrinsic vs. Prompted Values in Large Language Models (arXiv 2509.24319), Jongwook Han, Jongwon Lim, Injin Kong, Yohan Jo.
- **Venue**: ICML 2026.
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit**: none; two small custom stylesheets (`site.css`, `page-toc.css`) and two scripts.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page's `site.css`, `page-toc.css` and `index.html` read directly, on 2026-10-28.
