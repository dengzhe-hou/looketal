# DeepSeek-V3 — README Reference

> A corporate annual report on GitHub paper: a blue whale wordmark, three tidy rows of brand-colored tags, a numbered contents page, then chapter after numbered chapter of charts and bolded score tables.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/deepseek-ai/DeepSeek-V3 (last commit touching the file e975062, 2025-06-16; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the seven shields URLs and from the custom `figures/badge.svg` and `figures/logo.svg` in the DeepSeek-V2 repository that the README loads; chart sizes and colors come from `figures/benchmark.png` and `figures/niah.png` fetched from this repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The first screen is a brand header followed by a contents page. A centred blue whale-and-wordmark logo (514×109 rendered) sits above a thick grey `<hr>`, then three centred rows of flat badges (three, three and two badges, broken with `<br>`), then a centred bold "Paper Link" with an eye emoji. Below it an h2 "Table of Contents" holds a nine-item ordered list whose items match the numbered h2 headings that follow ("1. Introduction" to "9. Contact"). The body is long and disciplined: an introduction paragraph with an 80%-width grouped bar chart, a Model Summary split into three bold-titled blocks by `---` rules, a compact five-column download table, three centred benchmark tables with category labels in the first column and the best score in bold, six GitHub Note callouts used as table footnotes and caveats, a needle-in-a-haystack heat map, eight numbered "How to Run Locally" subsections with `shell` blocks, then license, citation and contact. There is no news list and no emoji in headings.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Lint comments**: three `<!-- markdownlint-disable ... -->` lines (first-line-h1, html, no-duplicate-header). They render nothing and explain why the README has no top `#` heading.
2. **Logo** (y≈94–203): `<div align="center"><img src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/logo.svg?raw=true" width="60%" alt="DeepSeek-V3" /></div>`. The SVG is 195×41.36 with every path filled #4d6bfe and a transparent background, so `width="60%"` renders it 514×109. It is loaded from the DeepSeek-V2 repository, shared across the company's READMEs.
3. **Rule** (y≈234): a raw `<hr>`, GitHub's 4px grey rule, full content width.
4. **Badge rows** (y≈271, 296 and 323): one `<div align="center" style="line-height: 1;">` holding eight `<a><img alt="..." src="..."/></a>` badges in three rows split by `<br>`. GitHub strips the `style` attribute, so rows keep the default line height and sit about 25px apart. Row 1: Homepage, Chat, Hugging Face. Row 2: Discord, WeChat, Twitter. Row 3: Code License, Model License. Row 1 spans about 473px. Details in Badges.
5. **Paper link** (y≈352): `<a href="https://arxiv.org/pdf/2412.19437"><b>Paper Link</b>👁️</a>`, inside the same div, after a third `<br>`. A bold body-size link followed by an eye emoji, the only paper reference in the header.
6. **Table of contents** (y≈403–678): `## Table of Contents` (h2 with rule) and an ordered list `1. [Introduction](#1-introduction)` through `9. [Contact](#9-contact)`. The "1. Introduction" h2 starts just below, at y≈730, inside the first screen.

There is no text title: the project name appears only in the logo's `alt` and in the body text.

## Badges

All shields badges use the static path form in the default `flat` style: 20px tall, 3px corner radius, Verdana 11px, label on #555555. Several repeat the color as a `color=` query parameter, and `logoColor=white` is given on badges without a `logo=` (Chat, Hugging Face), where it has no effect. Message text is white #ffffff on dark messages and #333333 on the light ones, as shields.io picks it from the background.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| DeepSeek (whale icon) | Homepage | #536af5 (label #555555) | custom SVG in the flat shape, `figures/badge.svg` from DeepSeek-V2 | www.deepseek.com |
| 🤖 Chat | DeepSeek V3 | #536af5 (label #555555) | flat (default) | chat.deepseek.com |
| 🤗 Hugging Face | DeepSeek AI | #ffc107 (label #555555, message text #333333) | flat (default) | huggingface.co/deepseek-ai |
| Discord (logo) | DeepSeek AI | #7289da (label #555555) | flat, `logo=discord` | discord.gg invite |
| WeChat (logo) | DeepSeek AI | `brightgreen`, rendered #44bb00 (label #555555) | flat, `logo=wechat` | a QR-code JPEG in the DeepSeek-V2 repo |
| Twitter (X logo) | deepseek_ai (rendered "deepseek ai") | `white` #ffffff (label #555555, message text #333333) | flat, `logo=x` | twitter.com/deepseek_ai |
| Code License | MIT | #f5de53 (label #555555, message text #333333) | flat (default) | LICENSE-CODE |
| Model License | Model Agreement | #f5de53 (label #555555, message text #333333) | flat (default) | LICENSE-MODEL |
| (link row) | **Paper Link**👁️ | GitHub link blue, bold | plain link | arxiv.org/pdf/2412.19437 |

The rows are grouped by purpose: product and model hub (row 1), community channels (row 2), licenses (row 3). The two brand-blue badges share #536af5, close to the logo's #4d6bfe; both license badges share #f5de53. In the Twitter badge the underscore in `deepseek_ai` is read by shields.io as a space, so it renders "deepseek ai". The METHOD_README table gives `brightgreen` as #4c1; the WeChat SVG returned on 2026-10-28 fills #44bb00.

Other colors on the page come from images and GitHub itself: the logo #4d6bfe; the benchmark chart's DeepSeek-V3 bars #4d6bfe with diagonal hatching, a light blue #aac1ff series and a sand #e8d2a0 series among grey bars; and GitHub's Note callout bar and title in #0969da.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h2 | Table of Contents | nine-item ordered list of anchor links |
| h2 | 1. Introduction | one paragraph of nine sentences with figures (671B, 37B, 14.8T, 2.788M H800 GPU hours), then `figures/benchmark.png` at 80% |
| h2 | 2. Model Summary | `---`, then three blocks each made of a bold title paragraph and bullets, separated by `---` |
| h2 | 3. Model Downloads | a centred five-column table, a Note callout, two paragraphs with links |
| h2 | 4. Evaluation Results | h3 Base Model (h4 Standard Benchmarks: table and Note; h4 Context Window: `figures/niah.png` at 80% and one sentence), h3 Chat Model (h4 Standard Benchmarks (Models larger than 67B): table and Note; h4 Open Ended Generation Evaluation: three-column table and Note) |
| h2 | 5. Chat Website & API Platform | two sentences with links |
| h2 | 6. How to Run Locally | an eight-item numbered list of runtimes with bold names, a paragraph, a `shell` conversion command, a Note; then h3 6.1 to 6.8 |
| h3 | 6.1 Inference with DeepSeek-Infer Demo (example only) | h4 System Requirements (Note, `pip-requirements` block), h4 Model Weights & Demo Code Preparation, h4 Model Weights Conversion, h4 Run, each with `shell` blocks |
| h3 | 6.2 to 6.8 | one runtime each (SGLang, LMDeploy, TRT-LLM, vLLM, LightLLM, AMD GPUs, Huawei Ascend NPUs), one to four paragraphs of links |
| h2 | 7. License | two sentences linking the code and model licenses |
| h2 | 8. Citation | an untagged code block holding the BibTeX entry |
| h2 | 9. Contact | one sentence with an email link |

Absent from the source: a text title or h1, author and affiliation lines, news or changelog, demo GIF or video, acknowledgements, star chart, emoji in headings, `<details>` blocks.

Present but unusual: the README has no `#` heading at all and silences the markdownlint rule that expects one; the logo and two badge targets are loaded from the DeepSeek-V2 repository; the Model Summary uses `---` rules plus bold paragraphs as sub-headings instead of h3s; the two standard-benchmark tables are long (32 and 22 score rows, each after three architecture rows) and are centred by wrapping them in `<div align="center">`; the "6.7" subsection's "SGLang instructions" link points to the 6.3 LMDeploy anchor; the contact link `[service@deepseek.com](service@deepseek.com)` has no `mailto:`, so GitHub resolves it as a relative path; the citation block has no `bibtex` tag; the Section 6 cross-link text reads "How_to Run_Locally".

## Components

**Logo block.** `<div align="center"><img src="...logo.svg?raw=true" width="60%" alt="Name" /></div>` followed by `<hr>`. A single-color #4d6bfe vector wordmark, no title text under it.

**Grouped badge rows.** One centred `<div>` with badges on separate source lines and `<br>` between groups; within a group the newlines render as single spaces. Each `<img>` has `alt` first and `src` on the next line. Brand colors per destination: #536af5 product, #ffc107 Hugging Face, #7289da Discord, #44bb00 WeChat, #ffffff X, #f5de53 licenses.

**Numbered table of contents.** `## Table of Contents` then `1. [Introduction](#1-introduction)`; every h2 below begins with the same number and a period ("## 1. Introduction"), so the anchors carry the number (`#5-chat-website--api-platform`).

**Ruled summary blocks.** Inside Model Summary: `---`, a bold paragraph title ("**Architecture: Innovative Load Balancing Strategy and Training Objective**"), a bullet list, `---`, and so on for Pre-Training and Post-Training.

**Download table.** Wrapped in `<div align="center">` with blank lines inside; five columns with bold headers (`| **Model** | **#Total Params** | **#Activated Params** | **Context Length** | **Download** |`), every column centred with `| :------------: |`, and download cells written `[🤗 Hugging Face](url)`.

**Benchmark tables.** Also wrapped in `<div align="center">`. The first column holds a category label (English, Code, Math, Chinese, Multilingual) only on the first row of each group and is blank otherwise; the second column is "Benchmark (Metric)"; the next rows give Architecture, # Activated Params and # Total Params before the scores. The best score in each row is bold, ties within 0.3 are all bold, and "-" marks missing values. No alignment colons, so cells are left-aligned under centred headers.

**Note callouts as footnotes.** `> [!NOTE]` directly after each table states how to read it ("Best results are shown in bold. Scores with a gap not exceeding 0.3 are considered to be at the same level."), and elsewhere for caveats (weight sizes, unsupported Transformers, Linux-only demo). GitHub draws them with a #0969da left bar and an info-icon "Note" title.

**Runtime list.** An ordered list `1. **DeepSeek-Infer Demo**: ...` with one bold runtime per item, then one h3 per runtime numbered "6.1" to "6.8", most ending with "(recommended)".

**Code blocks.** `shell` for commands (one long command per block, no line continuations), `pip-requirements` for pinned dependencies, and an untagged block for the citation.

**License and contact.** Plain sentences with links to `LICENSE-CODE` and `LICENSE-MODEL`, and a one-sentence contact line.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| logo.svg (DeepSeek-V2 repo) | SVG wordmark, single color #4d6bfe, transparent | 195×41.36 | `<img width="60%">` in `<div align="center">` | 514×109 | first element |
| benchmark.png | PNG, opaque white background, grouped bar chart | 1702×994 | `<p align="center"><img width="80%" src="figures/benchmark.png"></p>` | 685×400 | end of 1. Introduction |
| niah.png | PNG, opaque white background, heat map | 2310×1201 | `<p align="center"><img width="80%" src="figures/niah.png"></p>` | 685×356 | 4. Evaluation Results, Context Window |

The benchmark chart compares six models on six benchmarks (MMLU-Pro, GPQA-Diamond, MATH 500, AIME 2024, Codeforces, SWE-bench Verified) with a legend row along the top; DeepSeek-V3 is the leftmost, hatched #4d6bfe bar in each group with its value printed in bold above it. Both figures have no `alt` text and opaque white backgrounds, and no `<picture>` variant is provided, so they appear as white panels on GitHub's dark theme. The logo and badges work on either theme.

## Adapting to Other Content

- **A library.** Keep the centred logo at `width="60%"`, the `<hr>`, and badge rows grouped by purpose (docs and package; community; license), then the numbered Table of Contents. Replace Evaluation Results with an API section and keep "How to Run Locally" as numbered h3 subsections per platform.
- **A dataset.** Keep the header and replace the download table's columns with Split, Size, Format, Download; keep it centred with `:---:` columns and `[🤗 Hugging Face](url)` cells.
- **A benchmark with scores.** This README is already the model: category label in the first column only at group starts, bold best per row, a Note under each table that states the bold rule and the tie threshold.
- **A repo without a logo.** Use `<h1 align="center">` for the name in place of the logo, keep the `<hr>` and the three badge rows.
- **A single-paper research repo.** Drop the community row, keep the license row, and move the paper link into the first row as an arXiv badge.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Number the h2 headings and the contents list the same way | Number the contents list while leaving headings unnumbered |
| Group badges into rows by purpose with `<br>` | Let eight badges wrap wherever the column ends |
| Use each destination's brand color for its badge message | Give every badge the same blue |
| Explain bold and ties in a Note right under each results table | Bold best values without saying how ties are handled |
| Centre wide tables with `<div align="center">` and blank lines inside | Put the table Markdown on the same line as the `<div>` |
| Size charts with `width="80%"` and give them `alt` text | Leave figures without `alt`, as both charts here are |
| Write `mailto:` links and tag the citation block `bibtex` | Link a bare email address as a relative path |

## Agent Prompt Guide

1. "Start a README with three `<!-- markdownlint-disable -->` comments, then `<div align="center"><img src="figures/logo.svg" width="60%" alt="Name" /></div>` and `<hr>`. Under it, one `<div align="center">` with three badge rows split by `<br>`: Homepage #536af5, 🤖 Chat #536af5, 🤗 Hugging Face #ffc107; Discord #7289da with `logo=discord`, WeChat #44bb00 with `logo=wechat`, Twitter white #ffffff with `logo=x`; Code License and Model License #f5de53. All flat with the #555555 label. End the div with `<a href="paper.pdf"><b>Paper Link</b>👁️</a>`."
2. "Write `## Table of Contents` as a nine-item ordered list linking numbered h2s: 1. Introduction (paragraph plus an 80%-width chart), 2. Model Summary (`---`-separated bold-titled bullet blocks), 3. Model Downloads, 4. Evaluation Results (h3 Base Model and Chat Model with h4 tables), 5. Chat Website & API Platform, 6. How to Run Locally (h3 6.1 to 6.8), 7. License, 8. Citation, 9. Contact."
3. "Build the download table inside `<div align="center">` with bold headers and `| :---: |` on every column, download cells `[🤗 Hugging Face](url)`. Build results tables with a category label in the first column only at group starts, bold the best score per row, and follow each table with `> [!NOTE]` stating the bold rule and tie threshold."

## Similar Pages

- **readme-snuhcc-dice-bench** also opens with an image header, centred badges and reference tables, with emoji h2s and `---` rules where DeepSeek-V3 uses numbered h2s and a contents list.
- **readme-yrainy0615-gaussianplant** uses GitHub alert callouts heavily too, as environment caveats (Note, Important, Warning) rather than table footnotes.
- **readme-jiwoogit-varbooth** opens with a single image header and centred badges but keeps the body short, with no tables or results.

## Quick Start

````markdown
<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <img src="figures/logo.svg" width="60%" alt="Name" />
</div>
<hr>
<div align="center">
  <a href="https://example.com/"><img alt="Homepage"
    src="https://img.shields.io/badge/Name-Homepage-536af5"/></a>
  <a href="https://chat.example.com/"><img alt="Chat"
    src="https://img.shields.io/badge/🤖%20Chat-Name-536af5"/></a>
  <a href="https://huggingface.co/org"><img alt="Hugging Face"
    src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Org-ffc107"/></a>
  <br>
  <a href="https://discord.gg/XXXX"><img alt="Discord"
    src="https://img.shields.io/badge/Discord-Org-7289da?logo=discord&logoColor=white"/></a>
  <a href="https://twitter.com/org"><img alt="Twitter Follow"
    src="https://img.shields.io/badge/Twitter-org-white?logo=x&logoColor=white"/></a>
  <br>
  <a href="LICENSE-CODE"><img alt="Code License"
    src="https://img.shields.io/badge/Code_License-MIT-f5de53"/></a>
  <a href="LICENSE-MODEL"><img alt="Model License"
    src="https://img.shields.io/badge/Model_License-Model_Agreement-f5de53"/></a>
  <br>
  <a href="https://arxiv.org/pdf/XXXX.XXXXX"><b>Paper Link</b>👁️</a>
</div>

## Table of Contents

1. [Introduction](#1-introduction)
2. [Model Summary](#2-model-summary)
3. [Model Downloads](#3-model-downloads)
4. [Evaluation Results](#4-evaluation-results)
5. [How to Run Locally](#5-how-to-run-locally)
6. [License](#6-license)
7. [Citation](#7-citation)
8. [Contact](#8-contact)

## 1. Introduction

One paragraph with the key numbers.
<p align="center">
  <img width="80%" src="figures/benchmark.png" alt="Benchmark chart">
</p>

## 2. Model Summary

---

**Block Title: What It Does**

- Point.

---

## 3. Model Downloads

<div align="center">

| **Model** | **#Total Params** | **#Activated Params** | **Context Length** | **Download** |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| Name-Base | 0B | 0B | 0K | [🤗 Hugging Face](https://huggingface.co/org/Name-Base) |

</div>

> [!NOTE]
> Caveat about the weights.

## 4. Evaluation Results
### Base Model
#### Standard Benchmarks

<div align="center">

|  | Benchmark (Metric) | # Shots | Baseline A | Baseline B | Name |
|---|---|---|---|---|---|
| English | Benchmark (Acc.) | 5-shot | 0.0 | 0.0 | **0.0** |
| | Benchmark (EM) | 3-shot | **0.0** | 0.0 | 0.0 |

</div>

> [!NOTE]
> Best results are shown in bold. State the tie threshold.

## 5. How to Run Locally

### 5.1 Inference with Demo

```shell
python generate.py --ckpt-path /path/to/ckpt
```

## 6. License

## 7. Citation
```bibtex
@misc{key,
      title={...},
}
```

## 8. Contact
If you have any questions, please raise an issue or contact us at [team@example.com](mailto:team@example.com).
````

## Provenance

- Repo: https://github.com/deepseek-ai/DeepSeek-V3 (`README.md`, branch `main`, last README commit e975062 on 2025-06-16).
- Paper: the README describes the "DeepSeek-V3 Technical Report" (arXiv 2412.19437, author DeepSeek-AI). The gallery's selection record lists this repo under "Advancing Zero-shot Text-to-Speech Intelligibility across Diverse Domains via Preference Alignment", ACL 2025, first author Xueyao Zhang, field text-to-speech; that paper is not mentioned in this README, so the venue, person and field in the catalog come from the selection record and do not describe this page.
- Selection: a centered logo over grouped badge rows, a numbered table of contents that matches numbered headings, a sharp results chart, a compact download table and a GitHub Note callout make it a disciplined large-project template.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the seven shields URLs, `figures/logo.svg` and `figures/badge.svg` from the DeepSeek-V2 repository, and `figures/benchmark.png` and `figures/niah.png` fetched from this repo for pixel sizes and colors.
- Written 2026-10-28.
