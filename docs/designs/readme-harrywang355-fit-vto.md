# FIT-VTO — README Reference

> A fitting-room lookbook under a ruled title: three square-cornered tags, a lineup of people in clothes that are too big or too small, then the spec sheet.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/HarryWang355/FIT-VTO (last commit touching the file 5288a22, 2026-06-18; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the three badge URLs; the teaser size and transparency come from `assets/teaser.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README is a dataset card in the order a reader asks the questions. A centred `<h1>` holding the full paper title, with GitHub's grey rule under it, comes first; then a centred row of three `flat-square` badges; then one centred paragraph that stacks bold author names, a small `<sup>` equal-contribution note, the affiliations and an italic bold venue line. A transparent-background teaser at `width="100%"` (856×418 rendered) fills most of the first screen: three rows of garment, person and try-on images running from "Tight Fit" to "Loose Fit", with a grey rounded card of example measurements on the right. Below it the body is six plain `##` sections, each fenced by a `---` rule, so the page reads as stacked bands: Abstract, Dataset (a field / description schema table and a callout), Data Generation and Preparation (two numbered `###` steps that point to sub-READMEs), Repository Structure (a commented tree), Citation and Acknowledgements. There is no install section, no results table, no news and no license section.

## Header Block

Everything down to the teaser is centred. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116): `<h1 align="center">FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On</h1>`. GitHub h1, 2em (32px), weight 600, one line, with the 1px grey rule across the 856px content width. The full paper title is the heading; there is no separate short name or subtitle.
2. **Badge row** (y≈170): one `<p align="center">` holding three `<a><img src="https://img.shields.io/badge/...?style=flat-square..."></a>` blocks separated by `&nbsp;` lines, so each gap is a non-breaking space plus the source newlines (about 12px). Badges are 20px tall; the row spans about 440px. Details in Badges.
3. **Author paragraph** (y≈215 to 287): a single `<p align="center">` with four lines broken by `<br>`:
   - `<b>Yuanhao Wang*&nbsp;&nbsp;Johanna Karras*&nbsp;&nbsp;Yingwei Li&nbsp;&nbsp;Ira Kemelmacher-Shlizerman</b>`: one bold run, names unlinked, separated by double non-breaking spaces; `*` is plain text, not `<sup>`.
   - `<sup>* Equal Contribution, listed in no particular order</sup>`: the whole note in `<sup>`, so it renders at about 12px and slightly raised.
   - `University of Washington &nbsp;·&nbsp; Google Research`: plain text with a middle dot; no affiliation numbers.
   - `<em><b>ACM Transactions on Graphics (SIGGRAPH 2026)</b></em>`: the venue closes the block, italic and bold.
4. **Teaser** (y≈322 to 740): `<p align="center"><img src="assets/teaser.png" width="100%"></p>`. 3196×1559 RGBA PNG with a transparent background, 856×418 at the 920px column; no `alt`, no link, no caption. Its rotated row labels ("Layflat Image", "Person Image", "Try-On Image") and handwritten size labels are black on transparency.
5. **Rule** (y≈763): `---`, GitHub's thick grey `<hr>` (0.25em, 4px tall). The `## Abstract` heading follows at y≈805, so the first screen ends on the start of the abstract.

## Badges

