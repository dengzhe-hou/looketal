# Violet Starfield Showcase — Style Reference

> A night-sky opening with a shimmering lavender title, then bright white rooms with violet underlines.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (computed styles of the fixed nav, starfield canvas, hero title, authors, buttons, section titles, abstract, citation block and footer, plus a first-viewport color quantization), the first-viewport screenshot and a scaled full-page capture, and the page's own `static/css/style.css` with its HTML. Positions are document coordinates at 1440px wide. Content blocks use a scroll-reveal (`.reveal`, opacity 0 and 30px down until intersected), so in the captures the abstract box and the lower method figure appear faded or blank; their values come from CSS and computed styles.

## Overview

The Stackelberg Speaker is a hand-built single page in Inter. A fixed full-viewport canvas paints a starfield over a dark navy gradient; the hero is transparent over it, with three blurred violet, purple and pink orbs and a faint 60px grid that pulses. The title is 33.6px weight 800, filled with an animated lavender-to-periwinkle gradient clipped to the text. Authors are light slate, separated by middle dots; the affiliation is italic violet at 70% opacity. Four 10px-radius buttons sit below: an indigo-to-violet gradient "Paper" with a violet glow, and three glassy dark ones. The rest of the page is light: white and #f8fafc sections, each titled with a centered 32px bold heading over a 60px indigo-to-violet gradient bar. The abstract is a softly tinted, quote-marked box; the motivation pairs a hand-drawn figure with gradient-text subheads; the method has a wide hand-drawn strip and step cards; benchmarks are four emoji cards with colored top edges; the citation is a dark navy block.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): white #ffffff 42.1% (the Abstract section below y 527), indigo night #1d193c 13.5%, near-black #0b0c1e 9.7%, #181738 8.5%, #141633 8.1%, #11122b 7.5%, #0e1227 7.2% (the starfield gradient and orb glows), dusky violet #424069 3.5%. The dark hero fills the top 527px; the indigo button and lavender title are the only saturated marks.

Anatomy in DOM order (y = top of element box):

