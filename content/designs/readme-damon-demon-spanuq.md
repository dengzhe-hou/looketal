# SpanUQ — README Reference

> A command-line tool's manual with a conference stamp: a bracketed headline, four small colored tabs, a dotted jump bar, and numbers before the first paragraph ends.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/damon-demon/SpanUQ (last commit touching the file 778b1c1, 2026-09-25; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a first-screen capture and a 2700px tall capture of the light theme with the README column 920px wide (856px content width), and the shields.io SVGs for the four badge URLs. The capture files are saved at 1200×750, a 0.833 scale of the 1440×900 window; every y value below is converted back to the 1440×900 frame. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them. The README contains no images.

## Overview

The page reads like the documentation of a command-line tool that happens to come from a paper. A centred `<h1>` with the venue in square brackets, "[NeurIPS 2026] SpanUQ: Span-Level Uncertainty Quantification for LLM Generation", wraps to two lines over GitHub's grey rule. Under it sits one row of four small 20px flat badges with a #555555 label and a colored message (blue, dark red, green, orange), then a centred row of seven in-page anchor links separated by `•`, then a `---` rule. The body starts at once with `## Overview`: a bold-led two-sentence summary, four bold-led feature bullets, and a compact five-row Results table whose top rows are already visible on the first screen. From there the page is a long sequence of `bash` blocks, each with a one-line lead, organised into numbered steps; the Quick Start shows what the tool prints, including colored status dots, and every argument, field and method gets its own small table. There is no teaser image, no author line and no news.

## Header Block

Rendered positions are y values in the 1440×900 frame (the README box starts at y≈25 with its "README.md" file bar).

1. **Title** (y≈116 and 156, two lines): `<h1 align="center">[NeurIPS 2026] SpanUQ: Span-Level Uncertainty Quantification for LLM Generation</h1>`. GitHub h1, 2em (32px), weight 600, centred, with the 1px grey rule. The venue is part of the heading text, not a separate line or badge.
2. **Badge row** (y≈200–220): one `<p align="center">` holding four `<a><img src="https://img.shields.io/static/v1?label=...&message=...&color=..."></a>` joined by ` &ensp;` (an en space) on a single source line. Each badge is 20px tall with 3px corners; the SVGs are 103, 97, 124 and 152px wide and the row spans about 515px. Details in Badges.
3. **Section nav** (y≈254): `<p align="center">` with seven `<a href="#installation">Installation</a> •` style links (Installation, Quick Start, Dataset, Training, Evaluation, Pipeline, Citation), one per source line, separated by a bullet `•`. Body size, GitHub link blue.
4. **Rule** (y≈292): `---`, GitHub's 4px #d1d9e0 bar.
5. **First section** (y≈335): `## Overview`, ruled h2, then the summary paragraph with **SpanUQ** in bold and *span level* in italics.
6. **Results table** (from y≈672): `### Results` at y≈647 and a five-column table whose header and first four rows sit inside the first 900px.

There is no logo, subtitle, author line, affiliation line, teaser or caption.

## Badges

