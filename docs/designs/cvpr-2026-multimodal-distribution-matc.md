# MDM — Style Reference

> A clean seminar handout ruled in indigo ink: violet frames, a lilac band and one bold TL;DR stamp.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the navigation, hero, TL;DR, figure frames, section titles and citation), the 1440×900 and full-page screenshots, and the page's own `style.css` read directly. The root font size is 14.5px, so every rem value is 14.5px-based. Wanted Sans Variable (weights 400–1000) loads from jsDelivr and renders everywhere except the BibTeX block.

## Overview

A hand-built single page in Tailwind-like slate and indigo tokens. A sticky white bar (95% white, 10px blur) centres four section links in muted slate, with the current one in indigo #6366f1 bold. The hero is centred on white: a two-line 43.5px Wanted Sans bold title in slate-ink #0f172a, "CVPR 2026" in 26px indigo #4f46e5, a small indigo "Also presented at DataMFM Workshop" line, four 18px author names in #334155 with symbol superscripts, an 11.6px grey affiliation line, and five white outlined pill buttons with Font Awesome icons. A wide TL;DR box follows: lilac #f5f3ff fill, 2px #6366f1 border, 12px radius, a solid indigo "TL;DR" tag on the left and an 18px/500 centred sentence with italic phrases. The overview figure sits in a thin indigo-outlined white frame (7px radius, 3.6px padding) with a small centred caption. The Abstract is a full-width lilac band; later sections are white, separated by 1px #e2e8f0 rules, with left-aligned 36px indigo section titles underlined by a 2px grey rule. Figures, a demo video and result images all share the indigo-outlined frame. A lilac BibTeX block and a small footer close the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 72.1% plus #fdfffe 2.5%, #fffffd 0.3%; lilac #f5f3fe 8.2% and #faf9fc 2.4% (TL;DR fill); light grey #e0dfe3 6.6% (button borders, figure pastels); slate-violet #898ca2 5.1% (text, TL;DR border and indigo accents); #f0f3f2 2.9% (overview figure background).

Anatomy in DOM order (desktop 1440px; hero container max-width 64rem = 928px at x=256; TL;DR 1044px at x=198):

