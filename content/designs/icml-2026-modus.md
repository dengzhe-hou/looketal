# MODUS — Style Reference

> A mint-glass display case in front of a slowly sliding wall of depth maps, edge maps and photos, with one navy pill at the centre of an orbit.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, two scrolled captures of the body, extra computed-style queries on hero and section elements, and the page's inline `<style>` blocks on top of Bulma 0.9.4. Several hero sizes are set in `vh`, so they depend on viewport height; values below are for a 900px-tall window.

## Overview

A Bulma/Nerfies-lineage page rebuilt into an editorial, interactive site. A plain light-gray Bulma navbar lists ten sections. The hero fills the viewport on pale mint (#e8f3ee) behind a horizontally drifting mosaic of modality tiles (RGB photos, depth, normals, segmentation, edges, caption text, feature-map pies) at 42% opacity under a mint fade. A frosted mint card (18px radius, 14px blur) holds the title, with "MODUS" in a navy Space Grotesk wordmark, a gray "ICML 2026" line, three lines of teal author names, a row of six institution logos, footnotes and six charcoal Bulma pill buttons. Below the card, an orbit of white modality chips circles a navy "MODUS" pill. The washed-out mosaic lowers contrast around the card. Further down, sections alternate white, warm cream (#f7f4ed) and one deep navy band (#1c2a4a), each opening with a tiny tracked uppercase eyebrow; the TL;DR heading is an italic Cormorant Garamond serif in teal, and teal (#2c5d63) and copper (#b86a39) mark the two "experts" throughout.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): mint and sage #e3e8e3 15.0%, #eff5f2 12.5%, #d8eae1 10.7%, #d3dedd 11.0%, #c1cdcb 12.9%; gray-green #bbc0bd 19.6% (faded photo tiles); lavender #d2d1e0 12.8% (faded normal-map tiles); slate #878d8e 5.5% (text, buttons, tile detail). No color reaches full saturation because the mosaic sits at 42% opacity under a mint fade.

Anatomy in DOM order (1440×900):

1. **Navbar** (0–53px): Bulma `navbar is-light`, #f5f5f5; "MODUS" wordmark 17px Space Grotesk 700 #14213d, then TL;DR, Any-to-Any, Method, Chained Prediction, Self-Verification, Representation, Training, Benchmarks, Dataset, BibTeX in Inter 13px rgba(0,0,0,.7), padding 8px 12px, centred in a 960px container.
2. **Hero** (53–974px): `min-height: calc(100vh - 52px)`, #e8f3ee, 1px #cfe3d6 bottom border; mosaic tiles clamp(160px, 15vw, 240px) square with 8px gaps and 6px radii, scrolling left over 70s; fade layer mint at 55% / 30% / 30% / 55%.
3. **Hero card** (y=80, 900×434px, x=270): rgba(232,243,238,.62), blur 14px saturate 118%, 1px rgba(207,227,214,.5) border, 18px radius, shadow 0 16px 44px rgba(20,33,61,.12) plus white inset top line; padding 19.8px 32px 16.2px.
4. **Title** (y=101, two lines, 84px): Inter 36px/700 (clamp(1.4rem, 4vh, 2.4rem)), line-height 1.15, #363636, centred; "MODUS" in Space Grotesk 700 #14213d, letter-spacing -0.01em. Gap 24px.
5. **Venue** (y=209): "ICML 2026", Inter 16px/500 #5c5c5c. Gap 22px.
6. **Authors** (y=255, three lines): Inter 20px/500 #2c5d63, each name nowrap; superscripts #888888 400. 
7. **Affiliation logos** (y=362, 27px row): numbered logos (EPFL, Apple, and four universities and Lambda) with 15.2px #555555 numerals.
8. **Footnotes** (y≈395): "* equal contribution  † equal technical advising" in pale gray.
9. **Buttons** (y=440, 40px): arXiv, Code, Models ▾, Dataset, Demo, Thread; Bulma `button is-dark is-rounded`, #363636 fill, white Inter 16px/500, padding 7px 20px, 9999px radius, Font Awesome or emoji icon left, 0.3rem margins.
10. **Modality orbit** (y=525, 414×414px, centred): two dashed rings (rgba(20,33,61,.18) and .13); centre pill "MODUS" Space Grotesk 700 at 3.2vh (28.8px), letter-spacing 0.06em, white on linear-gradient(145deg, #1c2f52, #14213d 52%, #123a3c), 999px radius; outer chips white with 1px #d6e4dc and 12.5px/500 #14213d labels; inner chips #f7f4ed with #ebe5d6 borders at 11px; teal icons. Rings rotate in opposite directions (40s and 32s); clicking a chip pauses them and lights matching mosaic tiles.

A fixed scroll-spy rail (white 7px-radius cards with dots, active card teal-bordered) is present at the left but stays at opacity 0 until the hero is scrolled past; it is hidden entirely below 1280px.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Mint | #e8f3ee | (literal, `html` and `.publication-hero`) | hero ground, hero card tint at 62%, fade layer, first paint |
| Mint Rule | #cfe3d6 | (literal) | hero bottom border, hero card border at 50% |
| Ink | #1a1a1a | (literal, `body`) | body text |
| Title Charcoal | #363636 | (Bulma) | title, h3 section titles, dark pill buttons |
| Venue Gray | #5c5c5c | (literal) | venue line |
| Navy | #14213d | (literal) | MODUS wordmark, orbit chip labels, active chip fill, h2 method headline |
| Teal | #2c5d63 | --teal | links, author names, TL;DR heading, teal expert, scroll-spy active dot and border |
| Deep Teal | #1f4549 | --teal-d | link hover, scroll-spy group titles |
| Copper | #b86a39 | --warm | copper expert highlights, "separate targets" labels, accents in the method walk |
| Cream | #f7f4ed | (literal) | alternate sections, inner orbit chips, BibTeX and footer background |
| Cream Rule | #ebe5d6 | (literal) | alternate-section and footer hairlines, inner chip borders, inactive rail cards |
| Midnight Band | #1c2a4a | (literal, `#text2any.sec-dark`) | Text → Any section background |
| Band Rule | #2a385a | (literal) | Text → Any section border |
| Seafoam | #8fc7c1 | (literal) | eyebrow and active-chip icon color on the navy band, active chip ring |
| Eyebrow Taupe | #8a8378 | (literal) | `.sec-eyebrow` labels |
| Navbar Gray | #f5f5f5 | (Bulma `is-light`) | navbar background |
| Chip Border | #d6e4dc | (literal) | outer orbit chip borders |
| Code Gray | #4a4a4a | (literal) | BibTeX text |
| Step Ink | #161616 | --ink (`.mw-walk`) | method step headings |
| Step Mute | #74716a | --mute (`.mw-walk`) | method step eyebrows and notes |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text / UI | 'Inter', 'Noto Sans', sans-serif | Inter 400/500/600/700/800 | Manrope |
| Wordmark / method headings | 'Space Grotesk', 'Inter', sans-serif | Space Grotesk 500/600/700 | Archivo |
| Editorial serif | 'Cormorant Garamond', 'Palatino', 'Georgia', serif | Cormorant Garamond 600 italic | EB Garamond Italic |
| Mono | 'Roboto Mono', monospace | Roboto Mono 400/500 | IBM Plex Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title.is-1.publication-title` | clamp(1.4rem, 4vh, 2.4rem) → 36px / 700 / 1.15 | #363636; wordmark #14213d |
| TL;DR heading | `.tldr-title` | clamp(2.3rem, 4.4vw, 3.2rem) → 51.2px / 600 italic / 1.0, Cormorant Garamond | #2c5d63 |
| Method headline | `#method h2.title.is-3` | Space Grotesk 42px / 700 / 1.18, letter-spacing -0.018em, max 820px | #14213d |
| Method step heading | `.mw-walk h2` | Space Grotesk 28px / 700 / 1.2 | #161616 |
| Section title | `.title.is-4` | Inter 24px / 600 / 1.125 | #363636 (white on the navy band) |
| Eyebrow | `.sec-eyebrow` | 11px / 600 uppercase, letter-spacing 0.22em | #8a8378 (#8fc7c1 on navy) |
| Step eyebrow | `.mw-walk .eyebrow` | Roboto Mono 11.5px uppercase, 0.22em | #74716a |
| Body | `.content p`, `.content li` | Inter 16px / 1.7 | #1a1a1a |
| Authors | `.publication-authors` | Inter 20px / 500 | #2c5d63 |
| Venue | `.publication-venue` | 16px / 500 | #5c5c5c |
| Button | `.button.is-rounded` | Inter 16px / 500 | #ffffff |
| Nav links | `.navbar-item` | Inter 13px | rgba(0,0,0,.7) |
| Caption | `.mini-fig figcaption` | 0.82rem | #777777 |
| Table header | `table.results th` | 16px / 600 | #444444 |
| Code / BibTeX | `pre.bibtex`, `code` | Roboto Mono 12.5px / 1.55 | #4a4a4a; inline code Bulma red #da1039 on #f5f5f5 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero card | 18px (14px ≤768px) | 1px rgba(207,227,214,.5) | 0 16px 44px rgba(20,33,61,.12), inset 0 1px 0 white at 55% |
| Hero buttons | 9999px | transparent | none |
| Orbit centre pill | 999px | 1px white at 16% | 0 12px 32px rgba(20,33,61,.3), 0 0 0 7px teal at 7% |
| Orbit chips | 999px | 1px #d6e4dc (inner #ebe5d6) | 0 3px 12px rgba(20,33,61,.08); active 0 6px 22px navy at 35% + 3px seafoam ring |
| Mosaic tiles | 6px | none | hover 0 0 0 2px #14213d + seafoam glow |
| TL;DR card | 10px | 1px rgba(44,93,99,.1) | none; fill rgba(44,93,99,.035) |
| Scroll-spy cards | 7px | 1px #ebe5d6 (active #2c5d63) | active 0 2px 14px teal at 18% |
| BibTeX | 4px | none | none |
| Image tiles in the navy band | about 8px | none | soft dark shadow |

## Layout Metrics

- **Containers**: Bulma `container is-max-desktop` (960px; x=240 at 1440) for nav and content; hero card max 900px; method headline max 820px.
- **Hero**: full viewport minus the navbar; card padding clamp(0.9rem, 2.2vh, 2rem) clamp(1.4rem, 3vw, 2rem) clamp(0.7rem, 1.8vh, 1.6rem); orbit `width: clamp(320px, min(46vh, 76vw), 540px)` with ring radii clamp(130px, 18.5vh, 215px) and clamp(85px, 13.5vh, 140px).
- **Sections**: `.section { padding: 4rem 1.5rem }` (64px 24px); the checkpoints section uses 8px 24px 64px; method steps sit 6rem apart.
- **TL;DR card**: full 960px, padding 28px 36px, two columns (text left, diagram right).
- **Wide modules**: the chained / independent prediction comparison and the any-to-any grid break out to the page width (about 1424px); the Text → Any band uses a two-column layout with a large output on the left and a 2×3 grid of modality outputs on the right.
- **Tables**: centred, cells padding 8.8px 9.6px.
- **Footer**: cream, padding 40px 24px, 1px #ebe5d6 top border.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1280px | 24px; 960px container | 16px | 4vh (36px at 900 tall) | scroll-spy rail available after the hero |
| ≤1280px | 24px | 16px | 4vh | scroll-spy rail removed |
| ≤900px | 24px | 16px | 4vh | several two-column modules stack |
| ≤768px | 24px | 16px | clamp(1.2rem, 3.4vh, 1.7rem) | hero card padding 1.4rem 1.2rem 1rem, radius 14px; orbit fixed at 370px with smaller chips; TL;DR heading 1.9rem |
| ≤640px | 24px | 16px | as above | modality grids 4 columns; expert cards 1 column |

## Components

- **Frosted hero card** (`.hero-card`): background rgba(232,243,238,.62), `backdrop-filter: blur(14px) saturate(118%)`, 1px rgba(207,227,214,.5), radius 18px, max-width 900px, shadow 0 16px 44px rgba(20,33,61,.12) and inset white line; everything centred.
- **Dark pill button** (Bulma `button is-dark is-rounded`): #363636, white Inter 16px/500, padding 7px 20px, 9999px radius, icon left (X logo, GitHub, Hugging Face emoji, database, play). "Soon" variant at 55% opacity with a 9.5px uppercase tag on white at 18%.
- **Modality orbit**: navy gradient centre pill; outer white chips (padding 0.42rem 0.88rem, 12.5px/500 #14213d, teal 11.5px icon) on a dashed ring; inner cream chips (11px) counter-rotating; selected chip becomes #14213d with white text and a seafoam icon, others dim to 55%.
- **Section eyebrow** (`.sec-eyebrow`): 11px/600 uppercase, letter-spacing 0.22em, #8a8378, 0.45rem above the title.
- **TL;DR card** (`.tldr-card`): teal at 3.5% fill, 1px teal-at-10% border, 10px radius, padding 28px 36px; a centred bold lede with underlined teal and copper key phrases, then justified-looking text beside an architecture diagram.
- **Checkpoint card**: white card with a dark top edge, mono model name, "● AVAILABLE NOW" tag, three stats (params, active, modalities) and an outlined "View on Hugging Face ↗" pill.
- **Navy band** (`#text2any.sec-dark`): #1c2a4a, 1px #2a385a, cream text #f7f4ed, seafoam eyebrow, a pill toggle (Chained / Independent prediction) and labelled output tiles.
- **Comparison slider**: RGB vs generated modality with a round divider handle, modality pill tabs (active navy), round arrow buttons and dot pager.
- **BibTeX** (`pre.bibtex`): #f7f4ed, Roboto Mono 12.5px #4a4a4a, padding 16px 20px, 4px radius.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | Bulma light navbar with section links |
| Animated hero mosaic | yes | drifting modality tiles at 42% under a mint fade |
| Title card | yes | frosted mint card with wordmark title |
| Venue | yes | plain gray "ICML 2026" line, no badge |
| Authors / affiliation logos | yes | teal names, numbered logo row |
| Link buttons | yes | six charcoal Bulma pills, one with a dropdown |
| Modality orbit | yes | interactive rotating chips linked to the mosaic |
| TL;DR | yes | italic serif heading over a teal-tinted card with diagram |
| Model checkpoints | yes | two cards with stats and Hugging Face links |
| Interactive any-to-any grid | yes | source × target matrix with hover autoplay |
| Comparison slider, image grids | yes | RGB → Any slider; Text → Any band on navy |
| Method walk-through | yes | numbered steps with mono eyebrows and diagrams |
| Results tables | yes | small centred tables |
| BibTeX | yes | cream mono block |
| Scroll-spy sidebar | yes | fixed left rail after the hero, hidden ≤1280px |
| Footer | yes | cream band with acknowledgements |

## Adapting to Other Content

- **No modality outputs for a mosaic**: keep the mint ground and frosted card and fill the background with the paper's own figures cropped to squares at 42% opacity; without imagery, drop the card blur and use plain #e8f3ee.
- **Fewer authors**: keep 20px teal names; the logo row can carry affiliations alone.
- **Larger results tables**: place them in a cream (#f7f4ed) section with #ebe5d6 hairlines; header 600 #444444; highlight best values in #2c5d63 bold and second in #b86a39.
- **Long publication or news lists**: use eyebrow + title + rows of 7px-radius white cards with #ebe5d6 borders, the same shape as the scroll-spy cards.
- **Improving legibility**: raise the hero card alpha to 0.8 or lower the mosaic opacity to 0.3 rather than darkening the text.

## Do's and Don'ts

- Do keep the two-expert color code: teal #2c5d63 for one path, copper #b86a39 for the other.
- Do open every section with the tracked 11px uppercase eyebrow.
- Do alternate white, cream and the single navy band; keep hairlines at #ebe5d6.
- Don't put text straight on the mosaic; it always sits on the frosted card.
- Don't use the serif anywhere except the TL;DR heading.
- Don't saturate the hero; everything in it stays pale except the navy wordmark and centre pill.

## Surfaces

Mint hero with a frosted card; white, cream (#f7f4ed) and navy (#1c2a4a) section bands; teal-tinted TL;DR card; white chips and cards with hairlines; cream BibTeX and footer.

## Imagery

Generated modality outputs of the same scenes (London buses and buildings): RGB, depth, surface normals, segmentation, SAM masks, Canny and SAM edges, captions as text tiles, and DINO/CLIP feature visualisations as radial pies; architecture diagrams with small thumbnails; photo-real text-to-image results on the navy band.

## Layout

Navbar, full-height hero with card and orbit, then a long single column at 960px (TL;DR, checkpoints, any-to-any, RGB → Any, Text → Any, method walk-through, chained prediction, self-verification, representation, training, benchmarks, dataset, BibTeX) with a few full-width interactive modules. Page height about 17,500px at 1440 wide.

## Agent Prompt Guide

Quick colors: mint #e8f3ee, card rgba(232,243,238,.62), navy #14213d, charcoal #363636, teal #2c5d63, copper #b86a39, cream #f7f4ed, cream rule #ebe5d6, band #1c2a4a, eyebrow #8a8378.

1. "Build a frosted hero card over a pale mint (#e8f3ee) background mosaic at 42% opacity: card max-width 900px, background rgba(232,243,238,.62), backdrop-filter blur(14px) saturate(118%), 1px rgba(207,227,214,.5) border, 18px radius, box-shadow 0 16px 44px rgba(20,33,61,.12). Title Inter 36px/700 #363636 with the project name in Space Grotesk 700 #14213d; venue 16px/500 #5c5c5c; authors 20px/500 #2c5d63."
2. "Make dark pill buttons: background #363636, white Inter 16px/500, padding 7px 20px, border-radius 9999px, icon left; centred row with 0.3rem margins around each."
3. "Create a section opener: eyebrow 11px/600 uppercase, letter-spacing 0.22em, #8a8378, then an Inter 24px/600 #363636 title; on cream sections use background #f7f4ed with 1px #ebe5d6 top and bottom borders, padding 64px 24px."

## Similar Pages

- EPFL VILAB project pages for multimodal models (4M lineage) that combine Bulma with custom interactive modules.
- Editorial research pages with a scroll-spy rail and alternating cream and navy bands.

## Quick Start

```css
:root {
  --mint: #e8f3ee;
  --mint-rule: #cfe3d6;
  --card: rgba(232, 243, 238, 0.62);
  --ink: #1a1a1a;
  --title: #363636;
  --navy: #14213d;
  --teal: #2c5d63;
  --teal-d: #1f4549;
  --warm: #b86a39;
  --cream: #f7f4ed;
  --cream-rule: #ebe5d6;
  --band: #1c2a4a;
  --seafoam: #8fc7c1;
  --eyebrow: #8a8378;
  --font-sans: 'Inter', 'Noto Sans', sans-serif;
  --font-display: 'Space Grotesk', 'Inter', sans-serif;
  --font-serif: 'Cormorant Garamond', 'Palatino', 'Georgia', serif;
  --font-mono: 'Roboto Mono', monospace;
}
```

## Provenance

- **URL**: https://modus-multimodal.epfl.ch
- **Paper**: MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities (arXiv 2607.25948), Mingqiao Ye et al.
- **Venue**: ICML 2026.
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 and links this project page.
- **Template credit**: Bulma 0.9.4 with Nerfies-style classes (`publication-title`, `publication-links`), extended by long inline stylesheets; the scroll-spy comment cites soto.epfl.ch as its model.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, two scrolled body captures, targeted computed-style queries, and the page's inline CSS read directly, on 2026-10-28.
