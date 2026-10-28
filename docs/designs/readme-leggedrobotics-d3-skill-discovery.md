# D3 Skill Discovery — README Reference

> A field manual for a robot dog: a whiteboard diagram beside four lab photos, an emoji signpost row, and every heavy chapter folded away in drawers.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/leggedrobotics/d3-skill-discovery (last commit touching the file e8c1137, 2026-01-09; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). The figure size and its box colors come from `docs/overview_fig.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

This README is left-aligned where most paper repos are centred. A plain `#` title "D3: Divide, Discover, Deploy" with GitHub's grey rule and a `###` subtitle sit at the left edge; the only centred elements are the full-width method figure (a diagram of factorized skill discovery on the left and a 2×2 grid of ANYmal robot photos tagged z1 to z4 on the right, 856×304 rendered) and a row of five bold emoji links joined by " • ". There are no badges, no author list and no venue line in the header; the venue (CoRL 2025) first appears in bold in the Overview paragraph. The body is twelve `##` sections, every heading led by an emoji, separated by `---` rules, with a two-level emoji table of contents near the top. Long material (prerequisites, the whole Docker section, the directory tree, CLI arguments, sweeps, monitoring backends, tips, troubleshooting, third-party licenses) is folded into fifteen `<details>` blocks, so the tall capture shows a column of headings and summary triangles rather than walls of code.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈116): `# D3: Divide, Discover, Deploy`. GitHub h1, 2em (32px), weight 600, left-aligned, with the 1px grey rule under it across the 856px content width.
2. **Subtitle** (y≈182): `### Factorized Skill Learning with Symmetry and Style Priors`. GitHub h3, 1.25em (20px), weight 600, left-aligned, no rule. It appears in GitHub's outline menu as a heading.
3. **Method figure** (y≈216 to 520): `<p align="center"><img src="docs/overview_fig.png" width="100%" alt="Main figure of D3 paper"/></p>`. 2487×883 PNG on white, 856×304 at the 920px column; no link and no caption.
4. **Navigation row** (y≈548): `<p align="center">` with five `<a ...><strong>EMOJI Label</strong></a>` links separated by ` •` at line ends: 🌐 Project Page (external), 📖 Overview, 📦 Installation, 💻 Usage, 📝 Citation (in-page anchors such as `#-overview`, where the emoji drops out of the slug and leaves a leading hyphen). Body size, bold, GitHub link blue.
5. **Rule** (y≈586): `---`, GitHub's 4px grey `<hr>`. `## 📖 Overview` follows at y≈629, then the paragraph naming **CoRL 2025** and a `### ✨ Key Features` list, which run past the 900px fold.

## Badges

There are no shields.io badges, no logos and no image links in the header. The only button-like row is the navigation paragraph.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (link row) | 🌐 **Project Page** • 📖 **Overview** • 📦 **Installation** • 💻 **Usage** • 📝 **Citation** | GitHub link blue | bold links with emoji, joined by " • " | leggedrobotics.github.io/d3-skill-discovery/, `#-overview`, `#-installation`, `#-usage`, `#-citation` |

