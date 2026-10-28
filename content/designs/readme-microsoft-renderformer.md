# RenderFormer — README Reference

> A Cornell box turned into a cover page: a red, green and blue cube logo, a two-line ruled title, a black gallery of rendered scenes, then a nested contents list that maps the whole manual.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/microsoft/renderformer (last commit touching the file eec6a9b, 2026-10-13; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Image sizes and logo colors come from `medias/rf.png` and `medias/gallery-10.jpg` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The first screen is a centred stack that reads like a paper's title page set in GitHub's own type. A 320px square logo (a white "RF" cube on red, green and blue quadrants with a dark navy outline) sits on top, followed by the full paper title as a centred `<h1>` that breaks onto two lines, a centred row of five bold linked author names separated by middle dots, and the venue as a centred `<h2>` "SIGGRAPH 2025 Conference Papers". Both headings carry GitHub's grey bottom rule. Under the venue a full-width 5×2 gallery of rendered scenes on black backgrounds fills the bottom of the window. Below the fold come a centred plain-text caption, a centred row of five bold text links separated by `|`, one long left-aligned abstract paragraph, and then a `# Table of Content` with a four-level nested bullet list. The body uses `#` (h1) for every top-level section, so Installation, Usage, Bring Your Own Scene!, Acknowledgements, License and Citation all render at 32px with a rule. There are no badges, no emoji in headings and no news list.

## Header Block

The whole header is wrapped in one outer `<p align="center">`; GitHub's parser closes that paragraph as soon as it meets the inner `<div>`, so in the rendered HTML each element stands on its own and the outer `<p>` only contributes an empty paragraph. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Logo** (y≈110 to 430): `<div align="center"><img width=320 src="medias/rf.png"></div>`. The source is a 720×720 RGBA PNG; `width=320` renders it at 320×320, centred. GitHub wraps it in a link to the file.
2. **Title** (y≈482 and 522, rule at about 550): `<h1 align="center">RenderFormer: Transformer-based Neural Rendering of Triangle Meshes with Global Illumination</h1>`. GitHub h1, 2em (32px), weight 600, wrapping to two centred lines with a 1px grey rule under it across the 856px content width. The project name and the paper title are the same heading; there is no separate short name.
3. **Authors** (y≈579): one `<p align="center">` with five `<a href="..."><strong>Name</strong></a>` entries separated by `·` on its own source line. All five names link to personal pages or Google Scholar. No affiliation marks, no affiliation line and no equal-contribution mark.
4. **Venue** (y≈630, rule at about 652): `<h2 align="center">SIGGRAPH 2025 Conference Papers</h2>`. GitHub h2, 1.5em (24px), with the same bottom rule; it also becomes an entry in GitHub's outline menu.
5. **Gallery teaser** (y≈670 to about 1013, crossing the fold): `<div align="center"><img src="medias/gallery-10.jpg"> Examples of triangle-mesh based scenes ... and multiple light sources.</div>`. The JPG is 4345×1741 with no width attribute, so GitHub's `max-width: 100%` scales it to 856×343. It shows ten renders in a 5×2 grid, most on black.
6. **Caption** (y≈1030 to 1080): the plain sentence that follows the `<img>` inside the same `<div>`, so it renders centred at body size directly under the image, three lines long, without italics or a "Figure" label.
7. **Link row** (y≈1126): `<p align="center"><br><a href="..."><strong>Project Page</strong></a> | <a><strong>arXiv</strong></a> | <a><strong>Paper</strong></a> | <a><strong>Model</strong></a> | <a><strong>Official Code</strong></a></p>`. Five bold links in GitHub link blue separated by plain pipes; the leading `<br>` adds one blank line above the row.
8. **Abstract paragraph** (y≈1160 to 1370): one plain Markdown paragraph of seven sentences, left-aligned, with no bold and no heading. It ends the header block.

## Badges

The README uses no shields.io badges. The navigation is a row of bold text links that act as buttons.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (link row) | Project Page | #0969da (GitHub link blue) | bold text link, separated by ` \| ` | microsoft.github.io/renderformer/ |
| (link row) | arXiv | #0969da | bold text link | arxiv.org/abs/2505.21925 |
| (link row) | Paper | #0969da | bold text link | renderformer.github.io/pdfs/renderformer-paper.pdf |
| (link row) | Model | #0969da | bold text link | huggingface.co/microsoft/renderformer-v1.1-swin-large |
| (link row) | Official Code | #0969da | bold text link | github.com/microsoft/renderformer (the repo itself) |
| (author row) | five author names | #0969da | bold text links separated by `·` | personal pages and Google Scholar |

The link blue is the value in the github-markdown-css light theme that the capture uses; the README sets no color of its own.

Other colors visible in the header come from the logo, not from badges: red #f23340 (top left quadrant), green #5e9d59 (top right), blue #3c91cb (bottom) and the navy outline and shadow #042a45 around the white "RF" cube. The gallery adds the red and green walls of a Cornell box on black, which echo the logo's red and green.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | RenderFormer: Transformer-based Neural Rendering of Triangle Meshes with Global Illumination | title; authors follow without a heading |
| h2 (centred) | SIGGRAPH 2025 Conference Papers | venue; gallery, caption, link row and abstract follow without a heading |
| h1 | Table of Content | a nested bullet list of 28 anchor links on four levels (`-`, `*`, `+`, `-` markers by depth) |
| h1 | Installation | h2 Prerequisites (two bold-led bullets: System, Hardware), h2 Environment Setup (one `bash` block), h2 Pretrained Models (four-column model table, a paragraph on safetensors, a `<details>` note) |
| h1 | Usage | h2 Image Rendering with h3 Scene Conversion, h3 Rendering a Single Image Using Inference Script (h4 Available Arguments), h3 Inference with `RenderFormerRenderingPipeline` (a `python` block); h2 Video Rendering with h3 Download Example Data, h3 Rendering a Video (h4 Available Arguments) |
| h1 | Bring Your Own Scene! | h2 Scene Definition JSON with seven h3 subsections (structure, objects, camera, example, HDF5 fields, remeshing, Blender reference), h2 Blender Extension, h2 Scene Setting Tips (a numbered list with nested ranges) |
| h1 | Acknowledgements | a three-item code list and a long list of 3D model credits with bold model names |
| h1 | License | one paragraph and two bullets for submodule licenses |
| h1 | Citation | one sentence and a `bibtex` block |

Absent from the source: badges, news or changelog, results table, demo GIF or embedded video, project logo in a `<picture>` dark variant, quick start separate from Installation, contact section, emoji in headings.

Present but unusual: every top-level section is an h1 rather than an h2, so the body has seven 32px ruled headings; the venue is an `<h2>` heading rather than bold text; the header is wrapped in an outer `<p>` that GitHub closes immediately; the table of contents is hand-written and three of its anchors do not match GitHub's generated ids (`#usage-1` where the heading id is `usage`, `#inference-with--renderformerrenderingpipeline-` where it is `inference-with-renderformerrenderingpipeline`, and `#bring-your-own-scene-` where it is `bring-your-own-scene`), so those three links do not jump; the "Available Arguments" blocks are argparse help text fenced as `bash`.

## Components

**Centred stack in HTML.** Logo and gallery each sit in their own `<div align="center">`; title, authors and venue are `<h1>`, `<p>` and `<h2>` with `align="center"`. Spacing comes only from GitHub's heading and paragraph margins plus one `<br>` before the link row.

**Bold link rows.** Two rows use the same recipe: `<a href="..."><strong>Text</strong></a>` entries on separate source lines, joined by a separator on its own line (`·` between authors, `|` between destinations). Both render in #0969da at body size.

**Table of contents.** `# Table of Content` followed by a nested list that uses `-` for the first level, `*` for the second, `+` for the third and `-` again for the fourth, each indented two more spaces. GitHub renders all of them as bullets (disc, circle, square) with 2em indentation per level. Inline code inside a heading name is kept in the link text ("Inference with `RenderFormerRenderingPipeline`").

**Bold-led bullets.** Prerequisites use `- **System**: ...` and `- **Hardware**: ...`, with key terms (Linux, MacOS, Windows, NVIDIA CUDA GPUs, Apple Metal GPUs) also in bold.

**Model table.** `| Model | Params | Link | Model ID |` with `|-------|` delimiters and no alignment colons. Two rows (RenderFormer-V1-Base 205M, RenderFormer-V1.1-Large 483M); the Link cell is `[Hugging Face](...)` and the Model ID cell is inline code (`microsoft/renderformer-v1-base`). No bold best values.

**Collapsible note.** `<details><summary>Note on the released models</summary><br>...</details>` hides a one-paragraph caveat about a shader bug and retrained models; collapsed by default.

**Code blocks.** Fenced with language tags: `bash` for install, conversion, inference commands and argparse help listings, `python` for the minimal `RenderFormerRenderingPipeline` example (with a trailing comment showing the expected output shape), `bibtex` for the citation. GitHub renders them on its light grey code background with a copy button.

**Field lists.** Scene and HDF5 formats are documented as bullets whose first token is an inline-code field name (`` `mesh_path` ``, `` `triangles` ``), with nested bullets for sub-fields and array shapes in brackets ("[N, 3, 3]").

**Credits list.** Acknowledgements list each 3D model as a bold name, linked when a source exists, followed by ": By Author" or ": from Repository".

**Citation.** "If you find this work helpful, please cite our paper:" then `@inproceedings {zeng2025renderformer, ...}` with fields aligned in a column (`title      = {...}`).

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| rf.png | PNG logo, square, RGBA | 720×720 | `<img width=320 src="medias/rf.png">` in `<div align="center">` | 320×320 | top of the README |
| gallery-10.jpg | JPG grid of ten renders, mostly black backgrounds | 4345×1741 | `<img src="medias/gallery-10.jpg">` with no width, in `<div align="center">` | 856×343 | after the venue heading; plain centred caption in the same `<div>` |

The gallery is the only figure in the README. It is a 5×2 grid of RenderFormer outputs (Cornell box, glossy objects, an "RF" letter scene with colored walls, a tree, a fox, crystals and others), so the first screen shows results rather than a method diagram. No GIF, no video, no `<picture>` dark variant. The logo's flat quadrants (#f23340, #5e9d59, #3c91cb) are the only designed color on the page.

## Adapting to Other Content

- **A library.** Keep the 320px logo, put the library name alone in the `<h1>` (one line), replace the author row with a one-line description, keep the bold `|` link row (Docs, PyPI, Examples, Code) and keep the nested Table of Contents; drop the venue `<h2>`.
- **A dataset.** Keep the full header, swap the gallery for a sample grid at its natural width (scaled to 856px), and put a Download section with a table shaped like the model table (Split, Size, Link, ID) first in the contents list.
- **A benchmark with scores.** Keep the header and add a Results section after Installation with a pipe table, numeric columns right-aligned (`| ---: |`) and the best value in bold; RenderFormer has no such table, so this is an extension.
- **A repo without a teaser.** Let the bold link row follow the venue heading directly and move the abstract paragraph up; the logo alone carries the first screen at 320×320.
- **A shorter manual.** Use `##` for top-level sections instead of `#` and drop the Table of Contents once there are fewer than about six sections; keep the order Installation, Usage, Citation.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put the logo at `width=320` in its own centred `<div>` | Let a large square logo render at its 720px source size |
| Join author names with `·` and destinations with `\|`, all as bold links | Mix badges and text links in the same row |
| Let a results gallery fill the 856px width with a centred caption under it | Shrink the gallery into a thumbnail |
| Map a long manual with a nested Table of Contents | Hand-write anchors without checking them against GitHub's ids (three of RenderFormer's do not resolve) |
| Hide caveats about released weights in `<details>` | Put model-release caveats inline above the install commands |
| Tag every code block (`bash`, `python`, `bibtex`) | Leave argparse help untagged in a long block |

