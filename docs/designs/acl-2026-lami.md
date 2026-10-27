# Noto Grey Band Academic — Style Reference

> A careful conference handout: Noto Serif headings, navy outlined buttons and soft grey bands taking turns.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the hero, buttons, section headings, TL;DR, abstract, tables, BibTeX and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/style.css` (about 8 KB, headed "LaMI Project Page — Clean Academic Style") with its HTML. Positions are document coordinates at 1440px wide.

## Overview

LaMI is a small hand-written page with a restrained academic voice. Everything is centered on white: a 36px Noto Serif title in near-black, a bold "ACL 2026 Oral" line, navy (#1a5276) author links, grey affiliations with superscripts, an italic "* Equal contribution" note, and four outlined navy buttons with Font Awesome icons. Sections follow in full-width bands that alternate white and #f8f9fa, each opened by a centered 26.4px Noto Serif heading: TL;DR, Abstract, Method (one large architecture figure with a caption that color-codes frozen blue and trainable orange), Results (three clean HTML tables with uppercase group rows and pale-blue highlighted "LaMI" rows), Qualitative Analysis (left-bordered example cards in green, blue and red) and BibTeX in a grey bordered box. Body text is Noto Sans; no shadows, no gradients.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 68.9%, band grey #f8f9fa 21.8% (the Abstract band from y 679), mid grey #c0c2c3 5.4% (text anti-aliasing and button outlines), remainder under 1.5%. Navy #1a5276 appears only in author names and the four button outlines.

Anatomy in DOM order (y = top of element box, content column x 254–1186):

1. **Title** (`h1.title`), y 72, two lines, Noto Serif 36px/700, line-height 46.8px, #1a1a1a, centered. Gap 24px.
2. **Venue line** (`p.venue-text > strong`), y 190, "ACL 2026 Oral", Noto Sans 16.8px bold, #333333. Gap 22px.
3. **Authors** (`.authors`), y about 241, Noto Sans 17.6px/500 links in #1a5276, line-height 1.8, comma-separated, superscripts ¹ ² *. Gap 8px.
4. **Affiliations** (`.affiliations`), Noto Sans 14.72px #555555, spans separated by three spaces. Gap 4px.
5. **Equal contribution** (`p.equal-contribution`), y 315, 13.12px italic #888888. Gap 24px.
6. **Buttons** (`.links`), y 361, four buttons 44px tall, gap 10px: "Paper", "ArXiv", "Code", "BibTeX", Noto Sans 14.4px/500 #1a5276 on #ffffff, 1.5px solid #1a5276 border (draws 1px at 1×), radius 4px, padding 9px 20px, icons left (file-pdf, archive, GitHub, quote). Hero bottom padding 40px.
7. **TL;DR section** (`section.section`), y 445, padding 56px: centered h2 "TL;DR" (y 501), then a 16.32px #333333 paragraph in a 780px narrow container (x 354–1086).
8. **Abstract band** (`section.section-gray`), from y 679 on #f8f9fa; the fold falls inside it.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| White | #ffffff | `body` | Page, hero, white sections, button fill, example cards |
| Band Grey | #f8f9fa | `.section-gray` | Abstract, Results and BibTeX bands |
| Heading Ink | #1a1a1a | `h1–h4`, `.title` | Title, section headings, table titles, example titles |
| Body Ink | #2c2c2c | `body` | Default text, table cells |
| Text Grey | #333333 | `.venue-text`, `.tldr-text`, `.abstract-text`, BibTeX code | Venue line, TL;DR, abstract, BibTeX |
| Secondary Grey | #444444 | `.method-text`, `.section-description`, `.example p` | Method and section descriptions, example text |
| Affiliation Grey | #555555 | `.affiliations`, `.caption`, `.example-question` | Affiliations, figure caption, italic example questions |
| Note Grey | #888888 | `.equal-contribution`, `footer` | Equal-contribution note, footer text |
| Navy | #1a5276 | `a`, `.btn` | Author links, button text and border, button hover fill, footer link |
| Header Fill | #f0f2f4 | `thead th` | Table header cells |
| Rule Grey | #cccccc | `thead th`, `.copy-btn` | 2px table header rule, backbone separators, copy button border |
| Row Rule | #eaeaea | `tbody td`, `footer` | 1px row rules, footer top border |
| Note Grey 2 | #777777 | `.table-note` | Notes under tables |
| Group Grey | #666666 | `tr.group-header td` | Uppercase table group labels, copy icon |
| Highlight Row | #eef5fb | `tr.highlight` | "LaMI" rows in tables (rule #d4e4ef) |
| Frozen Blue | #2e86c1 | `.color-frozen`, `.example.robustness` | "Blue: frozen" in the caption, robustness example edge (fill #f5fafd) |
| Trainable Orange | #d68910 | `.color-trainable` | "orange: trainable" in the caption |
| Success Green | #27ae60 | `.example.success` | Success example left edge (fill #f6fdf8) |
| Failure Red | #c0392b | `.example.failure` | Failure example left edge (fill #fdf6f5) |
| Code Box | #f5f6f8 | `.bibtex-container` | BibTeX box (1px #dddddd border) |

## Tokens — Typography

- **Headings**: declared `'Noto Serif', 'Georgia', serif` for `h1–h4`, from Google Fonts (400, 600, 400 italic requested). Rendered: Noto Serif 600 only (`fonts_loaded`); the title asks for 700, which no loaded face has, so it draws with the 600 face. Substitute: Source Serif 4 (similar width and sturdy serifs).
- **Body and UI**: declared `'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`. Rendered: Noto Sans 400, 400 italic, 500, 600, 700. Example and method card titles (`h4`, `.method-point h3`) switch to Noto Sans.
- **Mono**: `'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', monospace` for BibTeX (system font).
- **Icons**: Font Awesome 6.5.1 (Free and Brands).

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Paper title | `.title` | 36px (2.25rem) / 46.8px | 700 requested, 600 rendered | #1a1a1a |
| Section heading | `h2` | 26.4px (1.65rem) / 44.9px, centered | 600 | #1a1a1a |
| Table title | `h3.table-title` | 17.92px (1.12rem) / 30.5px, centered | 600 | #1a1a1a |
| Authors | `.authors a` | 17.6px (1.1rem) / 31.7px | 500 | #1a5276 |
| Venue | `.venue-text strong` | 16.8px (1.05rem) | 700 | #333333 |
| TL;DR | `.tldr-text` | 16.32px (1.02rem) / 28.6px | 400 | #333333 |
| Abstract | `.abstract-text` | 16px / 28.8px (1.8) | 400 | #333333 |
| Body | `body` | 16px / 27.2px (1.7) | 400 | #2c2c2c |
| Method text | `.method-text`, `.section-description` | 15.52px (0.97rem) / 1.7 | 400 | #444444 |
| Affiliations | `.affiliations` | 14.72px (0.92rem) | 400 | #555555 |
| Button | `.btn` | 14.4px (0.9rem) | 500 | #1a5276 |
| Table body | `tbody td` | 14.4px / 24.5px | 400 | #2c2c2c |
| Table header | `thead th` | 14.08px (0.88rem) | 600 | #2c2c2c |
| Caption | `.caption` | 14.08px / 1.6 | 400 (lead bold) | #555555 |
| Table group label | `tr.group-header td` | 13.44px, uppercase, 0.03em | 600 | #666666 |
| BibTeX | `.bibtex-container code` | 13.44px / 1.6 | 400 mono | #333333 |
| Footer | `footer` | 13.6px | 400 | #888888 |
| Equal contribution | `.equal-contribution` | 13.12px | 400 italic | #888888 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Button | 4px | 1.5px solid #1a5276 (1px at 1×) | none |
| Method figure | 4px | none | none |
| Example card | 6px | 4px left (#27ae60, #2e86c1 or #c0392b) | none |
| BibTeX box | 6px | 1px solid #dddddd | none |
| Copy button | 4px | 1px solid #cccccc | none |
| Table header | 0 | 2px solid #cccccc bottom | none |
| Table rows | 0 | 1px solid #eaeaea bottom; highlight rows #d4e4ef | none |
| Footer | 0 | 1px solid #eaeaea top | none |

No shadows or gradients anywhere.

## Layout Metrics

- **Container**: `.container` max-width 980px, padding 0 24px, so content spans x 254–1186 (932px). `.container-narrow` is 780px (732px of text, x 354–1086) for TL;DR and Abstract.
- **Hero**: padding 72px 24px 40px, all centered.
- **Sections**: `.section` padding 56px 0; h2 margin-bottom 20px; bands alternate white and #f8f9fa with no rules between them.
- **Method**: description max-width 760px centered with 28px bottom margin; figure full container width (932px), caption max-width 700px left-aligned, 14px above; figure block 40px bottom margin.
- **Tables**: full container width, header cells padded 10px 16px, body cells 8px 16px, group rows 16px top / 6px bottom; table titles 40px above (first 0).
- **Examples**: vertical stack with 20px gaps, card padding 22px 26px.
- **BibTeX**: box padding 20px 24px, copy button absolute at 12px from the top right.
- Rendered height about 6,650px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px | 24px inside a 980px container | 16px | 36px | layout as described |
| ≤768px | 24px (hero 16px) | 16px | 24.8px (1.55rem) | hero padding 48px 16px 32px; sections 40px; authors 16px; table cells 8px 10px at 13.12px |
| ≤480px | 24px | 16px | 20.8px (1.3rem) | buttons stack vertically, full width up to 220px, centered |

## Components

- **Outlined navy button**: inline-flex, gap 7px, padding 9px 20px, Noto Sans 14.4px/500, #1a5276 text on #ffffff, 1.5px solid #1a5276 border, 4px radius, Font Awesome icon on the left; hover fills #1a5276 with white text.
- **Centered section heading**: Noto Serif 26.4px/600 #1a1a1a, centered, 20px below; the text under it stays left-aligned.
- **Results table**: full width, collapse; header cells #f0f2f4, 14.08px/600, 2px #cccccc bottom rule; body 14.4px with 1px #eaeaea rules; uppercase 13.44px/600 #666666 group rows ("MASKED LANGUAGE MODELS") with extra top padding; the method's rows #eef5fb with bold numbers and a #d4e4ef rule; 1.5px #cccccc separators between backbones; a 13.12px #777777 note below.
- **Example card**: padding 22px 26px, 6px radius, 4px colored left border with a matching tint (success #27ae60 on #f6fdf8, robustness #2e86c1 on #f5fafd, failure #c0392b on #fdf6f5); Noto Sans 15.2px/600 title, italic #555555 question, 14.72px #444444 explanation.
- **BibTeX box**: #f5f6f8 with 1px #dddddd border, 6px radius, padding 20px 24px, mono 13.44px #333333; an icon-only copy button (1px #cccccc border, #666666 icon, hover #1a5276).
- **Footer**: centered 13.6px #888888 line with a #1a5276 link, 1px #eaeaea top border, padding 36px 24px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Title, venue, authors | yes | centered serif title, bold venue line, navy author links |
| Link buttons | yes | four outlined navy buttons |
| TL;DR | yes | centered heading, one paragraph |
| Abstract | yes | grey band, 780px column |
| Method figure | yes | full-width figure with color-keyed caption |
| Method point cards | present but non-standard | `.method-point` styles exist (white, 1px #e8e8e8, 6px radius) but the page uses plain bold-led paragraphs instead |
| Results tables | yes | three HTML tables with group rows and highlighted rows |
| Qualitative examples | yes | three left-bordered tinted cards |
| BibTeX | yes | grey bordered box with copy icon |
| Teaser image | absent from the source | `.teaser` styles exist but no teaser in the markup |
| Navigation, videos | absent from the source | none |
| Footer | yes | one centered contact line |

## Adapting to Other Content

- **More authors**: keep the comma-separated 17.6px navy list; it wraps on the centered line. Use superscript numbers tied to the 14.72px affiliation spans.
- **A teaser**: use the declared `.teaser` rule: centered image up to 620px, 4px radius, with a 14.08px #555555 caption up to 700px.
- **Videos**: same as figures: full 932px width, 4px radius, no frame or shadow.
- **Key contributions**: use the declared `.method-point` cards in a two-column grid with a 32px gap (white, 1px #e8e8e8, 6px radius, 24px padding, 16.32px/600 Noto Sans title).
- **Long publication lists or news**: a plain list in a white band with Noto Serif 17.92px year headings and 14.4px items; links #1a5276.
- **More tables**: repeat the table recipe; keep group rows uppercase grey and the proposed method in #eef5fb.

## Do's and Don'ts

- Do center headings and the hero, but keep paragraphs left-aligned.
- Do alternate white and #f8f9fa bands for section rhythm instead of rules.
- Do keep one link color, #1a5276, for authors, buttons and links.
- Do mark the proposed method in tables with #eef5fb rows and bold numbers.
- Don't add shadows, gradients or rounded corners above 6px.
- Don't fill the buttons by default; they fill navy only on hover.
- Don't use serif type for body text; serif is for headings only.

## Surfaces

White and #f8f9fa bands only. Inset surfaces: table header #f0f2f4, highlighted rows #eef5fb, tinted example cards (#f6fdf8, #f5fafd, #fdf6f5) and the BibTeX box #f5f6f8.

## Imagery

One architecture diagram in the paper's style: a thought cloud of generated parrot images, pale blue encoder and LLM boxes, orange fusion-layer boxes and stacked token columns, on white with no frame. No photos, no videos.

## Layout

A 980px centered container with a 780px narrow column for TL;DR and Abstract. All sections are full-bleed bands; content is a single column of headings, text, a figure and tables. Rendered height about 6,650px.

## Agent Prompt Guide

Quick colors: white #ffffff, band #f8f9fa, heading #1a1a1a, body #2c2c2c, text #333333, affiliations #555555, navy #1a5276, header fill #f0f2f4, highlight row #eef5fb.

1. "Build a centered hero on white with 72px top padding: a Noto Serif 36px #1a1a1a title (weight 600 face), 24px below a bold 16.8px #333333 'ACL 2026 Oral' line, then Noto Sans 17.6px/500 author links in #1a5276 with superscripts, 14.72px #555555 affiliations and a 13.12px italic #888888 equal-contribution note."
2. "Add four outlined buttons 10px apart: Noto Sans 14.4px/500 #1a5276 on #ffffff, 1.5px solid #1a5276 border, 4px radius, padding 9px 20px, a Font Awesome icon on the left; on hover fill #1a5276 with white text."
3. "Create a results table at full container width: header cells #f0f2f4 with 14.08px/600 labels and a 2px #cccccc bottom rule; body 14.4px with 1px #eaeaea rules and 8px 16px padding; uppercase 13.44px/600 #666666 group rows; the proposed method's rows filled #eef5fb with bold numbers."

## Similar Pages

- Plain academic project pages that drop the Nerfies/Bulma template for a single hand-written stylesheet.
- Pages with alternating white and light-grey section bands and centered serif headings.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --band: #f8f9fa;
  --heading: #1a1a1a;
  --text: #2c2c2c;
  --text-2: #333333;
  --muted: #555555;
  --link: #1a5276;
  --th-bg: #f0f2f4;
  --row-rule: #eaeaea;
  --highlight: #eef5fb;
  --font-sans: 'Noto Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-serif: 'Noto Serif', Georgia, serif;
  --container: 980px;
  --narrow: 780px;
}
```

## Provenance

- **URL**: https://guyyariv.github.io/LaMI/
- **Paper**: LaMI: Augmenting Large Language Models via Late Multi-Image Fusion (arXiv 2406.13621), Guy Yariv, Idan Schwartz, Yossi Adi, Sagie Benaim (The Hebrew University of Jerusalem, Bar-Ilan University).
- **Venue**: ACL 2026 (oral, per the page).
- **Selection reason**: existing verified entry (entries.json); arXiv 2406.13621 comment states acceptance at ACL 2026. Chosen as a restrained serif academic page done with care: outlined buttons, alternating grey bands, a TL;DR block, a well-captioned method figure and a clean table.
- **Template credit**: none; the stylesheet is titled "LaMI Project Page — Clean Academic Style".
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture, `static/style.css` and `index.html`. Date 2026-10-28.
