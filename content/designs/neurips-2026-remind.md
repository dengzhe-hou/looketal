# ReMind Media Wall — Style Reference

> A corporate research reel: a floating glass pill nav, a grotesk headline that turns electric blue halfway through, and wall-to-wall video tiles.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's stylesheets assets/css/styles.css (an Applied Intuition house style with design tokens) and assets/css/site.css (page additions). The hero fades in on load, so the 1440 screenshot catches the title partly transparent (gray and pale blue); the computed values after the transition are #111111 and #006cfa, and those are used here.

## Overview

ReMind is a white, left-aligned page with a 1280px frame. A frosted pill-shaped header floats 14px from the top: a black triangular brand mark with "ReMind" in Applied Sans Display Bold, and small gray nav links on the right. The hero has a mono uppercase eyebrow with a small black square, then a 58px bold grotesk title whose subtitle half ("Eliciting Dynamic Memory for Out-of-Sight State Evolution") is in #006cfa, a 24px XCharter serif standfirst, and four small white outlined buttons. Every section after that is a "media wall": a mono numbered eyebrow ("01 · OUT-OF-SIGHT STATE EVOLUTION"), a 35px semibold heading, a serif lead, then rows separated by hairlines, each with a bold row label on the left, a gray serif description on the right, and a tight grid of 16:9 video tiles (4, 5 or 6 across, 8px gaps). Sections alternate white and #f6f7f9 and are divided by 1px #e4e4e4 rules. The footer is a near-black band.

## First Viewport

Color share of the 1440×900 viewport: #ffffff 83% (page), #6a8ab6 3% and #bfcde0 3% (the blue title half mid-fade), #fdfdfd 3%, #f5f6f7 3% and #fafafb 2% (the header pill and the start of the next section), #dee1e4 2% (hairlines and pill border). At rest the fold is white with black and #006cfa type; no media is above the fold.

Anatomy in DOM order (content x 104–1336):

1. **Header pill** `header.site-header > .header-pill`: fixed, inset 14px from the top and 16px from the sides, max-width 1280px, 60px tall, padding 0 22px; background rgba(255,255,255,.72) with saturate(160%) blur(14px), 1px rgba(17,17,17,.07) border, radius 999px, shadow 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07). Brand at left: 1.15em black triangle-arrow mask + "ReMind" Applied Sans Display 16.8px/700, letter-spacing -0.01em, #111111. Nav right: State, Control, OOD generalization, Clean video, Method, Citation, Code ↗, Applied Sans Text 13px/400, letter-spacing .01em, #767676, 24px apart; active link #111111 600. Gap to hero eyebrow 26px.
2. **Eyebrow** `p.eyebrow`: "CAUSAL AUTOREGRESSIVE VIDEO GENERATION", SFMono/JetBrains Mono stack 13.8px uppercase, letter-spacing .16em, #767676, preceded by a 0.5em #111111 square. Top at 114px. Gap 16px.
3. **Title** `h1`: Applied Sans Display 57.6px/700 (clamp 2.05rem, 5vw, 3.6rem), line-height 1.04, letter-spacing -0.02em, #111111, left, max-width 25ch (959px), four lines; `span.accent` in #006cfa. Gap 24px.
4. **Lead** `p.lead`: XCharter 24px/400 (clamp 1.25rem, 2.2vw, 1.5rem), line-height 1.45, #2a2a2a, max-width 56ch (854px), three lines with em dashes. Gap 40px.
5. **Buttons**: Code ↗, arXiv ↗, Models ↗, Dataset ↗; 39px tall white outlined buttons, 13px/600, radius 8px, 1px #e4e4e4 border, about 10px apart.
6. **Section rule** at y 695 (hero padding-bottom 96px): 1px #e4e4e4; the 01 section starts below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| White | #ffffff | --white | page, odd sections, header pill base, buttons |
| Ink | #111111 | --ink | title, headings, row labels, brand, eyebrow square, footer band |
| Applied Blue | #006cfa | --blue | title accent, figure labels, button hover border and text, primary button, BibTeX copy hover, skip link |
| Blue Dark | #0052bd | --blue-dark | primary button hover |
| Gray | #767676 | --gray | nav links, eyebrows, row descriptions, tile captions |
| Lead Ink | #2a2a2a | (literal) | hero lead and section leads |
| Caption Ink | #333333 | (literal) | figure captions |
| Gray Line | #e4e4e4 | --gray-line | section rules, row rules, button borders, media frame borders |
| Gray Soft | #f6f7f9 | --gray-soft | alternating section background |
| Highlight Wash | #e0ecff | --blue-wash-2 | marker-style highlight under key lead phrases |
| Dark Mat | #0d1117 | --dark-mat | ground behind videos and images in media frames |
| Code Ground | #0f1115 | (literal) | BibTeX block |
| Code Text | #e7e9ee | (literal) | BibTeX text |
| Footer Text | #cfd3da | (literal) | footer text on the #111111 band |

