# World from Motion — README Reference

> A gallery wall with one lit screen: quiet centred credits, four bold words for doors, and a single dark loop that wipes old against new.

**Theme:** both

Read from `README.md` on the default branch `main` of github.com/GradientSpaces/World-from-Motion (last commit touching the file f8a38a7, 2026-10-18; captured 2026-10-28). Evidence is the raw Markdown, the HTML that GitHub's API returns for it, a first-screen capture and a 2700px tall capture of the light theme with the README column 920px wide (856px content width), and `docs/assets/teaser.webp` fetched from the repo for its size, frame count and colors. The capture files are saved at 1200×750, a 0.833 scale of the 1440×900 window; every y value below is converted back to the 1440×900 frame. GitHub sets the type (its system stack, Segoe UI in the Windows captures), the 16px body size and the heading rules; nothing in the README overrides them. The README is 4 KB and has no badges at all.

## Overview

The README is a paper title page done almost entirely in Markdown. Inside one `<div align="center">` come a `#` title with GitHub's grey rule, a `###` subtitle without a rule, a bold venue line, two lines of linked author names joined by middle dots with superscript affiliation numbers, a two-entry affiliation line, and a row of four bold text links separated by ` · `. The only image is a full-width animated WebP that loops a 2×3 grid of scenes on a near-black frame, each with a sliding divider between the initial reconstruction and the method's result; its bottom edge lands at the fold. After the centred block the page becomes left-aligned prose with four plain `##` sections: a four-step numbered Getting started list, a seven-row code-structure table, BibTeX, and a combined acknowledgements and license paragraph. There are no badges, no emoji, no news, no results table and no `<details>`.

## Header Block

Rendered positions are y values in the 1440×900 frame (the README box starts at y≈25 with its "README.md" file bar). The block opens with `<div align="center">` followed by a blank line, so the Markdown inside is still parsed.

1. **Title** (y≈140): `# World from Motion`. GitHub h1, 2em (32px), weight 600, centred, with the 1px grey rule across the 856px content width.
2. **Subtitle** (y≈206): `### Generative Dynamic Gaussian Reconstruction from Monocular Video`. GitHub h3, 1.25em (20px), weight 600, no rule; it is a real heading and appears in the outline menu.
3. **Venue line** (y≈246): `**NeurIPS 2026**`. A bold body-size paragraph, no link and no badge.
4. **Authors** (y≈286 and 310): Markdown links `[Liyuan Zhu](https://www.zhuliyuan.net/)<sup>1,2</sup> ·` on separate source lines, a `<br>` after the fifth name, nine names in total. The source newlines render as spaces, so the separator reads " · ".
5. **Affiliations** (y≈350): `<sup>1</sup>Stanford University &nbsp; <sup>2</sup>NVIDIA`. Plain text, one non-breaking space between entries; no equal-contribution or corresponding-author marks are used.
6. **Link row** (y≈390): `[**Project page**](...) · [**Paper**](...) · [**Teaser**](...) · [**Interactive viewer**](...)`. Four bold body-size links in GitHub link blue, separated by middle dots. "Teaser" links to an `.mp4` on the project site and "Interactive viewer" to a hosted 3D Gaussian viewer.
7. **Teaser** (y≈418 to about 905): `<a href="https://research.nvidia.com/labs/amri/projects/world-from-motion/"><img src="docs/assets/teaser.webp" width="100%" alt="Six in-the-wild scenes rendered from a new camera path. ..."></a>`. The animated WebP is 1024×582, so `width="100%"` renders it 856×487; it links to the project page, not to itself. There is no visible caption; the description lives in the `alt` text and in a line drawn inside the image.
8. **Close and intro**: `</div>`, then a three-sentence left-aligned paragraph that names MoSca and DiffSynth in plain text. This ends the header block.

## Badges

The README uses no shields.io or image badges. The only button-like element is the bold link row.

| Label | Message | Color (hex) | Style | Links to |
|---|---|---|---|---|
| (link row) | **Project page** · **Paper** · **Teaser** · **Interactive viewer** | GitHub link blue | bold Markdown links separated by ` · ` | research.nvidia.com/labs/amri/projects/world-from-motion/, arxiv.org/abs/2607.01202, the project's `hero_teaser.mp4`, the project's `interactive_3dgs/` viewer |

Colors visible on the page that are not GitHub's own come from the teaser: a near-black frame #0c0c0c, light grey serif header text, and "World from Motion" in a yellow-green whose sampled pixels range from #638b21 to #7aba00 (anti-aliased; the exact source value is inferred to be close to NVIDIA green #76b900). The h1 rule is GitHub's #d1d9e0.

