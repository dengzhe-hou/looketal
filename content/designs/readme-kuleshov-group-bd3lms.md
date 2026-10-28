# Block Diffusion — README Reference

> A seminar handout: the paper title as a blue link, three tiny colored tabs, and one ticked-and-crossed comparison chart that makes the argument before the abstract does.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/kuleshov-group/bd3lms (last commit touching the file add6a51, 2025-04-16; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the three badge URLs; the figure's size and colors come from `graphical_abstract.png` fetched from the repo. GitHub sets the type (its system stack), the 16px body size and the heading rules; nothing in the README overrides them. Rendered y values below are in the 1440×900 frame.

## Overview

This README is plain Markdown from top to bottom, left-aligned, with no HTML layout at all. The `#` heading is the full paper title written as a link to arXiv, followed by the venue in plain parentheses, so the h1 renders as two lines of GitHub link blue ending in black "(ICLR 2025 Oral)". A "By ..." author line, three small flat badges and the graphical abstract follow. The graphical abstract is the page's one image and its whole pitch: three rows (Autoregression, Diffusion, Block Diffusion (Ours)) each with four green ticks or red crosses for quality, length, KV caching and parallelism, over monospace token sequences on a pale tan highlight. A one-paragraph abstract with bold initials spelling the acronym, a two-group "In this repo, we provide" list and a numbered nine-item Code Organization map come next. The body is a short set of plain `##` sections (Code Organization, Getting Started, Reproducing Experiments, Citation) with h3 and h4 subsections, long backslash-continued `bash` commands, and no emoji in headings, no tables and no news.

## Header Block

1. **Title** (y≈116 and 156): `# [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://arxiv.org/abs/2503.09573) (ICLR 2025 Oral)`. GitHub h1, 2em (32px), weight 600, left-aligned. The linked part takes GitHub's link color, the parenthesised venue stays in the text color; it wraps after "and". GitHub's 1px grey rule sits under it (y≈184).
2. **Authors** (y≈214 and 238): a Markdown paragraph starting `By ` with eight linked names separated by `, `. No superscripts, no affiliations, no equal-contribution marks; it wraps to a second line at the 856px width.
3. **Hidden Colab badge**: `<!-- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](...) -->`, an HTML comment, so nothing renders.
4. **Badge row** (y≈275): three Markdown image links on consecutive lines, each with the alt text `deploy`: `[![deploy](https://img.shields.io/badge/Paper_📃-green)](...)`, `[![deploy](https://img.shields.io/badge/Blog_📝%20%20-8A2BE2)](...)`, `[![deploy](https://img.shields.io/badge/HuggingFace_🤗%20-BD3LMs%20-orange)](...)`. GitHub joins them into one left-aligned paragraph; widths 55, 49 and 150px, 20px tall, so the row is about 262px. Details in Badges.
5. **Graphical abstract** (y≈310 to 630): `![graphical_abstract](graphical_abstract.png)` with no width attribute. The 1705×654 PNG is scaled by GitHub's `max-width: 100%` to 856×328.
6. **Abstract paragraph** (from y≈668): `We introduce ***BD3-LMs***, a family of **B**lock **D**iscrete **D**enoising **D**iffusion **L**anguage **M**odels ...`. The model name is bold italic and the six initials are bold, so the acronym is spelled out in the sentence.
7. **Hidden demo line**: a second HTML comment with the same Colab badge.
8. **Contents list** (below the fold): `In this repo, we provide:` then a `*` list with two bold items, **The BD3-LM framework** (three numbered children) and **Baseline implementations** (four numbered children with bracketed paper links such as `[[AR](https://arxiv.org/abs/2406.07524)]`). GitHub renders the nested ordered lists with lowercase roman numerals (i., ii., iii.). This ends the header block.

## Badges

All three use the static path form with no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, white (#ffffff) text. Two are single-segment badges (one text field, no label), and the emoji are part of the badge text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (none) | Paper 📃 | `green`, rendered #67ac09 | flat (default), single segment | openreview.net/forum?id=tyEyYT267x |
| (none) | Blog 📝 | #8a2be2 | flat (default), single segment | m-arriola.com/bd3lms/ |
| HuggingFace 🤗 | BD3LMs | `orange`, rendered #ea7233 (label #555555) | flat (default) | huggingface.co/collections/kuleshov-group/bd3-lms-... |

The named colors are given as the hex values in the SVGs shields.io returned on 2026-10-28 (`green` #67ac09, `orange` #ea7233). Underscores in the badge path become spaces and the trailing `%20%20` and `%20` add padding that shields.io trims. All three images have the alt text `deploy`, a leftover from a template, so screen readers hear "deploy" three times. There is no arXiv badge; arXiv is reached through the linked h1.

Colors in the graphical abstract, not badges: ticks and positive labels in green #4d9900 with darker #006600 text, crosses in red #ea6b66 with #990000 text, token text in navy #020272 on a tan #f7e8c3 highlight, and black #000000 row titles.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 | Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models (ICLR 2025 Oral) | linked title; authors, badges, graphical abstract, abstract and the "In this repo" list follow without a heading |
| h2 | Code Organization | preceded by `<a name="code-organization"></a>`; a nine-item numbered list of files and folders in inline code, with nested `-` lists under `scripts/` and `ssd-lm/` |
| h2 | Getting Started | preceded by `<a name="getting_started"></a>`; a three-line `bash` block for conda and pip, a FlashAttention note, two one-line `bash` blocks |
| h3 | Checkpoints | three prose paragraphs of Hugging Face and Google Drive links, no table |
| h2 | Reproducing Experiments | one paragraph naming `main.py` and `scripts/` |
| h3 | Generate Arbitrary-Length Sequences | h4 HuggingFace model and h4 Local checkpoint, each a long backslash-continued `bash` block |
| h3 | Likelihood Evaluation | one `bash` block |
| h3 | Training Pipeline | one `bash` block and a paragraph on batch size |
| h3 | Acknowledgements | one sentence linking MDLM and SEDD |
| h2 | Citation | an untagged code block with an `@inproceedings{` entry |

Absent from the source: logo, centred layout, affiliations, project-page badge (the blog stands in for it), news, results tables, model-zoo table, GIF or video, `<details>` blocks, table of contents, license section, emoji headings.

Present but unusual: the venue sits in the h1 after the linked title; all three badges share the alt text `deploy`; two commented-out Colab badges remain in the source; Code Organization uses triple-backtick inline code (```` ```main.py``` ````), which GitHub renders as ordinary inline code; Acknowledgements is an h3 inside Reproducing Experiments rather than its own h2; the citation block has no `bibtex` tag, so it renders without syntax colors; the AR baseline link and the MDLM link point to the same arXiv ID (2406.07524).

## Components

**Linked title with venue.** `# [Full Title](https://arxiv.org/abs/XXXX.XXXXX) (Venue Year Award)`. The link makes the h1 itself the paper link, and the venue in parentheses reads as a tag.

**Author line.** `By [Name](url), [Name](url), ...` as a single paragraph; no superscripts.

**Single-segment badges.** `https://img.shields.io/badge/Text_emoji-color` for a one-field badge (Paper 📃 on #67ac09, Blog 📝 on #8a2be2), next to one two-field badge (HuggingFace 🤗 | BD3LMs, label #555555, message #ea7233).

**Acronym sentence.** `***Name***` for the model name and `**B**lock **D**iscrete ...` bolding each initial, inside the first sentence of the abstract.

**Grouped contribution list.** `* **Group title**` bullets with two-space-indented `1.`/`2.` children; baseline names end with a bracketed link `[[SEDD](url)]` and an italic qualifier `*(supports sample generation only)*`.

**Code-organization map.** A numbered list `1. ```file.py```: What it does` for top-level files and folders, with four-space-indented `- ``subdir/``: description` children for script folders. Explicit `<a name="..."></a>` anchors sit above this and the next heading.

**Command blocks.** `bash` blocks that start with shell variables and a trailing comment (`BLOCK_SIZE=4 # 4, 8, 16`), then `python -u main.py \` with one Hydra override per line, four-space indented. Each block is introduced by a sentence that names the `mode=` value and the folder of example scripts.

**Citation.** `## Citation` directly followed by an untagged fenced block with `@inproceedings{` on its own line and the key on the next.

**Acknowledgement line.** One sentence, "This repository was built off of [MDLM](...) and [SEDD](...)."

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| graphical_abstract.png | PNG (RGBA, white background), comparison chart | 1705×654 | `![graphical_abstract](graphical_abstract.png)` with no width | 856×328 | header, between the badge row and the abstract |

The image is a three-row comparison. Each row has a bold black title at the left ("Autoregression:", "Diffusion:", "Block Diffusion (Ours):"), four property labels with a green tick #4d9900 or red cross #ea6b66, and beneath them a monospace navy #020272 token sequence with a downward arrow labelled "Generation steps", where newly generated tokens sit on a tan #f7e8c3 band. The last row is all ticks, so the eye lands on the method. There is no caption, no `<picture>` pair and no dark-theme variant; on GitHub's dark theme the white background would show as a white block (inferred from the opaque white pixels, not captured).

## Adapting to Other Content

- **A library.** Replace the linked paper title with `# Name` and a one-line description, keep the three-badge row (Docs, Blog, Hugging Face), and use the comparison-chart idea as a feature table image: rows are alternatives, columns are properties, ticks and crosses in #4d9900 and #ea6b66.
- **A dataset.** Keep the linked h1 and venue, swap the chart for a three-row sample strip at full column width (856px), and turn Code Organization into a file-format map with the same numbered `file`: description pattern.
- **A benchmark.** Add a `## Results` section after Getting Started with a pipe table, numeric columns right-aligned (`---:`) and bold best values; Block Diffusion has no table, so this is an extension.
- **A repo without a figure.** Let the badge row lead straight into the acronym paragraph and the "In this repo, we provide" list; that list then carries the overview.
- **Cleanup when adapting.** Give each badge its own alt text, tag the citation block `bibtex`, and remove commented-out badges.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Make the h1 the paper link and add the venue in parentheses | Repeat the paper title as a separate arXiv badge |
| Explain the idea with one tick-and-cross comparison image | Open with a dense architecture diagram that needs a caption |
| Spell the acronym with bold initials in the first sentence | Leave the acronym undefined until the method section |
| Map the code as a numbered list of files with one-line roles | Paste a raw `tree` dump with no descriptions |
| Show full commands with one override per line | Hide the important flags inside shell scripts only |
| Give each badge descriptive alt text | Reuse one alt text (`deploy`) for every badge |
| Tag the citation block `bibtex` | Leave the BibTeX block untagged |

## Agent Prompt Guide

1. "Write a left-aligned GitHub README header in plain Markdown: `# [Full Paper Title](https://arxiv.org/abs/XXXX.XXXXX) (Venue Year Oral)`, a `By [Name](url), ...` author paragraph, then three flat shields.io badges on one line: single-segment `Paper 📃` in green #67ac09, single-segment `Blog 📝` in #8a2be2, and `HuggingFace 🤗 | ModelName` with label #555555 and orange #ea7233 message. Follow with one comparison image `![graphical_abstract](graphical_abstract.png)` and no width."
2. "Draw the comparison image as three rows (two prior approaches and 'Ours'), each with four property labels marked by a green tick #4d9900 or a red cross #ea6b66, and a monospace navy #020272 example sequence on a tan #f7e8c3 highlight; make the last row all ticks."
3. "After the image, write one abstract paragraph that bolds each initial of the acronym, an 'In this repo, we provide:' list with two bold groups and numbered children, then `## Code Organization` as a numbered file map, `## Getting Started` with a `bash` install block and `### Checkpoints`, `## Reproducing Experiments` with h3 per mode and backslash-continued `bash` commands, and `## Citation` with a `bibtex` block."

## Similar Pages

- readme-eth-medical-ai-lab-med-prm also puts the venue inside the h1, as a bracketed `[EMNLP 2025]` prefix rather than Block Diffusion's trailing parentheses.
- readme-damon-demon-spanuq and readme-adobe-research-obj-and-mat-selection also carry a code-structure section; compare their trees with Block Diffusion's numbered file list.
- readme-huggingface-peft is a language-model library README in the set, for contrast with this paper-code layout.
- Block Diffusion's distinguishing choices are the linked h1 title and the single tick-and-cross comparison figure. Its blog (m-arriola.com/bd3lms/) is a separate web page and is not described here.

## Quick Start

````markdown
# [Full Paper Title](https://arxiv.org/abs/XXXX.XXXXX) (Venue Year Oral)
By [Author One](https://example.org/), [Author Two](https://example.org/), [Author Three](https://example.org/)

[![Paper](https://img.shields.io/badge/Paper_📃-green)](https://openreview.net/forum?id=XXXX)
[![Blog](https://img.shields.io/badge/Blog_📝-8A2BE2)](https://example.org/blog/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace_🤗-ModelName-orange)](https://huggingface.co/collections/org/name)

![graphical_abstract](graphical_abstract.png)

We introduce ***ACRO***, a family of **A**cronym **C**omponents ... One paragraph abstract.

In this repo, we provide:
* **The ACRO framework**
  1. Component one
  2. Component two
* **Baseline implementations**
  1. Baseline [[NAME](https://arxiv.org/abs/XXXX.XXXXX)]

## Code Organization
1. `main.py`: Routines for training and evaluation
2. `models/`: Network architectures
3. `scripts/`: Shell scripts for training/evaluation
    - `train/`: Training scripts

## Getting Started

```bash
conda create --name env python=3.9
conda activate env
pip install -r requirements.txt
```

### Checkpoints

Checkpoints are on Hugging Face: [org/name](https://huggingface.co/org/name).

## Reproducing Experiments

### Likelihood Evaluation
To compute test perplexity, use `mode=ppl_eval`:
```bash
BLOCK_SIZE=4 # 4, 8, 16

python -u main.py \
    mode=ppl_eval \
    block_size=${BLOCK_SIZE}
```

### Acknowledgements
This repository was built off of [Project](https://github.com/org/project).

## Citation
```bibtex
@inproceedings{key2025,
  title={...},
}
```
````

## Provenance

- Repo: https://github.com/kuleshov-group/bd3lms (`README.md`, branch `main`, last README commit add6a51 on 2025-04-16).
- Paper: "Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models", ICLR 2025 (Oral, per the README), arXiv 2503.09573; first author Marianne Arriola. Blog https://m-arriola.com/bd3lms/.
- Selection: the linked title with the venue in parentheses, a check/cross comparison graphic that explains the idea at a glance and a numbered code-organization map make a clear template for method papers.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the three badge URLs (emoji URL-encoded as in the rendered HTML), `graphical_abstract.png` fetched from the repo for size and colors.
- Written 2026-10-28.
