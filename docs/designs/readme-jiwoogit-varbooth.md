# ARBooth — README Reference

> A photo booth at a pet show: a drawn kiosk holds up the paper title like a shop sign, and a wall of portrait prints of one fluffy dog does the rest.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/jiwoogit/VARBooth (last commit touching the file febf8f4, 2025-07-24; captured 2026-10-28). The README calls the project ARBooth throughout, and its clone line points to `github.com/jiwoogit/ARBooth.git`. Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a 1440×900 first-screen capture and a 2700px tall capture of the light theme, with the README column 920px wide (856px content width). Badge colors come from the SVGs that shields.io returns for the four badge URLs; image sizes and colors come from `assets/logo.png`, `assets/main_white.png` and `assets/main_black.png` fetched from the repo. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them.

## Overview

The README has no text title at all. Its first element is a wide illustrated banner (`assets/logo.png`, 856×221 rendered) in which a cartoon photo booth labelled "ARBooth", with a camera on its roof and an orange-red curtain, stands at the left end of a pale blue rounded panel #deebf7 that holds the paper title in heavy black sans-serif on two lines. Logo, project name and paper title are one image. Below it sit four centred flat badges, a `---` rule, one sentence naming the paper and venue, and a full-width sample grid (856×336) that shows the subject photos on the left and twelve generated variations captioned "⟨S*⟩ dog ..." with the token in red. The grid is a `<picture>` with separate light and dark versions. Another `---` rule fences a three-item task checklist, a third rule follows it, and the rest is a plain sequence of eleven h2 sections (Overview through Contact) with short paragraphs and `bash` blocks. There are no tables, no results, no emoji and no news list.

## Header Block

Rendered positions are y values in the 1440×900 capture (the README box starts at y≈25 with its "README.md" file bar; content starts at y≈80).

1. **Banner** (y≈96–312): `![ARBooth Title](assets/logo.png "Fine-Tuning Visual Autoregressive Models for Subject-Driven Generation")`. A plain Markdown image, not centred and not sized; the 3584×925 PNG is scaled by GitHub's `max-width: 100%` to 856×221. The paper title is in the image and in the image's `title` attribute (shown as a hover tooltip), never as text. The PNG has a transparent background (about 45% of its pixels); the booth is drawn with dark outlines on cream #fef5de and the title panel is #deebf7.
2. Two blank lines in the source, which add no extra space.
3. **Badge row** (y≈347): one `<p align="center">` holding four `<a><img src="https://img.shields.io/badge/..."></a>` lines, each 20px tall; the row spans about 438px. Details in Badges.
4. **Rule** (y≈388): `---`, GitHub's 4px grey `hr`.
5. **Intro sentence** (y≈427–451): `This is the official implementation for the paper "[ICCV 2025] Fine-Tuning Visual Autoregressive Models for Subject-Driven Generation".` Left-aligned body text, wrapping to two lines. This is the only place the venue appears.
6. **Sample grid** (y≈480 to about 815): a `<picture>` with `<source srcset="assets/main_black.png" media="(prefers-color-scheme: dark)">`, `<source srcset="assets/main_white.png" media="(prefers-color-scheme: light)">` and a fallback `<img src="assets/main_white.png" alt="ARBooth Main">`. No width is set; the 4931×1938 PNG scales to 856×336. Not wrapped in a centred block, so it starts at the left content edge.
7. **Rule** (y≈846): `---`, then the "Status Checklist" h2 lands at the fold (y≈888).

## Badges

All four use the static path form with no `style=`, `logo=` or `labelColor=` parameter, so they render in shields.io's default `flat` style: 20px tall, 3px corner radius, Verdana 11px, label on the default #555555 grey, white message text.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| ArXiv | 2504.02612 | #b31b1b (label #555555) | flat (default) | arxiv.org/abs/2504.02612 |
| (none) | Project-Page | #4b8bbe, one segment | flat (default) | jiwoogit.github.io/ARBooth |
| HuggingFace | ARBooth | `yellow`, which shields.io currently renders #d8b800 (label #555555) | flat (default) | huggingface.co/wldn0202/ARBooth |
| Docker | ready | `blue` #007ec6 (label #555555) | flat (default) | hub.docker.com/repository/docker/wldn0202/arbooth/general |

