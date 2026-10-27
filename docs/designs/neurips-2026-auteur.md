# Auteur Amber Reel — Style Reference

> A film-festival program, orange title card and a sunset-gradient abstract banner.

**Theme:** light

Values come from `css/style.css`, `css/slider.css`, and a large inline `<style>` block in `index.html` whose `:root` defines the brand tokens. A comment in that block names "Voxel Dynamics" as the source of the accent orange and the banded section style. Roles are interpreted. Rendered output was not viewed.

## Overview

Auteur (UCL and collaborators) is a video-heavy page (88 `<video>` elements) for language-driven camera framing. Everything is Inter, with JetBrains Mono applied to every `<span>` for DSL captions (the title and affiliations are explicitly reset to Inter). The 2.25rem, 800-weight centered title is set entirely in brand orange `#e8590c`. Below it: 1.25rem/600 ink author links, a very light 100-weight gray `NeurIPS 2026` line, and three ink pill buttons (arXiv, Dataset, Demo) with logo icons that invert to white on hover. The abstract sits in a full-width orange-to-amber gradient banner with white 28px text. The rest of the page alternates white and `#f6f7f9` full-width bands separated by hairlines, each with an 800-weight orange section title, slider carousels of video rows, contribution cards, an iterative-editing walkthrough with coral step badges, and results tables with a peach "ours" row.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Director Orange | `#e8590c` | `--brand` | Title, section titles, hover tints |
| Amber Light | `#f59e0b` | `--brand-light` | Gradient end, contribution icon tile |
| Ember | `#c2410c` | `--brand-dark` | Gradient start of abstract banner |
| Screen Blue | `#3a7bd9` | `--accent-2` | Secondary accent (rarely used, inferred) |
| Film Ink | `#1a1d24` | `--ink`, `--text-color` | All text, button fill |
| Slate Muted | `#5a6472` | `--muted` | Secondary text |
| Hairline | `#e2e6ec` | `--line` | Band dividers, table rules, card borders |
| Studio Gray | `#f6f7f9` | `--surface` | Alternate bands, contribution cards |
| Table Head | `#eef1f5` | `--surface-2` | Results table header |
| Peach Ours | `#fff3e9` | `--ours` | Highlighted "ours" table row |
| Credits Gray | `#666666` | (literal) | Conference line |
| BibTeX Panel | `#F4F4F4` | (literal) | BibTeX block |
| Coral Badge | `#fb8072` | (literal) | Iteration step badges |
| DSL Panel | `#f7f7f7` | (literal) | DSL snippet boxes |
| Link Blue | `#1f78b4` | (literal) | Inline links in style.css |

## Tokens — Typography

- **Sans:** `Inter` 400–800 (Google Fonts), fallback system UI, Roboto, Helvetica.
- **Mono:** `JetBrains Mono` 400/500 (Google Fonts) for all `span` text and prompt captions; "Courier New" in DSL boxes.
- **Weights:** 800 title and section titles; 700 card heads and table header; 600 author links; 100 conference line.

| Role | Size | Weight | Line height | Extra |
|---|---|---|---|---|
| Title | 2.25rem, max 80% width | 800 | 1.14 | -0.02em, brand orange |
| Conference | 1.5rem | 100 | | `#666` |
| Authors | 1.25rem | 600 | | ink links |
| Affiliations | 1.125rem | 400 | | |
| Section title | `clamp(1.5rem, 3vw, 1.95rem)` | 800 | | -0.02em, orange, centered |
| Abstract banner text | 28px | 400 | 1.6 | white, opacity .95 |
| Prompt text | 18px mono | 400 | | |
| Results table | 0.9rem (head 0.86rem) | 400 / 700 | | |
| Button | 1rem | | | |
| BibTeX | 0.75em | | | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons | 1.5rem |
| Iteration step badge | 999px |
| Iteration step card, overview box | 16px / 1rem |
| Contribution cards (`--radius`) | 14px |
| Section blocks, iteration images | 12px |
| DSL boxes | 10px |
| Contribution icon tile | 9px |

- **Shadows:** `--shadow: 0 1px 2px rgba(16,24,40,.06), 0 8px 24px rgba(16,24,40,.06)` on card hover; iteration steps `0 4px 12px rgba(0,0,0,.06)`; overview box uses a 3px right/bottom border as a hard offset shadow.
- **Layout:** `.section-inner` 1200px (teaser up to 1500px); abstract banner inner 900px; abstract, results, qualitative 960px; failures 640px.
- **Band rhythm:** `clamp(2.5rem, 5vw, 4rem)` vertical padding with a 1px top hairline.