## Section Outline

| Level | Text | What it holds |
|---|---|---|
| h1 (centred, ruled) | World from Motion | title only |
| h3 (centred) | Generative Dynamic Gaussian Reconstruction from Monocular Video | subtitle; venue, authors, affiliations, link row and teaser follow without a heading |
| h2 | Getting started | a four-item ordered list, each item one sentence ending in a doc link, the fourth with **Ours (sample)** and **Ours (distill)** in bold; then a paragraph naming two Hugging Face repos in inline-code links |
| h2 | Code structure | a two-column Directory / Contents table, seven rows |
| h2 | Citation | a `bibtex` block, no lead sentence |
| h2 | Acknowledgements and license | two paragraphs: license with links to LICENSE and NOTICE, then third-party credits linking THIRD_PARTY_NOTICES.md |

Absent from the source: badges, news, results or leaderboard table, installation commands in the README (they live in `docs/INSTALL.md`), model zoo table, `<details>`, table of contents, contact section, emoji, a caption under the teaser.

Present but unusual: the subtitle is an h3 directly under the h1, so there is no h2 in the header; the teaser is an animated WebP rather than a GIF or MP4; one link in the link row ("Teaser") is a bare video file; Getting started gives no commands at all, only links to four docs; the Hugging Face model and mask repos appear as inline-code link text (`` [`liyzzz/World-from-Motion`](...) ``) rather than badges.

## Components

**Centred Markdown block.** `<div align="center">` with blank lines inside, so headings, bold text and links are plain Markdown yet centred. Spacing comes only from GitHub's paragraph and heading margins.

**Dot-separated credits.** Author names and the link row both use ` · ` (space, middle dot, space) as the separator, written as a trailing `·` at the end of each source line. Superscripts are `<sup>1,2</sup>` with no space before them.

**Bold link row.** Four `[**Name**](url)` links, one per source line, standing in for badges.

**Numbered getting-started list.** An ordered list of four imperative sentences (Build, Prepare, Reconstruct, Reproduce), each pointing to one Markdown doc; the fourth wraps onto an indented continuation line.

**Code-structure table.** Pipe table with `| --- | --- |` and no alignment colons, so GitHub centres the header cells and left-aligns the body; the left column is a directory in inline code (`src/wfm/`, `docs/`, `scripts/`, `config/`, `tests/`, `reproduce/`, `vendor/`), the right column a short noun phrase. The rendered table is about 650px wide, narrower than the column.

**Citation.** `@inproceedings{zhu2026worldfrommotion, ...}` with fields aligned by ` = ` and the full author list in natural order joined by `and`; the long author line scrolls horizontally in the rendered block.

**License paragraph.** Prose with inline links, combined with acknowledgements under one heading.

## Imagery

| Image | Type | Source size | Markdown | Rendered at 920px | Placement |
|---|---|---|---|---|---|
| teaser.webp | animated WebP, 73 frames at 67 ms (about 4.9 s, infinite loop), near-black frame #0c0c0c | 1024×582 | `<img ... width="100%">` inside `<a>` to the project page, inside the centred div | 856×487 | last element of the header, directly after the link row |

The teaser carries its own header strip, "initial reconstruction ◂|▸ World from Motion" in a serif face with the method name in yellow-green, over a grey line "same new camera path · each scene from a single monocular video". Below it a 2×3 grid of in-the-wild clips each shows a white vertical divider with a round handle that sweeps across the frame, left of the divider the baseline and right of it the method. No `<picture>` switch is used; the dark frame reads on both GitHub themes, and the rest of the page is text, so the README works in both.

## Adapting to Other Content

- **A library.** Keep the `#` name, `###` one-line description and the bold link row (Docs · PyPI · Examples); drop authors and affiliations; replace the teaser with a short code block.
- **A dataset.** Keep the full header and swap the teaser for a looping sample grid at `width="100%"` (856px); turn Code structure into a split table (Split / Size / Download).
- **A benchmark with scores.** Add a `## Results` table after Getting started with numeric columns right-aligned (`| ---: |`); World from Motion links to `REPRODUCTION.md` for numbers instead, so this is an extension.
- **A repo without a teaser.** End the centred block at the link row; the h1 rule plus the link row still give a finished header.
- **More install detail.** Keep it in `docs/INSTALL.md` and link it from step 1 rather than growing the README.

## Do's and Don'ts

