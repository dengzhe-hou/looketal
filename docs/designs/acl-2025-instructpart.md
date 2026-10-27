# InstructPart · Teal Keyword Title — Style Reference

> A part catalogue in miniature: hundreds of 1.8 cm swatches under a teal-lettered title.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9 plus a lightly edited Nerfies `index.css`); roles are interpreted from markup and one rendered viewport. Bulma palette colors in the frequency scan are listed only where the page uses them.

## Overview

InstructPart is a classic Academic Project Page Template page with one memorable typographic move: the title letters that spell the project name ("Instruct", "Part", "Instruct" in "Instruction") are colored CSS `teal`, so the acronym reads out of the full title. Below a single-line venue ("ACL 2025 Main" in bold) and five dark pill buttons, a wide teaser figure with caption opens the page. The body is dense: four HTML tables of dataset examples using 387 thumbnails fixed at 1.8 cm × 1.8 cm and 564 cells of 10px centered text, followed by results, a video demonstration and BibTeX.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Keyword Teal | `teal` (`#008080`, CSS named color) | `--title-key` | Acronym letters inside the title (4 spans) |
| Bulma Ink | `#363636` | `--text-heading` | Title remainder, headings, dark pill fill |
| Body Grey | `#4a4a4a` | `--text` | Body text |
| Author Sky | `#209cee` | `--link-author` | Author links (`hsl(204,86%,53%)`) |
| Light Band | `#f5f5f5` | `--bg-band` | `hero is-light` sections (3 uses) |
| Slider Black | `#000000` | `--slider-dot` | Carousel pagination dots |

## Tokens — Typography

- **Display:** Google Sans for title and authors.
- **Body:** Noto Sans.
- **Example tables:** 10px centered text; one `pre-wrap` 10px block for long instructions.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Venue line | 1.25rem (`is-size-5`) | 700 (`<b>`) | 1.5 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Abstract (justified) | 1rem | 400 | 1.5 |
| Figure caption | .875rem–1rem | 400, "Figure 1." bold | 1.5 |
| Table cell text | 10px | 400 | — |
| Equal-contribution note | smaller | 400 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Link buttons | 290486px pill |
| Carousel items | 0 (stock 10px border removed) |
| Thumbnails | 0 |

Carousel item padding 20px. Shadows: none of its own. Container `is-max-desktop` (960px) with `is-four-fifths` content columns; thumbnails are physical-unit sized (1.8cm).

## Components

- **Keyword title:** `h1.title.is-1` with `<span style="color: teal;">` wrapping the acronym fragments.
- **Pill buttons:** `button is-normal is-rounded is-dark` with icons: Paper, Supplementary, arXiv, Data, Code.
- **Teaser figure:** full-width image under the buttons with "Figure 1." caption in small text.
- **Example grid table:** rows of 1.8cm square images with 10px centered labels (object, part, instruction).
- **Results carousel:** Bulma carousel with black pagination dots, padded items without borders.

## Page Modules

- **Title/author block:** teal-keyed title, sky-blue authors (8 names), "Robotics Institute, Carnegie Mellon University" with venue below in bold.
- **Venue badge:** bold text line "ACL 2025 Main".
- **Link buttons:** Paper, Supplementary, arXiv, Data, Code.
- **Teaser:** task illustration with kettle, robot and part labels.
- **Highlights:** bullet section after teaser.
- **Abstract:** justified.
- **Dataset:** "InstructPart Dataset and Tasks" with four example tables.
- **Results:** "Experimental Results" figures and tables in a carousel.
- **Video:** "Video Demonstration".
- **BibTeX:** two `pre` blocks.
- **Footer:** Academic Project Page Template credit, CC BY-SA 4.0.

## Do's and Don'ts

- Do color only the letters that form the project name; the rest of the title stays ink.
- Do size example thumbnails in a fixed physical unit so grids align.
- Don't color headings or buttons teal; the accent lives in the title only.
- Don't enlarge table text; the 10px labels are meant as captions to the images.

## Surfaces

White page with three `#f5f5f5` light bands; tables sit directly on the band without cards.

## Imagery

Real-world photos with colored part masks, a cartoon task schematic, many small square crops.

## Layout

960px column, four-fifths centered text, wide tables that can scroll on mobile.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, band `#f5f5f5`, heading `#363636`, title keyword `teal`, authors `#209cee`.

1. "Build a title where only the acronym letters are teal: Google Sans 3rem/600 `#363636`, wrap 'Instruct' and 'Part' fragments in spans colored `teal`."
2. "Build an example grid: an HTML table of 1.8cm × 1.8cm images, each with a 10px centered caption under it, no borders."
3. "Build a header venue line: affiliation then a bold 'ACL 2025 Main' on its own line, followed by five dark pill buttons."

## Similar Pages

Academic Project Page Template; GeAR in this batch (same template, different furniture).

## Quick Start

```css
:root {
  --bg: #ffffff; --band: #f5f5f5; --text: #4a4a4a; --heading: #363636;
  --title-key: teal; --author: #209cee;
  --radius-pill: 290486px; --thumb: 1.8cm;
  --font-display: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --max-width: 960px;
}
.example td { text-align: center; font-size: 10px; }
.example img { width: var(--thumb); height: var(--thumb); }
```

## Provenance

- **URL:** https://zifuwan.github.io/InstructPart/
- **Paper:** InstructPart: Task-Oriented Part Segmentation with Instruction Reasoning (arXiv 2505.18291), Zifu Wan et al.
- **Venue:** ACL 2025 (main).
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and links this page.
- **Template credit:** footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method:** extract_style.py scan (which reported 390 images and 565 occurrences of 10px), counting of inline style attributes, a diff of `index.css` against stock Nerfies, and one rendered viewport.