## Tokens — Typography

- **Display**: declared `"Applied Sans Display", "Helvetica Neue", Arial, sans-serif`; renders Applied Sans Display 600 and 700 (self-hosted TTF). Substitute: Inter Display.
- **UI sans**: declared `"Applied Sans Text", "Helvetica Neue", Arial, sans-serif`; renders Applied Sans Text 400 and 600. Substitute: Inter.
- **Serif (body)**: declared `"XCharter", Georgia, "Times New Roman", serif`; renders XCharter 400. Substitute: Charis SIL (same Charter design).
- **Mono**: declared `"SFMono-Regular", "JetBrains Mono", Menlo, Consolas, monospace`; renders Consolas on Windows. Substitute: JetBrains Mono.

| Role | Selector | Size at 1440 | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `.hero h1` | 57.6px (clamp 32.8px, 5vw, 57.6px) | 700 display | 1.04 | -0.02em |
| Section heading | `h2` | 35.2px (2.2rem) | 600 display | 1.12 | -0.01em |
| Hero lead | `.hero .lead` | 24px | 400 serif | 1.45 | 0 |
| Section lead | `.lead` | 20.8px (1.3rem) | 400 serif | 1.5 | 0 |
| Row label | `h3` | 18.9px (1.18rem) | 600 display | 1.12 | -0.005em |
| Body | `body` | 17px | 400 serif | 1.62 | 0 |
| Brand | `.brand-mark` | 16.8px | 700 display | 1.62 | -0.01em |
| Eyebrow | `.eyebrow` | 13.8px mono uppercase | 400 | 1.62 | .16em |
| Nav, buttons, captions | `.nav a`, `.btn`, `figcaption` | 13.1px (0.82rem) | 400 / 600 / 400 sans | 1.5–1.62 | .01em / 0 |
| Tile label | `.tile-label` | 11.5px uppercase sans | 600 | 1.25 | .03em |
| BibTeX | `.bibtex` | 12.8px mono | 400 | 1.55 | 0 |

Three families with fixed jobs: display grotesk for titles and labels, serif for reading text, mono for eyebrows and code.

## Tokens — Spacing & Shapes

- **Radius**: 999px for the header pill; 10px (`--radius`) for media frames, cards and BibTeX; 5px for showcase video tiles (radius / 2); 8px for buttons; 6px for the copy button.
- **Shadows**: `--shadow` 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07) on the header pill and standalone media frames; `--shadow-lift` 0 2px 6px rgba(17,17,17,.06), 0 18px 48px rgba(0,108,250,.10) on dialogs. Showcase tiles have no shadow.
- **Borders**: 1px #e4e4e4 for section and row rules, buttons and frames.
- **Spacing scale**: 0.5, 1, 1.5, 2.5, 4, 6rem (8, 16, 24, 40, 64, 96px).

## Layout Metrics

