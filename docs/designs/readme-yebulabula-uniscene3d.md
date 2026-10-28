# UniScene3D — README Reference

> A storybook crest over a lecture handout: a pale-blue cityscape logo, a big two-line title, four logo-capped tags, and one figure that reads left to right from images and pointmaps to a radar of wins.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/Yebulabula/UniScene3D (last commit touching the file 8a1e748, 2026-07-03; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for each badge URL; image sizes and transparency come from the PNG headers and pixel data of `paper_logo.png` and `figure1.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

Everything above the abstract sits in one `<div align="center">`. A transparent illustrated logo (a light-blue line-art city, planet and moon above the word "UniScene3D", 257px wide) opens the page, followed by the full paper title as a two-line `<h1>` with GitHub's rule, a plain venue line, five comma-separated author links, a bold affiliation, and a row of four flat badges that each carry a brand logo (arXiv, Chrome, Hugging Face twice). A two-part teaser fills the rest of the screen: a clean pipeline on top (Images and Pointmaps flowing into a pale teal "UniScene3D" box, then out to a list of four tasks) and a qualitative strip below with two 3D scene renders under quoted referring expressions and a radar chart against SOTA. After the div, an italic one-paragraph abstract with bold-italic key phrase leads into a linked Contents list, a two-item News list with rocket emoji and inline-code dates, and a "Key Takeaways" section of five bullets, each opening with a bold label (Core Question, Preliminary Finding, Model Contribution, Key Training Idea, Result). The rest is a practical how-to in plain `##` sections with short `bash` blocks.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Logo** (y≈96–265): `<p><img src="assets/paper_logo.png" alt="UniScene3D logo" width="30%"></p>`. The 805×531 PNG has a transparent background; `width="30%"` of the 856px column gives 257×169.
2. **Title** (y≈314–354, two lines): `<h1>RGB-Pointmap Pretraining for Unified 3D Scene Understanding</h1>`, centred by the div. GitHub h1, 2em (32px), weight 600; the title wraps after "Scene", and the 1px grey rule sits under the second line.
3. **Venue line** (y≈412): `European Conference on Computer Vision (ECCV) 2026` as bare text directly after `</h1>`, not wrapped in any tag, so it renders as a plain line with no paragraph margin of its own.
4. **Authors** (y≈436): `<p>` with five `<a>` names separated by commas and source newlines, one line at this width. No superscripts (a single affiliation).
5. **Affiliation** (y≈476): `<p><strong>Imperial College London</strong></p>`.
6. **Badge row** (y≈507–527): `<p align="center">` with four `<a>` blocks, each holding one `<img ... align="absmiddle">`. About 520px wide. Details in Badges.
7. **Teaser** (y≈546 to about 1016, crossing the fold): `<p><img src="assets/figure1.png" alt="UniScene3D teaser figure" width="100%"></p>`. The 1591×873 PNG renders 856×470. `</div>` follows.
8. **Abstract**: one left-aligned paragraph wrapped in `*...*`, with `***multi-view RGB-Pointmap***` in bold italic. It acts as the teaser's caption and ends the header block.

## Badges

All four use the static path form `https://img.shields.io/badge/<label>-<message>-<hex>` with `logo=` and `logoColor=`, no `style=`, so they render in the default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, a 14px logo at the left of the label, label on #555555. Message text is white (#ffffff) except on the yellow Model badge, where shields.io switches to #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | UniScene3D | #b31b1b (label #555555) | flat, `logo=arxiv&logoColor=white` | arxiv.org/abs/2604.02546 |
| Project | Page | #111827 (label #555555) | flat, `logo=googlechrome&logoColor=white` | yebulabula.github.io/UniScene3D/ |
| Model | Hugging Face | #f6c343 (label #555555, message text #333333) | flat, `logo=huggingface&logoColor=yellow` | huggingface.co/MatchLab/UniScene3D |
| Data | ScenePoint | #4dabf7 (label #555555) | flat, `logo=huggingface&logoColor=yellow` | huggingface.co/datasets/MatchLab/ScenePoint |

Rendered widths are 133, 103, 145 and 125px. Each `<img>` has `alt` ("arXiv", "Project Page", "Model", "Data") and `align="absmiddle"`, which GitHub keeps. The arXiv message is the project name rather than the paper number, and the near-black #111827 Project badge reads almost as a solid dark tag. In the Windows capture the arXiv logo renders as a small chevron-like mark.

Other colored marks visible on the page: the logo's line art is light blue (its most frequent saturated pixels are around #59b2f4), and the teaser's central "UniScene3D" box is pale teal #daecec with grey arrows and black labels. The teaser's 3D renders, camera icons and radar fills keep their own colors and were not measured.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | RGB-Pointmap Pretraining for Unified 3D Scene Understanding | title; venue, authors, affiliation, badges, teaser and the italic abstract follow without a heading |
| h2 | Contents | ten bullet links to the sections below |
| h2 | News | two bullets `- 🚀 \`YYYY-MM-DD\`: ...`, newest first |
| h2 | Key Takeaways | five bullets, each `**Label**: sentence`, the core question's last sentence also in bold |
| h2 | Expected Repository Structure | one commented `text` tree |
| h2 | Installation | three numbered h3 steps (create environment, install PyTorch with pinned versions in inline code, install the rest), each with a `bash` block |
| h2 | Data Preparation | paragraphs with a Hugging Face link, a bullet list of folders in inline code, a note on source datasets |
| h2 | Pretraining | one config link and a one-line `bash` block |
| h2 | Evaluation | a download note, then h3 Viewpoint Grounding, Scene Retrieval, Scene Type Classification (zero-shot and few-shot) and 3D VQA Fine-Tuning, each with a short `bash` block; a bullet list of environment variables |
| h2 | Acknowledgements | one paragraph with three project links |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | License | one sentence linking LICENSE |

Absent from the source: a results table in Markdown (results appear only in the teaser's radar), a model zoo table, a demo GIF or video, a TODO list, a contact section, emoji in headings, `<details>` blocks.

Present but unusual: the venue line is untagged text inside the centred div; the paper title, not the project name, is the h1 (the name lives in the logo); the abstract sits outside the div in italics, acting as a caption; a "Key Takeaways" section explains the paper in bolded lead-in bullets before any how-to; the News line "See you in Sweden 🇸🇪!" shows the flag as the letters "SE" on Windows; the BibTeX `booktitle` is `{arxiv}` although the header names ECCV 2026.

## Components

**Centred HTML header.** `<div align="center">` with a blank line after it, then `<p>` blocks for logo, authors, affiliation, badges and teaser, an `<h1>` for the title and one untagged venue line. Elements are separated by blank lines.

**Logo badge row.** Four flat badges, label #555555, messages #b31b1b, #111827, #f6c343, #4dabf7, every one with a 14px logo; links are the destination, the message is the thing (project name, Hugging Face, dataset name).

**Italic abstract.** A paragraph wrapped in single asterisks, with the core phrase in triple asterisks for bold italic, placed directly after the centred block.

**Contents list.** `## Contents` with `- [Section](#anchor)` bullets in page order, ten entries.

**News list.** `- 🚀 \`2026-06-20\`: Sentence.` with an ISO date in inline code, two entries, newest first.

**Key Takeaways.** Five bullets separated by blank lines (so GitHub renders them as loose list items with paragraph spacing), each starting `- **Label**:`. The labels follow the argument of the paper: question, preliminary finding, contribution, training idea, result.

**Numbered h3 steps.** Installation uses `### 1. Create an environment`, `### 2. Install PyTorch`, `### 3. Install the remaining dependencies`, each followed by a one- or two-line `bash` block.

**Code blocks.** `text` for the commented repository tree, `bash` for every command, `bibtex` for the citation; all short.

**Citation, acknowledgements and license.** "If you find this repository useful, please cite the paper:" then `@inproceedings{mao2026uniscene3d, ...}` with aligned `=`; prose acknowledgements; a one-sentence license line.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| paper_logo.png | PNG, illustrated wordmark, transparent background | 805×531 | `<img ... width="30%">` in `<p>` | 257×169 | top of header |
| figure1.png | PNG, two-part teaser on white | 1591×873 | `<img ... width="100%">` in `<p>` | 856×470 | header, after the badge row |

The teaser's upper half is a pipeline: two stacked thumbnails each for Images (Appearance) and Pointmaps (Geometry, a rainbow depth map), arrows into a rounded pale teal box labelled "UniScene3D", a column of blue squares marked "3D scene representation", and curved arrows fanning out to Viewpoint Grounding, Scene Retrieval, Scene Type Classification, 3D Visual Question Answering and "...". The lower half shows two 3D room renders, each under a quoted query in a dashed box ("I am sitting on one of the green seats."), with legends comparing UniScene3D to a "w/o image" or "w/o pointmap" variant, and a radar chart of seven task scores (UniScene3D vs SOTA). Those are the only two images in the README. The transparent logo would survive GitHub's dark theme, but the white-backed teaser would not, and there is no `<picture>` switch, so the theme is light.

## Adapting to Other Content

- **A representation-learning or foundation-model paper.** Keep the order logo, h1 title, venue, authors, affiliation, logo badges, teaser, italic abstract, Contents, News, Key Takeaways. Size the logo at `width="30%"` (257px) and export the teaser about 1600px wide so it renders 856px.
- **A dataset.** Keep the Model/Data badge pair but lead with the Data badge, and make the teaser's lower half a sample strip; put the folder list from Data Preparation directly after Key Takeaways.
- **A repo without a logo.** Let the `<h1>` open the header; put the project name in the arXiv badge message, as here, so the name still appears above the fold.
- **A library.** Drop authors and venue, keep the four logo badges and the Contents list, and turn Key Takeaways into a five-bullet feature list with the same `**Label**:` lead-ins.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Give every badge a logo and keep them on the #555555 label | Mix logo and logo-less badges in one row |
| Explain the paper in five bold-labelled takeaways before the how-to | Bury the main finding under installation steps |
| Use an italic paragraph after the teaser as its caption | Leave a dense teaser without a sentence explaining it |
| Add a Contents list when there are ten or more sections | Rely on GitHub's outline button alone |
| Wrap the venue line in a `<p>` | Leave it as untagged text, which loses paragraph spacing |
| Keep the venue consistent across header and BibTeX | Cite `booktitle = {arxiv}` under an ECCV header |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">`: `<p>` with a transparent logo at `width="30%"`, `<h1>` with the full paper title, a venue line, a `<p>` of comma-separated linked authors, `<p><strong>Institution</strong></p>`, then `<p align="center">` with four flat shields.io badges on the #555555 label, each with a logo: arXiv #b31b1b (`logo=arxiv&logoColor=white`), Project Page #111827 (`logo=googlechrome&logoColor=white`), Model Hugging Face #f6c343 (`logo=huggingface&logoColor=yellow`, message text #333333), Data #4dabf7 (`logo=huggingface&logoColor=yellow`)."
2. "Put a `width="100%"` teaser (about 1591×873, renders 856×470) in the div: a pipeline on top with inputs flowing into a pale teal #daecec model box and out to a list of tasks, and qualitative renders plus a radar chart below. After `</div>`, write the abstract as one italic paragraph with the key phrase in bold italic."
3. "Follow with `## Contents` (bullet links), `## News` (`- 🚀 \`YYYY-MM-DD\`: ...`), and `## Key Takeaways` with five loose bullets labelled **Core Question**, **Preliminary Finding**, **Model Contribution**, **Key Training Idea**, **Result**. Then plain `##` sections: Expected Repository Structure (`text` tree), Installation (`### 1.` to `### 3.` with `bash`), Data Preparation, Pretraining, Evaluation (one h3 per task), Acknowledgements, Citation (`bibtex`), License."

## Similar Pages

- readme-qiuzidian-pano3dcomposer: a 3D-scene README with the same logo-capped flat badges (`logo=arxiv`, `logo=googlechrome`, white logo color) under a centred title.
- readme-mdyao-photoagent: also opens with an image above the title and uses a googlechrome-logo Project Page badge, but in `for-the-badge` style.
- readme-seohongpark-ogbench: an illustrated logo at a fixed width over a centred `<h1>` and one uniform badge row.
- readme-eku127-satnav: the same centred title, author, affiliation, badges and full-width teaser sequence, with logo-less badges and no Contents or takeaways section.

UniScene3D's distinguishing choices are a paper-title h1 under an illustrated logo, logos on every badge, an italic abstract as teaser caption, and a Key Takeaways section written as the paper's argument.

## Quick Start

````markdown
<div align="center">

<p>
  <img src="assets/logo.png" alt="ProjectName logo" width="30%">
</p>

<h1>Full Paper Title on One or Two Lines</h1>
<p>Venue (ABBR) Year</p>
<p>
  <a href="https://example.org/">Author One</a>,
  <a href="https://example.org/">Author Two</a>,
  <a href="https://example.org/">Author Three</a>
</p>

<p><strong>Institution</strong></p>

<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX">
    <img src="https://img.shields.io/badge/arXiv-ProjectName-b31b1b?logo=arxiv&logoColor=white" alt="arXiv" align="absmiddle">
  </a>
  <a href="https://example.github.io/project/">
    <img src="https://img.shields.io/badge/Project-Page-111827?logo=googlechrome&logoColor=white" alt="Project Page" align="absmiddle">
  </a>
  <a href="https://huggingface.co/org/model">
    <img src="https://img.shields.io/badge/Model-Hugging%20Face-f6c343?logo=huggingface&logoColor=yellow" alt="Model" align="absmiddle">
  </a>
  <a href="https://huggingface.co/datasets/org/data">
    <img src="https://img.shields.io/badge/Data-DatasetName-4dabf7?logo=huggingface&logoColor=yellow" alt="Data" align="absmiddle">
  </a>
</p>

<p>
  <img src="assets/figure1.png" alt="Teaser: pipeline, qualitative results and radar chart" width="100%">
</p>

</div>

*ProjectName learns X from ***key input***, unifying A and B. We evaluate it across tasks under several settings.*

## Contents

- [News](#news)
- [Key Takeaways](#key-takeaways)
- [Installation](#installation)
- [Citation](#citation)

## News

- 🚀 `YYYY-MM-DD`: Paper accepted to Venue Year.
- 🚀 `YYYY-MM-DD`: Code, model and data released.

## Key Takeaways
- **Core Question**: The gap, ending in **the question in bold?**

- **Preliminary Finding**: What the pilot showed.

- **Model Contribution**: What the model does.

- **Key Training Idea**: The objective.

- **Result**: What transfers where.

## Expected Repository Structure

```text
name/
├── configs/
└── run.py        # main entry point
```

## Installation

### 1. Create an environment

```bash
conda create -n name python=3.10 -y
conda activate name
```

## Data Preparation

## Pretraining

## Evaluation

### Task One

```bash
bash scripts/task_one.sh
```

## Acknowledgements

## Citation

If you find this repository useful, please cite the paper:

```bibtex
@inproceedings{key,
  title     = {...},
}
```

## License
````

## Provenance

- Repo: https://github.com/Yebulabula/UniScene3D (`README.md`, branch `main`, last README commit 8a1e748 on 2026-07-03).
- Paper: "RGB-Pointmap Pretraining for Unified 3D Scene Understanding", ECCV 2026, arXiv 2604.02546; first author Ye Mao. Project page https://yebulabula.github.io/UniScene3D/.
- Selection: a logo, title, badge row and a two-part teaser (pipeline plus qualitative and radar panels) lead into a contents list and a Key Takeaways section that explains the work in bolded lead-in bullets.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for all four badge URLs, PNG headers and alpha/pixel data for `paper_logo.png` and `figure1.png`.
- Written 2026-10-28.