## Components

- **Pill button.** Ink `#1a1d24` fill, 2px ink border, 1.5rem radius, white label beside an SVG logo; hover inverts to white fill with ink text and darkened logo.
- **Abstract banner.** Full-width `linear-gradient(135deg, #c2410c, #f59e0b)`, 60px 20px padding, white h2 and body at 28px.
- **Section band.** Full-width, alternating `#ffffff` and `#f6f7f9`, hairline top.
- **Contribution card.** `#f6f7f9`, hairline border, 14px radius, 34px icon tile with amber gradient; on hover lifts 3px, gains shadow and an orange-tinted border.
- **Video slider.** Header row with title and prev/next controls, slides of 2, 3 or 4 videos (360px or 340px blocks) with bold 16–17px labels.
- **Iteration step card.** White, 16px radius, coral `#fb8072` pill badge, italic `#444` edit text, `#f7f7f7` DSL box in Courier New.
- **Results table.** White, centered cells, `#eef1f5` header, "ours" row on `#fff3e9`, hover row tinted 5% orange.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Orange 800 title, ink 600 authors |
| Venue badge | Thin gray text "NeurIPS 2026" | |
| Link buttons | arXiv, Dataset (HF), Demo (GitHub) | Ink pills with logos |
| Teaser | Wide image band up to 1500px | |
| Abstract | Gradient banner | |
| Contributions | Card grid (auto-fit, min 250px) | |
| Method | Motion/framing primitives, pipeline sections | |
| Results videos | Model comparisons, VACE, cross-renderer sliders | |
| Results tables | 6 tables | Peach ours row |
| Sliders / 3D / HF Space | Video carousels only | |
| BibTeX | `#F4F4F4` block with copy button | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do make the title and every section heading the same brand orange.
- Do use the gradient only once, for the abstract banner.
- Do label prompts and DSL in mono; the page sets all spans to JetBrains Mono.
- Don't color buttons orange; they stay ink and invert on hover.
- Don't stack bands without the hairline divider.

## Surfaces

White and studio-gray bands, one ember-to-amber banner, peach highlight rows, light gray code panels.

## Imagery

Short generated video clips in rows and sliders, a wide teaser image, and per-step framing images with 1px `#eee` borders.

## Layout

Full-width bands with 1200px inner content; slider sections narrow to 320–960px depending on clip count. Prompt layouts split 55% / 35% and stack below 1000px.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, band `#f6f7f9`, ink `#1a1d24`, muted `#5a6472`, line `#e2e6ec`, brand `#e8590c`, amber `#f59e0b`, ember `#c2410c`, ours `#fff3e9`.

1. "Center an Inter 800 title at 2.25rem in `#e8590c` with -0.02em tracking, 1.25rem/600 ink author links, and a 1.5rem weight-100 `#666` 'NeurIPS 2026' line."
2. "Create a full-width abstract banner with `linear-gradient(135deg, #c2410c, #f59e0b)`, 60px padding, a 900px inner column, white 28px/1.6 text."
3. "Style ink pill buttons: `#1a1d24` fill, 2px ink border, 1.5rem radius, logo plus white label; hover inverts to white with ink text."

## Similar Pages

The "Voxel Dynamics" page that the inline CSS credits for its orange and banded layout (not verified here); ReMind in this collection for a similarly video-dense layout.

## Quick Start

```css
:root {
  --brand: #e8590c; --brand-light: #f59e0b; --brand-dark: #c2410c; --accent-2: #3a7bd9;
  --ink: #1a1d24; --muted: #5a6472; --line: #e2e6ec;
  --surface: #f6f7f9; --surface-2: #eef1f5; --ours: #fff3e9;
  --radius: 14px;
  --shadow: 0 1px 2px rgba(16,24,40,.06), 0 8px 24px rgba(16,24,40,.06);
  --font: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace;
}
```

## Provenance

- **URL:** https://cyberiada.github.io/Auteur/
- **Paper:** Auteur: Language-Driven Cinematographic Framing for Human-Centric Video Generation (arXiv 2606.01900), Muhammed Burak Kizil et al.
- **Venue:** NeurIPS 2026
- **Selection reason:** arXiv comment states NeurIPS 2026 acceptance and links this page.
- **Template credit:** no footer credit; inline CSS comments cite "Voxel Dynamics" for the accent and band style. Some comments are in Turkish ("beyaz", "Küçük ekranlar için").
- **Measurement method:** static HTML (including its inline style block) and two stylesheets read directly; `extract_style.py` frequencies used as a cross-check. Not viewed in a browser. The third button is labeled "Demo" but links to a GitHub repo.
