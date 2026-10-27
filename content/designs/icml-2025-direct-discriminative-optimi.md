# DDO Cosmos Cards — Style Reference

> A corporate lab notebook on sage paper: a black brand bar, one electric green that ties the title to every button, and each section filed in its own soft white card.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the lab's shared stylesheets (../style.css for the brand header and footer, ../project.css for project pages). The root font size is 18px (`html { font-size: 18px }`), so rem values below are converted at 18px. Sections fade in on scroll (`.reveal-start`), which is why the first Abstract card is still transparent in the 1440 screenshot.

## Overview

The page is an NVIDIA Cosmos Lab project page built on the lab's shared template. A 50px black sticky bar carries the NVIDIA logo, a thin divider and "Cosmos Lab", with Products, Press and Publications on the right. The canvas is a pale sage (#f1f3ee). The hero is left-aligned in a 1000px column: a 29px bold title whose first phrase, "Direct Discriminative Optimization", is larger and in NVIDIA green (#76b900); gray author names separated by middle dots; "ICML 2025" in amber and "· Spotlight" in rust; then three green pill buttons with soft green glows. The teaser figure sits in a white 16px-radius card with a light shadow, its caption inside the card. Every section after (Abstract, DDO Pipeline, Results, Citation) is its own white rounded card with a bold heading over a 2px gray rule. A round outlined "Top" button and a near-black footer close the page.

## First Viewport

Color share of the 1440×900 viewport: #f1f3ee 49% (sage canvas), #ffffff 24% (teaser card), #919482 11% (gray plot curves and text, blended), #f1f3ed 8% and #f7f8f5 5% (canvas variants and the incoming Abstract card), #ecf4f3 2% (the light-blue plot fill), #f3f3ef 1%. Above the fold the only saturated colors are the green title phrase and buttons, the amber/rust venue line, the black bar and the plot's blue, orange and red marks.

Anatomy in DOM order (hero column x 220–1220):

1. **Brand bar** `header.site-header`: sticky, 50px, #000000; inner max-width 1280px with 48px padding. NVIDIA wordmark logo (108×38) at x 128, a thin divider, "Cosmos Lab" 16.5px white. Nav Products, Press, Publications: 15.75px, rgba(255,255,255,.8), padding 6px 12px, radius 6px; hover white with a 2px #76b900 underline that scales in. Gap 40px (page padding) + 24px (hero padding).
2. **Title** `h1.project-title`: NVIDIA-NALA 28.8px/700 (clamp 1.4rem, 2vw, 1.7rem), line-height 1.3, letter-spacing -0.01em, #333333, left, two lines; `span.title-special` "Direct Discriminative Optimization" at 33.1px (1.15em) in #76b900. Gap 24px.
3. **Authors** `p.project-authors`: 18px/400 #555555, names separated by " · ". Gap 18px.
4. **Venue line** `.project-venue`: "ICML 2025" 18.9px/500 #c27b1d, then "· Spotlight" 18.9px/500 #b0401a with a #bbbbbb dot. Gap 30px.
5. **Buttons** `.project-links`: Paper, Code, Hugging Face; 39px tall green pills, 8px apart, small line icons left.
6. **Teaser card** `.teaser-card` (from y ≈ 404): #ffffff, radius 16px, padding 12px, shadow 0 2px 8px rgba(0,0,0,.07); a 976px-wide two-panel density plot (radius 8px) and a 16.5px #1a1a1a caption below it inside the card.
7. **Abstract card** begins 20px below the teaser card at the fold edge.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Sage Canvas | #f1f3ee | (literal) | page background |
| Card White | #ffffff | (literal) | teaser card, section cards, results figures, button label |
| Brand Black | #000000 | (literal) | sticky brand bar |
| Footer Black | #0a0a0a | --footer-bg | footer band |
| NVIDIA Green | #76b900 | --green | title phrase, link buttons, nav hover underline, copy button border, links in authors and abstract, subheadings, best table cells, active carousel dot |
| Green Hover | #63a000 | (literal) | link button hover |
| Green Ink | #5a8e00 | (literal) | copy button text |
| Title Gray | #333333 | (literal) | title, BibTeX text, table cells |
| Ink | #1a1a1a | (literal) | body text, section headings, captions |
| Author Gray | #555555 | (literal) | author line |
| Venue Amber | #c27b1d | (literal) | venue name |
| Award Rust | #b0401a | (literal) | "Spotlight" award label |
| Dot Gray | #bbbbbb | (literal) | separator dot before the award |
| Rule Gray | #e8e8e8 | (literal) | 2px rule under section headings |
| Code Wash | #f6f6f6 | (literal) | BibTeX block |
| Code Border | #e0e0e0 | (literal) | BibTeX and table borders |
| Table Head | #f0f0f0 | (literal) | table header cells |
| Table Head Rule | #d4d4d4 | (literal) | 1.5px rule under table headers |
| Table Row Rule | #ececec | (literal) | table row borders |
| Table Head Text | #222222 | (literal) | table header text |
| Nav Button Border | #cccccc | (literal) | "Top" page-nav button border |
| Muted | #666666 | (literal) | "Top" button text, figure captions in results |
| Nav Text | rgba(255,255,255,.8) | (literal) | brand-bar nav links |

