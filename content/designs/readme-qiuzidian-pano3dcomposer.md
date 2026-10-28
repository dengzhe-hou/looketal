# Pano3DComposer — README Reference

> A gallery label hung under a diptych: name, subtitle, two authors and four small tags, then the same room shown twice, as photograph and as reconstruction.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/qiuzidian/Pano3DComposer (last commit touching the file 891facb, 2026-10-05; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs; method-figure accent colors are medians of saturated pixels in `assets/method_overview.png` fetched from the repo. Rendered positions are y values in the 1440×900 frame. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The header is a strict typographic ladder inside one `<div align="center">`: a short `#` project name with GitHub's h1 rule, an `###` subtitle with the full paper title, a two-author line with a `·` separator and a dagger, one affiliation, a bold venue line, and one row of four flat badges, each with a white logo (arXiv, Chrome, Python, PyTorch). Two equal panoramas sit side by side under it (input on the left, generated scene on the right, each 49% wide), with a `<sub>` caption that says which is which. Under the div a left-aligned paragraph states the result in bold (**editable, metric-scale 3D scene**) and five bullets open with bold leads. The body is plain `##` headings without emoji: Method (one 95% figure), Installation (a long `bash` block plus a collapsed Notes block), Model weights, Usage with three `###` sub-sections and two tables, Demo data, Dataset split, License, Citation and Acknowledgements. There is no news list, no results table and no table of contents.

## Header Block

Everything down to the caption is inside `<div align="center">` with blank lines around the Markdown.

1. **Name** (y≈140): `# Pano3DComposer`. GitHub h1, 2em (32px), weight 600, one line; the 1px grey rule sits under it at about y≈168.
2. **Subtitle** (y≈206): `### Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image`. GitHub h3, 1.25em (20px), weight 600, no rule, one line at 856px. Being a real heading, it takes a slot in GitHub's outline menu.
3. **Authors** (y≈246): `Zidian Qiu &nbsp;·&nbsp; Ancong Wu<sup>†</sup>`. Plain text, not links; a middle dot padded by non-breaking spaces; the dagger marks the corresponding author and is not explained anywhere (inferred meaning).
4. **Affiliation** (y≈287): `Sun Yat-sen University`. Plain text.
5. **Venue** (y≈326): `**CVPR 2026**`. Bold body text, no link.
6. **Badge row** (y≈364): four HTML lines, two `<a><img></a>` and two bare `<img>` (Python and PyTorch are not links). 20px tall, about 446px wide in total (133 + 103 + 101 + 97 plus three spaces). Details in Badges.
7. **Teaser pair** (y≈396 to about 605): `<img src="assets/teaser_input.jpg" width="49%" alt="Input panorama"> <img src="assets/teaser_scene.jpg" width="49%" alt="Generated compositional 3D scene">` on one source line. Each 1024×512 JPEG renders at about 419×210; the single space between them leaves a gap of about 4px. Neither is linked.
8. **Caption** (y≈643): `<sub>Left: input panorama. Right: generated scene (object meshes + background Gaussians).</sub>`. Small centred text, about 12px.
9. **Intro** (y≈679, after `</div>`): a left-aligned paragraph with the result phrase in bold, then five bold-lead bullets (y≈767 onward). The fifth bullet crosses the fold.

## Badges

All four use the static path form with a hex message color, `logo=` and `logoColor=white`, and no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, faint vertical gloss, Verdana 11px, white text, label on #555555 with the white logo at its left.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv (arXiv logo) | 2603.05908 | #b31b1b (label #555555) | flat (default), `logo=arxiv&logoColor=white` | arxiv.org/abs/2603.05908 |
| Project (Chrome logo) | Page | #2f6f4f (label #555555) | flat (default), `logo=googlechrome&logoColor=white` | qiuzidian.github.io/pano3dcomposer-page/ |
| python (Python logo) | 3.10 | #3776ab (label #555555) | flat (default), `logo=python&logoColor=white` | not linked |
| PyTorch (PyTorch logo) | 2.4 | #ee4c2c (label #555555) | flat (default), `logo=pytorch&logoColor=white` | not linked |

Two badges are links (paper, project page) and two are environment facts that repeat the tested versions from Installation. Message colors follow each destination's brand: arXiv red, Python blue, PyTorch orange-red; the project page uses a dark green. Every `alt` is plain ("arXiv", "Project page", "Python 3.10", "PyTorch 2.4").

Colors on the page that are not badges come from the method figure: its "Alignment-VGGT" band and label in amber #ffc000, coral #ff6b5c token cells and green #78cf8b token cells (pixel medians), over pale blue, green, orange and yellow section fills.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | Pano3DComposer | name only |
| h3 (centred) | Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image | subtitle; authors, affiliation, venue, badges, teaser pair and caption follow in the same div; intro paragraph and five bullets follow the div without a heading |
| h2 | Method | one centred figure at `width="95%"`, no text |
| h2 | Installation | one paragraph of tested hardware, one long `bash` block with `#` comment groups, `<details><summary>Notes</summary>` with four bullets |
| h2 | Model weights | one sentence, a one-line `bash` download command, one sentence |
| h2 | Usage | one paragraph on input format |
| h3 | Single panorama | an untagged directory-tree block with `#` comments, a one-line `bash` command, a two-column Output / Content table |
| h3 | Multiple panoramas | one sentence with a bold requirement, an untagged tree, a `bash` command, two paragraphs on outputs and coordinate frames |
| h3 | Options | a two-column Flag / Effect table of eight flags |
| h2 | Demo data | one sentence crediting the CC0 panorama |
| h2 | Dataset split | one sentence with train and test counts |
| h2 | License | one paragraph, MIT plus vendored licenses |
| h2 | Citation | a `bibtex` block, no lead sentence |
| h2 | Acknowledgements | one sentence listing eight linked projects, one per source line |

Absent from the source: news or changelog, table of contents, results or benchmark table, GIF or embedded video, Quick Start section separate from Usage, model zoo table (one weights file), contact section, emoji in headings.

Present but unusual: the subtitle is an `###` heading inside the centred div; the authors are plain text without links; two of the four badges are not links; the teaser is two equal `49%` images on one line rather than one figure; the caption uses `<sub>`; the Method section is a figure with no prose; License comes before Citation; the Options table escapes a pipe as `on\|off` inside inline code.

## Components

**Centred Markdown header.** One `<div align="center">` with Markdown headings (`#`, `###`), plain lines, a bold line, HTML badge lines, the image pair and a `<sub>` caption, separated by blank lines.

**Badge row.** `<a href="..."><img src="https://img.shields.io/badge/arXiv-2603.05908-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"></a>` per line; label grey #555555, messages #b31b1b, #2f6f4f, #3776ab, #ee4c2c, each with a white logo.

**Side-by-side images.** Two `<img width="49%">` tags separated by one space on one line, followed by a blank line and a `<sub>` caption that names left and right.

**Bold-lead bullets.** `- **Feed-forward layout**: one clause.` Five bullets, each one sentence; the fourth ends the bold part without a colon ("**Coarse-to-fine refinement** with ...").

**Centred figure block.** `<div align="center"><img src="assets/method_overview.png" width="95%" alt="Method overview"></div>` with no caption.

**Code blocks.** `bash` for install, download and inference commands, with `#` comment lines grouping the install steps ("# CUDA extensions (nvcc must match the CUDA version of PyTorch)"); untagged fences for directory trees drawn with box characters and aligned `#` comments; `bibtex` for the citation.

**Tables.** Two columns each, `|--------|---------|` delimiters, no alignment colons. Left column in inline code (file names or flags), right column one short phrase.

**Collapsible notes.** `<details><summary>Notes</summary>` after the install block, holding four bullets with relative links into `third_party/`; plain summary, collapsed by default.

**Citation, license, acknowledgements.** `@inproceedings{qiu2026pano3dcomposer, ...}` with aligned `=` signs; one license paragraph with inline links; one acknowledgement sentence that lists linked projects one per source line and ends "We thank the authors for releasing their code."

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/teaser_input.jpg | JPEG, equirectangular panorama photo | 1024×512 | `<img ... width="49%" alt="Input panorama">` | about 419×210 | header, left of the pair |
| assets/teaser_scene.jpg | JPEG, rendered panorama of the generated scene | 1024×512 | `<img ... width="49%" alt="Generated compositional 3D scene">` | about 419×210 | header, right of the pair; `<sub>` caption below both |
| assets/method_overview.png | PNG, white background, pipeline diagram | 3189×1576 | `<div align="center"><img ... width="95%"></div>` | about 813×402 | only content of the Method section |

The teaser pair shows the same Poly Haven bedroom twice at the same 2:1 framing, so the comparison works without labels inside the images. The method figure has four colored regions (Preprocessing, Background Modeling, Composition, Object Generation & Alignment) and an amber-framed Alignment-VGGT band along the bottom. No `<picture>`, no dark variant, no GIF and no video.

## Adapting to Other Content

- **A library.** Keep the `#` name and `###` one-line description, drop authors and venue, keep the badge row with environment badges (Python #3776ab, PyTorch #ee4c2c) next to a docs link, and replace the image pair with a short code sample.
- **A dataset.** Keep the header; use the 49% pair for one raw sample and its annotation, and replace Model weights with a download section of the same shape (one sentence, one command, one sentence).
- **A benchmark with scores.** Add a Results section after Method with a numeric table; Pano3DComposer has no results table, so right-aligned numbers (`| ---: |`) and bold best values would be an extension.
- **A repo without a before/after pair.** Use one teaser at `width="95%"` (about 813px) in the div, keep the `<sub>` caption.
- **A repo with many views.** Three images at `width="32%"` (about 274px each) on one line keep the same one-line rhythm.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Separate a short name (`#`) from the full title (`###`) | Put a 75-character title in the h1 |
| Show input and output side by side at equal `49%` widths | Stack them vertically at full width |
| Name left and right in a one-line `<sub>` caption | Leave a comparison pair unlabelled |
| Give every badge a white logo and a brand message color | Mix logo and logo-less badges in one row |
| Group a long install script with `#` comments | Split each `pip install` into its own block |
| Collapse vendoring notes in `<details>` | Interrupt the install flow with caveats |
| Use two-column tables for outputs and flags | Explain each flag in prose |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside `<div align="center">`: `# ProjectName`, an `###` line with the full paper title, a plain author line joined by `&nbsp;·&nbsp;` with a `<sup>†</sup>` on the corresponding author, a plain affiliation line, a bold venue line, and four flat shields.io badges with white logos on label grey #555555: arXiv (message #b31b1b), Project Page (message #2f6f4f, `logo=googlechrome`), python 3.10 (message #3776ab), PyTorch 2.4 (message #ee4c2c). Then two `<img width="49%">` images on one line and a `<sub>` caption naming left and right. Close the div."
2. "After the div, write one paragraph with the main result in bold and five bullets that open with a bold phrase and a colon. Then plain `##` sections without emoji: Method (one `<div align="center"><img width="95%"></div>`), Installation, Model weights, Usage with `###` sub-sections, Demo data, Dataset split, License, Citation, Acknowledgements."
3. "In Installation, write one long `bash` block grouped by `#` comment lines and add `<details><summary>Notes</summary>` with short bullets after it. In Usage, show input layout as an untagged box-drawing tree with aligned `#` comments, then a one-line `bash` command and a two-column table with `|--------|---------|` delimiters. End with a `bibtex` block."

## Similar Pages

- readme-sisyphm-studiorecon: the same `<div align="center">` with `#` name, `###` subtitle, bold venue, a flat badge row and a teaser inside the div.
- readme-gradientspaces-world-from-motion: `#` name and `###` subtitle in a centred div, bold venue, but bold text links instead of badges.
- readme-xiyuche-geov2v: a centred `#`/`###` pair over a full-width image; it moves the authors below the teaser.

## Quick Start

````markdown
<div align="center">

# ProjectName

### Full Paper Title on One Line

Author One &nbsp;·&nbsp; Author Two<sup>†</sup>

University

**Venue Year**

<a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?logo=arxiv&logoColor=white" alt="arXiv"></a>
<a href="https://example.github.io/name/"><img src="https://img.shields.io/badge/Project-Page-2f6f4f?logo=googlechrome&logoColor=white" alt="Project page"></a>
<img src="https://img.shields.io/badge/python-3.10-3776ab?logo=python&logoColor=white" alt="Python 3.10">
<img src="https://img.shields.io/badge/PyTorch-2.4-ee4c2c?logo=pytorch&logoColor=white" alt="PyTorch 2.4">

<img src="assets/teaser_input.jpg" width="49%" alt="Input"> <img src="assets/teaser_output.jpg" width="49%" alt="Output">

<sub>Left: input. Right: output.</sub>

</div>

ProjectName turns X into an **editable result**: one sentence on how.

- **Feature one**: one clause.
- **Feature two**: one clause.
- **Feature three**: one clause.

## Method

<div align="center">
<img src="assets/method_overview.png" width="95%" alt="Method overview">
</div>

## Installation

Tested on Linux with Python 3.10 and PyTorch 2.4.

```bash
conda create -n name python=3.10 -y && conda activate name
pip install -r requirements.txt

# CUDA extensions
pip install ...
```

<details>
<summary>Notes</summary>

- Note one.
- Note two.

</details>

## Model weights

```bash
huggingface-cli download org/name weights.safetensors --local-dir checkpoints
```

## Usage

### Single input

```
demo/scene/
├── inputs/scene.jpg       # comment
└── masks/scene/           # comment
```

```bash
python scripts/infer.py --scene demo/scene --out outputs/scene
```

| Output | Content |
|--------|---------|
| `file.glb` | What it holds |

### Options

| Flag | Effect |
|------|--------|
| `--flag` | What it does |

## License

## Citation

```bibtex
@inproceedings{key,
  title = {...},
}
```

## Acknowledgements
````

## Provenance

- Repo: https://github.com/qiuzidian/Pano3DComposer (`README.md`, branch `main`, last README commit 891facb on 2026-10-05).
- Paper: "Pano3DComposer: Feed-Forward Compositional 3D Scene Generation from Single Panoramic Image", CVPR 2026, arXiv 2603.05908; first author Zidian Qiu. Project page https://qiuzidian.github.io/pano3dcomposer-page/.
- Selection: the header follows a clear hierarchy (name, subtitle, authors, venue, badges), the input/output teaser has a caption, and bold-lead feature bullets plus a collapsible Notes block keep a long install section in order.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, the two teaser JPEGs and `assets/method_overview.png` fetched from the repo for pixel sizes and accent colors.
- Written 2026-10-28.
