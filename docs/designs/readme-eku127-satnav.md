# SatNav — README Reference

> A mission briefing laid out on white paper: a centred title plate, a strip of six two-tone tags, then one wide satellite map that does the explaining.

**Theme:** light

Read from `README.md` on the default branch `master` of github.com/Eku127/SatNav (last commit touching the file 922690d, 2026-09-28; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the badge URLs and the SVGs that shields.io returns for them; workflow diagram colors come from `docs/assets/readme/workflow.svg` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README opens like a paper title page. A centred `<h1>` "SatNav" and a centred `<h2>` subtitle each carry GitHub's grey bottom rule, so the top of the page reads as two ruled bands. Below them come a bold venue line, two lines of linked author names with superscript affiliation marks, a single affiliation line, one row of six flat shields.io badges in a shared "dark grey label, colored message" form, a two-link language toggle, and a full-width teaser image followed by an italic one-line caption. The teaser (2400×1184 PNG, 856×422 rendered) almost fills the rest of the first screen. After a two-sentence left-aligned introduction the body switches to ordinary GitHub prose with eight plain `##` sections and no emoji: a runnable Quick Start with two `bash` blocks, a color-keyed workflow diagram, a resource table, a baselines table, a task-oriented documentation table, a collapsed repository tree, BibTeX, license and acknowledgements. There is no news list and no results table.

## Header Block

Everything down to the caption sits in centred blocks. Rendered positions are y values in the 1440×900 capture (the README box starts at y=25 with its "README.md" file bar; content starts at y≈80).

1. **Title** (y≈115): `<h1 align="center">SatNav</h1>`. GitHub h1, 2em (32px), weight 600, with a 1px grey rule under it across the 856px content width.
2. **Subtitle** (y≈186–216, two lines): `<h2 align="center">A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery</h2>`. GitHub h2, 1.5em (24px), with the same bottom rule. Because it is a real heading, it also appears in GitHub's outline menu as the second entry.
3. **Venue line** (y≈265): `<p align="center"><strong>NeurIPS 2026 Evaluations &amp; Datasets</strong></p>`. Body size, bold, no link and no badge.
4. **Authors** (y≈305 and 329): one `<p align="center">` with seven `<a>` names, each followed by `<sup>1,*</sup>`-style marks, separated by `&nbsp;` and broken after the fourth name with `<br>`. Three names link to web pages and four link to `mailto:` addresses. `*` marks equal contribution and `†` the corresponding author by convention; the README itself never defines either mark (inferred).
5. **Affiliations** (y≈369): `<p align="center"><sup>1</sup> HKUST(GZ) &nbsp;&nbsp; <sup>2</sup> LASER, IDEA &nbsp;&nbsp; <sup>3</sup> HKUST</p>`. Plain text, double non-breaking spaces between entries.
6. **Badge row** (y≈397–417): one `<p align="center">` holding six `<a><img src="https://img.shields.io/badge/..."></a>` lines. Each badge is 20px tall; the newlines between tags render as single spaces, and the row spans about 752px. Details in Badges.
7. **Language toggle** (y≈451): `<p align="center"><a href="docs/en-US/README.md">English</a> &nbsp;|&nbsp; <a href="docs/zh-CN/README.md">简体中文</a></p>`. Two body-size links with a plain pipe.
8. **Teaser** (y≈480 to about 902): `<p align="center"><a href="docs/assets/readme/overview-final.png"><img src="docs/assets/readme/overview-final.png" width="100%" alt="..."></a></p>`. `width="100%"` gives 856px wide and about 422px tall at the 920px column; the image links to itself. Its bottom edge lands at the fold of the 900px window.
9. **Caption** (just below the fold): `<p align="center"><em>Follow boundaries, navigate between landmarks, and trace routes through satellite scenes.</em></p>`.
10. **Intro paragraph**: plain Markdown, left-aligned, two sentences, with **SatSim** in bold. This ends the header block.

## Badges

All six use the static path form `https://img.shields.io/badge/<label>-<message>-<hex>` with no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 grey. Message text is white (#ffffff) on dark messages and #333333 on the yellow ones, as shields.io picks it from the background.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Paper | arXiv | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2609.31507 |
| Paper | OpenReview | #8c1b13 (label #555555) | flat (default) | openreview.net/forum?id=hOEniyN6hl |
| Website | Project Page | #2a8c82 (label #555555) | flat (default) | eku127.github.io/SatNav/ |
| Wiki | Documentation | #2878d0 (label #555555) | flat (default) | eku127.github.io/SatNav/wiki/ |
| Dataset | Hugging Face | #ffd21e (label #555555, message text #333333) | flat (default) | huggingface.co/datasets/Eku127/SatNav-Episodes-v0.1 |
| Models | Hugging Face | #ffd21e (label #555555, message text #333333) | flat (default) | huggingface.co/collections/Eku127/satnav-baseline-model-zoo |
| (link row) | English &nbsp;\|&nbsp; 简体中文 | GitHub link blue | plain links, not bold | docs/en-US/README.md, docs/zh-CN/README.md |

The label is a category (Paper, Website, Wiki, Dataset, Models) and the message is the destination, so two badges can share a label (both "Paper") or a message (both "Hugging Face"). Message colors follow the destination's own brand: arXiv red, OpenReview dark red, Hugging Face yellow; teal and blue for the project's own sites.

Other colored marks visible on the page come from the workflow diagram, not from badges: offline-training green #27834b, online-navigation blue #2563eb and evaluation amber #d69a12 (legend text #b47f0d), on box fills #f0fdf4, #eff6ff and #fffbeb.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred) | SatNav | title only |
| h2 (centred) | A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery | subtitle; venue, authors, affiliations, badges, language toggle, teaser, caption and intro follow without a heading |
| h2 | Quick Start | one bold lead sentence, a five-command `bash` block (clone, conda env, editable install), a one-line `bash` block that runs the example, the output path in inline code, links to the install guide and more examples |
| h2 | From satellite maps to navigation evaluation | linked workflow SVG, one paragraph, then two links separated by ` · ` (episode video, viewer guide) |
| h2 | Dataset & Model Zoo | bold linked dataset name with bold counts (118,494 episodes, 59 scenes), split names in inline code, a two-column Resource / Where to start table |
| h2 | Baselines | one sentence, a five-column model table (Model, Training, Evaluation, Checkpoints, Ref), notes on SwiftVLN, lightweight baselines and per-model environments |
| h2 | Documentation | a two-column "I want to… / Guide" table, a line linking the English and Chinese docs, and a `<details>` repository tree |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | License | one paragraph (MIT code license, separate data terms) |
| h2 | Acknowledgements | two paragraphs of linked project names |

Absent from the source: news or changelog, results or leaderboard table, demo GIF or embedded video, installation section separate from Quick Start, table of contents, contact section, star-history chart, emoji in headings.

Present but unusual: the subtitle is an `<h2>` rather than bold text, so it takes a heading rule and a slot in the outline; four author links are `mailto:` addresses; the teaser image links to its own file; the walk-through video is a plain text link to an `.mp4` in the repo rather than an embedded player; the Baselines table uses "—" in three cells for a model that is set up elsewhere.

## Components

**Centred HTML paragraph.** Every header element is its own `<p align="center">` (or `<h1>`/`<h2>` with `align="center"`), one element per block, so GitHub's paragraph margin (16px) is the only spacing. No `<br>` padding or empty paragraphs are used for spacing; `<br>` appears only inside the author line.

**Badge row.** Six static shields.io badges, each `<a href="..."><img src="https://img.shields.io/badge/Label-Message-HEX" alt="..."></a>` on its own source line. Label grey #555555 throughout; message colors #b31b1b, #8c1b13, #2a8c82, #2878d0, #ffd21e, #ffd21e. Every `alt` is a descriptive phrase ("Paper on arXiv", "SatNav Wiki").

**Bold lead sentence.** Sections open with a bold first sentence that states the outcome ("**Run your first episode with the bundled synthetic scene.**") followed by plain text.

**Code blocks.** Fenced with language tags: `bash` for commands (blank line separating clone, environment and install groups), `text` for the repository tree, `bibtex` for the citation. GitHub renders them on its light grey code background with a copy button.

**Link pairs.** Secondary links sit on one line separated by ` · ` (space, middle dot, space): "[Watch a Path Follower episode](...) · [Open the viewer guide](...)". The same separator joins two links inside a table cell.

**Resource tables.** Pipe tables with `| --- |` delimiters and no alignment colons. GitHub centres the header cells, left-aligns body cells and stripes alternate rows. The left column is a plain noun phrase; the right column is a single action link ("Download on Hugging Face", "Read the dataset specification"). The Documentation table phrases the left column as a user goal ("I want to…", "Bring my own navigation model").

**Model table.** Five columns: Model, Training, Evaluation, Checkpoints, Ref. Cells are short links ("Guide", "Download", "Use training outputs", "GitHub") pointing at anchors inside per-model docs (`#9-full-training`, `#10-configure-online-evaluation`). No numbers, no bold best values.

**Collapsible tree.** `<details><summary><strong>Repository structure</strong></summary>` wrapping a `text` block of seven `folder/  description` lines, collapsed by default.

**Citation.** One sentence "If you use SatNav in your research, please cite:" then an `@inproceedings{jiang2026satnav, ...}` block with braces protecting `{SatNav}` and `{UAV}` and a `note` field for the track.

**License and acknowledgements.** Prose paragraphs with inline links, no badges and no logos.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| overview-final.png | PNG, light panels on white | 2400×1184 | `<img ... width="100%">` inside `<a>` to itself, in `<p align="center">` | 856×422 | header, after the language toggle; italic centred caption below |
| workflow.svg | SVG, Arial labels, white background | width 1080, height 585 | `[![alt](workflow.svg)](workflow.svg)` with no width | 856×464 (scaled by GitHub's `max-width: 100%`) | first line of "From satellite maps to navigation evaluation" |

The teaser is a three-part panel: a stats card on the left (SatNav wordmark, 118K episodes, 59 scenes, 18 cities, 3 task families), a 3×3 grid of satellite crops grouped into Boundary, Landmark and Route rows, and a zoomed stadium episode with the instruction text in a light translucent box. The rows are keyed blue, green and yellow, which matches the workflow diagram's green, blue and amber legend in hue; whether the two use identical hex values was not measured (inferred to be close from the captures).

The workflow diagram uses rounded boxes with a colored left bar, a bold #172a42 title and two grey detail lines, connected by labelled arrows; a three-line color legend sits at its lower left. Neither image uses `<picture>` or a dark-theme variant. The one video is linked as text, not embedded.

## Adapting to Other Content

- **A library.** Keep the h1 name and h2 one-line description, drop the author and affiliation blocks, keep one badge row (Docs, PyPI, License) in the same label-grey form with one message color per destination, and put a short code example where the teaser was. Quick Start stays the first `##` section.
- **A dataset.** Keep the full header. Make the teaser a sample grid at `width="100%"` (856px), and move "Dataset & Model Zoo" ahead of Quick Start with the same two-column Resource / Where to start table.
- **A benchmark with scores.** Keep the Baselines table shape and add a separate results table after it with numeric columns right-aligned (`| ---: |`) and the best value in bold; SatNav itself has no such table, so this is an extension.
- **A repo without a teaser.** Let the badge row and language toggle close the header, and promote the workflow-style diagram (about 1080px wide source, rendered at 856px) to sit directly under the intro paragraph.
- **A single-language repo.** Drop the toggle paragraph entirely rather than leaving one link.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Put each header element in its own `<p align="center">` | Pad the header with empty paragraphs or stacked `<br>` |
| Keep every badge label on the default #555555 and vary only the message color | Mix `flat`, `for-the-badge` and logo badges in one row |
| Name the destination in the badge message (arXiv, OpenReview, Hugging Face) | Use generic messages like "link" or "here" |
| Give the teaser `width="100%"` and an italic one-line caption | Shrink the teaser to a thumbnail or leave it without a caption |
| Open the body with a runnable Quick Start that needs no download | Lead with a long installation matrix |
| Write table cells as one action link each | Fill tables with raw URLs |
| Collapse the repository tree in `<details>` | Show the full tree inline |

## Agent Prompt Guide

1. "Write a README header in GitHub Markdown: `<h1 align="center">` with the project name, `<h2 align="center">` with the full paper title, a centred bold venue line, a centred author line with `<sup>` affiliation marks and `&nbsp;` separators, a centred affiliation line, then one centred row of six flat shields.io badges (default label grey #555555; messages arXiv #b31b1b, OpenReview #8c1b13, Project Page #2a8c82, Documentation #2878d0, Hugging Face #ffd21e twice), a centred English | 中文 toggle, a `width="100%"` teaser linked to itself and an italic centred caption."
2. "After the header, write eight plain `##` sections in this order: Quick Start, a workflow section with a linked SVG diagram, Dataset & Model Zoo, Baselines, Documentation, Citation, License, Acknowledgements. Open Quick Start with one bold sentence, then a `bash` block for install and a one-line `bash` block for the first run. No emoji in headings."
3. "Build resource tables with two columns (a noun phrase, then one action link), `| --- |` delimiters and no alignment colons; join two links in a cell with ` · `. Put the repository tree in `<details><summary><strong>Repository structure</strong></summary>` with a `text` block, and end with a `bibtex` block introduced by one sentence."

## Similar Pages

This is the first README entry in the gallery, so no README neighbours are listed yet. Later centred-header academic READMEs can be compared on the h1, author, affiliation and badge-row sequence; SatNav's distinguishing choices are an `<h2>` subtitle with a rule, a single uniform badge family, a bilingual toggle and a Quick Start that runs on bundled data. Its project page (eku127.github.io/SatNav/) is a separate web page and is not described here.

## Quick Start

````markdown
<h1 align="center">ProjectName</h1>

<h2 align="center">
  Full Paper Title on One or Two Lines
</h2>

<p align="center">
  <strong>Venue Year Track</strong>
</p>

<p align="center">
  <a href="https://example.org/">Author One</a><sup>1,*</sup> &nbsp; <a href="https://example.org/">Author Two</a><sup>1,*</sup> &nbsp;
  <a href="https://example.org/">Author Three</a><sup>2</sup><br>
  <a href="https://example.org/">Author Four</a><sup>1,2,†</sup>
</p>

<p align="center">
  <sup>1</sup> Institution A &nbsp;&nbsp;
  <sup>2</sup> Institution B
</p>

<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/Paper-arXiv-B31B1B" alt="Paper on arXiv"></a>
  <a href="https://openreview.net/forum?id=XXXX"><img src="https://img.shields.io/badge/Paper-OpenReview-8C1B13" alt="Paper on OpenReview"></a>
  <a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/Website-Project%20Page-2A8C82" alt="Project website"></a>
  <a href="https://example.github.io/project/wiki/"><img src="https://img.shields.io/badge/Wiki-Documentation-2878D0" alt="Documentation"></a>
  <a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/badge/Dataset-Hugging%20Face-FFD21E" alt="Dataset on Hugging Face"></a>
  <a href="https://huggingface.co/collections/org/name"><img src="https://img.shields.io/badge/Models-Hugging%20Face-FFD21E" alt="Models on Hugging Face"></a>
</p>

<p align="center">
  <a href="docs/en-US/README.md">English</a> &nbsp;|&nbsp;
  <a href="docs/zh-CN/README.md">简体中文</a>
</p>

<p align="center">
  <a href="docs/assets/teaser.png">
    <img src="docs/assets/teaser.png" width="100%" alt="Describe the teaser.">
  </a>
</p>

<p align="center">
  <em>One-line caption for the teaser.</em>
</p>

Two-sentence introduction with the core component in **bold**.

## Quick Start

**State what the first run achieves.** Say what it does not need.

```bash
git clone https://github.com/org/name.git
cd name
pip install -e .
```

```bash
python examples/first_example.py
```

## From input to evaluation

[![Workflow](docs/assets/workflow.svg)](docs/assets/workflow.svg)

One paragraph. [Secondary link](docs/a.md) · [Secondary link](docs/b.md)

## Dataset & Model Zoo

| Resource | Where to start |
| --- | --- |
| Item | [Action link](https://example.org/) |

## Baselines

| Model | Training | Evaluation | Checkpoints | Ref |
| --- | --- | --- | --- | --- |
| Name | [Guide](docs/x.md) | [Guide](docs/y.md) | [Download](docs/z.md) | [GitHub](https://github.com/org/name) |

## Documentation

| I want to… | Guide |
| --- | --- |
| Goal | [Guide](docs/guide.md) |

<details>
<summary><strong>Repository structure</strong></summary>

```text
pkg/      What it holds
docs/     What it holds
```

</details>

## Citation

If you use ProjectName in your research, please cite:

```bibtex
@inproceedings{key,
  title = {...},
}
```

## License

## Acknowledgements
````

## Provenance

- Repo: https://github.com/Eku127/SatNav (`README.md`, branch `master`, last README commit 922690d on 2026-09-28).
- Paper: "SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery", NeurIPS 2026 Evaluations and Datasets Track, arXiv 2609.31507; first author Jiajun Jiang. Project page https://eku127.github.io/SatNav/.
- Selection: Learning pool, rank 1. The header is close to a model first screen (title, subtitle, venue, affiliations, one row of consistent labeled badges, a language toggle and an annotated teaser with a caption), and it leads straight into a runnable Quick Start, a color-keyed pipeline diagram and a tidy resource-to-link table.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the badge URLs, `workflow.svg` and the teaser PNG header fetched from the repo for colors and pixel sizes.
- Written 2026-10-28.