Colors visible on the page come from the method figure, not from badges. Pixel-sampled from `docs/overview_fig.png`: the state and skill boxes are keyed red fill #ffc6c6 (outline #ff8686), green fill #ccffaa (outline #7ac24a) and cyan fill #c6f4ff, on a white #ffffff ground with black #000000 serif math labels. The robot itself is red in the photos; the fourth photo tag (z4) is lavender. Both are photo colors and were not sampled to a single value.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 | D3: Divide, Discover, Deploy | title |
| h3 | Factorized Skill Learning with Symmetry and Style Priors | subtitle; figure, navigation row and `---` follow |
| h2 | 📖 Overview | one paragraph with **D3: Divide, Discover, Deploy** and **CoRL 2025** in bold; `### ✨ Key Features` with four bullets, each "emoji **Bold name**: description" |
| h2 | 📋 Table of Contents | a nested bullet list of anchor links, two levels, every entry led by its heading's emoji |
| h2 | 📦 Installation | `<details>` Prerequisites table; `### 1️⃣` to `### 4️⃣` keycap-numbered steps with `bash` blocks; a `<details>` "What does `install.sh` do?" with a ✅ list |
| h2 | 🐳 Docker Installation (Alternative) | the entire section inside one `<details>` ("Using Docker for Easy Setup"), with its own `###` headings, a table, a tip callout and `bash` blocks |
| h2 | 🏗️ Repository Structure | a `<details>` "Click to expand directory tree" around an untagged tree with `#` comments |
| h2 | 🌍 Environments | one sentence; `### 🔬 Unsupervised Skill Discovery (USD)` with a four-column table and a `<details>` FAQ; `### 🎮 Downstream Tasks` with a three-column table |
| h2 | 💻 Usage | five `###` subsections (training, high-level training, evaluation, interactive control, sweeps), each a sentence, a `bash` block and optional `<details>` or callout |
| h3 | 📈 Monitoring Training | placed after its own `---` rule; two `<details>` blocks (WandB, TensorBoard) |
| h2 | 🧠 Algorithm Details | `### 📚 Supported USD Algorithms` (table and two bold-led lists) and `### 🔀 Factorized USD` (a research-note callout and a `<details>` with `python` blocks) |
| h2 | 📊 Performance & Training Tips | two `<details>` blocks holding hardware and timing tables and tuning tips |
| h2 | 🐛 Troubleshooting | one `<details>` of **Problem** / **Solution** pairs separated by `---` |
| h2 | 📝 Citation | one sentence and a `bibtex` `@inproceedings` block |
| h2 | ⚖️ License | one sentence with **BSD-3-Clause License** in bold; a `<details>` third-party license table |

The source has 16 `---` lines: 14 between sections and two inside the Troubleshooting `<details>`.

Absent from the source: badges, author names and affiliations, a venue line in the header, news, results table, model zoo or checkpoint links, demo GIF or video, acknowledgements section.

Present but unusual: the subtitle is an `###` with no rule under it; "📈 Monitoring Training" is an `###` that sits after a `---` as if it were a section, while the table of contents lists it under Usage; the License sentence's link text is "LICENSE" but its target is `LICENCE`; every heading at every level starts with an emoji, including keycap digits for steps.

## Components

**Navigation row.** `<p align="center">` holding `<a href="..."><strong>🌐 Project Page</strong></a> •` per line. The bullet " • " is the separator; the first link leaves the repo and the rest jump to in-page anchors.

**Emoji headings.** Every `##` and `###` heading opens with one emoji (📖, 📦, 🐳, 🏗️, 🌍, 💻, 🧠, 📊, 🐛, 📝, ⚖️; ✨, 🔬, 🎮, 🎓, 🎨, 📈, 📚, 🔀). Ordered steps use keycap digits (`### 1️⃣ Install Isaac Lab`, `#### 1️⃣ Configure Sweep`).

**Table of contents.** `## 📋 Table of Contents` with `- [📖 Overview](#-overview)` items and two-space-indented children. Anchors keep GitHub's emoji-stripped slugs (`#-overview`, `#️-repository-structure`).

**Collapsible blocks.** Fifteen `<details>`, collapsed by default. The summary is usually `<summary><b>EMOJI Title</b></summary>` followed by a blank line, `<br>` and a blank line, so the opened content starts one line lower. Some summaries are plain text ("Click to expand directory tree") or contain a linked inline-code filename.

**Requirement tables.** Two columns with `|------------|-----------------|` delimiters and no alignment colons; the left column is bold (`| **Python** | 3.10+ |`).

**Task tables.** Four columns (Environment, Description, Task ID, Config File) with the first cell bold and emoji-led (`**🦿 Low-Level USD**`), the task ID in inline code and the config file as an inline-code link.