1. **Navigation** (`.sidebar`, 0–67px, sticky): rgba(255,255,255,0.95), blur 10px, 1px #e2e8f0 bottom rule, shadow 0 1px 2px rgba(0,0,0,0.05), padding 14.5px, links 21.75px apart, centred from x=552. Labels 13.775px/600 #64748b; active "Overview" 700 #6366f1.
2. **Title** (`h1.hero-title`, y=125, two lines, 109px): Wanted Sans 43.5px/700 (3rem at ≥768px), line-height 1.25, #0f172a, centred, manual line break. Gap 26px.
3. **Venue** (`p.hero-status`, y=248): "CVPR 2026", 26.1px/600, #4f46e5, centred. Gap 22px.
4. **Workshop line** (`p.hero-status`, y=312): 14.5px/600 #4f46e5, "DataMFM Workshop" as a link. Gap 28px.
5. **Authors** (`.hero-authors`, y=364): 18.125px/500 #334155, flex-wrap with 21.75px column gaps; superscripts * and †. Gap 26px.
6. **Affiliation and notes** (`.hero-affiliations`, y=411): 11.6px #64748b (inline `font-size: 0.8rem` overrides the stylesheet's 1rem), three items 7.25px apart. Gap 15px.
7. **Buttons** (`.hero-buttons`, y=447, 40px tall, 14.5px gaps): Paper, Slides, Poster, Code, BibTeX; white outlined pills. Gap 43px.
8. **TL;DR box** (`.tldr-box`, y=530–680, 1044px): #f5f3ff, 2px #6366f1, 12px radius, padding 29px; inner flex row with the "TL;DR" tag (16.3px/700 white on #6366f1, 7.25px radius, padding 3.6px 14.5px) and an 18.125px/500 #1e293b centred sentence with three italic phrases. Gap 29px.
9. **Overview figure** (`.analysis-image-container`, y=709, 993×509): white, 1px #6366f1, 7.25px radius, 3.6px padding; image radius 3.6px. Its top 191px shows above the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Ink | #0f172a | (literal) | hero title, headings |
| Body Slate | #1e293b | --color-text-main | body text, TL;DR text, button labels, captions |
| Author Slate | #334155 | (literal) | author names |
| Muted Slate | #64748b | --color-text-muted | nav labels, affiliation line, citation text |
| Light Slate | #94a3b8 | --color-text-light | footer text |
| Indigo | #6366f1 | --color-primary | TL;DR border and tag, active nav label, figure frame borders, carousel controls |
| Deep Indigo | #4f46e5 | --color-primary-dark | venue line, workshop line, section titles, highlighted table rows |
| Soft Indigo | #818cf8 | --color-primary-light | qualitative overlay titles |
| Lilac | #f5f3ff | --color-bg-alt | TL;DR fill, Abstract band, BibTeX block, carousel button fill |
| Hairline | #e2e8f0 | --color-border | nav bottom rule, section top rules, section-title underline, citation border |
| Button Edge | #cbd5e1 | (literal) | outlined button borders, carousel dots |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Wanted Sans Variable', 'Wanted Sans', -apple-system, Segoe UI, Roboto, Arial, sans-serif | Wanted Sans Variable 400–1000 | Pretendard |
| Mono | monospace | Consolas | JetBrains Mono |
| Icons / math | Font Awesome 6.4; MathJax 3 | Font Awesome 6 Free/Brands; MJXTEX fonts | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Root | `html` | 14.5px | — |
| Title | `.hero-title` | 3rem = 43.5px / 700 / 1.25 | #0f172a |
| Venue | `.hero-status` | 1.8rem (inline) = 26.1px / 600 | #4f46e5 |
| Workshop line | `.hero-status` | 1rem = 14.5px / 600 | #4f46e5 |
| Authors | `.hero-authors` | 1.25rem = 18.125px / 500 | #334155 |
| Affiliation and notes | `.hero-affiliations` (inline 0.8rem) | 11.6px / 400 | #64748b |
| Nav label | `.sidebar-label` | 0.95rem = 13.775px / 600 (active 700) | #64748b (active #6366f1) |
| Button | `.btn` | 14.5px / 500 | #1e293b |
| TL;DR tag | `.tldr-label` | 1.125rem = 16.3px / 700 | #ffffff |
| TL;DR text | `.tldr-text` | 1.25rem = 18.125px / 500 / 1.625 | #1e293b |
| Section title | `.section-title` | 2.5rem = 36.25px / 700 / 1.2, left | #4f46e5 |
| Body / abstract | `p`, `.abstract-text` | 1.25rem = 18.125px / 400 / 1.625 | #1e293b |
| Figure caption | `.table-caption` | 0.85rem = 12.3px / 400 / 1.4, centred | #1e293b |
| BibTeX | `.citation-code` | 14.5px monospace / 1.625 | #64748b |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Outlined buttons | 9999px | 1px #cbd5e1 | none |
| TL;DR box | 12px | 2px #6366f1 | none |
| TL;DR tag | 7.25px | none | none |
| Figure frame | 7.25px (image 3.6px) | 1px #6366f1 | none |
| Section title | 0 | 2px #e2e8f0 bottom | none |
| Sections | 0 | 1px #e2e8f0 top | none |
| Navigation | 0 | 1px #e2e8f0 bottom | 0 1px 2px rgba(0,0,0,0.05) |
| Carousel buttons | 50% (36px) | 1px #6366f1 | none |
| Citation block | 3.6px | 1px #e2e8f0 | none |

## Layout Metrics

