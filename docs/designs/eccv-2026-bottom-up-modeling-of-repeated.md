# Repeated Elements — Style Reference

> A blueprint index card: pale blue dot-grid paper, a bookish serif title, small-caps blue labels, and a single navy slab for the citation.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, plus targeted probes of the hero, contribution list, figure panels, results table and BibTeX band), the 1440×900 shot and a full-page capture, and the page's own `style.css` and `index.html`. No web fonts load: the title stack starts with Iowan Old Style (macOS) and renders Palatino Linotype on Windows; the body stack renders Arial on Windows (Helvetica is substituted) and the system face on macOS.

## Overview

A short, restrained single-column page (4,770px) on cool off-white #f7f9fc with slate text #3c4c63. The header band carries a faint 15px dot grid in 8%-opacity blue and ends with a 1px #dfe7f1 rule. Everything in it is centred: a filled blue #1f7dd9 "ECCV 2026" pill, a two-line 42px/500 serif title in deep navy #101e33, authors separated by middots with dotted underlines and blue superscripts (an orange ✉ marks the corresponding author), a 14px affiliation line, and four 43px buttons with 8px radius and emoji icons (blue filled "Paper (PDF)", white outlined arXiv, Code, BibTeX). Below, sections in a 920px column are separated by 1px #dfe7f1 rules and open with 13px bold uppercase labels in deep blue #0f4e8c (ABSTRACT, CONTRIBUTIONS, METHOD, RESULTS, CONCLUSION). The teaser figure sits in a white 10px-radius frame; the method and qualitative figures sit in white 10px-radius panels with a ruled caption; contributions use 8px blue square bullets; the results table is set in monospace inside a white rounded wrapper with blue group headers, orange requirement dots and a pale-blue "Ours" row. The page ends with a full-width navy #0f1b2c BibTeX band with rounded corners and a centred gray acknowledgement.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): paper #f7f9fc / #f6f9fc / #fcfdfe / #f8f9fc / #f7f9fd / #fafaf4 together 83.7%; light gray #f1f3f5 6.4% (teaser frame and dot grid); warm olive-gray #a8a798 10.0% (the apple teaser image and text antialiasing). The blue pill and button cover too little area to form a cluster.

Anatomy in DOM order (desktop 1440px, everything centred in `.wrap`, max 920px with 24px padding → content x 284–1156):

