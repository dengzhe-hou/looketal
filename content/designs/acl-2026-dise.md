# Aurora Card Stack — Style Reference

> A tidy stack of rounded cards washed in a blue-violet-apricot dawn, signed with a gradient wordmark.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the wordmark, title, venue line, authors, arXiv button, cards, figures, BibTeX and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `style.css` on top of Bootstrap 5.3.0-alpha3, with its HTML. Positions are document coordinates at 1440px wide.

## Overview

DiSE is a Bootstrap 5 page with a small custom stylesheet and one recurring gradient: 107.54° from Microsoft-ish blue (#0078d4) through violet (#8661c5) to apricot (#ff9349). It appears as the "DiSE" wordmark's text fill, the arXiv pill, a 5px bar under section titles and the footer band, and in a pale form (#e6eff7 → #eeebf5 → #fcf4ee) as the fill of the Abstract and Motivation cards. The header is centered on white between thin grey rules: a 67.2px gradient wordmark, a 48px heavy serif title, a bold grey "ACL 2026 Main" line, bold author names with superscripts, grey affiliations and notes, and a single gradient "arXiv" pill. Content lives in 16px-radius Bootstrap cards stacked down a 1320px container: tinted cards with centered 32px titles, and white cards with left-aligned titles over the gradient bar, display-math blocks on #f8f8fb, softly shadowed figures, and three tinted metric cards.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 58.9%, pale lavender #ededf5 13.6% (middle of the Abstract card's tint), light grey #e2e4e2 10.1% (figure panels and rules), mid grey #918f95 5.9% (text anti-aliasing), warm white #f8f5f4 5.6% (apricot end of the card tint), pale blue #edf0f5 3.8% (blue end of the card tint), remainder under 2%. The strongest color is the violet arXiv pill and the gradient wordmark.

Anatomy in DOM order (y = top of element box, container x 60–1380):

1. **Top rule**: a Bootstrap `hr` (1px top border in #212529 at 25% opacity, 16px margins) at y 16 across the container. Gap about 30px.
2. **Wordmark** (`.hero-mark.x-gradient-font`), "DiSE", declared Playfair Display, rendered Georgia 67.2px/800, line-height 1, text filled with `linear-gradient(107.54deg, #0078d4 0.3%, #8661c5 40.23%, #ff9349 100%)`, centered. Gap 8px.
3. **Title** (`h1.title-font`), y 122, two lines, rendered Georgia 48px/600, line-height 57.6px, #000000 (`text-body-emphasis`), centered. Gap 16px.
4. **Venue line** (`p.venue-line`), y 253, "ACL 2026 Main", Avenir Next Cyr 19.2px/700, #555555. Then a second 1px rule at about y 302.
5. **Authors** (`.author .author-name`), y 326 and 363, two centered rows, Avenir Next Cyr 18px/700 #333333, inline-blocks with 16px side margins, superscripts at 0.8em. Gap about 25px.
6. **Affiliations** (`.organization`), 16.2px #666666, superscripted numbers; **footnote** (`.footnote`) 14.4px #888888. Gap about 20px.
7. **arXiv pill** (`#links a`), y 508, 115×35, white Avenir Next Cyr 16px/500, gradient fill, radius 50px, shadow 0 0 4px rgba(0,0,0,0.5), icomoon icon left. Gap about 45px.
8. **Abstract card** (`.card > .card-body.x-gradient-block`), starting at about y 588, 16px radius, pale tri-tone gradient fill, padding 32px; centered "Abstract" 32px/800 #3f3f3f (y 621), then 16.48px #3f3f3f text and a figure at 92% width with a soft shadow.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Gradient Blue | #0078d4 | `.x-gradient-font`, `#links a`, `.body-hr`, `.footer` start | Wordmark fill, arXiv pill, title bar, footer band |
| Gradient Violet | #8661c5 | same gradients, middle stop | Same elements |
| Gradient Apricot | #ff9349 | same gradients, end stop; `a.link:hover` | Same elements; link hover |
| Tint Blue | #e6eff7 | `.x-gradient-block` start | Abstract and Motivation card fill |
| Tint Lavender | #eeebf5 | `.x-gradient-block` middle | Same cards |
| Tint Apricot | #fcf4ee | `.x-gradient-block` end | Same cards |
| Card Ink | #3f3f3f | `.x-gradient-block` | Text and titles in tinted cards |
| Body Ink | #212529 | Bootstrap `body` | Text and titles in white cards |
| Title Black | #000000 | `.text-body-emphasis` | Paper title |
| Venue Grey | #555555 | `.venue-line`, `.figure-caption` | Venue line, figure captions |
| Author Ink | #333333 | `.author-name a` | Author names (hover #007bff) |
| Affiliation Grey | #666666 | `.organization` | Affiliations |
| Note Grey | #888888 | `.footnote` | Equal-contribution and corresponding notes |
| Link Violet | #6567c9 | `a` | Inline links |
| Math Fill | #f8f8fb | `.equation-block` | Display-math blocks |
| Metric Border | #e4e6f0 | `.metric-card` | Metric card border (fill #f2f7fc → #f5f2fb → #fff6f0) |
| Metric Ink | #423f94 | `.metric` | Metric card headline |
| Metric Text | #4a4a4a | `.metric-card p` | Metric card body text |
| Header Rule | #e5e5e5 | `.footer` border, `.blog-header` | Footer top border |
| Code Pink | #d63384 | Bootstrap `code` | BibTeX text |
| Button Blue | #0d6efd | Bootstrap `.btn-primary` | "Copy BibTeX" button |
| White | #ffffff | `body`, `.card`, `.figure-img` | Page, white cards, figure backgrounds, pill and footer text |

## Tokens — Typography

- **Body and UI**: declared on `*` as `'Avenir', 'Avenir Next Cyr', 'Config', 'Microsoft YaHei', 'Times New Roman'`, with Avenir Next Cyr self-hosted (`fonts/avenir-next`). Rendered here: Avenir Next Cyr 400, 500, 700, 900 (`fonts_loaded`); on macOS the system Avenir is picked first. Substitute: Nunito Sans (similar geometric humanist width).
- **Title and wordmark**: declared `"Playfair Display", Georgia, "Times New Roman", serif`, but no Playfair face is loaded, so both render in Georgia (bold for the 600 and 800 weights). Substitute if you want the intended look: Playfair Display 600/800 from Google Fonts.
- **Math**: KaTeX 0.16.7 (KaTeX_Main, KaTeX_Math loaded). **Icons**: icomoon for the arXiv glyph, Bootstrap Icons loaded.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Wordmark | `.hero-mark` | 67.2px (4.2rem) / 1 | 800 (Georgia bold) | gradient fill |
| Paper title | `.title-font` | 48px (3rem) / 57.6px | 600 (Georgia bold) | #000000 |
| Card title | `.card-title` | 32px / 38.4px | 800 | #3f3f3f (tinted) / #212529 (white) |
| Subheading | `h4` in cards | 24px | 500 | #212529 |
| Venue line | `.venue-line` | 19.2px (1.2rem) | 700 | #555555 |
| Authors | `.author-name a` | 18px | 700 | #333333 |
| Card text | `.card-text` | 16.48px (1.03rem) / 24.7px | 400 | #3f3f3f / #212529 |
| Metric headline | `.metric` | 16.32px (1.02rem) | 800 | #423f94 |
| Affiliations | `.organization` | 16.2px (0.9em) | 400 | #666666 |
| Pill button | `#links a` | 16px | 500 | #ffffff |
| Caption | `.figure-caption` | 15.04px (0.94rem) | 400 | #555555 |
| Footer | `.footer-title`, `.footer-text` | 15px | 800 | rgba(255,255,255,0.9) / 0.7 |
| Footnote | `.footnote` | 14.4px (0.8em) | 400 | #888888 |
| BibTeX | `code` | 14.42px / 21.6px | 400 | #d63384 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Cards (`.card`, `.x-gradient-block`) | 16px | Bootstrap 1px rgba(0,0,0,0.175) | none |
| arXiv pill (`#links a`) | 50px | none | 0 0 4px rgba(0,0,0,0.5); hover 0 0 6px rgba(0,0,0,0.75) |
| Figure image (`.figure-img.rounded`) | 6px | none | 0 6px 18px rgba(0,0,0,0.1) |
| Metric card | 14px | 1px solid #e4e6f0 | none |
| Equation block | 12px | none | none |
| Title bar (`hr.body-hr`) | 0 | none; a 5px gradient bar | none |
| Copy BibTeX button | 6px | 1px #0d6efd | none |

## Layout Metrics

- **Container**: Bootstrap 5 `.container`, 1320px at ≥1400px (x 60–1380) with 12px padding; card body padding 32px, so card text runs x 105–1335 (1230px).
- **Header**: `.hero` padding 12px 0 4px; wordmark 8px above the title; venue 16px below the title; author rows with 4.8px vertical and 16px horizontal margins; organization 16px above, footnote 8px; `#links` 16px vertical margin with 140×38 slots.
- **Cards**: separated by a single `<br>` (one 24px line); card title 22.4px above content; `hr.body-hr` pulls up 16px under left-aligned titles and leaves 16px below.
- **Figures**: hero figure at 92% of the card (1132px), wide figures at 86%, figure pairs in a 2-column grid with 20px gap; captions 10px below.
- **Metric cards**: 3-column grid, gap 14px, padding 18px, min-height 128px.
- **Footer**: 80px top margin, padding 16px 0, full-width gradient. Rendered height about 7,300px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1400px | container 1320px | 16px | 48px | as described |
| 1200–1399px | container 1140px | 16px | 48px | same |
| 992–1199px | container 960px | 16px | 48px | same |
| 769–991px | container 720px | 16px | 48px | same |
| ≤768px | container 540px or fluid, 12px | 16px | 33.6px (2.1rem); wordmark 49.6px | card padding 20px; authors one per line; figure pairs and metric grid stack; figures 100% |

## Components

- **Gradient wordmark**: 67.2px heavy serif, `background: linear-gradient(107.54deg, #0078d4 .3%, #8661c5 40.23%, #ff9349 100%)` clipped to text, centered above the title.
- **Gradient pill button**: 115×35, padding 8px 16px, 50px radius, the same three-stop gradient (`fixed` attachment), white 16px/500 text with an 18–20px icomoon glyph left, shadow 0 0 4px rgba(0,0,0,0.5); hover grows to 135×40 and 17px text.
- **Tinted section card**: Bootstrap card with 16px radius, body `linear-gradient(107.54deg, #e6eff7 .39%, #eeebf5 51.23%, #fcf4ee 100%)`, padding 32px, #3f3f3f text, centered 32px/800 title.
- **White section card**: Bootstrap card, 16px radius, white, padding 32px; left-aligned 32px/800 #212529 title followed by a 5px full-width gradient bar (`hr.body-hr`), 24px `h4` subheads.
- **Equation block**: #f8f8fb, 12px radius, padding 10px 14px, centered KaTeX display math.
- **Shadowed figure**: white background, 6px radius, shadow 0 6px 18px rgba(0,0,0,0.1), caption 15.04px #555555.
- **Metric card**: 1px #e4e6f0 border, 14px radius, padding 18px, pale gradient #f2f7fc → #f5f2fb → #fff6f0; headline 16.32px/800 #423f94; text #4a4a4a.
- **Gradient footer**: full-width three-stop gradient, white 15px/800 title and 70%-white text, bold white links.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Wordmark | yes | gradient serif "DiSE" |
| Title and venue | yes | heavy serif title, bold grey venue line between rules |
| Authors, affiliations | yes | bold names in two centered rows |
| Link buttons | yes | one gradient pill (arXiv) |
| Abstract | yes | tinted card with centered title and figure |
| Motivation | yes | tinted card |
| Method with equations | yes | white card, gradient bar, math block, figure pair |
| Observations figures | yes | white card, wide figures |
| Metric cards | yes | three tinted cards |
| Results tables | present but non-standard | results are shown as table images (`.table-figure`), not HTML tables |
| BibTeX | yes | Bootstrap `code` in a card with a blue Copy button |
| Videos, navigation | absent from the source | none |
| Footer | yes | full-width gradient band with template credit |

## Adapting to Other Content

- **More authors**: add rows of `.author-name` inline-blocks; on phones each name takes its own line.
- **More links**: repeat the gradient pill in 140px slots; for a missing resource use the declared `.disabled` grey (rgb(192,192,192)).
- **A results table**: render it as HTML inside a white card: 16px Avenir Next, header weight 800 #212529, 1px #e4e6f0 rules, the method row filled with the pale card gradient.
- **Videos**: place them like figures at 92% or 86% width with the 6px radius and soft shadow.
- **Long publication lists or news**: a white card with the gradient bar under its title and a plain list; highlight the newest item in a tinted metric card.
- **Fixing the title font**: load Playfair Display 600 and 800 so the title and wordmark render as designed rather than in Georgia.

## Do's and Don'ts

- Do reuse the one 107.54° blue-violet-apricot gradient for every accent: wordmark, pill, title bar, footer.
- Do alternate tinted cards (centered titles) and white cards (left titles with the gradient bar).
- Do keep cards at 16px radius and figures at 6px with a soft shadow.
- Do keep the title serif and everything else in Avenir.
- Don't introduce a second accent palette; Bootstrap's default blue survives only on the Copy button.
- Don't place text directly on the strong gradient except the pill and footer.
- Don't use sharp corners on content blocks.

## Surfaces

White page; stacked Bootstrap cards that are either white or tinted with the pale gradient (#e6eff7 → #eeebf5 → #fcf4ee); #f8f8fb math blocks; pale gradient metric cards; a full-saturation gradient footer.

## Imagery

Paper figures with grey and blue token grids, transformer blocks, green "ours" panels with checkmarks, latent-space sketches with arrows, colored histogram distributions and result-table images. All white-backed with a soft shadow and small radius.

## Layout

A centered header, then a single 1320px column of full-width cards, each holding left-aligned or centered text, centered figures (92% or 86% width) and occasional two- or three-column grids. Rendered height about 7,300px.

## Agent Prompt Guide

Quick colors: gradient #0078d4 → #8661c5 → #ff9349, tint #e6eff7 → #eeebf5 → #fcf4ee, card ink #3f3f3f, body #212529, venue #555555, authors #333333, math #f8f8fb, metric #423f94.

1. "Build a centered header on white: a 67.2px weight-800 serif wordmark filled with linear-gradient(107.54deg, #0078d4 .3%, #8661c5 40.23%, #ff9349 100%) clipped to text; a 48px weight-600 serif title in #000000; a bold 19.2px #555555 'ACL 2026 Main' line; bold 18px #333333 author names; then one 115×35 pill with the same gradient, white 16px/500 text and shadow 0 0 4px rgba(0,0,0,0.5)."
2. "Create a section card: 16px radius, background linear-gradient(107.54deg, #e6eff7 .39%, #eeebf5 51.23%, #fcf4ee 100%), padding 32px, a centered 32px weight-800 #3f3f3f title, 16.48px #3f3f3f text, and a centered figure at 92% width with 6px radius and shadow 0 6px 18px rgba(0,0,0,0.1)."
3. "Create a white card with a left-aligned 32px weight-800 #212529 title, directly under it a 5px bar with linear-gradient(107.54deg, #0078d4, #8661c5, #ff9349), then text and a display-math block on #f8f8fb with 12px radius and padding 10px 14px."

## Similar Pages

- Microsoft-Research-flavored project pages that share the 107.54° blue-violet-orange gradient template (the footer credits the original template author).
- Bootstrap 5 card-stack project pages.

## Quick Start

```css
:root {
  --grad: linear-gradient(107.54deg, #0078d4 .39%, #8661c5 51.23%, #ff9349 100%);
  --grad-tint: linear-gradient(107.54deg, #e6eff7 .39%, #eeebf5 51.23%, #fcf4ee 100%);
  --card-ink: #3f3f3f;
  --body-ink: #212529;
  --venue: #555555;
  --author: #333333;
  --link: #6567c9;
  --math-bg: #f8f8fb;
  --metric-ink: #423f94;
  --metric-border: #e4e6f0;
  --radius-card: 16px;
  --font-sans: 'Avenir', 'Avenir Next Cyr', sans-serif;
  --font-title: "Playfair Display", Georgia, "Times New Roman", serif;
}
```

## Provenance

- **URL**: https://zhongzero.github.io/DiSE/
- **Paper**: Efficient Self-Evaluation for Diffusion Language Models via Sequence Regeneration (DiSE; arXiv 2603.02760), Linhao Zhong, Linyu Wu, Wen Wang, Yuling Xi, Chenchen Jing, Jiaheng Zhang, Hao Chen, Chunhua Shen (Zhejiang University, National University of Singapore, Zhejiang University of Technology).
- **Venue**: ACL 2026 Main.
- **Selection reason**: existing verified entry (entries.json); arXiv 2603.02760 comment states acceptance at ACL 2026 Main. Chosen for its gradient wordmark and serif title with content in soft-tinted rounded cards and a display-math block.
- **Template credit**: the footer says the webpage template was originally made by Ximing Xing.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, `style.css`, Bootstrap 5.3.0-alpha3 defaults and `index.html`. Date 2026-10-28.
