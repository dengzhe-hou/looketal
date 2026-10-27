# ReMind Editorial Blue — Style Reference

> A full-page lab advert in a science weekly, one blue ink and a wall of video.

**Theme:** light

Values are read from the page's own stylesheets (`assets/css/styles.css`, the Applied Intuition "Research Website Template" core, and `site.css` overrides). The CSS is fully tokenized, so most hex codes below are declared custom properties rather than frequency guesses. Roles are interpreted from usage.

## Overview

ReMind is a corporate-lab research page (Applied Intuition) built on an in-house design system whose own header comment describes a white, editorial page with a single accent. The palette is ink `#111111`, grays, and Applied Blue `#006CFA`, used only for the accent half of the title, numbers, focus rings and hover. Prose is set in the XCharter serif; headlines in Applied Sans Display; labels in mono ALL-CAPS eyebrows preceded by a small black square. A frosted-glass pill header floats above the page. The body is dominated by 68 videos in 4-, 5- and 6-column grids, each in a 16:9-ish dark mat frame. Sections are numbered (`01 · Out-of-sight state evolution` … `07 · Citation`) and alternate white and `#f6f7f9`.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Applied Blue | `#006CFA` | `--blue` | The one accent: title accent span, contribution numbers, hover, focus |
| Deep Applied | `#0052bd` | `--blue-dark` | Primary button hover |
| Steel Blue | `#3d7fc4` | `--blue-muted` | Pending/placeholder text |
| Blue Wash | `#eef4ff` | `--blue-wash` | Light blue surface |
| Highlighter | `#e0ecff` | `--blue-wash-2` | `mark.hl` marker swipe under key claims |
| Press Ink | `#111111` | `--ink` | Headlines, body text, footer background |
| Standfirst Gray | `#2a2a2a` | (literal) | `.lead` paragraphs |
| Caption Gray | `#767676` | `--gray` | Eyebrows, nav links, captions, byline |
| Hairline | `#e4e4e4` | `--gray-line` | Section rules, button borders, frame borders |
| Soft Band | `#f6f7f9` | `--gray-soft` | Alternating section background |
| Paper | `#ffffff` | `--white` | Page background |
| Video Mat | `#0d1117` | `--dark-mat` | Background behind every video |
| Terminal | `#0f1115` | (literal) | BibTeX block background |
| Terminal Text | `#e7e9ee` | (literal) | BibTeX text |
| Footer Text | `#cfd3da` | (literal) | Footer copy on ink |

Chart series tokens (`--series-1` `#1f2937` to `--series-4` `#c3c9d2`, blue sequential ramp `#003a86`…`#cfe1fe`) are defined but this page has no charts.

## Tokens — Typography

- **Display:** `Applied Sans Display` 600/700 (vendored TTF). Substitute: Helvetica Neue, Inter Display.
- **UI / labels:** `Applied Sans Text` 400/600. Substitute: Helvetica Neue, Inter.
- **Prose:** `XCharter` serif (vendored OTF). Substitute: Charter, Georgia.
- **Mono:** `SFMono-Regular`, JetBrains Mono, Menlo.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Hero title | `clamp(2.05rem, 5vw, 3.6rem)`, max 25ch | 700 | 1.04 | letter-spacing -0.02em |
| Hero lead | `clamp(1.25rem, 2.2vw, 1.5rem)` serif | 400 | 1.45 | max 56–64ch |
| h2 | 2.2rem | 600 | 1.12 | -0.01em, max 22ch |
| h3 | 1.18rem | 600 | 1.12 | |
| Body | 1.0625rem (~17px) serif | 400 | 1.62 | hyphenated |
| Eyebrow | 0.86rem mono | 400 | | uppercase, 0.16em tracking |
| Meta / buttons / nav | 0.82rem | 600 | | |
| Tile label | 0.72rem | 600 | | uppercase, 0.03em |
| BibTeX | 0.8rem mono | 400 | 1.55 | |

## Tokens — Spacing & Shapes

Spacing scale: 0.5, 1, 1.5, 2.5, 4, 6rem (`--space-1`…`--space-6`).

| Element | Radius |
|---|---|
| Header pill, brand mark | 999px |
| Media frame, cards, BibTeX (`--radius`) | 10px |
| Showcase tile frame | 5px (`--radius / 2`) |
| Buttons | 8px |
| Copy button | 6px |

- **Shadows:** `--shadow: 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07)` on header and large frames; `--shadow-lift` adds a blue `rgba(0,108,250,.10)` glow. Grid tiles have no shadow.
- **Layout:** `--wide` 1280px, `--reading` 720px, 24px side padding; header height 60px, inset 14px.

## Components

