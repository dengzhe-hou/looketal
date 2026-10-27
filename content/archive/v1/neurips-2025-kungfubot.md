# KungfuBot Nerfies Dojo — Style Reference

> A Nerfies sheet pinned to a dojo wall, rows of looping kick videos with soft drop shadows.

**Theme:** light

Values come from Bulma, the stock Nerfies `static/css/index.css` (with one added `section { margin: 0 0; }` rule), and two inline `<style>` blocks in the page that define the video grid. Bulma's palette is filtered to colors visible in markup. Roles are interpreted. Rendered output was not viewed.

## Overview

KungfuBot (TeleAI China Telecom, SJTU and others) is a Nerfies page whose personality comes from its video grids. The hero is standard: Google Sans 3rem title, a plain `h2.is-size-3` "NeurIPS 2025" line with no color, nine authors with superscripts, five affiliations plus notes, and three dark rounded buttons (Paper PDF, arXiv, Code). Sections use the larger `title is-2` (2.5rem) headings for Video, Abstract, Method, Real World Experiments, Experiment Results and BibTeX. The main video plays at 30% width. Real-world skills (jump kick, roundhouse kick, side kick, and more) sit in a 3-column grid of 12px-rounded videos with a `0 6px 16px rgba(0,0,0,.2)` shadow and a 16px `#222` caption above each. Comments in the inline CSS are in Chinese.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page; also the 2px border on logo images |
| Bulma Ink | `#363636` | `--text-strong` | Titles, venue line |
| Body Graphite | `#4a4a4a` | `--text` | Body text |
| Caption Black | `#222222` | `--caption` | Video captions |
| Author Sky | `hsl(204, 86%, 53%)` | `--author-link` | Author links |
| Button Night | `#363636` | `--btn-dark` | `is-dark` rounded buttons |
| Code Mist | `#f5f5f5` | `--surface` | BibTeX `pre` |
| Footer Fog | `#fafafa` | `--footer` | Bulma footer |
| Footer Icon | `#000000` | (template) | Footer icon links |

## Tokens — Typography

- **Display:** `Google Sans` (title, authors). Substitute: Product Sans, Inter.
- **Body:** `Noto Sans`. Substitute: Open Sans.
- **Mono:** Bulma `monospace`.
- **Weights:** 400 body, 600 titles; venue line inherits Bulma heading weight 400 (inferred, since it is not a `.title`).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Venue (`h2.is-size-3`) | 2rem | 400 (inferred) | 1.5 |
| Authors / affiliations (`is-size-5`) | 1.25rem | 400 | 1.5 |
| Section heading (`title is-2`) | 2.5rem | 600 | 1.125 |
| Sub-section (`title is-4`) | 1.5rem | 600 | 1.125 |
| Video caption | 16px | 400 | 1.5 |
| Body | 1rem | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons (`is-rounded`) | 290486px |
| Grid videos | 12px |
| Logo images (`.image-container img`) | 10px |
| `pre` | 4px |

- **Shadows:** grid videos `0 6px 16px rgba(0,0,0,.2)`; nothing else.
- **Layout:** `container is-max-desktop` (960px, inferred from Bulma 0.9); the inline `.grid-container` is declared at `width: 150%` with 40px padding and an inline override to `repeat(3, 1fr)` with 20px gap, so the grid can overflow the column (inferred from CSS, not checked in a render).
- **Section rhythm:** Bulma `.section` padding, with the added rule zeroing section margins.

## Components

- **Venue line.** Unstyled `h2.is-size-3` "NeurIPS 2025" directly under the title.
- **Link buttons.** Dark Bulma pills with Font Awesome PDF, Academicons arXiv and GitHub icons; Paper links to a local `static/pdf/paper.pdf`.
- **Main video.** Native `<video>` autoplay, muted, loop, controls, `width="30%"`.
- **Skill grid.** `.grid-container` with 3 equal columns, 20px gap, centered items; each `.video-item` has a caption on top and a shadowed 12px-rounded video below. A second grid (`.grid-container2`) uses `minmax(480px, 1fr)` for wider result clips.
- **Logo row.** `.image-container` flex row, 20px gap, images at max 10% width with a 2px white border and 10px radius.
- **BibTeX.** Bulma `pre` on `#f5f5f5`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered, Google Sans |
| Venue badge | Plain h2 text "NeurIPS 2025" | |
| Link buttons | Paper (PDF), arXiv, Code | Dark pills |
| Teaser | Main video at 30% width | |
| Abstract | Yes | Justified, four-fifths column |
| Method figure | Single image, max-height 600px | |
| Results videos | Real-world experiments grid, main results, ablation, sim-to-real | Shadowed rounded videos |
| Tables / sliders / 3D | No (carousel assets loaded, unused) | |
| BibTeX | Yes | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do caption each skill clip above the video in plain 16px text.
- Do round and shadow videos uniformly (12px, `0 6px 16px rgba(0,0,0,.2)`).
- Do keep the hero untouched Nerfies.
- Don't size grids above 100% of their container; the 150% width is a quirk, not a pattern to copy.
- Don't color the venue line unless you want to depart from this page.

## Surfaces

White throughout; `#f5f5f5` code block; `#fafafa` footer.

## Imagery

Real-robot humanoid videos (kicks and dynamic skills) looping silently, plus a method diagram and result figures.

## Layout

Single centered column; video sections break into 3-column grids.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, title `#363636`, body `#4a4a4a`, caption `#222222`, author links `hsl(204,86%,53%)`, buttons `#363636`, code `#f5f5f5`.

1. "Make a Nerfies hero: Google Sans 3rem/600 title, a plain 2rem 'NeurIPS 2025' line, 1.25rem author spans with blue links, then dark rounded Paper/arXiv/Code buttons."
2. "Create a 3-column video grid with 20px gaps; each item has a 16px `#222` caption above an autoplaying muted loop video with 12px radius and `0 6px 16px rgba(0,0,0,.2)` shadow."
3. "Use Bulma `title is-2` (2.5rem/600) centered headings for Video, Abstract, Method and Results sections."

## Similar Pages

Nerfies and its forks; V2W and LangSplatV2 in this collection; many 2025 humanoid-robotics pages share the shadowed video-grid pattern.

## Quick Start

```css
:root {
  --bg: #ffffff; --text-strong: #363636; --text: #4a4a4a; --caption: #222222;
  --author-link: hsl(204, 86%, 53%); --btn-dark: #363636;
  --surface: #f5f5f5; --footer: #fafafa;
  --font-display: 'Google Sans', 'Inter', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --radius-pill: 290486px; --radius-video: 12px;
  --shadow-video: 0 6px 16px rgba(0, 0, 0, 0.2);
  --container: 960px;
}
.video-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
```

## Provenance

- **URL:** https://kungfubot.github.io/
- **Paper:** KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills (arXiv 2506.12851), Weiji Xie et al., TeleAI.
- **Venue:** NeurIPS 2025
- **Selection reason:** arXiv comment states NeurIPS 2025 acceptance and links this page.
- **Template credit:** footer states "This website is adapted from Nerfies" under CC BY-SA 4.0.
- **Measurement method:** static HTML (with inline styles) and `index.css` parsed with `extract_style.py`; Bulma defaults filtered by reading markup. Not viewed in a browser; the effect of the 150% grid width is inferred.
