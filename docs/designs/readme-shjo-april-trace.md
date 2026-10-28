# TRACE — README Reference

> A press release pinned above a lab notebook: a centred title, a strip of block-letter badges, then four big numbers in a box before a word of explanation.

**Theme:** light

Read from `README.md` on the default branch `master` of github.com/shjo-april/TRACE (last commit touching the file d9d94b9, 2026-03-02; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; figure colors and pixel sizes come from `assets/teaser.png` and `assets/method_overview.png` fetched from the repo. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them. Rendered y values below are in the 1440×900 frame.

## Overview

The whole header sits inside one `<div align="center">`: an `<h1>` paper title that wraps to two lines, an `<h3>` award line with a star emoji, one row of four `for-the-badge` shields, a linked author line with superscript marks, and a two-line affiliation and footnote block. Two `---` rules then fence a bold blockquote announcing that code is still to come. The most distinctive element follows: a centred four-column Markdown table whose header row is the headline numbers (+5.1 AP, +7.1 PQ, 81× Faster, 0.889 ODS) and whose two body rows name the task and the dataset or unit. Only after that does the body begin, with emoji `##` headings (💡 TL;DR, 📢 News, 🔍 Overview, 📊 Main Results, 🛠️ Installation, 🚀 Quick Start, 📁 Model Zoo, 📂 Project Structure, 📖 Citation, 📜 License). Two full-width figures carry the explanation: a two-panel teaser under TL;DR and a three-part method figure under Overview. Four results tables follow with bold TRACE rows. Installation, Quick Start and Model Zoo each open with a "⏳ Coming in April 2026." blockquote even though the README was last edited in March 2026 and read in October 2026.

## Header Block

1. **Opening wrapper**: `<div align="center">` followed by a blank line, so the Markdown inside it is still parsed.
2. **Title** (y≈140 and 180): `# TRACE: Your Diffusion Model Is Secretly an Instance Edge Detector`. GitHub h1, 2em (32px), weight 600, centred, wrapping after "Edge"; GitHub's 1px grey rule sits under it across the 856px content width.
3. **Award line** (y≈246): `### ⭐ ICLR 2026 Oral Presentation (Top 1.13%, 223/19,814)`. GitHub h3, 1.25em (20px), weight 600, no rule. It appears as an entry in GitHub's outline menu.
4. **Badge row** (y≈288): four Markdown image links `[![Project Page](https://img.shields.io/badge/Project-Page-gold?style=for-the-badge)](...)` on consecutive source lines, which GitHub joins into one paragraph with single spaces. Each badge is 28px tall; the row is about 600px wide. Details in Badges.
5. **Authors** (y≈336): one Markdown line of six linked names separated by `, `, each followed by `<sup>1*</sup>`, `<sup>2*</sup>`, `<sup>2</sup>` or `<sup>2†</sup>`. Body size, GitHub link blue.
6. **Affiliations and footnotes** (y≈376 and 400): `<sup>1</sup>OGQ &nbsp;&nbsp; <sup>2</sup>Seoul National University  ` with two trailing spaces for a hard line break, then `<sup>*</sup>Equal contribution &nbsp;&nbsp; <sup>†</sup>Corresponding authors`. Unlike many READMEs, the marks are defined in the header.
7. **Closing wrapper**: `</div>`.
8. **First rule** (y≈438): `---`, which GitHub renders as a 4px light grey bar across the content width.
9. **Release notice** (y≈476 and 500): a two-line blockquote, `> **🚧 Code, pretrained models, and presentation materials will be released in April 2026. Please stay tuned!**  ` then `> If you'd like to be notified, please **⭐ star** this repository and **👁️ watch** for updates.` Left-aligned with GitHub's grey left bar; the first line is bold.
10. **Second rule** (y≈538): `---`.
11. **Headline-stat strip** (y≈583 to 658): a table inside a second `<div align="center">`, with `|:---:|` centring on all four columns. Header cells are the numbers (`+5.1 AP`, `+7.1 PQ`, `81× Faster`, `0.889 ODS`), the first body row the task (`Unsupervised Instance Seg.`, `Tag-supervised Panoptic Seg.`, `One-step Distillation`, `Instance Edge Quality`) and the second the dataset or unit (`COCO`, `VOC 2012`, `45ms / image`, `2× over best baseline`). GitHub bolds the header row and stripes the second body row; the table renders about 804px wide, centred.
12. **TL;DR** (heading at y≈716): `## 💡 TL;DR`, one paragraph with four bold phrases and the acronym spelled out as `**TRA**nsforming diffusion **C**ues to instance **E**dges`, then the teaser `<div align="center"><img src="./assets/teaser.png" width="100%"></div>`, which begins just below the 900px fold. This ends the header block.

## Badges

All four use the static path form `https://img.shields.io/badge/<label>-<message>-<color>?style=for-the-badge` with no `logo=` or `labelColor=`. In `for-the-badge` style shields.io draws square-cornered 28px badges with uppercase, letter-spaced 10px text, so "Project Page" reads PROJECT | PAGE. The label background is the default #555555 and label text white (#ffffff).

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| PROJECT | PAGE | `gold`, rendered #ffd700 (label #555555, message text #333333) | for-the-badge | shjo-april.github.io/TRACE |
| PAPER | PDF | `red`, rendered #dd4343 (label #555555) | for-the-badge | openreview.net/pdf?id=BjElYlJKMj |
| OPENREVIEW | FORUM | #8c1b13 (label #555555) | for-the-badge | openreview.net/forum?id=BjElYlJKMj |
| ARXIV | 2503.07982 | #b31b1b (label #555555) | for-the-badge | arxiv.org/abs/2503.07982 |

Badge widths from the returned SVGs are 135.75, 112, 174.75 and 164.75px. The named color `red` is drawn as #dd4343 in the SVG that shields.io returned on 2026-10-28, not the #e05d44 of the flat palette; `gold` is passed through as the CSS name, which is #ffd700. The message text is white except on gold, where shields.io switches to #333333. There is no link row of bold text links; the four badges are the only navigation.

Colors in the figures, not badges: the method figure's green check labels ("✓ Instance Emergence", "✓ Attn-to-Edge", "✓ Self-Distillation") are #006600, its red "Semantic" and "Before Training" labels and red fine-tuned blocks are #dd2222, and the frozen-diffusion outlines are blue #2266ee. The teaser uses the same #006600 green for its check boxes and arrows.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | TRACE: Your Diffusion Model Is Secretly an Instance Edge Detector | title; the centred div continues |
| h3 (centred) | ⭐ ICLR 2026 Oral Presentation (Top 1.13%, 223/19,814) | award line; badges, authors, affiliations and footnotes follow; then two rules around the release notice and the headline-stat strip |
| h2 | 💡 TL;DR | one bold-studded paragraph and the full-width teaser |
| h2 | 📢 News | three bullets with `**[YYYY.MM]**` dates and an emoji each |
| h2 | 🔍 Overview | full-width method figure, one paragraph, three bold numbered stage paragraphs |
| h2 | 📊 Main Results | four h3 subsections, each a table; two end with a one-line blockquote takeaway |
| h3 | Unsupervised Instance Segmentation | baseline / `+ **TRACE**` paired rows with gains in parentheses |
| h3 | Weakly-supervised Panoptic Segmentation | Method, Supervision, VOC PQ, COCO PQ |
| h3 | Diffusion vs. Non-Diffusion Backbones | Backbone, Type, Params, AP<sup>mk</sup> |
| h3 | Instance Edge Quality | ODS, OIS, clDice; TRACE last and all bold |
| h2 | 🛠️ Installation | "⏳ Coming in April 2026." blockquote, a commented `bash` block, h3 Requirements with four bullets |
| h3 | Requirements | Python, PyTorch, CUDA, GPU |
| h2 | 🚀 Quick Start | the same pending blockquote and three numbered h3 steps, each a `bash` block with backslash-continued flags |
| h3 | 1. Generate Instance Edges (Training-Free) / 2. One-Step Self-Distillation / 3. Apply to Downstream Tasks | one `bash` block each |
| h2 | 📁 Model Zoo | pending blockquote and a four-column table whose Download cells all read "Coming Soon" |
| h2 | 📂 Project Structure | an untagged code block with a box-drawing file tree and `#` comments |
| h2 | 📖 Citation | one sentence and a `bibtex` block |
| h2 | 📜 License | one sentence linking Apache 2.0 |

Absent from the source: logo, teaser GIF or video, table of contents, `<details>` blocks, dataset section, acknowledgements, contact section, star-history chart, bilingual toggle.

Present but unusual: the award line is an `<h3>` inside the centred div; a stale release notice and three "Coming in April 2026" placeholders remain after the date passed, and the Quick Start commands describe scripts (`trace_infer.py`, `trace_train.py`) that the README itself says are not yet released; the headline-stat table puts numbers in the header row; the award line says "Top 1.13%" while the News entry says "1.18% acceptance rate" for the same 223 papers; the Project Structure block has no language tag.

## Components

**Centred div header.** `<div align="center">`, blank line, ordinary Markdown (`#`, `###`, badge links, author line), blank line, `</div>`. The blank lines are what let GitHub parse the Markdown inside the HTML block.

**Block-letter badge row.** Four `[![Alt](https://img.shields.io/badge/Label-Message-color?style=for-the-badge)](url)` lines, label #555555, messages gold #ffd700, red #dd4343, #8c1b13 and #b31b1b. Alt text repeats the destination ("Project Page", "Paper", "OpenReview", "arXiv").

**Fenced notice.** `---`, a bold blockquote line with 🚧, a plain second line with bold **⭐ star** and **👁️ watch**, `---`. The two rules make it read as a banner across the page.

**Headline-stat strip.** A three-row, four-column table in `<div align="center">`, every column `:---:`. Row 1 (header, bold by GitHub): a signed gain, a speed-up or a score. Row 2: the task. Row 3: the dataset, timing or comparison. No bold or links inside cells.

**News list.** `- **[2026.02]** 🎉 TRACE is selected as ...`: bold bracketed `YYYY.MM` date, one emoji per item (🎉, ✅, 📄), bold venue names, newest first.

**Numbered stage paragraphs.** Three separate paragraphs beginning `**1. Instance Emergence Point (IEP)**`, `**2. ...**`, `**3. ...**` rather than a Markdown list, so each stage is a bold run-in heading.

**Results tables.** First column `:---` (left), all others `:---:` (centred). TRACE rows are written `+ **TRACE**` or `DHR + **TRACE** (Swin-L)` with every TRACE number bold and the gain in plain parentheses after it (`**7.9** (+4.9)`). Superscripts in headers use `<sup>`, as in `AP<sup>mk</sup>`. Two tables are followed by a one-sentence `>` blockquote stating the takeaway with a bold phrase.

**Pending placeholders.** `> ⏳ Coming in April 2026.` directly under the Installation, Quick Start and Model Zoo headings; Model Zoo cells read "Coming Soon" instead of links.

**Code blocks.** `bash` blocks with `#` comment lines and blank lines between clone, environment and install groups; long commands broken with ` \` and four-space-indented flags. The tree block is fenced with no language tag and uses `├──`, `│` and `└──` with aligned `#` comments. The citation is a `bibtex` block with aligned `=` signs, `{{TRACE}}` braces and a `note = {Oral Presentation}` field.

**License line.** One sentence with a relative link `[Apache 2.0 License](./LICENSE)`; no acknowledgements follow.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/teaser.png | PNG, two-panel paper figure on white, serif labels | 2381×980 | `<div align="center"><img src="./assets/teaser.png" width="100%"></div>` | 856×352 | end of TL;DR, starting just below the fold |
| assets/method_overview.png | PNG, three-row pipeline figure on white | 1379×1211 | same `<div align="center">` wrapper, `width="100%"` | 856×752 | top of Overview, before the text |

Both are paper figures reused as-is, with no caption line in the README and no `alt` text. The teaser pairs "(a) Observation: Instance Cues in Diffusion Models" with "(b) TRACE: Extracting Instance Boundaries", using cat photos, attention heat maps and green check labels (#006600). The method figure stacks "(a) Instance Edge Generation via Diffusion Forward", "(b) One-step Self-Distillation with Edge Decoder" and a training-progress strip, with red #dd2222 for trainable or rejected items and blue #2266ee for frozen modules. No `<picture>` pairs, no dark-theme variants, no GIFs.

## Adapting to Other Content

- **A library.** Keep the centred div with an h1 name and an h3 one-liner, keep one `for-the-badge` row (Docs, PyPI, License), and replace the stat strip with three columns such as speed, memory and supported backends. Skip the release notice.
- **A dataset.** Use the stat strip for counts (images, classes, annotations) with the split or modality in row 2 and the unit in row 3; put a sample-grid image at `width="100%"` (856px) under TL;DR.
- **A benchmark.** Keep the four-column strip for the headline gaps and the paired `Baseline` / `+ **Method**` table form, with the gain in parentheses after each bold number.
- **A repo without a teaser.** Let the stat strip close the header and move the method figure (about 1380px source, 856px rendered) directly under TL;DR.
- **A released repo.** Drop the `---` notice and all "Coming in" placeholders, and turn the Model Zoo Download cells into links.

## Do's and Don'ts

| Do | Don't |
|---|---|
| State the contribution as four numbers in the header row of a centred table | Bury the headline gains inside a prose paragraph |
| Pair each number with a task row and a dataset or unit row | Give a bare number without the benchmark it was measured on |
| Keep all badges in one `for-the-badge` family with the #555555 label | Mix flat and for-the-badge badges in one row |
| Define `*` and `†` on a line under the affiliations | Leave author marks unexplained |
| Bold every TRACE number and put the gain in plain parentheses | Bold the gain too, which doubles the emphasis |
| Remove the release notice and "Coming in" placeholders once the date passes | Leave a past release date in three sections |
| Use one figure per idea at `width="100%"` | Shrink paper figures below the column width, where their serif labels become unreadable |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside `<div align="center">` with blank lines around the content: `#` paper title, `###` award or venue line with ⭐, one row of four `for-the-badge` shields.io badges (label #555555; messages Project Page gold #ffd700, Paper PDF red #dd4343, OpenReview Forum #8c1b13, arXiv ID #b31b1b), a comma-separated author line with `<sup>1*</sup>` marks, and two lines for affiliations and the `*`/`†` definitions."
2. "After the header, add `---`, a two-line blockquote (bold first line), `---`, then a centred four-column table with `|:---:|` alignment whose header row holds the headline numbers (e.g. +5.1 AP, 81× Faster), body row 1 the task and body row 2 the dataset or unit. Follow with `## 💡 TL;DR`: one paragraph with bold key phrases and a `width="100%"` teaser in `<div align="center">`."
3. "Write the body as emoji `##` sections in this order: 📢 News (`**[YYYY.MM]**` bullets), 🔍 Overview (full-width figure plus three bold numbered stage paragraphs), 📊 Main Results (h3 per table, first column `:---`, others `:---:`, method rows bold with gains in parentheses, optional one-line blockquote takeaway), 🛠️ Installation, 🚀 Quick Start (numbered h3 steps with `bash` blocks), 📁 Model Zoo, 📂 Project Structure (box-drawing tree), 📖 Citation (`bibtex`), 📜 License."

## Similar Pages

- readme-deepmancer-hairport, readme-chuan-10-agile and readme-progresslm-progresslm also build their badge rows from `for-the-badge` shields; hairport and Agile also carry a News section. Compare how many badges each puts in one row against TRACE's four.
- readme-nvlabs-motionbricks and readme-vveicao-freeorbit4d also have a News section, but explain themselves with GIFs (a method GIF in MotionBricks, an input/output GIF grid in FreeOrbit4D) where TRACE uses static paper figures and numbers.
- TRACE's distinguishing choice is the three-row headline-stat table between the header and the first heading; its project page (shjo-april.github.io/TRACE) is a separate web page and is not described here.

## Quick Start

````markdown
<div align="center">

# ProjectName: Full Paper Title

### ⭐ Venue Year Award (Top X%, N/M)

[![Project Page](https://img.shields.io/badge/Project-Page-gold?style=for-the-badge)](https://example.github.io/project)
[![Paper](https://img.shields.io/badge/Paper-PDF-red?style=for-the-badge)](https://openreview.net/pdf?id=XXXX)
[![OpenReview](https://img.shields.io/badge/OpenReview-Forum-8c1b13?style=for-the-badge)](https://openreview.net/forum?id=XXXX)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?style=for-the-badge)](https://arxiv.org/abs/XXXX.XXXXX)

[Author One](https://example.org/)<sup>1*</sup>, [Author Two](https://example.org/)<sup>2*</sup>, [Author Three](https://example.org/)<sup>2†</sup>

<sup>1</sup>Institution A &nbsp;&nbsp; <sup>2</sup>Institution B  
<sup>*</sup>Equal contribution &nbsp;&nbsp; <sup>†</sup>Corresponding authors

</div>

---

> **🚧 One-line status notice.**  
> Second line with **⭐ star** and **👁️ watch**.

---

<div align="center">

| +X.X Metric | +X.X Metric | N× Faster | 0.XXX Score |
|:---:|:---:|:---:|:---:|
| Task one | Task two | Component | Quality measure |
| Dataset | Dataset | ms / image | comparison |

</div>

## 💡 TL;DR

One paragraph with the **key finding** in bold and the **ACRONYM** spelled out.

<div align="center">
  <img src="./assets/teaser.png" width="100%">
</div>

## 📢 News

- **[YYYY.MM]** 🎉 Event with **bold venue**.

## 🔍 Overview

<div align="center">
  <img src="./assets/method_overview.png" width="100%">
</div>

One paragraph.

**1. Stage One** does this.

**2. Stage Two** does this.

## 📊 Main Results

### Task One

| Method | Dataset A | Dataset B |
|:---|:---:|:---:|
| Baseline | 5.8 | 3.0 |
| + **Method** | **9.7** (+3.9) | **7.9** (+4.9) |

> One-sentence takeaway with a **bold phrase**.

## 🛠️ Installation

```bash
git clone https://github.com/org/name.git
cd name
pip install -r requirements.txt
```

## 🚀 Quick Start

### 1. First Step

```bash
python infer.py \
    --image_path ./examples/input.jpg
```

## 📁 Model Zoo

| Backbone | Dataset | Metric | Download |
|:---|:---:|:---:|:---:|
| Name | Data | 0.0 | [Link](https://example.org/) |

## 📂 Project Structure

```
name/
├── configs/      # Configuration files
└── README.md
```

## 📖 Citation

If you find ProjectName useful in your research, please consider citing:

```bibtex
@inproceedings{key,
  title     = {...},
}
```

## 📜 License

This project is released under the [Apache 2.0 License](./LICENSE).
````

## Provenance

- Repo: https://github.com/shjo-april/TRACE (`README.md`, branch `master`, last README commit d9d94b9 on 2026-03-02).
- Paper: "TRACE: Your Diffusion Model is Secretly an Instance Edge Detector", ICLR 2026 (Oral, per the README), arXiv 2503.07982; first author Sanghyun Jo. Project page https://shjo-april.github.io/TRACE.
- Selection: a headline-stat strip table (+5.1 AP, 81× faster) under the badges is a distinctive way to state the contribution, backed by a TL;DR and well-labelled method figures, though the release-pending notice and emoji headings make it a little busier.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `assets/teaser.png` and `assets/method_overview.png` fetched from the repo for pixel sizes and figure colors.
- Written 2026-10-28.