All three use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` with `style=flat-square`: 20px tall, square corners, no gloss, Verdana 11px, label on shields.io's default #555555 grey, white (#ffffff) text on both halves. Two carry a `logo=` parameter that draws a 14px white Simple Icons mark before the label.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Project Page (logo=github) | FIT | #007ec6 (`blue`; label #555555) | flat-square | johannakarras.github.io/FIT/ |
| arXiv (logo=arxiv) | 2604.08526 | #b31b1b (label #555555) | flat-square | arxiv.org/abs/2604.08526 |
| 🤗 Dataset | Preview (100K) | #67ac09 (`green` as returned by shields.io; label #555555) | flat-square | huggingface.co/datasets/Yuanhao-Harry-Wang/fitvto-100k |

Rendered widths read from the SVGs: 123px, 133px and 162px. The labels are destinations or categories and the messages are specifics (the project short name, the arXiv ID, the release size), so the badge row doubles as a fact line. The Hugging Face mark is an emoji typed into the label text, not a `logo=`.

There are no link rows that act as buttons. Colors seen in the teaser and used in Components: the measurement card fill #efefef (pixel-sampled from the PNG) and black #000000 label text on a transparent background.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On | title; badges, author paragraph, teaser and a `---` follow without a heading |
| h2 | Abstract | two paragraphs of the paper abstract; **FIT** expanded with bold initials (`**F**it-**I**nclusive **T**ry-on`) and the scale (**1M try-on image triplets**) in bold |
| h2 | Dataset | one sentence, a bold linked inline-code dataset ID followed by " — 100K training samples · 5K evaluation benchmark · CC-BY-NC-ND-4.0", "Each sample contains:", a two-column Field / Description table, then a `>` callout led by **Preview scale:** |
| h2 | Data Generation and Preparation | one sentence ("Follow the steps below in order.") and two `###` steps |
| h3 | Step 1 — 3D Garment Simulation | one paragraph and a pointer line `📄 &nbsp;See **[`garmentcode_generation/`](...)** for installation, asset setup, and usage.` |
| h3 | Step 2 — Sim2Real Retexturing | one paragraph and the same pointer line form for `sim2real/` |
| h2 | Repository Structure | an untagged fenced block holding a box-drawing tree with aligned `#` comments |
| h2 | Citation | "If you find this work useful, please cite:" and a `bibtex` block (`@article{fitvto2026, ...}`) |
| h2 | Acknowledgements | one sentence linking GarmentCode, FLUX.1-dev and OminiControl |

Every section boundary is a `---` line (six in all), including the one between the teaser and Abstract and the one before Acknowledgements.

Absent from the source: installation or quick start in the top README (both live in the two sub-READMEs), results or benchmark table, news, table of contents, license section or badge, demo GIF or video, emoji in headings, `<details>` blocks.

Present but unusual: the badge row sits above the authors rather than below them; the venue is the last line of the author paragraph; the step headings use an em dash ("Step 1 — ..."); the header lists Wang first and the BibTeX lists Karras first, which the "listed in no particular order" note covers; the BibTeX `journal` is "SIGGRAPH" while the venue line says ACM Transactions on Graphics; the teaser has no `alt`.

## Components

**Centred badge paragraph.** `<p align="center">` with each badge as an indented `<a href="..."><img src="..." alt="..."></a>` block and a bare `&nbsp;` line between blocks. All three use `style=flat-square`, label #555555 and messages #007ec6, #b31b1b, #67ac09.

**Stacked author paragraph.** One `<p align="center">` whose lines are joined with `<br>`: a `<b>` name run with `&nbsp;&nbsp;` separators, a `<sup>` contribution note, affiliations joined by `&nbsp;·&nbsp;`, and `<em><b>` venue text. Spacing inside the block is line height only; the block as a whole takes GitHub's 16px paragraph margin.

**Section rules.** A `---` line before every `##` heading. GitHub draws it as a 4px grey bar with 24px margins, which reads heavier than the 1px rule under each h2 and gives the page its banded rhythm.

**Schema table.** `| Field | Description |` with the delimiter `|:---:|:---|`, so the Field column is centred and Description is left-aligned. Field cells are inline code; related fields share one cell joined by ` / ` (`` `body_height` / `body_bust` / `body_waist` / `body_hips` ``). Descriptions end with the unit or image size in parentheses ("(768×1024)", "(cm)").

**Spec line.** `**[`dataset-id`](url)** — 100K training samples · 5K evaluation benchmark · CC-BY-NC-ND-4.0`: a bold link wrapping inline code, an em dash, then facts joined by ` · `.

**Callout.** A single-line blockquote `> **Preview scale:** ...` with a bold lead label and dot-separated counts. GitHub renders it with a 4px grey left border and grey text.

