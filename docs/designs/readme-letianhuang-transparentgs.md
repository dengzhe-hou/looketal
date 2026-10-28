# TransparentGS — README Reference

> A journal title page dropped onto a playroom: a bold two-line title, a tidy block of names and labs, four small tags, then a sunlit room whose glass objects are tagged like museum exhibits.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/LetianHuang/transparentgs (last commit touching the file 4720083, 2026-04-20; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; image sizes and the teaser's label colors come from the image files fetched from their URLs. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README opens as a compact academic title page. A centred `<h1>` wrapped in `<strong>` carries the full paper title over two lines with GitHub's grey rule under it, and a centred `<h3>` gives the venue on two lines ("SIGGRAPH 2025" over "(ACM Transactions on Graphics)"). Ten linked author names follow in two rows with superscript affiliation numbers, then four affiliation lines stacked by `<br>`, then one tight row of four flat 20px badges. The teaser is a large photograph of a playroom whose transparent, glossy and diffuse objects carry in-image labels in translucent red and teal boxes; it is wider than tall and runs past the fold. After it the body moves quickly through News, TL;DR, Overview with a pipeline figure, Citation and a TODO checklist before turning into a long, task-oriented manual for the viewer (install, scene assets, two run steps, a GUI tutorial with many screenshots), followed by Dataset, Segmentation, Training and Acknowledgements.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈24 with its "README.md" file bar; content starts at y≈90).

1. **Opening wrapper**: `<p align="center">` on the first line. HTML does not allow a heading inside `<p>`, so GitHub's output closes it immediately as an empty paragraph, and the matching `</p>` after the badge div closes nothing. The wrapper has no visible effect; each element below carries its own alignment.
2. **Title** (y≈139–180, two lines): `<h1 align="center"><strong>TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians</strong></h1>`. GitHub h1, 2em (32px); the `<strong>` raises it from weight 600 to bold. The grey rule sits under the second line at y≈208, across the 856px content width.
3. **Venue** (y≈246 and 272): `<h3 align="center">SIGGRAPH 2025 <br> (ACM Transactions on Graphics)</h3>`. GitHub h3, 1.25em (20px), no rule; the `<br>` puts the journal on its own line.
4. **Authors** (y≈311 and 335): one `<p align="center">` holding ten `<span class="author-block">` groups pasted from a project page. GitHub strips the `class`, so the spans are plain inline wrappers. Each name is `<a href>` plus `<sup>n</sup>` and five `&nbsp;`, which makes the wide gaps between names; a `<br>` after the fifth name splits the list into rows of five. The last author's mark is `<sup>* 1</sup>`, rendered as "* 1" with a space, and the README never defines `*` (corresponding author by convention, inferred).
5. **Affiliations** (y≈359–431): in the same `<p>`, after a `<br>`, four `<span><sup>n</sup>Lab, University</span><br>` lines, one per row, so the block is a narrow centred column.
6. **Badge row** (y≈468–488): `<div align="center">` holding four `<a><img src="https://img.shields.io/badge/..."></a>` lines. Each badge is 20px tall and the row spans about 538px. One `href` is unquoted (`<a href=https://arxiv.org/abs/2504.18768>`); GitHub still renders it. Details in Badges.
7. **Teaser** (y≈500 onward, past the fold): `![teaser](https://github.com/LetianHuang/LetianHuang.github.io/blob/main/assets/img/transparent_teaser.png)`, a plain Markdown image pointing at another repo's `blob` URL, which GitHub rewrites to `raw`. No width is set, so the 3819×2546 PNG scales to 856×571 by GitHub's `max-width: 100%`, and about 400px of it is visible in the first screen. No caption.

## Badges