The Project-Page badge is a single colored block because its path `Project--Page-4b8bbe` uses `--` (an escaped hyphen) and has only one text field, so shields.io treats the text as the message with no label. The other three follow the "label, then message" form. The source writes the label as "ArXiv" with a capital A. The METHOD_README table gives `yellow` as #dfb317; the SVG that shields.io returns on 2026-10-28 fills it with #d8b800, which is the value seen in the capture.

Other colors on the page come from images, not badges: the banner panel #deebf7 and booth body #fef5de, and the red #ff0000 "⟨S*⟩" token in the grid captions. Caption text is black #000000 in `main_white.png` and white #ffffff in `main_black.png`; both grid files have transparent backgrounds.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| (image) | ARBooth banner | logo and paper title as one image; badges, rule, intro sentence, sample grid and rule follow without a heading |
| h2 | Status Checklist | a three-item GitHub task list (one checked, two open), followed by `---` |
| h2 | Overview | two sentences |
| h2 | Hardware Requirements | one sentence and one bullet ("GPU Memory: **≥ 40GB**") |
| h2 | Installation | h3 "Option 1: Manual Setup" (sentence, three-line `bash` block) and h3 "Option 2: Docker Setup" (sentence, one-line `bash` block, a Docker Hub link line) |
| h2 | Pretrained Checkpoints | link to the upstream weights, an untagged two-file tree, then a bold sentence linking the fine-tuned checkpoints |
| h2 | Data Preprocessing | one paragraph pointing to DreamMatcher |
| h2 | Training | sentence with inline-code variables, one-line `bash` block, two sentences on output and config |
| h2 | Evaluation | metric names in one sentence, one-line `bash` block |
| h2 | Inference | one sentence, one-line `bash` block |
| h2 | Fine-tuning Tips | two bold-titled bullets, each with indented sub-bullets |
| h2 | Acknowledgements | four `*` bullets of "Name (owner/repo)" links and a thank-you line |
| h2 | Citation | one sentence and a `bibtex` block |
| h2 | Contact | one `*` bullet with a name and mailto link |

Absent from the source: a text title or `#` heading, author and affiliation lines, news, results table, model zoo table, demo GIF or video, license section, table of contents, emoji anywhere.

Present but unusual: the only h1-level identity is an image with the title in its tooltip; the venue appears only inside the intro sentence's quotation marks; the project is named ARBooth while the repository is VARBooth; the Project-Page badge has no label segment; the status checklist sits between two rules directly under the hero, ahead of the Overview; the sample grid uses `<picture>` while the banner above it does not.

## Components

**Banner image.** `![Alt](assets/logo.png "Paper title")`: a Markdown image with a title string, no HTML, no width. Logo, name and paper title are drawn together in one 3584×925 PNG, so the header is one picture rather than a stack of text.

**Badge row.** `<p align="center">` with one `<a href><img src="https://img.shields.io/badge/..." alt="..."></a>` per line. Messages #b31b1b, #4b8bbe, #d8b800 and #007ec6; labels #555555. Each `alt` is the destination name ("arXiv", "Project Page", "Hugging Face", "Docker").

**Fencing rules.** `---` between the badges and the intro, after the sample grid, and after the checklist. The three rules box the hero and the checklist off from the documentation; no other section is fenced.

**Status checklist.** `- [x]` and `- [ ]` items. GitHub renders them as disabled checkboxes with no bullet, one checked ("Code & checkpoint upload completed") and two open feature items.

**Two-option install.** An h2 with two h3 options ("Option 1: Manual Setup", "Option 2: Docker Setup"), each a one-sentence lead and a `bash` block, the Docker option ending with a plain "Docker Hub link:" line.

