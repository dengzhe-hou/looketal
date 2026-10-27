# Archon — Style Reference

> A midnight observatory: an opalescent logotype, teal signal lights and numbered mission cards glowing on deep space.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share, and a DOM probe of the hero, section titles, cards, video embed and BibTeX), the 1440×900 and full-page screenshots plus a mid-page capture of the generation grid, and the page's `static/css/index.css` (an `--archon-*` dark layer over Bulma and the Nerfies base) and three inline `<style>` blocks read directly. Google Fonts serves only the regular (400) face of Google Sans and Noto Sans here, so every bold and semibold weight on the page is browser-synthesized from 400. Inline `font-family: 'Roboto'` headings fall back to the system sans because Roboto is not loaded.

## Overview

A long Nerfies-derived results page turned fully dark by an override layer. The body sits on near-black #03050a with three faint radial glows (teal at the top left, amber at the top right, blue mid-page) over a vertical #03050a → #06101d → #03050a gradient. The hero is centred: a 760px-wide image logotype "ARCHON" in iridescent glass letters, a 43px white Google Sans paper title with a soft teal text glow, two rows of teal (#32d6d3) author links, white affiliations, tiny 12px notes, a bold 28.8px "CVPR 2026" line, three glassy pill buttons with blue-teal tint and a blue hairline, and a TL;DR panel with a 22px radius, teal border, teal-to-amber tinted fill and a teal glow, opening with an amber "TL;DR:". Sections that follow have 40px centred titles underlined by a 3px #5dade2 rule, a framework figure that sits directly on the dark ground, three numbered "What do we explore?" cards each tinted in its own hue (amber, teal, coral), a 1120px YouTube embed, then many generation and editing grids: translucent navy cards with 18px radii holding JSON prompt frames and videos, captioned in grey Times New Roman. A floating round menu button at the left edge opens a dark pill side navigation.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): near-black #04060c 20.9%, #03060b 18.1%, #03050a 11.1%, #03090e 7.8%, #010409 3.8% (about 62% together); teal-tinted dark #122429 14.8% and #081115 13.8% (the TL;DR panel and the teal glow); cool grey #6d7680 9.7% (anti-aliased white text and the logotype edges). The logotype's purple, gold and blue highlights are too small to form clusters.

Anatomy in DOM order (desktop 1440px; Bulma `.container.is-max-desktop` 960px at x=240):