1. **Header band** (`header.hero`, 0–420px): padding 72px 0 40px; background #f7f9fc with `radial-gradient(circle, rgba(31,125,217,0.08) 1px, transparent 1.4px)` at `background-size: 15px 15px`; 1px #dfe7f1 bottom border. No navigation bar.
2. **Venue pill** (`span.venue`, y=72, 103×30): 12.5px/700 uppercase, letter-spacing 0.08em, white on #1f7dd9, padding 5px 14px, 999px radius. Gap 22px.
3. **Title** (`h1`, y=124, 99px, two lines): Iowan Old Style / Palatino Linotype 42px/500, line-height 1.18, #101e33, max 920px. Gap 26px.
4. **Authors** (`p.authors`, y=249): 17px #101e33; names linked with a 1px dotted #6b7c93 bottom border; superscripts .65em #0f4e8c; "✉" in #e1662e; separators " · ". Gap 6px.
5. **Affiliations** (`p.affiliations`, y=282): 14px #6b7c93 with #0f4e8c superscripts. Gap 30px.
6. **Buttons** (`.links`, y=335, 43px, 12px gaps): 14.5px/600, padding 9px 18px, 8px radius, 7px gap to a 15px emoji icon; "📄 Paper (PDF)" #1f7dd9 fill and border with white text; "📚 arXiv", "💻 Code", "❉ BibTeX" white with a 1px #dfe7f1 border and #101e33 text. Header ends at y=420.
7. **Teaser** (`section.teaser`, from y=428 after main's 8px padding; padding-top 40px): figure image at y=468, 872×172, white, 1px #dfe7f1 border, 10px radius; caption 14px/1.5 #6b7c93 centred 14px below, lead phrase bold #3c4c63.
8. **Abstract** (`section.abstract`, from y=716): label at y=768; paragraph 17px/1.6 #3c4c63 at y=809, continuing below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #f7f9fc | --paper | body and header background |
| Panel | #ffffff | --panel | outline buttons, teaser frame, figure panels, table wrapper |
| Ink | #101e33 | --ink | title, authors, outline button text, table method names, bold contribution phrases |
| Ink Soft | #3c4c63 | --ink-soft | body paragraphs, contributions, legend items, table cells |
| Ink Faint | #6b7c93 | --ink-faint | affiliations, captions, table header text, acknowledgement, contact line, author link underline |
| Line | #dfe7f1 | --line | header rule, section rules, button borders, figure and table borders, caption rules, empty dots |
| Blue | #1f7dd9 | --blue | venue pill, primary button, contribution square bullets, legend arrows, outline button hover border |
| Deep Blue | #0f4e8c | --blue-deep | section labels, superscripts, table group headers, Ours row text, links, primary hover |
| Blue Tint | #eaf2fc | --blue-tint | Ours table row, outline button hover fill |
| Warm Orange | #e1662e | --warm | corresponding-author ✉, full requirement dots, link hover |
| Half Dot | #e8a98a | (literal) | half requirement dots in the table |
| Navy Slab | #0f1b2c | (literal) | BibTeX band background |
| Code Ice | #cfe0f5 | (literal) | BibTeX text and Copy button text |
| Dot Grid | rgba(31,125,217,0.08) | (literal) | 1px dots on the header band |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display serif | 'Iowan Old Style', Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif | no web font; Palatino Linotype on Windows, Iowan Old Style on macOS | Source Serif 4 |
| Body | -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif | no web font; Arial on Windows (Helvetica substitution), SF Pro on macOS | Inter |
| Mono | ui-monospace, 'SF Mono', Menlo, Consolas, monospace | Consolas on Windows | JetBrains Mono |

| Role | Selector | Size / weight / line-height / tracking | Color |
|---|---|---|---|
| Title | `h1` | clamp(28px, 4.2vw, 42px) → 42px / 500 / 1.18 | #101e33 |
| Section label | `section > .wrap > h2` | 13px / 700 / uppercase / 0.1em | #0f4e8c |
| Body | `body` | 16px / 400 / 1.6 | #3c4c63 |
| Abstract | `.abstract p` | 17px / 1.6 | #3c4c63 |
| Venue pill | `.venue` | 12.5px / 700 / uppercase / 0.08em | #ffffff |
| Authors | `.authors` | 17px | #101e33 |
| Affiliations | `.affiliations` | 14px | #6b7c93 |
| Button | `.btn` | 14.5px / 600 | white or #101e33 |
| Contribution | `ul.contrib li` | 16px / 1.5; `b` 700 #101e33 | #3c4c63 |
| Legend item | `ul.legend li` | 14.5px, → arrow in 700 #1f7dd9 | #3c4c63 |
| Caption | `.teaser figcaption`, `.figure-panel figcaption` | 14px / 1.5–1.55 | #6b7c93, lead in bold #3c4c63 |
| Table | `table` | 13.5px; cells monospace; method names 600 sans | #3c4c63 / #101e33 |
| Table header | `thead th` | 11px / 700 / uppercase / 0.02em; group row 10.5px | #6b7c93; group #0f4e8c |
| BibTeX | `.bibtex pre` | mono 12.8px / 1.6 | #cfe0f5 |
| Acknowledgement | `.ack`, `.contact` | 13px / 1.6 (contact in mono) | #6b7c93 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / effect |
|---|---|---|---|
| Venue pill | 999px | none | solid #1f7dd9 |
| Buttons | 8px | 1px #1f7dd9 (primary) or #dfe7f1 | hover border #1f7dd9, text #0f4e8c, fill #eaf2fc |
| Teaser image, figure panels, table wrapper | 10px | 1px #dfe7f1 | none |
| Figure panel images | 4px | none | none |
| Contribution bullets | 2px, 8×8px | none | solid #1f7dd9 |
| BibTeX band | 10px | none | #0f1b2c fill |
| Copy button | 6px | 1px rgba(255,255,255,0.15) | rgba(255,255,255,0.08) fill, hover 0.16 |
| Header band | 0 | 1px #dfe7f1 bottom | dot grid |

## Layout Metrics

- **Container**: `.wrap { max-width: 920px; margin: 0 auto; padding: 0 24px }` → content x 284–1156 (872px) at 1440.
- **Header**: padding 72px 0 40px; vertical chain 30 (pill) + 22 + 99 (title) + 26 + 27 (authors) + 6 + 23 + 30 + 43 (buttons) = 306px from y=72 to y=378, then 40px padding and the 1px rule.
- **Main**: padding 8px 0 20px; teaser section padding 40px 0 0 with no rule; every other section padding 52px 0 with a 1px #dfe7f1 bottom rule; label margin-bottom 20px.
- **Contributions**: flex column, gap 12px; bullets 22px left padding.
- **Figure panels**: padding 20px, margin 18px 0; caption 14px below the image with 14px top padding over a 1px #dfe7f1 rule; legend grid auto-fit minmax(200px, 1fr), gaps 8px 20px.
- **Table**: wrapper 1px #dfe7f1, 10px radius, white, horizontal scroll; min-width 640px; cells padding 9px 10px; group header row padding-bottom 2px; rule rows add a 1px #dfe7f1 top border; Ours row #eaf2fc.
- **BibTeX band**: the section itself takes the `.bibtex` class, so it renders as a full-width #0f1b2c band (1440px, y 4272–4516) with 10px corners and padding 20px 22px, holding an inner 872px block; Copy button at top/right 12px.
- **Footer**: padding 40px 0 60px, centred; acknowledgement max 720px, 18px above the mono contact line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| base (1440) | 24px inside 920px (content x 284–1156) | 16px | 42px | none |
| ≤1000px | 24px | 16px | 4.2vw, e.g. 37.8px at 900 | none |
| ≤667px | 24px | 16px | 28px floor | none |
| ≤640px | 24px | 16px | 28px | header padding 48px 0 32px; sections 38px; table scrolls horizontally below 640px wide content |

## Components

- **Venue pill** (`.venue`): inline-block, #1f7dd9 fill, white 12.5px/700 uppercase with 0.08em tracking, padding 5px 14px, 999px radius, 22px above the title.
- **Primary button** (`.btn.primary`): padding 9px 18px, 8px radius, #1f7dd9 fill and border, white 14.5px/600, emoji icon at 15px with 7px gap; hover #0f4e8c.
- **Outline button** (`.btn`): white, 1px #dfe7f1, #101e33 text; hover #1f7dd9 border, #0f4e8c text, #eaf2fc fill. A disabled variant uses #6b7c93 text and a 10px uppercase "soon" pill.
- **Section label**: 13px/700 uppercase, 0.1em tracking, #0f4e8c, sans-serif, 20px above content; no large section headings anywhere.
- **Square-bullet contribution list** (`ul.contrib`): 8×8px #1f7dd9 squares with 2px radius at 0.5em, 22px indent, 12px gaps, bold lead phrase in #101e33.
- **Figure panel** (`.figure-panel`): white, 1px #dfe7f1, 10px radius, padding 20px; image with 4px radius; caption separated by a 1px #dfe7f1 rule; optional legend of "→" items with blue arrows.
- **Results table**: white rounded wrapper; first header row of group labels (COUNTING, IMAGE RECON., PROTOTYPE) in 10.5px/700 #0f4e8c, second row 11px/700 uppercase #6b7c93 over a 1px rule; method names 600 sans #101e33, numbers in monospace #3c4c63; requirement dots 9px (full #e1662e, half #e8a98a, none #dfe7f1); Ours row #eaf2fc with 700 #0f4e8c text; a 12.5px #6b7c93 note below.
- **BibTeX band**: #0f1b2c, 10px radius, padding 20px 22px; label in the same #0f4e8c (low contrast on navy); pre mono 12.8px/1.6 #cfe0f5; Copy button 12px/600 #cfe0f5 on rgba(255,255,255,0.08), 1px rgba(255,255,255,0.15), 6px radius, padding 6px 10px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation bar | absent from the source | the dot-grid header band starts the page |
| Venue badge | yes | filled blue pill |
| Title / authors / affiliations | yes | centred serif title, dotted-underlined authors, gray affiliations |
| Link buttons | yes | 8px-radius buttons with emoji icons, one filled blue |
| Teaser | yes | wide pipeline figure in a white rounded frame with caption |
| Abstract | yes | 17px paragraph under an uppercase label |
| Contributions | yes | blue square-bullet list |
| Method figure | yes | white panel with ruled caption and arrow legend |
| Results table | yes | monospace table with grouped headers, dot markers and a tinted Ours row |
| Qualitative figures | yes | two white panels |
| Conclusion | yes | short paragraph with bold phrase |
| BibTeX | yes | full-width navy band with rounded corners |
| Footer | yes | centred acknowledgement and mono contact line |

## Adapting to Other Content

- **More authors**: keep the single centred 17px line with " · " separators and let it wrap; give each affiliation a #0f4e8c superscript and keep the 14px #6b7c93 line.
- **A second results table**: reuse the wrapper (white, 1px #dfe7f1, 10px radius) at the 872px content width, with grouped 10.5px #0f4e8c headers, monospace cells and the #eaf2fc Ours row; mark best values in 700 #0f4e8c rather than color fills.
- **Long publication or news lists**: use the contribution-list pattern (8px blue squares, 12px gaps) with a 13px mono #6b7c93 date before each item.
- **Videos**: put each in a figure panel (white, 10px radius, 20px padding) with a ruled 14px caption.
- **More sections**: add another 52px-padded section with a 13px uppercase #0f4e8c label and a 1px #dfe7f1 rule; do not introduce larger section headings.

## Do's and Don'ts

- Do keep section headings as small uppercase blue labels; the serif appears only in the title.
- Do frame every figure and table in white on the pale paper with 1px #dfe7f1 borders and 10px radii.
- Do reserve orange #e1662e for small marks (corresponding author, requirement dots, link hover).
- Do keep the dot grid confined to the header band.
- Don't add shadows; separation comes from hairlines and the paper/white contrast.
- Don't load web fonts; the look depends on system Palatino/Iowan and Helvetica/Arial.
- Don't use the navy slab for anything but the BibTeX block.

## Surfaces

Cool paper #f7f9fc with a dotted header band; white #ffffff panels, frames and table wrapper; #eaf2fc for the Ours row; one full-width navy #0f1b2c band for the citation.

## Imagery

Photographs of repeated objects (apples, pills, figurines, watches, strawberries, flowers) arranged in comparison grids, a pipeline teaser showing prototype, position, appearance and color stages with dashed grouping, and a schematic architecture figure in gray, green and white boxes.

## Layout

A centred hero followed by a narrow 872px reading column; sections stack with 52px padding and hairline separators, and figures and the table run at full column width. The page is short and even in rhythm, with no side-by-side layouts.

## Agent Prompt Guide

Quick colors: paper #f7f9fc, panel #ffffff, ink #101e33, body #3c4c63, faint #6b7c93, line #dfe7f1, blue #1f7dd9, deep blue #0f4e8c, tint #eaf2fc, orange #e1662e, navy #0f1b2c.

1. "Build a centred header band: background #f7f9fc with radial-gradient(circle, rgba(31,125,217,0.08) 1px, transparent 1.4px) at 15px 15px, padding 72px 0 40px, 1px #dfe7f1 bottom border. Inside a 920px wrap: a #1f7dd9 pill (white 12.5px/700 uppercase, 0.08em, padding 5px 14px), a 42px/500 Palatino-style serif title in #101e33 (line-height 1.18), 17px authors with dotted #6b7c93 underlines and #0f4e8c superscripts, 14px #6b7c93 affiliations, and 8px-radius buttons (padding 9px 18px, 14.5px/600): one #1f7dd9 filled, others white with 1px #dfe7f1."
2. "Make sections: padding 52px 0, 1px #dfe7f1 bottom rule, a 13px/700 uppercase label in #0f4e8c with 0.1em tracking and 20px margin below; body 17px #3c4c63. Contributions as a list with 8×8px #1f7dd9 squares (2px radius), 22px indent and 12px gaps."
3. "Create a results table: white wrapper with 1px #dfe7f1 and 10px radius; group header row 10.5px/700 uppercase #0f4e8c, column header row 11px/700 uppercase #6b7c93 with a 1px #dfe7f1 bottom rule; cells padding 9px 10px in monospace 13.5px #3c4c63; method names 600 #101e33; the Ours row background #eaf2fc with 700 #0f4e8c text."

## Similar Pages

- Minimal academic pages from vision labs that use a serif title over a sans body and small uppercase section labels.
- Analysis-by-synthesis and inverse-graphics papers with one comparison table and figure panels.

## Quick Start

```css
:root {
  --paper: #f7f9fc;
  --panel: #ffffff;
  --ink: #101e33;
  --ink-soft: #3c4c63;
  --ink-faint: #6b7c93;
  --line: #dfe7f1;
  --blue: #1f7dd9;
  --blue-deep: #0f4e8c;
  --blue-tint: #eaf2fc;
  --warm: #e1662e;
  --navy: #0f1b2c;
  --font-display: 'Iowan Old Style', Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  --font-body: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  --max-w: 920px;
}
```

## Provenance

- **URL**: https://vayvi.github.io/repeated-elements/
- **Paper**: Bottom-up Modeling of Repeated Elements via Single Image Analysis-by-Synthesis (arXiv 2609.07939), Syrine Kalleli, Alexei A. Efros, Mathieu Aubry (LIGM / ENPC, UC Berkeley).
- **Venue**: ECCV 2026.
- **Selection reason**: the arXiv comment states acceptance at ECCV 2026 and links this project page.
- **Template credit**: none stated; a small hand-written page with one `style.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), targeted probes of hero, contributions, figure panels, results table, BibTeX band and footer, the 1440×900 shot and a full-page capture, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
