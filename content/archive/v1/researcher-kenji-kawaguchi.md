# Kenji Kawaguchi — Style Reference

> A department web directory page from before stylesheets had opinions.

**Theme:** light

Measurements are normalized from the static HTML and its single inline `<style>` block; roles are interpreted. Almost every color here is a browser default, so most values are marked (inferred).

## Overview

A raw HTML page hosted on MIT CSAIL people space. One inline style block sets Helvetica 16px, a 1100px wrapper with a 30px margin, and a floated headshot. Everything else is browser default: blue underlined links (some with `text-decoration: none` inline), `<hr>` rules between sections, `<font size="5">` for the institution line. The page reads as a stack: photo floated left beside the name, institution and center, a rule, a recruiting sentence, a rule, then a long "Selected Publications" list split into Conference Papers, Journal Articles, Book Chapter and Technical Reports. Each entry is a paragraph with the author list (own name in bold, asterisks for equal contribution), the title, the venue and year, then bracketed `[pdf] [BibTeX]` links and an italic bold award note such as "Selected for ICLR Spotlight (5% accept rate)". Later sections cover service, invited talks, education and positions, and code.

Note that this page is stale. It still says "Harvard University" in the title and announces an NUS appointment "from Fall 2021"; the most recent entries are 2021 papers.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Default Link Blue | #0000ee (inferred) | `--link` | Browser default link color |
| Visited Purple | #551a8b (inferred) | `--link-visited` | Browser default visited link |
| Plain Black | #000000 (inferred) | `--text` | Body text |
| Paper White | #ffffff (inferred) | `--bg` | Page background |
| Utility Blue | `blue` (#0000ff) | `--blue-text` | `.blue-text` helper class |
| Rule Grey | browser `<hr>` (inferred) | `--rule` | Section separators |

## Tokens — Typography

- **Primary:** `Helvetica, arial, sans-serif` at 16px. Substitute: Arial or Nimbus Sans.
- **Weights:** normal and bold; bold marks the owner's name and award notes.
- **Helpers:** `.small` 12px, `.large` 20px (defined, sparsely used).

| Level | Element | Size | Notes |
|---|---|---|---|
| Name | h1 | 2em (inferred) | preceded by three empty italic lines for vertical offset |
| Institution | `<font size="5">` bold | 24px (inferred) | linked, no underline |
| Center | `<font size="+1">` | about 18px (inferred) | linked, no underline |
| Section | h2 | 1.5em (inferred) | Selected Publications, Service, Talks, Education, Code |
| Sub-section | h3 | 1.17em (inferred) | Conference Papers, Journal Articles, with `margin-top: 2em` inline |
| Body | p | 16px | |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Square | 0 | everything |

- **Shadows:** none.
- **Layout max-width:** inline `<div style="margin: 30px; max-width: 1100px;">` (left-aligned, not centered).
- **Image:** `img { max-width: 100%; margin-bottom: 30px; }`; `.headshot { float: left; margin-right: 30px; }`, unfloated under 700px.

## Components

- **Header block.** Role: identity. Floated headshot, then the h1 name, a bold linked institution line at font size 5, and a linked center line at +1; cleared by an `<hr style="clear: both;">`.
- **Recruiting line.** Role: open positions. Plain sentence between two rules.
- **Publication paragraph.** Role: one paper. Authors (own name `<b>`, `*` equal contribution), title, venue sentence, line break, `[pdf] [BibTeX]` where BibTeX links to a separate `bibtexNN.html` page, optional `<i><b>` award or spotlight note.
- **Section heading.** Role: page sections. Browser-default h2 and h3.

## Page Modules

- **Title/author block:** floated photo with name and affiliation lines.
- **Bio/photo:** headshot only; bio limited to the recruiting sentence.
- **Publication list:** grouped by type, text only, no thumbnails.
- **Link buttons:** bracketed text links `[pdf] [BibTeX]`.
- **BibTeX block:** each entry links to its own BibTeX HTML page rather than an inline block.
- **Awards:** inline italic bold notes under entries.
- **Talks, service, education, code:** plain sections near the bottom.
- **News, venue badges, teaser media, contact form:** not present.

## Do's and Don'ts

- Do keep it to one inline style block and browser defaults; that is the whole aesthetic.
- Do mark the owner's name in bold and equal contribution with asterisks.
- Do put the award or spotlight note in bold italic right after the links.
- Don't center the wrapper; the original hugs the left margin at 30px.
- Don't restyle links beyond removing underlines on the header links.
- Don't treat the content as current; it reflects 2021.

## Surfaces

None beyond the white page and `<hr>` rules.

## Imagery

One headshot (`image/kenji.jpg`). No other images.

## Layout

Left-aligned block, 1100px max with 30px margin. The headshot floats left on desktop and becomes a block above the name under 700px.

## Agent Prompt Guide

**Quick colors:** browser defaults only: text #000000, link #0000ee, visited #551a8b, background #ffffff (all inferred).

1. "Build a plain academic header: a headshot floated left with 30px right margin, then an h1 name, a bold 24px linked university line with no underline, an 18px linked center line, and a full-width `<hr>` that clears the float. Helvetica 16px, no other styling."
2. "Create a publication paragraph: author list with the owner's name bold and asterisks for equal contribution, the title, the venue and year, a line break, then `[pdf] [BibTeX]` text links and a bold italic note like 'Selected for ICLR Spotlight (5% accept rate)'."
3. "Group publications under default h3 subheads (Conference Papers, Journal Articles, Book Chapter, Technical Reports) with 2em top margin."

## Similar Pages

- [Zekun Shi](https://zekun-shi.github.io/), his student in this batch.
- [Danica J. Sutherland](https://djsutherland.ml/) for another text-only theory page with more structure.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --link: #0000ee;
  --font: Helvetica, Arial, sans-serif;
  --content-max: 1100px;
}
body { font: 16px var(--font); color: var(--text); background: var(--bg); }
.page { margin: 30px; max-width: var(--content-max); }
img { max-width: 100%; margin-bottom: 30px; }
.headshot { float: left; margin-right: 30px; }
@media (max-width: 700px) { .headshot { float: none; display: block; margin: 0 0 30px 0; } }
.small { font-size: 12px; } .large { font-size: 20px; }
```

## Provenance

- **URL:** https://people.csail.mit.edu/kawaguch/
- **Venue/award:** NeurIPS 2024 Best Paper (last author of "Stochastic Taylor Derivative Estimator"), per https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/ (authors from arXiv 2412.00088)
- **Selection reason:** Rule B.
- **Template credit:** none; hand-written HTML.
- **Measurement method:** the inline style block and markup were read with `extract_style.py` and curl. The extractor found no colors because none are declared; color and heading sizes are browser defaults, marked (inferred). Not rendered in a browser. The page content is outdated (title says Harvard, mentions an NUS appointment starting Fall 2021); a newer page at ml.comp.nus.edu.sg/kawaguchi is linked from his student's site but was not measured here.