**Numbered steps.** `### Step N — Title`, one paragraph saying what the step does, then a pointer line opening with `📄 &nbsp;` and a bold link to the sub-folder's README.

**Code blocks.** The repository tree uses an untagged fence with `├──`/`└──` characters and `#` comments aligned in a column; the citation uses `bibtex`. No `bash` blocks in this file.

**Citation and acknowledgements.** One sentence, then the `@article` block with aligned `=` signs; acknowledgements is one prose sentence with three inline links. No license line.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| assets/teaser.png | PNG, RGBA, transparent background | 3196×1559 | `<img src="assets/teaser.png" width="100%">` in `<p align="center">` | 856×418 | header, after the author paragraph; no caption |

The teaser is a three-row grid of eight columns: layflat garment photos, person photos, and the try-on results, with rotated serif row labels on the left and a "Tight Fit ← → Loose Fit" arrow plus handwritten garment and body sizes under each column ("M Garment, 2XL Body"). A rounded grey (#efefef) card on the right shows one person and one shirt with dimension lines and handwritten measurements. Because the background is transparent and the labels are black, the figure is designed for the white light theme; on GitHub's dark theme the labels would sit on a dark page (not captured). It is the only image; there is no `<picture>` pair, GIF or video.

## Adapting to Other Content

- **Another dataset.** Keep the order exactly: h1 title, badge row (Project Page, arXiv, Dataset), author paragraph with the venue last, a `width="100%"` sample grid, then Abstract and Dataset. Keep the centred-field schema table and put release size and license on one spec line.
- **A method repo with code.** Replace "Data Generation and Preparation" with "Installation" and "Usage" sections, keeping the `### Step N — Title` form for ordered steps and the `📄 &nbsp;See **[...]**` pointer when a step has its own README.
- **A benchmark with scores.** Add a "Results" section after Dataset with numeric columns right-aligned (`| ---: |`) and the best value in bold; FIT has no such table, so this is an extension.
- **A repo without a teaser.** Let the author paragraph close the header and follow it directly with the `---` rule; do not leave an empty image paragraph.
- **A repo with a dark-theme audience.** Export the teaser on a white (#ffffff) background rather than transparency, since black labels on transparency disappear on a dark page.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use one badge style (`flat-square`) with the default #555555 label for every badge | Mix `flat`, `flat-square` and `for-the-badge` in one row |
| Put each fact in the badge message (arXiv ID, release size) | Use messages like "link" or "here" |
| Stack authors, contribution note, affiliations and venue in one centred paragraph with `<br>` | Split them into four paragraphs with separate margins |
| Separate every `##` section with `---` | Use `---` inside a section where a heading would do |
| Centre the field-name column of a schema table with `:---:` and keep fields in inline code | Leave units out of the description column |
| Give each pipeline step one paragraph and one pointer to its own README | Repeat sub-README install steps in the top README |

## Agent Prompt Guide

1. "Write a GitHub README header: `<h1 align="center">` with the full paper title, then a centred row of three shields.io badges in `style=flat-square` separated by `&nbsp;` (Project Page with `logo=github` and message #007ec6, arXiv with `logo=arxiv` and message #b31b1b, '🤗 Dataset' with a release-size message in #67ac09; all labels #555555). Then one centred paragraph: bold author names separated by `&nbsp;&nbsp;`, `<br>`, a `<sup>` equal-contribution note, `<br>`, affiliations joined by `&nbsp;·&nbsp;`, `<br>`, the venue in `<em><b>`. Then a `width="100%"` teaser on a white background and a `---` rule."
2. "After the header write six `##` sections, each preceded by `---`: Abstract, Dataset, Data Generation and Preparation, Repository Structure, Citation, Acknowledgements. No emoji in headings. In Dataset, write one bold linked inline-code dataset ID followed by ' — ' and facts joined by ' · ', then a Field / Description table with `|:---:|:---|` and inline-code field names, then a `> **Preview scale:**` callout."
3. "Write ordered pipeline steps as `### Step N — Title`, one paragraph each, ending with `📄 &nbsp;See **[`folder/`](folder/README.md)** for installation and usage.` Show the repository as an untagged fenced tree with `├──` branches and aligned `#` comments, and end with a `bibtex` `@article` block introduced by one sentence."

## Similar Pages

- **readme-eku127-satnav**: also a dataset paper with a centred title and a full-width teaser, but SatNav puts the venue and authors before a uniform `flat` badge row and has a runnable Quick Start; FIT puts `flat-square` badges directly under the h1 and has no install section.
- **readme-nvlabs-motionbricks**: same h1-title, badge-row, teaser order with arXiv #b31b1b among default shields.io badges.
- **readme-snuhcc-dice-bench**: another dataset or benchmark repo whose badge row points to arXiv, a project page and a Hugging Face dataset.

## Quick Start

````markdown
<h1 align="center">Full Paper Title: A Dataset for Something</h1>

<p align="center">
  <a href="https://example.github.io/project/">
    <img src="https://img.shields.io/badge/Project%20Page-NAME-blue?style=flat-square&logo=github" alt="Project Page">
  </a>
  &nbsp;
  <a href="https://arxiv.org/abs/XXXX.XXXXX">
    <img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?style=flat-square&logo=arxiv" alt="arXiv">
  </a>
  &nbsp;
  <a href="https://huggingface.co/datasets/org/name">
    <img src="https://img.shields.io/badge/🤗%20Dataset-Preview%20(100K)-green?style=flat-square" alt="Dataset">
  </a>
</p>

<p align="center">
  <b>Author One*&nbsp;&nbsp;Author Two*&nbsp;&nbsp;Author Three</b>
  <br>
  <sup>* Equal Contribution</sup>
  <br>
  Institution A &nbsp;·&nbsp; Institution B
  <br>
  <em><b>Journal or Venue (Conference Year)</b></em>
</p>

<p align="center">
  <img src="assets/teaser.png" width="100%" alt="Describe the teaser.">
</p>

---

## Abstract

Paragraph one. Paragraph two introduces **NAME** (**N**ame **A**cronym) and its scale in **bold**.

---

## Dataset

A preview release is available on Hugging Face:

**[`org/dataset-id`](https://huggingface.co/datasets/org/dataset-id)** — 100K training samples · 5K evaluation benchmark · License

Each sample contains:

| Field | Description |
|:---:|:---|
| `field_a` | What it is (size) |
| `field_b` / `field_c` | What they are (unit) |

> **Preview scale:** count · count · full release coming soon.

---

## Data Generation and Preparation

This repository contains the full pipeline. Follow the steps below in order.

### Step 1 — First Stage

One paragraph on what this stage does.

📄 &nbsp;See **[`stage_one/`](stage_one/README.md)** for installation and usage.

### Step 2 — Second Stage

One paragraph on what this stage does.

📄 &nbsp;See **[`stage_two/`](stage_two/README.md)** for installation and usage.

---

## Repository Structure

```
repo/
├── stage_one/          # What it holds
│   └── README.md
└── stage_two/          # What it holds
    └── README.md
```

---

## Citation

If you find this work useful, please cite:

```bibtex
@article{key2026,
  title     = {...},
  year      = {2026},
}
```

---

## Acknowledgements

This work builds on [Project](https://example.org/) for something.
````

## Provenance

- Repo: https://github.com/HarryWang355/FIT-VTO (`README.md`, branch `main`, last README commit 5288a22 on 2026-06-18).
- Paper: "FIT: A Large-Scale Dataset for Fit-Aware Virtual Try-On", SIGGRAPH 2026 (ACM Transactions on Graphics), arXiv 2604.08526; first author Johanna Karras (equal contribution with Yuanhao Wang; the header lists Wang first). Project page https://johannakarras.github.io/FIT/.
- Selection: a clean pattern for dataset repos, with a labeled teaser, an abstract, a field and description table for the data schema, numbered generation steps and a commented directory tree, all separated by consistent rules.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the three badge URLs, and `assets/teaser.png` fetched from the repo for its size, transparency and card color.
- Written 2026-10-28.
