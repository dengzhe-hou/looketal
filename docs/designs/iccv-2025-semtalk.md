# SemTalk — Style Reference

> Cherry blossom on frosted glass: soft pink washes drift behind white cards, and every link, badge and best number blushes the same sakura pink.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `/paper_site_static/static/css/paper-modern.css?v=9` (a shared stylesheet of the author's site, minified) and `index.html`. The page has a self-hosted variable Inter declared inline. Cards lift on hover; screenshots show them at rest. Declared but not visible: the stylesheet sets `--bg` to a pale pink that no rendered element uses, because `body` paints its own gradient background.

## Overview

A soft, rounded card page (about 8,200px tall) on a fixed pastel background (several faint pink, lilac and blue radial washes over a near-white vertical gradient). A sticky translucent nav bar carries a pink "SemTalk" wordmark and bold gray links. The hero is a large frosted white card (28px radius, pink-tinted shadow, two blurred pink glows in its corners) with a pale pink "Project Page" pill, a 43.2px/800 dark title, a gray subtitle, pink author links, a big pink "🔥 ICCV 2025" line and a row of pill buttons, the first filled with a pink gradient. Below, a teaser figure in its own rounded card with an italic caption, then white section cards (22px radius) for Abstract, Demo (YouTube embed in a pink-tinted shell), Method, Semantic Emphasis, Qualitative Results, Quantitative Results (metric cards and two tables), BibTeX and Related Work. There is no footer. Everything is centred in a 1160px column with 26px gaps between cards.

## First Viewport

Color share (quantized 1440×900 shot): near-white pinks and lilacs dominate: #f8f2f7 19.4%, #fefdfe 17.4%, #fefefe 14.0%, #f2f2f8 13.9%, #ffffff 9.3%, #faf8fb 8.1%, #fdfdfd 3.4%; #b8b3b8 14.4% is the gray-pink teaser figure entering at the bottom. Pink text covers too little area to form a cluster.

Anatomy in DOM order (desktop 1440px, column x=140 to 1300):

1. **Sticky nav** (`nav.project-nav`, 0–65px): background rgba(255,255,255,0.90), `backdrop-filter: blur(16px)`, 1px rgba(232,145,179,0.16) bottom border, shadow `0 8px 24px rgba(31,41,55,0.05)`; inner row min-height 64px. Left "SemTalk" 18.4px/900 #d47a9e, letter-spacing -0.02em. Right links Overview … Related Work and a "More Related Research ▾" dropdown, 14.72px/750 #374151, padding 21px 0 18px, 26px gaps, 3px transparent bottom border that turns #e891b3 on hover (text #d47a9e).
2. **Hero section** (`section.hero`, y=65–640): padding 48px 0 28px.
3. **Hero card** (`.hero-card`, y=113–612): background rgba(255,255,255,0.86) with `backdrop-filter: blur(14px)`, 1px rgba(255,255,255,0.6) border, 28px radius, shadow `0 12px 40px rgba(232,145,179,0.10)`, padding 42px 34px 30px; corner glows `radial-gradient(circle, rgba(232,145,179,0.16), transparent 70%)` (220px at -80px,-80px) and `radial-gradient(circle, rgba(240,160,184,0.14), transparent 70%)` (240px at the bottom-right, -90px,-90px).
4. **Badge** (y=156, 34px tall): "Project Page", 13px/700, letter-spacing 0.02em, #d47a9e on rgba(232,145,179,0.12), 1px rgba(232,145,179,0.18) border, padding 8px 14px, 999px radius. Gap 18px.
5. **Title** (`h1.title`, y=208–301): 43.2px/800, line-height 1.08, letter-spacing -0.03em, #1f2937, centred, max 980px, two lines. Gap 16px.
6. **Subtitle** (y=317): 16.8px/400, line-height 1.75, #667085, max 860px. Gap 24px.
7. **Authors** (y≈370–401): 17.28px, line-height 1.8, links 600 #e891b3 (hover #d47a9e underlined), superscripts in #1f2937. Gap 10px.
8. **Affiliations** (y≈411): 15.7px, line-height 1.7, #667085, separated by " · ". Gap 28px.
9. **Venue line** (`.venue-highlight`, y=473–510): "🔥 ICCV 2025", 32px/900, letter-spacing -0.02em, #d47a9e, `text-shadow: 0 6px 18px rgba(190,24,93,0.13)`; the emoji is 34.56px with `filter: drop-shadow(0 5px 8px rgba(234,179,8,0.28))`. Gap 26px.
10. **Button row** (y=536–581): arXiv (primary), Demo, Results ▾ (dropdown), Code, Model, BibTeX; 12px gaps. Card bottom padding 30px, then section padding 28px.
11. **Teaser card** (y=666): `.teaser-box`, 960px wide, starts after a 26px section margin and crosses the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #1f2937 | --text | title, section titles, body text in cards, secondary button text |
| Muted | #667085 | --muted | subtitle, affiliations, leads, captions, table notes |
| Body Gray | #374151 | (literal) | nav links, abstract and description text, BibTeX code |
| Table Head Ink | #111827 | (literal) | table headers and table titles |
| Sakura | #e891b3 | --sakura | author links, nav hover underline, primary button gradient start |
| Sakura Dark | #d47a9e | --sakura-dark | wordmark, badge text, venue line, section icons, best table values, metric numbers, hover text |
| Sakura Light | #f0a0b8 | --sakura-light | primary button gradient end |
| Page Wash Top | #fefbfc | (literal, body gradient) | top of the page background |
| Page Wash Mid | #f8f5f9 | (literal, body gradient) | page background at 40% |
| Page Wash Bottom | #f5f7fb | (literal, body gradient) | bottom of the page background |
| Card White | #ffffff | --card-solid | section cards, figure boxes, table wraps, metric cards |
| Blush Panel | #fef7f9 | (literal) | end of figure and teaser caption gradients, video shell gradient |
| Blush Panel 2 | #fffafb → #fef5f7 | (literal gradient) | BibTeX box, highlight items, table header cells |
| Sakura Tint | rgba(232,145,179,0.12) | (literal) | badge fill; at 0.10 the venue tags and dropdown hover; at 0.16 the current related-research item |
| Sakura Line | rgba(232,145,179,0.15) | --line | card and table borders (0.10–0.22 depending on element) |
| Lilac Wash | rgba(186,163,220,0.09) | (literal, body) | radial wash at 85% 10% |
| Sky Wash | rgba(168,200,235,0.08) | (literal, body) | radial wash at 90% 80% |
| Rose Shadow | rgba(190,24,93,0.13) | (literal) | venue line text-shadow |
| Gold Glow | rgba(234,179,8,0.28) | (literal) | flame emoji drop-shadow |
| Star Gold | #e8a040 | (literal) | star icon in the GitHub star badge |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text / display | "Inter", sans-serif (self-hosted variable woff2, weights 100–900) | Inter 100–900 | Inter |
| Code | "JetBrains Mono", "Fira Code", "Courier New", monospace | not loaded; Courier New renders on Windows | JetBrains Mono |
| Icons | Font Awesome 6, Academicons | Font Awesome 6 Free 900 / Brands 400, Academicons 400 | — |
| Math | MathJax | MJXTEX fonts loaded | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title` | clamp(2rem, 3vw, 3.15rem) → 43.2px / 800 / 1.08, letter-spacing -0.03em | #1f2937 |
| Venue line | `.venue-highlight` | clamp(1.45rem, 2.4vw, 2rem) → 32px / 900 / 1.15, letter-spacing -0.02em | #d47a9e |
| Section title | `.section-title` | 1.55rem = 24.8px / 800, letter-spacing -0.02em | #1f2937 |
| Wordmark | `.project-nav-brand` | 1.15rem = 18.4px / 900, letter-spacing -0.02em | #d47a9e |
| Nav link | `.project-nav-links a` | 0.92rem = 14.72px / 750 | #374151 |
| Subtitle | `.subtitle-text` | 1.05rem = 16.8px / 400 / 1.75 | #667085 |
| Authors | `.authors` | 1.08rem = 17.28px / 600 links / 1.8 | #e891b3 |
| Affiliations | `.affiliations` | 0.98rem = 15.7px / 400 / 1.7 | #667085 |
| Button | `.btn` | 0.96rem = 15.36px / 700 | #1f2937; primary #ffffff |
| Badge | `.badge` | 13px / 700, letter-spacing 0.02em | #d47a9e |
| Abstract / description | `.abstract-text, .desc-text` | 16px / 400 / 1.95, justified | #374151 |
| Lead | `.lead` | 16px / 1.8 | #667085 |
| Caption | `.figure-caption` / `.teaser-caption` | 15.2px / 1.7 (teaser 15.5px italic) | #667085 |
| Table | `table.project-table` | 0.86rem = 13.76px; header 800 | #1f2937; header #111827; best 900 #d47a9e |
| Metric number | `.project-metric strong` | 1.35rem = 21.6px / 1.15 | #d47a9e |
| BibTeX | `.bibtex-box pre` | 0.9rem = 14.4px / 1.6 | #374151 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero card | 28px | 1px rgba(255,255,255,0.6) | `0 12px 40px rgba(232,145,179,0.10)`; hover lifts 4px with `0 16px 48px rgba(232,145,179,0.14), 0 4px 12px rgba(0,0,0,0.04), inset 0 1px 0 rgba(255,255,255,0.7)` |
| Section card | 22px | 1.5px transparent; hover rgba(232,145,179,0.22) | `0 12px 40px rgba(232,145,179,0.10)`; hover lifts 5px with `0 14px 44px rgba(232,145,179,0.12), 0 4px 12px rgba(0,0,0,0.05), inset 0 1px 0 rgba(255,255,255,0.7), inset 0 -1px 0 rgba(0,0,0,0.02)` |
| Teaser / figure box | 20px | 1.5px transparent (figure 1px rgba(232,145,179,0.10)) | `0 8px 24px rgba(232,145,179,0.07)` |
| Video shell | 22px; iframe 16px | 1px rgba(232,145,179,0.12) | `0 12px 28px rgba(232,145,179,0.08)` |
| BibTeX box, highlight items | 18px | 1px rgba(232,145,179,0.10) | hover `0 4px 16px rgba(232,145,179,0.08)` |
| Table wrap, metric cards | 16px | 1px rgba(232,145,179,0.14) | `0 8px 24px rgba(232,145,179,0.06)` (metrics 0.07) |
| Buttons, badge, venue tags | 999px | 1px rgba(232,145,179,0.2) (primary none) | `0 8px 20px rgba(232,145,179,0.06)`; hover `0 14px 28px rgba(232,145,179,0.14)` |
| Section icon chip | 12px, 40px square | none | none |
| Dropdown menus | 12px (results), 16px (nav) | 1px rgba(232,145,179,0.22) | `0 16px 36px rgba(17,24,39,0.14)` / `0 18px 42px rgba(31,41,55,0.14)` |

## Layout Metrics

- **Container**: `.container { width: min(1160px, calc(100% - 32px)); margin: 0 auto }` → x=140 to 1300 at 1440. The nav inner row uses the same width.
- **Hero**: section padding 48px 0 28px; card padding 42px 34px 30px; inner column max 980px (title), 860px (subtitle); badge-to-title 18px, title-to-subtitle 16px, subtitle-to-authors 24px, authors-to-affiliations 10px, venue line margin 28px auto 22px, button row margin-top 26px (collapses with the venue's 22px), button gap 12px. Rendered card 499px tall.
- **Sections**: each `.section` has margin-top 26px; cards padding 28px; section title margin-bottom 16px with a 12px gap to an optional icon chip.
- **Figures**: teaser box `min(100%, 960px)`; figure boxes `min(100%, 920px)`, `.medium` 800px, `.narrow` 680px with 16px image padding; images capped at `min(720px, 72vh)` height (teaser `min(760px, 76vh)`).
- **Video**: shell 100% of the 1104px card content, padding 16px, iframe 16:9.
- **Results**: metrics in 3 columns, gap 14px; tables in a 2-column grid, gap 16px (tables keep a 720px min-width and scroll inside their wrap).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | 16px min, centred 1160px column | 16px | clamp → 43.2px at 1440 (max 50.4px at 1680+) | 2-column tables and highlights, 3 metrics |
| ≤900px | 12px (nav width calc(100% - 24px)) | 16px | 32px | nav 56px tall, links 13.4px with 18px gaps; cards padding 22px 18px; results dropdown becomes static; metrics, tables, highlights and two-col go to 1 column; figures full width |

## Components

- **Pill button** (`.btn`): inline-flex, gap 10px, padding 12px 18px, 999px radius, rgba(255,255,255,0.9) fill, 1px rgba(232,145,179,0.2) border, 15.36px/700 #1f2937, 18px Font Awesome / Academicons icon on the left, shadow `0 8px 20px rgba(232,145,179,0.06)`. Hover: translateY(-2px), shadow `0 14px 28px rgba(232,145,179,0.14)`, border at 0.4.
- **Primary button** (`.btn.primary`): `background: linear-gradient(135deg, var(--sakura) 0%, var(--sakura-light) 100%)` (#e891b3 → #f0a0b8), white text, no border; hover shadow `0 14px 28px rgba(232,145,179,0.25)`.
- **Results dropdown**: the Results button is a `details` summary with a rotating chevron; menu 12px radius, white, 8px padding, options 14.4px/700 with 8px radius and pink hover tint.
- **Badge** (`.badge`): 13px/700 #d47a9e, padding 8px 14px, rgba(232,145,179,0.12) fill, 1px rgba(232,145,179,0.18) border, pill.
- **Section card** (`.section-card`): white, 22px radius, 28px padding, sakura shadow; on hover it lifts 5px, gains a faint pink 135deg wash `linear-gradient(135deg, rgba(232,145,179,0.04) 0%, rgba(240,160,184,0.06) 50%, rgba(232,145,179,0.03) 100%)` and a pink border.
- **Teaser box**: white, 20px radius, image centred; caption strip `linear-gradient(180deg, #fff 0%, #fef7f9 100%)` with 1px rgba(232,145,179,0.08) top border, padding 14px 18px 16px, italic 15.5px #667085 with a bold italic lead-in.
- **Video shell**: 16px padding, 22px radius, the same white-to-#fef7f9 gradient, 1px pink border; YouTube iframe 16:9 with 16px radius.
- **Metric card** (`.project-metric`): white, 16px radius, 16px padding, 1px rgba(232,145,179,0.14); number 21.6px #d47a9e; label 14.4px #667085.
- **Results table**: wrap 16px radius, white, pink border; optional 15.2px/800 #111827 title; header cells `linear-gradient(180deg, #fffafb 0%, #fef5f7 100%)` 800 #111827; cells 9px 12px, numbers right-aligned, 1px rgba(232,145,179,0.10) row rules; best values 900 #d47a9e; venue tags as small pink pills (12.2px/800, padding 3px 9px).
- **BibTeX box**: `linear-gradient(180deg, #fffafb 0%, #fef5f7 100%)`, 18px radius, padding 18px 22px, 14.4px code in #374151, wrapped.
- **Nav dropdown** ("More Related Research"): 285px menu, 16px radius, 9px padding, white at 0.98 with `blur(18px)`; items 14.08px with 10px radius, current item #d47a9e on rgba(232,145,179,0.16).
- **Lightbox**: images with `.media-zoomable` open in a 22px-radius dialog over rgba(17,24,39,0.78) with `blur(8px)`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav | yes | translucent white, pink wordmark, underline-on-hover links, related-research dropdown |
| Hero card | yes | frosted white card with corner glows |
| Project badge | yes | pale pink pill "Project Page" |
| Title / subtitle / authors / affiliations | yes | centred, pink author links |
| Venue line | present but non-standard | a large 32px pink "🔥 ICCV 2025" text line instead of a pill |
| Link buttons | yes | six pills, the first filled with a pink gradient, Results as a dropdown |
| Teaser | yes | rounded white card with italic caption |
| Abstract | yes | section card, justified 16px text at 1.95 line-height |
| Demo video | yes | YouTube iframe in a pink-tinted shell |
| Method / emphasis figures | yes | figure boxes with gradient caption strips |
| Results tables | yes | metric cards plus two pink-headed tables |
| BibTeX | yes | blush gradient box |
| Related work | yes | text card with inline links |
| Footer | absent from the source | page ends with the Related Work card |

## Adapting to Other Content

- **More authors**: authors already wrap at 17.28px inside the 980px column; keep superscripts and the " · " affiliation separators, and keep the venue line on its own row.
- **A results table**: use `.project-table` in a 16px-radius white wrap at 13.76px, header gradient #fffafb → #fef5f7, best values 900 #d47a9e; one table spans 1104px with `.project-table-wide`.
- **Long publication or news lists**: put each item in a `.highlight-item` (18px radius, #fffafb → #fef5f7 gradient, 18px padding, 16px/800 heading, 15.4px #667085 text) in the 2-column grid inside a section card.
- **Key numbers**: use the 3-column metric cards (21.6px #d47a9e numbers) rather than a new style.
- **A footer**: if needed, use the stylesheet's `.footer` (centred, 15px #667085, links 600 #e891b3, padding 26px 0 46px).

## Do's and Don'ts

- Do keep every surface rounded and white on the pastel background; radii step 28px (hero) / 22px (sections) / 20px (figures) / 16px (tables).
- Do tint all shadows and borders with sakura rgba(232,145,179,…), not gray.
- Do keep the single gradient fill for the primary button only.
- Do use #d47a9e for emphasized pink text (wordmark, venue line, best numbers) and #e891b3 for links.
- Don't use saturated colors other than sakura; lilac and sky appear only as faint background washes.
- Don't put text on the pastel background directly; it always sits on a white card.
- Don't add hard dark borders or square corners.

## Surfaces

A fixed page background of four radial washes over a vertical gradient, quoted literally: `radial-gradient(ellipse at 15% 5%, rgba(232,145,179,0.13), transparent 40%), radial-gradient(ellipse at 85% 10%, rgba(186,163,220,0.09), transparent 35%), radial-gradient(ellipse at 50% 60%, rgba(240,160,184,0.06), transparent 50%), radial-gradient(ellipse at 90% 80%, rgba(168,200,235,0.08), transparent 40%), linear-gradient(180deg, #fefbfc 0%, #f8f5f9 40%, #f5f7fb 100%)`, `background-attachment: fixed`. On it: a frosted hero card at 86% white, solid white section cards, and blush gradient panels for captions, BibTeX and table headers.

## Imagery

Pastel method and teaser diagrams (pink, blue and gray SMPL-X body renders, waveform and transcript bars), a YouTube demo with blue and pink avatars, and qualitative comparison strips. Figures are rendered in the same pink/blue palette as the page, which makes the page feel unified.

## Layout

One centred 1160px column of stacked rounded cards with 26px gaps: hero card, teaser card, then one card per section. Text inside cards is left-aligned (abstract justified); only the hero is centred.

## Agent Prompt Guide

Quick colors: ink #1f2937, muted #667085, body #374151, sakura #e891b3, sakura dark #d47a9e, sakura light #f0a0b8, card #ffffff, blush panel #fef7f9, page #fefbfc → #f5f7fb.

1. "Build a frosted hero card: rgba(255,255,255,0.86) with backdrop-filter blur(14px), 28px radius, 1px rgba(255,255,255,0.6) border, shadow 0 12px 40px rgba(232,145,179,0.10), padding 42px 34px 30px, centred content. Pill badge 13px/700 #d47a9e on rgba(232,145,179,0.12); title Inter 43.2px/800, line-height 1.08, letter-spacing -0.03em, #1f2937; subtitle 16.8px #667085; author links 17.28px/600 #e891b3; venue line 32px/900 #d47a9e with text-shadow 0 6px 18px rgba(190,24,93,0.13)."
2. "Make pill buttons: padding 12px 18px, 999px radius, rgba(255,255,255,0.9) fill, 1px rgba(232,145,179,0.2) border, 15.36px/700 #1f2937 with an 18px icon, shadow 0 8px 20px rgba(232,145,179,0.06), hover translateY(-2px). Primary: linear-gradient(135deg, #e891b3 0%, #f0a0b8 100%), white text, no border."
3. "Create section cards: white, 22px radius, 28px padding, 26px apart, shadow 0 12px 40px rgba(232,145,179,0.10); title 24.8px/800 #1f2937; body 16px/1.95 #374151 justified. Tables inside a 16px-radius wrap with header gradient #fffafb → #fef5f7, 13.76px cells, best values 900 #d47a9e."

## Similar Pages

- The author's other project pages that share `paper-modern.css` (listed in the "More Related Research" menu).
- Card-based "soft UI" research pages with pastel backgrounds and tinted shadows.

## Quick Start

```css
:root {
  --card: rgba(255, 255, 255, 0.86);
  --card-solid: #fff;
  --text: #1f2937;
  --muted: #667085;
  --line: rgba(232, 145, 179, 0.15);
  --sakura: #e891b3;
  --sakura-dark: #d47a9e;
  --sakura-light: #f0a0b8;
  --shadow: 0 12px 40px rgba(232, 145, 179, 0.10);
  --radius: 22px;
  --maxw: 1160px;
  --font: "Inter", sans-serif;
}
body {
  background: radial-gradient(ellipse at 15% 5%, rgba(232, 145, 179, 0.13), transparent 40%),
              radial-gradient(ellipse at 85% 10%, rgba(186, 163, 220, 0.09), transparent 35%),
              linear-gradient(180deg, #fefbfc 0%, #f8f5f9 40%, #f5f7fb 100%);
  background-attachment: fixed;
}
```

## Provenance

- **URL**: https://xiangyuezhang.com/SemTalk/
- **Paper**: SemTalk: Holistic Co-speech Motion Generation with Frame-level Semantic Emphasis (arXiv 2412.16563), Xiangyue Zhang, Jianfang Li, Jiaxu Zhang, Ziqiang Dang, Jianqiang Ren, Liefeng Bo, Zhigang Tu (Wuhan University; Tongyi Lab, Alibaba Group; Zhejiang University).
- **Venue**: ICCV 2025.
- **Selection reason**: the arXiv comment states acceptance at ICCV 2025 and links this project page.
- **Template credit**: none stated; the page uses the author site's shared `paper-modern.css` (custom, minified) with Font Awesome, Academicons and MathJax.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `paper-modern.css` and `index.html` read directly, on 2026-10-28.
