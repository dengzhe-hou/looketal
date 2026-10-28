# StudioRecon — README Reference

> A quiet studio contact sheet: a small centred nameplate, four thin tags, one wide reconstruction still, then a pipeline drawing pinned above a five-row stage table.

**Theme:** light

Read from `README.md` on the default branch `master` of github.com/sisyphm/StudioRecon (last commit touching the file add194a, 2026-07-28; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the badge URLs; image sizes and the teaser's accent color come from `assets/teaser.png` and `assets/pipeline.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The header is written almost entirely in Markdown inside one `<div align="center">`, so it looks like ordinary GitHub headings and paragraphs that happen to be centred. A ruled `# StudioRecon` sits over an unruled `###` subtitle, a bold venue line, an author line joined by spaced middle dots, an affiliation line and one row of four small flat badges. Below them a 95%-wide teaser figure (four low-overlap input videos on the left, the reconstructed room with camera frustums on the right, an enhanced filmstrip across the bottom) takes the rest of the first screen. After a three-line summary with one bold phrase, the body is short and plain: How It Works (a paragraph, a full-width pipeline figure and a five-row stage table), Setup, Quick Start (five small `bash` blocks), Rendering (a trajectory table), Documentation (a doc-link table), Citation and License. There is no emoji, no news list and no `<details>` block.

## Header Block

All header elements are inside `<div align="center">` ... `</div>` with blank lines around the Markdown, which lets GitHub parse the Markdown inside the HTML block. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈138, rule at about 168): `# StudioRecon`. GitHub h1, 2em (32px), weight 600, centred by the wrapping `<div>`, with the 1px grey rule across the full 856px content width.
2. **Subtitle** (y≈207): `### 4D Human-Scene Reconstruction from Low-Overlap Captures`. GitHub h3, 1.25em (20px), weight 600, no rule. Choosing h3 instead of h2 keeps the subtitle visibly subordinate and free of a second rule.
3. **Venue** (y≈246): `**SIGGRAPH Conference Papers '26**`. Body size, bold, unlinked.
4. **Authors** (y≈286): `[Minhyuk Hwang](https://github.com/sisyphm)\* &nbsp;·&nbsp; Sangmin Kim\* &nbsp;·&nbsp; Seunguk Do &nbsp;·&nbsp; Daneul Kim &nbsp;·&nbsp; Jaesik Park`. Only the first author is a link (GitHub link blue); the rest are plain text. `\*` escapes the asterisk for equal contribution.
5. **Affiliation** (y≈326): `Seoul National University &nbsp;·&nbsp; \*equal contribution`. One line that carries both the single affiliation and the footnote for the asterisk.
6. **Badge row** (y≈353 to 373): four Markdown image links, `[![arXiv](https://img.shields.io/badge/arXiv-2607.09125-b31b1b)](https://arxiv.org/abs/2607.09125)` and so on, one per source line. They render in one paragraph separated by single spaces; each badge is 20px tall and the row is about 560px wide (116 + 86 + 194 + 154 px plus gaps). Details in Badges.
7. **Teaser** (y≈400 to about 946, crossing the fold): `<img src="assets/teaser.png" width="95%">`. The 1217×818 PNG renders at 813×546, centred, so a 21px margin shows on each side of the 856px column. The image has no caption line and no `alt` text; its own labels ("Low-overlap 4 Input Videos", "Initial Reconstruction", "Our Enhanced Result", "Novel View Rendering") are set in serif type inside the PNG.
8. **Summary** (after `</div>`, below the fold): three source lines that render as one left-aligned paragraph, "Given as few as **four sparse, low-overlap videos**, StudioRecon reconstructs ...". Only the key phrase is bold.

## Badges

