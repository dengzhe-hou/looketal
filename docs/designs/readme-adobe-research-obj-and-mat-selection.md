# MAOAM — README Reference

> A conference proceedings page with its own table of contents: bold names on a centred line, a small ACM SIGGRAPH seal, six slim tags, and a grid of watermelon and kitchen shots washed in teal where the model chose.

**Theme:** light

Read from `README.md` on the default branch `master` of github.com/adobe-research/obj-and-mat-selection (last commit touching the file 004caf2, 2026-07-29; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the six badge URLs; image sizes and the teaser's overlay color come from the PNGs in `docs/` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The header is one `<div align="center">` that reads top to bottom like a paper's first page: a `#` title over two lines with GitHub's grey rule, two rows of bold linked author names joined by middle dots, one affiliation line, a gap, a 180px ACM SIGGRAPH logo, a bold venue line "SIGGRAPH Conference Papers '26", and a row of six flat 20px badges. The teaser, a 92% wide figure of input photos and teal selection overlays with italic prompt captions and two group labels (Material selection, Object selection), fills the rest of the screen. Under it a one-line TL;DR blockquote and a linked Contents list of eight entries (six with emoji) set up the body. Horizontal rules (`---`) separate the `##` sections, which mix emoji headings (✨, 🧠, ⚙️, 📊) with plain ones (Demo, Data, Acknowledgements, Citation). The body behaves like a paper companion: figures at 92% with data-source and statistics tables under them, then long setup, demo, evaluation and data-schema sections with many code blocks.

## Header Block

Everything down to the teaser sits inside `<div align="center">`. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈24 with its "README.md" file bar; content starts at y≈90).

1. **Title** (y≈139–180, two lines): `# MAOAM: Unified Object &amp; Material Selection with Vision-Language Models`. GitHub h1, 2em (32px), weight 600; the entity renders as "&" and the line breaks after "Vision-". The grey rule sits at y≈208 across the 856px content width.
2. **Authors** (y≈236 and 260): one `<p>` with eight `<a href="..."><b>Name</b></a><sup>n</sup>` entries separated by `&nbsp;·&nbsp;` lines and a `<br>` after the fifth name. All names are bold links in GitHub link blue.
3. **Affiliations** (y≈300): a Markdown paragraph, `<sup>1</sup>&nbsp;University of Wisconsin–Madison &nbsp;·&nbsp; <sup>2</sup>&nbsp;Adobe Research, UK &nbsp;·&nbsp; <sup>3</sup>&nbsp;Adobe Research, USA`, plain text on one line, using the same middle-dot separator as the authors.
4. **Spacer**: a lone `<br>` paragraph, which opens about 40px of empty space before the logo.
5. **Venue logo** (y≈366–438): `<img src="docs/siggraph_logo.png" width="180" alt="SIGGRAPH">`. The 1000×400 PNG renders at 180×72; its opaque white background holds the ACM SIGGRAPH mark in grey and a red-blue swirl.
6. **Venue line** (y≈443): `**SIGGRAPH Conference Papers '26**`. Body size, bold.
7. **Badge row** (y≈470–490): `<p>` holding six `<a>` blocks, each written over three source lines with `<img alt="..." src="https://img.shields.io/badge/...">` in the middle. Each badge is 20px tall and the row spans about 626px. Details in Badges.
8. **Teaser** (y≈512 to 832): `<img src="docs/teaser.png" width="92%" alt="MAOAM teaser">`. The 6588×2675 PNG renders at 788×320. No link and no caption below it; the captions are drawn inside the figure.
9. **After the div**: a `<br>` and then the TL;DR blockquote at y≈874, written over two `>` source lines as "**TL;DR** — MAOAM is a unified model that selects **objects or materials** from **text prompts, clicks, or both**.", rendered as one line with GitHub's grey left bar and muted text. The Contents heading follows below the fold.

## Badges