- **Container**: `.wide` max-width 1280px with 24px inline padding (content 1232px, x 104–1336 at 1440); `.reading` 720px for prose-only blocks.
- **Hero**: padding-top 60 + 14 + 40 = 114px, padding-bottom 96px; title max 25ch, lead max 56ch.
- **Sections**: padding-block 96px (64px ≤820px), 1px #e4e4e4 top border; intro max-width 58rem with h2 max 22ch and lead max 62ch, 40px below the intro.
- **Showcase rows**: each row starts with a 1px rule and 16px padding-top; heading grid 0.6fr / 1.4fr with 24px gap (label left, description right); 16px below; rows 64px apart.
- **Video grids**: `video-grid--4`, `--5`, `--6` with 8px gaps; tiles 16:9 (832/480), 5px radius; captions min-height 2.4rem.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >1100px | 24px | 17px | 5vw, max 57.6px | video grids 4/5/6 across |
| ≤1100px | 24px | 17px | 5vw | 5- and 6-up grids become 3 across, 4-up becomes 2 |
| ≤820px | 24px | 17px | 5vw | header splits into two frosted circles (brand, menu) with a full-screen overlay nav at 1.7rem; header 52px; sections 64px |
| ≤700px | 24px | 17px | 5vw | showcase heading stacks; all grids 2 across |
| ≤440px | 24px | 17px | 32.8px floor | grids 1 across |

## Components

