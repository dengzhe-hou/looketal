# AGILE — README Reference

> A lab bench under bright light: a five-letter name, a strip of heavy uppercase tags, then a contact sheet of hands gripping scissors, mugs and controllers.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/Chuan-10/AGILE (last commit touching the file 4b0d0cd, 2026-10-16; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; the teaser size and its accent colors come from `assets/teaser.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The whole header is one `<div align="center">` written mostly in plain Markdown, so the top of the page reads as a short centred stack. A one-word `#` title "AGILE" with GitHub's grey rule sits over a `###` subtitle that carries the full paper title without a rule. Directly under the subtitle comes a single row of four `for-the-badge` shields (28px tall, uppercase), then a Markdown jump-nav of four text links joined by ` · `, a one-line author list with superscript marks, an affiliation line, an equal-contribution note and a bold venue line. The teaser, a 2×6 contact sheet of video frames over reconstructed hands and objects, fills the rest of the first screen at full width. Below the fold the body is ordinary GitHub prose in eleven plain `##` sections with no emoji: dated News bullets, a two-sentence Overview, bold-led Highlights, a three-column Modules table, a Code and Data section, a small right-aligned results table, a numbered Getting Started, a TODO checklist, License, Citation and Acknowledgements.

## Header Block

Everything down to the teaser sits inside `<div align="center">`, so even the Markdown paragraphs are centred. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈24 with its "README.md" file bar; content starts at y≈90).

1. **Title** (y≈139): `# AGILE`. GitHub h1, 2em (32px), weight 600, with a 1px grey rule under it across the 856px content width.
2. **Subtitle** (y≈206): `### Hand-Object Interaction Reconstruction from Video via Agentic Generation`. GitHub h3, 1.25em (20px), weight 600, no rule. It is a real heading, so it also appears in GitHub's outline menu.
3. **Badge row** (y≈234–262): `<p>` holding four `<a><img src="https://img.shields.io/badge/...?style=for-the-badge"></a>` lines. Each badge is 28px tall; with the single spaces between tags the row spans about 620px. Details in Badges.
4. **Jump-nav** (y≈296): a Markdown line, `[Prepared data](...) · [Generated objects](...) · [Optimized results](...) · [Installation](docs/installation.md)`. Four body-size links in GitHub link blue separated by a middle dot; the first three point into the Hugging Face dataset tree, the last to a repo doc.
5. **Authors** (y≈336): one Markdown line of nine names, three of them linked (`[Jin-Chuan Shi](https://chuan-10.github.io/)<sup>1\*</sup>`), the rest plain text, all separated by `, ` and each followed by `<sup>` marks. The asterisk is escaped (`\*`) so Markdown does not read it as emphasis. The line fits on one row at 856px.
6. **Affiliations** (y≈376): `<sup>1</sup>State Key Lab of CAD & CG, Zhejiang University &nbsp; <sup>2</sup>Zhejiang University of Technology`. Plain text, one non-breaking space between entries.
7. **Contribution note** (y≈416): `<sup>\*</sup>Equal contribution`, its own paragraph.
8. **Venue line** (y≈456): `**ACM SIGGRAPH 2026, Conference Track**`. Body size, bold, no link and no badge. It comes after the authors, not before.
9. **Teaser** (y≈486 to 828): `<img src="assets/teaser.png" width="100%">`, no `alt`, no link, no caption. The 2350×940 PNG renders at 856×342. The `</div>` follows and the `## News` heading starts at y≈872, still inside the first screen.

## Badges

All four use the static path form with `?style=for-the-badge`, so shields.io renders them 28px tall with square corners, no gloss, and both label and message set in bold uppercase with wide letter spacing (shields.io rewrites "Project" to "PROJECT"). The label is on the default #555555 grey; message text is white (#ffffff) except on the yellow badge, where shields.io picks #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| PROJECT | PAGE | #007ec6 (`blue`, label #555555) | for-the-badge | agile-hoi.github.io |
| ARXIV (white arXiv logo before the label) | 2602.04672 | #b31b1b (label #555555) | for-the-badge, `logo=arxiv` | arxiv.org/abs/2602.04672 |
| PAPER | PDF | #67ac09 (`green` as shields.io now draws it, label #555555) | for-the-badge | arxiv.org/pdf/2602.04672 |
| HUGGING FACE | DATA | #ffd21e (label #555555, message text #333333) | for-the-badge | huggingface.co/datasets/Chrisss/AGILE |
| (link row) | Prepared data · Generated objects · Optimized results · Installation | GitHub link blue | plain Markdown links, not bold | Hugging Face dataset folders, docs/installation.md |

