# How a Look et al. README DESIGN.md is written (2026-10-28)

A code README has fewer design tools than a web page. GitHub fixes the font, colors, widths and heading styles; the author controls only the Markdown structure, the small set of HTML that GitHub allows (`align`, `width`, `<picture>`, `<details>`, `<sub>`, `<sup>`, tables), images and GIFs, and badges. A README DESIGN.md therefore records structure and presentation, not CSS. It follows the same evidence-first rules as `METHOD.md`.

## Evidence, in order of authority

1. **GitHub's own rendering**: `tools/readme_render.py` saves the HTML GitHub's API returns for the README and the raw Markdown; `tools/snap.py` captures the rendered page (README column 920px wide inside a 1440px window, light theme). Look at the first-screen and tall captures directly.
2. **Raw Markdown**: the source of every structural claim. Quote the exact Markdown or HTML for the header block, badges and any unusual component.
3. **Images and badges**: open badge URLs to read their style, label, message and color (shields.io parameters `style=`, `color=`, `logo=`, `labelColor=`). Give image widths as written in the source (`width="80%"`, `width=600`) and what they render to at a 920px column (856px content width).

## Rules

- Every claim names the Markdown that produces it. Write "inferred" only when the source cannot settle a value.
- Badge colors are hex values read from the badge URL or the shields.io named color (`blue` is `#007ec6`, `brightgreen` `#4c1`, `green` `#97ca00`, `yellow` `#dfb317`, `orange` `#fe7d37`, `red` `#e05d44`, `lightgrey` `#9f9f9f`, `blueviolet` `#8a2be2`, `success` `#4c1`, `informational` `#007ec6`).
- One property, one value across the file. The Agent Prompt Guide and Quick Start reuse values from the tables.
- Separate "absent from the source" from "present but unusual" in Section Outline.
- Theme: `light` when images and badges are designed for a white background only, `both` when the README switches images with `<picture>` and `prefers-color-scheme` or uses images that work on both, `dark` only if it is designed for GitHub's dark theme.

## Required sections (in order)

1. `# <Style name> — README Reference`, `> mood line`, `**Theme:**`, a one-paragraph measurement note (repo, README path, commit or date read, render width).
2. `## Overview`: what the README looks like as rendered.
3. `## Header Block`: the first screen in source order (logo, title, subtitle, authors, affiliations, venue line, badge rows, link navigation, teaser), each with its exact Markdown/HTML, alignment, width and the rendered size at 920px.
4. `## Badges`: table Label | Message | Color (hex) | Style | Links to. Include link rows that act as buttons (bold links separated by `|`).
5. `## Section Outline`: table of headings in order (level, text including emoji, what the section holds), then which standard sections are absent.
6. `## Components`: recipes for each recurring element (news list with date format, results tables with alignment and bold best values, model zoo table, collapsible `<details>`, code blocks with language tags, citation block, acknowledgement and license lines).
7. `## Imagery`: teaser and figure types (GIF, PNG, video link, `<picture>` pairs), widths, captions, placement.
8. `## Adapting to Other Content`: how to apply this structure to a different repo (a library, a dataset, a benchmark, a repo without a teaser), with sizes.
9. `## Do's and Don'ts`.
10. `## Agent Prompt Guide`: three prompts that use only values from the sections above.
11. `## Similar Pages`, `## Quick Start` (a Markdown skeleton in a ```markdown block that reproduces the header block and the section outline with placeholders), `## Provenance` (repo URL, paper and venue, selection reason, evidence used, date).

## Notes from the first file

- When the Quick Start skeleton contains fenced code blocks, fence the skeleton itself with four backticks.
- Colors that are not badges but are used in Components, the Agent Prompt Guide or the Quick Start (diagram legends, colored callouts in images) are listed in a closing paragraph of Badges, so the color check can find them.