All six use the static path form `https://img.shields.io/badge/<label>-<message>-<hex>.svg` in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 grey. Message text is white (#ffffff) except on the two yellow badges, where shields.io picks #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2606.04880 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2606.04880 |
| Paper | ACM DL | #b31b1b (label #555555) | flat (default) | doi.org/10.1145/3799902.3811186 |
| Project | Page | #1f6feb (label #555555) | flat (default) | jadenpark0.github.io/project_pages/maoam/ |
| 🤗 (emoji as label) | Weights | #ffd21e (label #555555, message text #333333) | flat (default) | huggingface.co/jpark677/maoam_ckpts |
| 🤗 (emoji as label) | Test data | #ffd21e (label #555555, message text #333333) | flat (default) | huggingface.co/datasets/jpark677/maoam_data |
| License | Adobe Research | #44bb00 (`brightgreen`, label #555555) | flat (default) | LICENSE |

Badge widths from the SVGs: 116, 94, 86, 76, 82 and 150px. Two badges share the arXiv red for the two versions of the paper; the project page takes GitHub's own accent blue #1f6feb rather than shields.io `blue`; the Hugging Face badges replace a text label with the 🤗 emoji (URL-encoded `%F0%9F%A4%97`). The named `brightgreen` renders as #44bb00 (#4b0) in the served SVG. Every `alt` is a short noun ("arXiv", "Paper", "Project page", "Weights", "Test data", "License").

Other colored marks come from the imagery, not from badges: the teaser's selection overlays are a flat teal (median sampled value about #74dedd) laid over the photos, its prompt captions are italic black serif on white, and the method diagram uses light blue and salmon module boxes. The logo adds a small red and blue swirl.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | MAOAM: Unified Object & Material Selection with Vision-Language Models | title; authors, affiliations, logo, venue, badges and teaser follow without a heading |
| (blockquote) | TL;DR | one sentence with two bold phrases |
| h2 | Contents | eight bullets linking to the sections below, six with an emoji |
| h2 | ✨ Capabilities | one sentence pointing to the project page |
| h2 | 🧠 Architecture and data | method figure at 92%, one paragraph; h3 Material mask sources (paragraph, dataset figure, four-column Set table), h3 Description generation, h3 VQA generation with hard-negative mining (figure), h3 Training data composition |
| h2 | ⚙️ Setup | three-column backbone table, a `> **Hardware.**` note, two `bash` blocks; h3 Pretrained weights (`bash`), h3 Code structure (unlabelled tree) |
| h2 | Demo | one paragraph, one `bash` block with two commands, a paragraph, a four-column Mode / Click / Text / Notes table with `&check;` marks |
| h2 | 📊 Evaluation | two paragraphs, a `bash` block for paths; h3 MAOAM-GLaMM and h3 MAOAM-Sa2VA, each a `bash` block with two commands |
| h2 | Data | one paragraph, a five-column split statistics table with a bold Total row; h3 Download (long `bash` block, a `> **Note…**` blockquote, a three-column upstream source table, an unlabelled layout tree); h3 File schemas with four h4 entries, each a `jsonc` or `python` block |
| h2 | Acknowledgements | two paragraphs (funding, linked base implementations) |
| h2 | Citation | a `bibtex` block, no lead sentence |

Absent from the source: news or changelog, results or benchmark table with scores, demo GIF or embedded video, star-history chart, license section (the license is only a badge), contact section, caption lines under figures.

Present but unusual: a venue logo image sits between the affiliations and the badge row; emoji appear in only four of the eight `##` headings, and the Contents list gives Acknowledgements an emoji (🙏) that its heading does not have; every `##` section is separated by a `---` rule, so each section top shows two grey lines (the rule and the heading's own border); the Capabilities section is one sentence that sends readers to the project page; Citation is the last section and has no lead sentence.

## Components

**Centred title page.** `<div align="center">` with a blank line after it so the inside is Markdown; bold linked authors in an HTML `<p>`; affiliations as a Markdown line; a `<br>` spacer; a 180px logo; a bold venue line; a badge `<p>`; a 92% teaser.

**Middle-dot separators.** `&nbsp;·&nbsp;` between author names and between affiliation entries, so both lines share one rhythm.

**Badge row.** Six flat badges, label #555555, messages #b31b1b twice, #1f6feb, #ffd21e twice and #44bb00. Each `<a>` is spread over three source lines; the line breaks render as single spaces between badges.

**TL;DR blockquote.** One `>` quote outside the div, opening with bold `**TL;DR**` and an em dash, with the two key phrases in bold.

**Contents list.** A bullet list of in-page anchor links, emoji included in the link text (`[✨ Capabilities](#-capabilities)`, `[⚙️ Setup](#%EF%B8%8F-setup)`).

**Section rules.** A `---` line before each `##` heading from Capabilities onward.

**Figure blocks.** `<div align="center"><img src="docs/....png" width="92%" alt="..."></div>`, one per figure, with the explanatory paragraph or table directly after.

**Tables with mixed alignment.** The Set table `|:--|:--:|:--:|:--|` (name left, counts centred, source left); the backbone table `|:-:|:-:|:-:|` (all centred); the Data statistics table `|:--|--:|--:|--:|--:|` (counts right-aligned, every Total cell bold); the source table `|:--|:--|--:|` (size right-aligned). Set and model names in the first column are bold.

**Callout notes.** Plain blockquotes that open with a bold label ending in a period (`> **Hardware.**`, `> **Note on EntitySeg images.**`, `> **Key convention.**`), not GitHub alert syntax.

**Code blocks.** `bash` for commands, with `#` comment lines as group labels and `\` line continuations; unlabelled blocks for directory trees with `├──` characters and `←` or `#` annotations; `jsonc` for schemas with inline comments; `python` for one record example; `bibtex` for the citation. GitHub renders them on its light grey code background with a copy button.

**Check marks in tables.** `&check;` and an en dash `–` in the Demo mode table cells.

**Citation.** An `@inproceedings{park2026maoam, ...}` block with aligned `=` and wrapped author lines, after a final `---`.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| siggraph_logo.png | PNG logo on opaque white | 1000×400 | `<img ... width="180">` | 180×72 | header, between affiliations and venue line |
| teaser.png | PNG figure: photo grid with teal overlays and italic captions | 6588×2675 | `<img ... width="92%">` | 788×320 | header, last element |
| method.png | PNG architecture diagram | 5139×1181 | `<img ... width="92%">` in `<div align="center">` | 788×181 | first element of Architecture and data |
| dataset.png | PNG annotation examples in three groups (RealMat, SynMat, SAMa) | 10785×3518 | `<img ... width="92%">` in `<div align="center">` | 788×257 | Material mask sources, above the Set table |
| vqa_gen.png | PNG pipeline diagram | 1005×569 | `<img ... width="92%">` in `<div align="center">` | 788×446 (scaled up from 1005px source) | VQA generation section |

All figures share the 92% width, so they align with each other and leave a 34px margin on each side of the 856px column. Captions are drawn inside the figures (prompt text under each cell, group labels under brackets), and nothing below them repeats a caption. None uses `<picture>` and the logo and figures are on opaque white, so the README is designed for the light theme only. There are no GIFs or videos.

## Adapting to Other Content

- **A library.** Keep the centred `#` name and the badge row (Docs, PyPI, License), drop authors and the logo, keep the TL;DR blockquote and the linked Contents list, and use `---` between sections.
- **A dataset.** This README's Data section is the model: a split statistics table with right-aligned counts and a bold Total row, a source table with sizes, an unlabelled layout tree and one `jsonc` schema per file.
- **A paper without a venue logo.** Drop the `<br>` spacer and the logo, keep the bold venue line directly above the badges.
- **A repo without a teaser.** End the div at the badge row and let the TL;DR blockquote and Contents list carry the first screen; the method figure at 92% (788px) follows in the first section.
- **A shorter README.** Remove the emoji from the Contents and headings together, so the two always match.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use one separator (`&nbsp;·&nbsp;`) for both author and affiliation lines | Mix commas and dots between names |
| Keep every figure at the same `width="92%"` | Let figures fall back to different natural widths |
| Put a data-source or statistics table directly under the figure it explains | Describe the datasets only in prose |
| Right-align count columns with `--:` and bold the Total row | Centre numbers of different lengths |
| Open callouts with a bold label ending in a period | Use bare "Note:" text that blends into the paragraph |
| Keep emoji consistent between the Contents list and the headings | Give a Contents entry an emoji its heading lacks |
| Give the TL;DR one sentence | Repeat the abstract in the blockquote |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">`: `# Name: Full Paper Title`, a `<p>` of bold linked authors (`<a><b>Name</b></a><sup>n</sup>`) separated by `&nbsp;·&nbsp;` with a `<br>` after the fifth, an affiliation line with the same separator, a `<br>`, a 180px venue logo, a bold venue line, then six flat shields.io badges (label #555555; messages arXiv #b31b1b, Paper ACM DL #b31b1b, Project Page #1f6feb, 🤗 Weights and 🤗 Test data #ffd21e with #333333 text, License #44bb00) and a `width="92%"` teaser with captions drawn inside the image."
2. "After the div, add a one-sentence `> **TL;DR** —` blockquote, a `## Contents` list of anchor links, and `##` sections in this order, each preceded by `---`: Capabilities, Architecture and data, Setup, Demo, Evaluation, Data, Acknowledgements, Citation. Put each figure in `<div align="center">` at `width="92%"` with its table directly under it."
3. "Build tables with explicit alignment: names `:--` and bold, counts `--:` with a bold Total row, sizes `--:`, and use `&check;` for yes cells. Write callouts as blockquotes opening with a bold label ending in a period. Use `bash` for commands with `#` group comments, unlabelled blocks for trees, `jsonc` for schemas and `bibtex` for the final citation."

## Similar Pages

- **readme-letianhuang-transparentgs**: the closest relative, a centred academic header with superscript affiliations, compact flat badges and a teaser that labels itself, but without a logo or contents list.
- **readme-chuan-10-agile**: another SIGGRAPH 2026 README in one centred div with a strong table habit, using heavy for-the-badge tags and a text jump-nav instead of a contents list.
- **readme-eku127-satnav**: a centred title page with one uniform badge family and a full-width teaser; SatNav puts a runnable Quick Start first where MAOAM puts the architecture and data.
- **readme-nvlabs-motionbricks**: also documentation-heavy but with no author block, a left-aligned title and no emoji.

## Quick Start

````markdown
<div align="center">

# Name: Full Paper Title

<p>
  <a href="https://example.org/"><b>Author One</b></a><sup>1</sup>
  &nbsp;·&nbsp;
  <a href="https://example.org/"><b>Author Two</b></a><sup>2</sup>
  <br>
  <a href="https://example.org/"><b>Author Three</b></a><sup>2</sup>
</p>

<sup>1</sup>&nbsp;University A &nbsp;·&nbsp;
<sup>2</sup>&nbsp;Lab B

<br>

<img src="docs/venue_logo.png" width="180" alt="Venue">

**Venue Papers 'YY**

<p>
  <a href="https://arxiv.org/abs/XXXX.XXXXX">
    <img alt="arXiv" src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg">
  </a>
  <a href="https://doi.org/10.XXXX/XXXX">
    <img alt="Paper" src="https://img.shields.io/badge/Paper-ACM%20DL-b31b1b.svg">
  </a>
  <a href="https://example.github.io/project/">
    <img alt="Project page" src="https://img.shields.io/badge/Project-Page-1f6feb.svg">
  </a>
  <a href="https://huggingface.co/org/ckpts">
    <img alt="Weights" src="https://img.shields.io/badge/%F0%9F%A4%97-Weights-ffd21e.svg">
  </a>
  <a href="https://huggingface.co/datasets/org/data">
    <img alt="Test data" src="https://img.shields.io/badge/%F0%9F%A4%97-Test%20data-ffd21e.svg">
  </a>
  <a href="LICENSE">
    <img alt="License" src="https://img.shields.io/badge/License-Name-brightgreen.svg">
  </a>
</p>

<img src="docs/teaser.png" width="92%" alt="Name teaser">

</div>

<br>

> **TL;DR** — Name is a model that does **X** from **Y**.

## Contents

- [✨ Capabilities](#-capabilities)
- [🧠 Architecture and data](#-architecture-and-data)
- [⚙️ Setup](#%EF%B8%8F-setup)
- [Citation](#citation)

---

## ✨ Capabilities

---

## 🧠 Architecture and data

<div align="center">
<img src="docs/method.png" width="92%" alt="Architecture">
</div>

| Set | Masks | Images | Source |
|:--|:--:|:--:|:--|
| **SetA** | ~0K | ~0K | Where it comes from. |

---

## ⚙️ Setup

> **Hardware.** One sentence on the GPU requirement.

```bash
uv sync
```

---

## Data

| Split | Pairs | Images |
|:--|--:|--:|
| **A** | 0 | 0 |
| **Total** | **0** | **0** |

---

## Citation

```bibtex
@inproceedings{key,
  title     = {...},
}
```
````

## Provenance

- Repo: https://github.com/adobe-research/obj-and-mat-selection (`README.md`, branch `master`, last README commit 004caf2 on 2026-07-29).
- Paper: "MAOAM: Unified Object and Material Selection with Vision-Language Models", SIGGRAPH 2026 Conference Papers, DOI 10.1145/3799902.3811186, arXiv 2606.04880; first author Jaden Park. Project page https://jadenpark0.github.io/project_pages/maoam/.
- Selection: a venue logo and badge row over a labeled teaser, a one-line TL;DR blockquote, a short linked contents list, and a data-sources table under the figure, so the README works as a compact paper companion.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the six badge URLs, the logo and four figure PNGs fetched from the repo for pixel sizes and the sampled overlay color.
- Written 2026-10-28.
