# Prism Title Docs — Style Reference

> A clean product documentation site whose title catches light through a rotating prism.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

Bulma is loaded but the page runs on its own token sheet (`:root` with --bg, --line, --text, --link, --accent, --radius 16px). Spoqa Han Sans Neo, self-hosted in 400/500/700, sets every word. A sticky translucent nav bar with section links sits on top. The title is the showpiece: a conic gradient (navy, royal blue, sand, peach, coral, raspberry, back to navy) rotates behind it every 8s, masked so it shows only on selection-like highlight. Below, the page reads like docs: uppercase blue venue line, TL;DR with a 3px blue left rule, hairline-separated sections, wide scrollable comparison tables with a sticky first column, and a BibTeX block with a copy button that turns green.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Soft Well | `#f7f7f8` | `--bg-soft` | Formula box and BibTeX `pre` |
| Hairline | `#e3e5e8` | `--line` | Section dividers, table rows, BibTeX border |
| Strong Hairline | `#d4d8de` | `--line-strong` | Button borders, table top/bottom |
| Slate Ink | `#1f2937` | `--text` | Body text |
| Title Black | `#121212` | `--title` | Paper title color |
| Muted Slate | `#4b5563` | `--muted` | Affiliations, captions, nav links |
| Royal Link | `#2563eb` | `--link` | Venue line, author links, TL;DR rule |
| Deep Teal | `#0f766e` | `--accent` | `.card-label` uppercase labels |
| Paper Button Blue | `#1d4ed8` | `--btn-paper` | Paper button text on #eef4ff |
| arXiv Brick | `#b91c1c` | `--btn-arxiv` | arXiv button text on #fff3f2 |
| Copied Green | `#166534` | `--ok` | Copy button after copy (#f0fdf4 fill, #86efac border) |
| Prism Navy | `#1d243a` | `--prism-0` | Conic gradient start and end |
| Prism Coral | `#f46e5a` | `--prism-mid` | Conic gradient middle (with #3757cf, #ffd06b, #c03764 and others) |

The conic gradient runs #1d243a, #3757cf, #768fde, #f4e4bb, #ffd06b, #ffb269, #fe8b71, #f46e5a, #c03764, #fdedf7, #f9e17e, #c6d6fb, #5156b9, #1d243a. A blurred inset glow #6e6eff sits in the selection overlay.

## Tokens — Typography

**Families.** "Spoqa Han Sans Neo" (self-hosted woff2, 400/500/700/800 in use) for everything; monospace for BibTeX; MathJax for symbols in headings. Substitutes: Pretendard or Inter.

| Role | Size | Weight | Notes |
|---|---|---|---|
| Paper title | clamp(2.05rem, 3.7vw, 3.2rem), line-height 1.28, letter-spacing -0.03em, max 24ch | 700 (inferred) | #121212 |
| Venue line | 0.95rem, uppercase, letter-spacing 0.08em | 800 | #2563eb |
| Section title | clamp(1.6rem, 2.3vw, 2.1rem), line-height 1.15, letter-spacing -0.02em | 700 (inferred) | |
| Sub-heading (`h3`) | 1.15rem, line-height 1.35 | 700 (inferred) | |
| Authors | 1.04rem, line-height 1.9 | 400 | links #2563eb |
| Body | 1rem, line-height 1.82 | 400 | |
| TL;DR | 1.03rem, line-height 1.85 | 400 | 3px left rule |
| Nav link | 0.92rem | 600 | |
| Card label | 0.8rem, uppercase, letter-spacing 0.08em | 800 | #0f766e |
| BibTeX code | 0.95rem, line-height 1.7 | 400 | monospace |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius | 16px | declared base radius (large panels) |
| --radius-btn | 12px | `.pub-btn` link buttons |
| --radius-sm | 10px | copy button, BibTeX `pre` |
| --radius-select | 12px | title selection overlay |

**Shadows.** `--shadow: 0 8px 24px rgba(15, 23, 42, 0.05)`, shown on link button hover with a 1px lift.

**Layout width.** Hero pads 3.25rem top, 1.5rem bottom; sections 1.25rem top, 1.75rem bottom; text blocks capped at 54rem; authors 48rem; affiliations 52rem; comparison tables min-width 2200px inside a horizontal scroller.

## Components

- **Sticky nav.** `.site-nav`: sticky top, rgba(255,255,255,0.96) with 10px backdrop blur, 1px #e3e5e8 bottom border; brand uppercase 1rem weight 800; links 0.92rem 600 #4b5563 with a 2px underline that turns #1f2937 when active.
- **Prism title.** Title wrapped in `.publication-title-highlight` with an absolutely placed 960px conic gradient rotating 8s linear infinite, masked; selection overlay blurred 12px with hard-light blend.
- **Link button.** `.pub-btn`: inline-flex, gap 0.55rem, padding 0.8rem 1rem, radius 12px, 1px #d4d8de, 0.95rem weight 700; Paper #1d4ed8 on #eef4ff, arXiv #b91c1c on #fff3f2, Code #1f2937 on #f8fafc. Labels: arXiv, Code, Citation.
- **TL;DR.** 1rem left padding, 3px solid #2563eb left border.
- **Section header.** 1.2rem top padding with a 1px #e3e5e8 top border; no card.
- **Method flow.** Grid `1fr 120px 1fr` with an animated SVG arrow (base fill rgba(37,99,235,0.2)).
- **Formula box.** #f7f7f8 strip with hairline top and bottom borders, horizontal scroll.
- **Comparison table.** Separate borders, #d4d8de top/bottom, cells 0.62rem 0.72rem padding centered, header 700, second header row muted 0.9rem, sticky first column with a 1px right shadow line.
- **BibTeX block.** Header row with copy button (white, 1px #d4d8de, 10px radius, weight 700); `pre` #f7f7f8, 1px #e3e5e8, 10px radius, 1rem padding.

## Page Modules

- **Title/author block.** Uppercase blue venue line above a centered prism title, authors, affiliations, a note line.
- **Link buttons.** arXiv, Code, Citation (tinted rounded-rectangle buttons, not pills).
- **Teaser figure.** Figure with muted caption under a TL;DR.
- **Abstract.** Full-width text block.
- **Method.** Two-stage flow (exocentric observation to egocentric reconstruction) with MathJax symbols in headings and a formula box.
- **Results tables.** Two wide comparison tables (H2O; TACO, Assembly101, Ego-Exo4D, inferred from heading) with sticky first column.
- **Qualitative results and analysis.** Real-world scenarios, conditioning modalities, backbone, pose strategies, consistency, wrong-text guidance, failure cases.
- **BibTeX.** With copy button.
- Not present: video, slider, 3D viewer, demo, template credit.

## Do's and Don'ts

**Do**

- Separate sections with a single top hairline instead of cards or bands.
- Give each link button its own soft tint keyed to the destination.
- Keep wide tables scrollable with a sticky row-label column.

**Don't**

- Don't animate anything except the title prism and the flow arrow.
- Don't use pill buttons; the radius is 12px.
- Don't color body text pure black; it is #1f2937.

## Surfaces

White page, translucent sticky nav, #f7f7f8 wells for formulas and code, tinted link buttons.

## Imagery

Exocentric and egocentric frame pairs, hand-object pose renders, comparison grids, failure-case images. Images are block-level with no frame.

## Layout

Centered narrow docs layout with sticky nav and anchor scrolling (`scroll-padding-top: 5rem`). Method uses a three-column flow; results use 2-up media grids and scrolling tables.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Text #1f2937
- Link #2563eb
- Hairline #e3e5e8
- Accent label #0f766e

**Example component prompts**

1. Create a sticky top nav: white at 96% opacity with 10px backdrop blur, 1px #e3e5e8 bottom border, uppercase 800-weight brand left, 0.92rem 600-weight #4b5563 links right with a 2px underline on active.
2. Create three link buttons with 12px radius and 1px #d4d8de border: Paper (#1d4ed8 on #eef4ff), arXiv (#b91c1c on #fff3f2), Code (#1f2937 on #f8fafc); hover lifts 1px with shadow 0 8px 24px rgba(15,23,42,.05).
3. Create a wide comparison table: horizontal scroll, sticky first column on white with a 1px right line, centered cells 0.62rem 0.72rem padding, bold header and a muted 0.9rem sub-header row.

## Similar Pages

- Documentation-style research pages with a sticky section nav.
- Exocentric-to-egocentric view synthesis pages.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --bg-soft: #f7f7f8;
  --line: #e3e5e8;
  --line-strong: #d4d8de;
  --text: #1f2937;
  --muted: #4b5563;
  --link: #2563eb;
  --accent: #0f766e;
  --shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
  --radius: 16px;
  --font-body: 'Spoqa Han Sans Neo', sans-serif;
}
body { margin: 0; font-family: var(--font-body); color: var(--text); background: var(--bg); }
.pub-btn { display: inline-flex; gap: .55rem; padding: .8rem 1rem; border-radius: 12px;
  border: 1px solid var(--line-strong); font-weight: 700; font-size: .95rem; }
```

## Provenance

- URL: https://redorangeyellowy.github.io/EgoWorld/
- Paper: EgoWorld: Translating Exocentric View to Egocentric View using Rich Exocentric Observations (Junho Park et al.), arXiv 2506.17896.
- Venue: ICLR 2026 (per the arXiv comment). Field: egocentric vision.
- Selection reason: arXiv comment states acceptance at ICLR 2026 and links the project page.
- Template credit: none on the page; no Nerfies footer. Bulma is loaded but the visible system is custom.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified. Raw HTML color counts include numeric character references (for example `&#8595;` arrows) that are not colors; they were ignored.