All four use the older `static/v1?label=&message=&color=` endpoint with no `style=`, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555 and white (#ffffff) text with a #010101 text shadow, as the returned SVGs show.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Project (github-pages logo) | Page | #007ec6 (`blue`; label #555555) | flat (default) | damon-demon.github.io/SpanUQ.html |
| ArXiv (arxiv logo) | Paper | #8b0000 (`darkred`, a CSS keyword the SVG writes as `fill="darkred"`; label #555555) | flat (default) | arxiv.org/abs/2607.05721 |
| 🤖 Released | Models | #67ac09 (`green`; label #555555) | flat (default) | huggingface.co/DamonDemon/SpanUQ |
| 🤗 Hugging Face | Dataset | #ea7233 (`orange`; label #555555) | flat (default) | huggingface.co/datasets/DamonDemon/SpanUQ-Benchmark |
| (nav row) | Installation • Quick Start • Dataset • Training • Evaluation • Pipeline • Citation | GitHub link blue | plain anchor links separated by `•` | in-page anchors |

The label names the thing and the message names the kind of destination, so the pattern is reversed on the two Hugging Face badges (label "🤖 Released", message "Models"). The named colors `green` and `orange` were read from the SVGs shields.io returns today (#67ac09 and #ea7233), which differ from the older shields.io values (#97ca00 and #fe7d37); the README itself only says `green` and `orange`.

No other colors are chosen by the author. The sample output block uses the emoji 🟢 🟡 🔴 as status dots, whose color comes from the viewer's emoji font. The rules are GitHub's #d1d9e0.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred, ruled) | [NeurIPS 2026] SpanUQ: Span-Level Uncertainty Quantification for LLM Generation | title; badge row, nav row and `---` follow |
| h2 | Overview | bold-led summary, "Key features:" and four bold-led bullets |
| h3 | Results | a five-column table, Model plus four metrics with ↑/↓ in the headers |
| h2 | Installation | a `bash` clone-and-install block, a requirements list, two one-line optional `bash` installs |
| h2 | Quick Start | h3 Step 1: Download Checkpoint & Dataset; h3 End-to-End Inference (Fastest Demo) with a sample-output block; h3 Step 2: Extract Hidden States (requires GPU); h3 Step 3: Evaluate with an "Expected output" block; h3 Alternative: On-the-fly Extraction; h3 Option B: Build Dataset from Scratch |
| h2 | Dataset | one sentence with a bold dataset name, a split-size table; h3 Data Format with two field tables; h3 Preparing Data for Training with a `bash` block and a directory tree |
| h2 | Training | a `bash` block, a Key training arguments table, a two-phase bullet list; h3 Post-hoc Calibration |
| h2 | Evaluation | a `bash` block, an Available methods table; h3 Layer Probing |
| h2 | Data Construction Pipeline | a Note blockquote, a four-step text diagram; h3 Prerequisites and h3 Step 1 to Step 4, each a `bash` block |
| h2 | Project Structure | an annotated tree in an untagged code block |
| h2 | Resources | three bullets with 📄 and 🤗 and bold labels |
| h2 | Citation | a `bibtex` block |
| h2 | License | one sentence |

Absent from the source: logo, teaser or any image, author and affiliation lines, news, demo GIF or video, `<details>`, acknowledgements, contact section, star-history chart.

Present but unusual: the venue is bracketed inside the h1; the nav row duplicates GitHub's own outline menu; the Quick Start interleaves numbered steps with unnumbered alternatives, and "Option B" has no "Option A"; the Pipeline note links to `#option-1-use-pre-built-dataset-recommended`, an anchor that no heading produces; the clone command uses `github.com/DamonDemon/SpanUQ.git` while the repo lives at `damon-demon/SpanUQ` (the DamonDemon path returned 404 on 2026-10-28); the Dataset sentence says "~293K annotated spans" while its table lists 344,288 spans for each Qwen backbone.

## Components

**Bracketed venue title.** `[Venue Year] Name: Full Title` as one centred `<h1>`, letting the heading rule close the title.

**Small flat badge row.** Four `static/v1` badges on one source line separated by ` &ensp;`; label #555555, messages #007ec6, #8b0000, #67ac09, #ea7233; two carry Simple Icons logos (github-pages, arxiv), two carry emoji in the label.

**Bullet nav bar.** A centred paragraph of seven anchor links separated by `•`, followed by a `---` rule.

**Bold-led bullets.** "Key features:" followed by four bullets that each start with a bold phrase (**DETR-style span decoder**, **Mixture of Beta (MoB)**, **10–20× faster**, **Generalizes across LLM families**).

**Results table.** `| Model | AUROC ↑ | MAE ↓ | ρ_span ↑ | ρ_seq ↑ |` with `|:------|:-------:|:-----:|:--------:|:-------:|`: model names left-aligned, metrics centred, three decimals, no bold best values. GitHub renders it about 480px wide, about half the column.

**Numeric tables.** The split table right-aligns every count (`------:`) and uses thousands separators (17,468; 344,288).

**Reference tables.** Field, argument and method tables use `|:------|:-----------|` (left-aligned), with names in inline code and a dash "—" for empty defaults.

**Step headings with code.** `### Step n: Verb Phrase` followed by a one-line lead and a `bash` block with backslash-continued flags, one per line, indented four spaces.

**Sample output.** Untagged code blocks showing what the tool prints: a framed report with ═ and ─ rules and 🟢 🟡 🔴 status dots, and a plain "Expected output" metrics table.

**Inline notes.** Plain blockquotes with a bold label, `> **GPU requirement**: ...` and `> **Note**: ...`, not GitHub alert syntax.

**Annotated tree.** Untagged code blocks of box-drawing trees (`├──`, `└──`) with `# comment` annotations aligned in a column.

**Resources list.** Bullets of the form `- 🤗 **Model Checkpoints**: [org/name](url)`.

**Citation and license.** `@article{zhang2026spanuq, ...}` with `journal={arXiv preprint arXiv:2607.05721}`; one license sentence.

## Imagery

The README has no images, GIFs or videos. Its only visual elements are the four badges, GitHub tables, and code blocks; the "image" of the method is the sample output block, which shows annotated spans with 🟢 🟡 🔴 dots next to uncertainty scores, and the four-line text diagram of the data pipeline. Nothing depends on a light background, so the page reads the same on both GitHub themes.

## Adapting to Other Content

- **A library.** Keep the title without brackets, the flat badge row (Docs, PyPI, License) and the bullet nav bar; keep Installation and Quick Start as they are.
- **A dataset.** Move Dataset ahead of Installation, keep the split table with right-aligned counts and the two field tables, and add a sample-record code block.
- **A paper repo with a teaser.** Insert one `width="100%"` figure (856px) between the nav bar and the `---` rule; keep the Results table directly under Overview.
- **A method with several backbones.** Keep one row per backbone in the Results table and one config file per backbone in the tree.
- **A shorter README.** Cut the nav bar when there are fewer than five `##` sections; GitHub's outline menu covers it.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put a compact results table inside the first screen | Push numbers below install instructions |
| Show sample output after the first runnable command | Leave users to guess what a command prints |
| Give every argument, field and method its own small table | Describe flags in running prose |
| Right-align numeric columns in data tables | Center long integers |
| Number steps consistently and pair alternatives (Option A / Option B) | Leave "Option B" without an "Option A" |
| Make every in-page anchor match a real heading | Link to an anchor no heading produces |
| Use the repo's real path in the clone command | Clone from a different owner name |

## Agent Prompt Guide

1. "Write a README header: `<h1 align="center">[Venue Year] Name: Full Title</h1>`, then one `<p align="center">` with four flat `static/v1` shields joined by ` &ensp;`: Project/Page `blue` (#007ec6) with the github-pages logo, ArXiv/Paper `darkred` (#8b0000) with the arxiv logo, 🤖 Released/Models `green` (#67ac09), 🤗 Hugging Face/Dataset `orange` (#ea7233); then a centred row of anchor links separated by `•`, and a `---` rule."
2. "Open with `## Overview`: a two-sentence summary with the name in bold, 'Key features:' and four bullets that start with a bold phrase, then `### Results` with a table `| Model | Metric ↑ | Metric ↓ |` aligned `|:------|:-------:|:-----:|`, three decimals, no bold."
3. "Write Quick Start as `### Step n: Verb Phrase` headings, each with a one-line lead and a `bash` block with one flag per backslash-continued line, followed by an untagged code block showing the expected output; put arguments, fields and methods in left-aligned reference tables with names in inline code."

## Similar Pages

- readme-seohongpark-ogbench: also a tool-first README with package badges and bold-led feature bullets, but with a logo and an environment grid instead of a results table.
- readme-mdyao-photoagent: also uses tables to make the method scannable and badges right under the title, but with `for-the-badge` buttons and heavy imagery.
- readme-eku127-satnav: a fuller academic header (subtitle, authors, affiliations, teaser) in front of a similar runnable Quick Start.

## Quick Start

````markdown
<h1 align="center">[Venue Year] Name: Full Title of the Paper</h1>

<p align="center">
  <a href="https://example.github.io/name.html"><img src="https://img.shields.io/static/v1?label=Project&message=Page&color=blue&logo=github-pages"></a> &ensp;<a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/static/v1?label=ArXiv&message=Paper&color=darkred&logo=arxiv"></a> &ensp;<a href="https://huggingface.co/org/name"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%96%20Released&message=Models&color=green"></a> &ensp;<a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/static/v1?label=%F0%9F%A4%97%20Hugging%20Face&message=Dataset&color=orange"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#dataset">Dataset</a> •
  <a href="#training">Training</a> •
  <a href="#evaluation">Evaluation</a> •
  <a href="#citation">Citation</a>
</p>

---

## Overview

**Name** is a ... It ...

Key features:
- **Feature one** that ...
- **Feature two** for ...

### Results

| Model | Metric ↑ | Metric ↓ |
|:------|:-------:|:-----:|
| Backbone A | 0.000 | 0.000 |

## Installation

```bash
git clone https://github.com/owner/name.git
cd name
pip install -e .
```

## Quick Start

### Step 1: Download Checkpoint & Dataset

```bash
python scripts/download.py \
    --backbone ModelA \
    --output_dir ./data
```

Expected output:
```
Method        metric_a    metric_b
name            0.0000      0.0000
```

## Dataset

| Model | Train | Dev | Test |
|:------|------:|----:|-----:|
| Backbone A | 0 | 0 | 0 |

## Training

| Argument | Default | Description |
|:---------|:--------|:-----------|
| `--lr` | 1e-4 | Learning rate |

## Evaluation

## Project Structure

```
name/
├── pkg/        # Core library
└── scripts/    # Entry points
```

## Citation

```bibtex
@article{key,
  title={...},
}
```

## License
````

## Provenance

- Repo: https://github.com/damon-demon/SpanUQ (`README.md`, branch `main`, last README commit 778b1c1 on 2026-09-25).
- Paper: "SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation", NeurIPS 2026 (arXiv 2607.05721); first author Yimeng Zhang. The README's h1 shortens the title to "for LLM Generation", and its BibTeX is an arXiv `@article`. Project page https://damon-demon.github.io/SpanUQ.html.
- Selection: the bracketed-venue title, one row of styled badges and an inline section nav bar sit above a compact results table, and the step-numbered Quick Start includes sample output, a good pattern for a tool-style repo.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), first-screen and 2700px captures at a 920px README column, shields.io SVGs for all four badge URLs, a GitHub API check of the clone path in the Installation block.
- Written 2026-10-28.