All four use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 grey and white (#ffffff) text with a #010101 text shadow.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| DOI | 10.1145/3730892 | #007ec6 (`blue`, label #555555) | flat (default) | doi.org/10.1145/3730892 |
| arXiv | 2504.18768 | #b31b1b (label #555555) | flat (default), `.svg` suffix | arxiv.org/abs/2504.18768 |
| Project | Page | #44bb00 (`Green` as shields.io now draws it, label #555555) | flat (default) | letianhuang.github.io/transparentgs |
| YouTube (white YouTube logo) | SIGGRAPH Trailer | #dd4343 (`red` as shields.io now draws it, label #555555) | flat, `logo=youtube&logoColor=white` | youtube.com/watch?v=HfHC0wNYry8&t=130s |

Badge widths from the SVGs: 140, 116, 86 and 183px. The capitalised `Green` and the named `red` render today as #44bb00 and #dd4343 in the served SVGs, not the older #97ca00 and #e05d44. None of the badges has an `alt` attribute, and the DOI badge comes first, which puts the published version ahead of the preprint.

Other colored marks on the first screen come from the teaser, not from badges: translucent red label boxes (median sampled fill about #ee6c65) for the transparent and glossy objects, and translucent teal boxes (about #5fabbc) for the material-editing example, with small red and teal dots marking the labelled points; text in the boxes is white small caps. The pipeline figure uses pale green, grey and light blue panels on a #f2f2f2 background.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians | title; venue, authors, affiliations, badges and teaser follow |
| h3 (centred) | SIGGRAPH 2025 (ACM Transactions on Graphics) | venue only |
| h2 | News | two bold-dated paragraphs (`**[2025.08.04]**`), each with one emoji (🎈 and a GitHub emoji `<img>` for :smile:) |
| h2 | TL;DR | one paragraph naming the three contributions |
| h2 | Overview | one paragraph with in-text citations, then the pipeline PNG |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | TODO List | five checked task-list items, three linking to later sections |
| h2 | TransparentGS Viewer (Renderer) | the manual: h3 Functions (checked task list, a GIF and a screenshot), Software Requirements, Cloning the Repository and Setup (`shell` blocks and a `<details>`), Scene Assets (a tree, h4 Public scene and Custom scene), Step I: Bake GaussProbe, Step II: Boot up the renderer, Full Pipeline (optional), each with a `shell` block and a collapsed argument list, then Renderer GUI Tutorial with h4 entries per control and screenshots |
| h2 | Dataset | one sentence with a Google Drive link |
| h2 | Standalone demo : Segmentation | one link to a sub-README |
| h2 | Training Pipeline | prose, a multi-line `shell` command with `{PLACEHOLDER}` arguments, two result images |
| h2 | Acknowledgements | one paragraph of linked project names |

Absent from the source: table of contents, results or comparison table, model zoo, license section, contact section, star-history chart, emoji in headings, a caption under any figure.

Present but unusual: Citation comes fourth, before any install or usage text; the TODO list is complete (every item checked) and links to sections; command-line arguments are documented as `####` headings inside `<details>`, so each flag becomes a small heading when expanded; the same `<details>` block for `renderer.py` arguments appears twice; the teaser lives in a different repository; the outer `<p align="center">` wrapper is malformed and inert.

## Components

**Academic header.** Centred `<h1>` with `<strong>` for the title, centred `<h3>` with `<br>` for venue and journal, then one centred `<p>` with linked names, `<sup>` marks and `&nbsp;` runs, and affiliations stacked with `<br>`.

**Badge row.** Four flat shields.io badges in a `<div align="center">`, each `<a href='...'><img src='https://img.shields.io/badge/Label-Message-color'></a>` on its own line with single-quoted attributes. Label #555555; messages #007ec6, #b31b1b, #44bb00, #dd4343. Only the YouTube badge has a logo.

**News entries.** Separate paragraphs, not bullets: `**[YYYY.MM.DD]** emoji Sentence.` with day precision and one emoji per line.

**TL;DR and Overview.** A `## TL;DR` paragraph of two sentences, then `## Overview` as one paragraph explaining the figure that follows. Citations appear in author-year form in plain text ("SAM2 [Ravi et al. 2024]").

**Code blocks.** Fenced as ```` ``` shell ```` (with a space before the tag) for commands, with inline `#` comments ("# Windows only", "# Newly Added"); the directory tree has no language tag and uses box-drawing characters; the citation uses `bibtex`. GitHub renders them on its light grey code background with a copy button.

**Collapsible argument lists.** `<details><summary><span style="font-weight: bold;">Command Line Arguments for probes_bake.py</span></summary>` then `#### --flag` headings each followed by a one-line description. GitHub's HTML keeps only `<summary><span>...</span></summary>`, stripping the inline style, so the summary shows in normal weight. The same pattern wraps one setup note ("About the Eigen C++ library") with a `shell` block and a Google Drive fallback link. All of them are collapsed by default.

**Task lists.** `- [x]` items for both the TODO List and the Functions list, so feature bullets render as checked boxes.

**Tutorial entries.** `####` heading per GUI control, a numbered list with bold option names (`1. **reflect**: ...`), and a screenshot `![Alt text](assets/...png)` under the item.

**Citation.** One sentence "If you find this work useful in your research, please cite:" then an `@article{transparentgs, ...}` block with journal, volume, number, pages, DOI URL and publisher.

**Acknowledgements.** One paragraph listing about fifteen linked projects, ending "and so on. Please follow the licenses."

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| transparent_teaser.png | PNG photograph with in-image labels | 3819×2546 | `![teaser](...blob/main/assets/img/transparent_teaser.png)`, no width | 856×571 | header, right after the badge row, no caption |
| pipeline.png | PNG diagram on #f2f2f2 | 2948×1058 | `![pipeline](https://letianhuang.github.io/transparentgs/static/images/exp/pipeline.png)` from the project page | 856×307 | end of Overview |
| garden_2DGS_relighting_shadow_transparent.gif | animated GIF, 252 frames | 600×279 | `![Alt text](assets/...gif)`, no width | 600×279 (natural size, left-aligned) | Functions, under the 2DGS shadow item |
| TransparentGS_viewer_utility.png and GUI_tutorial_*.png | PNG screenshots | not measured | `![Alt text](assets/...png)`, no width | up to 856px wide | Functions and Renderer GUI Tutorial, one per control |
| Training_demo1.png, Training_demo2.png | PNG results | not measured | `![alt text](assets/...png)` | up to 856px wide | end of Training Pipeline |

The teaser does the explaining that a caption would: each object carries a translucent box naming its material class and the scene object ("Transparent: Luck", "Glossy: Mirror", "Diffuse: Lego", "Transparent (Material Editing): Apple"), pointed at by a small dot. Only the GIF moves; no figure uses `<picture>` or a dark variant, and the pipeline figure's light grey panel is drawn for a white page, so the README is light only.

## Adapting to Other Content

- **A library.** Keep the bold centred h1 for the name and the h3 for a one-line description in place of the venue, drop authors and affiliations, keep one flat badge row (Docs, PyPI, License) and put TL;DR directly after it.
- **A dataset.** Keep the full header; make the teaser an annotated sample at full width (856px) with in-image labels naming each category, and move Dataset up so it follows TL;DR.
- **A paper without a large teaser.** Let the badge row close the header and promote the pipeline figure (856px) to right after TL;DR.
- **A tool with many flags.** Reuse the collapsed argument pattern: one `<details>` per script with `####` per flag, placed right under the command it documents.
- **A short-title project.** Put the name alone in the h1 and move the full title to the h3, adding the venue as a separate centred line.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put each header block in its own aligned element | Wrap headings in `<p align="center">`; GitHub closes it and the wrapper does nothing |
| Label objects inside the teaser when the figure has to explain itself | Add a separate legend under the teaser that repeats the labels |
| Keep News, TL;DR, Overview and Citation short and above the manual | Bury the citation under hundreds of lines of setup |
| Collapse long argument lists in `<details>` beside their command | Repeat the same `<details>` block in two places |
| Give badges an `alt` text and quote every `href` | Leave attributes unquoted or badges without `alt` |
| Keep each author's mark tight (`<sup>*,1</sup>`) | Leave a line break inside `<sup>` that renders as "* 1" |

## Agent Prompt Guide

1. "Write a README header in GitHub HTML: `<h1 align="center"><strong>Full Paper Title</strong></h1>`, `<h3 align="center">Venue Year <br> (Journal)</h3>`, one `<p align="center">` with linked author names, `<sup>` affiliation numbers and five `&nbsp;` between names, a `<br>` after the fifth name, then each affiliation on its own line with `<br>`. Follow with a `<div align="center">` of four flat shields.io badges (label #555555; messages DOI #007ec6, arXiv #b31b1b, Project Page #44bb00, YouTube with `logo=youtube&logoColor=white` #dd4343) and a full-width photographic teaser with in-image labels and no caption."
2. "After the header, write `##` sections in this order: News as bold-dated paragraphs (`**[YYYY.MM.DD]**`), TL;DR as two sentences, Overview as one paragraph followed by the pipeline figure, Citation with a `bibtex` block, a TODO List of task-list items linking to later sections, then the usage manual, Dataset, Training Pipeline and Acknowledgements."
3. "In the manual, give each run step a `###` heading, one `shell` block, and a `<details>` whose summary names the script and whose body lists each flag as a `####` heading with a one-line description. For a GUI tutorial, use a `####` heading per control, a numbered list with bold option names and a screenshot under each item."

## Similar Pages

- **readme-eku127-satnav**: the closest header shape (centred title, authors with `<sup>` marks, affiliations, flat badge row, full-width teaser), but SatNav uses a short h1 with an `<h2>` subtitle and a bold venue line, where TransparentGS puts the whole title in the h1 and the venue in an h3.
- **readme-chuan-10-agile**: another SIGGRAPH graphics README with a centred header and a full-width image grid, but with for-the-badge tags placed before the authors and a Modules table instead of a long manual.
- **readme-adobe-research-obj-and-mat-selection**: same academic title-page order with a labeled teaser, but its labels sit under the image cells and it adds a venue logo and a contents list.

## Quick Start

````markdown
<h1 align="center"><strong>ProjectName: Full Paper Title</strong></h1>
<h3 align="center">Venue Year <br> (Journal Name)</h3>

<p align="center">
  <a href="https://example.org/">Author One</a><sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://example.org/">Author Two</a><sup>1</sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://example.org/">Author Three</a><sup>2</sup>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <br>
  <a href="https://example.org/">Author Four</a><sup>*,1</sup>
  <br>
  <sup>1</sup>Lab A, University A<br>
  <sup>2</sup>Lab B, University B
</p>

<div align="center">
  <a href="https://doi.org/10.XXXX/XXXX"><img src="https://img.shields.io/badge/DOI-10.XXXX%2FXXXX-blue" alt="DOI"></a>
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg" alt="arXiv"></a>
  <a href="https://example.github.io/project"><img src="https://img.shields.io/badge/Project-Page-Green" alt="Project page"></a>
  <a href="https://www.youtube.com/watch?v=XXXX"><img src="https://img.shields.io/badge/YouTube-Trailer-red?logo=youtube&logoColor=white" alt="Trailer"></a>
</div>

![teaser](assets/teaser.png)

## News

**[YYYY.MM.DD]** We release the code.

## TL;DR

Two sentences naming the contributions.

## Overview

One paragraph that walks through the figure.

![pipeline](assets/pipeline.png)

## Citation

If you find this work useful in your research, please cite:

```bibtex
@article{key,
    title = {...},
}
```

## TODO List

- [x] Release the [rendering code](#viewer).

## Viewer

### Setup

``` shell
git clone git@github.com:org/name.git --recursive
cd name
conda env create --file environment.yml
```

### Step I: First command

``` shell
python step_one.py --arg value
```

<details>
<summary>Command Line Arguments for step_one.py</summary>

  #### --arg
  what it does

</details>

## Dataset

## Training Pipeline

## Acknowledgements
````

## Provenance

- Repo: https://github.com/LetianHuang/transparentgs (`README.md`, branch `main`, last README commit 4720083 on 2026-04-20).
- Paper: "TransparentGS: Fast Inverse Rendering of Transparent Objects with Gaussians", SIGGRAPH 2025 (ACM Transactions on Graphics 44(4)), DOI 10.1145/3730892, arXiv 2504.18768; first author Letian Huang. Project page https://letianhuang.github.io/transparentgs.
- Selection: a full academic header with superscript affiliations and compact badges, a teaser photo annotated with in-image labels, then News, TL;DR, Overview figure and an early citation block in a compact, logical order.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, the teaser, pipeline PNG and the Functions GIF fetched for pixel sizes and sampled label colors.
- Written 2026-10-28.