## Agent Prompt Guide

1. "Write a README header in GitHub HTML: a centred `<div>` with a square logo at `width=320`, a centred `<h1>` with the full paper title, a centred `<p>` of bold author links separated by `·`, a centred `<h2>` with the venue, a centred `<div>` holding a full-width results gallery image (no width attribute, scales to 856px) followed by a plain caption sentence, and a centred `<p>` that starts with `<br>` and holds five bold links (Project Page | arXiv | Paper | Model | Official Code) in GitHub link blue #0969da. No badges."
2. "After a one-paragraph abstract, add `# Table of Content` as a nested bullet list of anchor links on up to four levels, then top-level `#` sections in this order: Installation (Prerequisites, Environment Setup, Pretrained Models), Usage, Bring Your Own Scene!, Acknowledgements, License, Citation. Check every anchor against GitHub's heading ids."
3. "Write the Pretrained Models table as `| Model | Params | Link | Model ID |` with a `[Hugging Face](...)` link and the model ID in inline code, follow it with a `<details><summary>Note on the released models</summary>` caveat, and document input formats as bullets whose first token is an inline-code field name."

## Similar Pages

- readme-vveicao-freeorbit4d also opens with a logo image above a centred title, venue line and authors, but uses `for-the-badge` badges and an HTML results table where RenderFormer uses bold text links and one gallery image.
- readme-deepmancer-hairport shares the paper-like reading order (title, venue, authors, figure with caption) but puts a news list and numbered figure captions before installation and has no table of contents.
- readme-eku127-satnav uses the same centred `<h1>` and `<h2>` pair with rules, but with a short project name in the `<h1>` and a uniform badge row.