| Do | Don't |
|---|---|
| Use bold text links separated by ` · ` instead of badges | Add a badge row next to the link row |
| Make the one teaser animated and full width (`width="100%"`) | Stack several teasers or a GIF plus a video link in the header |
| Put the comparison inside the teaser (a sweeping divider) | Explain the before/after in a long caption |
| Keep Getting started to four numbered links to docs | Paste long install commands into the README |
| Show the layout as a Directory / Contents table | Paste a full `tree` dump |
| Leave a blank line after `<div align="center">` so Markdown still parses | Hand-write every header element in HTML |

## Agent Prompt Guide

1. "Write a README header inside `<div align="center">` with blank lines so Markdown parses: `# Name`, `### Full subtitle`, `**Venue Year**`, author links joined by ` · ` with `<sup>1,2</sup>` marks and a `<br>` after the fifth name, an affiliation line `<sup>1</sup>Institution &nbsp; <sup>2</sup>Institution`, then four bold links `[**Project page**](...) · [**Paper**](...) · [**Teaser**](...) · [**Interactive viewer**](...)`, and one animated WebP at `width="100%"` linked to the project page. No badges."
2. "After `</div>`, write a three-sentence intro, then four `##` sections: Getting started (an ordered list of four one-sentence steps, each linking one doc), Code structure (a two-column Directory / Contents table with `| --- | --- |` and directories in inline code), Citation (a `bibtex` block) and Acknowledgements and license (two paragraphs)."
3. "Design the teaser as a near-black #0c0c0c frame with a one-line serif header naming baseline and method, the method name in yellow-green, and a 2×3 grid of clips each with a white sweeping divider; export as a looping animated WebP about 1024px wide."

## Similar Pages

- readme-eku127-satnav: the same centred academic sequence (title, subtitle, venue, authors, affiliations, links, full-width teaser), but SatNav uses a badge row and a caption where World from Motion uses bold text links and none.
- readme-mdyao-photoagent: also a full-width visual teaser under centred credits, but with a logo, `for-the-badge` buttons and many more body sections.
- readme-seohongpark-ogbench: shows the opposite choice for links, pulling Paper and Project page out as heading-size text under the teaser.

## Quick Start

````markdown
<div align="center">

# ProjectName
### Full Subtitle of the Paper

**Venue Year**

[Author One](https://example.org/)<sup>1,2</sup> ·
[Author Two](https://example.org/)<sup>2</sup> ·
[Author Three](https://example.org/)<sup>2</sup><br>
[Author Four](https://example.org/)<sup>1</sup> ·
[Author Five](https://example.org/)<sup>2</sup>

<sup>1</sup>Institution A &nbsp; <sup>2</sup>Institution B

[**Project page**](https://example.org/project/) ·
[**Paper**](https://arxiv.org/abs/XXXX.XXXXX) ·
[**Teaser**](https://example.org/project/teaser.mp4) ·
[**Interactive viewer**](https://example.org/project/viewer/)

<a href="https://example.org/project/"><img src="docs/assets/teaser.webp" width="100%" alt="Describe what the looping teaser shows."></a>

</div>

Three-sentence introduction: what goes in, what the method does, what it builds on.

## Getting started

1. Build the environment using the [installation guide](docs/INSTALL.md).
2. Prepare the [model bundle](docs/ASSETS.md).
3. Run the method with the [usage guide](docs/USAGE.md).
4. Reproduce **Main result** using [REPRODUCTION.md](REPRODUCTION.md).

## Code structure

| Directory | Contents |
| --- | --- |
| `src/pkg/` | What it holds |
| `docs/` | What it holds |

## Citation

```bibtex
@inproceedings{key,
  title = {...},
  year = {2026}
}
```

## Acknowledgements and license
````

## Provenance

- Repo: https://github.com/GradientSpaces/World-from-Motion (`README.md`, branch `main`, last README commit f8a38a7 on 2026-10-18).
- Paper: "World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video", NeurIPS 2026 (arXiv 2607.01202); first author Liyuan Zhu. Project page https://research.nvidia.com/labs/amri/projects/world-from-motion/.
- Selection: it shows restraint well, with a centred academic header, plain-text links in place of badges, one dark before/after teaser, a four-step getting-started list, a code-structure table and nothing extra.
- Evidence: raw Markdown and GitHub-rendered HTML (saved 2026-10-28), first-screen and 2700px captures at a 920px README column, `docs/assets/teaser.webp` fetched from the repo and read for size, frame count, frame duration and colors.
- Written 2026-10-28.
