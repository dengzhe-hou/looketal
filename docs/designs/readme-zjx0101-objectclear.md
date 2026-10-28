# ObjectClear — README Reference

> A before-and-after contact sheet under a red wordmark: the logo, the title, a neat row of blue tags, and then six columns of photographs where the skater, the cow and the cyclist simply vanish, shadows and all.

**Theme:** light

Read from `README.md` on the default branch `main` of github.com/zjx0101/ObjectClear (last commit touching the file c052d91, 2026-08-03; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io and api.infinitescript.com return for each badge URL; image sizes come from the PNG and GIF headers fetched from the repo, and the wordmark color from a pixel count on the logo PNG. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README opens on a classic CV-paper first screen, everything wrapped in one `<div align="center">`. A small red "Object Clear" wordmark with a mirrored reflection sits at the top, then the full paper title as a centred `<h2>` with GitHub's grey rule, four linked author names with superscript marks, one affiliation line, a bold "CVPR 2026", and a row of five flat badges (four shields.io, one live visitor counter) in shades of blue plus arXiv red. A bold centred one-sentence summary introduces a full-width teaser that does two jobs: the top row shows three input-with-mask and output pairs, and the two rows below compare ObjectClear with four named baselines under a label strip. A centred "For more visual results, go checkout our project page" line and a horizontal rule close the header. The body then switches to emoji-prefixed `##` headings (⭐ Update, 🎃 Overview, 📷 OBER Dataset, ⚙️ Installation, ⚡ Inference, 🚀 Training, 📊 Evaluation with ReMOVE+, 🪄 Interactive Demo, 📝 License, 📑 Citation, 📧 Contact), a dated update list with fire emoji on the latest two items, a fully ticked TODO checklist, two wide method figures, a large dataset sample grid and two side-by-side demo GIFs.

## Header Block

The whole block, including the teaser and the closing rule, sits inside one `<div align="center">`. Every element is written as HTML, so nothing in the header depends on Markdown parsing except the closing `---`. Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Wordmark** (y≈96–144): `<img src="./assets/ObjectClear_logo.png" alt="ObjectClear Logo" style="height: 52px;">` inside a `<div style="text-align: center;">`. GitHub drops the div's `style` but keeps the image's `height: 52px`, so the 969×262 PNG renders 192×52. The letters are solid #c00000 on a white (not transparent) background, with a faded mirror image underneath.
2. **Title** (y≈192): `<h2>Precise Object and Effect Removal with Adaptive Target-Aware Attention</h2>`, centred by the outer div. GitHub h2, 1.5em (24px), weight 600, with the bottom rule across the 856px column; it takes the first slot in GitHub's outline menu.
3. **Authors** (y≈241): a `<div>` of four `<a target='_blank'>` names separated by `&emsp;`, with `<sup>*</sup>` and `<sup>*,†</sup>` marks. The last `<a>` is never closed in the source; GitHub closes it after the `<sup>`, so the marks render inside the link, in link blue. The marks are not explained anywhere in the README (inferred: equal contribution and corresponding author).
4. **Affiliation** (y≈266): `<div>S-Lab, Nanyang Technological University&emsp;</div>`, plain text.
5. **Venue** (y≈290): `<div><strong>CVPR 2026 </strong></div>`, bold body text, no link.
6. **Badge row** (y≈325–345): five badges inside `<div><h4 align="center"> ... </h4></div>`. Because the container is an `<h4>`, the row gets heading margins (24px above) and an empty-looking entry in GitHub's outline. Each badge is 20px tall; with one space between images the row spans about 620px. Details in Badges.
7. **Summary sentence** (y≈378–402, two lines): `<strong>ObjectClear is an object removal model that can jointly eliminate the target object and its associated effects ...</strong>`, bold, centred, body size.
8. **Teaser** (y≈432 to about 945, crossing the fold): `<div style="width: 100%; text-align: center; margin:auto;"><img style="width:100%" src="assets/teaser.png"></div>`. GitHub keeps the `width: 100%` on the image, so the 2174×1304 PNG renders 856×513. No `alt`.
9. **More-results line**: `For more visual results, go checkout our <a href="..." target="_blank">project page</a>`, centred.
10. **Rule**: a Markdown `---` on its own line inside the div renders a full-width `<hr>` (the blank line before it re-enables Markdown). The div then closes and `## ⭐ Update` starts left-aligned.

## Badges

Every badge uses the flat default style: 20px tall, 3px corner radius, a faint vertical gloss, Verdana 11px, label on #555555, white (#ffffff) text. Four come from shields.io static paths, one from a badgen-style counter. Each `<img>` sits inside its own `<a target='_blank'>` on separate source lines, indented inside the `<h4>`. No badge has `alt` text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| 🐳 (emoji only) | Project Page | named `blue`, #007ec6 (label #555555) | flat (default) | zjx0101.github.io/projects/ObjectClear/ |
| arXiv | 2505.22636 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2505.22636 |
| Demo | 🤗 Hugging Face | named `blue`, #007ec6 (label #555555) | flat (default) | huggingface.co/spaces/jixin0101/ObjectClear |
| Dataset | 🧸 OBER | named `blue`, #007ec6 (label #555555) | flat (default) | huggingface.co/datasets/sczhou/OBERDataset_ObjectClear |
| Visitors | live count (36,978 in the first-screen capture) | #3977dd (label #555555) | flat (badgen-style SVG from `api.infinitescript.com/badgen/count?...&color=3977dd`) | not linked by the author (GitHub links the image to itself) |

Rendered widths are about 100, 116, 142, 108 and 103px. Emoji sit inside the label or message text, not as shields.io logos: the Project Page badge's label is the whale alone, and the Demo and Dataset messages begin with 🤗 and 🧸. Three of five messages share #007ec6 and the counter's #3977dd is a near neighbour, so the row reads as a blue strip with one red arXiv tag.

Other colored marks on the page: the wordmark is #c00000, and the teaser overlays each target object with a translucent green mask outline (not measured; its role is "selected region"). The method figures use their own pastel boxes and a red dashed frame around the attention module; these were not measured.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h2 (centred, inside div) | Precise Object and Effect Removal with Adaptive Target-Aware Attention | title; authors, affiliation, venue follow in divs |
| h4 (centred, inside div) | (badge images only) | the badge row; summary, teaser, results link and rule follow |
| h2 | ⭐ Update | five bullets `- [YYYY.MM] ...`, newest first, the latest two in bold with 🔥 |
| h3 | ✅ TODO | four `- [x]` task-list items, all ticked |
| h2 | 🎃 Overview | the pipeline figure only, no text |
| h2 | 📷 OBER Dataset | data pipeline figure, a definition paragraph, a 🔥 release line, a 🚩 blockquote on the non-commercial license, the sample grid |
| h2 | ⚙️ Installation | a numbered list of two steps, each with an indented `bash` block |
| h2 | ⚡ Inference | h3 "Quick Test": a paragraph with bold and underlined (`<u>`) sentences, an untagged directory tree, a `shell` block with two `##` comment lines, a **Note:** blockquote |
| h2 | 🚀 Training | four numbered h3 steps (weights, dataset, training, validation), `shell` blocks including a 29-line `accelerate launch` command, untagged tree, a final **Note:** blockquote |
| h2 | 📊 Evaluation with ReMOVE+ | two paragraphs, link to `evaluation/README.md` |
| h2 | 🪄 Interactive Demo | one paragraph, a `shell` block, two GIFs side by side |
| h2 | 📝 License | a bold "Non-Commercial Use Only Declaration" line and one paragraph |
| h2 | 📑 Citation | one sentence and a `bibtex` block |
| h2 | 📧 Contact | one sentence with two addresses in inline code |

Absent from the source: a Markdown results table (results live in the teaser image and on Google Drive links), a model zoo table, a table of contents, an acknowledgements section, a `<picture>` dark variant.

Present but unusual: the paper title is an `<h2>` and the badge row an `<h4>`, so both enter the outline; the teaser carries its own baseline labels instead of a Markdown caption; the Overview section is a figure with no prose; the TODO list is kept with every box ticked; one author link is left unclosed in the source.

## Components

**Centred HTML header.** One outer `<div align="center">` wraps nested `<div>` blocks, one per element (title, authors, affiliation, venue, badges), separated by `&emsp;` inside lines rather than by paragraphs. Divs have no margin, so authors, affiliation and venue stack tightly (about 24px apart) while the `<h4>` badge row and the bold summary get paragraph-sized gaps.

**Badge row in a heading.** `<h4 align="center">` containing `<a target='_blank'><img src="https://img.shields.io/badge/..."></a>` pairs, label #555555, messages #007ec6, #b31b1b, #007ec6, #007ec6, then the #3977dd counter.

**Update list.** `- [YYYY.MM] Sentence.` with the month in square brackets; the two newest entries open with `**🔥 ... !**` in bold, older ones are plain. Links go to Hugging Face and Google Drive; an in-page link (`[Training](#-training)`) jumps to an emoji heading's anchor.

**Ticked TODO.** `### ✅ TODO` with `- [x]` items that GitHub renders as disabled, checked boxes.

**Notes and warnings.** Markdown blockquotes: `> 🚩 Note that ... **non-commercial** ...` and `> **Note:** ...`, rendered with GitHub's grey left bar, not GitHub alert syntax.

**Stepwise install.** A numbered list whose items contain indented fenced `bash` blocks with `#` comment lines; later sections use `shell` as the language tag and leave directory trees untagged.

**Side-by-side GIFs.** `<p align="center">` with two `<img width="49%">` GIFs on separate lines.

**Citation and contact.** "If you find our repo useful for your research, please consider citing our paper:" then `@InProceedings{zhao2026objectclear, ...}` with aligned `=` signs; the contact line puts both e-mail addresses in inline code rather than `mailto:` links.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| ObjectClear_logo.png | PNG wordmark, red with reflection, white background | 969×262 | `<img ... style="height: 52px;">` | 192×52 | top of header |
| teaser.png | PNG, 6-column photo grid with label strips | 2174×1304 | `<img style="width:100%">` in a div | 856×513 | header, after the bold summary |
| ObjectClear_pipeline.png | PNG, two-panel method diagram (Training, Inference) | 2404×1032 | `![overall_structure](...)` | 856×367 | 🎃 Overview |
| OBER_pipeline.png | PNG, two-panel data pipeline (camera-captured, simulated) | 3650×923 | `![OBER_dataset_pipeline](...)` | 856×216 | 📷 OBER Dataset, first |
| dataset_samples.png | PNG, sample grid with masks | 3593×2178 | `![OBER_dataset_samples](...)` | 856×519 | 📷 OBER Dataset, last |
| user_clicks.gif, user_strokes.gif | animated GIF demo recordings | 1280×720 each | `<img width="49%">` pair in `<p align="center">` | about 419×236 each | 🪄 Interactive Demo |

The teaser is the selling image. Its top row alternates "Input with Mask" and "ObjectClear (Ours)" for three scenes (skater with shadow, figure on a jetty with reflection, cyclist with reflection), labels set in white serif type on a dark strip over each photo. A thin grey line separates two lower rows that compare six columns, captioned beneath in black serif: Input with Mask, PowerPaint, RORem, OmniEraser, OmniPaint, ObjectClear (Ours). The baseline columns show leftover shadows or ghosted animals, so the grid makes the "effects" claim visually. The method figures use paper-style serif labels on white. No image switches with `<picture>`, and the logo's white background would show as a white block in dark mode.

## Adapting to Other Content

- **An image-editing or restoration method.** Keep the whole header; build the teaser as three input/output pairs on top and a labelled method-vs-baselines grid below, exported about 2200px wide so it renders 856px with readable labels, and keep the "more results on the project page" line under it.
- **A dataset.** Promote the dataset section's two figures (pipeline at about 3650×923, sample grid at about 3600×2200) into the header in place of the teaser, and keep the 🚩 license blockquote right under them.
- **A library.** Drop authors, venue and teaser; keep the wordmark at `height: 52px`, the badge row and the bold one-sentence summary, then go straight to Installation.
- **A repo without a logo.** Let the `<h2>` title open the header; nothing else changes.
- Put the badge row in a `<p align="center">` instead of an `<h4>` if the outline menu matters; the visual result is nearly the same with a smaller top margin.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Label every column of a comparison teaser with the method name, own method last as "(Ours)" | Show outputs without saying which method made them |
| Pair inputs with masks visibly drawn on them | Make readers guess which object was removed |
| Keep badges in one flat family on the #555555 label | Mix flat badges with `for-the-badge` or social badges |
| Add `alt` text to badges and the teaser | Leave every image without `alt`, as this README does |
| Close every `<a>` in the author line | Rely on GitHub to repair unclosed tags |
| Use a dated `[YYYY.MM]` update list and mark only the newest items with 🔥 | Put fire on every entry |

## Agent Prompt Guide

1. "Write a centred README header in one `<div align="center">`: a wordmark PNG with `style="height: 52px;"` (red #c00000 letters), an `<h2>` with the full paper title, a div of four linked authors separated by `&emsp;` with `<sup>` marks, a div with the affiliation, a div with `<strong>Venue Year</strong>`, then an `<h4 align="center">` row of flat badges on the #555555 label: emoji-labelled Project Page #007ec6, arXiv #b31b1b, Demo 🤗 Hugging Face #007ec6, Dataset #007ec6, Visitors counter #3977dd."
2. "Below the badges add one bold centred sentence that says what the model removes, then a full-width teaser (`<img style="width:100%">`, about 2174×1304, renders 856×513): a top row of three input-with-mask/output pairs and two lower rows comparing Input with Mask, four baselines and 'Ours (last)', labels inside the image. Close with a centred 'For more visual results, see our project page' line and `---`."
3. "Write the body with emoji-prefixed `##` headings in this order: ⭐ Update (`- [YYYY.MM] ...`, newest two bold with 🔥), ### ✅ TODO (`- [x]` items), 🎃 Overview (figure only), 📷 Dataset (figures plus a 🚩 license blockquote), ⚙️ Installation (numbered steps with `bash`), ⚡ Inference, 🚀 Training, 📊 Evaluation, 🪄 Interactive Demo (two `width="49%"` GIFs), 📝 License, 📑 Citation (`bibtex`), 📧 Contact."

## Similar Pages

- readme-itsmag11-omegance: also from S-Lab, NTU, with the same top-to-bottom order of title, author line, "S-Lab, Nanyang Technological University", a bold venue and a badge row, written in Markdown rather than nested divs.
- readme-drexubery-viewcrafter: a logo image sized with an inline `style="height:..."` above a flat shields.io row that includes a Hugging Face demo badge.
- readme-mdyao-photoagent: another image-editing repo with an icon, a centred title and a Hugging Face badge, but using `for-the-badge` tags.
- readme-eku127-satnav: the same centred paper-header sequence with a full-width teaser, built from `<p align="center">` blocks and without emoji headings.

ObjectClear's distinguishing choices are the labelled baseline comparison inside the teaser, a badge row placed in an `<h4>`, and emoji on every body heading.

## Quick Start

````markdown
<div align="center">
<div>
    <img src="./assets/logo.png" alt="ProjectName logo" style="height: 52px;">
    <h2>Full Paper Title</h2>
</div>

<div>
    <a href="https://example.org/">Author One<sup>*</sup></a>&emsp;
    <a href="https://example.org/">Author Two</a>&emsp;
    <a href="https://example.org/">Author Three<sup>*,†</sup></a>
</div>
<div>
    Lab, University
</div>

<div>
    <strong>Venue Year</strong>
</div>

<div>
    <h4 align="center">
        <a href="https://example.github.io/project/"><img src="https://img.shields.io/badge/%F0%9F%90%B3-Project%20Page-007ec6" alt="Project page"></a>
        <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg" alt="arXiv"></a>
        <a href="https://huggingface.co/spaces/org/name"><img src="https://img.shields.io/badge/Demo-%F0%9F%A4%97%20Hugging%20Face-007ec6" alt="Demo"></a>
        <a href="https://huggingface.co/datasets/org/name"><img src="https://img.shields.io/badge/Dataset-Name-007ec6" alt="Dataset"></a>
        <img src="https://api.infinitescript.com/badgen/count?name=org/name&ltext=Visitors&color=3977dd" alt="Visitors">
    </h4>
</div>

<strong>ProjectName is a model that does X while preserving Y.</strong>

<div>
    <img style="width:100%" src="assets/teaser.png" alt="Inputs with masks, baselines and ours">
</div>

For more visual results, see our <a href="https://example.github.io/project/">project page</a>

---
</div>

## ⭐ Update
- [YYYY.MM] **🔥 Training code is now released!**
- [YYYY.MM] Release the inference code and demo.

### ✅ TODO
- [x] Release the training code

## 🎃 Overview
![overall_structure](assets/pipeline.png)

## 📷 Dataset
![dataset_pipeline](assets/data_pipeline.png)

> 🚩 Note that the dataset is made available solely for **non-commercial** research use.

## ⚙️ Installation
1. Clone Repo
    ```bash
    git clone https://github.com/org/name.git
    ```

## ⚡ Inference

## 🚀 Training

## 📊 Evaluation

## 🪄 Interactive Demo
<p align="center">
  <img src="assets/demo1.gif" width="49%" />
  <img src="assets/demo2.gif" width="49%" />
</p>

## 📝 License

## 📑 Citation
```bibtex
@InProceedings{key,
    title = {...},
}
```

## 📧 Contact
````

## Provenance

- Repo: https://github.com/zjx0101/ObjectClear (`README.md`, branch `main`, last README commit c052d91 on 2026-08-03).
- Paper: "Precise Object and Effect Removal with Adaptive Target-Aware Attention", CVPR 2026, arXiv 2505.22636; first author Jixin Zhao. Project page https://zjx0101.github.io/projects/ObjectClear/.
- Selection: a textbook first screen; a wordmark, title, authors, venue and a uniform badge row sit above a labelled baseline comparison grid with a link to more results, followed by a dated update list and clean method figures.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, SVGs for all five badge URLs (the whale label fetched URL-encoded), PNG/GIF headers for all images and a pixel count on the logo.
- Written 2026-10-28.