## Quick Start

````markdown
<div align="center">
  <img width=320 src="assets/logo.png">
</div>

<h1 align="center">ProjectName: Full Paper Title That May Wrap Onto Two Lines</h1>

<p align="center">
  <a href="https://example.org/"><strong>Author One</strong></a>
  ·
  <a href="https://example.org/"><strong>Author Two</strong></a>
  ·
  <a href="https://example.org/"><strong>Author Three</strong></a>
</p>

<h2 align="center">Venue Year Track</h2>

<div align="center">
  <img src="assets/gallery.jpg">
  One plain sentence describing what the gallery shows.
</div>

<p align="center">
<br>
  <a href="https://example.github.io/project/"><strong>Project Page</strong></a>
  |
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><strong>arXiv</strong></a>
  |
  <a href="https://example.org/paper.pdf"><strong>Paper</strong></a>
  |
  <a href="https://huggingface.co/org/model"><strong>Model</strong></a>
  |
  <a href="https://github.com/org/name"><strong>Official Code</strong></a>
</p>

One abstract paragraph, left-aligned.

# Table of Content

- [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Environment Setup](#environment-setup)
  * [Pretrained Models](#pretrained-models)
- [Usage](#usage)
- [Bring Your Own Data](#bring-your-own-data)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Citation](#citation)

# Installation

## Prerequisites

- **System**: Tested on ...
- **Hardware**: Tested on ...

## Environment Setup

```bash
git clone https://github.com/org/name
cd name
pip install -r requirements.txt
```

## Pretrained Models

| Model | Params | Link | Model ID |
|-------|--------|------|----------|
| Name-Base | 000M | [Hugging Face](https://huggingface.co/org/name-base) | `org/name-base` |

<details>
<summary>Note on the released models</summary>
<br>
One paragraph of caveats.
</details>

# Usage

```python
from name import Pipeline
```

# Bring Your Own Data

- `field_name`: what it holds

# Acknowledgements

# License

# Citation

If you find this work helpful, please cite our paper:

```bibtex
@inproceedings{key,
    title      = {...},
}
```
````

## Provenance

- Repo: https://github.com/microsoft/renderformer (`README.md`, branch `main`, last README commit eec6a9b on 2026-10-13).
- Paper: "RenderFormer: Transformer-based Neural Rendering of Triangle Meshes with Global Illumination", SIGGRAPH 2025 Conference Papers, arXiv 2505.21925; first author Chong Zeng. Project page https://microsoft.github.io/renderformer/.
- Selection: a model first screen, with a square logo, centred title, author line, venue line, a sharp captioned teaser grid, a single row of text links, then a full nested table of contents that maps the whole manual before installation starts.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, `medias/rf.png` and `medias/gallery-10.jpg` fetched from the repo for pixel sizes and logo colors, heading ids in the rendered HTML checked against the table of contents anchors.
- Written 2026-10-28.
