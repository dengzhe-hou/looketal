# OnePose Night Launch — Style Reference

> A product launch at midnight: a tiled video wall sinking into indigo, an ice-cyan gradient headline floating over it, and blueprint-gridded cards waiting below the fold.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), DOM probes of the hero overlays, buttons, sticky nav, section cards, embeds, galleries and footer, the 1440×900 and full-page screenshots, and the page's inline `<style>` blocks and `index.html`. The page uses the Tailwind CDN build (v3 class names), Font Awesome, three.js and GSAP. The hero is `h-screen`, so the full-page screenshot, taken in a tall window, shows only the stretched hero; everything below the fold is described from the DOM probes. The hero text block floats on a 6s up-and-down animation (`translateY` 0 to −10px); it was at −10px when measured.

## Overview

A dark, product-style page (about 6,450px tall) on Tailwind gray-900 (#111827). The first screen is a full-viewport looping video of a 4×4 wall of robot-hand grasping clips, darkened by two stacked gradient scrims: a diagonal black-to-navy-to-purple wash and a bottom-up black fade. Left-aligned at x=48 sit a 60px bold headline "One View, Many Worlds" filled with a cyan gradient (#4facfe → #00f2fe), a 24px white subtitle with the full paper title, three pill buttons (frosted white "Paper" with blue text, a blue-to-purple gradient "Huggingface Demo", a near-black "GitHub Code"), and a 16px light-grey author line. Below the hero a frosted sticky bar holds centred section links. The content is a 1280px column of large cards (12px radius, faint 30px blueprint grid, blue hairline border and blue-tinted shadow) for Abstract with an embedded demo, Method Overview with thumbnails and a figure, an Online Demo iframe, and Experiments with video galleries and a gradient "Load More" button; a gray-900 footer closes the page.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): deep navy and indigo #1a1d3c / #213366 / #17264a / #14122b together 51.8%; slate blue and violet #354278 / #303563 / #272953 together 39.4%; dusty blue #50679d 8.7% (lit video tiles showing through the scrims). The cyan headline and white buttons are too small to form clusters.

Anatomy in DOM order (desktop 1440px):

1. **Hero** (`header.relative.h-screen.overflow-hidden`, 0–900px): `<video class="absolute inset-0 w-full h-full object-cover">` (autoplay, loop, muted) of a tiled clip wall; scrim 1 `background-image: linear-gradient(to right bottom, rgba(0, 0, 0, 0.8), rgba(30, 58, 138, 0.8), rgba(88, 28, 135, 0.7))`; scrim 2 `linear-gradient(to top, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0))` at opacity 0.8. No navbar inside the hero.
2. **Content frame** (`div.absolute.inset-0.flex.flex-col.justify-center.items-start`, padding 48px): the 278px text block (`.animate-float.max-w-7xl`) is vertically centred, starting at y=311 at rest and y=301 at the top of its float.
3. **Headline** (`h1.text-4xl.md:text-6xl > span.gradient-text`, y=301, 60px tall): Inter 60px/700, line-height 1, letter-spacing −1.5px (`tracking-tight`); text filled with `linear-gradient(90deg, #4facfe, #00f2fe)` via `background-clip: text`. Margin-bottom 24px.
4. **Subtitle** (`p.text-xl.md:text-2xl`, y=385, 64px): Inter 24px/400, line-height 32px, #ffffff, max-width 768px, two lines. Margin-bottom 32px.
5. **Buttons** (`div.flex.flex-wrap.gap-3`, y=481, 50px tall, 12px gap): Paper, Huggingface Demo, GitHub Code; Inter 16px/600, padding 12px 24px, radius 9999px. Margin-bottom 24px.
6. **Authors** (`p.text-sm.md:text-base.text-gray-200`, y=555): eight comma-separated links, Inter 16px #e5e7eb; hover underline and #d1d5db.
7. **Sticky nav** (`nav.sticky.top-0`, starts at y=900, just below the fold): 73px, rgba(17,24,39,0.8) with `backdrop-filter: blur(12px)` and a 1px rgba(31,41,55,0.5) bottom border.

Arithmetic check: content frame 900 − 2 × 48 = 804px; (804 − 278) / 2 = 263; 48 + 263 = 311 at rest, 301 at −10px; 301 + 60 + 24 = 385; 385 + 64 + 32 = 481; 481 + 50 + 24 = 555; 555 + 24 = 579 = 301 + 278.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Night | #111827 | (Tailwind `gray-900`) | body, card base colour, GitHub button, footer |
| Card Navy | rgba(10,25,47,0.9) | (literal, `.section-card`) | top layer of every section card |
| Grid Line | rgba(56,182,255,0.1) | (literal) | 1px blueprint grid lines every 30px in cards; card radial glows |
| Card Border | rgba(59,130,246,0.2) | (`border-blue-500/20`) | 1px card border; hover rgba(59,130,246,0.7) |
| Card Shadow | rgba(59,130,246,0.1) | (`shadow-blue-500/10`) | card shadow colour; hover rgba(59,130,246,0.4) |
| Cyan Start | #4facfe | (`.gradient-text`, second rule) | headline and section-heading gradient start |
| Cyan End | #00f2fe | (`.gradient-text`) | gradient end |
| White | #ffffff | (Tailwind) | subtitle, nav links, button text, footer title |
| Frost | rgba(255,255,255,0.9) | (`bg-white/90`) | Paper button fill |
| Blue 600 | #2563eb | (Tailwind) | Paper button text, in-card links, Load More gradient start, nav underline start |
| Blue 500 | #3b82f6 | (Tailwind) | Huggingface button gradient start; active thumbnail outline |
| Purple 600 | #9333ea | (Tailwind) | Huggingface and Load More gradient end |
| Violet 600 | #7c3aed | (literal) | nav hover underline gradient end |
| Navy Scrim | rgba(30,58,138,0.8) | (`via-blue-900/80`) | hero scrim middle stop |
| Purple Scrim | rgba(88,28,135,0.7) | (`to-purple-900/70`) | hero scrim end stop |
| Text Grey | #d1d5db | (`text-gray-300`) | card body text, card h3, thumbnail captions |
| Author Grey | #e5e7eb | (`text-gray-200`) | hero author line |
| Muted Grey | #9ca3af | (`text-gray-400`) | footer subtitle and icons |
| Fine Grey | #6b7280 | (`text-gray-500`) | copyright line |
| Rule Grey | #1f2937 | (`gray-800`) | footer divider; nav link hover fill |
| Button Rim | #374151 | (`border-gray-700`) | GitHub button border |
| Nav Hover | #60a5fa | (`text-blue-400`) | nav link hover text |
| Iframe Rim | #e5e7eb | (`border-gray-200`) | 2px border around the embedded demo |

Declared but not visible: the first `.gradient-text` rule (`linear-gradient(90deg, #2563eb, #7c3aed)`) is overridden by a later `<style>` block, and `.section-card`'s own `box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3)` loses to Tailwind's `shadow-lg` (it returns only through the `:hover` rule).

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| All text | 'Inter', sans-serif (Google Fonts 300–700) | Inter 400, 600, 700 | Inter |
| Icons | Font Awesome | Font Awesome solid and brands | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Headline | `h1.text-4xl.md:text-6xl.font-bold.tracking-tight` | 60px / 700 / 60px, letter-spacing −1.5px | gradient #4facfe → #00f2fe |
| Subtitle | `p.text-xl.md:text-2xl` | 24px / 400 / 32px | #ffffff |
| Hero button | `a.px-6.py-3.rounded-full.font-semibold` | 16px / 600 / 24px | per button |
| Authors | `p.text-sm.md:text-base` | 16px / 400 / 24px | #e5e7eb |
| Nav link | `a.nav-link` | 16px / 400 | #ffffff; hover #60a5fa |
| Section heading | `h2.text-3xl.font-bold.text-center.gradient-text` | 30px / 700 / 36px, centred | gradient #4facfe → #00f2fe |
| Card sub-heading | `h3.text-xl.font-semibold` | 20px / 600 / 28px | #d1d5db |
| Card body | `p.text-gray-300.leading-relaxed` | 16px / 400 / 26px | #d1d5db |
| Thumbnail caption | `p.text-xs` | 12px / 400 / 16px | #d1d5db |
| Footer title | `footer h3.text-2xl` | 24px / 700 / 32px | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 9999px | GitHub only: 1px #374151 | none; hover Tailwind `shadow-lg` and translateY(−4px) |
| Nav links | 9999px | none | none; hover fill #1f2937 and a 2px `linear-gradient(90deg, #2563eb, #7c3aed)` underline growing to full width |
| Section cards | 12px (`rounded-xl`) | 1px rgba(59,130,246,0.2) | `0 10px 15px -3px rgba(59, 130, 246, 0.1), 0 4px 6px -4px rgba(59, 130, 246, 0.1)`; hover `0 15px 30px rgba(59, 130, 246, 0.4)` and translateY(−10px) |
| Embedded demo iframe | 8px | 2px #e5e7eb | Tailwind `shadow` |
| Figures and gallery videos | 8px (`rounded-lg`) | none | Tailwind `shadow` / `shadow-lg` |
| Example thumbnails | 4px | none; active outline 3px #3b82f6, offset 2px | none; hover scale 1.05 |
| Load More | 9999px | none | Tailwind `shadow` |

Card background, quoted literally: `linear-gradient(rgba(10, 25, 47, 0.9), rgba(10, 25, 47, 0.9)), linear-gradient(to right, rgba(56, 182, 255, 0.1) 1px, transparent 1px), linear-gradient(to bottom, rgba(56, 182, 255, 0.1) 1px, transparent 1px)` with `background-size: 100% 100%, 30px 30px, 30px 30px`, `backdrop-filter: blur(10px)`, over #111827; a `::before` adds `radial-gradient(circle at 20% 30%, rgba(56, 182, 255, 0.1) 0%, transparent 40%), radial-gradient(circle at 80% 70%, rgba(56, 182, 255, 0.1) 0%, transparent 40%)`.

## Layout Metrics

- **Hero**: 100vh (900px), content padding 48px (`md:p-12`), text block max-width 1280px (`max-w-7xl`) but subtitle capped at 768px; left-aligned at x=48.
- **Sticky nav**: 73px; inner `.container.mx-auto.px-4.py-4` 1280px at x=80; five links centred with 32px between them (x=419–1021).
- **Main**: `main.container.mx-auto.px-4.py-12`, 1280px at x=80, padding 48px 16px; cards 1248px wide at x=96, padding 32px, 80px apart (`mb-20`).
- **Inside cards**: headings centred across 1182px; text and the demo iframe in an 896px measure at x=272; method figure 709px centred; demo iframe 1152×720 in the Online Demo card.
- **Galleries**: rows of 160–166px video and image tiles with 16px gaps; "Load More" button 209×40, padding 8px 64px.
- **Footer**: #111827, padding 48px 0; title and subtitle left, three icon links right; a 1px #1f2937 rule 32px above the centred copyright.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1280px (1440 render) | hero 48px; container 1280px | 16px | 60px | full layout |
| 1024–1279px | container 1024px | 16px | 60px | same |
| 768–1023px | container 768px | 16px | 60px | same |
| <768px | hero padding 32px (`p-8`); container 16px padding | 16px; authors and buttons 14px (`text-sm`) | 36px (`text-4xl`), subtitle 20px | footer stacks (`flex-col`) |

## Components

- **Video wall hero with double scrim**: full-screen cover video, a diagonal scrim `linear-gradient(to right bottom, rgba(0, 0, 0, 0.8), rgba(30, 58, 138, 0.8), rgba(88, 28, 135, 0.7))` plus a bottom fade `linear-gradient(to top, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0))` at 0.8 opacity; text left-aligned and floating 0–10px on a 6s ease-in-out loop.
- **Gradient headline**: Inter 60px/700, tracking −1.5px, `background: linear-gradient(90deg, #4facfe, #00f2fe); -webkit-background-clip: text; -webkit-text-fill-color: transparent`.
- **Button trio**: 50px pills, padding 12px 24px, 16px/600, 12px apart, leading Font Awesome icon with 8px gap. Primary-light: rgba(255,255,255,0.9) fill, #2563eb text, hover solid white. Gradient: `linear-gradient(to right, rgb(59, 130, 246), rgb(147, 51, 234))`, white text. Dark: #111827 fill, 1px #374151 border, white text. All lift 4px with Tailwind `shadow-lg` on hover, 300ms.
- **Frosted sticky nav**: rgba(17,24,39,0.8), blur(12px), 1px rgba(31,41,55,0.5) bottom rule; pill links 16px white, padding 8px 16px; hover fill #1f2937, text #60a5fa and a gradient underline.
- **Blueprint card** (`.section-card`): #111827 base with the 30px grid and radial glows described above, 1px rgba(59,130,246,0.2) border, 12px radius, 32px padding; centred gradient h2 (30px/700); hover lifts 10px with a blue glow.
- **Example strip**: 96×64 thumbnails with 4px radius and 12px captions; the active one gets a 3px #3b82f6 outline.
- **Load More**: pill with `linear-gradient(to right, rgb(37, 99, 235), rgb(147, 51, 234))`, white 16px text, padding 8px 64px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-screen video hero | yes | tiled clip wall under two gradient scrims |
| Title / subtitle | yes | gradient short title, white full paper title |
| Link buttons | yes | three pills: frosted white, gradient, dark |
| Authors | yes | single light-grey line in the hero |
| Affiliations / venue | absent from the source | neither appears in the hero or cards |
| Sticky section nav | yes | frosted bar below the hero |
| Abstract | yes | blueprint card with an embedded interactive demo |
| Method overview | yes | card with example thumbnails and a figure |
| Online demo | yes | card with a large Hugging Face iframe |
| Experiments | yes | card with video and image galleries and Load More |
| Footer | yes | gray-900 band with title, icons and copyright |
| BibTeX | absent from the source | — |
| Results table | absent from the source | results appear as figures and galleries |

## Adapting to Other Content

- **More authors**: keep a single 16px #e5e7eb line in the hero; at 768px max width it holds about nine names, so wrap to a second line rather than shrinking. Add affiliations as a second 14px #9ca3af line beneath.
- **A venue badge**: add a pill above the headline using the dark button recipe (#111827, 1px #374151 border, 9999px radius, 14px/600 white text), not a new colour.
- **A results table**: place it inside a blueprint card at the 896px measure; header row 14px/600 #ffffff on rgba(59,130,246,0.1), body 16px #d1d5db, 1px rgba(59,130,246,0.2) row rules, best values in #00f2fe.
- **BibTeX**: a card with a #111827 code well, 12px radius, 14px monospace #d1d5db, and the gradient copy button styled like Load More.
- **Long publication or news lists**: rows inside one card, 16px #d1d5db text, dates in 600 #4facfe, 1px rgba(59,130,246,0.2) separators.

## Do's and Don'ts

- Do darken hero video with both scrims; the diagonal wash supplies the navy-to-purple cast.
- Do keep gradient text to the short project name and section headings (#4facfe → #00f2fe).
- Do keep buttons as pills and let only one of them carry the blue-to-purple gradient.
- Do wrap every section in the blueprint card with its 30px grid and blue hairline.
- Don't use #2563eb text links on the dark cards for long passages; it is low contrast there (keep it to short labels).
- Don't introduce light sections; the whole page stays on #111827.
- Don't centre the hero text; it hangs from the left 48px gutter.

## Surfaces

Full-screen scrimmed video; #111827 page; frosted rgba(17,24,39,0.8) sticky nav; navy blueprint cards with a 30px cyan grid at 10% and soft blue glows; white-bordered iframes; #111827 footer with a #1f2937 rule.

## Imagery

A tiled wall of short clips of a robot hand grasping objects outdoors among plants (with pose axes drawn on objects), rendered blue and purple by the scrims; inside, a method diagram, example thumbnails of everyday objects, 3D reconstruction videos and real-robot grasp clips.

## Layout

A full-bleed first screen with left-aligned type, then a centred 1280px column of large stacked cards, each holding centred headings and an 896px text measure. Generous 80px gaps between cards.

## Agent Prompt Guide

Quick colors: page #111827, card navy rgba(10,25,47,0.9), grid rgba(56,182,255,0.1), card border rgba(59,130,246,0.2), headline gradient #4facfe → #00f2fe, button gradient #3b82f6 → #9333ea, text #d1d5db, authors #e5e7eb, white #ffffff.

1. "Build a 100vh hero: cover video, then two overlays: linear-gradient(to right bottom, rgba(0,0,0,0.8), rgba(30,58,138,0.8), rgba(88,28,135,0.7)) and linear-gradient(to top, rgba(0,0,0,0.8), transparent, transparent) at opacity 0.8. Left-aligned content with 48px padding, vertically centred: Inter 60px/700 headline, letter-spacing -1.5px, filled with linear-gradient(90deg, #4facfe, #00f2fe) via background-clip text; 24px/32px #ffffff subtitle max 768px; a 16px #e5e7eb author line."
2. "Create three 50px pill buttons 12px apart, Inter 16px/600, padding 12px 24px: one rgba(255,255,255,0.9) with #2563eb text, one with linear-gradient(to right, #3b82f6, #9333ea) and white text, one #111827 with a 1px #374151 border and white text; hover translateY(-4px) and a large shadow."
3. "Make section cards on #111827: radius 12px, padding 32px, 1px rgba(59,130,246,0.2) border, background linear-gradient(rgba(10,25,47,0.9), rgba(10,25,47,0.9)) over a 30px grid of 1px rgba(56,182,255,0.1) lines, shadow 0 10px 15px -3px rgba(59,130,246,0.1); centred 30px/700 gradient heading (#4facfe → #00f2fe); body 16px/26px #d1d5db in an 896px measure; hover lift 10px and shadow 0 15px 30px rgba(59,130,246,0.4)."

## Similar Pages

- Tailwind-CDN research pages styled like AI product launches (full-screen video, gradient headline, gradient pill buttons, dark cards).
- 3D-generation and pose-estimation project pages that embed a Hugging Face Space as the main demo.

## Quick Start

```css
:root {
  --night: #111827;
  --card: rgba(10, 25, 47, 0.9);
  --grid: rgba(56, 182, 255, 0.1);
  --card-border: rgba(59, 130, 246, 0.2);
  --cyan-start: #4facfe;
  --cyan-end: #00f2fe;
  --btn-from: #3b82f6;
  --btn-to: #9333ea;
  --text: #d1d5db;
  --authors: #e5e7eb;
  --font: 'Inter', sans-serif;
  --container: 1280px;
  --card-radius: 12px;
}
.gradient-text { background: linear-gradient(90deg, var(--cyan-start), var(--cyan-end)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.section-card { border-radius: var(--card-radius); border: 1px solid var(--card-border); background: linear-gradient(var(--card), var(--card)), linear-gradient(to right, var(--grid) 1px, transparent 1px), linear-gradient(to bottom, var(--grid) 1px, transparent 1px); background-size: 100% 100%, 30px 30px, 30px 30px; background-color: var(--night); }
```

## Provenance

- **URL**: https://gzwsama.github.io/OnePoseviaGen.github.io/
- **Paper**: One View, Many Worlds: Single-Image to 3D Object Meets Generative Domain Randomization for One-Shot 6D Pose Estimation (arXiv 2509.07978), Zheng Geng, Nan Wang, Shaocong Xu, Bohan Li, Zhaoxi Chen, Chongjie Ye, Sida Peng, Hao Zhao.
- **Venue**: CoRL 2025 (Oral, per the arXiv comment; the page itself shows no venue).
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 (Oral) and links this project page.
- **Template credit**: none stated; a hand-built single page on the Tailwind CDN with three.js and GSAP; footer reads "© 2025 OnePoseviaGen Research Team".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), DOM probes of overlays, buttons, nav, cards, embeds and footer at 1440, the 1440×900 and full-page screenshots, and the inline `<style>` blocks and `index.html` read directly, on 2026-10-28.