## Tokens — Typography

- **Sans**: declared `'NVIDIA-NALA', Arial, Helvetica, sans-serif`; renders NVIDIA Sans (NALA build) as a variable font (100–900) plus static 400, 500, 700. Substitute: Inter (close proportions), or DM Sans for the rounder feel.
- **Mono**: `ui-monospace, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace` for BibTeX (Consolas on Windows).

| Role | Selector | Size at 1440 | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title phrase | `.title-special` | 33.1px (1.15em of title) | 700 | 1.3 | -0.01em |
| Title | `.project-title` | 28.8px (clamp 25.2px, 2vw, 30.6px) | 700 | 1.3 | -0.01em |
| Section heading | `.proj-heading` | 26.1px (clamp 19.8px, 2.4vw, 26.1px) | 700 | 23.1px (inherited 1.4em) | -0.01em |
| Subheading | `.proj-subheading` | 19.8px green | 700 | 1.4 | -0.01em |
| Venue, award | `.venue-pill`, `.award-pill` | 18.9px | 500 | 1.4 | 0 |
| Authors | `.project-authors` | 18px | 400 | 1.4 | 0 |
| Body | `body` | 16.5px | 400 | 1.4em (23.1px) | 0 |
| Brand-bar nav | `.header-nav a` | 15.75px | 400 | 1.4 | 0 |
| Page nav | `.page-nav-btn` | 15.3px | 500 | 1.4 | 0 |
| Link buttons | `.link-btn` | 14.9px (0.83rem) | 600 | 1.4 | 0 |
| BibTeX | `.citation pre` | 14px mono | 400 | 1.4 | 0 |
| Copy button | `.copy-btn` | 13.5px | 600 | 1.4 | 0 |
| Figure captions | `.results-grid figcaption` | 14px (0.78rem) | 400 | 1.4 | 0 |

## Tokens — Spacing & Shapes

- **Radius**: 100px for link buttons and the page-nav button; 16px for the teaser and section cards; 10–12px for results figures and carousel cards; 8px for images, BibTeX and table wraps; 6px for nav links; 4px for the copy button.
- **Shadows**: cards 0 2px 8px rgba(0,0,0,.07); link buttons 0 2px 8px rgba(118,185,0,.35), hover 0 4px 14px rgba(118,185,0,.45) with a 1px lift; results figures hover 0 6px 20px rgba(0,0,0,.13).
- **Borders**: 2px #e8e8e8 under section headings; 1px #e0e0e0 around BibTeX and tables; 1.5px #76b900 on the copy button; 1.5px #cccccc on the page-nav button.

## Layout Metrics