**One-command sections.** Training, Evaluation and Inference each hold one sentence, a one-line `bash` block calling `scripts/<task>_arbooth.sh`, and at most two sentences after it.

**Bold call-out sentence.** The fine-tuned checkpoint link is a whole bold paragraph (`**You can download our fine-tuned checkpoints from [Hugging Face (wldn0202/ARBooth)](...).**`) rather than a badge or alert.

**Nested tip bullets.** `- **Iteration Settings**:` followed by two-space-indented sub-bullets, the same for `- **Class Prompt Selection**:`.

**Code blocks.** `bash` for commands and `bibtex` for the citation; the weights tree is an untagged block with box-drawing characters.

**Citation and contact.** One lead sentence ("If our paper or repository assists your research, kindly cite us:"), an `@article{chung2025fine, ...}` block, then a Contact section with one bullet "Name ([email](mailto:email))".

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| logo.png | PNG, transparent background, cartoon booth plus title panel | 3584×925 | `![ARBooth Title](assets/logo.png "...")`, no width | 856×221 | first element |
| main_white.png / main_black.png | PNG pair, transparent background, photo grid with typeset captions | 4931×1938 each | `<picture>` with two `<source media="(prefers-color-scheme: ...)">` and a light fallback `<img>` | 856×336 | after the intro sentence |

The grid has a narrow left column of four subject photos labelled "Subject", then two rows of six generated square images, each with a two- or three-line serif caption beginning with the red "⟨S*⟩" token ("⟨S*⟩ dog wearing a top hat", "⟨S*⟩ dog riding a motorcycle along a coastal highway"). The captions are part of the image, so the dark version swaps black caption text for white. The banner has no dark variant; its title stays legible on the pale blue panel in either theme, while the booth's dark outlines sit directly on the page background (inferred from the transparent pixels; the dark theme was not captured).

## Adapting to Other Content

- **A library.** Replace the booth banner with a wordmark banner at the same aspect (about 4:1, 856×221 rendered), keep the centred flat badge row with a single-segment project badge, and replace the sample grid with a short usage example.
- **A dataset.** Keep the banner and make the `<picture>` grid a sample gallery with captions baked into the image in both light and dark versions; add a Download section in place of Pretrained Checkpoints.
- **A benchmark with scores.** Keep the banner, badges and checklist, and add a results table after Overview, since this README has none; right-align numeric columns (`| ---: |`) and bold the best value.
- **A repo without a teaser.** Let the banner carry the page alone: banner, badge row, `---`, intro sentence, `---`, checklist, `---`.
- **A repo with a text title requirement.** Add `<h1 align="center">` with the project name under the banner, since the image title is invisible to search and screen readers apart from its alt and tooltip.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Draw the name and the paper title into one banner image if the project has a mascot | Repeat the same title as text directly under a banner that already shows it |
| Put the paper title in the image's title string and alt | Leave a banner image with no alt text |
| Use `<picture>` with light and dark versions for figures whose captions are baked in | Ship a transparent figure with black captions only |
| Fence the hero and the checklist with `---` rules | Fence every short section, which flattens the hierarchy |
| Keep each run section to one sentence and one `bash` line | Spread one script call across several paragraphs |
| Keep badges flat with the #555555 label | Mix a one-segment badge into a row without checking it reads as intended |
| Name the venue once, clearly | Hide the venue only inside a quoted sentence if the venue matters to readers |

## Agent Prompt Guide

1. "Start a README with a full-width banner image `![Name Title](assets/logo.png "Full paper title")` that combines a mascot and the paper title on a pale blue #deebf7 panel (about 3584×925 source, 856×221 rendered). Below it, a `<p align="center">` row of four flat shields.io badges: ArXiv-ID #b31b1b, a one-segment Project--Page #4b8bbe, HuggingFace-Name `yellow` (#d8b800), Docker-ready `blue` #007ec6, labels on the default #555555. Then `---`."
2. "After the rule, write one sentence naming the paper and venue in brackets, then a `<picture>` with `main_black.png` for `prefers-color-scheme: dark` and `main_white.png` for light (856×336 rendered), then `---`, an h2 Status Checklist with `- [x]` and `- [ ]` items, and `---`."
3. "Write plain h2 sections in this order: Overview, Hardware Requirements, Installation (h3 Option 1: Manual Setup and h3 Option 2: Docker Setup, each with a `bash` block), Pretrained Checkpoints (untagged tree plus one bold link sentence), Data Preprocessing, Training, Evaluation, Inference (one `bash` line each), Fine-tuning Tips (bold bullets with sub-bullets), Acknowledgements, Citation (`bibtex`), Contact. No emoji and no tables."