- **Floating pill header**: see First Viewport; on scroll it stays fixed; active nav link turns #111111 600.
- **Outline button** `.btn`: Applied Sans Text 13.1px/600, padding 0.6em 1.05em, radius 8px, 1px #e4e4e4 border, #ffffff fill, #111111 text, trailing "↗" icon; hover border and text #006cfa; active shifts 1px down.
- **Primary button** `.btn-primary`: #006cfa fill and border, #ffffff text; hover #0052bd.
- **Eyebrow**: mono 13.8px uppercase, .16em tracking, #767676, with a 0.5em #111111 square before it and "NN ·" numbering.
- **Showcase row**: 1px #e4e4e4 top rule; h3 row label 18.9px/600 left; #767676 serif description right; grid of 16:9 video tiles (#0d1117 ground, 5px radius, 1px #e4e4e4 border) with 8px gaps.
- **Media frame** `.media-frame`: 16:9, 1px #e4e4e4 border, 10px radius, dark #0d1117 mat with a faint blue radial glow, `--shadow`.
- **Highlight** `mark.hl`: transparent top 60%, #e0ecff bottom 40%, like a highlighter stroke.
- **BibTeX** `.bibtex`: #0f1115, radius 10px, padding 24px, 12.8px mono #e7e9ee; copy button 11.5px/600 white on rgba(255,255,255,.08) with a rgba(255,255,255,.18) border and 6px radius, hover #006cfa.
- **Footer**: #111111 band, padding 40px 0, 13.1px #cfd3da, white brand mark.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | floating frosted pill with section links |
| Title block | yes | left-aligned bold grotesk with a blue second half |
| Authors / affiliations | absent from the source | no byline in the hero (the template's `.byline` style is unused) |
| Link buttons | yes | small white outlined buttons with arrows |
| Teaser | absent from the source | the hero is text only; media starts in section 01 |
| Video gallery | yes | dense 4/5/6-up 16:9 tile grids with row labels |
| Section bands | yes | alternating #ffffff and #f6f7f9 with hairline rules |
| Method | yes | text with a figure and labelled subsections (PM-RoPE) |
| Results table | absent from the source | results are videos only |
| BibTeX | yes | dark code block with a copy button |
| Footer | yes | near-black band |

## Adapting to Other Content

- **Authors**: add the template's byline under the lead: a 1px #e4e4e4 rule, then mono 13.1px #767676 with names in #111111, line-height 1.7.
- **Results table**: in a `.wide` section, use Applied Sans Text 13.1px, header 600 #767676 uppercase with a 1px #111111 bottom rule, rows split by 1px #e4e4e4, the proposed method's row values in 600 #006cfa.
- **Teaser video**: one `.media-frame` (16:9, 10px radius, dark mat, `--shadow`) under the buttons, full 1232px width.
- **Long publication list**: rows with the showcase-heading grid (0.6fr / 1.4fr): venue and year as the left label, title and authors in serif on the right, 1px rules between.
- **News**: an eyebrow "NN · NEWS" and a list of rows, date in mono 13.1px #767676, text in 17px serif.

## Do's and Don'ts

- Do color only the second half of the title (the subtitle) in #006cfa.
- Do keep three families with fixed roles: display for headings, serif for reading, mono for eyebrows.
- Do number every section eyebrow with "NN ·" and a black square.
- Do pack videos tightly (8px gaps) in rows with a label and a one-line description.
- Do alternate white and #f6f7f9 sections with 1px #e4e4e4 rules.
- Don't fill the link buttons; they are white with a hairline border.
- Don't round video tiles beyond 5px or add shadows to them.
- Don't center anything; the page is flush left in the 1280px frame.

## Surfaces

White page and odd sections, #f6f7f9 alternating sections, a frosted white pill header, #0d1117 mats behind media, #0f1115 code, and a #111111 footer band.

## Imagery

Dozens of short generated video clips (kitchens, liquids, lighting changes, camera pans) in 16:9 tiles; a method figure in the method section. The empty-looking band in the tall capture is the 02 section before its lazy-loaded videos appear.

## Layout

Text-only hero, then stacked sections in a 1280px frame, each an intro plus labelled rows of video grids. About 7,500px tall.

## Agent Prompt Guide

Quick colors: white #ffffff, ink #111111, blue #006cfa (hover #0052bd), gray #767676, lead #2a2a2a, line #e4e4e4, soft band #f6f7f9, media mat #0d1117, footer text #cfd3da.

1. "Build a floating pill header: fixed, 14px from the top, max-width 1280px, 60px tall, padding 0 22px, radius 999px, background rgba(255,255,255,.72) with backdrop-filter saturate(160%) blur(14px), 1px solid rgba(17,17,17,.07), shadow 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07); brand 16.8px/700 #111111 left; nav 13.1px #767676 right, 24px gaps."
2. "Build a hero: mono 13.8px uppercase eyebrow, letter-spacing .16em, #767676, with a 0.5em #111111 square; h1 57.6px/700 grotesk, line-height 1.04, letter-spacing -0.02em, #111111, with the subtitle part in #006cfa; a 24px serif lead in #2a2a2a, line-height 1.45, max 56ch; white buttons 13.1px/600, radius 8px, 1px solid #e4e4e4, hover #006cfa."
3. "Build a showcase row: 1px solid #e4e4e4 top rule, 16px padding-top; a grid 0.6fr / 1.4fr with an 18.9px/600 label left and a #767676 serif description right; then a 4-column grid of 16:9 video tiles with 8px gaps, 5px radius, 1px solid #e4e4e4 and #0d1117 ground."

## Similar Pages

- Industry-lab research pages built on a tokenized house style (floating pill nav, mono eyebrows, alternating bands).
- Video-generation project pages that present results as dense labelled video walls.

## Quick Start

```css
:root {
  --blue: #006cfa;
  --blue-dark: #0052bd;
  --blue-wash-2: #e0ecff;
  --ink: #111111;
  --gray: #767676;
  --gray-line: #e4e4e4;
  --gray-soft: #f6f7f9;
  --white: #ffffff;
  --dark-mat: #0d1117;
  --font-display: "Applied Sans Display", "Helvetica Neue", Arial, sans-serif;
  --font-sans: "Applied Sans Text", "Helvetica Neue", Arial, sans-serif;
  --font-serif: "XCharter", Georgia, "Times New Roman", serif;
  --font-mono: "SFMono-Regular", "JetBrains Mono", Menlo, Consolas, monospace;
  --fs-body: 1.0625rem;
  --fs-title: clamp(2.05rem, 5vw, 3.6rem);
  --wide: 1280px;
  --header-h: 60px;
  --radius: 10px;
  --shadow: 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07);
}
```

## Provenance

- **URL**: https://remind-applied.github.io/
- **Paper**: Teaching Video Generators to Remember: Eliciting Dynamic Memory for Out-of-Sight State Evolution (arXiv 2605.25333), Tianshuo Xu et al.
- **Venue**: NeurIPS 2026.
- **Selection reason**: existing verified entry; the arXiv comment reads "Accepted by Neurips 2026. Project page: https://remind-applied.github.io/".
- **Template credit**: stylesheet header credits Applied Intuition, Inc. (Apache-2.0); this is their house project-page style.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and styles.css plus site.css read directly. Captured 2026-10-28.
