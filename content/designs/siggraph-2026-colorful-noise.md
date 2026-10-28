# Colorful-Noise — Style Reference

> A painter's studio on linen paper: a rainbow ribbon across the top, a spectrum-dipped wordmark, and handwritten labels pinned beside every picture.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and tall screenshots, and the page's inline `<style>` block and markup in `index.html`. Author chip colors are set by inline `style` attributes, not by the `.author` rule, and were read from the markup. Hero blocks use a `fadeUp` animation (0.6s, 0.1–0.4s delays); the values below are the settled state.

## Overview

A warm, crafted page on linen off-white #faf9f7 with near-black brown ink #1a1816. A 4px eight-stop spectrum bar runs across the very top, and the same spectrum colours the "Colorful-Noise:" part of the title through gradient-clipped text. Typography pairs DM Serif Display (wordmark, h1, h2, h3) with DM Sans for everything else, and Caveat handwriting for labels inside figures and gallery prompts. The hero is left-aligned for the venue pill and title, then centres the pastel author chips, a lab logo block, and a button row. A soft white teaser card with a 16px radius follows. Sections are separated only by 1px #ede9e2 rules and open with a small uppercase rust kicker preceded by a 24×3px spectrum dash. The memorable module is the radial "bear" diagram: a low-frequency colour prior and an edge map in the centre with generated animals fanned around them on thin curved connectors in blue and purple.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): linen off-white family #faf9f7 / #faf9f1 / #faf9f8 / #f8f9f7 / #fcf9f5 together 62.6%; slate #585a62 15.3% (noise tiles, scribble and photo content in the teaser plus the dark buttons); warm beige #ebe8e3 14.3% (the teaser's #f0ece6 image ground and borders); white #fefefd 7.9% (header and button fills). The spectrum bar and title gradient are too thin to form clusters.

Anatomy in DOM order (desktop 1440px; content column x=120 to 1320):

