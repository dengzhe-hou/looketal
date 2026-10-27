# Authority Bias Essay — Style Reference

> A lab essay printed on good white stock: a serif headline, one ink-sketch cartoon, and a rust-red pencil for the margins.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's single stylesheet, styles.css. The page has no media queries other than one at 760px and no dark mode.

## Overview

The page reads like a long-form blog post from the Lossfunk lab, not a project landing page. A handwritten "lossfunk" logo sits alone at the top left. The title is Source Serif 4 Semibold at 48px, left-aligned in an 880px column with a gray sans byline (authors, lab, venue) and two black pill buttons. Below is a wide 16:9 hand-drawn cartoon (a user, an LLM robot and a top-hatted "verified" source). The article then narrows to a 640px serif text column on pure white, with a tinted "In brief" callout ruled in rust red (#b5452d), model-switch pills, prompt and response panels, figures that break out to 880px with rust "Figure N." labels, and a citation block. Links are underlined in rust. The only color on the page is that rust accent.

## First Viewport

Color share of the 1440×900 viewport: #ffffff 70% (page), #fdfdfd 12%, #fefefd 7% and #fafdfe 3% (the near-white ground of the cartoon), #959495 7% (the cartoon's gray-black ink). The fold is almost entirely white; the title and the black button are the darkest masses.

Anatomy in DOM order:

1. **Header** `header.site-header`: padding 22px 64px; only the handwritten logo image, 36px tall, at x 64. Gap 96px to the hero.
2. **Title** `.hero h1` (hero column 880px, x 280–1160): Source Serif 4 48px/600, line-height 1.12, letter-spacing -0.015em, #141413, left-aligned, `text-wrap: balance`, max-width 820px (three lines). Gap 24px.
3. **Meta line** `p.meta`: "Abhinav Rajeev Kumar and Paras Chopra · Lossfunk · NeurIPS 2026", Plus Jakarta Sans 15px/400, line-height 1.4, #5e5d59. Gap 28px.
4. **Buttons** `.actions`: "Read the paper" filled #141413 pill with #ffffff text, "Code" outlined pill; 40px tall, 10px apart. Gap 48px.
5. **Hero art** `figure.hero-art`: 880×495 (16:9), radius 12px, #f2f1ec placeholder ground fully covered by the illustration (a black-ink cartoon on white with blue "Correct" and red "Wrong" marks).

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Page White | #ffffff | --page | body background, filled-button label, figure image ground |
| Ink | #141413 | --ink | title, body text, h2, filled button and selected tab fill, outlined borders, prompt rule |
| Ink Hover | #3d3d3a | (literal) | filled button hover |
| Muted | #5e5d59 | --muted | meta line, figure captions, example intro, footer |
| Rust | #b5452d | --accent | link underlines, "IN BRIEF" label, list markers, callout left border, "Figure N." labels |
| Rule | #e3e2dd | --rule | paper-block top rule, footer top rule, response dividers |
| Panel | #f5f4f0 | --panel | In-brief callout, responses panel, BibTeX block |
| Placeholder | #f2f1ec | --placeholder | hero-art ground (hidden under the image) |

## Tokens — Typography

- **Serif (body and headings)**: declared `"Source Serif 4", Georgia, "Times New Roman", serif`; renders Source Serif 4 400, 400 italic, 600. Substitute: Newsreader.
- **Sans (UI)**: declared `"Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif`; renders Plus Jakarta Sans 400, 500, 600, 700. Substitute: Manrope.
- **Mono**: `ui-monospace, "SF Mono", Menlo, monospace` (system).

| Role | Selector | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `.hero h1` | 48px (32px ≤760px) | 600 serif | 1.12 | -0.015em |
| Section title | `.post h2` | 27px (23px ≤760px) | 600 serif | 1.25 | -0.01em |
| Citation heading | `.post h3` | 18px sans | 600 | 1.3 | 0 |
| Body | `body`, `.post p` | 17px serif (16px ≤760px) | 400 | 1.55 | 0 |
| Meta, buttons, tabs | `.meta`, `.button`, `.tabs button` | 15px sans | 400 / 500 / 500 | 1.4 / 1.33 / 1.3 | 0 |
| Response summary | `.responses summary` | 15px sans | 700 | 1.4 | 0 |
| Captions, footer | `.figure figcaption`, `.site-footer` | 14px sans | 400 | 1.45–1.5 | 0 |
| Brief label | `.brief-label` | 13px sans uppercase | 700 | 1.3 | 0.06em |
| BibTeX | `pre` | 13px mono | 400 | 1.55 | 0 |

The split is strict: serif for everything you read, sans for everything you click or that labels something.

## Tokens — Spacing & Shapes

- **Radius**: 999px for buttons and model tabs; 12px for hero art and BibTeX; 8px for figures, the responses panel, the copy button and the right side of the brief callout (`0 8px 8px 0`); 16px for the zoom dialog.
- **Shadows**: none.
- **Borders**: 1px #141413 on buttons and tabs; 3px #b5452d left border on the brief; 1px #141413 left rule on the prompt quote; 1px #e3e2dd for section and footer rules and between responses.
- **Links**: underline 1.5px #b5452d with 3px offset; hover 2px.

## Layout Metrics

- **Containers**: hero and figures `min(880px, 100% - 48px)` centered (x 280–1160 at 1440); article `.post` max-width 688px with 24px padding, so the text column is 640px (x 400–1040).
- **Figure breakout**: `.figure` width min(880px, 100vw − 48px) with a negative left margin of half the difference, so figures extend 120px past each side of the 640px text column.
- **Vertical rhythm**: header padding 22px; hero margin-top 96px; title → meta 24px; meta → buttons 28px; buttons → art 48px; art → article 64px; paragraphs 16px apart; h2 margin 52px above, 14px below; figures 32px above and below; brief 32px; examples 40px; paper block 48px with 32px padding above a rule; footer 96px above.
- **Brief callout**: padding 18px 22px 6px; list items 12px apart.
- **Responses panel**: padding 8px 28px; summaries 16px vertical padding.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >760px | 24px (header 64px) | 17px | 48px | hero 880px, text 640px, figures break out to 880px |
| ≤760px | 24px (header 20px) | 16px | 32px | hero margin 48px; h2 23px at 40px top margin; footer stacks; figures stay within the viewport minus 48px |

## Components

- **Filled pill** `.button`: padding 9px 20px, 1px #141413 border, radius 999px, #141413 fill, #ffffff Plus Jakarta Sans 15px/500, no icon; hover fill and border #3d3d3a.
- **Outline pill** `.button-outline`: same size, transparent, #141413 text; hover fills #141413 with #ffffff text.
- **In-brief callout** `.brief`: #f5f4f0 fill, 3px #b5452d left border, radius 0 8px 8px 0, padding 18px 22px 6px; label "IN BRIEF" 13px/700 uppercase 0.06em #b5452d; ordered list in 17px serif with rust 15px/600 sans markers.
- **Model tabs** `.tabs button`: padding 7px 16px, 1px #141413 border, radius 999px, transparent, 15px/500 sans; selected #141413 fill with #ffffff text; 8px gaps.
- **Prompt quote** `.prompt`: 1px #141413 left rule, padding 4px 0 4px 16px, labels in bold serif, quoted text italic.
- **Responses accordion** `.responses`: #f5f4f0 panel, radius 8px, padding 8px 28px; each `details` summary 15px/700 sans with a CSS chevron (8px, 1.5px #141413 strokes) that rotates when open; 1px #e3e2dd dividers.
- **Figure**: image radius 8px on #ffffff, caption 14px/1.45 #5e5d59 sans prefixed by "Figure N." in 600 #b5452d; images open in a dialog (radius 16px, backdrop rgba(20,20,19,.6)).
- **Citation**: 18px/600 sans heading with a "Copy BibTeX" button (padding 6px 12px, 1px #141413 border, radius 8px, 14px/500; hover inverted); BibTeX on #f5f4f0, radius 12px, padding 16px 18px.
- **Footer**: 1px #e3e2dd top rule, padding 32px 64px 48px, 14px #5e5d59, logo 28px on the right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | absent from the source | logo only, no links |
| Title block | yes | left-aligned serif headline in an 880px column |
| Authors / affiliations | yes, non-standard | a single gray sans meta line (two authors, lab, venue); no affiliation list |
| Link buttons | yes | two black pills, filled and outlined |
| Teaser | yes, non-standard | hand-drawn cartoon illustration, 16:9 |
| Abstract | yes, non-standard | written as essay paragraphs, then an "In brief" numbered callout |
| Interactive examples | yes | model tabs, prompt quote, accordion of responses |
| Figures | yes | breakout figures with rust "Figure N." captions, zoomable |
| Results table | absent from the source | results are figures only |
| BibTeX | yes | panel block with a copy button |
| Footer | yes | rule, credits and logo |

## Adapting to Other Content

- **More authors**: keep the single meta line while it fits two lines at 15px; beyond that, put a second meta line for affiliations in the same 15px #5e5d59 sans, separated by " · ".
- **Results table**: place it inside the 640px column (or as a breakout to 880px like a figure) in Plus Jakarta Sans 14px; header 600 with a 1px #141413 bottom rule, rows separated by 1px #e3e2dd, no fills; highlight the best value in 600 weight, and label it "Table N." in #b5452d like figure captions.
- **Long publication list**: serif 17px entries in the text column with the title as a rust-underlined link and venue in 15px #5e5d59 sans; 16px between entries.
- **News**: a dated list inside an In-brief style callout: #f5f4f0 panel, 3px #b5452d left border, rust 13px uppercase label "NEWS".
- **More buttons**: add outlined pills only; keep exactly one filled black pill.

## Do's and Don'ts

- Do keep body text serif at 17px/1.55 in a 640px column on pure white.
- Do use sans only for UI and labels (meta, buttons, captions, tabs).
- Do reserve rust #b5452d for link underlines, labels and the one callout rule.
- Do let figures break out to 880px while text stays at 640px.
- Don't add color blocks, gradients or shadows; panels are #f5f4f0 at most.
- Don't center the title; it aligns with the left edge of the 880px hero column.
- Don't add a nav bar; the logo alone is the header.

## Surfaces

Pure white #ffffff page; #f5f4f0 panels for the brief, responses and BibTeX; images on white with 8–12px radii. No bands, no cards with borders, no elevation.

## Imagery

A black-ink hand-drawn cartoon as the teaser (with small blue and red annotation marks), then plotted figures from the paper (bar and line charts, heatmaps) on white.

## Layout

Single column essay: an 880px hero block (title, meta, buttons, art) over a 640px reading column, with figures breaking out to 880px. About 8,900px tall.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #141413, muted #5e5d59, accent #b5452d, rule #e3e2dd, panel #f5f4f0, button hover #3d3d3a.

1. "Build an essay hero: an 880px left-aligned column with 96px top margin; h1 Source Serif 4 48px weight 600, line-height 1.12, letter-spacing -0.015em, #141413, max-width 820px, text-wrap balance; 24px below, a meta line in Plus Jakarta Sans 15px #5e5d59; 28px below, pills with 10px gap."
2. "Build pill buttons: padding 9px 20px, radius 999px, 1px solid #141413, Plus Jakarta Sans 15px/500; filled variant #141413 with #ffffff text, hover #3d3d3a; outline variant transparent with #141413 text, hover inverts."
3. "Build an In-brief callout: background #f5f4f0, border-left 3px solid #b5452d, radius 0 8px 8px 0, padding 18px 22px 6px; label 13px/700 uppercase, letter-spacing 0.06em, #b5452d; ordered list in Source Serif 4 17px/1.55 #141413 with #b5452d markers."

## Similar Pages

- Lab blog posts that present a paper as an essay (narrow serif column, one illustration, few UI elements).
- Distill-style articles where figures break out of a narrow text measure.

## Quick Start

```css
:root {
  --page: #ffffff;
  --ink: #141413;
  --ink-hover: #3d3d3a;
  --muted: #5e5d59;
  --rule: #e3e2dd;
  --panel: #f5f4f0;
  --placeholder: #f2f1ec;
  --accent: #b5452d;
  --sans: "Plus Jakarta Sans", "Helvetica Neue", Arial, sans-serif;
  --serif: "Source Serif 4", Georgia, "Times New Roman", serif;
  --text: 640px;
  --wide: 880px;
}
body { background: var(--page); color: var(--ink); font: 400 17px/1.55 var(--serif); }
a { text-decoration-color: var(--accent); text-decoration-thickness: 1.5px; text-underline-offset: 3px; }
```

## Provenance

- **URL**: https://authority-bias.vercel.app/
- **Paper**: Authority Bias in Language Models: Source Deference and User Agreement Are Not Interchangeable (arXiv 2609.37616), Abhinav Rajeev Kumar and Paras Chopra.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and links this page.
- **Template credit**: Lossfunk lab page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and styles.css read directly. Captured 2026-10-28.
