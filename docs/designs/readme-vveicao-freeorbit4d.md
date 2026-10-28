# FreeOrbit4D — README Reference

> A screening-room program: a glowing orbit emblem, a blue linked title, two chunky tags, then bordered grids where every input clip plays beside its re-shot result.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/VVeiCao/FreeOrbit4D (last commit touching the file 700ead9, 2026-08-12; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the badge URLs; image and GIF sizes and frame counts come from `assets/title.png`, `assets/demo/camel_input.gif`, `camel_inter.png`, `bear_traj1.gif`, `assets/viser.png` and `assets/mask.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The first screen is a centred stack that hands over to a results grid quickly. A small logo image (the word "FreeOrbit4D" in glossy italic letters on a dark blue globe with an orbit ring) sits on top, then the full paper title as a centred blue link at h3 size, a centred h4 venue line, two `for-the-badge` badges, a centred author line with superscript affiliation numbers, an affiliation line and a bold TL;DR in h4. Under the TL;DR a bordered HTML table with three columns (Input Video, Interactive 4D, Output Video) starts at y≈543, so the fold cuts through its first row of animated GIFs. A second, narrower table shows one input against two camera trajectories, and a one-line link to the project page ends the showcase. Only after that do the ordinary `##` sections begin: 🔥 News, Installation, Quick Start, Custom Camera Trajectories, Run on Your Own Video, Citation and Acknowledgements.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Logo** (y≈96 to 211): `<p align="center"><img src="assets/title.png" width="200"></p>`. The source is 752×431, so `width="200"` renders it at 200×115, centred.
2. **Title** (y≈253 and 278): `### <p align="center">[FreeOrbit4D: Training-free Arbitrary Camera Redirection ... 4D Reconstruction](https://arxiv.org/abs/2601.18993)</p>`. GitHub renders an h3 containing a centred paragraph with one link, so the title is 1.25em (20px), weight 600, in GitHub link blue, wrapped onto two centred lines, with no rule. The whole title links to the arXiv abstract.
3. **Venue** (y≈323): `<h4 align="center">SIGGRAPH Conference Papers '26</h4>`. GitHub h4, 1em (16px), weight 600, no rule.
4. **Badge row** (y≈348 to 376): `<p align="center">` with two `<a><img src="https://img.shields.io/badge/...svg?style=for-the-badge"></a>` lines, Project Page and arXiv. Each badge is 28px tall; the row is about 305px wide (136 + 165 px plus a gap). Details in Badges.
5. **Authors** (y≈411): `<p align="center">` with eight `<a href="...">Name</a><sup>n</sup>,` entries, one per source line. All eight names are regular-weight links; marks run from `<sup>1</sup>` to `<sup>3,4</sup>`. No equal-contribution mark.
6. **Affiliations** (y≈451): `<p align="center"><sup>1</sup>University of Illinois Urbana-Champaign, <sup>2</sup>University of Pennsylvania, <sup>3</sup>Eyeline Labs, <sup>4</sup>Netflix</p>`. Comma-separated, plain text.
7. **TL;DR** (y≈497 and 518): `<h4 align="center"><b>TL;DR: FreeOrbit4D is an effective training-free method for large-angle camera redirection via geometry-complete 4D proxy.</b></h4>`. A one-sentence summary set as a bold h4, two centred lines.
8. **Showcase table** (from y≈543, crossing the fold): `<div align="center"><table>` with a header row of three bold labels (the middle one adds `<br><sub>(click to explore)</sub>`) and three rows of `<img ... width="280">`. See Components and Imagery.

## Badges

Both use `https://img.shields.io/badge/<label>-<message>-<color>.svg?style=for-the-badge`. In that style shields.io draws square-cornered 28px badges, uppercases both parts, sets the label in regular and the message in bold Verdana with wide letter spacing, and puts the label on #555555 with white (#ffffff) text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| PROJECT | PAGE | `green`, served as #67ac09 (label #555555) | for-the-badge | freeorbit4d.vision.ischool.illinois.edu/ |
| ARXIV | 2601.18993 | #b31b1b (label #555555) | for-the-badge | arxiv.org/abs/2601.18993 |
| (title link) | full paper title | #0969da (GitHub link blue) | h3 text link | arxiv.org/abs/2601.18993 |

The badges have no `alt` attribute. The Project Page badge uses the named color `green`, which the SVG that shields.io returns fills with #67ac09; the arXiv badge gives its red as hex. The title link and the arXiv badge point to the same URL.

Other colors on the page: author names and body links are GitHub link blue #0969da; table borders are GitHub's grey #d1d9e0 with alternate rows on its light stripe #f6f8fa. The logo is a dark navy globe with a white-and-blue glossy wordmark, and the Interactive 4D thumbnails draw the camera path as a rainbow gradient; neither was sampled to a single value.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h3 (centred, linked) | FreeOrbit4D: Training-free Arbitrary Camera Redirection for Monocular Videos via Foreground-Complete 4D Reconstruction | title; the logo precedes it |
| h4 (centred) | SIGGRAPH Conference Papers '26 | venue; badges, authors and affiliations follow without a heading |
| h4 (centred, bold) | TL;DR: FreeOrbit4D is an effective training-free method ... | summary; the three-column showcase table follows |
| h3 | Multiple Trajectories from a Single Input | a second three-column table (input, two trajectories) and a project-page link line |
| h2 | 🔥 News | two bullets with bold full dates and an emoji inside each item |
| h2 | Installation | one paragraph with bold version pins, h3 Setup with a commented `bash` block |
| h2 | Quick Start | two `bash` blocks with output paths in inline code and a docs link |
| h2 | Custom Camera Trajectories | one `bash` block, a centred 760px screenshot of the trajectory editor, a three-step numbered list, a second `bash` block |
| h2 | Run on Your Own Video | one paragraph with a bold constraint, h3 Step 1 — Annotate the foreground (a `bash` block and a 600px screenshot of the mask UI), h3 Step 2 — Run the pipeline |
| h2 | Citation | a `bibtex` block with no lead sentence |
| h2 | Acknowledgements | one paragraph of linked project names |

Absent from the source: an h1 or h2 title (the page has no h1 at all), license section, table of contents, model zoo table, results table with numbers, dataset section, `<details>` blocks, `<picture>` dark variants.

Present but unusual: the title is a Markdown link inside an HTML `<p>` inside an h3, which makes it blue and gives it no rule; the venue and TL;DR are h4 headings; the results showcase comes before any `##` section, so the first ruled heading is "🔥 News"; the project-page badge and the "project page" text link under the second table go to different hosts (freeorbit4d.vision.ischool.illinois.edu and cvmlgroup.web.illinois.edu/freeorbit4d); the `bibtex` entry is missing the comma after the `title` field, so it will not parse as written; the README has no license section or badge.

## Components

**Centred HTML header.** Logo, badges, authors and affiliations are separate `<p align="center">` blocks; venue and TL;DR are `<h4 align="center">`. No `<br>` padding; spacing comes from paragraph and heading margins.

**for-the-badge pair.** Two `<a href="..."><img src="https://img.shields.io/badge/Label-Message-COLOR.svg?style=for-the-badge"></a>` lines; label grey #555555, messages #67ac09 and #b31b1b.

**Author line with superscripts.** `<a href="...">Name</a><sup>1</sup>,` per source line; GitHub renders the marks as small raised numbers in body color immediately after the blue names.

**Showcase table.** `<div align="center"><table>` then `<tr>` rows of `<td align="center">`. Row 1 holds bold column labels (`<b>Input Video</b>`, `<b>Interactive 4D</b><br><sub>(click to explore)</sub>`, `<b>Output Video</b>`). Each later row holds one example: input GIF, a PNG thumbnail wrapped in `<a>` to a hosted viser 4D viewer, and output GIF, all `width="280"`. GitHub draws 1px #d1d9e0 cell borders and stripes even rows with #f6f8fa, so each example sits in a framed cell. Because three 280px images plus cell padding exceed the 856px column, the table fills the full width and the images shrink to about 257px.

**Comparison table.** Same structure under `### Multiple Trajectories from a Single Input`: header labels Input Video, Trajectory #1, Trajectory #2, three example rows (bear, duck, hike), all GIFs at `width="240"`. This table is narrower than the column (about 800px) and centred by the wrapping `<div>`, so its images render at their full 240px.

**News list.** `- **May 10, 2026**: 🤗 We release the code of FreeOrbit4D!`: full date in bold with the colon outside the bold, an emoji at the start of the sentence, an exclamation mark at the end. Two items, newest first; the list starts directly under the heading with no blank line.

**Code blocks.** All `bash`, with `#` comment lines grouping clone, environment and checkpoint steps in Setup, and a trailing comment listing other demos on the Quick Start command. Output paths follow in inline code (`outputs/rendering/{scene_name}/...`).

**Screenshot plus steps.** In Custom Camera Trajectories, a centred `<img src="assets/viser.png" width="760">` is followed by a three-item numbered list of UI actions with button names in inline code (`Generate Trajectory`, `Save`).

**Citation.** A bare `bibtex` block, `@inproceedings{cao2026freeorbit4d, ...}` with `=` aligned at column 16, braces protecting `{FreeOrbit4D}`, `{4D}`, `{SIGGRAPH}` and `{ACM}`, and a `pages` field.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| title.png | PNG logo, wordmark on a dark globe, transparent surround | 752×431 | `<img src="assets/title.png" width="200">` in `<p align="center">` | 200×115 | top of the README |
| camel_input.gif and the other showcase GIFs | animated GIF, 30 frames | 320×185 (camel_input) | `<img ... width="280">` in `<td align="center">` | about 257×149 (shrunk by the table) | showcase table, columns 1 and 3 |
| camel_inter.png and the other viewer thumbnails | PNG render of the 4D point cloud with a rainbow camera path on white | 1850×1158 | `<a href="viser viewer"><img ... width="280"></a>` | about 257×161 | showcase table, column 2 |
| bear_traj1.gif and the other trajectory GIFs | animated GIF, 30 frames | 240×138 (bear_traj1) | `<img ... width="240">` | 240×138 | comparison table, all columns |
| viser.png | PNG screenshot of the trajectory editor | 3042×1678 | `<img src="assets/viser.png" width="760">` in `<p align="center">` | 760×419 | Custom Camera Trajectories |
| mask.png | PNG screenshot of the Gradio mask UI | 1928×1478 | `<img src="assets/mask.png" width="600" alt="...">` in `<p align="center">` | 600×460 | Run on Your Own Video, Step 1 |

The showcase is built from fifteen GIFs (six in the first table, nine in the second) and three linked PNGs arranged in two tables, so the results play inline without any embedded video. Only `mask.png` has `alt` text. Images have light or photographic backgrounds and no `<picture>` dark variants; the logo's dark globe is the only dark block on the page.

## Adapting to Other Content

- **A video method without an interactive viewer.** Keep the two-table pattern: a full-width table of Input / Ours (or Input / Baseline / Ours) at `width="280"`, then a narrower table of one input against variations at `width="240"`.
- **An image method.** Use the same bordered `<table>` grid with PNG pairs at `width="280"` (three columns) or `width="400"` (two columns, about 856px total), keeping the bold header row.
- **A dataset.** Keep the logo, title, venue, badges and authors, and make the showcase table one row per category with sample clips; add a Download section with a pipe table before Installation.
- **A library.** Drop the authors and TL;DR, keep the 200px logo and the badge pair (Docs, PyPI), and replace the showcase with a two-column table of code snippet and output image.
- **A repo without demos.** Let the TL;DR close the header and move Quick Start up; the h3 linked title and h4 venue still give a compact header without a rule.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put results in a bordered `<table>` with bold column labels | Stack GIFs one above another with no labels |
| Keep every image in one table at the same `width` | Mix widths within a row |
| Link interactive results from a thumbnail and say so in `<sub>(click to explore)</sub>` | Hide the viewer link in body text |
| Use one TL;DR sentence under the authors | Repeat the full abstract in the header |
| Check that the bibtex entry parses (FreeOrbit4D's misses a comma after `title`) | Leave citation fields unchecked |
| Point the badge and in-text project links to the same URL | Use two different hosts for the project page |

## Agent Prompt Guide

1. "Write a README header in GitHub HTML: a centred `<p>` with a logo at `width="200"`, then `### <p align="center">[Full paper title](https://arxiv.org/abs/XXXX.XXXXX)</p>` so the title is a blue #0969da h3 link, a centred `<h4>` venue line, a centred `<p>` with two `?style=for-the-badge` badges (Project PAGE `green` #67ac09, arXiv #b31b1b, label #555555), a centred author line with `<sup>` affiliation numbers, a centred affiliation line, and a centred bold `<h4>` TL;DR sentence."
2. "Under the TL;DR, build a results showcase as `<div align="center"><table>` with a header row of bold labels Input Video, Interactive 4D (with `<br><sub>(click to explore)</sub>`), Output Video, and three example rows of `<td align="center"><img ... width="280"></td>`, linking the middle thumbnail to the viewer. Follow it with `### Multiple Trajectories from a Single Input` and a second table of Input Video, Trajectory #1, Trajectory #2 at `width="240"`."
3. "After the showcase, write `##` sections in this order: 🔥 News (bold full dates), Installation (with an h3 Setup `bash` block), Quick Start, Custom Camera Trajectories (a centred 760px screenshot and a numbered list), Run on Your Own Video (h3 Step 1 and Step 2), Citation, Acknowledgements. Use `bash` for every command block."

## Similar Pages

- readme-microsoft-renderformer also opens with a logo above the title, venue and author line, but shows results as one gallery image and navigates with bold text links instead of badges.
- readme-deepmancer-hairport uses the same `for-the-badge` style, with seven badges and numbered paper figures rather than a table of GIFs.
- readme-sisyphm-studiorecon covers a neighbouring 4D reconstruction topic with a single composite teaser and a stage table instead of a clip grid.

## Quick Start

````markdown
<p align="center">
  <img src="assets/title.png" width="200">
</p>

### <p align="center">[ProjectName: Full Paper Title](https://arxiv.org/abs/XXXX.XXXXX)</p>

<h4 align="center">Venue Year</h4>

<p align="center">
  <a href="https://example.org/project/"><img src="https://img.shields.io/badge/Project-Page-green.svg?style=for-the-badge"></a>
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://example.org/">Author One</a><sup>1</sup>,
  <a href="https://example.org/">Author Two</a><sup>2</sup>
</p>

<p align="center">
  <sup>1</sup>Institution A, <sup>2</sup>Institution B
</p>

<h4 align="center"><b>TL;DR: One sentence that states the contribution.</b></h4>

<div align="center">
<table>
<tr>
<td align="center"><b>Input Video</b></td>
<td align="center"><b>Interactive 4D</b><br><sub>(click to explore)</sub></td>
<td align="center"><b>Output Video</b></td>
</tr>
<tr>
<td align="center"><img src="assets/demo/a_input.gif" width="280"></td>
<td align="center"><a href="https://example.org/viewer"><img src="assets/demo/a_inter.png" width="280"></a></td>
<td align="center"><img src="assets/demo/a_output.gif" width="280"></td>
</tr>
</table>
</div>

### Multiple Trajectories from a Single Input

<div align="center">
<table>
<tr>
<td align="center"><b>Input Video</b></td>
<td align="center"><b>Trajectory #1</b></td>
<td align="center"><b>Trajectory #2</b></td>
</tr>
<tr>
<td align="center"><img src="assets/demo/b_input.gif" width="240"></td>
<td align="center"><img src="assets/demo/b_traj1.gif" width="240"></td>
<td align="center"><img src="assets/demo/b_traj2.gif" width="240"></td>
</tr>
</table>
</div>

For more results, please visit our [project page](https://example.org/project/).

## 🔥 News
- **Month D, YYYY**: 🤗 We release the code!

## Installation

### Setup

```bash
# Clone the repository and its submodules.
git clone --recursive https://github.com/org/name.git
```

## Quick Start

```bash
python run_pipeline.py full --config configs/scenes/example.yaml
```

## Custom Camera Trajectories

<p align="center">
  <img src="assets/editor.png" width="760">
</p>

1. Step one.
2. Step two.

## Run on Your Own Video

### Step 1 — Prepare the input

### Step 2 — Run the pipeline

## Citation

```bibtex
@inproceedings{key,
  title        = {...},
}
```

## Acknowledgements
````

## Provenance

- Repo: https://github.com/VVeiCao/FreeOrbit4D (`README.md`, branch `main`, last README commit 700ead9 on 2026-08-12).
- Paper: "FreeOrbit4D: Training-Free Arbitrary Camera Redirection for Monocular Videos via Foreground-Complete 4D Reconstruction", SIGGRAPH Conference Papers '26 (SIGGRAPH 2026), arXiv 2601.18993; first author Wei Cao. Project page https://freeorbit4d.vision.ischool.illinois.edu/.
- Selection: builds the results showcase as bordered HTML tables (input, interactive 4D, output, then input versus two trajectories), a clear grid pattern for video work that stays neat under a small logo and TL;DR line.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for both badge URLs, the logo, one showcase GIF, one viewer PNG, one trajectory GIF and both screenshots fetched from the repo for pixel sizes and frame counts.
- Written 2026-10-28.
