# ERNet — README Reference

> A lab notebook with tabbed dividers: a centred title page, two rows of colored tabs that jump to numbered steps, and a teaser that pairs the result with the speed chart that justifies it.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/guangzhaohe/ERNet (last commit touching the file c913da1, 2026-09-12; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs; teaser accent colors are medians of saturated pixels in `assets/ernet_teaser.png` fetched from the repo. Rendered positions are y values in the 1440×900 frame. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README is a usage guide with a paper header on top. A `<div align="center">` holds a Markdown `#` title (the full paper title, wrapping to two lines with GitHub's h1 rule), a bold venue line, five linked authors on one line, one affiliation, and eight shields.io badges split by a `<br>` into two rows: the first row points outward (Paper PDF, arXiv, Project Page) plus a jump to the weights, the second row is in-page navigation (Setup, Inference Demo, Citation) plus the license. Below the div a three-sentence intro names the paper in bold, and a full-width two-panel teaser (856×320) pairs a rendered registration result with an accuracy-versus-FPS scatter plot. The body is a numbered procedure: a task-list "Release checklist", then "1. Download the model weights" (a four-column checkpoint table), "2. Set up the environment" and "3. Run inference" with four `###` cases and an options table, followed by Acknowledgements, Issues, Citation and License. There is no news list, no table of contents and no emoji.

## Header Block

All items down to the badges are Markdown or HTML inside one `<div align="center">` with blank lines around the content.

1. **Title** (y≈139 and 180, two lines): `# ERNet: Efficient Non-Rigid Registration Network for Point Sequences`. GitHub h1, 2em (32px), weight 600; it wraps before "Sequences" at 856px, and the 1px grey rule sits under the second line at about y≈208.
2. **Venue** (y≈236): `**ICCV 2025**`. Bold body text placed above the authors, not below.
3. **Authors** (y≈277): five `[Name](url),` lines, one per source line, which render as one comma-separated line of link-blue names. No affiliation marks (single institution).
4. **Affiliation** (y≈317): `Zhejiang University`. Plain text.
5. **Badge row 1** (y≈354): four `<a href="..."><img src="https://img.shields.io/badge/..." alt="..."></a>` lines, about 382px wide in total (84 + 116 + 79 + 91 plus three spaces).
6. **Badge row 2** (y≈380): after a `<br>`, four more badges, about 345px wide (43 + 99 + 53 + 138 plus three spaces). The two rows are centred independently, so their edges do not line up.
7. **Intro** (y≈425–473, three lines, after `</div>`): "Official inference implementation of **ERNet: Efficient Non-Rigid Registration Network for Point Sequences (ICCV 2025)**." then two plain sentences. Left-aligned.
8. **Teaser** (y≈504 to about 824): `![ERNet registration results on sparse and partial point sequences](assets/ernet_teaser.png)` as its own paragraph. No width; GitHub's `max-width: 100%` scales the 5366×2005 PNG to 856×320. The panel captions "(a) ERNet Registered Trajectories" and "(b) Comparison Results on D-FAUST" are inside the image.
9. **Release checklist** (h2 at y≈865): the heading closes the first screen.

## Badges

All eight are shields.io static badges with no `style=` or `logo=`, so they render in the default `flat` style: 20px tall, 3px corner radius, faint vertical gloss, Verdana 11px, white text. Four use the two-part `label-message-color` path; four use the one-part `message-color` path, which renders a single colored block with no grey label.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Paper | ERNet | #007ec6 (label #555555) | flat (default), path color `blue` | arxiv.org/pdf/2510.15800 |
| arXiv | 2510.15800 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2510.15800 |
| (none) | Project Page | #67ac09 | flat, one part, path color `green` | guangzhaohe.com/ernet/ |
| (none) | Model Weights | #ea7233 | flat, one part, path color `orange` | `#1-download-the-model-weights` |
| (none) | Setup | #007ec6 | flat, one part, path color `blue` | `#2-set-up-the-environment` |
| (none) | Inference Demo | #800080 | flat, one part, path color `purple` (CSS named color, passed through as `fill="purple"`) | `#3-run-inference` |
| (none) | Citation | #555555 | flat, one part, path color `gray` | `#citation` |
| License | CC BY-NC 4.0 | #939393 (label #555555) | flat (default), path color `lightgrey` | LICENSE |

Row 1 is "where the paper lives" plus the weights jump; row 2 is "what to do here". Four badges are in-page anchors to numbered headings, so the badge rows double as a table of contents. The served SVGs give #67ac09 for `green`, #ea7233 for `orange` and #939393 for `lightgrey`; the shields.io named-color list in METHOD_README gives #97ca00, #fe7d37 and #9f9f9f for those names, and the served values are used here. Underscores in the path render as spaces ("Project_Page", "Inference_Demo") and `--` as a hyphen ("CC_BY--NC_4.0").

Colors on the page that are not badges come from the teaser: periwinkle blue #7f8fe4 and lavender #a495dd on the registered trajectories and the baseline points (pixel medians), with ERNet's own marker a pink-red triangle #ce7282, all on a pale blue ground plane and a light grey plot card.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | ERNet: Efficient Non-Rigid Registration Network for Point Sequences | title; venue, authors, affiliation and both badge rows follow in the same div; the intro and teaser follow the div without a heading |
| h2 | Release checklist | a five-item task list (three `[x]`, two `[ ]`), then one paragraph on what comes later |
| h2 | 1. Download the model weights | two sentences, a four-column checkpoint table, one paragraph, a `text` block of the expected `model/` tree, one paragraph |
| h2 | 2. Set up the environment | one paragraph of requirements, a `bash` block (clone, `CUDA_HOME=... bash setup.sh`, activate), one paragraph, a one-line `bash` check |
| h2 | 3. Run inference | section heading only |
| h3 | Included examples | one paragraph, a `bash` block with two commented commands, a `text` block of output paths, two paragraphs (one with the four panel names in bold joined by arrows) |
| h3 | Your own template and point sequence | one paragraph with a link to the input format, a `bash` command |
| h3 | DT4D animation files | one sentence, a `bash` command, one paragraph |
| h3 | Useful options | a two-column Option / Purpose table of six flags, two closing sentences |
| h2 | Acknowledgements | one paragraph of linked components |
| h2 | Issues | one paragraph asking for command, traceback, GPU and versions |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | License | copyright line, a paragraph with the license name in bold, a paragraph on third-party terms |

Absent from the source: news or changelog, table of contents (the badge rows play that role), results table, GIF or embedded video, training or evaluation sections (listed as unchecked in the release checklist), emoji in headings, `<details>` blocks.

Present but unusual: the badge rows link to in-page anchors of numbered headings; four badges have no label segment; the Paper badge and the arXiv badge point to the same paper (PDF and abstract); the venue line sits above the authors; procedural `##` headings are numbered "1." to "3." while the remaining `##` headings are not; the output video paths are given in a `text` block rather than embedded; an Issues section says exactly what to include in a bug report.

## Components

**Centred Markdown header.** One `<div align="center">` holding a `#` heading, a bold line, author link lines, a plain line and HTML badge lines, separated by blank lines.

**Two badge rows.** Eight `<a href><img src="https://img.shields.io/badge/..." alt="..."></a>` lines with a `<br>` after the fourth. Row 1 messages #007ec6, #b31b1b, #67ac09, #ea7233; row 2 #007ec6, #800080, #555555, #939393; two-part badges keep label grey #555555. Alt text matches the visible words ("Paper PDF", "arXiv", "Setup", "License: CC BY-NC 4.0").

**Numbered procedure headings.** `## 1. Download the model weights`, `## 2. Set up the environment`, `## 3. Run inference`; GitHub turns them into anchors `#1-download-the-model-weights` and so on, which the badges use.

**Release checklist.** `- [x] Release inference code ...` and `- [ ] Release the training code ...` lines; GitHub renders read-only checkboxes. Each item is one sentence ending in a period.

**Checkpoint table.** Four columns (Model, When to use it, Checkpoint filename, Download) with `| --- |` delimiters and no alignment colons. Model names in bold (**PCL**, **DEP**), a two-sentence "when to use" cell, the filename in inline code, and "Google Drive" as the link text.

**Options table.** Two columns (Option, Purpose); flags in inline code, sometimes two per cell joined by " / ", purposes as full sentences.

**Code blocks.** `bash` for commands, with `#` comments naming each case ("# Surface-sampled points → PCL model"); `text` for directory trees and output paths; `bibtex` for the citation.

**Bold inline sequence.** The output description uses one bold run with arrows: **input template → input points → predicted anchors → predicted mesh**.

**Citation and license.** "If you use ERNet in your research, please cite our paper:" then `@inproceedings{he2025ernet, ...}` with aligned `=` signs. License text in three short paragraphs with the license name in bold and links to LICENSE and THIRD_PARTY.md.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/ernet_teaser.png | PNG, opaque white background, two panels with in-image captions | 5366×2005 | `![ERNet registration results on sparse and partial point sequences](assets/ernet_teaser.png)`, no width | 856×320 | after the intro paragraph, before Release checklist |

Panel (a) is a 3D render: a bunny-like mesh moving along a rainbow arc of trajectories over a pale blue ellipse, with three tilted labels (Source Object, Sparse Point Sequence, ERNet Registration). Panel (b) is a scatter plot of ATE3D against FPS on a rounded light grey card, with baselines TCSR, NICP, NSFP and NDP as circles and "ERNet (Ours)" as a pink-red triangle in the lower right. It is the only image in the README; the output videos are named as paths, not embedded. No `<picture>`, no dark variant and no GIF.

## Adapting to Other Content

- **A library.** Keep the two badge rows: row 1 for Docs, PyPI and License, row 2 for in-page anchors (Install, Quick Start, API). Number the procedural headings so the anchors stay short.
- **A dataset.** Replace the checkpoint table with a split table of the same four-column shape (Split, When to use it, File, Download) and keep the Release checklist for pending splits.
- **A benchmark with scores.** Keep the result-plus-plot teaser at full width (856px) and add a results table after the procedure; ERNet has none, so right-aligned numeric columns are an extension.
- **A repo without a teaser.** End the header with the two badge rows and let the intro paragraph lead straight into the Release checklist.
- **A finished release.** Drop the unchecked items or remove the checklist rather than leaving an all-checked list.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Split outward links and in-page jumps into two badge rows with `<br>` | Mix eight unrelated badges in one long row |
| Number procedural headings and link to them from the header | Leave a long README without any navigation |
| Pair the qualitative result with the plot that supports it in one teaser | Put the comparison plot in a separate section far below |
| Say in the checklist what is released and what is not | Imply training code exists when only inference is released |
| Bold the model names and keep filenames in inline code in the checkpoint table | Hide checkpoint filenames in prose |
| Say exactly what to include when opening an issue | End with a bare "open an issue" line |
| Keep the label segment on badges that need a category | Use a one-part badge where the message alone is ambiguous |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside `<div align="center">`: a `#` heading with the full paper title, a bold venue line, one line of comma-separated author links, a plain affiliation line, then two rows of flat shields.io badges separated by `<br>`. Row 1: Paper ERNet (message #007ec6), arXiv number (message #b31b1b), one-part Project Page #67ac09, one-part Model Weights #ea7233 linking to `#1-download-the-model-weights`. Row 2: one-part Setup #007ec6, Inference Demo #800080, Citation #555555, and License CC BY-NC 4.0 (message #939393). Two-part badges keep label grey #555555."
2. "After the div, write a three-sentence intro with the full paper name in bold, then a full-width teaser `![alt](assets/teaser.png)` that pairs a qualitative render with a speed/accuracy plot. Add `## Release checklist` as a `- [x]` / `- [ ]` task list and one sentence on what comes next."
3. "Write the procedure as numbered `##` headings: `1. Download the model weights` with a four-column table (Model in bold, When to use it, filename in inline code, Google Drive link) and a `text` tree; `2. Set up the environment` with a `bash` block; `3. Run inference` with `###` cases, `bash` commands with `#` comments and a two-column Option | Purpose table. End with Acknowledgements, Issues, Citation (one sentence and `bibtex`) and License."

## Similar Pages

- readme-nepfaff-scenesmith: a centred header with a row of flat two-part badges (arXiv, Project, Video, License) in HTML `<a><img>` form.
- readme-sisyphm-studiorecon: the same `<div align="center">` around a Markdown `#` title, bold venue, author line and flat badges, but with one badge row.
- readme-itsmag11-omegance: a Markdown `#` title wrapping to two lines in a centred div with a bold venue line and one flat badge row.

## Quick Start

````markdown
<div align="center">

# ProjectName: Full Paper Title

**Venue Year**

[Author One](https://example.org/),
[Author Two](https://example.org/),
[Author Three](https://example.org/)

University

<a href="https://arxiv.org/pdf/XXXX.XXXXX"><img src="https://img.shields.io/badge/Paper-Name-blue" alt="Paper PDF"></a>
<a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b" alt="arXiv"></a>
<a href="https://example.org/project/"><img src="https://img.shields.io/badge/Project_Page-green" alt="Project Page"></a>
<a href="#1-download-the-model-weights"><img src="https://img.shields.io/badge/Model_Weights-orange" alt="Model Weights"></a>
<br>
<a href="#2-set-up-the-environment"><img src="https://img.shields.io/badge/Setup-blue" alt="Setup"></a>
<a href="#3-run-inference"><img src="https://img.shields.io/badge/Inference_Demo-purple" alt="Inference Demo"></a>
<a href="#citation"><img src="https://img.shields.io/badge/Citation-gray" alt="Citation"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey" alt="License: CC BY-NC 4.0"></a>

</div>

Official inference implementation of **ProjectName: Full Paper Title (Venue Year)**.
One sentence on what it does. One sentence on what this repository provides.

![Result render and speed/accuracy plot](assets/teaser.png)

## Release checklist

- [x] Release inference code.
- [x] Release pretrained checkpoints.
- [ ] Release the training code.

## 1. Download the model weights

| Model | When to use it | Checkpoint filename | Download |
| --- | --- | --- | --- |
| **A** | Input type for which this model fits. | `model_a.pth` | [Google Drive](https://drive.google.com/) |

```text
model/
└── model_a.pth
```

## 2. Set up the environment

```bash
git clone https://github.com/org/name.git
cd name
bash setup.sh
```

## 3. Run inference

### Included examples

```bash
# Case one → model A
python main.py assets/example_a
```

### Useful options

| Option | Purpose |
| --- | --- |
| `--flag` | What it does. |

## Acknowledgements

## Issues

## Citation

If you use ProjectName in your research, please cite our paper:

```bibtex
@inproceedings{key,
  title = {...},
}
```

## License
````

## Provenance

- Repo: https://github.com/guangzhaohe/ERNet (`README.md`, branch `main`, last README commit c913da1 on 2026-09-12).
- Paper: "ERNet: Efficient Non-Rigid Registration Network for Point Sequences", ICCV 2025, arXiv 2510.15800; first author Guangzhao He. Project page https://www.guangzhaohe.com/ernet/.
- Selection: two badge rows split paper links from in-page navigation, the teaser pairs a qualitative render with a speed/accuracy plot, and the release checklist, checkpoint table and numbered steps make it very easy to use.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the eight badge URLs, `assets/ernet_teaser.png` fetched from the repo for pixel size, background and accent colors.
- Written 2026-10-28.