- **Container**: `.container { max-width: 68rem (986px); margin: 0 auto; padding: 0 1rem }`, content 957px at x=242.
- **Hero**: `padding-top: 4rem` (58px) under the nav; inner `.hero-container` max-width 64rem (928px); title max-width 24em; authors max-width 56rem.
- **TL;DR**: max-width 72rem (1044px), padding 2rem (29px); figure container `.teaser-container` up to 1800px wide with the frame fitting the image (993px).
- **Sections**: `.section { padding: 3rem 0; border-top: 1px solid #e2e8f0 }` (43.5px); section title margin-bottom 2rem with 1rem padding under the text; results blocks 6rem apart; citation section padding 8rem 0.
- **Method**: figure floats right at 640px (max 55%) with 21.75px left margin; text wraps on the left.
- **Grids**: compute-efficiency 2 columns with 29px gap; chart grids 2 or 3 columns from 768px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1015px | (100% − 957px)/2 | 18.125px | 43.5px | TL;DR row layout; method figure floats right |
| 768–1014px | 14.5px | 18.125px | 43.5px | ablation grid wraps below 1024px |
| <768px | 14.5px | 14.5px (`p` 1rem) | 2.25rem = 32.6px | TL;DR stacks the tag above the text; compute and chart grids go to one column; captions 0.875rem |
| ≤640px | 14.5px; nav left-aligned with 21.75px side padding | 14.5px | 32.6px | nav links scroll horizontally |

## Components

- **Sticky text nav** (`.sidebar`): centred row of `.sidebar-item` links (padding 7.25px), labels 13.775px/600 #64748b; hover and active turn #6366f1 and 700.
- **Outlined pill button** (`.btn.btn-outline`): white, 1px #cbd5e1, 9999px radius, padding 7.25px 18.125px, 14.5px/500 #1e293b, Font Awesome icon left with a 7.25px gap; hover fill #f5f3ff.
- **TL;DR callout** (`.tldr-box`): #f5f3ff, 2px solid #6366f1, 12px radius, padding 29px; flex row (column on phones) with a solid indigo tag and a centred 18.125px/500 sentence using italics for key phrases.
- **Indigo figure frame** (`.analysis-image-container`): white, 1px #6366f1, 7.25px radius, 3.6px padding, fit-content width; image 3.6px radius, max-height 500px; caption 12.3px #1e293b centred 7.25px below with a bold "Figure:" lead-in.
- **Section title** (`.section-title`): left-aligned 36.25px/700 #4f46e5, fit-content width, 14.5px padding-bottom and a 2px #e2e8f0 underline, 29px margin below.
- **Lilac band** (`.section.alt-bg`): full-width #f5f3ff with a 1px #e2e8f0 top rule.
- **Carousel controls**: 36px circles in #f5f3ff with a 1px #6366f1 border and indigo icon, inverted on hover; dots #cbd5e1, active an indigo 17px pill.
- **Citation block**: #f5f3ff, 1px #e2e8f0, 3.6px radius, padding 14.5px, monospace #64748b, with a copy button that appears on hover.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky navigation | yes | four centred text links with indigo active state |
| Title / venue / workshop | yes | centred bold title, indigo venue and workshop lines |
| Authors / affiliation | yes | slate names, small grey notes line |
| Link buttons | yes | five white outlined pills |
| TL;DR | yes | lilac box with indigo border and tag |
| Overview figure | yes | indigo-outlined frame with caption |
| Abstract | yes | lilac full-width band |
| Method | yes | text wrapped around a right-floated framed figure, plus a framed demo video |
| Results tables | present but non-standard | retrieval and generalization tables are framed images; `.results-table` styles exist but are unused |
| Compute efficiency | yes | two-column chart grid |
| Qualitative results | yes | image grids |
| BibTeX | yes | lilac monospace block with copy button |
| Footer | yes | white with a top hairline, 12.7px #94a3b8 |

## Adapting to Other Content