1. **Side menu button** (`#navToggle`, fixed, x=32, y=427): 30px circle, linear-gradient(135deg, #5dade2, #32d6d3), white hamburger icon, shadow 0 14px 34px rgba(0,0,0,0.35).
2. **Logotype** (`.archon-hero-brand img`, y=96, 760×190): `width: min(760px, 92vw)`, centred; the hero container starts 36px from the top and the brand block adds a 24px top margin. Gap 12px.
3. **Paper title** (`h1.archon-paper-title`, y=298, two lines, 97px): Google Sans 43.2px (clamp(1.6rem, 3vw, 2.8rem)) at weight 600 (synthesized), line-height 1.12, #f4f8ff, text-shadow 0 18px 42px rgba(50,214,211,0.16). Gap 23px.
4. **Authors** (`.archon-authors`, y=418 and 461): Google Sans 20px/400, links #32d6d3, superscripts white; flex-wrap with gaps 6.7px 18.4px, max-width 980px. Gap 18px.
5. **Affiliations** (y=504): Google Sans 16px, line-height 1.85, #f4f8ff with superscript numbers, items 23px apart. Gap 18px.
6. **Notes** (y=555): Noto Sans 12px, #f4f8ff. Gap 13px.
7. **Venue** (`.archon-venue-text`, y=585): Google Sans 28.8px/800 (synthesized), #ffffff. Gap 40px.
8. **Buttons** (y=659, 40px tall, 12px apart): Paper, arXiv, Code Coming Soon; glass pills, Noto Sans 16px/700, icon left. Gap 38px.
9. **TL;DR panel** (`p.archon-tldr`, y=737–842, 920px at x=260): 1px rgba(50,214,211,0.46) border, 22px radius, fill linear-gradient(135deg, rgba(50,214,211,0.18), rgba(244,179,80,0.11)) over rgba(9,18,32,0.86), glow 0 22px 65px rgba(50,214,211,0.18); Noto Sans 20.48px/650, line-height 1.65, #eafcff, centred; "TL;DR:" 900 #f4b350, letter-spacing 0.02em. The Framework section begins just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Deep Space | #03050a | --archon-bg | page base and gradient ends |
| Night Navy | #06101d | (literal) | middle stop of the body gradient |
| Starlight | #f4f8ff | --archon-text | titles, body text, affiliations, button labels |
| Ice | #eafcff | (literal) | TL;DR text |
| Mist | #a9b7ca | --archon-muted | section leads, framework caption, video captions, card body text, side-nav links |
| Signal Teal | #32d6d3 | --archon-cyan | author links, TL;DR border and glow, nav toggle gradient end, "Video Parameterization" card title and bullets, JSON keys |
| Sky Blue | #5dade2 | --archon-blue | 3px section-title underline, button tint and border, nav toggle gradient start, card tints, `.highlight-blue` text |
| Amber | #f4b350 | --archon-gold | "TL;DR:" label, "Any-to-Any" card title and bullets, strong text in answers, JSON strings, author link hover |
| Coral | #ff6b7a | --archon-red | third card border and index gradient start, JSON numbers |
| Salmon | #ff8f7a | (literal) | third card title and bullets |
| Surface | rgba(9,18,32,0.86) | --archon-surface | TL;DR base, video cards, footer |
| Surface Strong | rgba(13,30,52,0.94) | --archon-surface-strong | question cards, JSON frames, button hover base |
| Border | rgba(120,162,220,0.26) | --archon-border | video card, JSON frame and footer borders |
| Video Black | #020408 | (literal) | video element background |
| Well | rgba(2,8,16,0.82) | (literal) | BibTeX fill, YouTube embed well (0.7), card answer boxes (0.42) |
| Button Base | rgba(7,17,31,0.84) | (literal) | base layer under the glass pill button tint |
| Orange Flare | #ff8a3d | (literal) | end of the amber number-badge gradient |
| Mint Flare | #6df0ec | (literal) | end of the teal number-badge gradient |
| Code Ice | #dcecff | (literal) | BibTeX text |

Card shadow everywhere is `--archon-shadow` 0 22px 70px rgba(0,0,0,0.45).

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / authors | 'Google Sans', sans-serif | Google Sans 400 only; 600/800 synthesized | Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 only; 650–900 synthesized | Noto Sans (load 400–900 to get true bolds) |
| Generation headings | inline 'Roboto', sans-serif | not loaded; system sans (Arial on Windows) | Roboto |
| Video captions | "Times New Roman", serif | system Times New Roman | Tinos |
| Code | Bulma monospace; JSON frames Consolas | system Consolas | JetBrains Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Logotype | `.archon-hero-brand img` | image, 760px wide | — |
| Paper title | `.archon-paper-title` | clamp(1.6rem, 3vw, 2.8rem) = 43.2px / 600 / 1.12 | #f4f8ff |
| Authors | `.archon-authors` | 20px / 400 / 1.65 | #32d6d3 links |
| Venue | `.archon-venue-text` | clamp(1.28rem, 2vw, 1.9rem) = 28.8px / 800 / 1.18 | #ffffff |
| TL;DR | `.archon-tldr` | clamp(1.08rem, 1.55vw, 1.28rem) = 20.48px / 650 / 1.65 | #eafcff |
| Section title | `.archon-section-title` (`h1.title.is-2`) | 40px / 600 / 45px, padding-bottom 10.4px | #f4f8ff |
| Generation heading | `h2.title.is-3` (inline Roboto) | 32px / 600 / 36px, centred | #f4f8ff |
| Section lead | `.archon-section-lead` | 1.1rem = 17.6px / 400 / 1.75 | #a9b7ca |
| Card title | `.archon-challenge-card h2` | 1.15rem = 18.4px / 800 / 1.25 | per card (#f4b350, #32d6d3, #ff8f7a) |
| Card question | `.challenge-question` | 0.98rem = 15.7px / 400 / 1.6 | #ffffff |
| Card bullet | `.challenge-answer-list li` | 15.7px / 720 / 1.48 | per card |
| Video caption | `.video-title-3x3` | clamp(8px, 1.5vw, 20px) Times New Roman / 400 | #a9b7ca |
| Button | `.publication-links .button` | 16px / 700 | #f4f8ff |
| BibTeX | `.archon-bibtex code` | 0.9rem = 14.4px / 1.65 | #dcecff |
| Side nav | `.side-nav a` | 0.9rem = 14.4px / 600 Google Sans | #a9b7ca, hover #32d6d3 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Glass pill buttons | 999px | 1px rgba(93,173,226,0.42) | 0 14px 36px rgba(0,0,0,0.28) |
| TL;DR panel | 22px | 1px rgba(50,214,211,0.46) | 0 22px 65px rgba(50,214,211,0.18) |
| Question cards | 24px | 1px tinted per card at 0.46 alpha | 0 22px 70px rgba(0,0,0,0.45) |
| Card answer box | 18px | 1px rgba(50,214,211,0.22) | none; fill rgba(2,8,16,0.42) |
| Number badge | 999px (40px circle) | none | none |
| Video cards | 18px | 1px rgba(120,162,220,0.26) | 0 22px 70px rgba(0,0,0,0.45) |
| Videos | 12px | none | none |
| YouTube embed | 10px (Bulma `.publication-video` `!important` beats the 24px override) | 1px rgba(50,214,211,0.3) | 0 22px 70px rgba(0,0,0,0.45) |
| BibTeX pre | 20px | 1px rgba(93,173,226,0.28) | 0 22px 70px rgba(0,0,0,0.45) |
| Side nav panel | 20px; links 999px | none | 0 18px 50px rgba(0,0,0,0.38) |
| Section-title underline | 0 | 3px #5dade2 bottom | none |

## Layout Metrics

- **Container**: Bulma `.container.is-max-desktop` 960px (x=240); the video section widens to `width: calc(100% - 2rem); max-width: 1180px`.
- **Hero**: container starts 36px down; logotype 24px top margin, 12px bottom; the hero section ends at y=870.
- **Sections**: Bulma `.section.is-small` with `padding: 48px 0` (overview); challenges 4rem (64px); video 3.5rem top / 4.25rem bottom; generation group headers inline padding 60px / 20px; BibTeX 3.5rem / 2.5rem.
- **Measures**: TL;DR 920px; section lead 860px; framework caption 960px, left-aligned; framework image `min(100%, 1040px)`.
- **Question grid**: 3 columns, gap 1.25rem (20px); cards 307px wide at 1440, padding 21.6px.
- **Video**: embed `min(100%, 1120px)`, 16:9 (1120×630 at 1440).
- **Generation grids**: `.carousel-row-2` 2 columns at max-width 85% with 8px gaps; 3×3, 4- and 6-column variants; the results carousel spans 100vw.
- **Footer**: rgba(9,18,32,0.86), 1px border on top, padding 48px 24px 96px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px | (100% − 960px)/2 | 16px | 43.2px (section 40px) | 3 question cards; side nav visible |
| 961–1215px | (100% − 960px)/2 | 16px | 3vw (clamp) | — |
| ≤960px | 24px (fluid container) | 16px | 3vw, floor 1.6rem | question cards stack to one column |
| ≤768px | 24px; TL;DR gets 16px side margins | 16px | 25.6px floor | side nav hidden; logotype `min(560px, 96vw)`; Bulma columns stack |
| ≤480px | 24px | 16px | 25.6px | 3×3 grids keep 3 columns at 6px gaps; 6-column rows → 3; 4-column rows → 2 |

## Components

- **Glass pill button** (`.publication-links .button`): 40px tall, padding 7px 20px, 999px radius, 1px rgba(93,173,226,0.42) border, fill linear-gradient(135deg, rgba(93,173,226,0.28), rgba(50,214,211,0.14)) over rgba(7,17,31,0.84), shadow 0 14px 36px rgba(0,0,0,0.28), Noto Sans 16px/700 #f4f8ff, icon left (Font Awesome, Academicons). Hover: border rgba(50,214,211,0.72), fill teal-to-amber over the strong surface, text #ffffff.
- **TL;DR panel**: as in First Viewport; amber 900-weight label then the sentence.
- **Section title** (`.archon-section-title`): inline-block, centred, 40px/600 #f4f8ff, padding-bottom 10.4px, 3px #5dade2 bottom border.
- **Numbered question card** (`.archon-challenge-card`): 24px radius, padding 21.6px, strong surface with a 145° tint of its hue (blue, teal or coral at 0.16–0.18 → 0.04), 1px border of the same hue at 0.46, a 112px radial glow circle peeking from the top right; a 40px round number badge with a two-colour gradient (amber → #ff8a3d, teal → #6df0ec, coral → amber) and white 800 numerals; title 18.4px/800 in the card hue; white question; answer box with 18px radius on rgba(2,8,16,0.42) holding glowing-dot bullets in the hue at 720 weight.
- **Video card** (`.video-item-*`): padding 10px, 18px radius, 1px `--archon-border`, fill linear-gradient(145deg, rgba(93,173,226,0.09), rgba(50,214,211,0.04)) over `--archon-surface`; video 12px radius on #020408; caption Times New Roman in #a9b7ca with a blue "Script (output):" label; a JSON frame above it (strong surface, 6px radius, keys teal, strings amber, numbers coral). A prompt overlay fades in on hover.
- **Side navigation**: fixed at left 2rem; gradient 30px toggle; panel rgba(3,5,10,0.82), 20px radius, padding 13.6px; links 999px pills with a 6px dot, #a9b7ca, hover rgba(93,173,226,0.13) fill, #32d6d3 text and a 5px shift right.
- **BibTeX**: 20px radius, 1px rgba(93,173,226,0.28), rgba(2,8,16,0.82), padding 20px 21.6px, 14.4px #dcecff.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Logotype | yes | iridescent image wordmark above the title |
| Title / authors / affiliations | yes | centred, teal author links, 12px notes |
| Venue | yes | bold 28.8px white "CVPR 2026" line |
| Link buttons | yes | three glass pills (Code "Coming Soon" keeps the active style) |
| TL;DR | yes | teal-bordered glowing panel |
| Framework figure | yes | full-colour diagram directly on the dark ground, grey caption below |
| Research questions | yes | three numbered hue-coded cards |
| Video | yes | YouTube embed, 1120px |
| Generation results | yes | many sections of video cards with JSON prompt frames and serif captions |
| Editing and comparisons | yes | same card grids |
| Results tables | absent from the source | `<table>` elements are layout wrappers only; no numeric tables |
| Abstract | absent from the source | the TL;DR and framework caption stand in |
| BibTeX | yes | dark rounded pre |
| Side navigation | yes | floating toggle with a dark pill menu |
| Footer | yes | translucent navy band with a border on top |

## Adapting to Other Content

- **Light figures**: keep figures without frames on the dark ground only if they have their own light panels (as the framework does); otherwise place them in a video-card shell with 10px padding.
- **A numeric results table**: put it in a `--archon-surface` card with 18px radius; header 14.4px/700 #f4f8ff with a 1px rgba(120,162,220,0.26) bottom rule; body #a9b7ca; best values #32d6d3 bold. Do not use white table fills.
- **More authors**: the flex-wrap author block takes extra rows at 6.7px/18.4px gaps; keep links teal and notes at 12px.
- **An abstract**: a 960px left-aligned 17.6px #a9b7ca paragraph under a `.archon-section-title`, like the framework caption.
- **News or publication lists**: rows inside a strong-surface card with 24px radius; date in a teal uppercase `.answer-label` pill (rgba(50,214,211,0.16), 12.5px/900, letter-spacing 0.08em), item text #f4f8ff.

## Do's and Don'ts

- Do keep everything on #03050a with soft radial glows; surfaces are translucent navy, never grey.
- Do give each conceptual group its own hue (amber, teal, coral) but keep links teal and rules sky blue.
- Do use 999px pills for buttons and generous 18–24px radii for panels.
- Don't use pure white panels or white table fills; text is #f4f8ff on dark.
- Don't rely on Google Fonts weights that the page does not load; request 600–800 explicitly when rebuilding.
- Don't mix in a light section; the override layer forces every Bulma `is-black` section transparent so the gradient runs unbroken.

## Surfaces

Near-black gradient page with teal, amber and blue radial glows; translucent navy cards (0.86 and 0.94 alpha); black video wells; a translucent footer.

## Imagery

An iridescent logotype, a colour-coded framework diagram, 3D head renders beside segmentation maps and photoreal talking-head video, JSON prompt snippets, YouTube video. Faces and synthetic renders dominate below the fold.

## Layout

Centred hero; Framework; What do we explore? (3 cards); Video; Any-to-Any Generation (six sub-sections); Editing (three); Comparisons; BibTeX; footer. About 14,300px tall at 1440 wide with 65 videos.

## Agent Prompt Guide

Quick colors: background #03050a, text #f4f8ff, muted #a9b7ca, teal #32d6d3, sky #5dade2, amber #f4b350, coral #ff6b7a, surface rgba(9,18,32,0.86), border rgba(120,162,220,0.26).

1. "Create a glowing TL;DR panel on #03050a: max-width 920px, centred, padding 17.6px 23.2px, 22px radius, 1px solid rgba(50,214,211,0.46) border, background linear-gradient(135deg, rgba(50,214,211,0.18), rgba(244,179,80,0.11)), rgba(9,18,32,0.86); box-shadow 0 22px 65px rgba(50,214,211,0.18); Noto Sans 20.48px/650, line-height 1.65, #eafcff, centred; lead with 'TL;DR:' in #f4b350 at 900 weight."
2. "Make glass pill buttons: height 40px, padding 7px 20px, 999px radius, 1px solid rgba(93,173,226,0.42), background linear-gradient(135deg, rgba(93,173,226,0.28), rgba(50,214,211,0.14)), rgba(7,17,31,0.84), shadow 0 14px 36px rgba(0,0,0,0.28), Noto Sans 16px/700 #f4f8ff, icon left; hover border rgba(50,214,211,0.72)."
3. "Build three numbered question cards in a 3-column grid with 20px gaps: 24px radius, padding 21.6px, background rgba(13,30,52,0.94) with a 145° tint of the card hue, 1px border of the hue at 0.46 alpha, shadow 0 22px 70px rgba(0,0,0,0.45); a 40px circular badge with a gradient and white 800 numeral; title 18.4px/800 in #f4b350, #32d6d3 or #ff8f7a; body #a9b7ca."

## Similar Pages

- Nerfies/Bulma pages converted to a dark theme with an override stylesheet.
- Digital-human and avatar pages with an image logotype and dense video-result grids.

## Quick Start

```css
:root {
  --archon-bg: #03050a;
  --archon-text: #f4f8ff;
  --archon-muted: #a9b7ca;
  --archon-blue: #5dade2;
  --archon-cyan: #32d6d3;
  --archon-gold: #f4b350;
  --archon-red: #ff6b7a;
  --archon-surface: rgba(9, 18, 32, 0.86);
  --archon-surface-strong: rgba(13, 30, 52, 0.94);
  --archon-border: rgba(120, 162, 220, 0.26);
  --archon-shadow: 0 22px 70px rgba(0, 0, 0, 0.45);
  --font-display: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
}
body {
  background: radial-gradient(circle at 12% 0%, rgba(50,214,211,0.18), transparent 28rem),
              radial-gradient(circle at 84% 8%, rgba(244,179,80,0.14), transparent 30rem),
              linear-gradient(180deg, #03050a 0%, #06101d 44%, #03050a 100%);
  color: var(--archon-text);
  font: 16px/1.5 var(--font-body);
}
```

## Provenance

- **URL**: https://zju3dv.github.io/archon/
- **Paper**: Archon: A Unified Multimodal Model for Holistic Digital Human Generation (arXiv 2605.30311), Chong Bao et al.
- **Venue**: CVPR 2026.
- **Selection reason**: the arXiv comment states acceptance at CVPR 2026 and links this page.
- **Template credit**: Nerfies/Bulma base (footer credit) with a custom `--archon-*` dark override layer in `static/css/index.css`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), a DOM probe of hero and components, the 1440×900 and full-page screenshots, a mid-page capture of the generation grid, and `index.css` plus the inline styles read directly, on 2026-10-28.
