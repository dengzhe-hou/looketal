# Terracotta Field Journal — Style Reference

> An engineering monograph printed on warm paper, with section numbers in terracotta mono.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

The most fully authored design in this batch. Bulma is still loaded, but a 19KB inline stylesheet replaces nearly every visible rule with an editorial-technical system: warm paper #faf8f3 under a 22px dot grid and an SVG noise grain, Fraunces variable serif for display (optical size 96-144, SOFT axis), IBM Plex Sans for body and IBM Plex Mono for every label. Terracotta #c2410c is the single accent, used on italic words in headings, superscripts, section numbers and button hover. Links are square, ink-filled, uppercase mono buttons that lift with a hard 4px offset shadow on hover. A floating pill navbar, numbered section indices, labeled figure plates and an ink-black footer complete it.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Warm Paper | `#faf8f3` | `--paper` | Page background, under a dot grid of rgba(15,17,21,0.045) |
| Paper Tint | `#f3efe6` | `--paper-tint` | Alternate surface and pillar hover |
| Surface White | `#ffffff` | `--bg-surface` | Figure plates, pillars, video cards |
| Field Ink | `#0f1115` | `--ink` | Text, button fill, footer background, positive compare column |
| Ink Soft | `#1d2025` | `--ink-soft` | Secondary dark |
| Rule Dark | `#2a2d33` | `--rule` | Footer top border |
| Rule Sand | `#e3dccd` | `--rule-soft` | Hairlines, grid gaps, plate borders |
| Terracotta | `#c2410c` | `--primary` | Accent: italic heading words, sup, section numbers, button hover |
| Burnt Terracotta | `#9a330a` | `--primary-dark` | Accent hover/pressed |
| Deep Teal | `#0f766e` | `--secondary` | Secondary accent |
| Amber | `#b45309` | `--accent` | Gradient end (`--gradient-brand` #c2410c to #b45309) |
| Muted Graphite | `#4a4d55` | `--text-muted` | Mono labels, affiliations |
| Light Graphite | `#7c7f87` | `--text-light` | Plate labels, notes |
| Signal Gold | `#fbbf24` | `--star` | Inline color on small superscript glyphs at 0.5em (7 uses; role inferred) |
| Venue Green | `#22c55e` | `--live-dot` | Dot inside the venue badge |

Bulma's palette appears in raw counts but is overridden; the page's own palette is fully declared in `:root`. #15803d appears twice inline (inferred: positive-result marker).

## Tokens — Typography

**Families.** `--font-display: 'Fraunces', ui-serif, Georgia`; `--font-body: 'IBM Plex Sans', system-ui`; `--font-mono: 'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo`. All three from Google Fonts. Body sets `font-feature-settings: "ss01", "cv11"`, line-height 1.65, antialiased. Substitutes: Newsreader or Source Serif 4 for Fraunces; Inter for Plex Sans; JetBrains Mono for Plex Mono.

| Role | Size | Weight | Family / settings |
|---|---|---|---|
| Paper title | clamp(2.4rem, 5.4vw, 4.4rem), line-height 1.02, letter-spacing -0.025em, max 18ch | 380 | Fraunces, opsz 120, SOFT 40 |
| Title emphasis (`em`) | inherit, italic | 360 | Fraunces, SOFT 80, #c2410c |
| Section title | clamp(2rem, 3.6vw, 3rem), line-height 1.05, max 28ch | 380 | Fraunces, opsz 96, SOFT 50 |
| Big metric | 3.4rem, line-height 1, letter-spacing -0.03em | 400 | Fraunces, opsz 144, SOFT 20 |
| Prose | 1.05rem, line-height 1.75, max 68ch | 400 | IBM Plex Sans |
| Authors | 1rem, line-height 1.75 | 400 (names 600) | IBM Plex Sans |
| Section index / hero meta | 0.72rem, uppercase, letter-spacing 0.12-0.18em | 500-600 | IBM Plex Mono |
| Button label | 0.78rem, uppercase, letter-spacing 0.06em | 500 | IBM Plex Mono |
| Plate label | 0.62rem, uppercase, letter-spacing 0.2em | 400 | IBM Plex Mono |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-none | 0 | link buttons, content boxes, video cards |
| --radius-sm | 4px | small controls |
| --radius-md | 6px | inline panels |
| --radius-lg | 10px | larger panels |
| --radius-pill | 9999px / 999px | floating navbar, nav links, venue badge |

**Shadows.** `--shadow-sm: 0 1px 2px 0 rgba(15,17,21,0.06)` on figure plates; `--shadow-md: 0 2px 6px -2px rgba(15,17,21,0.08), 0 8px 24px -12px rgba(15,17,21,0.08)` on the navbar; `--shadow-lg: 0 12px 32px -8px rgba(15,17,21,0.12), 0 24px 48px -16px rgba(15,17,21,0.10)` on plate hover; button hover uses a hard `4px 4px 0 var(--ink)`.

**Layout width.** Sections pad 6rem 1.5rem (4rem 1.25rem under 900px); hero 8rem top, 5rem bottom; prose capped at 68ch; Bulma container widths remain (1152px / 1344px).

## Components

- **Floating navbar.** `.navbar-float`: fixed pill (9999px radius), white, 1px rgba(15,17,21,0.08) border, shadow-md; links Plex Mono 0.82rem lowercase, #4a4d55, pill hover rgba(15,17,21,0.06).
- **Hero meta line.** Mono 0.72rem uppercase row with a pulsing 6px terracotta dot and a 40px #e3dccd rule.
- **Venue badge.** Inline-flex pill, Plex Mono 0.78rem, padding 0.45rem 0.9rem, ink fill with paper text, 6px green #22c55e dot.
- **Link button.** Square (radius 0), 2.6rem high, padding 0 1.25rem, ink fill and border, paper text, mono 0.78rem uppercase; `.is-ghost` transparent with ink text; hover terracotta fill, translate(-2px,-2px), shadow `4px 4px 0 #0f1115`. Labels: View Code, Watch Demo.
- **Section index.** Mono 0.72rem uppercase, letter-spacing 0.18em, terracotta number, flexible 1px sand rule to the right.
- **Figure plate.** White, 1px #e3dccd border, padding 1.25rem, shadow-sm, `data-label` printed top-left in 0.62rem mono; hover shadow-lg and image scale 1.015.
- **Figure caption.** Two-column grid (80px label, body), label in terracotta mono 0.68rem.
- **Pillar grid / video grid.** 1px-gap grids on a sand background so gaps read as hairlines; pillars white, hover #f3efe6; video cards square, ink video background, hover scale 1.02.
- **Metric card.** Fraunces 3.4rem number over a mono uppercase label; `.is-accent` variant inverts to ink.
- **Compare columns.** Negative column white, positive column ink with paper text, mono 0.72rem column heads.
- **Generalization table.** `.gen-table`: full width, collapsed, 0.85rem vertical padding, 1px sand top borders, 58px tag cell.
- **Footer colophon.** Ink background, paper text, 5rem padding, Fraunces 2rem heading, links underlined with rgba(250,248,243,0.3).

## Page Modules

- **Title/author block.** Left-aligned Fraunces title with terracotta italic word, Plex Sans authors with terracotta superscripts, mono affiliations and notes, a faded face image covering the right 52% of the hero.
- **Venue badge.** Ink pill "ICLR 2026" with green dot.
- **Link buttons.** View Code and Watch Demo (no Paper or arXiv button in the link row).
- **Teaser video.** Eight videos across the page in a square-cornered video grid.
- **Narrative sections.** Numbered: motivation, pipeline, three-stage training, feature properties, experiments, real-world tasks, beyond policies.
- **Results.** Metric cards, a component-analysis comparison, one results table (`gen-table`).
- **Footer colophon.** Title, copyright, venue, template credit.
- Not present: BibTeX block, abstract heading, slider, 3D viewer, HF demo.

## Do's and Don'ts

**Do**

- Use one accent (terracotta) and put it on italic words, numbers and superscripts.
- Set every label, index and button in uppercase IBM Plex Mono with wide tracking.
- Draw grid lines with 1px gaps over a sand background rather than borders on each cell.
- Number each section and give each figure a printed plate label.

**Don't**

- Don't round the link buttons; they are square with a hard offset shadow.
- Don't use pure white as the page background; it is warm paper #faf8f3.
- Don't mix in Bulma's blue links or dark pill buttons.
- Don't drop the BibTeX block if you reuse this system (this page omits it).

## Surfaces

Warm paper page with dot grid and grain, white figure plates, paper-tint hover states, ink-black inverted cards and footer.

## Imagery

Point-cloud feature fields rendered as colored parts, robot task videos on ink backgrounds, a desaturated face photo (grayscale 0.15, contrast 0.95, opacity 0.55) fading into the hero.

## Layout

Left-aligned editorial layout: hero text left with image right, then long numbered sections with 3-column pillar grids and auto-fill video grids (min 280px). Collapses to one column under 900px.

## Agent Prompt Guide

**Quick color reference**

- Paper #faf8f3
- Ink #0f1115
- Terracotta #c2410c
- Sand rule #e3dccd
- Muted #4a4d55

**Example component prompts**

1. Create a square link button: 2.6rem tall, fill #0f1115, text #faf8f3, IBM Plex Mono 0.78rem uppercase with 0.06em tracking; on hover fill #c2410c, shift up-left 2px, hard shadow 4px 4px 0 #0f1115.
2. Create a section index row: '02' in #c2410c Plex Mono 0.72rem weight 600, a label in #4a4d55 uppercase with 0.18em tracking, then a 1px #e3dccd rule filling the remaining width.
3. Create a figure plate: white, 1px #e3dccd border, 1.25rem padding, a 0.62rem mono label 'FIG. 3' at top-left, soft shadow that deepens on hover.

## Similar Pages

- Nerfies (credited base, heavily overridden).
- Editorial-style research pages that use Fraunces with IBM Plex.

## Quick Start

```css
:root {
  --ink: #0f1115;
  --paper: #faf8f3;
  --paper-tint: #f3efe6;
  --rule: #2a2d33;
  --rule-soft: #e3dccd;
  --primary: #c2410c;
  --primary-dark: #9a330a;
  --secondary: #0f766e;
  --accent: #b45309;
  --text-muted: #4a4d55;
  --text-light: #7c7f87;
  --shadow-sm: 0 1px 2px 0 rgba(15,17,21,0.06);
  --shadow-md: 0 2px 6px -2px rgba(15,17,21,0.08), 0 8px 24px -12px rgba(15,17,21,0.08);
  --shadow-lg: 0 12px 32px -8px rgba(15,17,21,0.12), 0 24px 48px -16px rgba(15,17,21,0.10);
  --radius-sm: 4px; --radius-md: 6px; --radius-lg: 10px;
  --font-display: 'Fraunces', ui-serif, Georgia, serif;
  --font-body: 'IBM Plex Sans', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', ui-monospace, Menlo, monospace;
}
body { font-family: var(--font-body); background: var(--paper);
  background-image: radial-gradient(rgba(15,17,21,0.045) 1px, transparent 1px); background-size: 22px 22px;
  color: var(--ink); line-height: 1.65; }
```

## Provenance

- URL: https://pa3ff.github.io/
- Paper: Learning Part-Aware Dense 3D Feature Field for Generalizable Articulated Object Manipulation (Yue Chen et al.), arXiv 2602.14193.
- Venue: ICLR 2026 (per the arXiv comment, and stated in the footer colophon). Field: robot manipulation.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: footer says "Template adapted from NeRFies"; the visible design is a custom inline system on top of Bulma.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified. All palette values come from the page's own `:root` declaration.