- **Floating header.** Fixed, inset 14px; inner pill with `rgba(255,255,255,.72)`, `backdrop-filter: saturate(160%) blur(14px)`, 1px `rgba(17,17,17,.07)` border. Nav links 0.82rem gray, active link ink 600.
- **Eyebrow.** Mono uppercase gray label with a 0.5em black square before it; doubles as the section number.
- **Button (`.btn`).** White, 1px `#e4e4e4` border, 8px radius, 0.6em 1.05em padding, 0.82rem/600, label plus `↗`. Hover turns border and text blue. All four links (Code, arXiv, Models, Dataset) use the outline variant.
- **Contribution triad.** Three columns, each with a 2px blue top rule and a 1.6rem blue display numeral.
- **Showcase tile.** Figure with a dark-mat video frame (aspect 832/480) and a gray caption whose label is uppercase 0.72rem.
- **BibTeX.** Dark `#0f1115` block, 10px radius, copy button top-right that turns blue on hover.
- **Footer.** Ink background, `#cfd3da` text, white links, white brand mark.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Left-aligned display title with blue accent clause; mono byline under a hairline rule |
| Venue badge | No visible badge in hero (inferred from markup) | |
| Link buttons | Code, arXiv, Models (HF), Dataset (HF) | Outline buttons with `↗` |
| Teaser | Video grids directly after hero | Dark-mat frames |
| Abstract | Lead paragraph instead of a labeled abstract | Serif standfirst |
| Method | Section 06 with three h3 items (PM-RoPE, Node Drop, data engine) | Muted paragraphs |
| Results | Five numbered video showcases, 68 videos total | 4/5/6-column grids |
| Tables / sliders / 3D / HF Space | No | |
| BibTeX | Yes | Dark code block with copy button |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep blue to one job per view: accent, number, or hover.
- Do number every section with a mono eyebrow.
- Do frame every video on the `#0d1117` mat with `object-fit: contain`.
- Don't add a second hue; the system's categorical palette is marked optional and unused here.
- Don't center text; the layout is left-aligned and editorial.

## Surfaces

White hero, alternating `#f6f7f9` content bands separated by 1px `#e4e4e4` rules, dark mats for media, ink footer.

## Imagery

All imagery is autoplaying video. No static figures.

## Layout

1280px wide column with 720px reading measure for prose. Showcase headings use a 0.6fr / 1.4fr two-column grid. Contribution triad collapses to one column under 860px.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f6f7f9`, ink `#111111`, gray `#767676`, line `#e4e4e4`, accent `#006CFA`, mat `#0d1117`.

1. "Create a numbered section eyebrow: mono 0.86rem uppercase, 0.16em tracking, `#767676`, preceded by a 0.5em black square, then a 2.2rem/600 display h2 capped at 22ch."
2. "Build a 6-column video grid with 0.5rem gaps; each tile is a 5px-radius frame on `#0d1117`, caption below in gray with an uppercase 0.72rem/600 label."
3. "Make outline link buttons: white, 1px `#e4e4e4` border, 8px radius, 0.82rem/600 ink text with `↗`; on hover the border and text turn `#006CFA`."

## Similar Pages

Corporate-lab editorial pages (e.g. Google Research blog-style project pages); Auteur and Which Way Did It Move in this collection share the tokenized, single-accent approach.

## Quick Start

```css
:root {
  --blue: #006CFA; --blue-dark: #0052bd; --blue-wash-2: #e0ecff;
  --ink: #111111; --gray: #767676; --gray-line: #e4e4e4;
  --gray-soft: #f6f7f9; --white: #ffffff; --dark-mat: #0d1117;
  --font-display: "Applied Sans Display", "Helvetica Neue", Arial, sans-serif;
  --font-sans: "Applied Sans Text", "Helvetica Neue", Arial, sans-serif;
  --font-serif: "XCharter", Georgia, serif;
  --font-mono: "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  --fs-body: 1.0625rem; --fs-h2: 2.2rem; --fs-meta: 0.82rem;
  --reading: 720px; --wide: 1280px; --radius: 10px;
  --shadow: 0 1px 2px rgba(17,17,17,.04), 0 8px 28px rgba(17,17,17,.07);
}
```

## Provenance

- **URL:** https://remind-applied.github.io/
- **Paper:** Teaching Video Generators to Remember (arXiv 2605.25333), Tianshuo Xu et al. The live page title ends "…for Out-of-Sight State Evolution", slightly different from the arXiv title in the batch list.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** Applied Intuition "Research Website Template" (Apache-2.0 header in `styles.css`); no third-party academic template.
- **Measurement method:** static HTML and two stylesheets parsed with `extract_style.py`, tokens read directly from `:root`. Rendered page not viewed; whether a venue label appears in the hero is not confirmed.
