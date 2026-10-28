# Med-PRM — README Reference

> A clinic's front desk: a navy wordmark over the door, a bracketed venue tag on the title, five color-coded tickets in a row, then the noticeboard, the process chart and the scoreboard in that order.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/eth-medical-ai-lab/Med-PRM (last commit touching the file d726b38, 2025-09-15; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs, checked against pixels in the capture; logo and figure sizes and colors come from `media/med-prm-logo-full-clear.png` and `media/overview.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The page opens with a large centred wordmark: a circular icon of a head in profile ringed by a document, a magnifier, a check mark and a book, next to "Med-PRM" in heavy navy letters. Under it the full paper title is an ordinary left-aligned `#` heading that starts with a bracketed venue tag, "[EMNLP 2025] Med-PRM: …", wrapping to two lines with GitHub's rule beneath. A centred row of five flat shields.io badges follows, then a `### News` list of four dated bullets with emoji, then `## 📖 Overview` with one bold-led bullet and a staged pipeline figure at 99% width. The rest is short: a seven-column scoreboard table, three numbered experiment steps with indented `bash` blocks, a contact line and an indented BibTeX block. The whole README ends at about 2,650px in the tall capture, about three screens, so it reads as a compact summary rather than documentation.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Logo** (y≈90 to 282): `<p align="center"><img src="media/med-prm-logo-full-clear.png" alt="medprm" style="width: 600px;"></p>`. GitHub keeps the inline `style` here (the API output reads `style="width: 600px; max-width: 100%;"`), so the 3389×1068 transparent PNG renders at 600×189, centred. The navy wordmark is the largest text on the page.
2. **Title** (y≈335 to 376, two lines): `# [EMNLP 2025] Med-PRM: Medical Reasoning Models with Step-wise Guideline-verified Process Rewards`. GitHub h1, 2em (32px), weight 600, left-aligned (no `align`), with the 1px grey rule under it. The bracketed venue is plain text inside the heading, not a link.
3. **Badge row** (y≈420 to 440): one `<p align="center">` holding five `<a ... target="_blank"><img src="https://img.shields.io/badge/..."></a>` lines. Each badge is 20px tall; the row spans about 600px. No `alt` attributes. Details in Badges.
4. **News** (y≈484 onward): `### News` (h3, 1.25em, no rule) and four `*` bullets. This is the last header element on the first screen; `## 📖 Overview` begins at about y≈707.

There are no author names, affiliations or teaser in the header; the authors appear only in the BibTeX block at the end.

## Badges

All five use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` with a shields.io named color and no `style=`, `logo=` or `labelColor=`, so they render in the default `flat` style: 20px tall, 3px corner radius, faint gloss, Verdana 11px, label on #555555 grey with white text. Hex values are the fills shields.io serves for each named color today; the capture pixels match them under the gloss.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2506.11474 | `red` #dd4343 (label #555555) | flat (default) | huggingface.co/papers/2506.11474 |
| Project | Page | `blue` #007ec6 (label #555555) | flat (default) | med-prm.github.io |
| 🤗 Hugging Face | Model | `orange` #ea7233 (label #555555) | flat (default) | huggingface.co/dmis-lab/llama-3.1-medprm-reward-v1.0 |
| 🤗 Hugging Face | Dataset | `orange` #ea7233 (label #555555) | flat (default) | huggingface.co/datasets/dmis-lab/llama-3.1-medprm-reward-training-set |
| Code | GitHub | `brightgreen` #44bb00 (label #555555) | flat (default) | github.com/eth-medical-ai-lab/Med-PRM (this repo) |

The 🤗 emoji is URL-encoded into the label (`%F0%9F%A4%97%20Hugging%20Face%20`), which widens those two labels to about 99px. The "arXiv" badge links to the Hugging Face papers page, not to arxiv.org; the News list links arxiv.org directly. The "Code / GitHub" badge points at the repository the reader is already in.

Other colors on the page come from images: the wordmark and icon navy #0f3d59, and in the overview figure a green #4c8736 for correct-step "+" boxes and check marks, red #ac2a0a for incorrect-step "−" boxes and crosses, steel blue #7ba4c1 for model chips and blue #3e6db4 for the knowledge-source logos.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (left) | [EMNLP 2025] Med-PRM: Medical Reasoning Models with Step-wise Guideline-verified Process Rewards | title; preceded by the centred logo and followed by the centred badge row |
| h3 | News | four dated bullets, newest first |
| h2 | 📖 Overview | one bullet with **MED-PRM** in bold, then the pipeline figure at 99% |
| h2 | Scoreboard | one seven-column table, four rows, MedQA-4 accuracy in the last column |
| h2 | 🔄 Experiment | ordered list of three bold-named steps, each with an indented `bash` block |
| h2 | Contact | one line with two plain email addresses (GitHub autolinks them) |
| (no heading) | **BibTeX Citation**: | a bold inline label and sentence, then an indented `bibtex` block |

Absent from the source: authors and affiliations in the header, teaser image or GIF, installation section, model zoo table separate from the badges, license section, acknowledgements, table of contents.

Present but unusual: News is an `###` that comes before the first `##`, so it sits under the h1 like a subheading; the venue appears as a bracketed prefix in the title; the citation has no heading and is introduced by a bold inline label; the BibTeX includes a biblatex-style `author+an` field marking three first and two last authors; the Experiment step 3 refers to "step 5", which does not exist in the list.

