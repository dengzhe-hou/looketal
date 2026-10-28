# TORA — README Reference

> A method poster pinned above a well-kept manual: a two-line centred title, three slim badges, one wide red-to-blue architecture figure, then a nested contents list that hands you the rest.

**Theme:** light

Read from `README.md` on the default branch `master` of github.com/NahyukLEE/tora (last commit touching the file 9ca3970, 2026-04-07; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs; figure accent colors are medians of saturated pixels in `assets/architecture.png` fetched from the repo. Rendered positions are y values in the 1440×900 frame. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README is a paper title block followed by a tidy manual. A centred `<h1>` holds the full paper title broken onto two lines with `<br>`, and takes GitHub's grey bottom rule. Under it a `<div align="center">` carries one line of four linked authors with `\*` and `<sup>` marks, one affiliation line that also explains the asterisk, and a row of three shields.io badges (arXiv with the arXiv logo, Project Page, Hugging Face). A full-width architecture diagram (856×310 rendered) follows, then a bold-italic **TL;DR** line in italics. The body opens with a two-level Table of Contents and then uses plain `##`/`###` headings without emoji: Overview with a bold-lead "Key features" list, Getting Started (three `bash` blocks, a teacher-weights table), Usage (dataset table, training command, a GitHub TIP alert, a collapsed options block), Advanced (a collapsed Hydra config tree, a NOTE alert for FAQ), Citation, Acknowledgments and License. There is no news list, no results table and no GIF.

## Header Block

1. **Title** (y≈116 and 156, two lines): `<h1 align="center">TORA: Topological Representation Alignment<br>for 3D Shape Assembly</h1>`. GitHub h1, 2em (32px), weight 600; the `<br>` puts the break after "Alignment" rather than wherever the 856px line would wrap. The 1px grey rule sits under the second line at about y≈184.
2. **Authors** (y≈212): inside `<div align="center">`, one Markdown paragraph of four `[Name](url)` links, the first two followed by `\*<sup>,1</sup>` and `\*<sup>,2</sup>`, the others by `<sup>2</sup>` and `<sup>2,3</sup>`. Each name ends its source line with a comma; the newlines render as spaces, so the line reads "Nahyuk Lee\*,1, Zhiang Chen\*,2, Marc Pollefeys2, Sunghwan Hong2,3" in link blue.
3. **Affiliations and legend** (y≈253): `<sup>1</sup> Independent Researcher, <sup>2</sup> ETH Zurich, <sup>3</sup> ETH AI Center &ensp; | &ensp; \* denotes equal contribution`. Plain text; an en-space, a pipe and an en-space separate the affiliations from the equal-contribution note, so no separate footnote line is needed.
4. **Hidden comment**: `<!-- TODO: Add badges when available -->` sits above the badges and renders nothing.
5. **Badge row** (y≈290): three `[![alt](https://img.shields.io/badge/...)](url)` lines in the same paragraph, each 20px tall, total width about 405px (133 + 120 + 142 plus two spaces). Details in Badges.
6. **Teaser** (y≈326 to about 636): after the `</div>`, `<p align="center"><img src="assets/architecture.png" width="100%"></p>`. The PNG is 4074×1476 on an opaque white background; `width="100%"` renders it 856×310. No `alt`, no link, no caption under it.
7. **TL;DR** (y≈667–691, two lines): `**_TL;DR:_** *Assemble unposed 3D parts into complete objects using rectified flow with teacher-guided topological representation alignment.*` Left-aligned, outside any centred block. The label is bold italic and the sentence italic, so the line reads as a caption for the figure.
8. **Table of Contents** (h2 at y≈743): starts on the first screen; the list runs below the fold.

## Badges

All three are shields.io static badges in the default `flat` style (no `style=`): 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, white text, label on #555555.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv (arXiv logo) | 2604.04050 | #b31b1b (label #555555) | flat (default), `logo=arxiv`, `color=%23B31B1B` overrides the path color `blue` | arxiv.org/abs/2604.04050 |
| Project Page | TORA | #007ec6 (label #555555) | flat (default), path color `blue` | nahyuklee.github.io/tora/ |
| 🤗 Hugging Face | Space | #d8b800 (label #555555) | flat (default), path color `yellow`, the emoji is part of the label text | huggingface.co/NahyukLEE/tora |

The label names the destination and the message gives the identifier (the arXiv number) or the item ("TORA", "Space"). The `yellow` badge is served with fill #d8b800 and white message text; the shields.io named-color list in METHOD_README gives #dfb317 for `yellow`, and the served SVG is used here. The arXiv badge carries the white arXiv glyph on the grey label; the other two have no logo.

Colors on the page that are not badges come from the architecture figure: a brick red #9a3827 on the student side (the left of the "TORA" block, the student Gram matrix, the projector features) and a steel blue #2e6081 on the teacher side; both are pixel medians, and the block itself is a red-to-blue gradient. GitHub's TIP (green) and NOTE (blue) alerts appear further down in GitHub's own alert colors.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | TORA: Topological Representation Alignment / for 3D Shape Assembly | title, two lines via `<br>`; authors, affiliations, badges, teaser and TL;DR follow without a heading |
| h2 | Table of Contents | a nested bullet list of in-page anchors, six top-level items, with three sub-items under Getting Started, three under Usage and two under Advanced |
| h2 | Overview | one paragraph with **TORA** in bold |
| h3 | Key features | five bullets, each opening with a bold phrase ("**Rectified Flow**", "**6 teacher encoders**:") |
| h2 | Getting Started | section heading only |
| h3 | Setup | three one-line instructions each followed by a `bash` block (clone with `--recursive`, conda env, `bash install.sh`), then one line of versions |
| h3 | Teacher Weights | a three-column table (Model, Size, Description) with filenames in inline code, then one line on auto-download |
| h3 | TORA Checkpoints | one sentence with a Hugging Face link |
| h2 | Usage | section heading only |
| h3 | Data Preparation | one paragraph, a three-column dataset table (Dataset, Source, Note), one line and a `bash` block of commented conversion commands |
| h3 | Training | one paragraph, a multi-line `bash` command with `\` continuations, a `> [!TIP]` alert, and `<details><summary>Available configuration options</summary>` |
| h3 | Evaluation | one line, a `bash` command, one line listing metrics |
| h2 | Advanced | section heading only |
| h3 | Configurations | `<details><summary>Hydra configuration structure</summary>` with an untagged tree block and a parameter list |
| h3 | FAQ | a `> [!NOTE]` alert pointing to GitHub Issues |
| h2 | Citation | a `bibtex` block, no lead sentence |
| h2 | Acknowledgments | one paragraph naming Rectified Point Flow and REPA |
| h2 | License | one line pointing to LICENSE |

Absent from the source: news or changelog, results or benchmark table, demo GIF or video, a caption under the teaser, a separate venue line (the venue appears nowhere in the README), a Model Zoo heading (checkpoints are one sentence), contact section, emoji in headings.

Present but unusual: the h1 carries the full paper title split by a manual `<br>`; the equal-contribution legend shares the affiliation line after a pipe; the badges sit under a hidden `TODO` comment; the clone command contains a literal placeholder `https://github.com/<org>/tora.git`; the dataset table's header and body rows omit the trailing pipe; License follows Acknowledgments and is missing from the Table of Contents; the Advanced section holds only collapsed content and an alert.

## Components

**Centred div header.** Authors, affiliations and badges sit in Markdown paragraphs inside one `<div align="center">` with blank lines around the content, so Markdown links and badge images still parse. The title is a separate `<h1 align="center">` above it and the teaser a separate `<p align="center">` below it.

**Badge row.** `[![arXiv](https://img.shields.io/badge/arXiv-2604.04050-blue?logo=arxiv&color=%23B31B1B)](...)` style lines, label grey #555555, messages #b31b1b, #007ec6 and #d8b800. Alt text is the bare destination name ("arXiv", "ProjectPage", "Hugging Face").

**TL;DR line.** `**_TL;DR:_** *one sentence.*` directly under the teaser, left-aligned, one sentence of about 20 words.

**Nested table of contents.** A `- [Text](#anchor)` list with two-space-indented sub-items; it mirrors the `##` and most `###` headings (Key features is left out).

**Bold-lead feature list.** `- **Phrase** rest` or `- **Phrase**: list`; counts are folded into the bold part ("**6 teacher encoders**", "**3 alignment losses**").

**Instruction-then-block steps.** Each setup step is a one-line sentence ending in a colon, then its own `bash` block, so three short blocks replace one long script.

**Tables.** Pipe tables with `|:---|` left-alignment colons on every column. Filenames in inline code in the first column, sizes as "178 MB", short descriptions. GitHub draws the grid and stripes alternate rows; no bold values.

**Alerts.** `> [!TIP]` after the training command (pointing to the upstream training guide) and `> [!NOTE]` as the whole FAQ section. GitHub renders each with a colored left bar, icon and title.

**Collapsible blocks.** `<details><summary>Available configuration options</summary>` holding bold-label lines ("**Teachers**: `uni3d` (default), ...") and a `bash` block of overrides; `<details><summary>Hydra configuration structure</summary>` holding an untagged code block with a box-drawing tree and `# comments`, then a bullet list of key parameters. Summaries are plain text, not bold.

**Code blocks.** `bash` for every command (with `#` comments inside the conversion block and `\` line continuations in training and evaluation), an untagged fence for the config tree, `bibtex` for the citation.

**Citation.** `@article{lee2026tora, ...}` with aligned `=` signs and `journal = {arXiv preprint arXiv:2604.04050}`; no lead sentence.

**Acknowledgments and license.** One linked paragraph; one line "See the [LICENSE](LICENSE) file for details."

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/architecture.png | PNG, opaque white background, diagram with rendered point clouds | 4074×1476 | `<p align="center"><img src="assets/architecture.png" width="100%"></p>` | 856×310 | header, directly after the badge div; TL;DR line below |

The figure reads left to right: a grey "Flow Matcher" column of DiT blocks with a highlighted late layer, a "3D Point Teacher" box and a "Projector" box feeding a central "TORA" block shaded from brick red #9a3827 to steel blue #2e6081, and on the right a large rounded panel comparing a red Student Gram Matrix with a blue Teacher Gram Matrix, the CKA loss formula, and the title "Topological Representation Alignment (TORA)" with the initials colored. It is the only image in the README. No `<picture>`, no dark variant, no GIF and no video link.

## Adapting to Other Content

- **A library.** Keep the two-line `<h1>` (name and one-line description joined by `<br>`), drop authors and affiliations, keep one three-badge row (Docs, PyPI, License) in the same flat label-grey form, swap the architecture figure for a short code sample and keep the TL;DR line.
- **A dataset.** Keep the header and put a sample grid at `width="100%"` (856px) where the architecture figure is; turn Teacher Weights into a file table with the same Model, Size, Description columns (file, size, contents).
- **A benchmark with scores.** Add a results table under Evaluation with the same `|:---|` style for text columns and right-aligned numeric columns; TORA itself only lists metric names, so this is an extension.
- **A repo without a teaser.** Let the TL;DR line follow the badge row directly, then the Table of Contents.
- **A short README.** Drop the Table of Contents and the Advanced section; it pays off only with more than about eight sections.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Break a long title with one deliberate `<br>` in the `<h1>` | Let a 60-character title wrap wherever the column ends |
| Put the equal-contribution note on the affiliation line after `&ensp; \| &ensp;` | Add a separate footnote paragraph for one symbol |
| Follow the teaser with a single bold-italic TL;DR sentence | Leave the figure without any one-line summary |
| Mirror the heading tree in a nested Table of Contents | Link only top-level sections when most content sits in `###` |
| Fold optional configuration into `<details>` with a plain summary | Inline every Hydra override in the main flow |
| Replace `<org>` placeholders before publishing | Ship a clone command that cannot be pasted |
| List License in the Table of Contents if it has a heading | Add sections after the TOC that the TOC omits |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown: `<h1 align="center">` with the full paper title split into two lines by `<br>`, then a `<div align="center">` holding a comma-separated author line with `\*` and `<sup>` marks, one line of `<sup>`-numbered affiliations followed by `&ensp; | &ensp; \* denotes equal contribution`, and three flat shields.io badges on label grey #555555 (arXiv with `logo=arxiv` and message #b31b1b, Project Page message #007ec6, 🤗 Hugging Face message #d8b800). Close the div, add `<p align="center"><img src="assets/architecture.png" width="100%"></p>` and a bold-italic `**_TL;DR:_**` line in italics."
2. "After the header, add `## Table of Contents` as a nested list of anchors, then `## Overview` with one bold-name paragraph and a `### Key features` list where each bullet starts with a bold phrase. Use plain headings without emoji: Getting Started (Setup, Teacher Weights, Checkpoints), Usage (Data Preparation, Training, Evaluation), Advanced (Configurations, FAQ), Citation, Acknowledgments, License."
3. "In Setup, write each step as one sentence ending in a colon and its own `bash` block. Use `|:---|` left-aligned tables with filenames in inline code. Put optional flags in `<details><summary>Available configuration options</summary>` with bold labels, a `> [!TIP]` after the training command and a `> [!NOTE]` for an unfinished FAQ. End with a `bibtex` block."

## Similar Pages

- readme-gradientspaces-world-from-motion: same research lineage (TORA builds on GradientSpaces' Rectified Point Flow) and the same centred author-plus-affiliation block, but it puts the subtitle in `###` and uses bold text links instead of badges.
- readme-yebulabula-uniscene3d: another ECCV 2026 3D paper with a centred header and an arXiv badge that uses `logo=arxiv`; it adds a logo image above the title.
- readme-qiuzidian-pano3dcomposer: a full-width teaser right after a short badge row and a bold-lead feature list, with the title split into a name and an `###` subtitle instead of one two-line `<h1>`.

## Quick Start

````markdown
<h1 align="center">ProjectName: First Half of the Paper Title<br>Second Half of the Title</h1>

<div align="center">

[Author One](https://example.org/)\*<sup>,1</sup>,
[Author Two](https://example.org/)\*<sup>,2</sup>,
[Author Three](https://example.org/)<sup>2</sup>,
[Author Four](https://example.org/)<sup>2,3</sup>

<sup>1</sup> Institution A, <sup>2</sup> Institution B, <sup>3</sup> Institution C &ensp; | &ensp; \* denotes equal contribution

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-blue?logo=arxiv&color=%23B31B1B)](https://arxiv.org/abs/XXXX.XXXXX)
[![ProjectPage](https://img.shields.io/badge/Project_Page-Name-blue)](https://example.github.io/name/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-yellow)](https://huggingface.co/org/name)

</div>

<p align="center">
  <img src="assets/architecture.png" width="100%">
</p>

**_TL;DR:_** *One sentence that says what the method does and how.*

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Setup](#setup)
  - [Weights](#weights)
- [Usage](#usage)
  - [Data Preparation](#data-preparation)
  - [Training](#training)
  - [Evaluation](#evaluation)
- [Citation](#citation)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

**ProjectName** is ... One paragraph.

### Key features
- **Feature one** for ...
- **3 options**: A, B, C

## Getting Started

### Setup

Clone the repository:

```bash
git clone --recursive https://github.com/org/name.git
cd name
```

Install dependencies:

```bash
bash install.sh
```

### Weights

| Model | Size | Description |
|:---|:---|:---|
| `model_base.pt` | 178 MB | Base encoder |

## Usage

### Data Preparation

### Training

```bash
python train.py \
    data_root="../dataset" \
    trainer.devices=8
```

> [!TIP]
> Point to the upstream guide for the base pipeline.

<details>
<summary>Available configuration options</summary>

**Options**: `a` (default), `b`, `c`

</details>

### Evaluation

```bash
python sample.py ckpt_path=./output/best.ckpt
```

## Citation

```bibtex
@article{key,
  title     = {...},
}
```

## Acknowledgments

## License

See the [LICENSE](LICENSE) file for details.
````

## Provenance

- Repo: https://github.com/NahyukLEE/tora (`README.md`, branch `master`, last README commit 9ca3970 on 2026-04-07).
- Paper: "TORA: Topological Representation Alignment for 3D Shape Assembly", ECCV 2026, arXiv 2604.04050; first author Nahyuk Lee. Project page https://nahyuklee.github.io/tora/.
- Selection: the wide method teaser is crisp, a one-line italic TL;DR follows it, and the nested table of contents, Key features list and small weights table are cleanly formatted.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the three badge URLs, `assets/architecture.png` fetched from the repo for pixel size, background and accent colors.
- Written 2026-10-28.
