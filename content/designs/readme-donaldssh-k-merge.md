# K-Merge — README Reference

> A conference title slide pinned to a white wall: one centred heading, a quiet credit block, a short strip of grey-and-color tags, then a pastel block diagram that tells the story before a word of prose.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/donaldssh/K-Merge (last commit touching the file 6c4d531, 2026-10-06; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the badge URLs, checked against pixels in the capture; the teaser's size and colors come from `docs/images/teaser.jpg` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The whole header sits inside one `<div align="center">` and is written in plain Markdown rather than HTML paragraphs. A single `#` heading carries the full paper title on two lines with GitHub's grey rule under it. Below it come one line of six linked author names with superscript affiliation numbers, one line of three affiliations, a bold venue line "ACL 2026 (main, oral)", a row of five small flat shields.io badges, and a 660×536 teaser diagram shown at its natural size, narrower than the column and centred. The diagram uses soft pastel blocks (pale yellow, green, lilac, pink, peach) on white, so the first screen reads as light and calm. After the teaser the page turns into a long left-aligned working document: an `## Abstract` of one paragraph, then setup, a LoRA library table, an experiments table, acknowledgements and a citation, with emoji in four of the six `##` headings. There is no news list, no results table and no logo.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Centring wrapper**: `<div align="center">` opens on the first line and closes after the teaser. Everything inside is ordinary Markdown separated by blank lines, so each item becomes a centred paragraph or heading.
2. **Title** (y≈140 to 180, two lines): `# K-Merge: Online Continual Merging of Adapters for On-device Large Language Models`. GitHub h1, 2em (32px), weight 600, with a 1px grey rule under it across the 856px content width. The title wraps after "On-".
3. **Authors** (y≈236): six Markdown links, each on its own source line, written as `[Donald Shenaj](https://donaldssh.github.io/)<sup>1,2,3</sup>&nbsp;`. The newlines and `&nbsp;` render as a double space between names, all on one line. The first line carries a stray `</a>` after the link; GitHub's sanitiser drops it and it has no visible effect. No equal-contribution or corresponding-author marks.
4. **Affiliations** (y≈277): `<sup>1</sup> Samsung R&D Institute UK &nbsp; <sup>2</sup> University of Pisa &nbsp;  <sup>3</sup> University of Padova`. Plain text, one line.
5. **Venue line** (y≈318): `**ACL 2026 (main, oral)**`. Body size, bold, no link and no badge.
6. **Badge row** (y≈344 to 364): five `[![alt](https://img.shields.io/badge/...)](url)` lines in one paragraph. Each badge is 20px tall; the row spans about 480px. Details in Badges.
7. **Teaser** (y≈390 to about 926): `![Paper teaser](docs/images/teaser.jpg)` with no width. The JPEG is 660×536 and renders at that size, centred, leaving about 98px of white on each side of the 856px column. Its lower edge falls just below the 900px fold. No caption.
8. **Close**: `</div>`, then `## Abstract` left-aligned below the fold.

## Badges

All five use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` with a shields.io named color and no `style=`, `logo=` or `labelColor=` parameter, so they render in the default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555 grey with white text. The hex values below are the fills shields.io serves today for each named color.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Project | Page | `green` #67ac09 (label #555555) | flat (default) | donaldssh.github.io/K-Merge |
| Paper | ACL | `red` #dd4343 (label #555555) | flat (default) | aclanthology.org/2026.acl-long.137/ |
| arXiv | 2510.13537 | `white` #ffffff (label #555555, message text #333333) | flat (default) | arxiv.org/abs/2510.13537 |
| Manim | Slides | `purple` #800080 (label #555555) | flat (default) | donaldssh.github.io/K-Merge/presentation.html |
| Cite us | BibTeX | `blue` #007ec6 (label #555555) | flat (default) | `#Citation` (in-page anchor) |

The label names the kind of thing and the message names the venue or format, so "Paper / ACL" and "arXiv / 2510.13537" sit side by side as two routes to the same paper. The white arXiv message is the one light cell in the row and reads as a blank tag on the white page. The last badge is an in-page jump: `Cite_us` uses an underscore that shields.io renders as a space, and it points at `<a name="Citation"></a>` placed just before the citation heading. GitHub rewrites that anchor to `user-content-citation` in lower case; whether the `#Citation` link resolves on github.com depends on GitHub's anchor script and was not tested (inferred to work).

Other colors visible on the first screen come from the teaser, not from badges: pale green #dde8ca and pale yellow #f7f9d2 for adapter blocks, light blue #8cc0f2 for the phone body and pink #ec9ba4 for one of the newer adapters.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred by the wrapper) | K-Merge: Online Continual Merging of Adapters for On-device Large Language Models | full title; authors, affiliations, venue, badges and teaser follow without a heading |
| h2 | Abstract | the paper abstract as one paragraph |
| h2 | ⚙️ Setup | conda commands, a 23-line `pip install` block, data-download blocks for each language source, `accelerate config` note, `mkdir` block, data-preparation script |
| h2 | 📚 LoRA Library | two training commands and a two-column Task tag / Dataset table |
| h2 | 💻 Experiments | a script tree in a code block, a three-column Script / `--lora_merge_strategy` / Method table, sweep and GPU notes, log and output paths |
| h2 | Acknowledgements | one sentence and three bare URLs as `*` bullets |
| h2 | 🔗 Citation | an untagged code block with `@inproceedings{shenaj2026k, ...}` |

Absent from the source: news or changelog, results or leaderboard table, logo, demo GIF or video, model zoo or checkpoint links, license section, contact section, table of contents, figure captions, language tags on code blocks.

Present but unusual: the full paper title is the h1 (no short project name above it); the venue line sits below the affiliations rather than above the authors; the teaser is a small 660px JPEG shown at natural width; one badge links to a hand-placed `<a name>` anchor; every code block is fenced without a language tag, so none is syntax-highlighted.

## Components

**Markdown-in-div header.** One `<div align="center">` with blank-line separated Markdown inside. Authors, affiliations, venue and badges are each one paragraph; GitHub's 16px paragraph margin is the only spacing. No `<p>`, `<br>` or `<h2>` tags are used.

**Author line.** `[Name](url)<sup>n</sup>&nbsp;` per source line, affiliation numbers comma-separated in the `<sup>` (`1,2,3`). Links go to personal pages, one OpenReview profile and one lab page.

**Badge row.** Five static flat badges, label grey #555555, messages #67ac09, #dd4343, #ffffff, #800080 and #007ec6, using shields.io color names (`green`, `red`, `white`, `purple`, `blue`) rather than hex. Alt text is a single lower-case word (`website`, `paper`, `arXiv`, `manim`, `BibTeX`).

**Code blocks.** Triple-backtick fences with no language tag, rendered as plain monospace on GitHub's light grey code background with a copy button. A one-sentence lead ending in a colon introduces each block ("We utilize a conda environment which can be created and activated as follows:").

**Reference tables.** Pipe tables with `|---|` delimiters and no alignment colons; GitHub centres header cells and left-aligns body cells. Identifiers sit in inline code (`correction`, `run_all_k_kmerge.sh`, `kmerge`) and the method column marks the paper's own rows with "(ours)" in plain text, not bold.

**Script tree.** A code block drawn with box characters (`├──`, `└──`) and `#` comments naming the base model for each folder.

**Acknowledgements.** One sentence "Our code extends:" then `*` bullets of bare GitHub URLs that GitHub autolinks.

**Citation.** `<a name="Citation"></a>` on its own line, `## 🔗 Citation`, then an untagged block with the ACL anthology entry including `booktitle` and `pages`. No lead sentence.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.jpg | JPEG, pastel vector-style diagram on white | 660×536 | `![Paper teaser](docs/images/teaser.jpg)` with no width, inside the centring div | 660×536, centred | last item of the header, directly under the badges; no caption |

The teaser has three bands. A timeline of adapter blocks L(1) … L(t+5) runs across the top with a "Time" arrow; the middle shows three numbered steps (1 download a new adapter to a phone drawn in light blue, 2 a K = 4 slot store around a brain icon, 3 Merge(L(t), L2)); the bottom is a staircase of stacked task blocks τ over an axis labelled "LLM Task Capabilities". Blocks are 3D slabs in pastel fills with serif math labels, the same visual vocabulary as a LaTeX/TikZ paper figure. There is one image in the README; no figures appear after the header, no `<picture>` switch and no dark-theme variant. On GitHub's dark theme the white JPEG would sit as a white panel.

## Adapting to Other Content

- **A paper repo with a short project name.** Keep the single centred `#` but put the short name first ("K-Merge: …") as here; if the title runs past two lines at 32px, move the long part into the Abstract and keep the h1 to the name and a phrase.
- **A library.** Drop the author, affiliation and venue paragraphs, keep the centring div with the h1 and one flat badge row (Docs, PyPI, License, Cite), and replace the teaser with a small usage snippet below the div. Keep the emoji-prefixed `##` sections for Setup and Experiments.
- **A dataset.** Keep the header unchanged; swap the "Manim / Slides" badge for a "Dataset / Hugging Face" badge and turn the LoRA Library table into a split table (split, file, size).
- **A benchmark with scores.** Add a results table after Abstract with numeric columns right-aligned (`|---:|`) and the best value in bold; K-Merge has no such table, so this is an extension.
- **A repo without a teaser.** End the div after the badge row and let the Abstract heading follow; with no image the header is about 260px tall.
- **A larger teaser.** If the figure source is wider than 856px, give it `width="100%"` inside an `<img>` tag; at 660px the K-Merge teaser works only because it is a compact diagram.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Wrap the header in one `<div align="center">` and write plain Markdown inside | Mix `<p align>` paragraphs and Markdown inside the same wrapper |
| Keep the badge row to five flat badges with the default #555555 label | Add `for-the-badge` or logo badges to the same row |
| Put the venue and presentation type in one bold line ("ACL 2026 (main, oral)") | Repeat the venue as both a bold line and a badge message |
| Show a compact diagram at its natural width when it is under 856px | Upscale a 660px JPEG to `width="100%"` |
| Lead each code block with one sentence ending in a colon | Leave long code blocks without a lead sentence |
| Mark your own method rows with "(ours)" in the method column | Bold whole table rows to flag your method |
| Add language tags to code fences when adapting this layout | Copy the untagged fences, which lose syntax highlighting |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside one `<div align="center">`: a single `#` heading with the full paper title, one paragraph of six author links each followed by `<sup>n</sup>&nbsp;`, one paragraph of three affiliations with `<sup>` numbers, a bold venue line like `**ACL 2026 (main, oral)**`, then five flat shields.io badges on separate source lines with label grey #555555 and messages Project Page #67ac09, Paper ACL #dd4343, arXiv number #ffffff, Manim Slides #800080 and Cite us BibTeX #007ec6, and finally `![Paper teaser](docs/images/teaser.jpg)` at natural width. Close the div."
2. "After the header, write `## Abstract` with one paragraph, then `## ⚙️ Setup`, `## 📚 LoRA Library`, `## 💻 Experiments`, `## Acknowledgements` and `## 🔗 Citation`. Introduce every code block with one sentence ending in a colon, and put identifiers in inline code."
3. "Build reference tables with `|---|` delimiters and no alignment colons: a two-column Task tag / Dataset table and a three-column Script / flag / Method table that marks the paper's own methods with '(ours)'. Place `<a name="Citation"></a>` before the citation heading so the 'Cite us / BibTeX' badge can jump to it."

## Similar Pages

- readme-eku127-satnav: also a centred academic header with one row of default-flat shields.io badges on #555555 labels and a white-background teaser; SatNav uses `<p align="center">` blocks, an `<h2>` subtitle and a full-width 856px teaser with a caption, where K-Merge uses a Markdown-in-div header, the full title as the only heading and a 660px teaser with none.
- readme-eth-medical-ai-lab-med-prm: same five-badge flat row and an EMNLP/ACL-family paper, but it leads with a wordmark logo, puts the venue in brackets inside the h1 and adds a News list and a scoreboard table.
- readme-progresslm-progresslm: another ACL 2026 oral; it centres its header with HTML paragraphs, uses `for-the-badge` emoji badges and leads with three full-width figures instead of one compact diagram.

## Quick Start

````markdown
<div align="center">

# ProjectName: Full Paper Title on One or Two Lines

[Author One](https://example.org/)<sup>1,2</sup>&nbsp;
[Author Two](https://example.org/)<sup>1</sup>&nbsp;
[Author Three](https://example.org/)<sup>2</sup>&nbsp;

<sup>1</sup> Institution A &nbsp; <sup>2</sup> Institution B

**Venue Year (track, presentation)**

[![website](https://img.shields.io/badge/Project-Page-green)](https://example.github.io/project)
[![paper](https://img.shields.io/badge/Paper-ACL-red)](https://aclanthology.org/XXXX/)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-white)](https://arxiv.org/abs/XXXX.XXXXX)
[![slides](https://img.shields.io/badge/Manim-Slides-purple)](https://example.github.io/project/presentation.html)
[![BibTeX](https://img.shields.io/badge/Cite_us-BibTeX-blue)](#Citation)

![Paper teaser](docs/images/teaser.jpg)

</div>

## Abstract
One paragraph.

## ⚙️ Setup
We utilize a conda environment which can be created and activated as follows:
```bash
conda create -n project python=3.9
conda activate project
```

## 📚 LoRA Library
| Task tag | Dataset |
|---|---|
| `tag` | dataset-name |

## 💻 Experiments
| Script | `--flag` | Method |
|---|---|---|
| `run_ours.sh` | `ours` | Method (ours) |

## Acknowledgements
Our code extends:
* https://github.com/org/repo

<a name="Citation"></a>
## 🔗 Citation
```bibtex
@inproceedings{key,
  title={...},
}
```
````

## Provenance

- Repo: https://github.com/donaldssh/K-Merge (`README.md`, branch `main`, last README commit 6c4d531 on 2026-10-06).
- Paper: "K-Merge: Online Continual Merging of Adapters for On-device Large Language Models", ACL 2026 (main, oral), arXiv 2510.13537; first author Donald Shenaj. Project page https://donaldssh.github.io/K-Merge.
- Selection: a restrained centred header with authors, affiliations, a venue line and a "Cite us / BibTeX" badge leads to a crisp vector-style concept diagram and an abstract, a minimal academic look without clutter.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for each badge URL with capture pixels as a check, and `docs/images/teaser.jpg` fetched from the repo for pixel size and colors.
- Written 2026-10-28.