Badge widths from the SVGs: 135.75, 181.75, 112 and 177px. The `green` keyword renders as #67ac09 in the SVG that shields.io serves today, not the older #97ca00. Two badges point at the same arXiv paper (abstract and PDF), and the `alt` texts are short nouns ("Project Page", "arXiv", "Paper", "Hugging Face Data").

Other colored marks on the page come from the teaser, not from badges: a pale blue halo around each reconstructed hand and object (median sampled value about #b1ceef), dark rounded photo tiles, and a deep red mug (about #992035) as the strongest accent on a white #ffffff background.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | AGILE | title only |
| h3 (centred) | Hand-Object Interaction Reconstruction from Video via Agentic Generation | subtitle; badges, jump-nav, authors, affiliations, contribution note, venue and teaser follow without a heading |
| h2 | News | three bullets, each led by a bold bracketed date (`**[2026.10]**`) |
| h2 | Overview | one paragraph with the method name and the output in bold |
| h2 | Highlights | four bullets, each opening with a bold sentence that ends in a period ("**Generate, review and refine.**") |
| h2 | Modules | one lead paragraph, then a three-column table Module / What it does / Outputs with five rows, each module name linked to its folder README |
| h2 | Code and Data | three paragraphs with bold release counts (18 sequences), links to data docs and the manifest |
| h2 | HO3D Results | a six-column table with arrows in the headers, two rows (paper and released code), then a paragraph on protocol differences |
| h2 | Getting Started | one sentence, a two-line `bash` block, a numbered list of three steps with an indented `bash` block in step 2, then three paragraphs of further routes |
| h2 | TODO | eight task-list items, four checked and four open |
| h2 | License | two paragraphs, non-commercial terms in bold |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | Acknowledgements | one sentence of seven linked project names |

Absent from the source: demo GIF or embedded video, table of contents, separate Installation section (it is a linked doc), model zoo table, contact section, star-history chart, emoji in headings, a caption under the teaser.

Present but unusual: the subtitle is an `###` heading rather than bold text, so it is large but unruled; the badge row comes before the authors, which pushes the paper metadata below the links; the jump-nav points into Hugging Face folders rather than to sections of the README; the results table puts the paper's numbers and the released code's numbers side by side, with the paper row linking to its arXiv table anchor; the clone command in Getting Started uses `aim-uofa/AGILE`, a different owner from the repo this README lives in; License comes before Citation.

## Components

**Centred Markdown block.** One `<div align="center">` with a blank line after the opening tag, so everything inside is parsed as Markdown and centred: headings, link lines, author line and image. Only the badge row uses an inner HTML `<p>`.

**Badge row.** Four `<a href="..."><img src="https://img.shields.io/badge/Label-Message-HEX?style=for-the-badge" alt="..."></a>` on separate source lines inside `<p>`. Label #555555 throughout; messages #007ec6, #b31b1b, #67ac09, #ffd21e. Only the arXiv badge carries a logo.

**Dot-separated link line.** Plain Markdown links joined by ` · ` (space, middle dot, space). Used once, as the header jump-nav.

**News list.** Bullets of the form `- **[YYYY.MM]** Sentence ending in "!"`, newest first, month precision, venue name bold inside the sentence.

**Bold-lead bullets.** Highlights bullets open with a bold imperative sentence ending in a period, then two or three plain sentences.

**Modules table.** Pipe table with `| --- | --- | --- |` delimiters and no alignment colons, so GitHub centres the header cells and left-aligns the body. Column one is a linked module name (`[Preprocessing](preprocessing/README.md)`); column two is two or three sentences of what it does; column three lists the outputs as a noun phrase ending in a period. GitHub stripes alternate rows.

**Results table.** First column left-aligned (`| --- |`), five numeric columns right-aligned (`| ---: |`). Header cells carry the unit and a direction arrow ("MPJPE (mm) ↓", "F@5 (%) ↑"). No bold best values; the two rows are a reference and a reproduction, not a ranking. A paragraph under the table states the averaging and protocol differences.

**Numbered steps with nested code.** `1.`, `2.`, `3.` list items; step 2 holds a `bash` block indented three spaces so it stays inside the list item.

**Code blocks.** Fenced with `bash` for commands and `bibtex` for the citation. GitHub renders them on its light grey code background with a copy button.

**Task list.** `- [x]` and `- [ ]` items under TODO, rendered by GitHub as disabled checkboxes.

**Citation.** One sentence "If you find this work useful, please consider citing:" then an `@article{shi2026agile, ...}` block with the arXiv preprint as the journal.

**License and acknowledgements.** Prose with inline links; the license names a contact person for commercial use. No badges or logos.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.png | PNG (RGBA, opaque white background), 2×6 grid of video frames over reconstructed hand-object renders | 2350×940 | `<img src="assets/teaser.png" width="100%">` inside the centred div | 856×342 | last element of the header, no caption |

The teaser is the only image in the README. It is split into four blocks of three frames (scissors, game controller, mug, pen); each block shows dark-cornered photo tiles on top and the reconstructed hand and object below, outlined by a pale blue halo and grounded by a soft grey shadow on white. Because the background is opaque white and the shadows are drawn for white, it is designed for the light theme only. There is no `<picture>` switch, no GIF and no video link in the README itself.

## Adapting to Other Content

- **A library.** Keep `#` name, `###` one-line description and the single for-the-badge row (Docs, PyPI, License), drop authors and venue, and turn the jump-nav into links to Install, API and Examples. Replace the Modules table's Outputs column with "Entry point".
- **A dataset.** Keep the full header; make the jump-nav point at the download folders as AGILE does, keep the teaser at `width="100%"` (856px) as a sample grid, and move Code and Data up to follow News.
- **A benchmark with scores.** Keep the results table form (left-aligned first column, right-aligned numeric columns, unit and arrow in each header) and add more method rows; if rows compete, bold the best value, which AGILE does not need.
- **A repo without a teaser.** Let the venue line close the centred div and promote the Modules table so it is the first thing under Overview.
- **A multi-part toolkit.** The Modules table scales: one row per folder, each linked to its own README, with "What it does" in two or three sentences and "Outputs" as file types.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Wrap the header in one `<div align="center">` and write the inside in Markdown | Mix centred and left-aligned paragraphs inside the header |
| Keep all badges in `for-the-badge` with the label on #555555 | Add a flat or logo-only badge to the same row |
| Use one ` · ` jump-nav line for the most-used destinations | Repeat the badge destinations in the jump-nav |
| Give each module a row with a link, a purpose and its outputs | Describe modules only in prose |
| Put unit and direction arrow in every numeric column header and right-align with `---:` | Leave units in the caption or mix alignments |
| Separate a paper reference row from the released-code row and say why they differ | Present reproduced numbers as the paper's |
| Escape `*` in author marks (`<sup>1\*</sup>`) | Let a bare `*` turn the author line italic |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">` using Markdown: `# Name`, `### Full paper title`, then a `<p>` with four shields.io badges in `style=for-the-badge` (label #555555; messages PROJECT PAGE #007ec6, ARXIV with `logo=arxiv` #b31b1b, PAPER PDF #67ac09, HUGGING FACE DATA #ffd21e with #333333 text), a jump-nav line of four Markdown links joined by ` · `, a one-line author list with `<sup>` marks and escaped `\*`, an affiliation line separated by `&nbsp;`, an equal-contribution note, a bold venue line, and a `width="100%"` teaser with no caption."
2. "After the header, write plain `##` sections in this order: News, Overview, Highlights, Modules, Code and Data, Results, Getting Started, TODO, License, Citation, Acknowledgements. News bullets start with `**[YYYY.MM]**`. Highlights bullets start with a bold sentence ending in a period. No emoji in headings."
3. "Build a Modules table with three columns (Module, What it does, Outputs), `| --- |` delimiters, each module name linked to its folder README. Build the results table with the first column `| --- |` and numeric columns `| ---: |`, putting unit and ↓ or ↑ in each header, one paper reference row and one released-code row, and a protocol paragraph under it."

## Similar Pages

- **readme-eku127-satnav**: also a centred paper header with a full-width teaser, but SatNav uses an `<h2>` subtitle with a rule, flat 20px badges and a bilingual toggle, where AGILE uses an unruled `###` and heavy for-the-badge tags.
- **readme-letianhuang-transparentgs**: same SIGGRAPH graphics context and a centred header, but TransparentGS puts the full paper title in the h1, uses flat badges after a long affiliation block, and labels its teaser inside the image.
- **readme-adobe-research-obj-and-mat-selection**: shares the single centred div, a 92% teaser and a strong table habit, but adds a venue logo and a linked contents list.
- **readme-nvlabs-motionbricks**: also documentation-first with a folder-to-purpose table; MotionBricks drops the author block entirely and left-aligns its title.

## Quick Start

````markdown
<div align="center">

# ProjectName

### Full Paper Title on One Line

<p>
  <a href="https://example.github.io/project"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge" alt="Project Page"></a>
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?style=for-the-badge&logo=arxiv" alt="arXiv"></a>
  <a href="https://arxiv.org/pdf/XXXX.XXXXX"><img src="https://img.shields.io/badge/Paper-PDF-green?style=for-the-badge" alt="Paper"></a>
  <a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/badge/Hugging%20Face-Data-FFD21E?style=for-the-badge" alt="Hugging Face Data"></a>
</p>

[Prepared data](https://huggingface.co/datasets/org/name/tree/main/a) · [Generated assets](https://huggingface.co/datasets/org/name/tree/main/b) · [Results](https://huggingface.co/datasets/org/name/tree/main/c) · [Installation](docs/installation.md)

[Author One](https://example.org/)<sup>1\*</sup>, Author Two<sup>1\*</sup>, Author Three<sup>1</sup>, [Author Four](https://example.org/)<sup>1,2</sup>

<sup>1</sup>Institution A &nbsp; <sup>2</sup>Institution B

<sup>\*</sup>Equal contribution

**Venue Year, Track**

<img src="assets/teaser.png" width="100%">

</div>

## News

- **[YYYY.MM]** Code and data released!
- **[YYYY.MM]** Accepted to **Venue Year**!

## Overview

**ProjectName** turns X into **Y**. One more sentence.

## Highlights

- **First idea in one sentence.** Two plain sentences.
- **Second idea in one sentence.** Two plain sentences.

## Modules

One lead sentence.

| Module | What it does | Outputs |
| --- | --- | --- |
| [Module](module/README.md) | Two sentences. | Output types. |

## Code and Data

Paragraph with **bold release counts**.

## Results

| Result | Metric A (unit) ↓ | Metric B (%) ↑ |
| --- | ---: | ---: |
| [Paper, Table 1](https://arxiv.org/abs/XXXX.XXXXX) | 0.00 | 00.00 |
| Released code and data | 0.00 | 00.00 |

One paragraph on protocol differences.

## Getting Started

```bash
git clone https://github.com/org/name.git
cd name
```

1. Follow the [installation guide](docs/installation.md).
2. Download a prepared sample:

   ```bash
   python tools/download.py --output /ABS/data
   ```

3. Follow the [guide](docs/run.md).

## TODO

- [x] Released item.
- [ ] Planned item.

## License

## Citation

If you find this work useful, please consider citing:

```bibtex
@article{key,
  title={...},
}
```

## Acknowledgements
````

## Provenance

- Repo: https://github.com/Chuan-10/AGILE (`README.md`, branch `main`, last README commit 4b0d0cd on 2026-10-16).
- Paper: "AGILE: Hand-Object Interaction Reconstruction from Video via Agentic Generation", ACM SIGGRAPH 2026 Conference Track, arXiv 2602.04672; first author Jin-Chuan Shi. Project page https://agile-hoi.github.io.
- Selection: a short title over a subtitle, uniform for-the-badge links plus a text jump-nav, a clean photo-grid teaser, and a three-column Modules table (what it does and its outputs) that reads like real documentation.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `assets/teaser.png` fetched from the repo for pixel size and sampled colors.
- Written 2026-10-28.