## Components

**Logo banner.** One centred `<img>` in a `<p align="center">`, sized with `style="width: 600px;"`. Transparent PNG, navy #0f3d59 on no background.

**Badge row.** Five flat static badges in one `<p align="center">`, each anchor with `target="_blank"`; label grey #555555, messages #dd4343, #007ec6, #ea7233, #ea7233 and #44bb00. The two Hugging Face badges share label and color and differ only in the message.

**News list.** `* [Month/DD/YYYY] emoji text` with the month spelled out inside square brackets (`[September/15/2025]`), followed by 🎉 or 📰. The project name and the key fact are bold (`**Med-PRM**`, `**Oral Presentation**`, `**80% accuracy on MedQA**`); one item links the bold venue (`**[EMNLP 2025](https://2025.emnlp.org/)**`). Newest first.

**Bold-led bullet.** The Overview is a single `-` bullet that opens with `**MED-PRM**` and runs four sentences, used as a paragraph.

**Scoreboard table.** Seven columns (Policy Model, Reward Model, Policy Base Model, Reward Base Model, Policy Training Method, Reward Training Method, MedQA-4) with padded `|--------------------|` delimiters and no alignment colons. GitHub centres the header cells and left-aligns the numbers. Rows are sorted by ascending MedQA-4 (78.24, 79.18, 79.87, 80.35); no value is bold. "-" fills an empty cell.

**Numbered steps.** `1. **Prepare Data**: Execute ...` with the bold step name, a colon and one sentence, then a `bash` block indented three spaces so it stays inside the list item. Blank line between steps.

**Contact line.** "Feel free to reach out to …" with two plain email addresses that GitHub autolinks.

**Citation.** `**BibTeX Citation**: If you use Med-PRM in your research, please cite it using the following BibTeX entry:` then a `bibtex` block indented three spaces, a `@misc{medprm2025, ...}` entry with `eprint`, `archivePrefix` and `primaryClass`.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| med-prm-logo-full-clear.png | PNG wordmark, transparent background | 3389×1068 | `<img ... style="width: 600px;">` in `<p align="center">` | 600×189 | first element of the page |
| overview.png | PNG pipeline figure, opaque white | 3816×2716 | `<img ... style="width: 99%;">` in `<p align="center">` | 847×603 | inside 📖 Overview, after the bullet |

The overview figure is a four-stage diagram with bold numbered stage titles drawn in the image itself: "1. Trace generation" (Q&A cards, an LLM chip, step traces, a retrieval arrow to a box of guideline-source logos), "2. Labeling" (an LLM (Large) chip marking steps +/−, then expert validation), "3. Training" (labelled traces into a Med-PRM chip with a 🔥) and "4. Use cases" (inference reranking and π training). Correct steps are green #4c8736 "+" boxes and wrong steps red #ac2a0a "−" boxes, so the figure has its own legend-free color code. Labels are in a sans-serif close to Arial at large size; at 847px the stage titles read at about body size. There is no GIF, no video and no `<picture>` switch; the logo's navy on transparent would sit on GitHub's dark background with very low contrast, which is why the theme is light.

## Adapting to Other Content

