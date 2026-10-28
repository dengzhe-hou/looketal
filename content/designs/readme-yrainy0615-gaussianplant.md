# GaussianPlant — README Reference

> A field notebook pressed flat: a sprouting title, two dark tags, a university seal, then one wide hand-annotated plant diagram and a quoted abstract before the lab manual starts.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/Yrainy0615/GaussianPlant (last commit touching the file 3c70adf, 2026-10-14; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the two badge URLs; teaser colors come from the fill and stroke values inside `configs/teaser_gsplant.svg` fetched from the repo, and the logo color from the pixels of `assets/osaka_logo.png`. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The whole header is one `<div align="center">` with plain Markdown inside it, so the title, subtitle, author line and badges are real Markdown elements that GitHub centres. A seedling emoji leads the h1, an h3 carries the full paper title, a bold author line separates four names with middle dots, and two flat badges sit on one line. A 64px square university logo follows, then a full-width SVG teaser (856×425) that shows multi-view input turning into green "Leaf-wise reconstruction" and orange "Branch extraction" outputs. Below the div a left-ruled blockquote gives a five-line summary with bold key terms. From there the README is a dense working manual: `---` rules between every h2, a nested contents list, numbered bold install steps, three kinds of GitHub alert callouts (Note, Important, Warning), an annotated directory tree, an ASCII pipeline diagram, flag tables with centred default columns, a small Chamfer results table, a collapsed legacy command and a BibTeX block. There is no news list and no project-page or dataset badge.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Wrapper**: `<div align="center">` opens on the first line, with a blank line after it so the Markdown inside is parsed. It closes after the teaser.
2. **Title** (y≈140): `# 🌱 GaussianPlant`. GitHub h1, 2em (32px), weight 600, centred, with the 1px grey rule under it across the 856px content width. The seedling emoji renders at text size before the name.
3. **Subtitle** (y≈206): `### Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants`. GitHub h3, 1.25em (20px), weight 600, no rule, one line at 856px.
4. **Authors** (y≈246): `**Yang Yang · Risa Shinoda · Hiroaki Santo · Fumio Okura**`. One bold body-size line, names separated by ` · ` (space, middle dot, space), no links, no affiliation marks.
5. **Badge row** (y≈283): two Markdown badges, `[![arXiv](https://img.shields.io/badge/arXiv-2512.14087-b31b1b.svg)](https://arxiv.org/abs/2512.14087)` and `[![GitHub](https://img.shields.io/badge/GitHub-GaussianPlant-181717.svg?logo=github)](https://github.com/Yrainy0615/GaussianPlant)`, on consecutive source lines so they render side by side with one space between them (116px and 151px wide, 20px tall).
6. **Affiliation logo** (y≈316–380): `<a href="http://cvl.ist.osaka-u.ac.jp/en/"><img height="64" src="assets/osaka_logo.png"></a>`. The source PNG is 225×225, so it renders 64×64: a white emblem on navy #2d287f. It is the only statement of affiliation in the header, and it links to the lab page.
7. **Teaser** (y≈395 to about 820): `<img src="configs/teaser_gsplant.svg" width="100%">`. The SVG has a 250.3×124.3 viewBox and no background rectangle, so it renders 856×425 on the page background. It has no `alt` and no link. `</div>` closes right after it.
8. **Summary quote** (y≈840, crossing the fold): a five-line Markdown blockquote (`> **GaussianPlant** jointly recovers a plant's **appearance** and its **structure** ...`) with bold key terms. GitHub draws it with a 4px grey left bar and grey text. It sits outside the centred div, so it is left-aligned.
9. **Rule**: `---` after the quote, the first of the rules that fence every h2 section.

## Badges

Both badges use the static path form with a `.svg` suffix and no `style=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, Verdana 11px, label on the default #555555 grey, white message text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2512.14087 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2512.14087 |
| GitHub (with GitHub logo) | GaussianPlant | #181717 (label #555555) | flat (default), `logo=github` | github.com/Yrainy0615/GaussianPlant |

The second badge links back to the repository the reader is already on. Both message colors are dark (arXiv red and GitHub near-black), so the row reads as two dark chips rather than a colorful strip.

Other colors on the page come from images and GitHub itself, not from badges. The teaser uses label green #4ea72e on a light green arrow #b4e5a2 for "Leaf-wise reconstruction", label orange #e97132 on a salmon arrow #f6c6ad for "Branch extraction", pure red #ff0000 for the extracted branch skeleton, and grey camera frustums (#a6a6a6 strokes). The affiliation logo is navy #2d287f. GitHub's alert callouts draw their left bar and title in fixed colors: Note blue #0969da, Important purple #8250df, Warning amber #9a6700.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | 🌱 GaussianPlant | title only |
| h3 (centred) | Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants | subtitle; authors, badges, logo and teaser follow inside the same div; the summary blockquote and a rule follow outside it |
| h2 | Contents | a bulleted list of nine links, with Step 1 and Step 2 nested under Pipeline |
| h2 | Installation | test environment sentence, three bold numbered steps ("**1. Clone (with submodules)**", "**2. Environment**", "**3. Verify**"), each with a `shell` block, then a Note alert (with its own `shell` block) and an Important alert |
| h2 | Dataset | one sentence, a bold "Download link:" with a bare Google Drive URL, one sentence pointing to Data layout |
| h2 | Data layout | one sentence, an untagged code block with an annotated directory tree, a Note alert with four bulleted caveats |
| h2 | Pipeline | an untagged code block holding an ASCII flow (`images ─▶ [1a] ... ─▶ [2] Structure extraction`) |
| h3 | Step 1 — Feature 3DGS pretraining | bold run-in labels "**1a · Per-view features**" and "**1b · Distillation**" with italic notes, an Important alert, a `shell` block, and a two-column "Step-2 input contract" table |
| h3 | Step 2 — Structure extraction (this repo) | the training command in a `shell` block with backslash continuations, a bulleted flag glossary with bold flag names, an outputs table, a three-row Chamfer table, a `<details>` legacy command and a Warning alert |
| h2 | Parameters to tune | a three-column flag table with a centred default column, then "**Recommended defaults**" bullets |
| h2 | Optional: semantic-only branch/leaf labelling | one paragraph, a `shell` block, and a Warning alert |
| h2 | Evaluation | metric sentence, a `shell` block with a trailing comment, a Note alert |
| h2 | Citation | a `bibtex` block only |

Absent from the source: news or changelog, project-page, dataset or model badges, demo GIF or video, license section, acknowledgements, contact line, star chart, emoji in section headings.

Present but unusual: the subtitle is an h3, not bold text; the affiliation is shown only as a 64px logo, with no text affiliation line; the GitHub badge links to the repository itself; the Contents list omits the "Optional: semantic-only branch/leaf labelling" section; seven alert callouts (three Note, two Important, two Warning) carry most of the caveats; the README describes changes "before Oct 2026" in a collapsed legacy block, so it is maintained as a changing lab manual rather than a frozen release page.

## Components

**Centred Markdown wrapper.** `<div align="center">`, a blank line, then ordinary Markdown (`#`, `###`, `**...**`, badge links), then `</div>`. Unlike per-element `<p align="center">` blocks, this keeps the title a real `#` heading with its rule.

**Badge pair.** Two `[![Alt](https://img.shields.io/badge/Label-Message-HEX.svg)](url)` lines; label grey #555555, messages #b31b1b and #181717, the second with `?logo=github`.

**Section rules.** `---` before every h2 from Contents to Citation, so each section starts with a thick grey GitHub rule (4px, the `hr` style) followed by the h2's own 1px rule.

**Nested contents list.** `- [Installation](#installation)` style bullets, with two-space-indented children for Step 1 and Step 2. The anchors follow GitHub's slug rule, including the doubled hyphen from the em dash (`#step-1--feature-3dgs-pretraining`).

**Bold numbered steps.** Install steps are bold paragraphs ("**1. Clone (with submodules)**") above a fenced `shell` block, not an ordered list, so each command block sits at full width.

**Alert callouts.** `> [!NOTE]`, `> [!IMPORTANT]` and `> [!WARNING]` blocks. Each starts with a bold sentence that states the rule ("**Do not add `--reg_overlap`.**", "**Use the provided PCA basis for the 128-d projection — don't fit your own.**") and then explains it. Alerts can hold bullets and fenced code. GitHub draws a colored left bar and icon title: Note #0969da, Important #8250df, Warning #9a6700.

**Code blocks.** `shell` for every command, `bibtex` for the citation, and untagged fences for the directory tree and the ASCII pipeline. Tree lines use box-drawing characters with right-hand `#` comments aligned in one column, and capitals mark what matters ("PRODUCED", "EVALUATION ONLY").

**Flag glossary.** A bulleted list where each item starts with the flag in bold code (`**`--label_init hybrid`**`), an em dash, and one to four sentences of explanation, with italics for named ideas (*Path traffic*).

**Tables.** Two- and three-column pipe tables with lowercase headers (`| asset | description |`, `| file | content |`, `| flag | default | what it controls / when to change |`). Column alignment is set only where values are short: `:---:` for defaults and for the two Chamfer columns. The best Chamfer value (56.9) is bold, and an en dash marks a missing cell. A one-sentence caption above the results table states the unit and averaging ("Mean branch Chamfer over newplant1–10 at 7k (mm, mean of both directions)"), and a sentence below states that each number is a single run.

**Collapsible legacy block.** `<details><summary>Legacy pipeline (joint colour/geometry/semantic init, before Oct 2026)</summary>` wrapping a `shell` block, collapsed by default.

**Citation.** A `bibtex` `@article{yang2025gaussianplant, ...}` block with aligned `=` signs and no lead sentence.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| osaka_logo.png | PNG, white emblem on navy | 225×225 | `<img height="64">` inside `<a>` to the lab page | 64×64 | header, between badges and teaser |
| teaser_gsplant.svg | SVG with embedded raster plant renders, transparent background | viewBox 250.3×124.3 | `<img width="100%">`, no `alt`, no link | 856×425 | header, last element inside the centred div |

The teaser reads left to right: a stack of input photos and four camera frustums around a reconstructed plant labelled "GaussianPlant" in black serif type, then two arrows, a light green one labelled "Leaf-wise reconstruction" in green #4ea72e and a salmon one labelled "Branch extraction" in orange #e97132. The leaf arrow ends at segmented leaves with green dotted circles and two round zoom insets outlined in #b4e5a2; the branch arrow ends at a bare branch with a red #ff0000 skeleton. The label type is a serif face embedded as paths in the SVG (inferred from the capture; the SVG holds glyph outlines, not font names).

No `<picture>` or dark variant is used, and the SVG has no background, so the black "GaussianPlant" label and the grey frustums would sit directly on GitHub's dark background; the README is designed for the light theme. All later figures are text: the ASCII pipeline and the directory tree.

## Adapting to Other Content

- **A library.** Keep the `<div align="center">` with `# emoji Name`, an h3 one-line description and the two-badge row (swap arXiv for a PyPI or Docs badge in the same flat #555555-label form), drop the logo, and put the summary blockquote straight under the div. Keep `---` rules and the nested Contents list.
- **A dataset.** Keep the header and replace the teaser with a sample grid at `width="100%"` (856px). Promote Dataset and Data layout to the first two sections and keep the annotated tree with aligned `#` comments and capitalised warnings.
- **A benchmark with scores.** Expand the small Chamfer table into the main results table: caption sentence above stating unit and averaging, `:---:` numeric columns, best value in bold, a single-run or seed-count sentence below.
- **A repo without a teaser.** End the div after the logo (64px tall) and let the blockquote summary carry the first screen; an ASCII pipeline in an untagged block can stand in for the figure.
- **A multi-environment research repo.** Reuse the Note / Important / Warning pattern: Note for toolchain fixes, Important for separate environments or required assets, Warning for flags or fallbacks to avoid, each opening with a bold rule sentence.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Wrap the header in one `<div align="center">` and keep real `#` and `###` headings inside it | Fake the title with a large image when a heading will do |
| Keep both badges flat with the #555555 label and dark messages | Add a badge row of a dozen colors for a two-link repo |
| Give the teaser `width="100%"` so it spans the 856px column | Let a transparent SVG with black labels assume a white page without testing dark mode |
| Open each alert with a bold sentence that states the rule | Bury a "do not use this flag" warning in a paragraph |
| Put `---` before every h2 so the long manual reads as separate cards | Mix rules before some sections and not others |
| State unit, averaging and run count around the results table | Show a bold best value without saying it is one run |
| Collapse superseded commands in `<details>` | Delete the legacy command or leave it inline next to the current one |
| Keep the Contents list in sync with every h2 | Leave a section out of the list, as the Optional section is here |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside one `<div align="center">` (blank line after the tag): `# 🌱 ProjectName`, `### Full paper title`, a bold author line with names separated by ` · `, two flat shields.io badges on consecutive lines (arXiv-ID with message #b31b1b and GitHub-Name with message #181717 and `logo=github`, both on the default #555555 label), a lab logo `<img height="64">` linked to the lab page, and a teaser `<img width="100%">`. Close the div, add a five-line blockquote summary with bold key terms, then `---`."
2. "After the header, write `---`-fenced h2 sections in this order: Contents (nested bullet links), Installation (bold numbered steps each above a `shell` block), Dataset, Data layout (untagged annotated tree), Pipeline (ASCII flow, then h3 Step 1 and Step 2), Parameters to tune, Evaluation, Citation (`bibtex` only). No emoji in section headings."
3. "Write caveats as GitHub alerts: `> [!NOTE]` for toolchain fixes, `> [!IMPORTANT]` for separate environments or required assets, `> [!WARNING]` for flags not to use; start each with a bold rule sentence. Write flag tables with lowercase headers and a `:---:` default column, and put superseded commands in `<details><summary>Legacy pipeline (...)</summary>`."

## Similar Pages

- **readme-shjo-april-trace** also wraps its whole header in a single `<div align="center">` with real Markdown headings inside; TRACE uses `for-the-badge` shields and an award line where GaussianPlant uses two flat badges and a logo.
- **readme-eku127-satnav** shares the centred title page and full-width teaser but builds it from separate `<p align="center">` blocks with linked authors and affiliations, and keeps the body short and link-driven where GaussianPlant's body is a long manual of alerts and flag tables.
- **readme-deepseek-ai-deepseek-v3** is the other README in this batch that leans on GitHub Note callouts, there as table footnotes rather than environment caveats.

## Quick Start

````markdown
<div align="center">

# 🌱 ProjectName

### Full Paper Title on One Line

**Author One · Author Two · Author Three · Author Four**

[![arXiv](https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg)](https://arxiv.org/abs/XXXX.XXXXX)
[![GitHub](https://img.shields.io/badge/GitHub-ProjectName-181717.svg?logo=github)](https://github.com/org/ProjectName)

<a href="https://lab.example.org/"><img height="64" src="assets/lab_logo.png"></a>

<img src="assets/teaser.svg" width="100%">

</div>

> **ProjectName** does X from Y. Name the two **key outputs** in bold and say
> what it needs and what it does not need.

---

## Contents

- [Installation](#installation)
- [Data layout](#data-layout)
- [Pipeline](#pipeline)
  - [Step 1 — First stage](#step-1--first-stage)
  - [Step 2 — Second stage](#step-2--second-stage)
- [Evaluation](#evaluation)
- [Citation](#citation)

---

## Installation

Tested on OS with GPU (CUDA version).

**1. Clone (with submodules)**

```shell
git clone https://github.com/org/ProjectName.git --recursive
cd ProjectName
```

**2. Environment**

```shell
conda create -y -n env python=3.10
pip install -r requirements.txt
```

> [!NOTE]
> Toolchain caveat and the fix.

> [!IMPORTANT]
> **What this step needs and what it does not.** Explanation.

---

## Data layout

```
<root_path>/
├── shared_asset.pth                # what it is
└── <scene>/
    └── result.ply                  # EVALUATION ONLY
```

---

## Pipeline

```
 input ─▶ [1] first stage ─▶ [2] second stage
```

### Step 1 — First stage

### Step 2 — Second stage

| file | content |
|------|---------|
| `output.ply` | what it holds |

<details>
<summary>Legacy pipeline (what changed, when)</summary>

```shell
python train.py --old_flags
```
</details>

> [!WARNING]
> **Do not use `--flag`.** Why.

---

## Evaluation

| setting | metric A | metric B |
|---------|:--------:|:--------:|
| baseline | 0.0 | – |
| ours | 0.0 | **0.0** |

---

## Citation

```bibtex
@article{key,
  title   = {...},
}
```
````

## Provenance

- Repo: https://github.com/Yrainy0615/GaussianPlant (`README.md`, branch `main`, last README commit 3c70adf on 2026-10-14).
- Paper: the README itself describes "GaussianPlant: Structure-aligned Gaussian Splatting for 3D Reconstruction of Plants" (arXiv 2512.14087; Yang Yang, Risa Shinoda, Hiroaki Santo, Fumio Okura). The gallery's selection record lists this repo under "NeuraLeaf: Neural Parametric Leaf Models with Shape and Deformation Disentanglement", ICCV 2025, first author Yang Yang; the README does not mention NeuraLeaf or ICCV, so the venue in the catalog comes from the selection record, not from this page.
- Selection: an illustrated teaser is followed by a quoted summary and a nested contents list, and GitHub Note and Important alert callouts are used well for environment caveats.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for both badge URLs, `configs/teaser_gsplant.svg` and `assets/osaka_logo.png` fetched from the repo for colors and sizes.
- Written 2026-10-28.
