# GuideDog — README Reference

> A field report pinned flush left: a long ruled title, small-print card-suit credits, three glossy tags, then a loud street-scene poster and the abstract set like a pulled quote.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/jun297/GuideDog (last commit touching the file b707b8a, 2026-07-21; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs; the teaser's size and colors come from `assets/figure.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

Unlike most academic READMEs, the header is left-aligned. A Markdown `#` heading carries the full paper title over two lines with GitHub's grey rule, followed by two lines of author names (some linked, some plain) marked with card-suit superscripts ♣ ♢ ♡ ♠, a `<sub>`-sized affiliation line, a `<sub>`-sized footnote line that also carries the venue, and one row of three flat shields.io badges. The only centred element is the teaser, a 1114×824 annotated street photograph that fills the rest of the first screen; the abstract follows as a Markdown blockquote, so it renders grey with a left bar. The body is a dataset-and-evaluation manual in eight plain `##` sections: an overview with bold counts, a dataset config table with a right-aligned numeric column and a `python` loading snippet, installation with a commented extras block, a reproduce-one-number quickstart, a task table, BibTeX, a dual-license list and an acknowledgement. There is no news list, no results table and no project page link.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116–156, two lines): `# GuideDog: A Real-World Egocentric Multimodal Dataset for Blind and Low-Vision Accessibility-Aware Guidance`. GitHub h1, 2em (32px), weight 600, left-aligned, wrapping naturally at the 856px content width, with the 1px grey rule beneath.
2. **Authors** (y≈214 and 238): `<p align="left">` with eight names. Linked names are `<a href='...' target='_blank'>Name</a>` (GitHub strips `target`), unlinked names are plain text; each is followed by `<sup>♣*</sup>`-style marks and separated by `&emsp;` after the first name and `&ensp;` elsewhere; one `<br>` splits four and four. Links render in GitHub blue, plain names in body black, so the line alternates color.
3. **Affiliations** (y≈281): `<p align="left"><sub><sup>♣</sup>Yonsei University &ensp; <sup>♢</sup>LG AI Research &ensp; ...</sub></p>`. The `<sub>` shrinks the whole line to about 12px.
4. **Footnotes and venue** (y≈322): `<p align="left"><sub><sup>*</sup>Equal contribution &nbsp;·&nbsp; <sup>†</sup>Work done while at SK Telecom &nbsp;·&nbsp; ACL 2026 (Main)</sub></p>`. The venue is the last item of a middle-dot list, not a separate bold line.
5. **Badge row** (y≈354): three Markdown image links `[![arXiv](https://img.shields.io/badge/...)](...)` on consecutive lines, so they join one paragraph and render 20px tall with single spaces between them; the row spans about 451px from the left edge.
6. **Teaser** (y≈402 to about 1035, past the fold): `<p align="center"><img src="assets/figure.png" alt="GuideDog overview"></p>` with no width, so GitHub's `max-width: 100%` scales the 1114×824 PNG to 856×633. No caption.
7. **Abstract blockquote** (below the fold): one `>` paragraph of four sentences with **GuideDog** and **GuideDogQA** in bold. GitHub renders it in its muted grey with a 4px left border. This ends the header block.

## Badges

All three use the static path form with no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2503.12844 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2503.12844 |
| 🤗 Dataset | kjunh/GuideDog | #ffd21e (label #555555, message text #333333) | flat (default) | huggingface.co/datasets/kjunh/GuideDog |
| License | MIT / Apache-2.0 | #67ac09 (`green` as shields.io now renders it; label #555555) | flat (default) | `#license` (in-page anchor) |

The label names the kind of artifact and the message is its identifier (the arXiv number, the Hugging Face repo id, the license pair), so each badge reads as a citation rather than a button. The hugging-face emoji is part of the label text (`%F0%9F%A4%97%20Dataset`), not a shields.io logo. The License badge links to the README's own License section. There is no text link row.

Teaser colors, read as the most frequent pixels of `figure.png`: navy #264e72 for the top title band and the "GuideDog Standards" box, pink #e95297 for the S2 obstacle caption, sky blue #68b9ff for the S3 direction caption, cream #fff9db for the S1 speech bubble.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 | GuideDog: A Real-World Egocentric Multimodal Dataset for Blind and Low-Vision Accessibility-Aware Guidance | title; authors, affiliations, footnotes, badges, teaser and abstract blockquote follow without a heading |
| h2 | Overview | two paragraphs: dataset size with bold counts (**22,084 image-description pairs**) and italic *gold* / *silver*, then what the repo is (a fork of `lmms-eval`) |
| h2 | Dataset | one sentence with the license, a four-row Config / Split / Rows / Use table, a `python` `load_dataset` block, a token note |
| h2 | Installation | a version line, a three-line `bash` block, a `bash` block of three extras with aligned `#` comments, a Docker and `.env` note |
| h2 | Quickstart: reproduce a single eval | one paragraph, a multi-line `bash` launch command with `\` continuations, a second `bash` block with `export OPENAI_API_KEY` |
| h2 | Tasks | a three-column Task name / Config × split / Metrics table with seven rows, one usage line |
| h2 | Citation | a `bibtex` block, no lead sentence |
| h2 | License | two bullets with bold license names, one paragraph for the dataset license |
| h2 | Acknowledgements | one sentence crediting `lmms-eval` |

Absent from the source: news, project page or demo link, results or leaderboard table, model zoo, GIF or video, table of contents, contact, emoji in headings.

Present but unusual: the header is left-aligned while only the teaser is centred; affiliations use card-suit symbols instead of numbers; the venue lives inside a `<sub>` footnote line; the abstract is a blockquote placed after the teaser, above Overview; the Dataset table right-aligns one numeric column (`|-------:|`) and pads every cell with spaces so the source reads as a grid.

## Components

**Small-print credits.** Affiliation and footnote lines are each one `<p align="left"><sub>...</sub></p>`, entries separated by `&ensp;` or `&nbsp;·&nbsp;`, so they sit visibly below body size under the full-size author line.

**Flat badge row.** Three Markdown image links on consecutive lines, default flat style, label #555555, messages #b31b1b, #ffd21e and #67ac09; messages are identifiers, not verbs.

**Abstract blockquote.** One `> ` paragraph directly under the teaser, with the two artifact names in bold; GitHub's muted color and left border separate it from the Overview prose.

**Config table.** Four columns with the numeric Rows column right-aligned (`|-------:|`) and the others left-aligned; config names in inline code; source cells padded to equal widths. GitHub centres header cells and stripes alternate rows.

**Loading snippet.** A `python` block of four `load_dataset` calls aligned into columns with extra spaces, one per config/split, right after the table it mirrors.

**Commented install block.** `bash` with one `pip install -e ".[extra]"` per line and aligned `# purpose` comments.

**Launch command.** `python -m accelerate.commands.launch -m lmms_eval \` with one flag per continued line, indented four spaces.

**Task table.** Task names in inline code, a "Config × split" column using the multiplication sign, and `(same)` to avoid repeating a long metric list.

**Citation, license, acknowledgement.** A `bibtex` block with `=` signs aligned; License as bold-led bullets; one acknowledgement sentence with an inline-code link.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| figure.png | PNG, annotated photograph with cartoon guide and text callouts | 1114×824 | `<img src="assets/figure.png">` with no width in `<p align="center">` | 856×633 | after the badge row, before the abstract blockquote; no caption |

The teaser is one street photograph under a navy title band ("Describe the situation to BLV people following GuideDog Standards."), with three numbered callouts S1, S2, S3 in cream, pink and sky blue, a cartoon character with sunglasses at the bottom centre, and a lower strip that lists the three standards next to an "MLLM" robot icon and its sample answer. The photo nearly touches the image edges (non-white pixels run from x=10 to x=1104 of 1114), so at 856px it reads as edge to edge. It is the only image in the README; there is no `<picture>`, GIF or video.

## Adapting to Other Content

- **A library.** Keep the left-aligned `#` title, drop the card-suit credits, keep a three-badge flat row (docs, PyPI, license) with identifier messages, and replace the teaser with the install and loading snippets.
- **A model release.** Keep the header; replace the Dataset config table with a checkpoint table using the same right-aligned numeric column for sizes or scores.
- **A benchmark with scores.** Add a results table after Tasks with right-aligned numbers (`| ---: |`) like the Rows column; GuideDog has none, so this is an extension.
- **A repo without a teaser.** Put the abstract blockquote directly under the badge row; it becomes the first visual break.
- **A centred variant.** If the project wants a centred header, change every `align="left"` to `center` and keep the `<sub>` lines; the teaser at 856px already sits centred.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep credits compact: one author line pair, then `<sub>` affiliation and footnote lines | Give affiliations and footnotes full body size |
| Use badge messages that are identifiers (arXiv number, repo id, license) | Use generic messages like "Paper" or "Link" |
| Let the teaser scale to the 856px column without a width attribute | Give the teaser a fixed pixel width that ignores the column |
| Quote the abstract as one blockquote paragraph under the teaser | Paste the abstract as plain body text before the teaser |
| Right-align numeric table columns and keep identifiers in inline code | Mix centred and left alignment arbitrarily in one table |
| Show one end-to-end command that reproduces one paper number | Lead with a long matrix of every model and task |

## Agent Prompt Guide

1. "Write a left-aligned README header in GitHub Markdown: a `#` heading with the full paper title, a `<p align="left">` author line with `<sup>` card-suit marks (♣ ♢ ♡ ♠) separated by `&ensp;` and split by one `<br>`, then two `<p align="left"><sub>` lines for affiliations and for footnotes ending with the venue, joined by `&nbsp;·&nbsp;`."
2. "Under the credits, add three default flat shields.io badges as Markdown image links on consecutive lines (arXiv number on #b31b1b, 🤗 Dataset repo id on #ffd21e, License MIT / Apache-2.0 on #67ac09, all with label #555555), then a centred teaser `<img>` with no width so it renders at 856px, then the abstract as one `>` blockquote paragraph."
3. "Write the body as plain `##` sections: Overview with bold counts, Dataset with a Config / Split / Rows / Use table whose Rows column is right-aligned and a `python` `load_dataset` block, Installation with a commented extras `bash` block, a one-number Quickstart, a Tasks table with inline-code names, Citation (`bibtex`), License, Acknowledgements."

## Similar Pages

- readme-eth-medical-ai-lab-med-prm: also a natural-language dataset/model README with a red arXiv badge and a Hugging Face badge, but with a centred logo image and a `#` title placed below it; GuideDog has no logo and keeps everything flush left.
- readme-snuhcc-dice-bench: an NLP benchmark README whose `#` heading is the full paper title with a centred badge row beneath; GuideDog adds the author block and swaps the banner for a photographic teaser.
- readme-eku127-satnav: another dataset release with a full-width teaser near the top, but SatNav is fully centred, captioned and leads with a runnable Quick Start rather than an abstract quote.

## Quick Start

````markdown
# ProjectName: Full Paper Title on One or Two Lines

<p align="left">
    <a href='https://example.org/'>Author One</a><sup>♣*</sup>&emsp;
    <a href='https://example.org/'>Author Two</a><sup>♣*</sup>&ensp;
    Author Three<sup>♢</sup>&ensp;
    Author Four<sup>♠</sup>
    <br>
    Author Five<sup>♢†</sup>
</p>

<p align="left"><sub><sup>♣</sup>Institution A &ensp; <sup>♢</sup>Institution B &ensp; <sup>♠</sup>Institution C</sub></p>

<p align="left"><sub><sup>*</sup>Equal contribution &nbsp;·&nbsp; <sup>†</sup>Footnote &nbsp;·&nbsp; Venue Year (Main)</sub></p>

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
[![Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Dataset-org/name-FFD21E)](https://huggingface.co/datasets/org/name)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license)

<p align="center">
  <img src="assets/figure.png" alt="Overview">
</p>

> One-paragraph abstract with the dataset name in **bold**.

## Overview

## Dataset

| Config    | Split  | Rows   | Use                 |
|-----------|--------|-------:|---------------------|
| `default` | test   |  1,000 | What it is used for |

```python
from datasets import load_dataset
test = load_dataset("org/name", split="test")
```

## Installation

```bash
git clone https://github.com/org/name.git
cd name
pip install -e .
```

## Quickstart: reproduce a single eval

```bash
python -m package \
    --model name \
    --tasks task_name \
    --output_path ./logs/
```

## Tasks

| Task name   | Config × split   | Metrics  |
|-------------|------------------|----------|
| `task_name` | default × test   | accuracy |

## Citation

```bibtex
@inproceedings{key2026,
    title     = {...},
}
```

## License

## Acknowledgements
````

## Provenance

- Repo: https://github.com/jun297/GuideDog (`README.md`, branch `main`, last README commit b707b8a on 2026-07-21).
- Paper: "GuideDog: A Real-World Egocentric Multimodal Dataset for Blind and Low-Vision Accessibility-Aware Guidance", ACL 2026 (Main), arXiv 2503.12844; first author Junhyeok Kim.
- Selection: a bold annotated teaser sits under a compact author and badge header, the abstract is set as a quoted block, and a small dataset-config table plus copy-ready loading code make the first screens unusually informative.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the three badge URLs, `assets/figure.png` fetched for pixel size and colors.
- Written 2026-10-28.
