# SceneSmith — README Reference

> An architect's cutaway pinned to the top of an operations manual: one large annotated floor plan with a long italic caption, then fifty-odd shell blocks of exact instructions.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/nepfaff/scenesmith (last commit touching the file 9df3f88, 2026-02-11; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; the logo's colors come from `media/symbol.svg`, and image sizes and accent colors from `media/teaser.webp` and `media/robot_eval.webp`, all fetched from the repo. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them. Rendered y values below are in the 1440×900 frame.

## Overview

The first screen is almost all picture. A centred `<h1>` pairs a small triangular logo with the word "SceneSmith", followed by a one-line "Code for ..." paragraph, a row of four small flat badges, a two-line author and affiliation block, and then the teaser at `width="100%"`: an annotated top-down render of a whole community center, ringed by circular close-ups and connected to them by dashed cyan arrows, with serif call-out text inside the image ("Objects are separable", "Articulated objects with objects placed inside"). Below the fold a bold-then-italic caption of about 80 words explains the figure. The citation comes immediately after, as the first `##` section, ahead of a nested table of contents. The rest of the README is an operations manual: eight emoji `##` sections (📦 Installation, 🐳 Docker, 💾 Data Setup, 🎬 Scene Generation, 🔍 Visualization, 📤 Export, 🤖 Robot Evaluation, 🧪 Testing) plus 📄 License, each preceded by a `---` rule, with 51 `sh` blocks, five `yaml` blocks, one `python` block, numbered bold-step lists and three `> **Important:**` or `> **Note:**` callouts. There is no results table and no news list; the second figure, a robot-evaluation pipeline with its own long caption, sits deep in the page.

## Header Block

1. **Title with logo** (y≈116): `<h1 align="center">` containing `<img src="media/symbol.svg" alt="" height="36" align="absmiddle">&nbsp;SceneSmith`. GitHub h1, 2em (32px), weight 600. The logo is a 90.07×78 viewBox SVG drawn at 36px tall (about 42px wide), vertically centred on the text by `align="absmiddle"`. GitHub's grey rule runs under the h1 across the 856px content width (y≈148).
2. **Subtitle line** (y≈176): `<p align="center">Code for "SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes".</p>`. Body size, plain text, quotation marks included; the paper title is not a heading and not bold.
3. **Badge row** (y≈214): `<p align="center">` holding four `<a><img src="https://img.shields.io/badge/...svg" alt="..."></a>` lines. Flat style, 20px tall; widths 116, 102, 102 and 82px, so the row spans about 414px. Details in Badges.
4. **Authors and affiliations** (y≈258 and 282): one `<p align="center">` with five `<a>` names, each followed by `<sup>1</sup>` or `<sup>2</sup>` and a comma, one per source line; `<br/>` after the last name, then `<sup>1</sup>Massachusetts Institute of Technology,` and `<sup>2</sup>Toyota Research Institute` on the second rendered line. Names are GitHub link blue; one links to LinkedIn. No equal-contribution or corresponding-author marks.
5. **Teaser** (y≈306 to about 862): `<p align="center"><img src="media/teaser.webp" alt="SceneSmith teaser" width="100%"></p>`. The 1946×1265 WebP renders 856×556 and fills the rest of the first screen.
6. **Caption** (below the fold): `<p align="center"><em><b>Fully automated text-to-scene generation.</b> This entire community center was generated ... (robots added for demonstration).</em></p>`. A bold italic lead sentence, then four italic sentences, all centred, so the caption sets as a ragged centred block five lines deep.
7. **Citation** (directly after): `## Citation` with a `bibtex` block (`@misc{scenesmith2026, ...}` with `eprint`, `archivePrefix`, `primaryClass` and `url`). Putting it before the table of contents is a deliberate early position. This ends the header block.

## Badges

