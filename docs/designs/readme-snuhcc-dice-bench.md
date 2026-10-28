# DICE-BENCH — README Reference

> A game-night box lid on a lab bench: one big charcoal banner with a white die, the long paper title in plain type, four bright tags, then tidy reference tables under emoji signposts.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/snuhcc/DICE-Bench (last commit touching the file d4fa0bd, 2025-07-01; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the four badge URLs; image sizes and colors come from `media/banner.png`, `media/pipeline.png` and `media/baseline_comparison.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The first screen is dominated by a full-width charcoal banner (856×334): a large white die with one orange-red pip on its top face at the left, and "DICE-BENCH" in heavy white sans-serif with the two-line subtitle "Evaluating the Tool-Use Capabilities of LLMs in Multi-Round, Multi-Party Dialogues" at the right. Under it the full paper title is repeated as a left-aligned h1 that wraps to two lines, followed by a centred row of four flat badges and a `---` rule. The body is a sequence of emoji-led sections, each fenced by `---`: a dated News list under an h3, an Overview with a pipeline figure, five key-point bullets and a comparison-table image, then two pipe tables (Directory Layout and Core Scripts) that serve as the reference core, an annotated data tree, a three-step Quick Start with `bash` blocks, a numbered experiment list, BibTeX and a contact line. There is no install badge, no results table in Markdown and no author list.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Banner** (y≈94–427): `<p align="center"><img src="media/banner.png" alt="DICE-BENCH Banner" style="width: 100%;"></p>`. GitHub keeps the inline style (rendered HTML: `style="width: 100%; max-width: 100%;"`), so the 1528×596 PNG renders 856×334. Background charcoal #282828, die faces #f2f3f3 and #d1d1d1, pip #f1552c.
2. **Title** (y≈462–534): `# DICE-BENCH: Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues`. A plain Markdown h1, left-aligned, 2em (32px), weight 600, wrapping to two lines at 856px, with the 1px grey rule under it.
3. **Badge row** (y≈574): `<p align="center">` holding four `<a href="..." target="_blank"><img src="https://img.shields.io/badge/..."></a>` lines. GitHub strips `target="_blank"`. Each badge is 20px tall and the row spans about 442px. None of the `<img>` tags has an `alt`.
4. **Rule** (y≈616): `---`, GitHub's 4px grey `hr`.
5. **News** (y≈656 onward): `### ✨ News (DICE-BENCH)`, an h3 with a sparkles emoji, then four bullets. The News list fits on the first screen; the "📖 Overview" h2 lands at the fold (y≈883).

## Badges

All four use the static path form with no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, Verdana 11px, label on the default #555555 grey, white message text. Three use named colors; the hex values below are the fills in the SVGs that shields.io returns on 2026-10-28, which are what the capture shows.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| arXiv | 2506.22853 | `red`, rendered #dd4343 (label #555555) | flat (default) | arxiv.org/abs/2506.22853 |
| Project | Page | `blue` #007ec6 (label #555555) | flat (default) | snuhcc.github.io/DICE-Bench/ |
| 🤗 Hugging Face | Space | `orange`, rendered #ea7233 (label #555555) | flat (default) | huggingface.co/datasets/OfficerChul/DICE-BENCH |
| Code | GitHub | `brightgreen`, rendered #44bb00 (label #555555) | flat (default) | github.com/snuhcc/DICE-Bench |

The METHOD_README named-color table gives `red` #e05d44, `orange` #fe7d37 and `brightgreen` #4c1 (#44cc11); shields.io's current SVGs use #dd4343, #ea7233 and #44bb00, so a reproduction that wants the captured look should write the hex values. The Hugging Face badge links to a dataset although its message says "Space", and the Code badge links back to the repository itself. The "Project-Page" pair is split across label and message ("Project" | "Page").

Other colors on the page come from images, not badges: the banner background #282828, die faces #f2f3f3 and #d1d1d1, and the pip #f1552c. The pipeline figure uses pastel panels and the comparison image uses red crosses and green ticks; neither was measured to a hex value.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| (image) | banner | name and short subtitle as one image |
| h1 | DICE-BENCH: Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues | full title; badge row and `---` follow |
| h3 | ✨ News (DICE-BENCH) | four dated bullets, newest first, then `---` |
| h2 | 📖 Overview | pipeline figure at 95%, a bold-led one-sentence definition, "Key points at a glance:", five bullets, a comparison-table image at 95%, `---` |
| h2 | 📂 Directory Layout | a two-column Path / Description table with four rows, `---` |
| h2 | 🛠️ Core Scripts | a three-column Script / Purpose / Key CLI flags table with three rows, one sentence on `uv`, `---` |
| h2 | 📁 Data Directory Explained | one sentence, an untagged tree, two bullets, one sentence, `---` |
| h2 | 🏃‍♂️ Quick Start | h3 "1. Environment (🛠 with **uv**)", h3 "2. Generate Synthetic Dialogues", h3 "3. Run vLLM Inference", each with `bash` blocks, `---` |
| h2 | 🔄 Experiment Steps | a three-item ordered list with bold step names, one sentence, `---` |
| h2 | 📜 Citation | a `bibtex` block, `---` |
| h2 | 🤝 Contact & Contributing | two sentences with a bold email and a link to the first author's site |

Absent from the source: author and affiliation lines, venue line in the header (the venue appears only in the News list), license section, acknowledgements, results table in Markdown (results are an image), demo GIF or video, table of contents, star chart.

Present but unusual: the News heading is an h3 placed before the first h2; the title appears twice, shortened in the banner and in full as a left-aligned h1 while the badges are centred; the comparison table is a 649×197 screenshot scaled up to 813px; three table cells glue a word to a bold word with no space (`a**small**`, `Generate**many**`, `Run**vLLM**`), which GitHub renders as "asmall", "Generatemany" and "RunvLLM"; the h1 is followed directly by a centred block, so the header mixes left and centre alignment.

## Components

**Banner paragraph.** `<p align="center"><img src="..." alt="..." style="width: 100%;"></p>`. GitHub keeps inline `width` styles on images, so `style="width: 100%;"` and `style="width: 95%;"` both work as sizes.

**Badge row.** `<p align="center">` with one `<a target="_blank"><img src="https://img.shields.io/badge/Label-Message-color"></a>` per line; messages #dd4343, #007ec6, #ea7233, #44bb00 on label #555555. The Hugging Face label carries the 🤗 emoji, URL-encoded as `%F0%9F%A4%97`.

**Section rules.** `---` after the badges and after every section through Citation, so each h2 sits between a 4px rule above and its own 1px rule below.

**Emoji headings.** Every h2 and the News h3 start with one emoji and a space: ✨, 📖, 📂, 🛠️, 📁, 🏃‍♂️, 🔄, 📜, 🤝. No emoji repeats.

**News list.** `* **MM/DD/YYYY** - text` bullets: bold US-style date, a spaced hyphen, a sentence with inline links and occasional bold, newest first. Four items from 05/16/2025 to 07/01/2025.

**Key-point bullets.** A bold-led definition sentence ("**DICE-BENCH** is a benchmark that ..."), a plain "Key points at a glance:" line, then five one-sentence `-` bullets with numbers (1,607 dialogues, 124 tools, about 64 percent exact match).

**Reference tables.** Pipe tables with long `| ------------ |` delimiters and no alignment colons, so GitHub centres the header cells and left-aligns the body. Paths and script names sit in inline code in the first column. The Directory Layout table has two columns (Path, Description); the Core Scripts table has three (Script, Purpose, Key CLI flags / variables), with variables as comma-separated inline code and output paths written "outputs to `outputs/...`".

**Annotated tree.** An untagged fenced block with a leading space on each line, box-drawing branches and right-hand `#` comments.

**Numbered Quick Start.** h3 headings numbered in the text ("### 1. Environment (🛠 with **uv**)") rather than an ordered list, each holding a one-line explanation and one or two `bash` blocks with trailing `#` comments, and an italic "*Fallback:*" note.

**Experiment steps.** An ordered list `1. **Prepare Data** - ...` with bold step names and a spaced hyphen, mirroring the News separator.

**Citation and contact.** A `bibtex` `@misc{...}` block with no lead sentence; contact is prose with the email in bold (`email **kyochul@snu.ac.kr**`, no explicit link in the source; GitHub autolinks it, so it renders as a bold mailto link) and a link to the first author's site.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| banner.png | PNG, charcoal background, illustrated die and white type | 1528×596 | `<img style="width: 100%;">` in `<p align="center">` | 856×334 | first element |
| pipeline.png | PNG, opaque white background, three-panel generation diagram | 6112×2742 | `<img style="width: 95%;">` in `<p align="center">` | 813×365 | first item in Overview |
| baseline_comparison.png | PNG, opaque white background, screenshot of the paper's comparison table | 649×197 | `<img style="width: 95%;">` in `<p align="center">` | 813×247 (scaled up about 1.25×) | end of Overview |

The pipeline figure has three titled stages (Tool Graph Construction, Scenario Configuration, Dialogue Generation) drawn as pastel rounded panels with small icons, code snippets and chat bubbles. The comparison image is a booktabs-style table with red ✗ and green ✓ marks and a bold "DICE-BENCH (ours)" last row. Both have opaque white backgrounds and no `<picture>` variant, so they appear as white boxes on GitHub's dark theme; the banner's charcoal background works on either. The README is designed for the light theme.

## Adapting to Other Content

- **A library.** Keep the 856px-wide dark banner with name and one-line description, drop the repeated h1 or shorten it to the name, keep the four-badge row (Docs, PyPI, License, Code), and make Directory Layout and Core Scripts tables the main reference.
- **A dataset.** Keep banner, h1 and badges with the Hugging Face badge first; put the annotated tree and the Directory Layout table directly after Overview, and state in a bold-led note which files are samples and where the full data lives.
- **A benchmark with scores.** Replace the 649×197 screenshot with a Markdown table (numeric columns right-aligned with `| ---: |`, best values bold) so it stays sharp at 813–856px.
- **A repo without a banner.** Centre the h1 with `<h1 align="center">` so it lines up with the badge row, and keep the News h3 as the first block after `---`.
- **A larger project.** Keep one emoji per h2, keep the `---` rules, and add a contents list after News once the page passes ten sections.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Size the banner `width: 100%` so it spans the 856px column | Leave a 1528px banner unsized and rely on clipping |
| Write news as `**MM/DD/YYYY** - sentence`, newest first | Mix date formats inside one list |
| Put paths and scripts in inline code in the first table column | Write file paths as plain text in tables |
| Use one distinct emoji per section heading | Put emoji on some headings and not others |
| Give each badge an `alt` and a message that matches its destination | Label a dataset link "Space" or leave `<img>` without `alt` |
| Keep a space before bold words in table cells | Write `a**small**`, which renders as "asmall" |
| Rebuild screenshot tables as Markdown or export them large | Upscale a 649px table screenshot to 813px |

## Agent Prompt Guide

1. "Start a README with `<p align="center"><img src="media/banner.png" alt="Name Banner" style="width: 100%;"></p>` (a 1528×596 dark banner, #282828 background, accent #f1552c), then `# Name: Full Paper Title` as a plain h1, then a `<p align="center">` row of four flat shields.io badges: arXiv-ID #dd4343, Project-Page #007ec6, 🤗 Hugging Face-Dataset #ea7233, Code-GitHub #44bb00, all on the default #555555 label, then `---`."
2. "After the header write `### ✨ News (Name)` with `* **MM/DD/YYYY** - sentence` bullets newest first, then `---`-fenced h2 sections with one emoji each: 📖 Overview (figure at `width: 95%`, bold-led definition, five key-point bullets), 📂 Directory Layout, 🛠️ Core Scripts, 📁 Data Directory Explained, 🏃‍♂️ Quick Start, 🔄 Experiment Steps, 📜 Citation, 🤝 Contact & Contributing."
3. "Write Directory Layout as a two-column Path | Description table and Core Scripts as a three-column Script | Purpose | Key CLI flags / variables table, with `| --- |` delimiters and no alignment colons, inline code for every path, script and variable, and a space before every bold word. Quick Start uses h3 headings '1. Environment', '2. ...', '3. ...' each with a `bash` block."

## Similar Pages

- **readme-jiwoogit-varbooth** also opens with a full-width title banner image and a centred four-badge row, but has no text h1, no emoji and no tables.
- **readme-deepseek-ai-deepseek-v3** shares the "large image header, centred badges, reference tables" pattern at a bigger scale, with numbered headings instead of emoji ones.
- **readme-eku127-satnav** documents its resources with two-column tables in the same spirit as Directory Layout, inside a text-built centred header.

## Quick Start

````markdown
<p align="center">
  <img src="media/banner.png" alt="Name Banner" style="width: 100%;">
</p>

# Name: Full Paper Title

<p align="center">
  <a href="http://arxiv.org/abs/XXXX.XXXXX" target="_blank"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-dd4343" alt="arXiv"></a>
  <a href="https://org.github.io/Name/" target="_blank"><img src="https://img.shields.io/badge/Project-Page-007ec6" alt="Project page"></a>
  <a href="https://huggingface.co/datasets/org/Name" target="_blank"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20-Dataset-ea7233" alt="Hugging Face dataset"></a>
  <a href="https://github.com/org/Name" target="_blank"><img src="https://img.shields.io/badge/Code-GitHub-44bb00" alt="Code"></a>
</p>

---

### ✨ News (Name)

* **MM/DD/YYYY** - Newest item with a [link](https://example.org/)!
* **MM/DD/YYYY** - Older item.

---

## 📖 Overview

<p align="center">
  <img src="media/pipeline.png" alt="Name Overview" style="width: 95%;">
</p>

**Name** is a benchmark that ...

Key points at a glance:

- Point with a number.
- Point with a number.

---

## 📂 Directory Layout

| Path | Description |
| ---- | ----------- |
| `src/` | Core package |
| `data/` | Sample data |

---

## 🛠️ Core Scripts

| Script | Purpose | Key CLI flags / variables |
| ------ | ------- | ------------------------- |
| `scripts/run.sh` | Generate a **small** dataset. | `VAR_A`, `VAR_B`, outputs to `outputs/run/` |

---

## 📁 Data Directory Explained

```
 data/
   ├── part_1.json          # full data (on Hugging Face)
   └── sample/
        └── part_1.json     # tiny subset
```

---

## 🏃‍♂️ Quick Start

### 1. Environment

```bash
uv init name
```

### 2. Generate Data

```bash
cd scripts
./run.sh
```

---

## 🔄 Experiment Steps

1. **Prepare Data** - ...
2. **Evaluate** - ...

---

## 📜 Citation

```bibtex
@misc{key,
  title={...},
}
```

---

## 🤝 Contact & Contributing

Questions? Open an issue or email **name@example.org**.
````

## Provenance

- Repo: https://github.com/snuhcc/DICE-Bench (`README.md`, branch `main`, last README commit d4fa0bd on 2025-07-01).
- Paper: "DICE-BENCH: Evaluating the Tool-Use Capabilities of Large Language Models in Multi-Round, Multi-Party Dialogues", ACL 2025, arXiv 2506.22853; first author Kyochul Jang. Project page https://snuhcc.github.io/DICE-Bench/.
- Selection: a full-width title banner and a tidy badge row lead into a dated news list, an overview figure and a comparison table, and the directory layout and core scripts are documented as clean two- and three-column tables, which is a model of reference structure.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, and the three PNGs fetched from the repo for pixel sizes and colors.
- Written 2026-10-28.
