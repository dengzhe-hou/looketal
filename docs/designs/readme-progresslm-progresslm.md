# ProgressLM — README Reference

> A conference poster unrolled down the page: a mascot-stamped title, a gold trophy line with the session time, five bold block-letter tabs, then three full-width figures that carry the argument while justified captions fill the gaps.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/ProgressLM/ProgressLM (last commit touching the file 047770c, 2026-05-18; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs, checked against pixels in the capture; image sizes and accent colors come from `docs/imgs/icon.png`, `teaser.png`, `bench_curation.png` and `statistics.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README opens like a presentation slide. A centred h1 starts with a small mascot icon and runs the full paper title over two lines above GitHub's grey rule. A centred h3 with a 🏆 announces "ACL 2026 Oral Presentation & ICLR 2026 Workshop on World Models", and a centred sentence gives the oral session's day, room and time. A centred credit block (seven linked names, an italic equal-contribution note, two affiliations) sits over one row of five tall `for-the-badge` buttons in blue, black, orange, orange and yellow. Then the figures take over: a 3000px teaser rendered across the full 856px column, two justified paragraphs, a benchmark-curation figure at full width, another justified paragraph, an `### Overview of ProgressLM-Dataset` heading and a statistics panel at full width with a justified caption. Only after these three figures does the page turn into a long, plain manual (Installation, Datasets, SFT Training, RL Training, Evaluation, Citation) built from `###` subsections, small reference tables and many `bash` blocks.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116 to 156, two lines): `<h1 align="center"><img src="docs/imgs/icon.png" height="30" />&nbsp;ProgressLM: Towards Progress Reasoning in Vision-Language Models</h1>`. GitHub h1, 2em (32px), weight 600, centred, with the 1px grey rule under it. The 812×851 icon renders at about 29×30 (GitHub adds `max-height: 30px`) and sits on the first line's baseline like a glyph. The title wraps after "Vision-".
2. **Venue line** (y≈223): `<h3 align="center">🏆 ACL 2026 Oral Presentation & ICLR 2026 Workshop on World Models</h3>`. GitHub h3, 1.25em (20px), weight 600, no rule; it is a heading, so it appears in the outline.
3. **Presentation note** (y≈262 to 287, two lines): `<p align="center">We will present it on Tuesday, July 7 at Harbor H-I during Oral Session F: ... 09:00-10:30. Welcome to join us!</p>`. Body size, plain.
4. **Credit block** (y≈326 to 374): one `<p align="center">` holding seven `<a>` names separated by ", " with `*` after the first two, a `<br>`, `<i>(* equal contribution)</i>`, a `<br>`, then `<sup>1</sup>Northwestern University &emsp; <sup>2</sup>University of California, Santa Barbara`. The names carry no affiliation numbers, although the affiliations are numbered.
5. **Badge row** (y≈402 to 430): one `<p align="center">` with five `<a><img src="https://img.shields.io/badge/<emoji>-<Message>-<color>?style=for-the-badge" alt="..." /></a>` lines. Each badge is 28px tall; the row spans about 620px. Details in Badges.
6. **Teaser** (y≈462 to about 881): `<p align="center"><img src="docs/imgs/teaser.png" width="100%" /></p>`. The 3000×1470 PNG renders at 856×419 and ends just above the 900px fold. No caption and no `alt`.
7. **Justified explanation**: two `<p align="justify">` paragraphs with `<b>` and `<i>` emphasis, the second opening with a bold italic research question. They act as the teaser's caption.

## Badges

All five use the static path form `https://img.shields.io/badge/<label>-<message>-<color>?style=for-the-badge`, where the label is a single emoji and the color is a shields.io name. `for-the-badge` renders 28px tall with square corners, no gloss, and the message in bold uppercase Verdana with letter spacing; the emoji label sits on a narrow #555555 cell about 35px wide. Hex values are the fills shields.io serves today for each named color, and they match the capture pixels exactly.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| 🌐 | WEBSITE | `blue` #007ec6 (label #555555) | for-the-badge | progresslm.github.io/ProgressLM/ |
| 📄 | PAPER | `black` #000000 (label #555555) | for-the-badge | arxiv.org/abs/2601.15224 |
| 🤗 | SFT MODEL | `orange` #ea7233 (label #555555) | for-the-badge | huggingface.co/Raymond-Qiancx/ProgressLM-3B-SFT |
| 🤗 | RL MODEL | `orange` #ea7233 (label #555555) | for-the-badge | huggingface.co/Raymond-Qiancx/ProgressLM-3B-RL |
| 🤗 | DATASET | `yellow` #d8b800 (label #555555) | for-the-badge | huggingface.co/datasets/Raymond-Qiancx/ProgressLM-Dataset |

The emoji replaces a text label, so each badge reads as an icon plus one word, which is what makes the row look like a set of uniform buttons. Messages are written in mixed case in the URL (`SFT Model`, with a literal space) and uppercased by the style. Every badge has an `alt` that repeats the message.

Other colors on the first screen come from the teaser: gold #f5c342 for the "Progress Reasoning" frame, orange #e67e48 for the highlighted demo frame No.3 and the "Episodic Retrieval" brace, blue #2f6eba for the "Mental Simulation" brace and highlighted reasoning text, and red #ea3323 for the wrong "About 70%" direct prediction.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | (icon) ProgressLM: Towards Progress Reasoning in Vision-Language Models | full title with a 30px mascot icon |
| h3 (centred) | 🏆 ACL 2026 Oral Presentation & ICLR 2026 Workshop on World Models | venue; the session note, credits, badges, teaser, two justified paragraphs, the curation figure and one more justified paragraph follow without a heading |
| h3 | Overview of ProgressLM-Dataset | the statistics panel at 100% and one justified caption paragraph |
| h2 | Installation | `###` SFT Environment, RL Environment and Evaluation Environment, each a one-line lead with a framework link and a `bash` block |
| h2 | Datasets | `###` prog-bench and human-bench, each a one-line description and a File / Description table with file names in inline code |
| h2 | SFT Training | `###` Configuration Files (table), Running SFT Training, Merge LoRA Weights, Scaling more CoT Data? (two bold "Step" lines with `bash` blocks) |
| h2 | RL Training (GRPO) | `###` Configuration Files (table) and Running RL Training |
| h2 | Evaluation | `###` Supported Models (Model / Directory / Description table), Benchmark Scripts (table), Running Evaluation (four `####` cases), Manual Evaluation Command, Evaluation Metrics (table with bold abbreviations), Other Model Evaluation (three `####` cases) |
| h2 | Citation | one sentence and a `bibtex` block |

Absent from the source: news or changelog, results or leaderboard table, GIF or embedded video, license section, acknowledgements, contact section, table of contents, figure captions under the teaser and curation figure.

Present but unusual: the first heading after the h1 is an `<h3>`, and a second `###` (dataset overview) also comes before any `##`, so the outline starts with three non-`##` entries; the body uses `<p align="justify">`, which GitHub keeps and renders as justified text; a session time and room are written into the README header; the authors line uses `*` marks but no affiliation superscripts; the h1 carries an inline icon image.

## Components

**Inline-icon title.** `<img src="..." height="30" />&nbsp;` as the first child of `<h1 align="center">`. A square icon at the h1's cap height reads as a mascot glyph, not a logo banner.

**Trophy venue heading.** `<h3 align="center">🏆 Venue Oral Presentation & Workshop</h3>`, followed by a centred plain-text paragraph with the session day, room and time.

**Credit block.** One `<p align="center">` with names as `<a>` links separated by ", ", `*` marks after equal-contribution authors, then `<br>` lines for `<i>(* equal contribution)</i>` and the affiliations separated by `&emsp;`.

**Button badges.** Five `for-the-badge` shields with emoji labels on #555555 and messages #007ec6, #000000, #ea7233, #ea7233 and #d8b800, one per source line inside `<p align="center">`. Model and dataset badges share the 🤗 label and are told apart by color (orange for models, yellow for the dataset).

**Figure plus justified text.** `<p align="center"><img src="..." width="100%" /></p>` followed by one or two `<p align="justify">` paragraphs with `<b>` for the key terms and `<b><i>` for a research question. Used three times in a row.

**Reference tables.** Pipe tables with `|------|-------------|` delimiters and no alignment colons; GitHub centres header cells and left-aligns body cells. File and script names sit in inline code; the metrics table bolds each abbreviation (`**NSE** (Normalized Score Error)`). No numeric results.

**Command blocks.** `bash` fences with `#` comment lines naming each variant ("# Qwen2.5-VL-3B (Single GPU)"), a leading `cd` into the working directory, and long commands broken with trailing backslashes, one environment variable per line.

**Citation.** "If you find this work useful, please cite our paper:" then an `@article{zhang2026progresslm, ...}` block that still lists the arXiv preprint as the journal.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| icon.png | PNG mascot, transparent background | 812×851 | `<img ... height="30" />` inside the h1 | about 29×30 | start of the title |
| teaser.png | PNG task figure, opaque white | 3000×1470 | `<img ... width="100%" />` in `<p align="center">` | 856×419 | directly after the badge row |
| bench_curation.png | PNG data-construction figure, opaque white | 2000×986 | `<img ... width="100%" />` in `<p align="center">` | 856×422 | after the two justified paragraphs |
| statistics.png | PNG statistics panel, opaque white | 2000×639 | `<img ... width="100%" />` in `<p align="center">` | 856×273 | under `### Overview of ProgressLM-Dataset` |

The teaser is two rounded panels drawn like a worked example: "First see how the task is being done:" over six robot-arm frames labelled No.1 to No.6 and 0% to 100%, then "Then, tell me how much of this task has been completed so far?" with an observation photo, a grey "Direct Prediction" box ending in a red "About 70%", and a gold-framed "Progress Reasoning" box with `<ref_think>` and `<score_think>` text, orange and blue braces for "Episodic Retrieval" and "Mental Simulation", and a green "46%" score. Titles are large bold sans-serif, so they read at body size even at 856px. The curation figure has three labelled sub-panels ((a) Demonstration Setup in a gold frame, (b) Observation Sampling in purple, (c) Answerability Augmentation in blue). The statistics panel combines three sunburst charts (Bench, SFT, RL), a legend, a grid of robot photos and a word cloud. All three figures are opaque white PNGs with no `<picture>` dark variant, so the page is designed for the light theme. There is no GIF or video.

## Adapting to Other Content

- **A figure-heavy paper repo.** Keep this order exactly: icon title, trophy h3, credits, button badges, then each figure at `width="100%"` (856px) followed by a justified paragraph. Export figures at 2000 to 3000px wide so they stay sharp at 856px on high-density screens.
- **A paper without an oral slot.** Drop the session-time paragraph and keep the h3 for the venue alone ("🏆" only for awards or orals).
- **A library.** Drop the credit block and the session note, keep the icon title and the badge row with Docs / PyPI / License messages in the same `for-the-badge` emoji form, and replace the three figures with one architecture figure and a Quickstart.
- **A dataset.** Lead with the statistics panel (it renders 856×273, short enough to sit in the first screen with the teaser), make the 🤗 DATASET badge first, and promote the File / Description tables to the first `##`.
- **A benchmark with scores.** Add a results table after the statistics panel with numeric columns right-aligned (`|------:|`) and the best value in bold; ProgressLM's README has none.
- **A repo with only one figure.** Keep the teaser and the two justified paragraphs, and use `##` for the dataset overview so the outline does not start with stray `###` entries.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Give every figure `width="100%"` and a source at least 2000px wide | Mix figure widths or upscale small images |
| Keep all five badges in one style (`for-the-badge`, emoji label, #555555) | Mix flat and `for-the-badge` badges in one row |
| Tell same-label badges apart by color and message (orange models, yellow dataset) | Use five different colors with no grouping |
| Follow each figure with a short paragraph that explains it | Stack three large figures with no text between them |
| Put affiliation numbers on author names when affiliations are numbered | Number affiliations but leave the names unmarked |
| Use `##` for top-level sections from the first one on | Start the outline with several `###` headings before any `##` |
| Remove the session-time line once the conference is over, or move it into a News list | Leave a dated room and time in the header indefinitely |

## Agent Prompt Guide

1. "Write a README header in GitHub HTML: `<h1 align="center">` with a 30px-high icon `<img height="30" />&nbsp;` before the full paper title, an `<h3 align="center">` '🏆 Venue Oral Presentation', a centred paragraph with the session time, and one `<p align="center">` credit block with linked names, `*` equal-contribution marks, an italic note and `&emsp;`-separated affiliations."
2. "Add one centred row of five shields.io badges with `?style=for-the-badge` and an emoji as the label (label #555555): 🌐 Website #007ec6, 📄 Paper #000000, 🤗 SFT Model #ea7233, 🤗 RL Model #ea7233, 🤗 Dataset #d8b800, each with an `alt` equal to its message."
3. "After the badges, place three figures, each as `<p align="center"><img src="..." width="100%" /></p>` (856px at a 920px column), each followed by one or two `<p align="justify">` paragraphs with `<b>` key terms. Then write `## Installation`, `## Datasets`, `## SFT Training`, `## RL Training (GRPO)`, `## Evaluation` and `## Citation`, using `###` subsections, File / Description tables with names in inline code, and `bash` blocks with `#` comment labels."

## Similar Pages

- readme-donaldssh-k-merge: also an ACL 2026 oral, but restrained: a Markdown-in-div header, flat badges and one compact 660px diagram where ProgressLM uses tall button badges and three full-width figures.
- readme-deepmancer-hairport: another header built on a row of `for-the-badge` shields under a centred title, with a bold venue line inside a centred paragraph.
- readme-chuan-10-agile: a centred title and `###` subtitle over a row of `for-the-badge` buttons (Project Page, arXiv, Paper, Hugging Face Data), the same button-row idea with text labels instead of emoji.
- readme-shjo-april-trace: block-letter `for-the-badge` badges under a centred title, followed by numbers rather than figures.

## Quick Start

````markdown
<h1 align="center">
  <img src="docs/imgs/icon.png" height="30" />&nbsp;ProjectName: Full Paper Title
</h1>

<h3 align="center">
  🏆 Venue Year Oral Presentation
</h3>

<p align="center">
  We will present it on Day, Month DD at Room during Session X, HH:MM-HH:MM. Welcome to join us!
</p>

<p align="center">
  <a href="https://example.org/">Author One</a>*, <a href="https://example.org/">Author Two</a>*, <a href="https://example.org/">Author Three</a>
  <br>
  <i>(* equal contribution)</i>
  <br>
  <sup>1</sup>Institution A &emsp; <sup>2</sup>Institution B
</p>

<p align="center">
  <a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/🌐-Website-blue?style=for-the-badge" alt="Website" /></a>
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/📄-Paper-black?style=for-the-badge" alt="Paper" /></a>
  <a href="https://huggingface.co/org/model-sft"><img src="https://img.shields.io/badge/🤗-SFT Model-orange?style=for-the-badge" alt="SFT Model" /></a>
  <a href="https://huggingface.co/org/model-rl"><img src="https://img.shields.io/badge/🤗-RL Model-orange?style=for-the-badge" alt="RL Model" /></a>
  <a href="https://huggingface.co/datasets/org/data"><img src="https://img.shields.io/badge/🤗-Dataset-yellow?style=for-the-badge" alt="Dataset" /></a>
</p>

<p align="center">
  <img src="docs/imgs/teaser.png" width="100%" />
</p>

<p align="justify">
Task definition with the <b>key idea</b> in bold.
</p>

<p align="center">
  <img src="docs/imgs/bench_curation.png" width="100%" />
</p>

<p align="justify">
How the data were built, with <b>(i) dimension one</b> and <b>(ii) dimension two</b>.
</p>

### Overview of ProjectName-Dataset

<p align="center">
  <img src="docs/imgs/statistics.png" width="100%" />
</p>

## Installation

### SFT Environment

```bash
conda create -n env python=3.11 -y
conda activate env
pip install -e .
```

## Datasets

| File | Description |
|------|-------------|
| `split.jsonl` | What it holds |

## Training

## Evaluation

| Metric | Description |
|--------|-------------|
| **ABC** (Full Name) | What it measures |

## Citation

If you find this work useful, please cite our paper:

```bibtex
@article{key2026,
  title={...},
}
```
````

## Provenance

- Repo: https://github.com/ProgressLM/ProgressLM (`README.md`, branch `main`, last README commit 047770c on 2026-05-18).
- Paper: "PROGRESSLM: Towards Progress Reasoning in Vision-Language Models", ACL 2026 (oral, per the README) and ICLR 2026 Workshop on World Models, arXiv 2601.15224; first author Jianshu Zhang. Project page https://progresslm.github.io/ProgressLM/.
- Selection: a presentation banner line and uniform button-style link badges sit over large, high-resolution explanatory figures and a dataset statistics panel, showing how to lead with figures for a figure-heavy paper.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for each badge URL with capture pixels as a check, and the four PNGs fetched from the repo for pixel sizes, transparency and accent colors.
- Written 2026-10-28.