**Callouts.** Blockquotes with a bold emoji lead: `> **💡 Tip**: ...`, `> **⚠️ Important**: ...`, `> **🔬 Research Note**: ...`. Six in all. GitHub renders them with a grey left bar and grey text; they are not GitHub's `[!TIP]` alert syntax.

**Code blocks.** `bash` for commands, with `\` line continuations and one flag per line; `python` for the algorithm template and configs; `yaml` for sweep files; the directory tree in an untagged fence.

**Troubleshooting pairs.** A `**Problem**:` line with the error message in inline code, then a `**Solution**:` line with a `bash` block or bullets, each pair separated by `---` inside the `<details>`.

**Citation and license.** "If you use this code in your research, please cite our paper:" then `@inproceedings{cathomen2025d3, ...}`; license is one bold-named sentence plus a collapsed three-column third-party table.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| docs/overview_fig.png | PNG, RGB, white background | 2487×883 | `<img src="docs/overview_fig.png" width="100%" alt="Main figure of D3 paper"/>` in `<p align="center">` | 856×304 | header, between the subtitle and the navigation row; no caption |

The figure joins a schematic and photos in one strip. On the left, colored pairs of state and skill boxes (s1/z1 red, s2/z2 green, sN/zN cyan) feed a "Skill Discovery Rewards" box holding METRA and DIAYN clouds and matching r1, r2, rN boxes, which feed an "On-Policy RL Training with Symmetry" box; a small render of the robot and an r_style box close the loop with serif math labels. On the right, four photos of the red ANYmal robot each carry a tag z1 to z4 in the same box style, with white arrows marking the motion. It is the only image in the README; there is no `<picture>` pair, GIF or video, and the figure's white background makes it a light-theme image.

## Adapting to Other Content

- **A library.** Keep the left-aligned `#` name and `###` one-line description, replace the method figure with a short code example, keep the bold emoji navigation row (Docs, Installation, Usage, Citation) and the `<details>` prerequisites table.
- **A dataset.** Keep the header and replace Environments with a Dataset section using the same task-table shape (Split, Description, Size, Download link).
- **A benchmark with scores.** Add a "📊 Results" section after Environments with numeric columns right-aligned (`| ---: |`) and the best value in bold, outside any `<details>` so it is visible; D3 has no such table, so this is an extension.
- **A repo without a figure.** Let the navigation row follow the subtitle directly, then the `---` rule.
- **A quieter version.** Drop emoji from `###` headings and keep them only on `##` headings and the navigation row; the folding pattern carries the page on its own.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Fold optional or alternative paths (Docker, sweeps, troubleshooting) into `<details>` with a bold summary | Fold the main install steps or the first training command |
| Keep the figure at `width="100%"` directly under the subtitle | Put a separate badge row between the title and the figure |
| Use one emoji per heading and keep the same emoji in the TOC and navigation row | Add a second emoji or decorative emoji inside body sentences |
| Write step headings with keycap digits in order (1️⃣ to 4️⃣) | Mix keycap and plain numbers in one sequence |
| Lead each callout with a bold emoji label (💡 Tip, ⚠️ Important) | Use callouts for content that belongs in the main text |
| Check that link text matches its target file | Label a link "LICENSE" when it points to `LICENCE` |

## Agent Prompt Guide

