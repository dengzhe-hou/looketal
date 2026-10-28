# HairPort — README Reference

> A paper laid out as a press kit: a row of loud capital-letter tags, a dated bulletin, and numbered figures that each carry a caption like a journal page, all separated by thick grey rules.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/deepmancer/HairPort (last commit touching the file 9e258f3, 2026-07-17; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs; image sizes come from `assets/images/teaser.png`, `paper_method.png` and `method.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README opens compactly. A centred `<h1>` "HairPort" with its grey rule is followed by one centred paragraph of three short lines (bold subtitle, bold venue, plain abbreviated author list), then seven `for-the-badge` shields that wrap into two centred rows of four and three. Each badge has a dark grey #555555 label and a saturated message color, all in uppercase. A one-sentence left-aligned summary closes the header, and the first `---` rule follows. From there the page alternates `---` rules (rendered as 4px light grey bars) with `##` sections: a News list of seven bold-dated items, a Results Teaser with a full-width figure and a small bold "Figure 1." caption, a Method At A Glance section with Figures 2 and 3 and a collapsed Paper Abstract, then a blockquote status note and a long, numbered Installation. The first screen ends partway into the teaser image. No emoji appear anywhere.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116, rule at about 145): `<h1 align="center">HairPort</h1>`. GitHub h1, 2em (32px), weight 600, short single line with a 1px grey rule across the 856px content width.
2. **Subtitle, venue and authors** (y≈174, 197, 221): one `<p align="center">` holding `<strong>In-context 3D-aware Hair Import and Transfer for Images</strong><br><strong>SIGGRAPH Conference Papers '26</strong><br>A. Heidari, A. Alimohammadi, and A. Mahdavi-Amiri`. Three centred lines at body size with no gap between them: two bold, one regular. Author names are initials plus surname, unlinked, with no affiliations or marks.
3. **Badge rows** (y≈251 to 277 and 284 to 310): one `<p align="center">` with seven badges, each `<a href="..."><img alt="..." src="https://img.shields.io/badge/...?style=for-the-badge"></a>` on its own source line (the Video badge has no `<a>`). Each badge is 28px tall; at 856px the row wraps after Project Page, giving four badges on the first row and three on the second. Details in Badges.
4. **Summary** (y≈345 to 370): one plain left-aligned Markdown sentence, two rendered lines, no bold.
5. **Rule** (y≈407): `---`, rendered by GitHub as a 4px (0.25em) bar in its border grey across the content width. The same rule separates every following section.
6. **News** (y≈450 to 670): `## News` and seven bullets; see Components.
7. **Results Teaser** (heading y≈747, image from about 785): `<p align="center"><img src="assets/images/teaser.png" alt="..." width="100%"><br><sub><b>Figure 1.</b> HairPort transfers hairstyles ...</sub></p>`. The 3455×1516 PNG renders at 856×376, so the first screen cuts it after its top row of faces; the caption is below the fold.

## Badges

All seven use the static path form `https://img.shields.io/badge/<label>-<message>-<color>?style=for-the-badge`. In that style shields.io draws square-cornered 28px badges, uppercases both parts, sets the label in regular and the message in bold Verdana with wide letter spacing, and puts the label on #555555. Message text is white (#ffffff) except on the yellow Weights badge, where shields.io switches it to #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| ARXIV | 2606.12562 | #b31b1b (label #555555) | for-the-badge | arxiv.org/abs/2606.12562 |
| DOI | 10.1145/3799902.3811046 | #2f6f9f (label #555555) | for-the-badge | doi.org/10.1145/3799902.3811046 |
| LICENSE | CC BY-NC-ND 4.0 | #dc6f35 (label #555555) | for-the-badge | creativecommons.org/licenses/by-nc-nd/4.0/ |
| PROJECT PAGE | LIVE | #2ea44f (label #555555) | for-the-badge | deepmancer.github.io/HairPort/ |
| VIDEO | COMING SOON | `lightgrey`, served as #939393 (label #555555) | for-the-badge | not linked |
| WEIGHTS | BALD CONVERTER | #ffcc4d (label #555555, message text #333333) | for-the-badge | huggingface.co/deepmancer/bald_konverter |
| DATASET | BALDY | #ff69b4 (label #555555) | for-the-badge | huggingface.co/datasets/deepmancer/baldy |

The label names a category and the message names the specific artifact or state ("LIVE", "COMING SOON"), so the row doubles as a status board. Six colors are given as hex in the URL; only the Video badge uses a named color, and the SVG that shields.io returns for `lightgrey` fills the message with #939393.

Other colors on the page come from GitHub itself: links in the News list and body are GitHub link blue #0969da, and the `---` rules are GitHub's border grey #d1d9e0. The figures add their own accents (soft blue and orange boxes in the method diagrams) that were not measured.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | HairPort | title; subtitle, venue, authors, badges and summary follow without a heading |
| h2 | News | seven bullets, each `**Month Year:**` then one sentence with an inline link |
| h2 | Results Teaser | one full-width figure with a `<sub>` "Figure 1." caption |
| h2 | Method At A Glance | Figures 2 and 3 at full width with `<sub>` captions, then a `<details>` "Paper Abstract" |
| h2 | Repository Status | a two-paragraph blockquote that opens with a bold sentence |
| h2 | Installation | h3 Requirements (four bold-led bullets), then numbered h3 steps 1 to 7 (environment, PyTorch, Get HairPort, remaining dependencies, external modules, data assets, Hugging Face login), each with a `bash` block |
| h2 | Quick Start | numbered h3 steps 1 to 5 (`bash`, `csv` and `text` blocks), then h3 Python API with a `python` block |
| h2 | Pipeline Stages | a three-column table of nine numbered stages, then a `bash` block for partial runs |
| h2 | Data Layout | a `text` tree of the data directory |
| h2 | Configuration | a bullet list of config areas, provenance notes, h3 Memory policy (GPU model residency) |
| h2 | Standalone Tools | h3 Individual stages, h3 Bald Converter, h3 3D Landmark Estimation, each with code |
| h2 | Project Structure | a `text` tree |
| h2 | External Dependencies / Models | h3 External modules with a Module / Repository / Used for table and a license note |
| h2 | Acknowledgements | one paragraph of linked project names |
| h2 | Citation | one sentence, a publication-details line, a `bibtex` block |
| h2 | License | two paragraphs and a copyright line |

Absent from the source: logo, affiliation line, linked author names, results table with numbers, embedded video or GIF, table of contents, emoji in headings or news items, star-history chart.

Present but unusual: a `---` rule before every `##` section from News to License (fifteen rules), so the page reads as a stack of separated panels; the Video badge is an unlinked placeholder ("COMING SOON"); figures are numbered with `<sub><b>Figure N.</b></sub>` captions exactly as in a paper; the full abstract sits in a `<details>` block inside the method section rather than at the top; Installation is long (seven numbered h3 steps) and comes before Quick Start.

## Components

**Stacked header paragraph.** Subtitle, venue and authors share one `<p align="center">` separated by `<br>`, so they render as a tight three-line block with no paragraph gaps between them. Bold marks the two lines that name the work and the venue.

**for-the-badge row.** Seven `<a><img alt="..." src="...?style=for-the-badge"></a>` lines in one centred `<p>`; every `alt` is set ("arXiv", "Paper DOI", "License: CC BY-NC-ND 4.0", "Project page", "Video coming soon", "Bald Converter weights", "Baldy dataset"). Label grey #555555; messages #b31b1b, #2f6f9f, #dc6f35, #2ea44f, #939393, #ffcc4d, #ff69b4.

**Section rule.** A bare `---` line between sections. GitHub draws it as a 4px bar in #d1d9e0 with 24px vertical margins, heavier than the 1px rule under each `##` heading, which gives the page its panelled rhythm.

**News list.** `- **June 2026:** Sentence with [inline link](...).` Dates are month and year only, newest first, bold with the colon inside the bold. Items mix announcements (preprint, DOI, acceptance, project page) and releases (code, dataset, weights).

**Numbered figure.** `<p align="center"><img src="..." alt="..." width="100%"><br><sub><b>Figure N.</b> One sentence.</sub></p>`. The `<sub>` makes the caption smaller than body text (GitHub renders it at about 75% size), and the bold "Figure N." label starts it. Every `alt` is a full descriptive phrase.

**Collapsible abstract.** `<details><summary><b>Paper Abstract</b></summary>` with blank lines around two Markdown paragraphs, where method components (**HairPort**, **Bald Converter**, **Baldy**, **3D-aware Transfer Pipeline**) are bold. Collapsed by default, it renders as a single "▸ Paper Abstract" line.

**Status blockquote.** `> **Official source preview.** ...` followed by `>` and a second paragraph with inline code, rendered with GitHub's grey left bar and muted text.

**Numbered steps.** Installation and Quick Start use h3 headings with the number in the text (`### 1. Create an environment`), each followed by one sentence and one fenced block. Language tags are `bash`, `csv`, `text` and `python`; comments inside `bash` blocks label alternatives ("# Resume from a stage").

**Stage table.** `| # | Stage | What happens |` with `|---|-------|--------------|` delimiters and no alignment colons; the stage name is bold and the description is one sentence that may contain inline code.

**Dependency table.** `| Module | Repository | Used for |` with `owner/name` link text in the middle column.

**Citation.** "If you use HairPort in your research, please cite:" then a plain line of publication details (dates, place, DOI link, ISBN in inline code, preprint link), then `@inproceedings{heidari2026hairport, ...}` with `=` aligned in a column.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.png | PNG photo grid, row labels "Face" and "Hair" in serif type | 3455×1516 | `<img ... width="100%">` in `<p align="center">` | 856×376 | Results Teaser, Figure 1 |
| paper_method.png | PNG method diagram, three stages | 2618×937 | `<img ... width="100%">` | 856×306 | Method At A Glance, Figure 2 |
| method.png | PNG two-panel diagram (dataset generation, LoRA finetuning) | 2443×1457 | `<img ... width="100%">` | 856×511 | Method At A Glance, Figure 3 |

All three figures are paper figures reused at full width, each with a numbered `<sub>` caption. The teaser is a 2×4 photo grid of source faces, reference hair and results; the method figures use pale blue and peach panels on white. No GIF, video or `<picture>` dark variant; the figures have white backgrounds and are designed for the light theme.

## Adapting to Other Content

- **A library.** Keep the h1, the three-line stacked paragraph (one-line description, version line, maintainers) and the for-the-badge row (Docs, PyPI, License, CI), then News and Installation separated by `---` rules; drop the numbered figures if there is nothing to show.
- **A dataset.** Make the badge row Dataset, Paper, License, and turn Results Teaser into a sample grid at `width="100%"` (856px) with a "Figure 1." caption; replace Pipeline Stages with a split table in the same `| # | Split | What it holds |` form.
- **A benchmark with scores.** Add a Results section after Method At A Glance with a pipe table, numeric columns right-aligned (`| ---: |`) and the best value in bold, introduced by a `<sub><b>Table 1.</b></sub>` caption to match the figure captions; HairPort has no results table, so this is an extension.
- **A repo without a teaser.** Move Method At A Glance up so Figure 1 is the method diagram, and keep the collapsed abstract under it.
- **A shorter README.** Keep the `---` rules only between the header and News and before Citation; with fewer than six sections, a rule before every heading looks heavy.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use one badge style (`for-the-badge`) for every badge in the row | Mix `flat` and `for-the-badge` badges |
| Name the artifact or its state in the message (BALDY, LIVE, COMING SOON) | Repeat the label in the message |
| Number every figure and caption it in `<sub>` with a bold "Figure N." | Leave full-width paper figures without a caption |
| Date news items with a bold month and year, newest first | Mix date formats within one list |
| Collapse the full abstract in `<details>` | Paste the abstract above the badges |
| Keep each install step to one sentence and one tagged block | Put several unrelated commands in one untagged block |

## Agent Prompt Guide

1. "Write a README header in GitHub HTML: a centred `<h1>` with the short project name, one centred `<p>` holding a bold subtitle, `<br>`, a bold venue line, `<br>`, a plain author list; then one centred `<p>` of seven `?style=for-the-badge` shields.io badges with label #555555 and messages arXiv #b31b1b, DOI #2f6f9f, License #dc6f35, Project Page LIVE #2ea44f, Video COMING SOON lightgrey (#939393, unlinked), Weights #ffcc4d, Dataset #ff69b4; then a one-sentence summary and a `---` rule."
2. "After the header, write `##` sections separated by `---` in this order: News, Results Teaser, Method At A Glance, Repository Status, Installation, Quick Start, Pipeline Stages, Data Layout, Configuration, Standalone Tools, Project Structure, External Dependencies / Models, Acknowledgements, Citation, License. News items are `- **Month Year:** sentence with link`."
3. "Show each figure as `<p align="center"><img src="..." alt="..." width="100%"><br><sub><b>Figure N.</b> one sentence</sub></p>`, put the abstract in `<details><summary><b>Paper Abstract</b></summary>`, write install steps as `### 1. Step name` followed by one sentence and a `bash` block, and end with a `bibtex` block introduced by one sentence."

## Similar Pages

- readme-vveicao-freeorbit4d also uses `for-the-badge` badges under a centred title, but only two of them, and it shows results in HTML tables of GIFs instead of numbered figures.
- readme-sisyphm-studiorecon pairs a method figure with a stage table as HairPort's Pipeline Stages does, with flat badges and no news list.
- readme-microsoft-renderformer has a similar centred title and venue but replaces badges with a bold text-link row and adds a full table of contents.

## Quick Start

````markdown
<h1 align="center">ProjectName</h1>

<p align="center">
  <strong>Full Paper Title</strong>
  <br>
  <strong>Venue Year</strong>
  <br>
  A. Author, B. Author, and C. Author
</p>

<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?style=for-the-badge"></a>
  <a href="https://doi.org/10.XXXX/XXXX"><img alt="Paper DOI" src="https://img.shields.io/badge/DOI-10.XXXX%2FXXXX-2f6f9f?style=for-the-badge"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-NAME-dc6f35?style=for-the-badge"></a>
  <a href="https://example.github.io/project/"><img alt="Project page" src="https://img.shields.io/badge/Project%20Page-live-2ea44f?style=for-the-badge"></a>
  <img alt="Video coming soon" src="https://img.shields.io/badge/Video-coming%20soon-lightgrey?style=for-the-badge">
  <a href="https://huggingface.co/org/weights"><img alt="Weights" src="https://img.shields.io/badge/Weights-Name-ffcc4d?style=for-the-badge"></a>
  <a href="https://huggingface.co/datasets/org/data"><img alt="Dataset" src="https://img.shields.io/badge/Dataset-Name-ff69b4?style=for-the-badge"></a>
</p>

One-sentence summary of what the method does.

---

## News

- **Month Year:** Announcement with an [inline link](https://example.org/).

---

## Results Teaser

<p align="center">
  <img src="assets/images/teaser.png" alt="Describe the figure." width="100%">
  <br>
  <sub><b>Figure 1.</b> One-sentence caption.</sub>
</p>

---

## Method At A Glance

<p align="center">
  <img src="assets/images/method.png" alt="Describe the figure." width="100%">
  <br>
  <sub><b>Figure 2.</b> One-sentence caption.</sub>
</p>

<details>
<summary><b>Paper Abstract</b></summary>

Abstract paragraphs.

</details>

---

## Installation

### 1. Create an environment

```bash
conda create -n name python=3.11 -y
```

---

## Quick Start

---

## Pipeline Stages

| # | Stage | What happens |
|---|-------|--------------|
| 1 | **Stage** | One sentence. |

---

## Citation

If you use ProjectName in your research, please cite:

```bibtex
@inproceedings{key,
  title     = {...},
}
```

---

## License
````

## Provenance

- Repo: https://github.com/deepmancer/HairPort (`README.md`, branch `main`, last README commit 9e258f3 on 2026-07-17).
- Paper: "HairPort: In-context 3D-aware Hair Import and Transfer for Images", SIGGRAPH Conference Papers '26 (SIGGRAPH 2026), arXiv 2606.12562, DOI 10.1145/3799902.3811046; first author Alireza Heidari. Project page https://deepmancer.github.io/HairPort/.
- Selection: for-the-badge badges in matched colors, a dated news list, and every figure carries a numbered caption like a paper, while a collapsible Paper Abstract and horizontal rules give long content a calm rhythm.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for all seven badge URLs, the three figure PNGs fetched from the repo for pixel sizes.
- Written 2026-10-28.
