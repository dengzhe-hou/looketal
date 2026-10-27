# Vermilion Editorial Rail — Style Reference

> A quarterly journal on warm paper, one vermilion pen, and a margin index that follows you down the page.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles and boxes of the side contents rail, hero chips, title, authors, logo tiles, link buttons, figure cards, section kickers, stat column, tables and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's inline `<style>` and Tailwind 3.4.16 Play CDN config. The page sets `body { zoom: 0.8 }` at ≥1024px, so every declared size renders at 80% on desktop; this file gives the rendered desktop size first and the declared size in parentheses. Colors are declared in OKLCH and converted to sRGB hex here.

## Overview

FOCA reads like an editorial feature rather than a template page. The background is warm off-white paper (#fbfaf6) with a faint 22px dot grid. A fixed left rail labelled "CONTENTS" lists six numbered sections in serif, and a vermilion line-and-dot marker slides to the active one. The hero starts with small rounded chips (an ICML logo chip, then "ROBOT LEARNING" and "VISION-LANGUAGE-ACTION" in spaced capitals). Then comes a large Source Serif 4 title in near-black ink (#141b24) with two phrases picked out in vermilion (#dd5230), and an italic grey subtitle. Twenty-three authors with superscripts sit in a compact Inter paragraph, and two rows of institution logos are set in white rounded tiles. Four small black pill links end in arrow icons and turn vermilion on hover. Every section opens with a hairline rule, a tiny vermilion small-caps kicker and a serif headline. The abstract puts a column of big serif statistics beside the text, and figures and tables sit in white 12px-radius cards with hairline borders and "FIGURE N" kickers in the captions.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): paper #fbfaf6 70.7%, white #fefefc 9.3% (logo tiles, chips, figure card), paper shade #f6f5f1 8.1%, warm grey #a9a2a0 7.8% (text, logos, rules), remainder 4.1%. The vermilion accent covers well under 1% of the area but is the only saturated color besides the logos.

Anatomy in DOM order (y = top of element box, rendered px):

1. **Scroll progress bar** (`#scroll-progress`), fixed at y 0, 3px tall, #dd5230, width grows with scroll (0% at the top).
2. **Contents rail** (`nav.side-nav-wrapper`, `zoom: 1.4`, shown at ≥1280px), fixed left, vertically centered (x 27–183, y 310–590): "CONTENTS" in Inter 11.2px/600 uppercase, tracking 0.24em, #4d5660; six links each a mono number (12.3px, #4d5660 at 50%) and a serif label (16.8px, #4d5660, hover #141b24), rows 43px apart. The active item carries a 24px #dd5230 line ending in a 6px dot.
3. **Chip row**, y about 60 at x 330: an ICML chip (white 60% fill, 1px #bbb7ad 60% border, fully rounded, ICML logo plus "ICML 2026" in 8.8px/600 uppercase tracking 0.14em, #141b24), then two chips "ROBOT LEARNING" and "VISION-LANGUAGE-ACTION" (8.8px/500, #4d5660, padding 4px 10px declared). Gap 26px.
4. **Title** (`h1.font-serif.md:text-6xl`), y 146, three left-aligned lines in a 781px column, Source Serif 4 48px/400 (60px), line-height 1.04, tracking -0.025em, #141b24; "Data-Efficient" and "Vision-Language-Action" in #dd5230.
5. **Subtitle** (`h1 > span.block.italic`), y 300, one line, Source Serif 4 italic 28.8px/400 (36px), #4d5660, 10px above it. Gap 25px.
6. **Authors** (`p.leading-relaxed`), y 357, four lines, Inter 12.8px/400 (16px), line-height 20.8px, #141b24 at 90%, superscript markers. Gap 10px.
7. **Notes and affiliations** (`p.text-sm.text-muted-foreground`), y 450 and 474, Inter 11.2px (14px), #4d5660, items separated by " · ", three lines of numbered institutions. Gap 26px.
8. **Logo tiles**, two centered rows (y 555 and 638), white tiles with 1px #bbb7ad 50% borders, 9.6px radius, padding 8px 12px declared, 32px gaps.
9. **Link pills** (`a.link-btn`), y 747, 31px tall, left-aligned: Paper, Code, Models and Datasets, Video; #141b24 fill, #fbfaf6 text, Inter 11.2px/500, Lucide icon left and arrow right. Gap 32px.
10. **Figure 1 card** (`figure.rounded-xl.border.bg-card`), y 810, 781px wide, white, framework diagram; the fold cuts it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #fbfaf6 | `--paper` oklch(0.985 0.005 95), `--background` | Page background, link-pill text, BibTeX text |
| Dot Grid | rgba(0,0,0,0.025) | body `radial-gradient` 1px dots, 22px grid | Background texture |
| Ink | #141b24 | `--ink` oklch(0.22 0.02 250), `--foreground` | Title, headings, author text (at 90%), table text, link-pill fill, BibTeX block fill |
| Muted Ink | #4d5660 | `--muted-foreground` oklch(0.45 0.02 250) | Subtitle, affiliations, chips, rail labels, stat labels, Key Idea body text, table headers, footer text |
| Vermilion | #dd5230 | `--accent` oklch(0.62 0.18 35), `--ring` | Title highlights, section kickers, figure-caption kickers, rail indicator, scroll bar, stat highlight, own-method table row, pill hover fill, footer email links |
| Rule | #bbb7ad | `--rule` oklch(0.78 0.015 90) | Section top rules and card borders (at 70%), chip and logo-tile borders (at 50–60%), table row rules (at 40%) |
| Border | #dad7d0 | `--border` oklch(0.88 0.01 90) | Default border color for all elements |
| Card White | #ffffff | `--card` oklch(1 0 0) | Figure and table cards, logo tiles, chips (at 60%), Key Idea cards (at 60%) |
| Accent Wash | rgba(221,82,48,0.1) | `bg-accent/10` | Own-method table row background |
| Card Shadow | rgba(0,0,0,0.05) | Tailwind `shadow-sm` | Figure card shadow `0 1px 2px` |

Declared but not visible: `--primary` (#13335a) and `--muted` (#f3f0e9) are defined in `:root` but no rendered element uses them.

## Tokens — Typography

- **Display and headings**: `serif: ['"Source Serif 4"', '"Source Serif Pro"', 'Georgia', 'serif']`, loaded from Google Fonts (400, 400 italic, 700). Rendered: Source Serif 4 400, 400i, 700 (`fonts_loaded`). Substitute: Newsreader (same text-serif proportions).
- **Text and UI**: `"Inter", ui-sans-serif, system-ui, sans-serif`, Inter 400–700 loaded. Substitute: Geist.
- **Mono**: JetBrains Mono 400 for rail numbers and the BibTeX block.
- **Zoom**: `@media (min-width: 1024px) { body { zoom: 0.8 } }`; the contents rail adds `zoom: 1.4` (net 1.12).

| Role | Selector | Rendered desktop (declared) / line-height | Weight | Color |
|---|---|---|---|---|
| Title | `h1.font-serif.md:text-6xl.tracking-tight` | 48px (60px) / 1.04 | 400 | #141b24, highlights #dd5230 |
| Subtitle | `h1 span.italic.md:text-4xl` | 28.8px (36px) italic | 400 | #4d5660 |
| Section headline | `h2.font-serif.md:text-4xl` | 28.8px (36px) / 1.05 | 400 | #141b24 |
| Key Idea title | `h3.font-serif.text-3xl` | 24px (30px) / 1.2 | 400 | #141b24 |
| Section kicker | `span.text-[11px].uppercase.tracking-[0.22em]` | 8.8px (11px) | 600 | #dd5230 |
| Abstract text | `div.font-serif.text-lg.leading-[1.7]` | 14.4px (18px) / 1.7 | 400, key phrases 700 | #141b24 at 90% |
| Stat number | `aside div.font-serif.text-3xl` | 24px (30px) | 400 | #141b24 |
| Stat label | `div.text-[13px].uppercase.tracking-[0.18em]` | 10.4px (13px) | 400 | #4d5660 |
| Authors | `p.leading-relaxed` | 12.8px (16px) / 20.8px | 400 | #141b24 at 90% |
| Affiliations | `p.text-sm.text-muted-foreground` | 11.2px (14px) / 18.2px | 400 | #4d5660 |
| Link pill | `a.link-btn` | 11.2px (14px) | 500 | #fbfaf6 |
| Figure caption | `figcaption.text-[15px]` | 12px (15px) / 1.625 | 400 | #141b24 at 70% |
| Table header | `th.text-[11px].uppercase.tracking-[0.18em]` | 8.8px (11px) | 500 | #4d5660 |
| Table method cell | `td.font-medium` | 11.2px (14px) | 500 | #141b24 |
| Table number | `td.font-serif.text-lg` | 14.4px (18px) | 400, own row 700 | #141b24, own row #dd5230 |
| Rail label | `.nav-label.font-serif.text-[15px]` | 16.8px (15px at zoom 1.12) | 400 | #4d5660 |
| BibTeX | `pre.text-xs` | 9.6px (12px) | 400 | #fbfaf6 on #141b24 |

## Tokens — Spacing & Shapes

`--radius` is 0.5rem; Tailwind radii render at 80% on desktop.

| Element | Radius (rendered) | Border | Shadow |
|---|---|---|---|
| Chip | 9999px | 1px #bbb7ad at 60% | none |
| Logo tile | 9.6px (`rounded-xl`) | 1px #bbb7ad at 50% | none |
| Link pill | 9999px | 1px #141b24 at 80%; hover border and fill #dd5230 | none |
| Figure card | 9.6px | 1px #bbb7ad at 70%, caption separated by a 1px top rule | `0 1px 2px rgba(0,0,0,0.05)` |
| Key Idea card | 9.6px | 1px #bbb7ad at 60% | none |
| Table card | 9.6px | 1px #bbb7ad at 70%; header rule 1px at 70%, row rules at 40% | none |
| Inner figure image | 6.4px (`rounded-lg`) | 1px #bbb7ad at 60% | none |
| BibTeX block | 9.6px | 1px #bbb7ad at 70% | none |

## Layout Metrics

- **Container**: Tailwind `max-w-5xl` (1024px declared) with `px-6`; at 1440px with zoom 0.8 it renders 819px wide (content 781px) centered at x 310–1129.
- **Hero**: `pt-14 md:pt-20 pb-10` (64px top and 32px bottom rendered on desktop); 32px rendered above the title (`mt-8`), 25px between subtitle and authors, logo rows 26px apart with 32px gaps.
- **Contents rail**: `fixed left-0 top-1/2 -translate-y-1/2`, hidden below 1280px (`xl:block`), 24px left margin, 156px wide.
- **Sections**: `section.max-w-5xl.px-6.pb-16`; each starts with `border-t` (1px rule) and `pt-8`, kicker and headline 12px apart, 40px (`mb-10`) before content, 51px bottom padding rendered.
- **Abstract grid**: `md:grid-cols-[1fr_2fr]` with a 40px gap (32px rendered): stat column about 250px, text column about 500px.
- **Key Idea cards**: stacked with 24px gaps (19px rendered), padding 32px (26px rendered), inner text capped at `max-w-4xl`, images at `max-w-3xl` or `max-w-4xl`.
- **Tables**: in a scrollable white card (`overflow-x-auto`), cells padding 16px 20px (13px 16px rendered).
- **Footer**: 1px top rule, `py-10`, flex row from 768px with the identity block left and a link list right.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1280px | centered 819px column (rendered) | 12.8px (16px) | 48px (60px) | contents rail visible |
| 1024–1279px | centered column | 12.8px (16px) | 48px (60px) | rail hidden; zoom 0.8 still applies |
| 768–1023px | 24px | 16px | 60px | no zoom, so type renders at full declared size; abstract grid 1:2; footer row layout |
| <768px | 24px | 16px | 36px (`text-4xl`) | single column; section headlines 30px; subtitle 30px; stat column stacks above the abstract; tables scroll horizontally |

## Components

- **Contents rail**: fixed, vertically centered; "CONTENTS" label, then a list of `a.nav-link` rows (mono number + serif label, both #4d5660, label turns #141b24 on hover); a `#nav-indicator` (24px 1px #dd5230 line plus a 6px #dd5230 dot) translates with a 300ms ease-out to the active row.
- **Tag chip**: `inline-flex rounded-full border border-rule/60 bg-card/60 px-2.5 py-1`, 11px declared uppercase Inter 500, tracking 0.14em, #4d5660. The venue chip holds a 60px-tall (48px rendered) logo and bold "ICML 2026".
- **Accent title**: serif 400, tight tracking, ink color with selected phrases wrapped in `span.text-accent`; an italic muted subtitle as a block span inside the h1.
- **Logo tile**: `rounded-xl border border-rule/50 bg-white px-3 py-2`, logo at max height 44–96px declared.
- **Link pill**: `a.link-btn`, fully rounded, #141b24 fill, 1px #141b24 at 80% border, padding 8px 16px declared, #fbfaf6 Inter 14px/500 declared, Lucide icon left, arrow icon right; hover fill and border #dd5230 with the arrow sliding 3px right (0.15s).
- **Section opener**: `border-t border-rule/70 pt-8`, a vermilion 11px uppercase kicker with 0.22em tracking ("ABSTRACT", "RESULTS · REAL WORLD"), then a 36px declared serif headline written as a sentence.
- **Stat column**: an `aside` of three blocks, each a 13px declared uppercase grey label, a 30px declared serif figure, and a 12px grey note, with one highlight in serif vermilion ("40% data").
- **Figure card**: white, `rounded-xl`, 1px rule border, `shadow-sm`; media on top, then a `border-t` caption (padding 16px 20px declared) starting with a vermilion "FIGURE N" kicker and continuing in 15px declared text at 70% ink.
- **Results table**: in a white rounded card; header row in 11px declared uppercase grey with 0.18em tracking; method names in Inter 500, numbers in serif 18px declared; row rules at 40% rule; the own-method row prefixed "▶", tinted `bg-accent/10`, all cells bold vermilion.
- **BibTeX block**: `pre.rounded-xl.bg-ink.p-6.text-xs`, JetBrains Mono on #141b24 in #fbfaf6.
- **Scroll reveal**: `.reveal` blocks fade in from 16px below over 0.6s; disabled under `prefers-reduced-motion`.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Contents / navigation | yes | fixed numbered side rail with sliding marker (≥1280px), footer link list |
| Venue and topic tags | yes | rounded chips above the title |
| Title with subtitle | yes | serif title with vermilion phrases, italic grey subtitle |
| Authors and affiliations | yes | compact Inter paragraph, numbered affiliations |
| Institution logos | yes | two centered rows of white tiles |
| Link buttons | yes | four black pills with arrows |
| Teaser figure | yes | framework diagram in a captioned card |
| Abstract with key numbers | yes | stat column beside serif abstract text |
| Method | yes | video card plus three Key Idea cards |
| Real-world and simulation results | yes | many videos (33) in captioned cards |
| Results tables | yes | four tables in white cards, own row tinted vermilion |
| BibTeX | yes | dark ink block |
| Footer | yes | identity line, correspondence emails in vermilion, section links |

## Adapting to Other Content

- **Fewer authors**: keep the same compact Inter paragraph; with under six names, raise it to 16px declared and drop the logo rows if institutions are few.
- **More sections**: the rail takes up to about eight items before it crowds the viewport; keep numbers two-digit.
- **A results table**: already native; mark only the own-method row with `bg-accent/10` and vermilion bold, and keep other rows unstyled.
- **News**: a section with a "NEWS" kicker and a list where each item has a mono date in #4d5660 and serif text, separated by 40%-rule hairlines.
- **Long publication lists**: same list pattern, titles in serif #141b24 with hover #dd5230, venue in an uppercase grey micro-label.
- **Without logos**: move affiliations into the chip row or keep the text list; the hero still holds with title, authors and pills.

## Do's and Don'ts

- Do keep exactly one saturated color, vermilion #dd5230, and use it for markers: title phrases, kickers, the active rail dot, the own-method row.
- Do open every section with a hairline, a spaced-capitals kicker and a sentence-style serif headline.
- Do put key numbers in serif beside prose rather than in colored badges.
- Do keep figures and tables inside white cards with hairline borders on the paper background.
- Don't rely on `zoom: 0.8` without checking small text: 11px kickers render at 8.8px on desktop.
- Don't use bold weights for headings; the serif stays at 400.
- Don't add colored section backgrounds; paper and white cards are the only surfaces.

## Surfaces

Paper (#fbfaf6) with a 22px dot grid as the base; white cards and tiles (#ffffff, sometimes at 60%) for figures, tables, logos and Key Ideas; one dark ink surface (#141b24) for the BibTeX block and the link pills. Hairlines in #bbb7ad at 40–70% do the separating.

## Imagery

A crisp framework diagram with pastel token blocks and orange highlights, robot-manipulation videos (ALOHA, UR5, simulation suites) in cards, method overview figures inside Key Idea cards, and a row of institutional logos in white tiles.

## Layout

A single 781px column (rendered) centered on paper, with a fixed contents rail in the left margin on wide screens. The abstract splits 1:2 into stats and text. Rendered height about 9,560px at 1440px.

## Agent Prompt Guide

Quick colors: paper #fbfaf6, ink #141b24, muted #4d5660, vermilion #dd5230, rule #bbb7ad, border #dad7d0, cards #ffffff, own-row wash rgba(221,82,48,0.1).

1. "Build an editorial hero on #fbfaf6 with a 22px dot grid (`radial-gradient(rgba(0,0,0,0.025) 1px, transparent 1px)`): rounded chips in 11px uppercase Inter (tracking 0.14em, #4d5660, white 60% fill, 1px #bbb7ad border); a Source Serif 4 60px/400 title in #141b24 (line-height 1.04, tight tracking) with key phrases in #dd5230; a 36px italic #4d5660 subtitle; authors in Inter 16px; black pill links (#141b24 fill, #fbfaf6 14px/500 text, icon left, arrow right; hover #dd5230)."
2. "Create a section opener: 1px #bbb7ad (70%) top rule, 32px padding-top, an 11px uppercase #dd5230 kicker with 0.22em tracking, then a 36px Source Serif 4 headline in #141b24 written as a sentence; below, a 1:2 grid with a stat column (13px uppercase #4d5660 label, 30px serif number, 12px grey note) beside 18px serif body text at line-height 1.7."
3. "Make a results table card: white, 12px radius, 1px #bbb7ad border; header 11px uppercase #4d5660 with 0.18em tracking and a 1px rule; method names Inter 14px/500, numbers Source Serif 4 18px, row rules at 40%; the own-method row prefixed '▶', background rgba(221,82,48,0.1), all text bold #dd5230."

## Similar Pages

- Editorial-style research sites built with shadcn-like OKLCH tokens and Tailwind (paper background, serif display, single accent).
- Long-form project pages with a fixed numbered table of contents in the margin.

## Quick Start

```css
:root {
  --paper: #fbfaf6;
  --ink: #141b24;
  --muted-ink: #4d5660;
  --accent: #dd5230;
  --rule: #bbb7ad;
  --border: #dad7d0;
  --card: #ffffff;
  --accent-wash: rgba(221, 82, 48, 0.1);
  --dot-grid: radial-gradient(rgba(0, 0, 0, 0.025) 1px, transparent 1px);
  --font-serif: 'Source Serif 4', 'Source Serif Pro', Georgia, serif;
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
  --radius: 0.5rem;
  --container: 1024px;
  --title-size: 60px;
  --headline-size: 36px;
  --kicker-size: 11px;
  --kicker-tracking: 0.22em;
}
```

## Provenance

- **URL**: https://focavla.github.io/
- **Paper**: FOCA: Future-Oriented Conditioning for Data-Efficient Vision-Language-Action Adaptation (arXiv 2606.20867), Duc Minh Nguyen, Nghiem Tuong Diep, Binh Gia Nguyen et al. (VinRobotics, VinUniversity, DFKI and others).
- **Venue**: ICML 2026.
- **Selection reason**: the arXiv 2606.20867 comment states acceptance at ICML 2026 and links the page. Chosen for the editorial serif headline with a single vermilion accent, small-caps section kickers, the sticky numbered contents rail, the stat column beside the abstract and neatly captioned figure frames.
- **Template credit**: none stated; hand-built on the Tailwind 3.4.16 Play CDN with OKLCH design tokens in an inline `<style>` and Lucide icons.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share (boxes in rendered px, font sizes as declared and scaled by the 0.8 body zoom), the first-viewport screenshot and scaled full-page capture, the inline `<style>`, Tailwind config and the HTML; OKLCH values converted to sRGB hex. Date 2026-10-28.