1. **Spectrum bar** (0–4px): `background: linear-gradient(90deg, var(--c1), var(--c2), var(--c3), var(--c4), var(--c5), var(--c6), var(--c7), var(--c8))`, i.e. #e05a5a → #e07b3a → #d4b84a → #5bab6e → #4a9ab5 → #5a6bbf → #8b5bbf → #c45aad.
2. **Sticky header** (`header`, y=4–61): #ffffff, 1px #e2ddd6 bottom border; inner `.container.header-inner` max 1280px with 40px side padding, height 56px. Left "Colorful-Noise" in DM Serif Display 20px/400 #1a1816, letter-spacing -0.02em; right nav links Motivation, Method, Results, Applications, BibTeX at 13px/400 #6b6560, padding 6px 12px, radius 6px, gap 4px; hover fill #f0ece6, text #1a1816.
3. **Hero** (`.hero`, padding 64px 0 56px), starting y=125.
4. **Venue pill** (`.venue-badge`, y≈125, 38px tall, left-aligned): 16px SIGGRAPH logo, "SIGGRAPH 2026" 14px/600 uppercase, letter-spacing 0.04em, #8f3619 on `linear-gradient(135deg, #fff3e0, #fce4ec)`, 1px #f5c6a0 border, 20px radius, padding 6px 16px, shadow `0 2px 8px rgba(200,80,42,0.12)`. Gap 20px.
5. **Title** (`h1`, y=183, three lines, left-aligned): DM Serif Display 50px (clamp(28px, 3.5vw, 50px)), line-height 1.15, letter-spacing -1px, #1a1816; computed weight 700 is synthesised from the single 400 file, so strokes render faux-bold. "Colorful-Noise:" uses `background: linear-gradient(90deg, var(--c1), var(--c3), var(--c5), var(--c7))` clipped to text. Gap 32px.
6. **Author chips** (y=388, centred, gap 8px): pills with 15px/500 #1a1816 text, padding 4px 14px, 20px radius; per-author inline colours pink #fce8e4 / border #e09484, green #e4f2e4 / #82bc82, blue #e4ecfa / #7fa4d8. Gap 10px + 10px.
7. **Lab block** (`.affil-row`, y=446–551, centred): 96px Canvas Lab hoopoe logo (opacity 0.9, margin-top 12px), a 1×52px #e2ddd6 divider, then "Canvas Lab" 19px/600 #1a1816 over "Reichman University" 15px #6b6560. Gap 24px.
8. **Button row** (`.links`, y=575, 40px tall, centred, gap 10px): two dark primaries "Paper (Arxiv)" and "Paper (PDF)" (#1a1816 fill, #faf9f7 text), then white Code, Colorful Sketches Dataset, Video. 15px stroke icons left. Gap 36px + 16px.
9. **Teaser card** (`.teaser-panel`, y=667, 1200px wide): white, 1px #e2ddd6, 16px radius, shadow `0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.04)`; inner image on #f0ece6 with Caveat column headings drawn into the figure; italic 13px #a09b94 caption below a 1px #ede9e2 rule.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Linen | #faf9f7 | --bg | page background, primary button text, legend strip |
| White | #ffffff | --surface | header, buttons, teaser/overview/diagram cards |
| Border | #e2ddd6 | --border | header rule, button borders, card borders, affiliation divider, footer rule |
| Border Soft | #ede9e2 | --border-soft | section top rules, caption rules, gallery dividers |
| Ink | #1a1816 | --text | body text, title, headings, primary buttons, BibTeX box |
| Muted | #6b6560 | --text-muted | nav links, body copy, affiliation institution, handwritten labels |
| Faint | #a09b94 | --text-faint | captions, footer, footnotes, toggle labels |
| Rust | #c8502a | --accent | section kickers, insight callout bar, "Result" toggle pill, footnote markers |
| Rust Wash | #f5ede9 | --accent-light | motivation and insight callout fills |
| Rust Dark | #8f3619 | --accent-dark | venue pill text, callout text, author hover text |
| Sand | #f0ece6 | --tag-bg | nav hover, button hover, teaser image ground, inactive toggle pill |
| Venue Border | #f5c6a0 | (literal) | venue pill border |
| Venue Peach | #fff3e0 | (literal) | venue pill gradient start |
| Venue Pink | #fce4ec | (literal) | venue pill gradient end |
| Spectrum Red | #e05a5a | --c1 | spectrum bar, title gradient start, kicker dash start |
| Spectrum Orange | #e07b3a | --c2 | spectrum bar |
| Spectrum Gold | #d4b84a | --c3 | spectrum bar, title gradient |
| Spectrum Green | #5bab6e | --c4 | spectrum bar |
| Spectrum Teal | #4a9ab5 | --c5 | spectrum bar, title gradient, low-frequency card labels |
| Spectrum Indigo | #5a6bbf | --c6 | spectrum bar |
| Spectrum Violet | #8b5bbf | --c7 | spectrum bar, title gradient end, high-frequency card labels |
| Spectrum Magenta | #c45aad | --c8 | spectrum bar end |
| Author Pink | #fce8e4 / #e09484 | (inline) | first author chip fill / border |
| Author Green | #e4f2e4 / #82bc82 | (inline) | second author chip fill / border |
| Author Blue | #e4ecfa / #7fa4d8 | (inline) | third author chip fill / border |
| LF Blue | #2271a3 / #dff0f7 / #b8d9ea | (literal) | "Low-frequency outputs" pill text / fill / border; LF card borders |
| HF Purple | #6139a8 / #ede5f7 / #d8cef0 | (literal) | "High-frequency outputs" pill text / fill / border; HF card borders |
| BibTeX Text | #c8c3ba | (literal) | BibTeX code text on #1a1816 |
| BibTeX Field | #8ab4f8 | (literal) | BibTeX field names |
| Hover Border | #ccc9c2 | (literal) | secondary button border on hover |
| Hover Dark | #333333 | (literal) | primary button fill on hover |
| Copy Gray | #aaaaaa | (literal) | BibTeX copy button text |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'DM Serif Display', Georgia, serif | DM Serif Display 400 only; h1–h3 compute weight 700 and are synthesised bold | Abril Fatface at 400 |
| Body / UI | 'DM Sans', sans-serif | DM Sans 300 italic, 400, 500 (600 snaps to 500) | Outfit |
| Handwriting | 'Caveat', cursive | Caveat 500, 600 | Kalam |
| Code | 'Courier New', monospace | system Courier New | Courier Prime |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1` | clamp(28px, 3.5vw, 50px) → 50px / 700 (synthetic) / 1.15, letter-spacing -1px | #1a1816, spectrum on `span.rainbow` |
| Section heading | `h2` | clamp(22px, 3vw, 30px) → 30px / 700 (synthetic) / 1.2, letter-spacing -0.6px | #1a1816 |
| Subsection | `.gallery-section-title`, `.app-subsection-title` | clamp(18px, 2.2vw, 24px) → 24px / 1.25 | #1a1816 |
| Header logo | `.header-logo` | 20px / 400, letter-spacing -0.02em | #1a1816 |
| Body | `body` | 16px / 400 / 1.7 | #1a1816 |
| Body copy | `.body-text`, `.hero-abstract` | 15px / 1.8 (abstract 1.85) | #6b6560 |
| Section kicker | `.section-tag` | 11px / 500 uppercase, letter-spacing 0.1em | #c8502a |
| Venue pill | `.venue-badge` | 14px / 600 uppercase, letter-spacing 0.04em | #8f3619 |
| Author chip | `.author` | 15px / 500 | #1a1816 |
| Nav link, button | `nav a`, `.btn` | 13px / 400 (nav), 500 (button) | #6b6560 / #1a1816 |
| Caption | `.teaser-caption` | 13px italic / 1.6 | #a09b94 |
| Handwritten label | `.toggle-card-label`, `.toggle-row-prompt` | Caveat 18–19px / 500 | #6b6560 |
| Callout | `.motivation-highlight`, `.freq-insight` | 14px / 1.7 | #8f3619 |
| BibTeX | `.bibtex-box` | Courier New 13px / 1.7 | #c8c3ba |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Teaser, overview, diagram, video cards, BibTeX box | 16px | 1px #e2ddd6 (BibTeX none) | `0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.04)` |
| Buttons | 8px | 1px #e2ddd6 (primary #1a1816) | none; hover translateY(-1px) |
| Nav links, copy button | 6px | copy 1px rgba(255,255,255,0.12) | none |
| Venue pill, author chips, frequency pills | 20px | 1px colored borders | venue `0 2px 8px rgba(200,80,42,0.12)`; author hover `0 2px 8px rgba(200,80,42,0.1)` |
| Toggle indicator, gti pills | 100px | 1px #e2ddd6 | card shadow |
| Callouts | 0 10px 10px 0 | 3px #c8502a left | none |
| Condition cards (radial diagram) | 12px | 2.5px #b8d9ea or #d8cef0 | card shadow |
| Output cards (radial diagram) | 8px | 1.5px #b8d9ea or #d8cef0 | `0 1px 4px rgba(0,0,0,.05)`; hovered `0 20px 50px rgba(0,0,0,.22)` with scale 1.72 |
| Gallery tiles | 4px | none | none; hover image scale 1.025 |

Kicker dash: `.section-tag::before` is 24×3px, radius 2px, `background: linear-gradient(90deg, var(--c1), var(--c5), var(--c7))`.

## Layout Metrics

- **Container**: `.container { max-width: 1280px; padding: 0 40px }`, so content runs x=120 to 1320 (1200px) at 1440.
- **Hero**: padding 64px 0 56px; headline block margin-bottom 32px; teaser card margin-top 16px; abstract paragraph margin-top 36px.
- **Sections**: padding 56px 0 with a 1px #ede9e2 top border; h2 margin-bottom 20px; kicker margin-bottom 10px.
- **Galleries**: `.toggle-grid` 5 or 4 equal columns with 6px gaps, square tiles; subsection blocks 48px apart; gallery dividers 48px margin.
- **Radial diagram**: `.freq-stage` 680px tall, condition cards 160px wide, output cards 148px wide placed absolutely around them with SVG connectors.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | 40px | 16px | 50px (3.5vw caps at 50px from 1429px) | 4–5 column galleries; nav visible |
| ≤900px | 20px | 16px | 3.5vw ≈ 31.5px at 900 | galleries 3 columns; nav hidden; diagram padding 18px 16px 16px |
| ≤768px | 20px | 16px | 28px floor below 800px | radial diagram becomes stacked groups with 3-column output grids; pills hidden |
| ≤560px | 20px | 16px | 28px | galleries 2 columns |
| ≤420px | 20px | 16px | 28px | mobile output grids 2 columns |

## Components

- **Spectrum bar**: 4px full-width strip, eight-stop 90deg gradient from #e05a5a to #c45aad, above the sticky header.
- **Venue pill** (`.venue-badge`): inline-flex, gap 8px, 16px logo, 14px/600 uppercase #8f3619, letter-spacing 0.04em, padding 6px 16px, radius 20px, `background: linear-gradient(135deg, #fff3e0, #fce4ec)`, 1px #f5c6a0, shadow `0 2px 8px rgba(200,80,42,0.12)`.
- **Author chip** (`.author`): 15px/500 #1a1816, padding 4px 14px, radius 20px, 1px border; pastel fill and matching border per author (pink #fce8e4/#e09484, green #e4f2e4/#82bc82, blue #e4ecfa/#7fa4d8). Hover: border #c8502a, text #8f3619, shadow `0 2px 8px rgba(200,80,42,0.1)`.
- **Lab block** (`.affil-row`): 96px logo, 1×52px #e2ddd6 divider, name 19px/600, institution 15px #6b6560, gap 14px.
- **Button** (`.btn`): inline-flex, gap 7px, 13px/500 DM Sans, padding 8px 16px, radius 8px, 1px #e2ddd6, #ffffff, 15px stroke icon. Hover: #f0ece6, border #ccc9c2, translateY(-1px). Primary: #1a1816 fill and border with #faf9f7 text, hover #333333.
- **Section kicker** (`.section-tag`): 11px/500 uppercase #c8502a, letter-spacing 0.1em, led by a 24×3px spectrum dash, gap 8px.
- **Callout** (`.motivation-highlight`): #f5ede9 fill, 3px #c8502a left border, radius 0 10px 10px 0, padding 14px 18px, 14px #8f3619.
- **Input/result toggle** (`.global-toggle-indicator`): white capsule, 1px #e2ddd6, radius 100px, card shadow; "Input" pill #1a1816 on, "Result" pill #c8502a when results show; 12px/600 uppercase pills, padding 4px 14px. Gallery tiles cross-fade input to result over 0.55s.
- **Radial frequency diagram**: two 160px condition cards (white, 12px radius, 2.5px blue or purple border, uppercase 11px/600 footer in #4a9ab5 or #8b5bbf) with 148px output cards around them; hover blurs others (blur 4px, opacity 0.15) and scales the hovered card 1.72 with a dark Caveat prompt bubble (rgba(26,24,22,0.92), 10px radius).
- **BibTeX** (`.bibtex-box`): #1a1816, 16px radius, padding 24px 28px, Courier New 13px #c8c3ba, keywords #c8502a, fields #8ab4f8; copy button top-right 11px #aaaaaa on rgba(255,255,255,0.08).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky nav | yes | white bar under a 4px spectrum strip, serif logo, 13px muted links |
| Venue badge | yes | peach-to-pink gradient pill with SIGGRAPH logo |
| Title / authors | yes | left-aligned serif title with spectrum prefix; centred pastel author chips |
| Affiliations | yes | lab logo block with divider |
| Link buttons | yes | two dark primaries and three white outline buttons |
| Teaser | yes | 16px-radius white card, Caveat labels inside the figure, italic caption |
| Abstract | yes | 15px muted paragraph under a kicker, directly after the teaser |
| Motivation diagram | yes | interactive radial bear diagram with LF/HF pills |
| Method overview | yes | overview card with caption |
| Results gallery | yes | input/result toggle grids with Caveat prompts |
| Applications | yes | subsections with galleries and footnotes |
| Video | present but non-standard | only a "Video" link button; no embedded player in the render |
| Results tables | absent from the source | all results are image grids |
| BibTeX | yes | dark 16px-radius code box with colored fields |
| Footer | yes | 13px #a09b94 line with 1px #e2ddd6 top rule |

## Adapting to Other Content

- **More authors**: keep chips at 15px/500 with 4px 14px padding and continue the pastel cycle with the spectrum hues at low tint (e.g. a violet chip at #ede5f7 / #d8cef0); wrap centred with 8px gaps.
- **A results table**: put it in a white 16px-radius card with the card shadow; header row 11px/500 uppercase #c8502a, body 15px #6b6560, 1px #ede9e2 row rules, best value 600 #1a1816.
- **Long publication or news lists**: use rows of 15px #6b6560 text with a 11px/500 uppercase #c8502a date, separated by 1px #ede9e2 rules at 56px section padding.
- **More applications**: repeat `.app-subsection` blocks (24px serif titles, 14px #6b6560 descriptions, 48px apart) with Caveat captions on figures.

## Do's and Don'ts

- Do keep the spectrum to three places: the 4px top bar, the title prefix, and the 24×3px kicker dashes.
- Do use Caveat only inside figures and gallery labels; it is the hand-made voice of the results.
- Do keep surfaces white on linen with 16px radii and the faint two-layer shadow.
- Do use rust #c8502a for kickers and active states only.
- Don't colour body text or headings with the spectrum hues.
- Don't center the title; only the authors, lab block and buttons are centred.
- Don't add borders between sections other than the 1px #ede9e2 rule.

## Surfaces

Linen #faf9f7 page; white #ffffff header and cards with 1px #e2ddd6 borders and the soft shadow; sand #f0ece6 behind figure images; rust-wash #f5ede9 callouts with a 3px rust bar; a single dark #1a1816 BibTeX box near the end.

## Imagery

Square diffusion outputs (landscapes, animals, dragons, cats) beside their low-frequency colour scribbles and noise tiles. Figures are drawn with Caveat handwriting and brush arrows, giving a sketchbook feel. Gallery tiles are square with 4px radii and cross-fade between the colour prior and the generated image.

## Layout

A 1200px column at 1440: left-aligned hero title over centred author chips, lab block and buttons, then a full-width teaser card, an abstract, and four sections (Motivation, Method, Results, Applications) plus Citation, each 56px padded with a top hairline. Galleries are 4–5 columns. About 12,200px tall.

## Agent Prompt Guide

Quick colors: page #faf9f7, surface #ffffff, text #1a1816, muted #6b6560, faint #a09b94, border #e2ddd6, accent #c8502a (dark #8f3619, wash #f5ede9), spectrum #e05a5a #d4b84a #4a9ab5 #8b5bbf.

1. "Build a hero on #faf9f7 under a 4px bar with linear-gradient(90deg, #e05a5a, #e07b3a, #d4b84a, #5bab6e, #4a9ab5, #5a6bbf, #8b5bbf, #c45aad). Left-aligned venue pill: 14px/600 uppercase #8f3619 on linear-gradient(135deg, #fff3e0, #fce4ec), 1px #f5c6a0, radius 20px, padding 6px 16px. Title in DM Serif Display 50px/1.15, letter-spacing -1px, #1a1816, with the method name filled by linear-gradient(90deg, #e05a5a, #d4b84a, #4a9ab5, #8b5bbf) clipped to text."
2. "Make centred author chips: DM Sans 15px/500 #1a1816, padding 4px 14px, radius 20px, 1px border, fills #fce8e4 / #e4f2e4 / #e4ecfa with borders #e09484 / #82bc82 / #7fa4d8; hover border #c8502a, text #8f3619."
3. "Create a section: padding 56px 0, 1px #ede9e2 top border; kicker 11px/500 uppercase #c8502a, letter-spacing 0.1em, with a 24×3px gradient dash (#e05a5a, #4a9ab5, #8b5bbf); h2 DM Serif Display 30px; body 15px/1.8 #6b6560; figure in a white card with 1px #e2ddd6, radius 16px, shadow 0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.04)."

## Similar Pages

- Hand-built image-generation project pages that use a topic-coloured gradient wordmark and handwritten figure labels.
- Warm off-white pages pairing DM Serif Display headings with DM Sans body and pastel author chips.

## Quick Start

```css
:root {
  --bg: #faf9f7;
  --surface: #ffffff;
  --border: #e2ddd6;
  --border-soft: #ede9e2;
  --text: #1a1816;
  --text-muted: #6b6560;
  --text-faint: #a09b94;
  --accent: #c8502a;
  --accent-light: #f5ede9;
  --accent-dark: #8f3619;
  --tag-bg: #f0ece6;
  --c1: #e05a5a; --c2: #e07b3a; --c3: #d4b84a; --c4: #5bab6e;
  --c5: #4a9ab5; --c6: #5a6bbf; --c7: #8b5bbf; --c8: #c45aad;
  --radius: 10px;
  --radius-lg: 16px;
  --shadow: 0 1px 3px rgba(0,0,0,0.07), 0 4px 16px rgba(0,0,0,0.04);
  --font-display: 'DM Serif Display', Georgia, serif;
  --font-body: 'DM Sans', sans-serif;
  --font-hand: 'Caveat', cursive;
}
```

## Provenance

- **URL**: https://nadavc220.github.io/colorful-noise/
- **Paper**: Colorful-Noise: Training-Free Low-Frequency Noise Manipulation for Color-Based Conditional Image Generation (arXiv 2605.00548), Nadav Z. Cohen, Ofir Abramovich, Ariel Shamir.
- **Venue**: SIGGRAPH 2026 Conference Paper (as listed in the arXiv comment).
- **Selection reason**: the arXiv comment lists the venue as SIGGRAPH 2026 Conference Paper without an explicit acceptance word and links this project page.
- **Template credit**: none stated; a custom single-file build; footer reads "© 2026 Cohen, Abramovich & Shamir".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, and the inline CSS and markup of `index.html` read directly, on 2026-10-28.
