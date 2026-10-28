# OGBench — README Reference

> A benchmark's shop window: a two-weight wordmark, four pale-grey tags with periwinkle tips, then a contact sheet of every arena it ships.

**Theme:** both

Read from `README.md` on the default branch `master` of github.com/seohongpark/ogbench (last commit touching the file a977253, 2026-10-07; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a first-screen capture and a 2700px tall capture of the light theme with the README column 920px wide (856px content width), the shields.io SVGs for the four badge URLs, and `assets/ogbench.svg` and `assets/env_teaser.png` fetched from the repo. The capture files are saved at 1200×750, a 0.833 scale of the 1440×900 window; every y value below is converted back to the 1440×900 frame. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; the README overrides them only through the `<summary>` heading trick described in Header Block.

## Overview

The top of the page is a centred logo-and-thumbnail block that reads like a product landing card. A 300px SVG wordmark ("OG" in bold periwinkle #598be7, "Bench" in a light black weight) sits above the full paper title set as an `<h1>` with no grey rule under it, followed by one row of four `for-the-badge` shields that all share a pale #f0f0f0 label and a #598be7 message. Under the badges a borderless 3×9 grid of environment thumbnails, each column labelled in monospace (maze, antmaze, humanoidmaze, antsoccer, visual-maze, cube, scene, puzzle, powderworld), fills the content width, and two large blue links, "Paper" and "Project page", close the block at h2 size. The body then switches to plain GitHub prose but uses `#` (h1, ruled) for every top-level section and `###` (h3) for subsections, skipping h2 entirely. Overview carries a bold-led feature list; Quick Start opens with a one-line `pip install ogbench`; long annotated `python` examples follow, each preceded by a red GitHub Caution callout at the exact point where users would reach for `gymnasium.make`. There is no news list, no results table and no teaser video.

## Header Block

Everything down to the "Paper / Project page" links is wrapped in one `<div align="center">`. Rendered positions are y values in the 1440×900 frame (the README box starts at y≈25 with its "README.md" file bar).

1. **Logo** (y≈94–156): `<img src="assets/ogbench.svg" width="300px"/>`. The SVG viewBox is 267.48×52.85, so it renders 300×59. Its stylesheet fills "OG" with `.cls-1 { fill: #598be7; }` and "Bench" with `.cls-2 { fill: black; }`, and switches `.cls-2` to white inside `@media (prefers-color-scheme: dark)`. GitHub wraps it in a link to the SVG file.
2. **Title** (y≈204): `<div id="user-content-toc"><ul align="center" type="none"><summary><h1>OGBench: Benchmarking Offline Goal-Conditioned RL</h1></summary></ul></div>`. Putting the heading inside `<summary>` makes GitHub's CSS apply `summary h1 { display: inline-block; border-bottom: 0; padding-bottom: 0 }`, so the 2em (32px) weight-600 title is centred with no rule under it. It still appears in GitHub's outline menu.
3. **Badge row** (y≈255–283): four `<a><img src="https://img.shields.io/..."/></a>` lines joined by ` &emsp;` (an em space), so the gaps are about 16px. Each badge is 28px tall; the four SVGs are 144.5, 118.5, 156.5 and 124.5px wide and the row spans about 617px. Details in Badges.
4. **Environment teaser** (y≈304–606): `![image](assets/env_teaser.png)`, plain Markdown with no width. The PNG is 5336×1881 with an opaque white background, so GitHub's `max-width: 100%` renders it 856×302. It is the only image in the first screen.
5. **Link heading** (y≈670): `<div id="toc"><ul align="center" type="none"><summary><h2><a href="https://arxiv.org/abs/2410.20092">Paper</a> &emsp; <a href="https://seohong.me/projects/ogbench/">Project page</a></h2></summary></ul></div>`. The same trick gives two 1.5em (24px) blue links with no rule. `id="toc"` is reused from the title block (GitHub prefixes both to `user-content-toc`).
6. **Close**: `</div>`, then the first ruled `# Overview` at y≈745, so the first screen ends on the opening paragraph.

There is no author line, affiliation line, venue line or caption anywhere in the header; the venue (ICLR 2025) appears only in the BibTeX `booktitle`.

## Badges

All four use `style=for-the-badge` and `labelColor=F0F0F0`, so every badge has a square-cornered 28px body, uppercase spaced Verdana-style text, a pale grey label with #333333 label text and a #598be7 message with white (#ffffff) text, as the returned SVGs show (`fill="#f0f0f0"`, `fill="#333"`, `fill="#598be7"`, `fill="#fff"`). Only the first carries a logo.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| PYTHON (python logo in #598be7) | 3.8+ | #598be7 (label #f0f0f0, label text #333333) | for-the-badge | python.org |
| PYPI | V1.2.2 (dynamic `pypi/v/ogbench`) | #598be7 (label #f0f0f0) | for-the-badge | pypi.org/project/ogbench/ |
| CODE STYLE | RUFF | #598be7 (label #f0f0f0) | for-the-badge | docs.astral.sh/ruff/ |
| LICENSE | MIT | #598be7 (label #f0f0f0) | for-the-badge | the repo's LICENSE file |
| (link heading) | Paper &emsp; Project page | GitHub link blue | `<h2>` links, not bold-separated | arxiv.org/abs/2410.20092, seohong.me/projects/ogbench/ |

The badge row is about the package, not the paper: version, Python floor, code style and license, in one color. The paper and project-page links are deliberately pulled out of the badge family into a large heading-size line below the teaser. The source URL for the third badge contains a literal space (`Code style-ruff`); GitHub's camo proxy encodes it and the badge renders.

Other colors visible on the page are GitHub's own alert colors, not chosen by the author: the Caution callout's left bar #cf222e with title #d1242f, and the Note callout's bar and title #0969da. The section rule under each `#` heading and the `---`-style rules come from GitHub (#d1d9e0).

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred, in `<summary>`, no rule) | OGBench: Benchmarking Offline Goal-Conditioned RL | title; badges and teaser follow |
| h2 (centred, in `<summary>`, no rule) | Paper &emsp; Project page | two links; closes the header |
| h1 | Overview | a three-line paragraph linking the project page |
| h3 | Features | eight bullets, most opening with a bold count or property (**8 types**, **85 datasets**, **410 tasks**), the first with three nested bold category bullets |
| h1 | Quick Start | holds four h3 subsections |
| h3 | Installation | one-line `shell` block `pip install ogbench`, dependency sentence, two anchor links to the next subsections |
| h3 | Usage for offline goal-conditioned RL | Caution callout, then a 40-line commented `python` example |
| h3 | Usage for standard (non-goal-conditioned) offline RL | a `<details>` table of default tasks, Caution callout, a long Note callout with a bullet list, a `python` example |
| h3 | Dataset APIs | two `python` blocks, one with an ASCII layout of dataset arrays in comments |
| h1 | Reference Implementations | intro paragraph with **standalone** in bold |
| h3 | Installation / Running the reference implementations / Tips for hyperparameters and flags | `shell` blocks, a bullet list of six agent files in inline code, a Note callout with a nested `shell` block, nine tip bullets |
| h1 | Reproducing Datasets | h3 Installation, Reproducing datasets, Reproducing expert policies with `shell` blocks |
| h1 | Additional Features | bullets, including eleven raw dataset URLs |
| h1 | Caveats | one long bullet on a version change |
| h1 | Acknowledgments | a bullet list of linked repos and one thanks line |
| h1 | Citation | a `bibtex` block |

Absent from the source: author and affiliation lines, venue line, news or changelog, results or leaderboard table, teaser video or GIF, model zoo table, table of contents, license section (the license is only a badge), contact section, emoji anywhere.

Present but unusual: both header headings sit inside `<summary>` within `<ul type="none">`, a known trick to centre a heading without its rule; the body never uses `##`, so every top-level section is an h1 with a rule and subsections jump straight to h3; the same Caution callout is repeated verbatim before both usage examples; the paper and project links are heading-size text, not badges; the PyPI badge is dynamic and showed V1.2.2 at capture, so its message changes with releases.

## Components

**Wordmark.** One SVG with two classes: a brand fill (#598be7) for the short prefix and a neutral fill that flips from black to white under `prefers-color-scheme: dark`, placed at `width="300px"`.

**Uniform badge row.** Four `for-the-badge` shields with identical `labelColor=F0F0F0` and message color #598be7, written one per source line and separated by ` &emsp;`. The wordmark's blue and the message blue are the same hex, which ties the logo to the row.

**Heading-size link line.** Two `<a>` inside an `<h2>` separated by `&emsp;`, under the teaser, standing in for paper and project-page badges.

**Bold-led feature list.** Six of the eight bullets start with a bold count or adjective (**8 types**, **85 datasets**, **410 tasks**, **pixel-based**, **Clean, well-tuned reference implementations**, **Fully reproducible**) and end in one plain clause; the last two (`pip`-installable APIs, no major dependencies) are plain, and the first nests three bold category bullets.

**One-line install.** `pip install ogbench` alone in a `shell` block, followed by a sentence naming exactly three dependencies in inline code.

**Placed callouts.** GitHub alert syntax `> [!CAUTION]` (red) placed directly above the code it warns about, and `> [!NOTE]` (blue) for longer explanations, one of which contains a nested `shell` block. The Caution body is two lines: a bold **not** and the right function in inline code.

**Annotated code.** `python` blocks with one comment per step, trailing inline comments aligned in a column, and a comment-drawn ASCII diagram of array layouts with `|<- traj 1 ->|` markers.

**Collapsible table.** `<details><summary><b>Click to see the list of default tasks</b></summary>` wrapping a two-column table with `:---:` on both columns, so every cell is centred; cells are inline code.

**Citation.** A bare `# Citation` heading and an `@inproceedings{ogbench_park2025, ...}` block with no lead sentence.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| ogbench.svg | SVG wordmark, transparent, dark-mode aware | viewBox 267.48×52.85 | `<img ... width="300px"/>` in `<div align="center">` | 300×59 | first element |
| env_teaser.png | PNG grid of 27 renders in 3 rows × 9 columns, monospace labels under the last row, opaque white | 5336×1881 | `![image](assets/env_teaser.png)`, no width | 856×302 | between badge row and link heading; no caption |

The thumbnails are dark navy and checkerboard scenes from MuJoCo (mazes, ant, humanoid, robot arms) with one pixel-art Powderworld column, so the grid reads as a contact sheet of environments rather than a method figure. There is no other image in the README; videos are linked to the project page in the Features list. The wordmark is the only asset that adapts to dark mode; the teaser stays a white panel there, which is still legible.

## Adapting to Other Content

- **A library.** Keep the wordmark at 300px and the four package badges in one color; replace the environment grid with a single-row screenshot or drop it, and keep the `# Overview` plus bold-led feature list.
- **A dataset.** Use the labelled thumbnail grid as the teaser at full width (856px) with one label per column, and put a `<details>` table of splits under Quick Start.
- **A benchmark with scores.** Add a `# Results` h1 after Quick Start with numeric columns right-aligned (`| ---: |`); OGBench links its benchmark table's commands but shows no scores, so this is an extension.
- **A repo without a logo.** Keep the `<summary>` title trick so the h1 has no rule, and let the badge row sit directly under it.
- **Paper links.** Keep them as the heading-size `Paper &emsp; Project page` line rather than adding them to the badge row, so the badge family stays one color.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Give every badge the same `labelColor=F0F0F0` and message #598be7 | Mix flat and `for-the-badge` styles or brand colors in one row |
| Match the wordmark's brand fill to the badge message color | Pick a logo color unrelated to the badges |
| Put a Caution callout right above the code it guards | Collect warnings in a separate FAQ far from the example |
| Lead each feature bullet with a bold count | Write feature bullets as full paragraphs |
| Keep install to one `pip` line with named dependencies | Open with a long environment matrix |
| Collapse lookup tables in `<details>` | Show reference tables inline before the example |
| Make the wordmark's text fill switch under `prefers-color-scheme: dark` | Ship a black-text logo on a transparent background with no dark variant |

## Agent Prompt Guide

1. "Write a centred README header inside `<div align="center">`: an SVG wordmark at `width="300px"` with the prefix in #598be7 and the rest in black that turns white under `prefers-color-scheme: dark`; the full paper title as `<h1>` inside `<ul align="center" type="none"><summary>` so it has no rule; one row of four `for-the-badge` shields (Python 3.8+, PyPI version, Code style ruff, License MIT) all with `labelColor=F0F0F0` and color 598BE7, separated by ` &emsp;`; a full-width grid image of environments with monospace labels; then `<h2>` links Paper &emsp; Project page in the same `<summary>` wrapper."
2. "Use `#` for top-level sections in this order: Overview, Quick Start, Reference Implementations, Reproducing Datasets, Additional Features, Caveats, Acknowledgments, Citation; use `###` for subsections. Under Overview add `### Features` with bullets that each start with a bold count."
3. "In Quick Start, put `pip install ogbench` alone in a `shell` block, then before each `python` example insert `> [!CAUTION]` with a two-line warning naming the wrong call in bold and the right call in inline code. Put lookup tables in `<details><summary><b>Click to see ...</b></summary>` with centred `:---:` columns."

## Similar Pages

- readme-mdyao-photoagent: also opens with a small centred logo over the title and a `for-the-badge` row, but varies the message color per destination (blue, red, yellow, green) where OGBench keeps one color.
- readme-damon-demon-spanuq: also leads with package-style badges and a feature list, but uses 20px flat badges and a results table instead of an image grid.
- readme-eku127-satnav: a centred academic header with authors and a caption; OGBench drops authors and lets the thumbnail grid do the summary.

## Quick Start

````markdown
<div align="center">
<img src="assets/logo.svg" width="300px"/>

<div id="user-content-toc">
  <ul align="center" type="none">
    <summary>
      <h1>Name: Full Paper Title</h1>
    </summary>
  </ul>
</div>

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-598BE7?style=for-the-badge&logo=python&logoColor=598BE7&labelColor=F0F0F0"/></a> &emsp;
<a href="https://pypi.org/project/name/"><img src="https://img.shields.io/pypi/v/name?style=for-the-badge&labelColor=F0F0F0&color=598BE7"/></a> &emsp;
<a href="https://docs.astral.sh/ruff/"><img src="https://img.shields.io/badge/Code%20style-ruff-598BE7?style=for-the-badge&labelColor=F0F0F0"/></a> &emsp;
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-598BE7?style=for-the-badge&labelColor=F0F0F0"/></a>

![image](assets/env_grid.png)

<div id="toc">
  <ul align="center" type="none">
    <summary>
      <h2><a href="https://arxiv.org/abs/XXXX.XXXXX">Paper</a> &emsp; <a href="https://example.org/project/">Project page</a></h2>
    </summary>
  </ul>
</div>

</div>

# Overview

One-paragraph description with a link to the [project page](https://example.org/project/).

### Features

- **N types** of environments:
  - **Group**: A, B and C.
- **N datasets** covering ...
- `pip`-installable, easy-to-use APIs.

# Quick Start

### Installation

```shell
pip install name
```

### Usage

> [!CAUTION]
> Do **not** use `wrong.call` to create an environment. Use `name.right_call` instead.

```python
import name
# Step comment.
```

<details>
<summary><b>Click to see the list of defaults</b></summary>

| Item | Default |
|:---:|:---:|
| `a-*` | `task1` |

</details>

# Reference Implementations

# Caveats

# Acknowledgments

# Citation

```bibtex
@inproceedings{key,
  title={...},
}
```
````

## Provenance

- Repo: https://github.com/seohongpark/ogbench (`README.md`, branch `master`, last README commit a977253 on 2026-10-07).
- Paper: "OGBench: Benchmarking Offline Goal-Conditioned RL", ICLR 2025 (arXiv 2410.20092); first author Seohong Park. Project page https://seohong.me/projects/ogbench/.
- Selection: a two-weight wordmark, uniform flat-colored badges and a labelled thumbnail grid of every environment carry the summary, followed by a crisp feature list, a one-line pip install and a Caution callout placed where users go wrong. The badges are `for-the-badge`, not shields.io's `flat` style; "flat" in the selection note describes their single solid color.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), first-screen and 2700px captures at a 920px README column, shields.io SVGs for all four badge URLs, `assets/ogbench.svg` and `assets/env_teaser.png` fetched from the repo for colors and pixel sizes, github-markdown-css 5.8.1 for the `summary h1` and alert rules.
- Written 2026-10-28.
