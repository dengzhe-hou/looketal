# MotionBricks — README Reference

> A product manual from a studio that ships: a plain left-set title, four quiet tags, a filmstrip of hooded characters and robots, then prose that explains itself in short sentences.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/NVlabs/motionbricks (last commit touching the file 54fc563, 2026-10-23; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors and widths come from the SVGs that shields.io returns for the four badge URLs; image sizes and the GIF's context and target colors come from the files in `docs/media/` fetched through Git LFS. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README reads like documentation rather than a paper poster. The first line is an ordinary left-aligned `#` heading holding the full paper title on two lines, with GitHub's grey rule under it. A single centred `<p>` holds both the four flat badges and the teaser, a 1600×668 filmstrip: four rendered stills of a hooded character with ghosted white target poses across the top, and ten small frames of a Unitree G1 robot across the bottom, all inside a thin dark frame. Then the page is prose: two paragraphs, a four-bullet "what you get" list with bold leads, and a short note pointing to a guided tutorial. The body has fifteen plain `##` sections with no emoji. One full-width GIF explains the method, two-column HTML tables pair SOMA and G1 GIFs for each demo, and two pipe tables carry the repository layout and the checkpoints. There are no author names, affiliations or venue line in the header.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈24 with its "README.md" file bar; content starts at y≈90).

1. **Title** (y≈116–156, two lines): `# MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives`. GitHub h1, 2em (32px), weight 600, left-aligned, with a 1px grey rule under the second line at y≈184.
2. **Badge row** (y≈200–220): the first four lines of one `<p align="center">`, each `<a href="..."><img src="https://img.shields.io/badge/..." alt="..."></a>`. Each badge is 20px tall and the row spans about 472px. Details in Badges.
3. **Teaser** (y≈233 to about 590): the fifth line of the same `<p>`, `<img src="docs/media/teaser.jpg" alt="MotionBricks animates characters and robots with one model" width="100%">`. At `width="100%"` it is too wide to share the line, so it wraps under the badges and renders at 856×357. No link and no caption; the `alt` text is a full sentence.
4. **Intro** (y≈618 onward): two left-aligned paragraphs. The first defines the model and links to the "How MotionBricks works" anchor; the second links the "SIGGRAPH 2026 paper" in running text, which is the only place the venue appears above the fold.
5. **Offer list** (below the fold): four bullets, each opening with a bold noun phrase ("**Pretrained models**", "**A Python runtime**", "**Two demos**", "**Two editors**") followed by plain text with in-page anchor links.
6. **Closing note**: one paragraph that ends "New to MotionBricks? The [guided tutorial](docs/guided_tutorial.md) walks through all four apps". The `## News` heading follows.

## Badges

All four use the static path form `https://img.shields.io/badge/<label>-<message>-<color>` in shields.io's default `flat` style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on the default #555555 grey and white (#ffffff) text with a #010101 text shadow. None has a logo.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| Project | Page | #007ec6 (`blue`, label #555555) | flat (default) | nvlabs.github.io/motionbricks/ |
| arXiv | 2604.24833 | #b31b1b (label #555555) | flat (default), `.svg` suffix | arxiv.org/abs/2604.24833 |
| Hugging Face | Models | #d8b800 (`yellow` as shields.io now draws it, label #555555, white text) | flat (default) | `#checkpoints` (in-page anchor) |
| License | Apache 2.0 | #76b900 (label #555555) | flat (default), `.svg` suffix | LICENSE |

Badge widths from the SVGs: 86, 116, 134 and 124px. The named `yellow` renders today as #d8b800 with white text in the served SVG, not the older #dfb317. The Hugging Face badge does not leave the page; it jumps to the Checkpoints table, which then links to Hugging Face. The license message color #76b900 is NVIDIA's brand green.

