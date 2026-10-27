# PhotoAgent — Style Reference

> A product launch at midnight: a cartoon fox mascot, an indigo-to-violet wordmark and glowing glass cards on ink black.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's own `css/style.css` (its header comment reads "OpenArt-inspired project page") and `index.html`. The CSS and the render agree; the only dimmed elements are the two "(Coming)" buttons, which the stylesheet sets to 55% opacity.

## Overview

A dark SaaS-style landing page rather than an academic template. A sticky, blurred header holds a 32px mascot icon with the "PhotoAgent" wordmark, six muted nav links and a gradient "Code & Demo" button. The centred hero stacks a tinted pill badge ("AUTONOMOUS IMAGE EDITING"), a 96px rounded mascot tile beside a 64px Space Grotesk wordmark filled with an indigo-to-violet gradient (#6366f1 → #a855f7), a 44px two-tone tagline, authors with underlined names, large muted affiliations, a short pitch paragraph and four gradient buttons. A full-width before/after teaser strip in a 20px-radius frame with an indigo hairline closes the hero. Sections alternate #0d0d12 and #13131a, each opening with a tinted uppercase pill, a 44–48px centred heading and a muted lead, followed by #1a1a24 cards with 20px radii, gradient top-edge reveals on hover and soft indigo glows.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): ink family #0d0d12 / #0d0d14 / #0d0d11 / #0b0b10 / #0c0d13 together 78.2%; lavender gray #988aa7 11.6% (muted text, button gradients and the teaser photos blended); deep violet #2e263b 8.6% (badge tint, dimmed buttons, glow); #160d10 1.6% (warm photo shadows).

Anatomy in DOM order (desktop 1440px; container 1200px with 24px padding, x=144–1296):

1. **Sticky header** (0–73px): background #0d0d12 at 85% with 12px backdrop blur, 1px rgba(255,255,255,.08) bottom border; nav row 72px tall. Left: 32px mascot icon (10px radius, dark drop shadow) and "PhotoAgent" in Space Grotesk 21.6px/700, letter-spacing -0.02em, #f0f0f5. Centre-right: Paradigm, Overview, How it works, Results, Dataset, Paper in DM Sans 15.2px/500 #9898a8, 32px apart. Right: gradient button "Code & Demo (★ to follow updates)", 44px tall.
2. **Hero** (`section.hero`, 73–1167px): padding 80px 0 100px; a radial indigo glow (rgba(99,102,241,.12)) spreads from the top centre.
3. **Badge** (y=166, 32px tall): "AUTONOMOUS IMAGE EDITING", DM Sans 12.8px/600 uppercase, letter-spacing 0.08em, #818cf8 on rgba(99,102,241,.15), radius 100px, padding 6px 14px. Gap 24px.
4. **Brand row** (y=222, 96px tall): mascot tile 96px, radius 22px, ring 0 0 0 2px indigo at 25% plus a 0 12px 32px black shadow; 20px gap; "PhotoAgent" Space Grotesk 64px/700, line-height 1.15, letter-spacing -0.03em, filled with linear-gradient(135deg, #6366f1, #a855f7). Gap 12px.
5. **Tagline** (y=330): Space Grotesk 44px/500, letter-spacing -0.02em, #c8c8d8, with "Aesthetic Intent" and "Visual Reality" in 700 #f0f0f5. Gap 24px.
6. **Authors** (y=407): DM Sans 17.6px/500 #f0f0f5; linked names carry a 1px #9898a8 underline that turns #818cf8 on hover. Gap 8px.
7. **Affiliations** (y=446, two lines): DM Sans 20.8px/400, line-height 1.5, #9898a8, max-width 720px. Gap 28px.
8. **Pitch** (y=542): DM Sans 19.2px, line-height 1.65, #9898a8, max-width 640px. Gap 36px.
9. **Buttons** (y=673, 54px tall): Paper (arXiv), Code (★ to follow updates), HuggingFace Demo (Coming), Dataset (Coming); gap 16px; the last two at 55% opacity. Gap 56px.
10. **Teaser** (y=784): one 1150px-wide strip of three input/output pairs (sunset portrait, latte, temple eaves) with serif "Input"/"Output" labels and a caption band baked into the image, inside a 20px-radius frame with a 1px indigo-at-20% border and 0 24px 48px black + 0 0 80px indigo glow. It continues below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #0d0d12 | --bg | page background, hero, paradigm and how-it-works sections, iteration buttons |
| Ink Alt | #13131a | --bg-alt | alternating sections ("What makes PhotoAgent different", Results) |
| Surface | #1a1a24 | --surface | feature, paradigm, how, scene and metric cards, paper card, viewers, nav dropdown |
| Text | #f0f0f5 | --text | headings, wordmark, author names, strong text |
| Tagline Gray | #c8c8d8 | (literal) | hero tagline regular words |
| Muted | #9898a8 | --text-muted | nav links, affiliations, pitch, section leads, card body, footer |
| Indigo | #6366f1 | --accent / --gradient-start | gradient start on wordmark, buttons and card top edges; active dots; bullet dots |
| Light Indigo | #818cf8 | --accent-light | hero badge text, agent column title, metric values, link text, hover underline |
| Violet | #a855f7 | --gradient-end | gradient end; "Editing, reimagined" and scenes badge text |
| Coral | #f87171 | (literal) | "Human-in-the-loop" column title |
| Border | rgba(255,255,255,0.08) | --border | header rule, card borders, footer rule |

Pain-column accents use rgba(239,68,68,.5) for the 3px top border and bullets; the agent column uses rgba(99,102,241,.6).

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | "Space Grotesk", system-ui, sans-serif | Space Grotesk 500/600/700 | Manrope |
| Text | "DM Sans", system-ui, sans-serif | DM Sans 400/400i/500/600/700 | Plus Jakarta Sans |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Wordmark (h1) | `.hero-title` | clamp(2.5rem, 6vw, 4rem) → 64px / 700 / 1.15, letter-spacing -0.03em | gradient #6366f1 → #a855f7 |
| Tagline | `.hero-tagline` | clamp(1.8rem, 4.5vw, 2.75rem) → 44px / 500 / 1.2, -0.02em | #c8c8d8, strong 700 #f0f0f5 |
| Paradigm heading | `.paradigm-title` | clamp(2rem, 5vw, 3rem) → 48px / 700 / 1.2 | #f0f0f5, "Agent" gradient |
| Section heading | `.section-title` | clamp(2rem, 4vw, 2.75rem) → 44px / 700, -0.02em, centred | #f0f0f5 |
| Sub-block heading | `.how-scenes-title`, `.aesthetic-intro-title` | clamp(1.5rem, 3vw, 2rem) / clamp(1.6rem, 3.5vw, 2.2rem), 700 | #f0f0f5 |
| Card heading | `.feature-card h3`, `.paper-card h3` | 1.2rem / 600; 1.35rem / 600 | #f0f0f5 |
| Column title | `.paradigm-col-title` | 1.15rem = 18.4px / 700 | #f87171 or #818cf8 |
| Logo | `.logo` | 1.35rem = 21.6px / 700, -0.02em | #f0f0f5 |
| Body | `body` | 1rem = 16px / 400 / 1.6 | #f0f0f5 |
| Section lead | `.section-lead` | 1.1rem / 400 / 1.65, max 680px | #9898a8 |
| Hero pitch | `.hero-subtitle` | 1.2rem = 19.2px / 1.65 | #9898a8 |
| Affiliations | `.hero-affiliations` | 1.3rem = 20.8px / 1.5 | #9898a8 |
| Authors | `.hero-authors` | 1.1rem = 17.6px / 500 | #f0f0f5 |
| Badge | `.hero-badge` | 0.8rem / 600 uppercase, 0.08em | #818cf8 |
| Section pill | `.paradigm-badge`, `.how-badge` | 0.78rem / 700 uppercase, 0.1em | #a855f7 or #818cf8 |
| Button | `.btn` / `.btn-lg` | 0.95rem / 600; large 1rem / 600 | #ffffff |
| Card body | `.feature-card p`, `.paradigm-list li` | 0.95rem / 1.6 | #9898a8 |
| Metric value | `.metric-value` | 1.75rem | #818cf8 |
| Footer | `.footer p` | 0.9rem | #9898a8 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 12px (--radius) | none | hover 0 8px 24px indigo at 35% |
| Badges and section pills | 100px | section pills 1px tint at 20% | none |
| Cards (feature, paradigm, how, scene, op, paper, viewers) | 20px (--radius-lg) | 1px rgba(255,255,255,.08) | hover up to 0 20px 50px indigo at 12% + 0 8px 24px black at 40% |
| Teaser frame, paradigm image | 20px | 1px indigo at 20–25% | 0 24px 48px black at 50%, 0 0 80px indigo at 8%; inset 0 0 60px black at 25% |
| Metric cards, footnotes, iteration buttons | 12px | 1px border token or tint | none |
| Mascot tile | 22px | 2px indigo ring at 25% | 0 12px 32px black at 50%, 0 0 40px indigo at 12% |
| Icon tiles in cards | 12–14px | none | none |
| Compare thumbnails | 10px | 2px border token, active #6366f1 | none |

Card hover adds a 3px top bar in linear-gradient(90deg, #6366f1, #a855f7) and lifts 2–6px. The paradigm image floats 8px on a 6s loop with an animated gradient border at 50% opacity.

## Layout Metrics

- **Container**: `.container { max-width: 1200px; margin: 0 auto; padding: 0 24px }` (content x=144–1296 at 1440).
- **Header**: sticky, 72px nav row plus 1px rule.
- **Hero**: padding 80px 0 100px; everything centred; text blocks cap at 800px (title), 720px (affiliations) and 640px (pitch); teaser spans the full 1152px content width.
- **Sections**: `.section { padding: 100px 0 }`; paradigm and how-it-works sections 120px 0 100px. Badge → heading 24px; heading → lead 16–20px; lead → content 48–60px.
- **Grids**: features auto-fit min 260px, gap 24px; paradigm columns 2 × 1fr, gap 32px, max 860px; how-it-works 4 cards up to 270px each with arrows between; scene and aesthetic-op grids 3 columns; metrics auto-fit min 200px.
- **Figures**: paradigm illustration max 960px centred; viewers and compare sliders fill the container inside 24px card padding.
- **Paper card**: max 680px, padding 40px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1067px | 24px inside 1200px | 16px | 64px | full layout |
| ≤960px | 24px | 16px | 6vw ≈ 58px | how-it-works cards 2 per row, arrows hidden; how section 80px 0 64px |
| ≤900px | 24px | 16px | 54px | scene, aesthetic-op and result I/O grids → 2 columns |
| ≤768px | 24px | 16px | 46px | nav links hidden; hero padding 56px 0 64px; buttons stack in a column; sections 64px; paradigm columns, dataset cards, memory block → 1 column |
| ≤667px | 24px | 16px | 40px floor | — |
| ≤560px | 24px | 16px | 40px | how, scene and op cards → 1 column |

## Components

- **Gradient button** (`.btn.btn-primary`): inline-flex, padding 10px 20px (large 14px 28px), radius 12px, no border, DM Sans 600 at 0.95rem (large 1rem), white text on linear-gradient(135deg, #6366f1, #a855f7). Hover: translateY(-1px) and 0 8px 24px indigo at 35%. "Coming" variant: same at 55% opacity, no pointer events.
- **Outline button** (`.btn-outline`): transparent, 1px rgba(255,255,255,.08) border, #f0f0f5 text; hover border #6366f1 and text #818cf8.
- **Tinted pill badge** (`.hero-badge`, `.paradigm-badge`, `.how-badge`): padding 6px 14–16px, radius 100px, uppercase 0.78–0.8rem/600–700, letter-spacing 0.08–0.1em; indigo version #818cf8 on indigo at 12–15%, violet version #a855f7 on violet at 12% with a 1px violet-at-20% border.
- **Wordmark lockup** (`.hero-brand`): flex, gap 20px; 96px mascot tile (22px radius, indigo ring) + gradient-filled 64px Space Grotesk title.
- **Glass card** (`.feature-card`, `.how-card`, `.how-scene-card`): #1a1a24, 1px rgba(255,255,255,.08), radius 20px, padding 28–32px; title Space Grotesk 1.05–1.2rem/600, body 0.86–0.95rem #9898a8; hover border indigo at 30–45%, translateY(-2 to -6px), 3px gradient top bar fades in. How-it-works cards also pulse their border in sequence every 8s.
- **Paradigm columns** (`.paradigm-col`): same card with a 3px top border (red at 50% or indigo at 60%), coral or light-indigo title, bullet list with 8px round dots.
- **Footnote panel** (`.aesthetic-intro-footnote`): padding 20px 24px, indigo at 5% fill, 1px indigo at 12%, radius 12px, 0.95rem #9898a8 with #818cf8 emphasis.
- **Before/after slider**: 20px-radius surface frame, white 1px divider, round gradient handle with 3px white border, "Before/After" labels 0.75rem on black at 65% with 6px radius; thumbnails 10px radius with 2px borders.
- **Iteration viewer**: surface card with 24px padding; image well on #0d0d12 with 12px radius; caption gradient to black at 75% with white 0.9rem text; Previous/Next buttons #0d0d12, 1px border, 12px radius, hover indigo border; round dots, active #6366f1.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Sticky header with logo and nav | yes | blurred ink bar, mascot icon, muted links, gradient CTA |
| Venue badge | absent from the source | no visible venue anywhere; the hero pill says "Autonomous image editing", and ICML is mentioned only in screen-reader-only SEO text (as "ICML 2025") |
| Logo / mascot | yes | 96px rounded tile beside the gradient wordmark |
| Title / tagline | yes | gradient 64px wordmark, 44px two-tone tagline |
| Authors / affiliations | yes | centred; underlined linked names; large muted affiliations |
| Link buttons | yes | four gradient buttons, two dimmed as "Coming" |
| Teaser | yes | framed full-width before/after strip |
| Abstract | present but non-standard | replaced by the hero pitch and section leads |
| Method overview | yes | paradigm illustration, two comparison columns, four step cards, memory block |
| Interactive demos | yes | iteration viewer, before/after slider with thumbnails, image lightbox |
| Results | yes | metric cards and image grids; no HTML tables |
| Dataset / benchmark | yes | UGC-Edit section with cards |
| Paper card / BibTeX | yes | paper card with title, authors and links; no BibTeX block |
| Footer | yes | centred muted lines over a hairline |

## Adapting to Other Content

- **More authors**: keep a single centred 17.6px line that wraps; move affiliations to two or three lines at the existing 20.8px size, or drop them to 1rem if they exceed three lines.
- **A venue badge**: reuse the hero pill style above the brand row, e.g. "ICML 2026 · ORAL" in #818cf8 on indigo at 15%.
- **A results table**: wrap it in a #1a1a24 card with 20px radius and 24px padding; header cells #9898a8 600 uppercase 0.8rem; body #f0f0f5; best values #818cf8 700; row rules rgba(255,255,255,.08).
- **Long publication or news lists**: use 12px-radius surface rows with a light-indigo date and muted body, separated by 12px; avoid gradient fills on list items.
- **No mascot**: keep the lockup but drop the tile; the gradient wordmark alone carries the hero.

## Do's and Don'ts

- Do keep the indigo-to-violet gradient (135deg, #6366f1 → #a855f7) for the wordmark, buttons and hover top bars only.
- Do open every section with a tinted uppercase pill, a centred Space Grotesk heading and a muted lead.
- Do alternate section grounds between #0d0d12 and #13131a and put content on #1a1a24 cards.
- Don't use solid indigo fills for large areas; tints stay at 5–15% opacity.
- Don't left-align section intros; all headings and leads are centred.
- Don't add hard shadows to cards at rest; depth appears on hover.

## Surfaces

Three ink layers (#0d0d12 page, #13131a alternate sections, #1a1a24 cards) with 8%-white hairlines. Radial indigo and violet glows (7–12%) sit behind the hero, paradigm and how-it-works sections and pulse slowly. Image frames get indigo-tinted borders and long black shadows.

## Imagery

Real photographs shown as before/after pairs (portraits, food, architecture), a flat illustrated paradigm diagram with a cute agent mascot, line icons in tinted tiles, and a cartoon fox mascot used as logo and app icon. Photos sit in 20px-radius frames on black.

## Layout

Sticky header, centred hero with teaser, then six full-width bands (Paradigm, Overview, How it works, Results, UGC-Edit dataset, Paper & resources) inside a 1200px container. Each band is centred: pill, heading, lead, then grids of cards or a large framed figure. Page height about 11,200px at 1440 wide.

## Agent Prompt Guide

Quick colors: page #0d0d12, alt #13131a, card #1a1a24, text #f0f0f5, muted #9898a8, gradient #6366f1 → #a855f7, light indigo #818cf8, border rgba(255,255,255,0.08).

1. "Build a centred dark hero on #0d0d12 with a radial rgba(99,102,241,.12) glow at the top: tinted pill (12.8px/600 uppercase, letter-spacing 0.08em, #818cf8 on rgba(99,102,241,.15), radius 100px, padding 6px 14px), then a 96px app-icon tile (22px radius) beside a Space Grotesk 64px/700 wordmark filled with linear-gradient(135deg, #6366f1, #a855f7), then a 44px/500 #c8c8d8 tagline with bold words in #f0f0f5."
2. "Make gradient buttons: padding 14px 28px, radius 12px, DM Sans 16px/600 white on linear-gradient(135deg, #6366f1, #a855f7); hover translateY(-1px) and box-shadow 0 8px 24px rgba(99,102,241,.35); a 'Coming' variant at opacity 0.55."
3. "Create a feature card: background #1a1a24, 1px rgba(255,255,255,.08) border, radius 20px, padding 32px; title Space Grotesk 19.2px/600 #f0f0f5; body DM Sans 15.2px #9898a8; on hover border rgba(99,102,241,.3), translateY(-2px), and a 3px linear-gradient(90deg, #6366f1, #a855f7) bar along the top edge."

## Similar Pages

- AI product landing pages in the OpenArt / Linear dark style adapted for research projects.
- Project pages with a mascot logo and a gradient wordmark, such as agent and editing-tool papers that present themselves as apps.

## Quick Start

```css
:root {
  --bg: #0d0d12;
  --bg-alt: #13131a;
  --surface: #1a1a24;
  --text: #f0f0f5;
  --text-muted: #9898a8;
  --tagline: #c8c8d8;
  --accent: #6366f1;
  --accent-light: #818cf8;
  --gradient-start: #6366f1;
  --gradient-end: #a855f7;
  --pain: #f87171;
  --border: rgba(255, 255, 255, 0.08);
  --radius: 12px;
  --radius-lg: 20px;
  --font-sans: "DM Sans", system-ui, sans-serif;
  --font-display: "Space Grotesk", system-ui, sans-serif;
}
```

## Provenance

- **URL**: https://mdyao.github.io/PhotoAgent/
- **Paper**: PhotoAgent: Exploratory Visual Aesthetic Planning with Large Vision Models (arXiv 2602.22809), Mingde Yao et al.; the page titles it "PhotoAgent: Agentic Photo Editing with Exploratory Visual Aesthetic Planning".
- **Venue**: ICML 2026 Oral.
- **Selection reason**: the arXiv comment states acceptance at ICML 2026 as an Oral and links this project page.
- **Template credit**: no footer credit; the stylesheet header calls it an "OpenArt-inspired project page".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the page's `style.css` and `index.html` read directly, on 2026-10-28.