1. **Navbar** (`nav.navbar`), y 0, fixed, 1440×61, transparent with padding 12.8px 0; after scrolling it becomes rgba(10,10,26,0.85) with 20px blur, a 1px rgba(99,102,241,0.1) bottom border and padding 8px 0. Inner `.nav-container` max-width 1100px, padding 0 32px.
2. **Logo text** (`a.nav-logo`), x 202, "Stackelberg Speaker", Inter 15.2px/700, rgba(255,255,255,0.9), letter-spacing -0.01em. **Nav links** right, Inter 13.6px/500 rgba(255,255,255,0.6), padding 6.4px 13.6px, radius 8px; active link #c7d2fe on rgba(99,102,241,0.15).
3. **Starfield** (`canvas#starry-bg`), fixed 1440×900 behind everything, `linear-gradient(180deg, #0a0a1a 0%, #0d1127 40%, #111827 100%)` with drawn white stars. Hero top padding 144px.
4. **Title** (`h1.hero-title`), y 144, max-width 800px, three lines, Inter 33.6px/800, line-height 42px, centered, text filled by `linear-gradient(135deg, #e0e7ff, #a5b4fc 25%, #c4b5fd 50%, #93c5fd 75%, #e0e7ff)` that shifts over 6s. Gap 24px.
5. **Authors** (`p.hero-authors`), y 294, "Zhang Zheng · Deheng Ye · Peilin Zhao · Hao Wang", Inter 16.8px/400, #cbd5e1, letter-spacing 0.02em. Gap 9.6px.
6. **Affiliation** (`p.hero-affiliation`), y 332, Inter 14.72px italic, rgba(167,139,250,0.7). Gap 40px.
7. **Buttons** (`.hero-links`), y 397, four 50px buttons, gap 13.6px: "Paper" with a 135° #6366f1 → #8b5cf6 gradient, white text, shadow 0 4px 15px rgba(99,102,241,0.35); "Code", "Data", "Models" with rgba(255,255,255,0.06) fill, 1px rgba(255,255,255,0.12) border, #e2e8f0 text; all Inter 15.2px/600, padding 11.2px 24px, radius 10px, Font Awesome icons left. Hero bottom padding 80px.
8. **Abstract section** (`section.section`), from y 527 on #ffffff, padding 80px; centered title "Abstract" at y 607 with the gradient bar under it. The abstract box below had not yet revealed in the capture.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Night Top | #0a0a1a | `#starry-bg` gradient 0% | Starfield background top |
| Night Mid | #0d1127 | gradient 40% | Starfield background middle |
| Night Base | #111827 | gradient 100% | Starfield background bottom |
| Indigo | #6366f1 | `--primary` | Paper button gradient start, section-title bar start, step numbers, game tag text, gradient subheads, abstract quote mark (15% opacity) |
| Violet | #8b5cf6 | `--accent` | Paper button gradient end, section-title bar end |
| Indigo Dark | #4f46e5 | `--primary-dark` | Bold phrases in motivation text |
| Indigo Light | #e0e7ff | `--primary-light` | Game tag fill, title gradient ends |
| Periwinkle | #a5b4fc | title gradient | Hero title gradient stop |
| Lavender | #c4b5fd | title gradient | Hero title gradient stop |
| Sky | #93c5fd | title gradient | Hero title gradient stop |
| Nav Active | #c7d2fe | `.nav-link.active` | Active nav link, logo hover |
| Author Slate | #cbd5e1 | `.hero-authors` | Hero author line |
| Affiliation Violet | rgba(167,139,250,0.7) | `.hero-affiliation` | Hero affiliation |
| Button Text | #e2e8f0 | `.btn-secondary` | Secondary hero button text, citation text |
| White | #ffffff | `--bg` | Section backgrounds, cards |
| Alt Band | #f8fafc | `--bg-alt` | Motivation and Benchmarks sections, footer |
| Text | #1e293b | `--text` | Section titles, card titles, bold text; citation gradient start |
| Text Secondary | #64748b | `--text-secondary` | Abstract and body paragraphs, captions, footer |
| Border | #e2e8f0 | `--border` | Card borders, footer top rule, faded rule atop alt sections |
| Citation Navy | #0f172a | `.citation-block` gradient end | Citation block (135° from #1e293b) |
| Pink | #ec4899 | `--accent-pink` | Third hero orb (10–12% alpha) |
| Cyan | #06b6d4 | `--accent-cyan` | Benchmark card top-edge gradients |

## Tokens — Typography