Other colored marks come from the imagery, not from badges: in `core_idea.gif` the context poses are bright green (median sampled value about #22cd5e) and the target pose is light blue (about #38a5e0), with white generated poses between them on a dark charcoal stage (about #202020). The prose refers to these as "green above" and "blue above".

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 | MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives | title; badges, teaser, intro, offer list and tutorial note follow without a heading |
| h2 | News | one undated bullet |
| h2 | Setup | hardware sentence, install sentence with links, a two-line `sh` block, a note on the TensorRT cache |
| h2 | How MotionBricks works | the `core_idea.gif` at 100%, two bullet lists with bold terms (context, target; root module, pose module, decoder) and prose on chaining; one h3 "One runtime for SOMA and G1" |
| h2 | Repository layout | one sentence, a two-column Folder / Contents table with five linked folders |
| h2 | Inbetweener | one sentence, a 2×1 HTML table of GIFs headed SOMA / Unitree G1, a one-line `sh` block, a link to its doc |
| h2 | Scene Preview | one paragraph, a 2×4 HTML table of GIFs, a two-line `sh` block, a link to its doc |
| h2 | Editors | one paragraph, a 2×1 HTML table of PNG screenshots, a two-line `sh` block, two paragraphs |
| h2 | Checkpoints | one paragraph, a `> Note:` blockquote, a six-column model table with two bold model names, a link to two model cards |
| h2 | Export ONNX models | one paragraph, an `sh` block with `#` comment labels, two paragraphs of options |
| h2 | Documentation | bold link to the guided tutorial, then three bold group labels (Apps, Integration, Models) each over bullets of the form `**[Doc](...):** description` |
| h2 | Related humanoid work at NVIDIA | eight bullets, `[Name](url): lower-case description` |
| h2 | Citation | one sentence and a `bibtex` block with aligned `=` |
| h2 | License | one sentence and four bullets with bold labels (Code, Documentation and media, Models, Sample motions), then three paragraphs |
| h2 | Acknowledgments | six bullets, `[Project](url) for <role>` |
| h2 | Contact | two sentences |

Absent from the source: author list, affiliations, venue line in the header, table of contents, results table, star-history chart, emoji anywhere, dated news entries, captions under images.

Present but unusual: badges and teaser share one `<p align="center">`, so the teaser's centring comes from the badge paragraph; the title is left-aligned while the badges are centred; the Hugging Face badge links to an in-page anchor; demo media are laid out in HTML `<table>` grids with column headers rather than stacked images; the bundled-models note is a plain `> Note:` blockquote, not a GitHub alert; the Contact section says the project is not accepting contributions.

## Components

**Centred media paragraph.** One `<p align="center">` with badge links on the first four lines and a `width="100%"` image on the fifth; the image wraps below the badges because it cannot share their line.

**Badge row.** Four flat badges, label #555555, messages #007ec6, #b31b1b, #d8b800 and #76b900, each with a descriptive `alt` ("Project Page", "Paper", "Hugging Face Models", "License").

**Bold-lead bullets.** Bullets that open with a bold noun phrase or term and continue in plain text: in the intro ("**Pretrained models** for the..."), in How it works ("The **context** is..."), in License ("**Code:** Apache 2.0"). Sentences are short and declarative throughout.

**Media comparison grid.** HTML `<table>` with a header row of `<th>` labels (SOMA, Unitree G1, or the two editor names) and rows of `<td><img ... width="100%"></td>`, so each cell's image fills about half the column. Scene Preview stacks four rows of paired GIFs.

**Folder table.** Pipe table `| Folder | Contents |` with `| --- | --- |` delimiters and no alignment colons; GitHub centres the header and left-aligns the body. Each folder is a link to itself, and Contents is a short noun list.

**Checkpoint table.** Six columns with explicit alignment: `|:-------|:-------------|:------:|:------:|:-------------:|:-------------:|`, so Model and Skeleton are left-aligned and Training Data, FPS, Hugging Face and License are centred. Model names are bold (`**MotionBricks-SOMA-RP-v1**`); the Hugging Face cell is the word "Link".

**Run commands.** Each app section ends with "Run it with this command:" (or a near variant) and a short `sh` block, then a link to that app's doc. All command blocks use the `sh` tag; the citation uses `bibtex`. GitHub renders them on its light grey code background with a copy button.

**Documentation index.** Bold paragraph labels (`**Apps**`, `**Integration**`, `**Models**`) over bullets of `**[Name](path):** one or two sentences`, so the link itself is the bold term.

**Note.** A plain blockquote that starts with "Note:" for a single caveat (bundled ONNX models make the checkpoint download optional).

**Citation.** One sentence "If you use this code in your research, please cite:" then `@article{wang2026motionbricks, ...}` with fields padded so the `=` signs align.

**License and acknowledgements.** Bulleted, with bold category labels for licenses and `for <role>` endings for acknowledgements. No badges or logos below the header.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.jpg | JPEG filmstrip in a thin dark frame | 1600×668 | `<img ... width="100%">` in the badge `<p align="center">` | 856×357 | header, under the badges, no caption |
| core_idea.gif | animated GIF, 38 frames, dark stage | 1280×480 | `<img ... width="100%">` in `<p align="center">` | 856×321 | first element of How MotionBricks works |
| inbetweener_soma.gif, inbetweener_g1.gif | animated GIFs (the SOMA one has 84 frames) | 1280×560 (SOMA) | `<td><img ... width="100%"></td>` | about 400px wide each (half the table, less cell padding) | Inbetweener, side by side |
| scene_preview_*.gif, locomotion_*_soma.gif, locomotion_*_g1.gif | animated GIFs | not measured | `<td><img ... width="100%"></td>` in a four-row table | about 400px wide each | Scene Preview |
| smart_primitive_editor.png, scene_editor.png | PNG screenshots of dark editor UIs | 1600×900 | `<td><img ... width="100%"></td>` | about 400×225 each | Editors |

Every image has a descriptive `alt` sentence ("Context poses in green, a strobe of generated poses, and a target pose in blue"). The teaser is a photographic render inside its own dark border, and the GIFs and editor screenshots sit on dark charcoal backgrounds, so the imagery reads on both GitHub themes without `<picture>` switching; the flat badges also work on both. The media live in Git LFS (the repo stores pointer files), which GitHub serves transparently.

## Adapting to Other Content

- **A library.** This README already works as one: keep the left-aligned `#` name, the four-badge row (Docs, PyPI, License and one destination), an intro paragraph and a bold-lead "what you get" list, then Setup, a How it works figure and a folder table.
- **A dataset.** Replace the checkpoint table with a split table in the same alignment pattern (name left, counts centred), and use the two-column `<table>` grid to pair samples from two sources at about 400px each.
- **A paper repo that needs authors.** Keep the plain h1, add one left-aligned author line under it, and leave the badges and teaser in the centred `<p>`; the venue stays in running text.
- **A repo without a teaser.** Close the centred `<p>` after the badges and let the How it works GIF (856px) carry the explanation, moved up to follow the intro.
- **A tool with several apps.** Give each app its own `##` with one sentence of purpose, a media grid, "Run it with this command:" and a one-line `sh` block, then a link to its doc.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Keep the title a plain left-aligned `#` and let the prose carry the venue | Stack author, affiliation and venue blocks over a documentation README |
| Put a full-sentence `alt` on every image | Leave GIFs without alternative text |
| Pair related demos in a `<table>` with `<th>` labels | Stack eight GIFs one above another |
| End each app section with one short command and a doc link | Inline the full option list in the README |
| Map each top-level folder to its purpose in a two-column table | Paste a full repository tree |
| Write bold-lead bullets with short declarative sentences | Pad sections with emoji or decorative dividers |
| Point a badge at an in-page anchor when the table there holds the links | Duplicate external links in both the badge row and the table |

## Agent Prompt Guide

1. "Write a README opening in GitHub Markdown: a left-aligned `# Name: Full Paper Title`, then one `<p align="center">` holding four flat shields.io badges (label #555555; messages Project Page #007ec6, arXiv #b31b1b, Hugging Face Models #d8b800 linking to `#checkpoints`, License Apache 2.0 #76b900) and, on the next line of the same paragraph, a `width="100%"` teaser with a one-sentence `alt`. Follow with two plain paragraphs and four bullets that start with a bold noun phrase."
2. "Write plain `##` sections in this order: News, Setup, How it works (a full-width GIF, then bullets with bold terms), Repository layout (two-column Folder / Contents table with `| --- |`), one section per app, Checkpoints, Export, Documentation, Related work, Citation, License, Acknowledgments, Contact. Use the `sh` tag for every command block and no emoji."
3. "For each app section, write one sentence of purpose, an HTML `<table>` whose header row names the two variants and whose cells hold `<img ... width="100%">` GIFs, then 'Run it with this command:' and a one-line `sh` block, then a link to the app's doc. For the checkpoint table, align columns `|:---|:---|:---:|:---:|:---:|:---:|` and bold the model names."

## Similar Pages

- **readme-chuan-10-agile**: also documentation-first, with a module table that maps parts to purpose, but AGILE keeps a centred academic header with authors and for-the-badge tags.
- **readme-eku127-satnav**: shares the runnable setup near the top and the resource tables, but opens with a centred title page and a bold venue line where MotionBricks has none.
- **readme-letianhuang-transparentgs**: the opposite approach to a long manual; it keeps setup, arguments and a GUI tutorial in one README, where MotionBricks moves detail into linked docs and keeps each app section short.
- **readme-adobe-research-obj-and-mat-selection**: a SIGGRAPH 2026 neighbour with tables throughout, but a full author header, a venue logo and a contents list.

## Quick Start

````markdown
# ProjectName: Full Paper Title

<p align="center">
  <a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/Project-Page-blue" alt="Project Page"></a>
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg" alt="Paper"></a>
  <a href="#checkpoints"><img src="https://img.shields.io/badge/Hugging%20Face-Models-yellow" alt="Hugging Face Models"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-76B900.svg" alt="License"></a>
  <img src="docs/media/teaser.jpg" alt="One sentence describing the teaser" width="100%">
</p>

ProjectName is a ... It ... See [How it works](#how-projectname-works).

This repository provides ... based on the [Venue paper](https://arxiv.org/abs/XXXX.XXXXX):

- **Pretrained models** for ...
- **A runtime**, built on ...
- **Demos**: an [App](#app) that ...

## News

- One sentence.

## Setup

```sh
uv sync
```

## How ProjectName works

<p align="center">
  <img src="docs/media/core_idea.gif" alt="Describe what the colors mean" width="100%">
</p>

- The **context** is ...
- The **target** is ...

## Repository layout

| Folder | Contents |
| --- | --- |
| [pkg](pkg) | The library: ... |
| [app](app) | The demos ... |

## App

One sentence of purpose.

<table>
  <tr>
    <th>Variant A</th>
    <th>Variant B</th>
  </tr>
  <tr>
    <td><img src="docs/media/app_a.gif" alt="Variant A demo" width="100%"></td>
    <td><img src="docs/media/app_b.gif" alt="Variant B demo" width="100%"></td>
  </tr>
</table>

Run it with this command:

```sh
uv run python -m app.demo
```

## Checkpoints

> Note: one caveat.

| Model | Skeleton | Training Data | FPS | Hugging Face | License |
|:-------|:-------------|:------:|:------:|:-------------:|:-------------:|
| **Model-A-v1** | [Rig](https://example.org/) | [Data](https://example.org/) | 30 | [Link](https://huggingface.co/org/name) | [License](https://example.org/) |

## Documentation

**Apps**

- **[App](docs/app.md):** What it covers.

## Citation

If you use this code in your research, please cite:

```bibtex
@article{key,
  title   = {...},
}
```

## License

- **Code:** [Apache 2.0](LICENSE).

## Acknowledgments

## Contact
````

## Provenance

- Repo: https://github.com/NVlabs/motionbricks (`README.md`, branch `main`, last README commit 54fc563 on 2026-10-23).
- Paper: "MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives", SIGGRAPH 2026 (ACM Transactions on Graphics 45(4)), DOI 10.1145/3811334, arXiv 2604.24833; first author Tingwu Wang. Project page https://nvlabs.github.io/motionbricks/.
- Selection: documentation-first restraint, with plain prose, a filmstrip teaser, a How it works figure explained in short bullets, and a repository-layout table that maps folders to purpose, with almost no decoration.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, `teaser.jpg`, `core_idea.gif`, `inbetweener_soma.gif` and the two editor PNGs fetched through Git LFS for pixel sizes and sampled colors.
- Written 2026-10-28.
