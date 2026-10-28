# ReTAS — README Reference

> A paper title page that turns into a picture book: two neat rows of square-cornered tags, a bold-named author block, a ruled break, then a cartoon of the actor and the observer arguing over a clock.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/unikcc/ReTAS (last commit touching the file e2824a8, 2026-04-29; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and sizes come from the SVGs that shields.io returns for the badge URLs; image sizes and image colors come from the PNGs in `assets/` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The whole header sits inside one `<div align="center">`. A two-line `<h1>` paper title (broken with `<br/>`) carries GitHub's grey bottom rule, then two separate rows of `flat-square` shields.io badges: five link badges (project page, paper, code, license, data) in the default grey-label form, and four technology badges (PyTorch, Python, DeepSpeed, vLLM) on a darker #333333 label, three of them with no label text at all. Eight bold linked author names in two lines with superscript affiliation numbers, two lines of affiliations, a Markdown `---` rule and a 75%-width cartoon teaser close the header; the teaser fills most of the first screen. The body is short and plain: seven `##` sections without emoji (Overview, Setup, Data, Modules, Results, Citation, License), a full-width method figure under a two-sentence overview, one `bash` block, a numbered data checklist, a four-row module path table, three result charts set two-up at 49% width, BibTeX and a one-word license line. There is no news list and no numeric results table; results are shown only as chart images.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Wrapper**: `<div align="center">` opens on the first line and closes after the teaser, so everything down to the teaser is centred without per-element `align`.
2. **Title** (y≈139–180, two lines): `<h1>Taming Actor-Observer Asymmetry in Agents<br/>via Dialectical Alignment</h1>`. GitHub h1, 2em (32px), weight 600, with the 1px grey rule under the second line across the 856px content width. The repo name "ReTAS" never appears in the header; the paper title is the title.
3. **Link badge row** (y≈234): `<p align="center">` with five `<a><img src="https://img.shields.io/badge/...?style=flat-square..."></a>` lines. Each badge is 20px tall with square corners; the row spans about 559px. The Paper badge links to `#`, so it is a label rather than a working link.
4. **Technology badge row** (y≈276): a second `<p align="center">` with four badges that add `labelColor=333`; the row spans about 346px. PyTorch, DeepSpeed and vLLM use an empty label (`/badge/-PyTorch-EE4C2C`), so only the logo (or nothing, for DeepSpeed) sits in the dark left part.
5. **Authors** (y≈320 and 344): one `<p align="center">` with each name as `<b><a href="...">Name</a></b><sup>n</sup>&nbsp;`, broken after the fifth name with `<br/>`. Names render in GitHub link blue and bold. Two names link to `#`. `*` on the fifth author marks the corresponding author by convention; the README never defines it (inferred).
6. **Affiliations** (y≈385 and 409): `<p align="center">` with `<sup>1</sup>National University of Singapore&nbsp;&nbsp;` entries and a `<br/>` after the third, so five institutions sit in two lines of body text.
7. **Rule** (y≈446): a Markdown `---` inside the div, which GitHub renders as its 4px light grey `<hr>` across the full content width.
8. **Teaser** (y≈478–848): `<img src="assets/hero.png" width="75%" alt="ReTAS"/>` with no link and no caption. The 1619×971 PNG renders at 642×385; its own pale margins make the drawn panel look about 620px wide in the capture.
9. **Overview heading** lands at the fold (y≈894), so the first screen ends exactly with the teaser.

## Badges

All nine use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` with `style=flat-square`: 20px tall, square corners (no `rx`), no gloss, Verdana 11px, white text except on the yellow message, where shields.io switches to #333333.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Project (Chrome logo, white) | Page | #007ec6 (`blue`; label #555555) | flat-square | unikcc.github.io/ReTAS/ |
| Paper (inline ACL logo, red #ed1c24) | ACL 2026 | #dd4343 (`red` as shields.io now renders it; label #555555) | flat-square | `#` (no target) |
| Code (GitHub logo) | GitHub | #000000 (`black`; label #555555) | flat-square | github.com/unikcc/ReTAS |
| License | MIT | #67ac09 (`green` as shields.io now renders it; label #555555) | flat-square | opensource.org/licenses/MIT |
| Data (Hugging Face logo, white) | HuggingFace | #ffd21e (label #555555, message text #333333) | flat-square | huggingface.co/datasets/BradNLP/ReTAS |
| (empty; PyTorch logo #ee4c2c) | PyTorch | #ee4c2c (label #333333) | flat-square | pytorch.org |
| Python (Python logo #ffd43b) | 3.10+ | #3776ab (label #333333) | flat-square | python.org/downloads/ |
| (empty, no logo) | DeepSpeed | #0078d4 (label #333333) | flat-square | github.com/microsoft/DeepSpeed |
| (empty; lightning logo #ff6f00) | vLLM | #ff6f00 (label #333333) | flat-square | github.com/vllm-project/vllm |

The first row is "what the project offers" (label = category, message = destination); the second row is "what it is built with", where each message color is the tool's own brand color and the logo is tinted to match it with `logoColor`. The Paper logo is a base64 Inkscape SVG passed as `logo=data:image/svg%2Bxml;base64,...`, whose fill is #ed1c24; `logoColor=white` does not recolor it. There is no bold text link row.

Image colors used below: the teaser's two halves are pale peach #f7e5dc (actor side) and pale blue #d9e1f2 (observer side), read as the most frequent pixels of `hero.png`.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | Taming Actor-Observer Asymmetry in Agents / via Dialectical Alignment | title; badges, authors, affiliations, rule and teaser follow inside the same centred div |
| h2 | Overview | two sentences with bold **Actor-Observer Asymmetry (AOA)** and **ReTAS**, the expansion of the acronym with bold initial letters, then a centred full-width framework figure |
| h2 | Setup | one `bash` block (uv install, clone, venv, two commented `uv pip install -e ".[train]"` lines), then one paragraph of version caveats with inline code |
| h2 | Data | one sentence with the gated Hugging Face link, then a three-step numbered list mixing a bold button name, inline code and an autolink |
| h2 | Modules | one sentence, then a two-column Path / Description table whose paths are linked inline code |
| h2 | Results | three chart PNGs in two centred divs, two at 49% side by side and one at 49% alone |
| h2 | Citation | a `bibtex` block, no lead sentence |
| h2 | License | the single word "MIT." |

Absent from the source: news or changelog, a numeric results table, demo GIF or video, model zoo or checkpoint links, quick-run example, table of contents, acknowledgements, contact, emoji in headings.

Present but unusual: the h1 is the full paper title rather than the project name; there are two badge rows with different label colors; two badges and two author links point to `#`; the abstract is replaced by a two-sentence Overview; results exist only as images, with a lone third chart that leaves the right half of its row empty.

## Components

**Centred wrapper.** One `<div align="center">` around the header, with each block inside as its own `<p align="center">` (the `align` is repeated though the div already centres). Blank lines around the Markdown `---` and the `<img>` let GitHub parse them inside the div.

**Two badge rows.** Row 1: `<a href="..."><img src="https://img.shields.io/badge/Label-Message-color?style=flat-square&logo=...&logoColor=white" alt="..."/></a>`, label #555555, messages #007ec6, #dd4343, #000000, #67ac09, #ffd21e. Row 2: `?style=flat-square&labelColor=333&logo=<tool>&logoColor=<brand hex>`, label #333333, messages #ee4c2c, #3776ab, #0078d4, #ff6f00. One badge per source line; GitHub renders the line breaks as single spaces.

**Bold author links.** `<b><a href="...">Name</a></b><sup>n</sup>&nbsp;` per author, a `<br/>` to split the list, affiliations in a separate paragraph with `&nbsp;&nbsp;` between entries.

**Code block.** One `bash` block with blank lines between the uv bootstrap, the clone-and-venv group and the install group; trailing `# comments` aligned with spaces to say what each extra installs.

**Numbered checklist.** Data access as a 1–3 ordered list: an action with the button name in bold, a command in inline code with an autolink `<https://...>`, and a script in inline code.

**Module path table.** `|---|---|` delimiters, no alignment colons. Left cells are links whose text is inline code (`` [`FinQA/`](FinQA/) ``); right cells are one short description with counts ("166 SQLite DBs", "10 domains × 2 scenarios"). GitHub centres the header cells and stripes alternate rows.

**Chart grid.** `<div align="center">` holding `<img width="49%">` pairs, each with a descriptive `alt`; a second div holds the odd chart.

**Citation and license.** A `bibtex` `@inproceedings{li2026taming,...}` block with the full author list, and "MIT." as the entire License section.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| hero.png | PNG cartoon, pastel panels on white | 1619×971 | `<img width="75%">` in the header div | 642×385 | after the `---` rule, closes the header; no caption |
| framework_overview.png | PNG three-panel method diagram (a, b, c) on white | 1888×1098 | `<img width="100%">` in `<div align="center">` | 856×498 | end of Overview |
| acc_bar.png | PNG bar chart | 928×514 | `<img width="49%">` | 419×232 | Results, left of first pair |
| aoa_mitigation.png | PNG bar chart | 885×478 | `<img width="49%">` | 419×226 | Results, right of first pair |
| exp_line.png | PNG line chart | 888×509 | `<img width="49%">` in its own div | 419×240 | Results, centred alone |

The teaser is split top and bottom: a human "Actor" and "Observer" around a clock on a peach-to-blue background, then "The Mirror Effect" band with an Executor agent and a Reviewer agent around a Python error box, red attribution labels on the left and blue on the right. The method figure uses boxed panels labelled a) Attribution Data Generation, b) Dialectical Synthesis, c) Dialectical Alignment, with thin colored outlines. The charts are paper figures pasted as PNGs, light blue and pink bars with hatched variants. Nothing uses `<picture>`, GIF or video.

## Adapting to Other Content

- **A library.** Keep the centred div, put the package name in the h1, keep both badge rows (offers on #555555 labels, stack on #333333 labels) and drop authors and affiliations; replace the teaser with a `width="75%"` (642px) diagram.
- **A dataset.** Keep the full header; promote the Data checklist to the first section and make the Modules table list splits or subsets with counts in the description column.
- **A benchmark with scores.** Keep the chart grid at 49% (419px each) but add a numeric table under it; ReTAS itself has none, so this is an extension.
- **A repo without a teaser.** End the header with the `---` rule and let the full-width method figure (856px) under Overview carry the first image.
- **Fewer tools.** If the stack is one or two items, fold them into the first row rather than leaving a short second row.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Wrap the header in one `<div align="center">` and keep each block a paragraph | Mix left- and centre-aligned blocks in the header |
| Use `flat-square` for every badge in both rows | Mix `flat`, `for-the-badge` and `flat-square` |
| Separate "offers" badges (label #555555) from "built with" badges (label #333333) | Put license, Python and paper badges in one undifferentiated row |
| Tint tool logos with their brand color (`logoColor=EE4C2C`) | Leave an empty-label badge with a blank dark stub, as the DeepSpeed badge does |
| Set the teaser at `width="75%"` under a `---` rule | Let the rule and the teaser compete with a caption block |
| Lay result charts two-up at `width="49%"` | Shrink charts below about 400px rendered |
| Point every badge and author link at a real target | Leave `href="#"` placeholders as ReTAS does for the paper and two authors |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown inside one `<div align="center">`: an `<h1>` with the full paper title broken in two with `<br/>`, then a `<p align="center">` row of five `flat-square` shields.io badges on the default #555555 label (Project Page #007ec6, Paper #dd4343, Code GitHub #000000, License MIT #67ac09, Data HuggingFace #ffd21e) and a second row of four tool badges with `labelColor=333` (PyTorch #ee4c2c, Python 3.10+ #3776ab, DeepSpeed #0078d4, vLLM #ff6f00), logos tinted with `logoColor`."
2. "Under the badges, add a centred author paragraph of `<b><a>Name</a></b><sup>n</sup>&nbsp;` entries split by one `<br/>`, a centred two-line affiliation paragraph, a Markdown `---`, and a teaser `<img width="75%">` with no caption; close the div."
3. "Write the body as plain `##` sections without emoji: Overview (two sentences plus a `width="100%"` method figure), Setup (one `bash` block with aligned `#` comments), Data (a three-step numbered list), Modules (a Path / Description table with inline-code links), Results (charts at `width="49%"`, two per centred div), Citation (`bibtex`), License (one word)."

## Similar Pages

- readme-mdyao-photoagent: also a centred header with Chrome-logo "Project Page" and logo badges, but in `for-the-badge` style with a small icon above the title; ReTAS uses the quieter `flat-square` and adds a second, darker-label row for the tool stack.
- readme-donaldssh-k-merge: an ACL 2026 README with a centred div, superscript author list and a bold venue line; it puts authors before badges, where ReTAS puts both badge rows first.
- readme-eku127-satnav: the same "title, badges, authors, affiliations, big teaser" first screen, but SatNav splits project name and paper title into h1 and h2 and uses one flat badge family with a caption under the teaser.

## Quick Start

````markdown
<div align="center">

<h1>Full Paper Title, First Half<br/>Second Half</h1>

<p align="center">
<a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/Project-Page-blue?style=flat-square&logo=googlechrome&logoColor=white" alt="Project Page"/></a>
<a href="https://aclanthology.org/XXXX/"><img src="https://img.shields.io/badge/Paper-Venue%20Year-red?style=flat-square" alt="Paper"/></a>
<a href="https://github.com/org/name"><img src="https://img.shields.io/badge/Code-GitHub-black?style=flat-square&logo=github" alt="Code"/></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/></a>
<a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/badge/Data-HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=white" alt="Dataset"/></a>
</p>

<p align="center">
<a href="https://pytorch.org/"><img src="https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat-square&labelColor=333&logo=pytorch&logoColor=EE4C2C" alt="PyTorch"/></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&labelColor=333&logo=python&logoColor=FFD43B" alt="Python"/></a>
<a href="https://github.com/microsoft/DeepSpeed"><img src="https://img.shields.io/badge/-DeepSpeed-0078D4?style=flat-square&labelColor=333" alt="DeepSpeed"/></a>
<a href="https://github.com/vllm-project/vllm"><img src="https://img.shields.io/badge/-vLLM-FF6F00?style=flat-square&labelColor=333&logo=lightning&logoColor=FF6F00" alt="vLLM"/></a>
</p>

<p align="center">
<b><a href="https://example.org/">Author One</a></b><sup>1</sup>&nbsp;
<b><a href="https://example.org/">Author Two</a></b><sup>2*</sup>
<br/>
<b><a href="https://example.org/">Author Three</a></b><sup>1</sup>
</p>

<p align="center">
<sup>1</sup>Institution A&nbsp;&nbsp;
<sup>2</sup>Institution B
</p>

---

<img src="assets/hero.png" width="75%" alt="ProjectName"/>

</div>

## Overview

Two sentences naming the problem in **bold** and the method in **bold**.

<div align="center">
<img src="assets/framework_overview.png" width="100%" alt="Framework overview"/>
</div>

## Setup

```bash
git clone https://github.com/org/name.git && cd name
uv venv --python 3.10
source .venv/bin/activate

uv pip install -e ".[train]"         # what this extra installs
```

## Data

1. Visit the dataset page, click **Agree and access**.
2. `hf auth login` with a Read token.
3. `bash scripts/download_data.sh`

## Modules

| Path | Description |
|---|---|
| [`TaskA/`](TaskA/) | Short description with a count |

## Results

<div align="center">
<img src="assets/chart_a.png" width="49%" alt="Chart A"/>
<img src="assets/chart_b.png" width="49%" alt="Chart B"/>
</div>

## Citation

```bibtex
@inproceedings{key2026,
  title={...},
}
```

## License

MIT.
````

## Provenance

- Repo: https://github.com/unikcc/ReTAS (`README.md`, branch `main`, last README commit e2824a8 on 2026-04-29).
- Paper: "Taming Actor-Observer Asymmetry in Agents via Dialectical Alignment", ACL 2026; first author Bobo Li. Project page https://unikcc.github.io/ReTAS/.
- Selection: the academic header (centred title, two coordinated badge rows, author and affiliation block) is followed by an illustrated teaser, a labelled method figure, a module path table and result charts, so the page shows a very complete paper-to-code layout.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for all nine badge URLs, the five PNGs in `assets/` fetched for pixel sizes and teaser colors.
- Written 2026-10-28.