All four use the static form `https://img.shields.io/badge/<label>-<message>-<color>.svg` with no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 and white (#ffffff) text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2602.09153 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2602.09153 |
| Project | Website | `green`, rendered #67ac09 (label #555555) | flat (default) | scenesmith.github.io |
| Video | Overview | `red`, rendered #dd4343 (label #555555) | flat (default) | youtu.be/V5Sg2NPqJb8 |
| License | MIT | `blue`, rendered #007ec6 (label #555555) | flat (default) | LICENSE (relative) |

The three named colors are given as the hex values in the SVGs shields.io returned on 2026-10-28; `green` and `red` came back as #67ac09 and #dd4343 rather than the older #97ca00 and #e05d44. Each `alt` names the destination ("arXiv", "Project Website", "Video", "License"). There is no link row of bold text links, and the video is reached only through its badge.

Colors outside the badges: the logo `media/symbol.svg` uses #231f20 outlines and text with three face fills: #68c0a4 (teal) on the left face, #8ca0cc (periwinkle) on the right face and #f9a87e (peach) on the bottom face. The teaser's dashed arrows and close-up rings are cyan #42c8f4 with small orange #f89a1c accents; the robot-evaluation figure uses cyan #12b7d4 and orange #db692b in the same roles.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | (logo) SceneSmith | title; subtitle line, badges, authors and affiliations, teaser and caption follow without a heading |
| h2 | Citation | one `bibtex` block, no lead sentence |
| h2 | Table of Contents | nested bullet list of anchor links, eight top-level entries with up to five children; then `---` |
| h2 | 📦 Installation | lead blockquote pointing to Docker; h3 Local Install (uv, five one-command `sh` blocks), h3 Multi-GPU Rendering Support (Optional), h3 Asset Generation Backends with h4 Hunyuan3D-2 Backend and h4 SAM3D Backend as numbered bold steps, h3 Environment Variables; one `> **Important:**` callout with a numbered link list |
| h2 | 🐳 Docker | h3 Prerequisites, Build, Data Preparation, SAM3D Checkpoints, Run, Volume Mounts (a three-column path table), and a second `> **Important:**` callout |
| h2 | 💾 Data Setup | a numbered list of the three default dependencies, then h3 HSSD Dataset Setup, Objaverse (ObjectThor) Setup, Articulated Object Datasets (h4 PartNet-Mobility Setup, ArtVIP Setup, Test Retrieval, Enable Articulated Retrieval), AmbientCG PBR Materials |
| h2 | 🎬 Scene Generation | one-line `sh` run command, config notes, GPU memory note; h3 Multi-GPU Support, Pipeline Stage Control (numbered five-stage list and h4 per usage), Branching from a Previous Experiment |
| h2 | 🔍 Visualization | h3 Intermediate Scenes, Portable House Scenes, with `sh` and `python` blocks |
| h2 | 📤 Export | h3 Export to MuJoCo and USD and a `> **Note:**` callout |
| h2 | 🤖 Robot Evaluation | one paragraph, the full-width pipeline figure with a bold-italic caption, h3 Pipeline Stages and h3 Stage 1 to Stage 4 |
| h2 | 🧪 Testing | three labelled `sh` blocks (unit, integration, all) and two notes |
| h2 | 📄 License | one sentence linking `LICENSE` |

Absent from the source: news or changelog, results or leaderboard table, model zoo, embedded GIF or video, `<details>` blocks, acknowledgements, contact section, venue line in the header (the ICML 2026 Spotlight acceptance is not mentioned anywhere in the README), equal-contribution marks.

Present but unusual: the citation is the first `##` section, before the table of contents; the table of contents lists "Docker" as a child of Installation although 🐳 Docker is its own `##` section; emoji headings produce anchors with a leading hyphen (`#-installation`, `#-docker`), which the table of contents uses correctly; every emoji `##` section is preceded by a `---` rule, so GitHub draws a 4px rule above each heading on top of the heading's own 1px bottom rule; the logo has an empty `alt`.

## Components

**Logo-in-heading.** `<h1 align="center"><img src="..." alt="" height="36" align="absmiddle">&nbsp;Name</h1>`: an SVG mark at 36px height sitting on the h1 text line, separated by one non-breaking space.

**Flat badge row.** Four `<a href="..."><img src="https://img.shields.io/badge/Label-Message-color.svg" alt="..."></a>` lines in a `<p align="center">`. Label #555555; messages #b31b1b, #67ac09, #dd4343, #007ec6. Label is the kind of resource (arXiv, Project, Video, License), message the specific item.

**Captioned figure.** `<p align="center"><img ... width="100%"></p>` followed by `<p align="center"><em><b>Bold title sentence.</b> Several explanatory sentences.</em></p>`. The caption is long and centred; the bold sentence acts as the figure title. Used twice, for the teaser and for the robot-evaluation figure.

**Nested table of contents.** A Markdown bullet list with two-space-indented children, each entry an anchor link (`[Local Install](#local-install)`). Top-level entries drop the emoji but link to the emoji anchors.

**Section dividers.** `---` on its own line before each emoji `##` heading.

**Numbered bold steps.** `1. **Install submodules**:` then a three-space-indented `sh` or `yaml` block, so the code sits inside the list item. Sizes and wait times appear in parentheses in the step title ("(~72GB, requires Git LFS)").

**Callouts.** Plain GitHub blockquotes, not alert syntax: `> **Important:** ...` and `> **Note:** ...`, sometimes followed by a numbered list of anchor links inside the quote. A short unbolded `>` line opens Installation.

**Code blocks.** Fenced with `sh` (51 blocks), `yaml` (5), `python` (1) and `bibtex` (1). Many are a single command introduced by a one-line sentence ending in a colon ("Install uv:"). Shell blocks carry `#` comment lines for alternatives ("# Force single GPU mode").

**Path table.** One three-column pipe table (Host Path, Container Path, Content) with plain `|-----|` delimiters and inline code in the first two columns.

**License line.** One sentence, "This project is licensed under the MIT License - see [LICENSE](LICENSE) for details."; no acknowledgements.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| media/symbol.svg | SVG logo, triangle with teal, periwinkle and peach faces and dark outlines | viewBox 90.07×78 | `<img ... height="36" align="absmiddle">` inside the h1 | about 42×36 | left of the title text |
| media/teaser.webp | static WebP, annotated 3D render on white | 1946×1265 | `<img ... width="100%">` in `<p align="center">` | 856×556 | header, after the authors; bold-italic centred caption below |
| media/robot_eval.webp | static WebP, pipeline figure on white | 2917×1565 | same pattern, `width="100%"` | 856×459 | top of 🤖 Robot Evaluation, after one paragraph; bold-italic centred caption below |

The teaser is a single rendered scene used as an explainer: a top-down cutaway of every room, with circular insets ringed in cyan #42c8f4, dashed cyan arrows to separate object crops, and serif call-outs that quote the prompt ("The storage room has shelves with boxes."). The robot-evaluation figure follows the same visual language with cyan #12b7d4 and orange #db692b. Both are single-frame WebPs, neither uses `<picture>` or a dark-theme variant, and the overview video is a YouTube badge link rather than an embed.

## Adapting to Other Content

- **A library.** Keep the logo-in-h1 and the one-line "Code for ..." paragraph (rewritten as "A library for ..."), the four flat badges (Docs, PyPI, Video, License) and the nested table of contents; replace the teaser with a short usage example and drop the author block.
- **A dataset.** Make the teaser a single annotated sample at `width="100%"` (856px) with a bold-italic caption that states counts, and promote 💾 Data Setup to the first section after the table of contents.
- **A benchmark with scores.** Add a `## 📊 Results` section after Scene Generation with a pipe table, right-aligned numeric columns (`---:`) and bold best values; SceneSmith itself has no results table.
- **A repo without a teaser.** Let the badge row and author block close the header and move the citation directly under them, as SceneSmith already does.
- **A short README.** Drop the table of contents and the `---` dividers; both pay off only when there are eight or more long `##` sections.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Let one annotated full-width figure explain the contribution | Stack several small teaser images in the header |
| Caption the figure with a bold title sentence followed by italic explanation | Leave a dense figure with no caption |
| Put the citation right after the header in a long README | Bury BibTeX after eight operational sections |
| Use a nested table of contents when the README has eight or more `##` sections | Repeat the table of contents in every section |
| Write install steps as numbered bold titles with indented `sh` blocks | Run multi-step installs as one long unexplained shell block |
| Flag incomplete setup with `> **Important:**` and anchor links to the missing steps | Hide required downloads in prose |
| Keep the badge row to four flat badges with the #555555 label | Add the venue or star counts as extra badges without need |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown: `<h1 align="center">` with an SVG logo at `height="36" align="absmiddle"`, `&nbsp;` and the project name; a centred `<p>` reading `Code for "Full Paper Title".`; a centred row of four flat shields.io badges (label #555555; arXiv ID #b31b1b, Project Website green #67ac09, Video Overview red #dd4343, License MIT blue #007ec6); a centred author paragraph with `<sup>` marks, `<br/>`, then the affiliations; a `width="100%"` teaser; and a centred `<em>` caption that opens with a `<b>` title sentence."
2. "After the header, put `## Citation` with a `bibtex` block, then `## Table of Contents` as a nested bullet list of anchor links, then `---`. Write the body as emoji `##` sections, each preceded by `---`: 📦 Installation, 🐳 Docker, 💾 Data Setup, 🎬 Scene Generation, 🔍 Visualization, 📤 Export, 🤖 Robot Evaluation, 🧪 Testing, 📄 License."
3. "Inside each section use h3 and h4 subsections, numbered steps with a bold title and an indented `sh` or `yaml` block, `> **Important:**` callouts that list missing steps as anchor links, and one three-column path table. Place any second figure at `width="100%"` with the same bold-italic centred caption form."

## Similar Pages

- readme-leggedrobotics-d3-skill-discovery, readme-microsoft-renderformer and readme-seohongpark-ogbench also combine a table of contents with `<details>` blocks for long operational content; SceneSmith uses a table of contents and `---` dividers but no `<details>`.
- readme-letianhuang-transparentgs and readme-yrainy0615-gaussianplant are other 3D-vision READMEs in the set with collapsible sections, for comparison with SceneSmith's fully expanded layout.
- SceneSmith's distinguishing choices are a single annotated teaser with a long bold-italic caption and the citation placed before the table of contents. Its project page (scenesmith.github.io) is a separate web page and is not described here.

## Quick Start

````markdown
<h1 align="center">
  <img src="media/symbol.svg" alt="" height="36" align="absmiddle">&nbsp;ProjectName
</h1>

<p align="center">
Code for "ProjectName: Full Paper Title".
</p>

<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg" alt="arXiv"></a>
  <a href="https://example.github.io/"><img src="https://img.shields.io/badge/Project-Website-green.svg" alt="Project Website"></a>
  <a href="https://youtu.be/XXXX"><img src="https://img.shields.io/badge/Video-Overview-red.svg" alt="Video"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
</p>

<p align="center">
<a href="https://example.org/">Author One</a><sup>1</sup>,
<a href="https://example.org/">Author Two</a><sup>2</sup> <br/>
<sup>1</sup>Institution A,
<sup>2</sup>Institution B
</p>

<p align="center">
  <img src="media/teaser.webp" alt="ProjectName teaser" width="100%">
</p>

<p align="center"><em>
<b>Bold figure title.</b> Several sentences explaining what the figure shows.
</em></p>

## Citation

```bibtex
@misc{key2026,
  title={...},
}
```

## Table of Contents

- [Installation](#-installation)
  - [Local Install](#local-install)
- [Data Setup](#-data-setup)
- [License](#-license)

---

## 📦 Installation

> For Docker-based setup, see [Docker](#-docker) below.

### Local Install

Install the dependencies:
```sh
uv sync
```

1. **Step title** (~size):
   ```sh
   bash scripts/install.sh
   ```

> **Important:** Installation is not complete yet. Continue with:
> 1. [Data Setup](#-data-setup)

---

## 🐳 Docker

---

## 💾 Data Setup

---

## 🎬 Scene Generation

```sh
python main.py +name=run_name
```

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
````

## Provenance

- Repo: https://github.com/nepfaff/scenesmith (`README.md`, branch `main`, last README commit 9df3f88 on 2026-02-11).
- Paper: "SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes", ICML 2026 Spotlight, arXiv 2602.09153; first author Nicholas Pfaff. Project page https://scenesmith.github.io/.
- Selection: one large annotated hero figure with a long italic caption does all the explaining, and the citation placed early plus a nested table of contents suit a long, operations-heavy README.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `media/symbol.svg`, `media/teaser.webp` and `media/robot_eval.webp` fetched from the repo for sizes and colors.
- Written 2026-10-28.
