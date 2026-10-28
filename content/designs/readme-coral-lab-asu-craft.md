# CRAFT — README Reference

> A tool manual with a conference ribbon: one centred title, a long strip of emoji-tagged badges, a dotted link bar, then a three-row table that explains the whole method before the first install line.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/coral-lab-asu/CRAFT (last commit touching the file 7c4be45, 2026-07-19; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs, and the Hugging Face badge from its SVG at huggingface.co. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The page has no images at all apart from badges. A `<div align="center">` holds a one-line `#` title with GitHub's grey rule, a single row of seven flat shields.io badges (three with white logos, three with emoji in the label), and a bold row of five emoji-prefixed text links joined by ` · `. Below the div, left-aligned prose introduces the method in three sentences and a three-row Stage / Model / Input → Output table stands in for the usual pipeline figure; a second paragraph on optional enrichment closes the intro. From there the README reads like package documentation: nine `##` sections, all but the last preceded by a Markdown `---` rule (eight 4px grey bars down the page), with `bash`, `ini`, `python` and `json` blocks, a two-row mode table and an untagged directory tree. There is no teaser, no author list, no news and no results table.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Wrapper**: `<div align="center">` with blank lines inside it, so the Markdown title, badge lines and link line are parsed as Markdown and centred.
2. **Title** (y≈139): `# CRAFT: Training-Free Cascaded Retrieval for Tabular QA`. GitHub h1, 2em (32px), weight 600, on one line, with the 1px grey rule across the 856px content width.
3. **Badge row** (y≈194): seven Markdown image links `[![Paper](https://img.shields.io/badge/...)](...)` on consecutive lines, joined into one paragraph; each badge is 20px tall and the row spans about 782px, nearly the full column.
4. **Link bar** (y≈239): `**[📄 Paper](...) · [🖼️ Poster](...) · [📊 Slides](...) · [🤗 Datasets](...) · [🌐 Website](...)**`. One bold paragraph of five links, each starting with an emoji, separated by a middle dot; it repeats four badge targets and adds the website, which has no badge.
5. **Intro** (y≈278–304, after the div closes): three left-aligned lines of prose with **training-free** and **no dataset-specific fine-tuning** in bold.
6. **Stage table** (y≈332–480): a three-column, three-row pipe table with bold stage names and an italic *(optional)*; at about 572px it does not span the column.
7. **Enrichment paragraph** (y≈508–581): four lines with bold **LLM enrichment** and **Gemini 1.5 Flash**, an emoji link to the 🤗 collection and an in-page anchor link.
8. **Rule and first section** (y≈618 and 660): `---` then `## Install`, whose first `bash` block (y≈700–846) ends the first screen.

## Badges

All seven use the static path form with no `style=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555. Three add `logo=...&logoColor=white`.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Paper (Google Scholar logo, white) | ACL 2026 | #b31b1b (label #555555) | flat (default) | aclanthology.org/2026.acl-long.149/ |
| arXiv (arXiv logo, white) | 2505.14984 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2505.14984 |
| 🤗 Datasets | CRAFT Collection | #d8b800 (`yellow` as shields.io now renders it; label #555555) | flat (default) | Hugging Face collection |
| 🖼️ | Poster | #6f42c1 (label #555555) | flat (default) | site/CRAFT_poster.jpg |
| 📊 | Slides | #ea7233 (`orange` as shields.io now renders it; label #555555) | flat (default) | site/CRAFT_slides.pdf |
| License | MIT | #d8b800 (`yellow`; label #555555) | flat (default) | LICENSE |
| Python (Python logo, white) | 3.9+ | #007ec6 (`blue`; label #555555) | flat (default) | python.org/downloads/ |
| (link row) | 📄 Paper · 🖼️ Poster · 📊 Slides · 🤗 Datasets · 🌐 Website | GitHub link blue | bold links, ` · ` separators | same targets plus coral-lab-asu.github.io/CRAFT/ |
| (section badge) | Dataset on HF | Hugging Face's own badge SVG, 124×27, with a light stroke #efefef | rounded pill | Hugging Face collection, at the top of "Data setup" |

Paper and arXiv share #b31b1b, so the two paper badges read as one pair; Datasets and License share the shields.io `yellow`, which renders darker than Hugging Face's own #ffd21e. Poster and Slides put an emoji in the label slot instead of a word. The color order is red, red, yellow, purple, orange, yellow, blue, without a single rule behind it.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | CRAFT: Training-Free Cascaded Retrieval for Tabular QA | title; badge row, link bar, intro, stage table and enrichment paragraph follow without a heading |
| h2 | Install | `bash` block of six `pip install` lines with extras and aligned comments, "From source" `bash` block, an `ini` block for `.env` |
| h2 | Quick start | one paragraph, a `bash` block of four numbered `# 1.`–`# 3.` commented commands, an output note, a "Useful flags" `bash` block |
| h2 | LLM enrichment (optional) | paragraph with inline-code config keys, a two-line `bash` block, a backends paragraph, a provenance paragraph with file links |
| h2 | Stage 2 modes | one sentence and a two-row Mode / How it works table |
| h2 | Custom datasets | bold file names (**corpus.jsonl**, **queries.jsonl**) each followed by a two-line `json` example |
| h2 | Data setup (NQ-Tables and OTT-QA) | the Hugging Face "Dataset on HF" badge, a `bash` download block, a `python` `load_dataset` block, a two-item bullet list of original corpora |
| h2 | Package layout | an untagged code block showing `src/craft_tabqa/` as a tree with box-drawing characters and descriptions |
| h2 | Citation | a `bibtex` block in ACL Anthology format |
| h2 | License | "MIT — see [LICENSE](LICENSE)." |

Absent from the source: teaser or any figure, author and affiliation block, news, results table, model zoo, demo GIF or video, table of contents, acknowledgements, contact, emoji in headings.

Present but unusual: the method is explained by a table rather than a figure; a second, larger Hugging Face badge appears mid-page inside a section; every section except License is preceded by `---`, so GitHub draws a 4px rule directly above each heading's own 1px rule; the Package layout block has no language tag.

## Components

**Centred header div.** `<div align="center">` with blank lines inside, holding Markdown (not HTML) for the title, badges and link bar.

**Flat badge row.** Seven `[![alt](https://img.shields.io/badge/Label-Message-color?logo=...&logoColor=white)](target)` lines; label #555555; messages #b31b1b, #b31b1b, #d8b800, #6f42c1, #ea7233, #d8b800, #007ec6. Emoji are written directly in the URL path (`🤗%20Datasets`, `🖼️-Poster`).

**Emoji link bar.** One bold paragraph, `**[📄 Paper](...) · [🖼️ Poster](...) · ...**`, each link led by its own emoji.

**Stage table.** `|-------|-------|----------------|` with no alignment colons; bold first column (**Stage 1**), plain model names, and an arrow notation "full corpus → top 5,000" in the last column.

**Section rule.** A Markdown `---` on its own line, with blank lines around it, before each `##` from Install to Citation; License has none.

**Commented command blocks.** `bash` blocks where trailing `# comments` are aligned with spaces into a column; numbered comment headers (`# 1. Build the SPLADE index ...`) group multi-step runs; `ini` for environment variables with `# enables Stage 3` comments.

**Mode table.** Two columns, inline-code mode names with an italic *(default)* marker in the first cell, full sentences in the second.

**Schema examples.** A bold file name with an em dash and a short description, then a `json` block holding one wrapped example object.

**Tree block.** An untagged fenced block drawing `src/craft_tabqa/` with `├──` and `└──`, descriptions aligned in a column.

**Citation and license.** ACL Anthology BibTeX with `editor`, `doi`, `pages` and `ISBN`; one-line license with a link.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| (none) | no teaser, figure, GIF or video | — | — | — | — |
| dataset-on-hf-md.svg | Hugging Face badge SVG, rounded pill | 124×27 | `[![Datasets on Hugging Face](https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md.svg)](...)` | 124×27 | first line of "Data setup", left-aligned |

The visual weight comes from typography and gray code panels: the stage table under the intro, and the many `bash` blocks on GitHub's light code background. The only images are the badges.

## Adapting to Other Content

- **A paper repo with a figure.** Keep the centred title, badge row and link bar, then place a `width="100%"` (856px) pipeline figure above the stage table rather than replacing it; the table still gives the numbers.
- **A dataset.** Replace the stage table with a split table (split, rows, use) and move "Data setup" ahead of Install.
- **A benchmark with scores.** Add a results table after the stage table with right-aligned numeric columns (`| ---: |`) and bold best values; CRAFT has none, so this is an extension.
- **A pure library.** Keep everything after the header as is; trim the badge row to Python, License and docs, and drop the Paper and Poster entries from the link bar.
- **Fewer links.** If there is no poster or slides, drop both the badge and the link-bar entry so the two rows stay in step.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Explain a staged method with a three-column table when no figure exists | Leave the method unexplained until the Install section |
| Give each optional extra its own `pip install "pkg[extra]"` line with an aligned comment | Hide extras in a single long command |
| Use the same message color for badges that point to the same thing (two paper badges at #b31b1b) | Give the paper and arXiv badges unrelated colors |
| Repeat key links in a bold ` · ` link bar for readers who skip badges | Add a website only in the link bar if the badge row is meant to be complete |
| Use `---` before sections in a long manual-style README | Stack a `---` above every heading in a short README, where the double rules look heavy |
| Tag every code block (`bash`, `ini`, `json`, `python`) | Leave the tree block untagged if a `text` tag would do |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">`: a one-line `#` title 'Name: Subtitle', then seven default flat shields.io badges as Markdown image links on consecutive lines (Paper ACL 2026 #b31b1b with a white Google Scholar logo, arXiv number #b31b1b with a white arXiv logo, 🤗 Datasets #d8b800, 🖼️ Poster #6f42c1, 📊 Slides #ea7233, License MIT #d8b800, Python 3.9+ #007ec6 with a white Python logo; labels #555555), then one bold line of five emoji-led links joined by ` · `."
2. "After the div, write a three-sentence intro with two bold phrases and a Stage / Model / Input → Output table of three rows with bold stage names and arrow notation in the last column, then one paragraph on optional steps."
3. "Write the body as plain `##` sections, each but License preceded by `---`: Install (a `bash` block of `pip install "pkg[extra]"` lines with aligned comments, then source install and an `ini` `.env` block), Quick start (numbered `# 1.` comments), an optional-feature section, a two-row mode table, custom data schemas as bold file names plus `json` blocks, data setup, a package tree, then Citation (`bibtex`) and a one-line License."

## Similar Pages

- readme-huggingface-peft: a tool-like README whose header is a centred title and one-line description followed straight by prose and a Quickstart, with no teaser; CRAFT adds a paper badge row and a stage table.
- readme-ltzheng-agent-studio: a centred `<h1>` with a row of flat badges mixing paper, project, Python and license, then manual-style sections; CRAFT adds the bold link bar and section rules.
- readme-damon-demon-spanuq: a centred title with a text link row of in-page anchors joined by `•`; CRAFT's link row instead points to external artifacts with emoji.

## Quick Start

````markdown
<div align="center">

# Name: One-Line Paper Title

[![Paper](https://img.shields.io/badge/Paper-Venue%20Year-b31b1b?logo=googlescholar&logoColor=white)](https://aclanthology.org/XXXX/)
[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/XXXX.XXXXX)
[![Hugging Face Datasets](https://img.shields.io/badge/🤗%20Datasets-Collection-yellow)](https://huggingface.co/collections/org/name)
[![Poster](https://img.shields.io/badge/🖼️-Poster-6f42c1)](site/poster.jpg)
[![Slides](https://img.shields.io/badge/📊-Slides-orange)](site/slides.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)

**[📄 Paper](https://aclanthology.org/XXXX/) · [🖼️ Poster](site/poster.jpg) · [📊 Slides](site/slides.pdf) · [🤗 Datasets](https://huggingface.co/collections/org/name) · [🌐 Website](https://org.github.io/name/)**

</div>

Name is a **key property** method for task. It reaches result with **no extra cost**.

| Stage | Model | Input → Output |
|-------|-------|----------------|
| **Stage 1** | Model A | full corpus → top 5,000 |
| **Stage 2** | Model B | 5,000 → top 100 |
| **Stage 3** | Model C | 100 → top 50 *(optional)* |

One paragraph on optional steps.

---

## Install

```bash
pip install pkg                 # core
pip install "pkg[extra]"        # + what the extra adds
```

---

## Quick start

```bash
# 1. First step
pkg preprocess --config configs/example.yaml

# 2. Second step
pkg retrieve   --config configs/example.yaml
```

---

## Modes

| Mode | How it works |
|------|--------------|
| `mode_a` *(default)* | One sentence. |

---

## Package layout

```
src/pkg/
├── cli.py               the command
└── core/                core modules
```

---

## Citation

```bibtex
@inproceedings{key-2026,
    title = "...",
}
```

## License

MIT — see [LICENSE](LICENSE).
````

## Provenance

- Repo: https://github.com/coral-lab-asu/CRAFT (`README.md`, branch `main`, last README commit 7c4be45 on 2026-07-19).
- Paper: "CRAFT: Training-Free Cascaded Retrieval for Tabular QA", ACL 2026 (Volume 1: Long Papers), aclanthology 2026.acl-long.149, arXiv 2505.14984; first author Adarsh Singh. Website https://coral-lab-asu.github.io/CRAFT/.
- Selection: the page explains the method with a three-row stage table instead of a figure, gives commented pip-extras install lines and a mode table, and separates sections with rules, a good example for a tool-like repo with no teaser image.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the seven badge URLs, the Hugging Face badge SVG.
- Written 2026-10-28.