1. "Write a left-aligned GitHub README header: `# Name: Expanded Name`, then `### One-line paper subtitle`, then a centred `width="100%"` method figure on white, then a centred row of five bold emoji links separated by ' • ' (🌐 Project Page, 📖 Overview, 📦 Installation, 💻 Usage, 📝 Citation) pointing to the project page and in-page anchors, then `---`. No badges and no author block; name the venue in bold in the first paragraph of `## 📖 Overview`."
2. "Write twelve `##` sections, each heading led by one emoji and each separated by `---`: 📖 Overview (with `### ✨ Key Features`), 📋 Table of Contents (nested anchor list), 📦 Installation (`### 1️⃣` to `### 4️⃣` steps with `bash` blocks), 🐳 Docker Installation (Alternative), 🏗️ Repository Structure, 🌍 Environments, 💻 Usage, 🧠 Algorithm Details, 📊 Performance & Training Tips, 🐛 Troubleshooting, 📝 Citation, ⚖️ License."
3. "Put prerequisites, the whole Docker section, the directory tree, CLI argument tables, troubleshooting and third-party licenses inside `<details><summary><b>EMOJI Title</b></summary>` blocks with `<br>` after the summary. Write tips as `> **💡 Tip**: ...` blockquotes and tables with a bold first column."

## Similar Pages

- **readme-snuhcc-dice-bench**: also uses emoji in headings and a left `#` title, but carries a badge row that D3 leaves out.
- **readme-chuan-10-agile**: the same `#` name plus `###` subtitle pair, centred inside a `<div>` and followed by `for-the-badge` badges; D3 keeps the pair left-aligned with no badges.
- **readme-seohongpark-ogbench**: another RL repo that uses `<details>`, with a centred logo and badge header in contrast to D3's figure-first header.

## Quick Start

````markdown
# Name: Expanded Name
### One-Line Paper Subtitle

<p align="center">
  <img src="docs/overview_fig.png" width="100%" alt="Main figure"/>
</p>

<p align="center">
  <a href="https://example.github.io/project/"><strong>🌐 Project Page</strong></a> •
  <a href="#-overview"><strong>📖 Overview</strong></a> •
  <a href="#-installation"><strong>📦 Installation</strong></a> •
  <a href="#-usage"><strong>💻 Usage</strong></a> •
  <a href="#-citation"><strong>📝 Citation</strong></a>
</p>

---

## 📖 Overview

This repository contains the official implementation of **Name**, presented at **Venue Year**. One sentence on what it does.

### ✨ Key Features

- 🔀 **Feature**: description

---

## 📋 Table of Contents

- [📖 Overview](#-overview)
- [📦 Installation](#-installation)
- [💻 Usage](#-usage)
  - [🎓 Training](#-training)
- [📝 Citation](#-citation)

---

## 📦 Installation

<details>
<summary><b>📋 Prerequisites</b></summary>

<br>

| Requirement | Version/Details |
|------------|-----------------|
| **Python** | 3.10+ |

</details>

### 1️⃣ First Step

```bash
command one
```

### 2️⃣ Second Step

```bash
command two
```

---

## 💻 Usage

### 🎓 Training

```bash
python scripts/train.py \
  --task Task-ID \
  --headless
```

> **💡 Tip**: one practical tip.

---

## 🐛 Troubleshooting

<details>
<summary><b>Common Issues and Solutions</b></summary>

<br>

**Problem**: `error message`

**Solution**: what to do.

</details>

---

## 📝 Citation

If you use this code in your research, please cite our paper:

```bibtex
@inproceedings{key2025,
  title     = {...},
  year      = {2025},
}
```

---

## ⚖️ License

This project is licensed under the **License Name**. See [LICENSE](LICENSE) for details.
````

## Provenance

- Repo: https://github.com/leggedrobotics/d3-skill-discovery (`README.md`, branch `main`, last README commit e8c1137 on 2026-01-09).
- Paper: "Divide, Discover, Deploy: Factorized Skill Learning with Symmetry and Style Priors", CoRL 2025; first author Rafael Cathomen. Project page https://leggedrobotics.github.io/d3-skill-discovery/.
- Selection: a distinct left-aligned style that combines a method diagram with robot photos and an icon-led table of contents, and puts prerequisites, Docker setup and the directory tree in collapsible blocks so the page stays scannable, though the emoji are heavy.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28, including the generated heading anchors), 1440×900 and 2700px captures at a 920px README column, and `docs/overview_fig.png` fetched from the repo for its size and box colors.
- Written 2026-10-28.