- **A real results table**: use the stylesheet's own `.results-table`: 11.6px, centred cells with 1px #f1f5f9 rules, header 600 with a 1px #1e293b rule, our-method rows #eef2ff with #4f46e5 text, wrapped in the indigo figure frame.
- **More authors and affiliations**: authors wrap within 56rem at 21.75px gaps; put numbered affiliations on the `.hero-affiliations` line at 11.6px #64748b.
- **More link buttons**: add outlined pills; reserve a filled dark pill (`.btn`, #1e293b) only if one link must stand out.
- **Long publication or news lists**: left-aligned 18.125px lines under an indigo `.section-title`, dates in #4f46e5 600, separated by 1px #e2e8f0 rules.
- **Alternating sections**: alternate white and `.alt-bg` lilac bands; keep at most one lilac band per two sections.

## Do's and Don'ts

- Do keep indigo (#6366f1 / #4f46e5) the only accent, used for frames, titles, venue and the TL;DR.
- Do frame every figure in the thin indigo outline with 3.6px inner padding.
- Do set everything in Wanted Sans, with weight (500–700) carrying hierarchy.
- Don't fill buttons with colour; they are white pills with a #cbd5e1 hairline.
- Don't centre section titles; only the hero is centred.
- Don't forget the 14.5px root size when converting rem values.

## Surfaces

White page and hero; one lilac (#f5f3ff) TL;DR box, Abstract band and BibTeX block; white indigo-outlined figure frames; a frosted white sticky nav.

## Imagery

A pastel method overview (k-means clustered thumbnails, a unit hypersphere diagram, encoder blocks), a demo video of image grids, result tables rendered as images, line charts for compute efficiency, and qualitative image–caption grids.

## Layout

Sticky nav; centred hero with TL;DR and overview figure; Abstract band; Proposed Method; Retrieval Results; Cross-Architecture Generalization; Compute Efficiency; Qualitative Results; Citation; footer. About 7,660px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: ink #0f172a, text #1e293b, authors #334155, muted #64748b, indigo #6366f1, deep indigo #4f46e5, lilac #f5f3ff, hairline #e2e8f0, button edge #cbd5e1.

1. "Create a TL;DR callout: max-width 1044px, centred, background #f5f3ff, 2px solid #6366f1, 12px radius, padding 29px; a flex row with a tag 'TL;DR' (Wanted Sans 16.3px/700 white on #6366f1, 7.25px radius, padding 3.6px 14.5px) and a centred sentence 18.125px/500 #1e293b, line-height 1.625, italic key phrases."
2. "Build outlined pill buttons: white, 1px solid #cbd5e1, 9999px radius, padding 7.25px 18.125px, Wanted Sans 14.5px/500 #1e293b, Font Awesome icon left with 7.25px gap, 14.5px between buttons; hover background #f5f3ff."
3. "Frame figures: wrapper fit-content, white, 1px solid #6366f1, 7.25px radius, 3.6px padding; image 3.6px radius; caption 12.3px #1e293b centred 7.25px below. Section titles above them are left-aligned 36.25px/700 #4f46e5 with a 2px #e2e8f0 underline and 14.5px padding-bottom."

## Similar Pages

- Hand-built Tailwind-style project pages with a single indigo accent and a TL;DR box.
- Dataset distillation and vision-language pages that present tables as framed images.

## Quick Start

```css
:root {
  --font-primary: 'Wanted Sans Variable', 'Wanted Sans', -apple-system, 'Segoe UI', Roboto, Arial, sans-serif;
  --color-primary: #6366f1;
  --color-primary-dark: #4f46e5;
  --color-bg: #ffffff;
  --color-bg-alt: #f5f3ff;
  --color-text-main: #1e293b;
  --color-text-muted: #64748b;
  --color-text-light: #94a3b8;
  --color-border: #e2e8f0;
  --container-width: 68rem;
}
html { font-size: 14.5px; }
body { font-family: var(--font-primary); color: var(--color-text-main); background: var(--color-bg); line-height: 1.6; }
.container { max-width: var(--container-width); margin: 0 auto; padding: 0 1rem; }
```

## Provenance

- **URL**: https://andyj1.github.io/mdm/
- **Paper**: Multimodal Distribution Matching for Vision-Language Dataset Distillation (arXiv 2605.23482), Jongoh Jeong, Hoyong Kwon, Minseok Kim, Kuk-Jin Yoon.
- **Venue**: CVPR 2026 (also presented at the DataMFM workshop).
- **Selection reason**: the arXiv comment states acceptance for publication at CVPR 2026 and links this page.
- **Template credit**: none credited; a custom `style.css` (variable names such as `--color-cat3d` and `.img-comp-badge.cameo` show it was adapted from the authors' earlier project page).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and components, the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