All four use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` with no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, rounded corners, label on #555555, Verdana 11px. Message text is white (#ffffff) except on the yellow DOI badge, where shields.io switches it to #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2607.09125 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2607.09125 |
| Project | Page | #1a73e8 (label #555555) | flat (default) | sisyphm.github.io/studiorecon-page/ |
| DOI | 10.1145/3799902.3811165 | #fbbc04 (label #555555, message text #333333) | flat (default) | doi.org/10.1145/3799902.3811165 |
| License | Non-Commercial | `green`, served as #67ac09 (label #555555) | flat (default) | LICENSE.md in the repo |

Three colors are given as hex in the URL; the License badge uses the named color `green`, and the SVG that shields.io returns for it fills the message with #67ac09. The Project Page blue #1a73e8 and DOI yellow #fbbc04 are Google's brand blue and yellow, which with arXiv red and the green license badge gives the row four distinct hues of similar weight.

Other colors on the page: the first-author link and body links are GitHub link blue #0969da. The teaser's "Novel View Rendering" arrow, label and the left end of the filmstrip frame are a soft violet, sampled at #d59add in the PNG; the frame fades to a pale blue-green on the right (inferred from the capture, not sampled).

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | StudioRecon | title |
| h3 (centred) | 4D Human-Scene Reconstruction from Low-Overlap Captures | subtitle; venue, authors, affiliation, badges and teaser follow without a heading, then the summary paragraph after the `</div>` |
| h2 | How It Works | one paragraph, a centred full-width pipeline figure, a two-column Stage / What happens table with five rows, a sentence on default enhancement settings |
| h2 | Setup | a three-line `bash` block (recursive clone, bootstrap script) and one paragraph linking `docs/INSTALL.md` and `docs/CHECKPOINTS.md` |
| h2 | Quick Start | five short `bash` blocks, each introduced by one sentence (prepare a scene, run the pipeline, dry run, single stage, split Gaussian training) |
| h2 | Rendering | one paragraph, a multi-line `bash` block, a paragraph on conda environments, a two-column Trajectory / Camera motion table with seven rows, two closing paragraphs on scale and output paths |
| h2 | Documentation | a two-column table with an empty header row linking six docs, and a one-sentence scope note |
| h2 | Citation | a `bibtex` block with no lead sentence |
| h2 | License | one paragraph |

Absent from the source: logo, news or changelog, results table with numbers, demo GIF or embedded video, model zoo table, table of contents, acknowledgements section, `<details>` blocks, emoji anywhere.

Present but unusual: the subtitle is an h3 so it has no rule; the affiliation line also defines the equal-contribution mark; only one of five authors is linked; the teaser has `width="95%"` rather than 100% and no caption or alt text; the Documentation table has an empty header row (`| | |`), which GitHub still renders as an empty `<thead>` row above the first link row.

## Components

**Markdown inside a centred div.** `<div align="center">`, a blank line, Markdown headings and paragraphs separated by blank lines, the teaser `<img>`, a blank line, `</div>`. No `<p align>` tags and no `<br>`; spacing comes from GitHub's heading and paragraph margins.

**Spaced dot separator.** `&nbsp;·&nbsp;` between authors and between the affiliation and the footnote, giving a wider gap around each dot than a plain `·`.

**Flat badge row.** Four `[![Label](https://img.shields.io/badge/Label-Message-HEX)](url)` lines in Markdown, label grey #555555, messages #b31b1b, #1a73e8, #fbbc04, #67ac09. The alt text is the label word.

**Figure plus stage table.** In How It Works, `<div align="center"><img src="assets/pipeline.png" width="100%"></div>` is followed directly by a `| Stage | What happens |` table with `| --- | --- |` delimiters. The Stage cell is bold and numbered (`**1. Sparse-to-dense view synthesis**`) to match the stage labels in the figure; the What happens cell is one comma-separated line of component names (SAM3, Pi3, GEN3C, CoMotion, DWPose, NLF, DiFiX). GitHub left-aligns body cells and stripes alternate rows.

**Lead sentence plus block.** Quick Start pairs one plain sentence ("Then run the pipeline:") with one `bash` block, repeated five times. Long commands break across lines with trailing ` \`.

**Option table.** Rendering's `| Trajectory | Camera motion |` table puts the CLI value in inline code in the first column (`` `orbit` ``, `` `static-orbit` ``) and one sentence in the second.

**Doc table.** `| | |` header, `| --- | --- |`, then rows of `` [`docs/INSTALL.md`](docs/INSTALL.md) | one-line description ``. The link text is the file path in inline code.

**Citation.** A bare `bibtex` block, `@inproceedings{hwang2026studiorecon, ...}` with `=` aligned, a wrapped author list, and `doi`, `eprint` and `archivePrefix` fields.

**License line.** One paragraph with a link to `LICENSE.md` and inline-code doc paths; no badge besides the one in the header.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.png | PNG composite: input thumbnails, reconstructed room with camera frustums, enhanced filmstrip; serif labels | 1217×818 | `<img src="assets/teaser.png" width="95%">` inside the header `<div align="center">` | 813×546 | header, after the badges; no caption |
| pipeline.png | PNG method diagram on white with light grey panels, pink and blue accents, "(Sec 3.x)" references | 1600×606 | `<img src="assets/pipeline.png" width="100%">` in `<div align="center">` | 856×324 | How It Works, after the first paragraph and before the stage table |

Both images are paper figures on white, designed for the light theme. The teaser's violet #d59add accent marks the novel-view path and the enhanced result. No GIF, no video and no `<picture>` dark variant.

## Adapting to Other Content

- **A library.** Keep the div-wrapped `#` name and `###` one-line description, drop venue and authors, keep a four-badge flat row (Docs, PyPI, License, CI), and replace the teaser with a short code example; keep the How It Works figure-plus-table if the library has stages.
- **A dataset.** Keep the full header with the teaser as a sample composite at `width="95%"` (813px), and turn How It Works into a collection pipeline figure with a Stage / What happens table; make the Documentation table the place for format specs.
- **A benchmark with scores.** Add a Results section after How It Works with a pipe table, numeric columns right-aligned (`| ---: |`) and the best value in bold; StudioRecon has no such table, so this is an extension.
- **A repo without a teaser.** Let the badge row close the header `<div>` and move the pipeline figure up so it sits directly under the summary paragraph at `width="100%"` (856px).
- **A repo with several authors' affiliations.** Add `<sup>` numbers to names and list affiliations on the affiliation line with the same `&nbsp;·&nbsp;` separator, keeping the footnote last.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Wrap Markdown header lines in one `<div align="center">` with blank lines inside | Mix `<p align>` blocks and Markdown in the same header |
| Use `###` for the subtitle so only the title carries a rule | Stack two ruled headings on top of each other |
| Keep four flat badges with the default #555555 label | Add `for-the-badge` badges to a header this quiet |
| Pair the pipeline figure with a numbered Stage / What happens table | Leave a method figure without any text that maps it to the code |
| Introduce each `bash` block with one plain sentence | Put five commands in one block with no explanation |
| Give the teaser alt text and, if needed, a one-line caption | Leave the teaser without alt text (StudioRecon does) |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside `<div align="center">` with blank lines: `# ProjectName`, `### Full paper title`, a bold venue line, an author line joined by `&nbsp;·&nbsp;` with `\*` for equal contribution, an affiliation line ending in `&nbsp;·&nbsp; \*equal contribution`, four flat shields.io badges as Markdown image links (label #555555; messages arXiv #b31b1b, Project Page #1a73e8, DOI #fbbc04, License green #67ac09), and `<img src="assets/teaser.png" width="95%">`."
2. "After the header, write a one-paragraph summary with one bold phrase, then `##` sections in this order: How It Works, Setup, Quick Start, Rendering, Documentation, Citation, License. No emoji and no news list."
3. "In How It Works, put a centred `width="100%"` pipeline figure directly above a `| Stage | What happens |` table whose first column is bold and numbered (`**1. Stage name**`). In Quick Start, introduce each `bash` block with one plain sentence. End with a bare `bibtex` block."

## Similar Pages

- readme-eku127-satnav shares the quiet centred header with one flat badge row and a full-width teaser, but uses `<p align>` HTML blocks and an h2 subtitle where StudioRecon uses Markdown in a `<div>` and an h3.
- readme-deepmancer-hairport has the same figure-then-stage-table idea in its Pipeline Stages section, inside a louder header with `for-the-badge` badges and a news list.
- readme-vveicao-freeorbit4d is another SIGGRAPH 2026 4D reconstruction README, but shows results as HTML tables of GIFs instead of one composite teaser.

## Quick Start

````markdown
<div align="center">

# ProjectName

### Full Paper Title

**Venue Year**

[Author One](https://example.org/)\* &nbsp;·&nbsp; Author Two\* &nbsp;·&nbsp; Author Three

Institution &nbsp;·&nbsp; \*equal contribution

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b)](https://arxiv.org/abs/XXXX.XXXXX)
[![Project Page](https://img.shields.io/badge/Project-Page-1a73e8)](https://example.github.io/project/)
[![DOI](https://img.shields.io/badge/DOI-10.XXXX%2FXXXX-fbbc04)](https://doi.org/10.XXXX/XXXX)
[![License](https://img.shields.io/badge/License-Non--Commercial-green)](LICENSE.md)

<img src="assets/teaser.png" width="95%" alt="Describe the teaser.">

</div>

Given **the key input**, ProjectName does one thing, then another.

## How It Works

One paragraph on the idea.

<div align="center">
<img src="assets/pipeline.png" width="100%">
</div>

| Stage | What happens |
| --- | --- |
| **1. Stage name** | Components used in this stage |
| **2. Stage name** | Components used in this stage |

## Setup

```bash
git clone --recursive https://github.com/org/name.git
cd name
```

## Quick Start

One sentence:

```bash
bash scripts/run.sh --config configs/example.yaml
```

## Rendering

| Option | Effect |
| --- | --- |
| `value` | One sentence. |

## Documentation

| | |
| --- | --- |
| [`docs/INSTALL.md`](docs/INSTALL.md) | What it covers |

## Citation

```bibtex
@inproceedings{key,
  title     = {...},
}
```

## License
````

## Provenance

- Repo: https://github.com/sisyphm/StudioRecon (`README.md`, branch `master`, last README commit add194a on 2026-07-28).
- Paper: "4D Human-Scene Reconstruction from Low-Overlap Captures", SIGGRAPH Conference Papers '26 (SIGGRAPH 2026), arXiv 2607.09125, DOI 10.1145/3799902.3811165; first author Minhyuk Hwang. Project page https://sisyphm.github.io/studiorecon-page/.
- Selection: a restrained centred header with a one-sentence summary under the teaser, then a How It Works pipeline figure paired with a tidy stage table that connects the method to the code without any emoji. The summary is plain text with one bold phrase rather than a fully bold sentence.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `assets/teaser.png` and `assets/pipeline.png` fetched from the repo for pixel sizes and the violet accent.
- Written 2026-10-28.