- **All text**: declared `'Inter', -apple-system, BlinkMacSystemFont, sans-serif`. Rendered: Inter 400, 500, 600, 700, 800 (`fonts_loaded`). Substitute: Manrope at weight 800 for the title (similar geometric heaviness), otherwise system-ui.
- **Mono**: `'JetBrains Mono', monospace` for the BibTeX block (400 loaded).
- **Icons**: Font Awesome 6.5.1 for buttons and copy; emoji for benchmark cards.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Hero title | `.hero-title` | 33.6px (2.1rem) / 42px | 800 | gradient fill (#e0e7ff → #a5b4fc → #c4b5fd → #93c5fd) |
| Section title | `.section-title` | 32px (2rem) / 54.4px, centered | 700 | #1e293b |
| Subsection | `.subsection-title` | 21.6px (1.35rem) | 600 | #1e293b |
| Motivation subhead | `.motivation-text h3` | 20.8px (1.3rem) | 700 | gradient #6366f1 → #8b5cf6 text |
| Game card title | `.game-card h3` | 18.4px | 600 | #1e293b |
| Step card title | `.step-card h3` | 17.6px (1.1rem) | 600 | #1e293b |
| Abstract, method intro | `.abstract-text`, `.method-intro` | 16.8px (1.05rem) / 1.85 | 400 | #64748b |
| Hero authors | `.hero-authors` | 16.8px, 0.02em | 400 | #cbd5e1 |
| Body | `body`, `.motivation-text p` | 16px / 1.7–1.8 | 400 | #1e293b / #64748b |
| Button | `.btn` | 15.2px (0.95rem) | 600 | #ffffff / #e2e8f0 |
| Logo | `.nav-logo` | 15.2px, -0.01em | 700 | rgba(255,255,255,0.9) |
| Hero affiliation | `.hero-affiliation` | 14.72px italic | 400 | rgba(167,139,250,0.7) |
| Caption, step text | `.figure-caption`, `.step-card p` | 14.72px / 1.6 | 400 | #64748b |
| Footer | `.footer` | 14.4px | 400 | #64748b |
| Nav link | `.nav-link` | 13.6px (0.85rem) | 500 | rgba(255,255,255,0.6) |
| BibTeX | `.citation-block pre` | 13.6px / 1.7 | 400 mono | #e2e8f0 |
| Game tag | `.game-tag` | 12.48px | 600 | #6366f1 on #e0e7ff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero buttons | 10px (`--radius-sm`) | primary none; secondary 1px rgba(255,255,255,0.12) | primary 0 4px 15px rgba(99,102,241,0.35); hover 0 8px 25px rgba(99,102,241,0.5) |
| Nav links | 8px | none | none |
| Abstract box | 16px (`--radius`) | 1px rgba(99,102,241,0.08) | none; fill 3% indigo-to-violet gradient |
| Figures (`.figure-img`, motivation image) | 16px | none | `--shadow-lg`: 0 10px 40px rgba(0,0,0,0.08) |
| Step and game cards | 16px | 1px #e2e8f0, 3px gradient top edge (game cards always, step cards on hover) | hover 0 12px 40px rgba(99,102,241,0.1) or rgba(0,0,0,0.08) |
| Step number | 50% (44px circle) | none | 0 4px 12px rgba(99,102,241,0.3) |
| Section-title bar | 2px | none (60×3px gradient) | none |
| Game tag | 999px | none | none |
| Citation block | 16px | 1px rgba(99,102,241,0.15) | 0 0 30px rgba(99,102,241,0.08) |
| Copy button | 8px | 1px rgba(255,255,255,0.12) | none |

## Layout Metrics

- **Container**: `.container` and `.nav-container` max-width 1100px, padding 0 32px, so content spans x 202–1238 (1036px).
- **Hero**: padding 144px 0 80px, centered; title max-width 800px; authors 24px below the title; affiliation 40px above the buttons; button gap 13.6px.
- **Sections**: padding 80px 0; section titles 40px above content; alt sections get a 1px fading #e2e8f0 rule on top.
- **Abstract**: box max-width 850px (768px of text at x 336), padding 32px 40px, quote glyph 64px Georgia at top left.
- **Motivation**: grid `auto 1fr`, gap 48px, max-width 900px; image column max 380px.
- **Method**: intro max-width 850px centered; full-width figure with 16px radius; step cards in three columns, gap 24px, padding 32px 24px.
- **Benchmarks**: four cards per row, gap 24px. **Citation**: max-width 750px, padding 24px 32px.
- Rendered height about 5,190px at 1440px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >900px | 32px inside a 1100px container | 16px | 33.6px | layout as described |
| 601–900px | 32px | 16px | 25.6px (1.6rem) | logo hidden; nav links 12.48px; motivation stacks (image max 320px); step cards one column; game cards two columns |
| ≤600px | 16px | 16px | 20.8px (1.3rem) | hero padding 112px 0 48px; sections 48px; section titles 25.6px; game cards one column; buttons stack; abstract padding 24px |

## Components

- **Gradient primary button**: inline-flex, gap 8px, padding 11.2px 24px, 10px radius, `linear-gradient(135deg, #6366f1, #8b5cf6)`, white Inter 15.2px/600, shadow 0 4px 15px rgba(99,102,241,0.35); hover lifts 2px with a stronger glow.
- **Glass secondary button**: same shape, rgba(255,255,255,0.06) fill with 10px backdrop blur, 1px rgba(255,255,255,0.12) border, #e2e8f0 text; hover fill 0.12 and border 0.25.
- **Gradient text title**: Inter 800, `background-clip: text` with the five-stop lavender gradient at 200% size, animated position.
- **Section title with bar**: Inter 32px/700 #1e293b centered, followed by a 60×3px `linear-gradient(90deg, #6366f1, #8b5cf6)` bar 12px below, 2px radius.
- **Quoted abstract box**: max 850px, padding 32px 40px, 16px radius, 3% indigo-to-violet gradient fill, 1px rgba(99,102,241,0.08) border, a 64px Georgia “ in #6366f1 at 15% opacity; text 16.8px/1.85 #64748b with #1e293b 600 bold phrases.
- **Benchmark card**: white, 1px #e2e8f0, 16px radius, padding 32px 24px, centered; a 3px top edge gradient per card (red-orange, indigo-violet, cyan-blue, emerald-cyan); 44.8px emoji, 18.4px/600 title, 14.08px #64748b text, a #e0e7ff pill tag in #6366f1 that fills on hover.
- **Step card**: white, 1px #e2e8f0, 16px radius, centered; 44px circular gradient number with glow; hover lifts 5px and shows a gradient top edge.
- **Citation block**: `linear-gradient(135deg, #1e293b, #0f172a)`, 16px radius, 1px rgba(99,102,241,0.15) border, soft violet glow, JetBrains Mono 13.6px #e2e8f0, a glass copy button at top right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed navbar | yes | transparent over the hero, dark glass after scroll |
| Starfield hero | yes | canvas stars, orbs, pulsing grid |
| Title, authors, affiliation | yes | gradient title, dotted author line, italic violet affiliation |
| Venue badge | absent from the source | the venue appears only in the footer ("ACL 2026") |
| Link buttons | yes | one gradient, three glass |
| Abstract | yes | quoted tinted box |
| Motivation | yes | image beside gradient-headed text |
| Method figure and steps | yes | wide hand-drawn strip, detailed diagram, step cards |
| Benchmarks | yes | four emoji cards with colored top edges |
| Results table | absent from the source | none |
| BibTeX | yes | dark navy gradient block |
| Footer | yes | #f8fafc band, one centered line |

## Adapting to Other Content

- **More authors**: keep the single dotted line in #cbd5e1; when it wraps past two lines, add numbered superscripts and move affiliations into the italic violet line.
- **A venue badge**: add a small glass pill above the title using the secondary-button recipe at 12.48px.
- **A results table**: put it on a white card (16px radius, 1px #e2e8f0) with a #f8fafc header row, #1e293b 600 labels, #64748b numbers, and the method row tinted rgba(99,102,241,0.06) with bold #4f46e5 values.
- **Videos**: present them like figures: 16px radius, `--shadow-lg`, centered, caption 14.72px #64748b.
- **Long publication lists or news**: a white card list on the #f8fafc band with 600 titles and #e0e7ff tag pills for venues.

## Do's and Don'ts

- Do keep the dark starfield only behind the hero; every section below is light.
- Do use the indigo-to-violet gradient for the primary button, the section-title bars, step numbers and subheads, and nowhere else.
- Do round cards, figures and the citation block at 16px and buttons at 10px.
- Do keep body copy in #64748b with #1e293b only for headings and bold phrases.
- Don't fill the title with a flat color; it is always the lavender gradient.
- Don't add more than one gradient button per row.
- Don't put hard borders around figures; use the soft large shadow.

## Surfaces

A fixed navy-black starfield canvas (#0a0a1a → #111827) behind a transparent hero with violet and pink blurred orbs; white and #f8fafc sections; white cards with #e2e8f0 borders; a pale indigo-tinted abstract box; a dark #1e293b → #0f172a citation block; a #f8fafc footer.

## Imagery

Hand-drawn stick-figure illustrations in black ink with pale teal and peach blobs (players, leader and follower at a table, light-bulb insight), plus a detailed method diagram. Figures sit on white with 16px corners and soft shadows. Emoji (🐺 and others) identify the benchmark games.

## Layout

A 1100px container. The hero is centered on the starfield; sections below center their titles and either center text (abstract, method intro) or use two-column (motivation), three-column (steps) and four-column (games) grids. Rendered height about 5,190px.

## Agent Prompt Guide

Quick colors: night #0a0a1a → #0d1127 → #111827, indigo #6366f1, violet #8b5cf6, title gradient #e0e7ff / #a5b4fc / #c4b5fd / #93c5fd, author #cbd5e1, text #1e293b, secondary #64748b, border #e2e8f0, alt band #f8fafc.

1. "Build a centered hero over a fixed dark canvas (linear-gradient(180deg, #0a0a1a, #0d1127 40%, #111827) with white stars), padding 144px 0 80px: an Inter 33.6px weight-800 title max 800px wide, filled with linear-gradient(135deg, #e0e7ff, #a5b4fc, #c4b5fd, #93c5fd, #e0e7ff) via background-clip text; authors 16.8px #cbd5e1 separated by ' · '; an italic 14.72px rgba(167,139,250,0.7) affiliation."
2. "Add hero buttons, 10px radius, padding 11.2px 24px, Inter 15.2px/600 with a Font Awesome icon: the first with linear-gradient(135deg, #6366f1, #8b5cf6), white text and shadow 0 4px 15px rgba(99,102,241,0.35); the others rgba(255,255,255,0.06) with a 1px rgba(255,255,255,0.12) border and #e2e8f0 text; hover lifts 2px."
3. "Add a section on white with 80px padding: a centered Inter 32px/700 #1e293b title with a 60×3px linear-gradient(90deg, #6366f1, #8b5cf6) bar 12px below; then a max-850px box with 16px radius, 1px rgba(99,102,241,0.08) border, a faint indigo gradient fill, padding 32px 40px and 16.8px #64748b text at line-height 1.85."

## Similar Pages

- "Dark hero, light body" project pages with canvas particle backgrounds and gradient-text titles.
- Tailwind-palette landing pages (slate and indigo) adapted to papers.

## Quick Start

```css
:root {
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --primary-light: #e0e7ff;
  --accent: #8b5cf6;
  --bg: #ffffff;
  --bg-alt: #f8fafc;
  --text: #1e293b;
  --text-secondary: #64748b;
  --border: #e2e8f0;
  --shadow-lg: 0 10px 40px rgba(0, 0, 0, 0.08);
  --radius: 16px;
  --radius-sm: 10px;
  --night: linear-gradient(180deg, #0a0a1a 0%, #0d1127 40%, #111827 100%);
  --title-fill: linear-gradient(135deg, #e0e7ff 0%, #a5b4fc 25%, #c4b5fd 50%, #93c5fd 75%, #e0e7ff 100%);
  --font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

## Provenance

- **URL**: https://3dagentworld.github.io/leader_follower/
- **Paper**: The Stackelberg Speaker: Optimizing Persuasive Communication in Social Deduction Games (arXiv 2510.09087), Zhang Zheng, Deheng Ye, Peilin Zhao, Hao Wang (The Hong Kong University of Science and Technology (Guangzhou)).
- **Venue**: ACL 2026.
- **Selection reason**: arXiv 2510.09087 comment states acceptance at ACL 2026; project page linked in the abstract. Chosen for the dark starfield hero with violet accents, centered section heads with underline bars, and the image-plus-text motivation block and hand-drawn method strip.
- **Template credit**: none; the stylesheet is titled "The Stackelberg Speaker - GitHub Pages Style".
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and first-viewport anatomy, first-viewport screenshot and scaled full-page capture (lower content caught mid scroll-reveal), `static/css/style.css` and `index.html`. Date 2026-10-28.