## Similar Pages

- **readme-snuhcc-dice-bench** also opens with a full-width banner image that carries the name and paper title, but repeats the title as a text h1 underneath and adds emoji section headings and tables.
- **readme-deepseek-ai-deepseek-v3** opens with an image wordmark too, sized at `width="60%"` and centred, with three rows of badges under it.
- **readme-eku127-satnav** is the text-built opposite: centred h1 and h2 title, authors and affiliations as HTML text, and a single-version teaser.

## Quick Start

````markdown
![Name Title](assets/logo.png "Full Paper Title")


<p align="center">
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img src="https://img.shields.io/badge/ArXiv-XXXX.XXXXX-b31b1b.svg" alt="arXiv"></a>
  <a href="https://example.github.io/project"><img src="https://img.shields.io/badge/Project--Page-4b8bbe.svg" alt="Project Page"></a>
  <a href="https://huggingface.co/org/name"><img src="https://img.shields.io/badge/HuggingFace-Name-yellow.svg" alt="Hugging Face"></a>
  <a href="https://hub.docker.com/r/org/name"><img src="https://img.shields.io/badge/Docker-ready-blue.svg" alt="Docker"></a>
</p>

---

This is the official implementation for the paper "[Venue Year] Full Paper Title".

<picture>
  <source srcset="assets/main_black.png" media="(prefers-color-scheme: dark)">
  <source srcset="assets/main_white.png" media="(prefers-color-scheme: light)">
  <img src="assets/main_white.png" alt="Name Main">
</picture>

---

## Status Checklist

- [x] Code & checkpoint upload completed
- [ ] Planned feature

---

## Overview

Two sentences.

## Hardware Requirements

* GPU Memory: **≥ XXGB**

## Installation

### Option 1: Manual Setup

```bash
git clone https://github.com/org/name.git
cd name
pip install -r requirements.txt
```

### Option 2: Docker Setup

```bash
docker pull org/name:latest
```

## Pretrained Checkpoints

```
weights/
├── base_model.pth
└── vae.pth
```

**You can download our fine-tuned checkpoints from [Hugging Face (org/name)](https://huggingface.co/org/name).**

## Training

```bash
bash scripts/train.sh
```

## Evaluation

```bash
bash scripts/eval.sh
```

## Inference

```bash
bash scripts/infer.sh
```

## Fine-tuning Tips

- **Tip title**:
  - Detail

## Acknowledgements

* [Project (owner/repo)](https://github.com/owner/repo)

## Citation

If our paper or repository assists your research, kindly cite us:

```bibtex
@article{key,
  title={...},
}
```

## Contact

* Name ([email@example.com](mailto:email@example.com))
````

## Provenance

- Repo: https://github.com/jiwoogit/VARBooth (`README.md`, branch `main`, last README commit febf8f4 on 2025-07-24). The README names the project ARBooth.
- Paper: "Fine-Tuning Visual Autoregressive Models for Subject-Driven Generation", ICCV 2025, arXiv 2504.02612; first author Jiwoo Chung. Project page https://jiwoogit.github.io/ARBooth.
- Selection: the custom illustrated banner merges logo and title into one header image, with a captioned subject-driven sample grid and horizontal rules separating a status checklist from the rest of the docs.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), 1440×900 and 2700px captures at a 920px README column, shields.io SVGs for the four badge URLs, and the three PNGs fetched from the repo for pixel sizes, transparency and colors.
- Written 2026-10-28.
