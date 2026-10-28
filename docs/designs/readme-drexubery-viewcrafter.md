# ViewCrafter — README Reference

> A contact sheet in motion: a wordmark and four badges up top, then ruled grids where a still photo, a tiny camera path and a moving render sit side by side.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/Drexubery/ViewCrafter (last commit touching the file 9f3884f, 2025-12-12; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; image sizes, frame counts and logo colors come from `assets/logo.png` and sample grid files (`train.png`, `ctrain.gif`, `train.gif`, `car2_1.png`, `car2.gif`) fetched from the repo. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them. Rendered y values below are in the 1440×900 frame.

## Overview

The page opens with the paper title as a left-aligned bold-italic `##` heading, then a centred block: a 100px-tall logo (a mint and lavender cube beside a black italic "ViewCrafter" wordmark), four flat badges separated by `&nbsp;`, two lines of bold-italic blue author links with `*` and `†` marks, and a bold TPAMI 2025 venue line. A left-aligned "please help ⭐ this repo" line follows. The body uses emoji `##` headings (🔆 Introduction, 🧰 Models, ⚙️ Setup, 💫 Inference, 📈 Evaluation, 😉 Citation, 📢 Disclaimer). The Introduction starts with a four-item dated changelog, then shows results as two HTML `<table>` image grids: for single-view input, columns Reference image / Camera trajectory / Generated novel view video with a still PNG, a small trajectory GIF and an output GIF per row; for two-view input, two reference PNGs and an output GIF. Each grid has three rows. A six-column Markdown model table lists resolution, frames, GPU memory with inference time and Hugging Face checkpoint links. Setup and Inference are numbered h3 steps with `bash` blocks and one GitHub `[!NOTE]` alert. The page ends with a `bib` citation block and a disclaimer closed by a horizontal rule.

## Header Block

1. **Title** (y≈110 and 140): `## ___***ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis***___`. GitHub nests the emphasis as `<em><strong><em><strong>`, so it renders as a bold-italic h2, 1.5em (24px), left-aligned and outside the centred block, wrapping after "View". GitHub's 1px h2 rule sits under it (y≈161). It is the first entry in GitHub's outline menu.
2. **Centred block opens**: `<div align="center">`.
3. **Logo** (y≈192 to 274): `<img src='assets/logo.png' style="height:100px"></img>`. GitHub keeps the `height` style; the 1306×295 PNG renders about 443×100, centred, and links to itself. The logo repeats the project name, so "ViewCrafter" appears twice on the first screen.
4. **Badge row** (y≈294): four `<a href='...'><img src='https://img.shields.io/badge/...'></a>` lines, each followed by `&nbsp;`, one leading space per line. Flat style, 20px tall; widths 116, 86, 96 and 142px, so the row spans about 470px with the gaps. Details in Badges.
5. **Authors** (y≈338 and 362): `_**[Wangbo Yu*](...), [Jinbo Xing*](...), [Li Yuan&dagger;](), ... <br> [Xiangjun Gao](...), ... [Yonghong Tian&dagger;]()**_`. The whole line is bold italic, so the ten names render as bold-italic link-blue text; the marks are typed inside the link text as `*` and `&dagger;` rather than in `<sup>`. Three names link to an empty `()` target, and `<br>` breaks the list after the sixth name.
6. **Spacer**: a bare `<br>` after the authors.
7. **Venue line** (y≈402): `<strong>Transactions on Pattern Analysis and Machine Intelligence (TPAMI) 2025</strong>` followed by another `<br>`. Body size, bold, centred, no link.
8. **Centred block closes**: `</div>`. No affiliation line and no definition of `*` and `†`.
9. **Star request** (y≈442): `🤗 If you find ViewCrafter useful, **please help ⭐ this repo**, which is important to Open-Source projects. Thanks!` as a left-aligned paragraph.
10. **Introduction** (heading at y≈494): `## 🔆 Introduction`, then the dated news list (y≈544 to 628), a one-paragraph capability statement with a bold `<strong>a single or sparse reference image</strong>`, and `### Zero-shot novel view synthesis (single view)` (y≈742) with the first grid starting at y≈788. The first row of images reaches the fold. This ends the header block.

## Badges

All four use the static path form with no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 and white (#ffffff) text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2409.02048 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2409.02048 |
| Project | Page | `Green`, rendered #44bb00 (label #555555) | flat (default) | drexubery.github.io/ViewCrafter/ |
| Youtube | Video | #b31b1b (label #555555) | flat (default) | youtube.com/watch?v=WGIEmu9eXmU |
| 🤗 Hugging Face | Demo | `blue`, rendered #007ec6 (label #555555) | flat (default) | huggingface.co/spaces/Doubiiu/ViewCrafter |

`Green` (capitalised) came back as #44bb00 (`#4b0` in the SVG) on 2026-10-28, and `blue` as #007ec6. The YouTube badge reuses the arXiv red #b31b1b rather than a YouTube red. None of the `<img>` tags has an `alt`. There is no link row of bold text links.

Colors outside the badges: the logo has an opaque white #ffffff background, a black #000000 italic wordmark and outline, and a cube with mint #9bfde1 faces and lavender faces (the lavender hex was not isolated from its gradient).

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h2 | ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis | bold-italic title; logo, badges, authors and venue follow in a centred div, then the star-request line |
| h2 | 🔆 Introduction | four news bullets with bold `__[YYYY-MM-DD]__` dates, one capability paragraph, two h3 image grids |
| h3 | Zero-shot novel view synthesis (single view) | HTML table, header row Reference image / Camera trajecotry / Generated novel view video, three rows of PNG, trajectory GIF and output GIF |
| h3 | Zero-shot novel view synthesis (two views) | HTML table, header row Reference image 1 / Reference image 2 / Generated novel view video, three rows of two PNGs and an output GIF |
| h2 | 🧰 Models | six-column Markdown table: Model, Resolution, Frames, GPU Mem. & Inference Time, Checkpoint, Description |
| h2 | ⚙️ Setup | h3 `1. Clone ViewCrafter` and h3 `2. Installation`, each a `bash` block; a `> [!NOTE]` alert about CUDA OOM on newer PyTorch |
| h2 | 💫 Inference | h3 `1. Command line`, then h3 Single view and h3 Sparse view with `(1)`/`(2)` steps and one-line `bash` blocks; h3 `2. Local Gradio demo`; h3 `3. Local Gradio demo with Docker` with an untagged block |
| h2 | 📈 Evaluation | one sentence, a one-line `bash` block, one paragraph on the input folder |
| h2 | 😉 Citation | one sentence and a `bib` block (highlighted as BibTeX) |
| h2 | 📢 Disclaimer | preceded by `<a name="disc"></a>`; one paragraph starting with ⚠️, then `****`, which renders as a closing horizontal rule |

Absent from the source: an h1 (the title is an h2), affiliations, definition of the author marks, results table with numbers, teaser figure above the fold, table of contents, `<details>` blocks, license section, acknowledgements, a separate News heading.

Present but unusual: the image grids are HTML `<table>` elements, not Markdown tables; GitHub strips their `class="center"` and the header row's `style="font-weight: bolder;text-align:center;"`, so the grids sit left-aligned and the header cells render in normal weight as ordinary `<td>` cells; the header text has a typo ("Camera trajecotry"); the news list sits under "Introduction" rather than its own heading, with dates written in two formats (`2024-11-6` and `2024-10-15`); the inference steps end lines with ` \` to force a line break; the logo repeats the title's project name directly under it.

## Components

**Bold-italic heading title.** `## ___***Title***___`: triple underscores around triple asterisks give bold italic, and the heading level is h2, so it is smaller than a usual h1 title and carries the h2 rule.

**Centred identity block.** `<div align="center">` with the logo `<img ... style="height:100px">`, the badge row, the bold-italic author paragraph and a `<strong>` venue line, using bare `<br>` tags for extra space.

**Badge row with `&nbsp;` gaps.** `<a href='url'><img src='https://img.shields.io/badge/Label-Message-color'></a> &nbsp;` four times. Label #555555; messages #b31b1b, #44bb00, #b31b1b, #007ec6.

**News bullets.** `- __[2024-10-15]__: 🔥🔥 Release the code for ...`: bold bracketed date by double underscores, a colon, optional emoji, a sentence starting with a verb; newest first.

**Image-grid table.** A raw `<table>` whose first `<tr>` holds three `<td>` column titles, followed by `<tr>` rows of `<td><img src=assets/name.png width="250"></td>` cells. Inputs are PNG stills, the camera path is a GIF at `width="150"`, outputs are GIFs at `width="250"`. Each grid has three example rows, one example per row, read left to right as input, control and output.

**Model table.** A Markdown pipe table with every column left-aligned (`|:---------|`). The memory column combines memory and time in one cell (`23.5GB & 120s (`perframe_ae=True`)`); the Checkpoint column is a `[Hugging Face](...)` link; Description is a short use note ("used for ablation").

**Numbered h3 steps.** Headings written `### 1. Clone ViewCrafter`, `### 2. Installation`, and inside Inference `(1)`/`(2)` paragraph steps ending in ` \` line breaks.

**Alert.** GitHub alert syntax `> [!NOTE]` with one sentence and an issue link; it renders with the blue NOTE title and left bar.

**Code blocks.** `bash` blocks with `#` comment lines and blank lines between conda, PyTorch3D and checkpoint groups; one-command blocks indented two spaces (`  sh run.sh`); one untagged `docker compose` block; a `bib` block for the citation.

**Disclaimer.** An `<a name="disc"></a>` anchor, a `##` heading and a ⚠️ paragraph, closed by `****` (a thematic break).

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/logo.png | PNG, opaque white background, cube icon and italic wordmark | 1306×295 | `<img src='assets/logo.png' style="height:100px">` in the centred div | about 443×100 | header, under the title |
| assets/train.png, wst.png, flower.png | PNG stills, reference photos | 908×512 (train.png) | `<img src=... width="250">` in a `<td>` | 250×141 | single-view grid, column 1 |
| assets/ctrain.gif, cwst.gif, cflower.gif | GIF, 25 frames, camera path on a 3D grid | 320×240 (ctrain.gif) | `width="150"` | 150×113 | single-view grid, column 2 |
| assets/train.gif, wst.gif, flower.gif | GIF, 25 frames, generated video | 1024×576 (train.gif, about 8 MB) | `width="250"` | 250×141 | single-view grid, column 3 |
| assets/car2_1.png, car2_2.png, barn_0.png, barn_2.png, house_1.png, house_2.png | PNG stills, paired reference views | 1712×958 (car2_1.png) | `width="250"` | 250×140 | two-view grid, columns 1 and 2 |
| assets/car2.gif, barn.gif, house.gif | GIF, 25 frames, generated video | 1024×576 (car2.gif, about 8 MB) | `width="250"` | 250×141 | two-view grid, column 3 |

With cell padding the single-view grid renders about 730px wide and the two-view grid about 830px, both left-aligned in the 856px column. The output GIFs play automatically, so the results section is the page's motion. There is no static teaser figure, no `<picture>` pair and no dark-theme logo; the logo's opaque white background would show as a white box on GitHub's dark theme (inferred from the alpha channel, not captured). The YouTube video is reached only through its badge.

## Adapting to Other Content

- **A library.** Keep the centred logo at `height:100px` and the four-badge row (Docs, PyPI, Demo, License), replace the image grids with a two-column input/output code example table, and promote Setup above the examples.
- **A dataset.** Use the grid table for samples: one row per scene, columns for modality (RGB, depth, mask) at `width="250"` (about 830px for three columns), and put a counts table in place of the model table.
- **A benchmark.** Keep the grid for qualitative examples and add a Markdown results table after Models with numeric columns right-aligned (`---:`) and bold best values; ViewCrafter has no such table.
- **A repo without GIFs.** Fill column 3 with still PNGs at the same `width="250"`, and add a project-page or video badge for motion.
- **When adapting.** Make the title an h1 rather than an h2, drop the repeated name if the logo is a wordmark, add `alt` text to badges and grid images, and centre the grids with `<div align="center">` around the table, since GitHub removes `class="center"`.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Lay out qualitative results as input, control and output columns in a table | Drop a dozen GIFs one after another without structure |
| Size inputs and outputs to the same `width="250"` and the control column smaller (`width="150"`) | Let each image render at its own native width |
| Put memory, inference time and checkpoint link in one model table row | Scatter checkpoint links through prose |
| Use GitHub's `> [!NOTE]` alert for a known installation pitfall | Put the pitfall in a code comment |
| Write news bullets with one date format | Mix `2024-11-6` and `2024-10-15` styles |
| Rely on `<div align="center">` to centre a table | Expect `class="center"` or inline `style` on `<tr>` to survive GitHub's sanitiser |
| Give the title one emphasis style | Repeat the project name in a bold-italic heading and a wordmark logo stacked together |

## Agent Prompt Guide

1. "Write a README header: `## ___***Full Paper Title***___` as a bold-italic h2, then `<div align="center">` with a logo `<img src='assets/logo.png' style="height:100px">`, four flat shields.io badges separated by `&nbsp;` (label #555555; arXiv ID #b31b1b, Project Page #44bb00, Youtube Video #b31b1b, 🤗 Hugging Face Demo #007ec6), a bold-italic author line `_**[Name*](url), ...**_` with `<br>` after the sixth name, and a `<strong>` venue line; close the div and add a one-line star request."
2. "Under `## 🔆 Introduction`, write four news bullets `- __[YYYY-MM-DD]__: ...`, one paragraph, then `### Zero-shot ... (single view)` with an HTML `<table>`: a first row of three `<td>` titles (Reference image, Camera trajectory, Generated novel view video) and three rows of `<td><img src=... width="250"></td>`, `width="150"` for the trajectory GIF and `width="250"` for the output GIF. Repeat with a two-reference-image grid."
3. "Add `## 🧰 Models` as a six-column left-aligned Markdown table (Model, Resolution, Frames, GPU Mem. & Inference Time, Checkpoint as a Hugging Face link, Description), then `## ⚙️ Setup` with numbered h3 steps and `bash` blocks plus a `> [!NOTE]` alert, `## 💫 Inference`, `## 📈 Evaluation`, `## 😉 Citation` with a `bibtex` block, and `## 📢 Disclaimer`."

## Similar Pages

- readme-vveicao-freeorbit4d builds the same kind of HTML-table GIF grid (input and output GIFs at `width="280"` in `<td align="center">` cells), so the two can be compared directly on cell width and alignment.
- readme-mdyao-photoagent and readme-nvlabs-motionbricks also place images inside table cells; readme-guangzhaohe-ernet uses GIFs as well.
- ViewCrafter's distinguishing choices are the three-column input / camera path / output grid and the model table with memory and time per checkpoint. Its project page (drexubery.github.io/ViewCrafter/) is a separate web page and is not described here.

## Quick Start

````markdown
## ___***ProjectName: Full Paper Title***___
<div align="center">
<img src='assets/logo.png' style="height:100px"></img>

 <a href='https://arxiv.org/abs/XXXX.XXXXX'><img src='https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg'></a> &nbsp;
 <a href='https://example.github.io/project/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> &nbsp;
 <a href='https://www.youtube.com/watch?v=XXXX'><img src='https://img.shields.io/badge/Youtube-Video-b31b1b.svg'></a> &nbsp;
 <a href='https://huggingface.co/spaces/org/name'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Demo-blue'></a> &nbsp;

_**[Author One*](https://example.org/), [Author Two*](https://example.org/), [Author Three&dagger;](https://example.org/)**_
<br>

<strong>Venue Name (ABBR) Year</strong>
<br>
</div>

🤗 If you find ProjectName useful, **please help ⭐ this repo**. Thanks!

## 🔆 Introduction

- __[YYYY-MM-DD]__: Release the code.

One paragraph with **the key capability** in bold. Below shows some examples:

### Examples (single input)
<table>
  <tr>
    <td>Reference image</td>
    <td>Camera trajectory</td>
    <td>Generated video</td>
  </tr>
  <tr>
    <td><img src=assets/input.png width="250"></td>
    <td><img src=assets/path.gif width="150"></td>
    <td><img src=assets/output.gif width="250"></td>
  </tr>
</table>

## 🧰 Models

|Model|Resolution|Frames|GPU Mem. & Inference Time|Checkpoint|Description|
|:---------|:---------|:--------|:--------|:--------|:--------|
|Name|576x1024|25|23.5GB & 120s|[Hugging Face](https://huggingface.co/org/name)|Use note|

## ⚙️ Setup

### 1. Clone ProjectName
```bash
git clone https://github.com/org/name.git
cd name
```
### 2. Installation
```bash
conda create -n env python=3.9
conda activate env
pip install -r requirements.txt
```
> [!NOTE]
> One known pitfall with a link to the issue.

## 💫 Inference
### 1. Command line
```bash
  sh run.sh
```

## 📈 Evaluation

## 😉 Citation
Please consider citing our paper if our code is useful:
```bibtex
@article{key2025,
  title={...},
}
```

## 📢 Disclaimer
⚠️ One paragraph.
````

## Provenance

- Repo: https://github.com/Drexubery/ViewCrafter (`README.md`, branch `main`, last README commit 9f3884f on 2025-12-12).
- Paper: "ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis", TPAMI 2025 (per the README venue line; the README's BibTeX still cites the arXiv preprint), arXiv 2409.02048; first author Wangbo Yu. Project page https://drexubery.github.io/ViewCrafter/.
- Selection: tables used as image grids (reference, trajectory, output) give an orderly results gallery, and the model-zoo table lists memory, time and checkpoint links in one place, though the italic title repeated above the logo is slightly redundant. The selection note calls the grids Markdown tables; the source shows they are raw HTML `<table>` elements.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `assets/logo.png` and six grid assets fetched from the repo for pixel sizes, frame counts and colors.
- Written 2026-10-28.