- **Page**: `.project-page` padding 40px clamp(12px, 3vw, 40px) 80px; content max-width 1000px centered (x 220–1220 at 1440).
- **Brand bar**: inner max-width 1280px, padding 0 clamp(16px, 4vw, 48px), height 50px.
- **Hero**: padding 24px 0 32px, left-aligned; title margin-bottom 24px; authors 18px; venue 30px; buttons 8px apart.
- **Teaser card**: margin-top 20px, padding 12px; image max-height 640px, contain.
- **Section cards**: `.proj-section` max-width 1000px, margin 20px auto 0, padding 40px clamp(12px, 4vw, 40px) = 40px, so card content is 920px (x 260–1180); heading 20px above content with 10px padding over the 2px rule.
- **Results grid**: auto-fill minmax(260px, 1fr), 12px gap, figures in white 10px-radius cards with 8px padding.
- **Page nav**: 48px above the footer area, centered.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥640px | clamp(12px, 3vw, 40px) | 16.5px | 2vw (25.2–30.6px) | brand-bar nav inline; results grid auto-fill 260px |
| ≤639px | 12–19px | 16.5px | 25.2px | nav collapses into a hamburger drop-down under the bar; results grid 1 column; figure blocks full width; hero bottom padding 20px |
| ≤479px | 12px | 16.5px | 25.2px | lab-wide hero variables tighten (no change to project content) |

## Components

- **Green pill** `.link-btn`: padding 8px 20px, radius 100px, no border, #76b900 fill, #ffffff 14.9px/600, 7px gap after a small line icon; shadow 0 2px 8px rgba(118,185,0,.35); hover #63a000 with a stronger glow and 1px lift.
- **Section card** `.proj-section`: #ffffff, radius 16px, padding 40px, shadow 0 2px 8px rgba(0,0,0,.07); heading 26.1px/700 #1a1a1a with 10px bottom padding and a 2px #e8e8e8 rule, 20px above the content.
- **Teaser card**: same surface with 12px padding; media radius 8px; caption in body text inside the card.
- **Venue line**: amber venue name, a #bbbbbb "·", rust award label, both 18.9px/500, no pill background despite the class names.
- **Results figure**: #ffffff card, radius 10px, padding 8px, light shadow; hover lifts 2px; caption 14px #666666 centered.
- **Table** `.proj-table`: wrapper 1px #e0e0e0 with 8px radius; header #f0f0f0 with a 1.5px #d4d4d4 bottom border, 14.8px/600 #222; cells 8px 14px with 1px #ececec rules; best values 700 #76b900 on rgba(118,185,0,.08).
- **BibTeX**: #f6f6f6, 1px #e0e0e0, radius 8px, padding 18px 20px, 14px mono #333333; copy button bottom-right: padding 5px 13px, radius 4px, 1.5px #76b900 border, rgba(118,185,0,.07) fill, #5a8e00 13.5px/600; hover fills green with white text.
- **Page-nav button**: padding 9px 20px, radius 100px, 1.5px #cccccc border, #666666 15.3px/500; hover border and text #76b900.
- **Brand bar nav link**: 15.75px rgba(255,255,255,.8), padding 6px 12px, hover #ffffff with a 2px green underline scaling in from the center.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | black lab brand bar, sticky, frosted when scrolled |
| Title block | yes | left-aligned bold title with a larger green lead phrase |
| Authors / affiliations | yes, non-standard | one dot-separated author line; no affiliations |
| Venue / award | yes | amber venue, rust "Spotlight" |
| Link buttons | yes | green glowing pills |
| Teaser | yes | toy-example figure in a white card with caption |
| Abstract | yes | white card, with sample grids and captions inside |
| Method figure | yes | "DDO Pipeline" card with diagram and bullet list |
| Results | yes | card with paper tables as images |
| BibTeX | yes | gray block with green copy button |
| Page nav | yes | outlined "Top" pill |
| Footer | yes | near-black lab footer with legal links |

## Adapting to Other Content

- **More authors**: keep the single dot-separated 18px #555555 line and let it wrap; turn names into links in #76b900; put affiliations on a second line in 16.5px #555555.
- **Results table**: use `.proj-table` in a section card: #f0f0f0 header, #ececec row rules, best values in bold #76b900 on a faint green tint.
- **Long publication list**: a section card with rows separated by 1px #e0e0e0; titles 16.5px/700 #1a1a1a, venue in #c27b1d, award in #b0401a, link pills in green below each.
- **News**: a card titled "News" with a bulleted list; dates in 700 #76b900.
- **Video results**: the template's carousel card (white, radius 12px, padding 8px) with round rgba(0,0,0,.55) arrows that turn green on hover and #76b900 active dots.

## Do's and Don'ts