- **A paper repo with a logo.** Keep the order logo, `#` title with a bracketed venue prefix, centred badge row, `### News`, then the first `##`. Size the logo to 600px with `width="600"` (more portable than inline `style`) and export it with a transparent background only if a dark-theme variant is also supplied via `<picture>`.
- **A library.** Keep the logo and badge row, replace the bracketed venue with a version or "PyPI" badge, turn the Scoreboard into a supported-models table and keep the three numbered Experiment steps as Install / Run / Train.
- **A dataset.** Make the second Hugging Face badge the first in the row, keep the pipeline figure at 99% (847px) as the construction diagram and turn the Scoreboard into a split table.
- **A benchmark with scores.** Keep the scoreboard shape but right-align the score column (`|------:|`) and bold the best value; Med-PRM leaves both at GitHub defaults.
- **A repo without a logo.** Start with the `#` title and let the badge row and News list form the header; the page then opens about 280px higher.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Give the wordmark a fixed 600px width so it dominates without filling the column | Let a 3389px logo render at the full 856px |
| Keep five flat badges with label grey #555555 and one color per destination | Point a "Code / GitHub" badge at the repo the reader is already in |
| Date News items in one fixed bracketed format, newest first | Mix date formats or bury the venue acceptance below older items |
| Put the staged pipeline figure directly under a one-paragraph overview | Separate the overview text and its figure with other sections |
| Sort the scoreboard rows by the reported metric | Leave an unsorted score column with no bold or alignment cue |
| Number setup steps and keep each `bash` block indented inside its list item | Reference a step number that does not exist in the list |
| Give the citation its own `##` heading when adapting this layout | Hide the BibTeX under a bold inline label after Contact |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown: a centred `<p align="center">` with a 600px-wide transparent wordmark logo (navy #0f3d59), then a left-aligned `#` title that starts with a bracketed venue tag like `[EMNLP 2025]`, then one `<p align="center">` of five flat shields.io badges with label grey #555555: arXiv number #dd4343, Project Page #007ec6, 🤗 Hugging Face Model #ea7233, 🤗 Hugging Face Dataset #ea7233, Code GitHub #44bb00."
2. "Follow the header with `### News` as four `*` bullets in the form `[Month/DD/YYYY] 🎉 **Project** ...`, newest first, then `## 📖 Overview` with one bold-led bullet and a centred pipeline figure at 99% width (847px at a 920px column), then `## Scoreboard` with a seven-column model table sorted by the final metric."
3. "Write `## 🔄 Experiment` as an ordered list of three steps, each `**Step name**: one sentence` followed by a `bash` block indented three spaces. End with `## Contact` and a `bibtex` citation block introduced by one sentence."

## Similar Pages

- readme-donaldssh-k-merge: same default-flat five-badge row on #555555 labels for an ACL-family paper, but it centres the title in a div, lists authors and affiliations and uses one compact 660px diagram with no News or results.
- readme-snuhcc-dice-bench: the closest neighbour, built on the same template: a centred full-width banner image, a left-aligned `#` title, a centred `<p>` of flat badges with `target="_blank"` (arXiv red, Project Page blue, 🤗 Hugging Face orange, Code GitHub brightgreen), a News `###` with dated bullets and `## 📖 Overview` with a centred pipeline figure. It adds `---` rules around News and puts the venue in News rather than in the title.
- readme-chuan-10-agile: a centred header with a News list, but it uses `for-the-badge` badges and a `#` short name with a `###` subtitle instead of a logo and a bracketed venue prefix.

## Quick Start

````markdown
<p align="center">
  <img src="media/logo.png" alt="project" width="600">
</p>

# [Venue Year] ProjectName: Full Paper Title

<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX" target="_blank"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-red"></a>
  <a href="https://example.github.io/" target="_blank"><img src="https://img.shields.io/badge/Project-Page-blue"></a>
  <a href="https://huggingface.co/org/model" target="_blank"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20-Model-orange"></a>
  <a href="https://huggingface.co/datasets/org/data" target="_blank"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20-Dataset-orange"></a>
  <a href="https://github.com/org/repo" target="_blank"><img src="https://img.shields.io/badge/Code-GitHub-brightgreen"></a>
</p>

### News
* [Month/DD/YYYY] 🎉 **ProjectName** is accepted to **[Venue Year](https://example.org/)**!
* [Month/DD/YYYY] 📰 **ProjectName** preprint is now available on [arXiv](https://arxiv.org/abs/XXXX.XXXXX).

## 📖 Overview

- **ProjectName** is ... (one paragraph).

<p align="center">
  <img src="media/overview.png" alt="Overview" width="99%">
</p>

## Scoreboard

| Policy Model | Reward Model | Base Model | Training Method | Metric |
|--------------|--------------|------------|-----------------|--------|
| Model A | Ours | Base | SFT | 78.24 |

## 🔄 Experiment

1. **Prepare Data**: Execute the data preparation script:

   ```bash
   python prepare.py
   ```

2. **Score**: Run a quick test:

   ```bash
   bash scripts/score.sh
   ```

## Contact
Feel free to reach out to name@example.org

**BibTeX Citation**: If you use ProjectName in your research, please cite it using the following BibTeX entry:

   ```bibtex
   @misc{key2025,
     title={...},
   }
   ```
````

## Provenance

- Repo: https://github.com/eth-medical-ai-lab/Med-PRM (`README.md`, branch `main`, last README commit d726b38 on 2025-09-15).
- Paper: "Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards", EMNLP 2025 (oral, per the README's News), arXiv 2506.11474; first author Jaehoon Yun. Project page https://med-prm.github.io/.
- Selection: a wordmark logo banner, a single badge row, a short news list, a staged pipeline figure and a scoreboard table give a compact overview that runs straight into numbered experiment steps and the citation.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for each badge URL with capture pixels as a check, and the logo and overview PNGs fetched from the repo for pixel sizes, transparency and colors.
- Written 2026-10-28.
