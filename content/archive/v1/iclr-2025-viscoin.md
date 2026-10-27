# VisCoIN Navy Memo — Style Reference

> A typed lab memo in Arial with navy headings and bracketed links.

**Theme:** light

Values come from the page's single inline `<style>` block, its inline `style` attributes, and the linked `css/bootstrap.min.css` (Bootstrap 4). Bootstrap's palette inflates the raw frequency counts but almost none of it is used. Measurements are normalized; roles are interpreted. The rendered page was not viewed.

## Overview

The VisCoIN page is a deliberately plain, early-2010s style academic page. Body text is Arial 16px in a 950px column with an 80px top margin. There are no `<section>` or `<h2>` elements: headings are spans sized inline (32px title, 28px section heads, 21px subsections, 18px sub-subsections), and the only color accent is the deep navy `rgb(9,14,152)` used for the five 19px author names. Spacing is done with empty `.gap-5/10/20/30` divs. Links appear as text in square brackets, "[ Paper ] [ Code ]". A thin gradient `hr` separates blocks. Results tables are embedded as PNG images, and MathJax renders inline math. There is no venue label, no BibTeX and no teaser video.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | (Bootstrap body) | Page background |
| Bootstrap Ink | `#212529` | (Bootstrap body) | Body text |
| Ink Navy | `rgb(9,14,152)` | (inline) | Author names (19px) and two other inline labels |
| Link Blue | `#007bff` | (Bootstrap) | Bracketed links |
| Rule Smoke | `rgba(0,0,0,0.3)` | (inline style block) | `hr` gradient |

Other Bootstrap tokens (`--indigo #6610f2`, `--green #28a745`, `--red #dc3545`, etc.) are declared by the framework but not used on visible elements.

## Tokens — Typography

- **Body:** Arial (declared on `body`), 16px. Substitute: Helvetica, Liberation Sans.
- **Loaded but unused:** Google Sans / Noto Sans / Castoro link tag; no rule applies them (inferred).
- **Math:** MathJax 3 CHTML.

| Role | Size | Weight | Color |
|---|---|---|---|
| Title | 32px (inline) | Bootstrap default | `#212529` |
| Section heading | 28px (inline) | default | `#212529` |
| Subsection (e.g. "Interpretation phase") | 21px (inline) | default | `#212529` |
| Sub-subsection, affiliations | 18px (inline) | default | `#212529` |
| Author names | 19px (inline) | default | `rgb(9,14,152)` |
| Body | 16px | 400 | `#212529` |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Body column | `max-width: 950px; margin: 80px auto` |
| `.paper` thumbnail block | 700px, 500px under 910px, 300px under 610px |
| Gap spacers | 5, 10, 20, 30px tall empty divs |
| Radius | none on content (Bootstrap `.25rem` only on unused controls) |
| `hr` | 1px tall, `linear-gradient(to right, rgba(0,0,0,.3) ×3)` |

No shadows on content.

## Components

- **Title block:** 32px title, navy 19px author names with superscripts separated by `&emsp;`, 18px two-line affiliations, "* Equal contribution".
- **Link row:** `[ Paper ] &emsp; [ Code ]`, plain text brackets around Bootstrap-blue links, with Font Awesome i2svg icons.
- **Heading:** 28px span, then a gradient `hr`, then a `.gap-10` or `.gap-20` spacer.
- **Figure:** full-width PNG (`viscoin_v3-1.png`, `interact_concept_v5-1.png`) inside `.container .col-md-8` row.
- **Results:** tables as images (`tab_acc.png`, `tab_rec.png`, `tab_ff.png`, `tab_cnst.png`).

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Arial, inline font sizes |
| Venue badge | No | No venue text anywhere on the page |
| Link buttons | Yes (text) | "[ Paper ]" to OpenReview PDF, "[ Code ]" to GitHub |
| Teaser figure / video | Yes | Static architecture figure |
| Abstract | Yes | Plain paragraph under a 28px heading |
| Method figure | Yes | Concept interaction and comparison figures |
| Results tables | Yes | Four PNG table images |
| Qualitative results | Yes | Six PNG grids (CUB, CelebA, Cars) |
| Image comparison slider / 3D / demo | No | |
| BibTeX | No | |
| Acknowledgements | No | |

## Do's and Don'ts

- Do keep everything in one Arial family and use navy only for author names.
- Do separate blocks with the faint gradient rule and fixed gap spacers.
- Don't add buttons; links stay as bracketed text.
- Don't load fonts you never apply (the Google Sans link is dead weight here).

## Surfaces

Single white surface. No cards, bands or shadows.

## Imagery

Fourteen PNG figures exported from the paper PDF (filenames end in `-1.png`, typical of pdftoppm output).

## Layout

One 950px column, centered with `margin: 80px auto`; figures in an 8-of-12 Bootstrap column.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#212529`, navy authors `rgb(9,14,152)`, link `#007bff`, rule `rgba(0,0,0,0.3)`.

1. "Build a 950px Arial page with an 80px top margin, a 32px title, author names at 19px in `rgb(9,14,152)` separated by em spaces, and links written as '[ Paper ]  [ Code ]'."
2. "Make a section heading: 28px span, followed by a 1px horizontal rule drawn as a 30% black linear gradient, then a 20px spacer div."
3. "Show results as stacked PNG table images, each full width in an 8/12 column, with a 21px subsection label above."

## Similar Pages

Classic hand-coded pages in the style of older vision-lab project pages; in this collection it is the plainest ICLR 2025 entry.

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #212529; --navy: rgb(9, 14, 152);
  --link: #007bff; --rule: rgba(0, 0, 0, 0.3);
  --font: Arial, Helvetica, sans-serif; --fs-body: 16px;
  --fs-title: 32px; --fs-section: 28px; --fs-sub: 21px; --fs-author: 19px; --fs-minor: 18px;
  --column: 950px;
}
body { font-family: var(--font); font-size: var(--fs-body); max-width: var(--column); margin: 80px auto; }
hr { border: 0; height: 1px; background-image: linear-gradient(to right, var(--rule), var(--rule)); }
```

## Provenance

- **URL:** https://jayneelparekh.github.io/VisCoIN_project_page/
- **Paper:** Restyling Unsupervised Concept Based Interpretable Networks with Generative Models (arXiv 2407.01331), Jayneel Parekh et al.
- **Venue:** ICLR 2025 (not stated on the page; Paper link goes to OpenReview).
- **Selection reason:** arXiv comment states acceptance at ICLR 2025 and links this page.
- **Template credit:** none; Bootstrap 4 plus a small inline style block.
- **Measurement method:** `extract_style.py` plus manual reading of the inline style block and inline attributes. Rendered page not viewed.