- Do tie everything interactive to one green (#76b900): title phrase, buttons, links, best values.
- Do place every section in its own white 16px-radius card on the sage canvas, 20px apart.
- Do keep the hero left-aligned in the 1000px column, no hero image.
- Do give buttons a soft green glow instead of borders.
- Don't introduce a second accent; amber and rust are only for venue and award.
- Don't put text directly on the sage canvas below the hero; it always sits in a card.
- Don't use the black bar color anywhere but the header and footer.

## Surfaces

Sage #f1f3ee canvas; #ffffff cards with 0 2px 8px rgba(0,0,0,.07) shadows; #f6f6f6 code; black #000000 brand bar; #0a0a0a footer.

## Imagery

A two-panel density plot as the teaser (blue and orange fills with red arrows), image-sample grids (EDM2 and VAR on ImageNet) with captions, a pipeline diagram and paper result tables rendered as images.

## Layout

A black brand bar, a text-only hero, then a vertical stack of 1000px white cards on sage: teaser, Abstract, Pipeline, Results, Citation, with a "Top" button and a dark footer. About 4,900px tall.

## Agent Prompt Guide

Quick colors: canvas #f1f3ee, card #ffffff, green #76b900 (hover #63a000), green ink #5a8e00, title #333333, ink #1a1a1a, authors #555555, venue #c27b1d, award #b0401a, rule #e8e8e8, code #f6f6f6 with #e0e0e0 border, bar #000000, footer #0a0a0a.

1. "Build a hero on #f1f3ee in NVIDIA Sans (or Inter): left-aligned 1000px column; title 28.8px/700, line-height 1.3, letter-spacing -0.01em, #333333, with its lead phrase at 1.15em in #76b900; authors 18px #555555 separated by ' · '; venue 18.9px/500 #c27b1d and '· Spotlight' in #b0401a; then green pills."
2. "Build green pill buttons: padding 8px 20px, radius 100px, background #76b900, #ffffff 14.9px/600, small line icon left with 7px gap, shadow 0 2px 8px rgba(118,185,0,.35); hover #63a000, shadow 0 4px 14px rgba(118,185,0,.45), translateY(-1px)."
3. "Build a section card: max-width 1000px, margin 20px auto 0, background #ffffff, radius 16px, padding 40px, shadow 0 2px 8px rgba(0,0,0,.07); heading 26.1px/700 #1a1a1a, padding-bottom 10px, border-bottom 2px solid #e8e8e8, margin-bottom 20px; body 16.5px/1.4 #1a1a1a."

## Similar Pages

- Other project pages on the same lab template (research.nvidia.com/labs/cosmos-lab), which share the brand bar, sage canvas and white section cards.
- Card-stack project pages with a single brand accent on buttons and title.

## Quick Start

```css
:root {
  --canvas: #f1f3ee;
  --card: #ffffff;
  --green: #76b900;
  --green-hover: #63a000;
  --green-ink: #5a8e00;
  --title: #333333;
  --ink: #1a1a1a;
  --authors: #555555;
  --venue: #c27b1d;
  --award: #b0401a;
  --rule: #e8e8e8;
  --code-bg: #f6f6f6;
  --code-border: #e0e0e0;
  --bar: #000000;
  --footer-bg: #0a0a0a;
  --page-max-width: 1000px;
  --card-shadow: 0 2px 8px rgba(0,0,0,0.07);
  --font: 'NVIDIA-NALA', Arial, Helvetica, sans-serif;
}
html { font-size: 18px; }
body { background: var(--canvas); color: var(--ink); font-size: 16.5px; line-height: 1.4em; font-family: var(--font); }
```

## Provenance

- **URL**: https://research.nvidia.com/labs/cosmos-lab/ddo/
- **Paper**: Direct Discriminative Optimization: Your Likelihood-Based Visual Generative Model is Secretly a GAN Discriminator (arXiv 2503.01103), Kaiwen Zheng, Yongxin Chen, Huayu Chen, Guande He, Ming-Yu Liu, Jun Zhu, Qinsheng Zhang.
- **Venue**: ICML 2025, Spotlight.
- **Selection reason**: the arXiv comment states acceptance at ICML 2025 as a Spotlight and links this page.
- **Template credit**: NVIDIA Cosmos Lab shared project-page template (style.css and project.css at the lab root); the page body is filled from JSON by project.js.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and style.css plus project.css read directly. Captured 2026-10-28.
