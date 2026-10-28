# URSA Editorial — Style Reference

> A quiet journal spread with one violet thread: a Fraunces headline, a lilac pill and a single outlined button pick out the paper while everything else stays ink on white.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), extra probes of the venue pill, video cards, BibTeX spans and paddings at 1440, 1100 and 900px, the 1440×900 and full-page screenshots, and the page's own `styles.css` and `index.html`. The hero is an autoplaying video, so the screenshot shows one frame of it. The four result videos had not loaded their first frame at capture time and show a spinner over a black control bar; they are ordinary `<video controls>` elements.

## Overview

A short, single-column project page (about 2,850px tall) on pure white with near-black ink (#0a0a0a). The look rests on a typographic contrast: Fraunces 700 for the title and headings, Inter for everything else. One violet, #5a4df5, is the only accent and appears in four places: the venue pill, the outlined "Paper" button, the bold method name in the abstract and inline links. A translucent sticky header with a text wordmark "URSA" and four text links sits above a centred hero; the teaser is a wide video that blends four rounded robot clips with a central scatter plot on white, so it reads as part of the page rather than as a framed media box. Below come three sections separated by 1px #e6e6e6 rules: Abstract, Key Results (a 2×2 grid of captioned videos with soft shadows), and Citation (a black BibTeX block with violet syntax colours).

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fefefe / #fdfdfd together 75.4%; mid-gray #959192 10.1% (the foam floor in the teaser clips); dark slate #403f4d 9.5% (title ink, robot bodies, blue walls and plot points blended); light gray #e1e1e4 4.9% (button borders, header rule, anti-aliasing). The violet covers too little area to form its own cluster.

Anatomy in DOM order (desktop 1440px, everything centred in a 960px column at x=240):

1. **Sticky header** (`header.site-header`, 0–61px): rgba(255,255,255,0.85) with `backdrop-filter: saturate(180%) blur(8px)` and a 1px #e6e6e6 bottom border. Inner `nav.container` is 60px tall with 32px side padding. Left "URSA" wordmark 16px/700 #0a0a0a, letter-spacing 0.2px, at x=272; right four links (Abstract, Key Results, Extended Video, Cite) 15.2px/400 #222222, 14px left margin each, ending at x=1168. Gap to title: hero padding-top 56px.
2. **Title** (`h1`, y=117, 148px tall): Fraunces 44px/700, line-height 1.12 (49.28px), #0a0a0a, centred, `text-wrap: balance`, three lines. Margin-bottom 8px; the authors' 10px top margin wins the collapse, so gap 10px.
3. **Authors** (`p.authors`, y=275): Inter 16.96px/600 #151515, letter-spacing 0.2px, word-spacing 0.2rem, names joined by " · ". Gap 16.96px.
4. **Lab line** (`p.lab`, y=320): 16px/400 #626262. Gap 16px.
5. **Venue pill** (`span.venue-badge`, y=362, 289×44px): "CoRL 2025" 700 plus " · Seoul, South Korea" 400, both 16px #5a4df5, on rgba(107,92,255,0.08), 1px #5a4df5 border, radius 9999px, padding 8px 14px, shadow `0 6px 20px rgba(107, 92, 255, 0.12)`. The `.venue-dot` span has no styles and renders 0×0. Gap: venue-wrap margin-bottom 8px collapses into the figure's 18px top margin, so 18px.
6. **Teaser video** (`.hero-figure video`, y=425, 960×385): autoplay, muted, loop; radius 10px on a white wrapper, no border or shadow. The clip itself draws four capsule-shaped robot views joined by thin black leader lines to a red-to-blue scatter plot with a colourbar labelled V(s₀, z). Gap 14px.
7. **Button row** (`.cta`, y=824, 48px tall): five buttons centred with 10px gaps (Paper, Poster, X logo, Copy BibTeX, Extended Video). Hero padding-bottom 22px, so the Abstract section's top rule lands at y=894.

Arithmetic check: 61 + 56 = 117; 117 + 148 + 10 = 275; 275 + 28 + 16.96 ≈ 320; 320 + 26 + 16 = 362; 362 + 44 + 18 = 424 (rendered 425); 425 + 385 + 14 = 824; 824 + 48 + 22 = 894.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | --bg | page background, button fills, video-card wrappers, hero video wrapper |
| Ink | #0a0a0a | --ink | body text, title, h2/h3 headings, wordmark, button labels |
| Author Ink | #151515 | (literal, `.authors`) | author line |
| Nav Ink | #222222 | (literal, `.nav-links a`) | header links |
| Muted | #626262 | --muted | lab line, video captions, footer text |
| Rule | #e6e6e6 | --rule | header bottom border, section top borders, footer top border, default button borders |
| Violet | #5a4df5 | --accent | venue pill text and border, Paper button text, border and icon, method name in the abstract, inline links, header link hover |
| Soft Violet | #8b82ff | --accent-2 | Paper button border on hover |
| Pill Wash | rgba(107,92,255,0.08) | (literal) | venue pill fill; Paper button shadow colour |
| Pill Glow | rgba(107,92,255,0.12) | (literal) | venue pill shadow |
| Hover Border | #d5d5d5 | (literal, `.btn:hover`) | default button border on hover |
| Code Black | #0b0b0b | (literal, `pre`) | BibTeX block background |
| Code Text | #e8e8e8 | (literal, `.bibtex-value`) | BibTeX field values |
| Code Entry | #9d96ff | (literal, `.bibtex-entry-type`) | "@inproceedings" |
| Code Key | #c4bfff | (literal, `.bibtex-key`) | citation key |
| Code Field | #b8b5ff | (literal, `.bibtex-field`) | field names (title, author…) |
| Code Punctuation | #888888 | (literal) | braces, equals signs, commas in BibTeX |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | "Fraunces", Georgia, "Times New Roman", serif (Google Fonts, opsz 9..144, weights 600 and 700) | Fraunces 700 | Source Serif 4 Bold |
| Body | "Inter", system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif (weights 400, 500, 600) | Inter 400, Inter 600 | Roboto |
| Code | browser `monospace` (no family declared on `pre`) | Consolas on Windows, Menlo on macOS | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | clamp(2rem, 4.2vw, 2.75rem) → 44px / 700 / 1.12, balanced wrap | #0a0a0a |
| Section heading | `h2` | clamp(1.25rem, 2.4vw, 1.5rem) → 24px / 700 / 1.2, margin-bottom 8px | #0a0a0a |
| Video title | `.video-item h3` | 1.1rem = 17.6px / 700 / 1.65, margin-bottom 12px | #0a0a0a |
| Body | `body` | 16px / 400 / 1.65 (26.4px) | #0a0a0a |
| Authors | `.authors` | 1.06rem = 16.96px / 600, letter-spacing 0.2px, word-spacing 0.2rem | #151515 |
| Lab | `.lab` | 16px / 400 | #626262 |
| Wordmark | `.brand` | 16px / 700, letter-spacing 0.2px | #0a0a0a |
| Header link | `.nav-links a` | 0.95rem = 15.2px / 400 | #222222 |
| Venue pill | `.venue-badge` | 16px; "CoRL 2025" 700, location 400; letter-spacing 0.2px | #5a4df5 |
| Button | `.btn` | 16px / 600 | #0a0a0a; primary #5a4df5 |
| Small button | `.btn.small` | 0.92rem = 14.72px / 600 | #0a0a0a |
| Video caption | `.video-item p` | 0.9rem = 14.4px / 400 / 1.5 | #626262 |
| Emphasis | inline `strong` with `color: var(--accent)` | 16px / 700 | #5a4df5 |
| BibTeX | `pre` | 0.95rem = 15.2px / 400 / 1.65 | #ffffff base, spans as listed |
| Footer | `.site-footer p` | 16px / 400 | #626262 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Venue pill | 9999px | 1px #5a4df5 | `0 6px 20px rgba(107, 92, 255, 0.12)` |
| Buttons | 12px | 1px #e6e6e6 (hover #d5d5d5) | none; hover `0 6px 18px rgba(0,0,0,.06)` |
| Primary button | 12px | 1px #5a4df5 (hover #8b82ff) | `0 6px 18px rgba(107, 92, 255, 0.08)`; hover `0 8px 24px rgba(107, 92, 255, 0.15)` |
| Hero video | 10px (video and wrapper) | none | none |
| Result video card | 14px (`--rad`) | 0px | `0 6px 24px rgba(0,0,0,.08)` |
| BibTeX block | 12px | none | `0 6px 18px rgba(0,0,0,.12)` |
| Sections | 0 | 1px #e6e6e6 top | none |

Header glass: `background: rgba(255,255,255,.85); backdrop-filter: saturate(180%) blur(8px)`.

## Layout Metrics

- **Container**: `.container { max-width: 960px; margin: 0 auto; padding: 0 32px }`. At 1440 the column sits at x=240–1200. Only the header nav keeps the 32px side padding; `.hero` (56px 0 22px) and `.section` (36px 0) override it, so hero and section content run the full 960px.
- **Hero**: padding 56px 0 22px; rendered from y=61 to y=894 (833px).
- **Sections**: padding 36px 0 with a 1px #e6e6e6 top border; h2 sits 37px below the rule (y=931 for Abstract). Abstract section 424px tall, Key Results 1,011px, Citation 378px.
- **Paragraphs**: 16px margins, full 960px measure (about 120 characters per line).
- **Video grid**: `grid-template-columns: repeat(2, 1fr)`, gap 2rem = 32px, margin-top 1.5rem = 24px; cards 464×261 (aspect-ratio 16/9, `object-fit: cover`), 12px under each card before the caption.
- **BibTeX**: full 960px, padding 14px 16px, followed by a centred small "Copy BibTeX" button 12px below.
- **Footer**: full-width 1px top rule, padding 26px 0, margin-top 36px, centred muted line.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1200px | nav 32px; hero and sections 0 inside 960px | 16px | 44px | 2-column video grid |
| 1025–1200px | `.container` padding 0 48px wins the cascade, so hero and sections lose their vertical padding (rendered `0px 48px` at 1100) | 16px | 44px | paragraphs, h2, videos and pre get 8px side margins |
| 769–1024px | `.container` 0 36px (sections render `0px 36px`); `.hero` restored to 48px 0 24px | 16px | 4.2vw (37.8px at 900) | video grid gap 1.5rem; h3 1.05rem; buttons padding 11px 16px |
| ≤768px | — | 16px | clamp | video grid 1 column, gap 1.5rem; links in a dropdown panel (480–768px: wrapped lilac pills instead) |
| ≤640px | 20px; hero 32px 0 20px; sections 28px 0 | 15.2px paragraphs | clamp(1.6rem, 6vw, 2rem) | hamburger menu; buttons min 140px, max 180px, padding 12px 16px |
| ≤480px | 20px | 15.2px | clamp | buttons two per row |
| ≤400px | 16px; hero 20px 0 16px | 15.2px | clamp(1.4rem, 7vw, 1.8rem) | pre 0.8rem |

## Components

- **Venue pill** (`.venue-badge`): inline-flex, gap 10px, padding 8px 14px, radius 9999px, fill rgba(107,92,255,0.08), 1px #5a4df5 border, shadow `0 6px 20px rgba(107, 92, 255, 0.12)`; text 16px #5a4df5 with the conference name in 700 and " · city, country" in 400; `white-space: nowrap`.
- **Button** (`.btn`): inline-flex centred, gap 10px, min-width 120px, height 48px, padding 10px 14px, radius 12px, #ffffff fill, 1px #e6e6e6 border, 16px/600 #0a0a0a; optional 22×22 icon on the left (PDF glyph, chart icon, play icon; the X button is icon only). Hover: translateY(-1px), border #d5d5d5, shadow `0 6px 18px rgba(0,0,0,.06)`; transition .12s ease.
- **Primary button** (`.btn.primary`): same shape, text and icon #5a4df5, border #5a4df5, shadow `0 6px 18px rgba(107, 92, 255, 0.08)`; hover border #8b82ff and shadow `0 8px 24px rgba(107, 92, 255, 0.15)`. Only the Paper button gets it.
- **Sticky glass header**: 60px nav row, white at 85% with saturate(180%) blur(8px), 1px #e6e6e6 bottom rule; text links hover to #5a4df5.
- **Video card** (`.video-item`): Fraunces 17.6px/700 title, 12px gap, 16:9 video in a white wrapper with 14px radius and `0 6px 24px rgba(0,0,0,.08)`, 12px gap, 14.4px/1.5 #626262 caption.
- **BibTeX block** (`pre`): #0b0b0b, radius 12px, padding 14px 16px, 15.2px monospace, shadow `0 6px 18px rgba(0,0,0,.12)`; entry type #9d96ff 600, key #c4bfff 500, field names #b8b5ff, values #e8e8e8, punctuation #888888. Horizontal overflow scrolls.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header / nav | yes | translucent white bar, text wordmark left, four text links right |
| Title / authors / affiliation | yes | Fraunces title, Inter 600 authors joined by middots, muted lab line |
| Venue badge | yes | lilac pill with violet border and soft violet glow |
| Teaser | yes | wide autoplay video, borderless on white |
| Link buttons | yes | white outlined buttons, Paper in violet |
| Abstract | yes | h2 plus one full-width paragraph with the method name in bold violet |
| Video results | yes | 2×2 grid of shadowed 16:9 cards with serif titles and muted captions |
| BibTeX | yes | black block with violet syntax colouring and a copy button |
| Footer | yes | centred muted copyright line under a full-width rule |
| Results table | absent from the source | — |
| Method figure | absent from the source | the hero video stands in for it |
| Code link | absent from the source | a commented-out "Resources" section exists in the markup but does not render |

## Adapting to Other Content

- **More authors**: keep the 16.96px/600 middot line with balanced wrapping; at 960px it fits about eight names per line. Put affiliations in the single 16px #626262 lab line, using superscript numbers rather than a second line style.
- **A results table**: place it inside a section at the full 960px; header row in Inter 600 #0a0a0a over a 1px #e6e6e6 rule, body 16px/400, best value in 700 #5a4df5 like the method name. No fills or zebra stripes.
- **More videos**: extend the 2-column grid (464px cards at 1440, 32px gap); each card keeps the Fraunces 17.6px title and a 14.4px muted caption.
- **Long publication or news lists**: a list at 16px/1.65 with dates in 600 #0a0a0a and links in #5a4df5; separate groups with the 1px #e6e6e6 section rule, not cards.
- **A method figure**: use the hero-figure treatment (full 960px, 10px radius, no border) so it blends with white.

## Do's and Don'ts

- Do set every heading in Fraunces 700 and every other text in Inter; the serif/sans contrast is the identity.
- Do keep #5a4df5 rare: the venue pill, one primary button, the method name and links.
- Do separate sections with 1px #e6e6e6 top rules and 36px padding, not background bands.
- Do keep teaser media borderless on white so it merges with the page.
- Don't fill buttons with violet; even the primary button is white with a violet outline.
- Don't add a second accent colour; the BibTeX block's lilac tints are the only variation.
- Don't let the column exceed 960px or add side gutters inside it at desktop width.

## Surfaces

Pure white page; a white-at-85% blurred header; white buttons and video wrappers lifted only by soft shadows (`0 6px 24px rgba(0,0,0,.08)` for videos); a translucent lilac fill on the venue pill; one black surface, the BibTeX block (#0b0b0b).

## Imagery

Real-world footage of a Unitree A1 quadruped on a grey and black foam-tile floor. The hero video crops four clips into capsule shapes around a red-yellow-blue scatter plot, all on white. Result videos are plain 16:9 recordings with native controls. No photos of people, no illustrations, no logos except the X glyph and small line icons in the buttons.

## Layout

One centred 960px column: sticky 61px header, centred hero (title, authors, lab, pill, video, buttons), then Abstract, Key Results and Citation sections separated by hairline rules, and a centred footer. Generous white space comes from section padding and the narrow column rather than from large gaps between items.

## Agent Prompt Guide

Quick colors: page #ffffff, ink #0a0a0a, muted #626262, rule #e6e6e6, accent #5a4df5, hover accent #8b82ff, code #0b0b0b.

1. "Build a centred hero in a 960px column with padding 56px 0 22px: Fraunces 44px/700 title, line-height 1.12, #0a0a0a, balanced wrap; Inter 16.96px/600 #151515 authors joined by ' · '; 16px #626262 lab line; a venue pill with padding 8px 14px, radius 9999px, background rgba(107,92,255,0.08), 1px #5a4df5 border, 16px #5a4df5 text (conference 700, location 400), shadow 0 6px 20px rgba(107,92,255,0.12)."
2. "Make a button row: centred flex, gap 10px; each button min-width 120px, padding 10px 14px, radius 12px, #ffffff, 1px #e6e6e6 border, Inter 16px/600 #0a0a0a with a 22px icon on the left; hover translateY(-1px), border #d5d5d5, shadow 0 6px 18px rgba(0,0,0,.06). The first button is primary: text and border #5a4df5, shadow 0 6px 18px rgba(107,92,255,0.08), hover border #8b82ff."
3. "Create a 2-column video grid with a 32px gap: each item has a Fraunces 17.6px/700 #0a0a0a title, 12px gap, a 16:9 video in a #ffffff wrapper with radius 14px and shadow 0 6px 24px rgba(0,0,0,.08), then a 14.4px/1.5 #626262 caption. Sections above and below have a 1px #e6e6e6 top border and 36px vertical padding."

## Similar Pages

- Hand-built single-file project pages that pair a Google serif display face with Inter body text and one accent colour.
- Robotics project pages that put a blended video teaser directly under the venue pill and a short row of outlined link buttons.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --ink: #0a0a0a;
  --muted: #626262;
  --rule: #e6e6e6;
  --accent: #5a4df5;
  --accent-2: #8b82ff;
  --pill-bg: rgba(107, 92, 255, 0.08);
  --code-bg: #0b0b0b;
  --font-body: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-display: "Fraunces", Georgia, "Times New Roman", serif;
  --max: 960px;
  --rad: 14px;
  --btn-radius: 12px;
}
body { font-family: var(--font-body); color: var(--ink); background: var(--bg); line-height: 1.65; }
h1, h2, h3 { font-family: var(--font-display); }
h1 { font-size: clamp(2rem, 4.2vw, 2.75rem); line-height: 1.12; text-wrap: balance; }
```

## Provenance

- **URL**: https://adaptive-intelligent-robotics.github.io/URSA/
- **Paper**: From Tabula Rasa to Emergent Abilities: Discovering Robot Skills via Real-World Unsupervised Quality-Diversity (arXiv 2508.19172), Luca Grillotti, Lisa Coiffard, Oscar Pang, Maxence Faldor, Antoine Cully (Adaptive & Intelligent Robotics Lab, Imperial College London).
- **Venue**: CoRL 2025, Seoul.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and the abstract links this project page.
- **Template credit**: none stated; a hand-written page with its own `styles.css` design tokens and `script.js`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes at 1440, 1100 and 900px, the 1440×900 and full-page screenshots, and `styles.css` and `index.html` read directly, on 2026-10-28.
