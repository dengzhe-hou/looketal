# Angelina Wang — Style Reference

> A faculty profile card with research themes folded like index cards.

**Theme:** light

Measurements are normalized from the static HTML, its inline `<style>`, `website_files/homepage.css`, and Bootstrap 5.2.2; roles are interpreted. Bootstrap ships many palette colors that this page never shows, so only colors traceable to the markup or the custom stylesheet are listed. Values marked (inferred) are Bootstrap defaults I did not see overridden.

## Overview

A compact Bootstrap page capped at 960px. The header is a two-column row: a 200 to 230px headshot with three small image-icon links (email, Bluesky, Scholar) under it, and to the right a bold 40px name in a muted steel blue (#446787), a three-line affiliation, and a pipe-separated nav to Publications, Teaching, Group and CV. The body is Open Sans prose. Its one distinctive device is a set of `<details>` blocks, one per research theme (AI fairness, Evaluation, Societal impacts), whose collapsed summary lists venue links with tiny pastel pills for "oral", "best paper" and "honorable mention", and whose open state swaps the summary to a plain question. Publications live on a separate page.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Harbor Steel | rgb(68,103,135) = #446787 | `--heading` | Name (h1) and content h3/h4 |
| Bootstrap Blue | #0d6efd (inferred default) | `--link` | Link color from Bootstrap 5.2 |
| Marigold Hover | #ff9a00 | `--link-hover` | `a:hover` and `.activeTitle` |
| Terracotta | #dc6c4e | `--project-strong` | `.proj strong` on project listings |
| Charcoal Ink | #212529 | `--text` | Bootstrap body text |
| Rose Pill | #f8d7da on #721c24 | `--pill-oral` | "oral" pill background and text (6 uses) |
| Mint Pill | #d4edda on #155724 | `--pill-award` | "best paper" and "honorable mention" pills (6 uses) |
| Page White | #ffffff | `--bg` | Background |

## Tokens — Typography

- **Primary:** Open Sans 400, 600, 700 with italics (Google Fonts), fallback `sans-serif`. Substitute: Noto Sans or Source Sans 3.
- **Mono:** Inconsolata appears in Bootstrap overrides but not in visible content.
- **Weights:** 400 body, 700 for h1, h3, h4, `.projTitle`, and strong phrases.

| Level | Element | Size | Notes |
|---|---|---|---|
| Display | `header h1` | 40px | bold, #446787 |
| Section | `#content h3` | 30px | bold, #446787, 20px top / 10px bottom margin |
| Sub-section | `#content h4` | Bootstrap default (inferred 1.5rem) | bold, #446787 |
| Body | `.container` | 16px | line-height 1.5 (Bootstrap) |
| Pill | inline span | 0.85em | padding 2px 6px |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Pill radius | 4px | Inline award and oral pills |
| Bootstrap radius | .375rem | Default component radius (inferred, unused on visible content) |

- **Shadows:** none in custom CSS; Bootstrap focus rings only.
- **Layout max-width:** `.container` forced to 540 / 720 / 960px at the 576 / 768 / 992px breakpoints and kept at 960px above that.
- **Rhythm:** `body { padding-top: 20px }`, `header` 20px top and bottom padding, `.content-block { margin-bottom: 43px }`, `.proj { margin-bottom: 30px }`.

## Components

- **Profile header.** Role: identity. Bootstrap row with `col-md-4` photo column and `col-md-8` text column. Centered on phones, left-aligned from 768px. Social icons are images capped at 31px tall in a flex row with 24px gaps.
- **Name.** Role: h1. 40px bold #446787 Open Sans, followed by `.affil` lines (title, school, office) and a pipe-separated text nav.
- **Theme disclosure.** Role: research theme with evidence. `<details class="fairness|evaluation|impacts">` with a `<summary>` that starts with a bold theme name and a parenthetical list of venue links; a small script rewrites the summary text when it opens.
- **Venue pill.** Role: highlight a distinction next to a venue link. Inline span with `padding: 2px 6px; border-radius: 4px; font-size: 0.85em;` and either rose (#f8d7da / #721c24) for "oral" or mint (#d4edda / #155724) for "best paper" and "honorable mention".
- **Link.** Role: inline links. Bootstrap blue; hover #ff9a00 with pointer cursor.

## Page Modules

- **Title/author block:** photo plus name, affiliation and nav, inside a Bootstrap row.
- **Bio/photo:** headshot up to 230px; paragraph bio with a bold recruiting sentence.
- **Research themes:** three collapsible `<details>` blocks that double as a selected-publications index.
- **Venue badge:** small pastel pills for oral, best paper, honorable mention.
- **Publication list, group, teaching:** separate pages (`pubs.html`, `group.html`, `teaching.html`).
- **Awards:** named in the bio paragraph (NSF GRFP, Rising Stars, Siebel, Microsoft fellowship).
- **Explainers:** short list of linked guides (AI Fairness FAQ, Statistics Primer).
- **Contact:** email icon in the header and a separate contact page.
- **News, BibTeX, teaser media:** not on the home page.

## Do's and Don'ts

- Do color headings in the muted steel blue and keep body text Bootstrap charcoal.
- Do mark distinctions with tiny pastel pills inside the sentence, not as a separate badge row.
- Do use `<details>` to keep the home page short while exposing venue evidence.
- Don't widen past 960px; the custom CSS deliberately overrides Bootstrap's 1140 and 1320px containers.
- Don't use Bootstrap buttons for nav; links are plain text with pipes.
- Don't add more pill colors than rose and mint.

## Surfaces

Flat white page with no cards. The only colored surfaces are the inline pills.

## Imagery

One square-ish headshot and three small brand icons (email, Bluesky, Google Scholar) as raster images.

## Layout

Bootstrap grid inside a 960px container. Header is 4/8 columns from the md breakpoint, stacked and centered below it. The content is a single 12-column block.

## Agent Prompt Guide

**Quick colors:** headings #446787, text #212529, link #0d6efd, hover #ff9a00, oral pill #f8d7da/#721c24, award pill #d4edda/#155724.

1. "Build a profile header in a 960px container: left column a 230px headshot with three 31px icon links below in a flex row (gap 24px); right column a 40px bold Open Sans name in #446787, three affiliation lines, and a text nav 'Publications | Teaching | Group | CV'."
2. "Create a research-theme disclosure using `<details>`: summary shows a bold theme name followed by venue links in parentheses, with inline pills (2px 6px padding, 4px radius, .85em) in rose #f8d7da/#721c24 for 'oral' and mint #d4edda/#155724 for 'best paper'."
3. "Style section headings as 30px bold #446787 with 20px top and 10px bottom margin on a white page with Open Sans 16px body."

## Similar Pages

- [Dora Zhao](https://dorazhao99.github.io/), same Princeton Visual AI lineage, for a soft HCI-flavored page.
- [Florian Tramèr](https://www.floriantramer.com/) for another Bootstrap 5 faculty page.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #212529;
  --heading: #446787;
  --link: #0d6efd;
  --link-hover: #ff9a00;
  --project-strong: #dc6c4e;
  --pill-oral-bg: #f8d7da;  --pill-oral-fg: #721c24;
  --pill-award-bg: #d4edda; --pill-award-fg: #155724;
  --radius-pill: 4px;
  --font: 'Open Sans', sans-serif;
  --content-max: 960px;
}
body { padding-top: 20px; font-family: var(--font); color: var(--text); background: var(--bg); }
.container { max-width: var(--content-max); font-size: 16px; }
header h1, #content h3, #content h4 { color: var(--heading); font-weight: bold; }
header h1 { font-size: 40px; }  #content h3 { font-size: 30px; margin: 20px 0 10px; }
a:hover { color: var(--link-hover); }
.pill { padding: 2px 6px; border-radius: var(--radius-pill); font-size: .85em; }
```

## Provenance

- **URL:** https://angelina-wang.infosci.cornell.edu/ (angelina-wang.github.io redirects here)
- **Venue/award:** ACL 2025 Best Paper (first author of "Fairness through Difference Awareness"), per https://2025.aclweb.org/program/awards/
- **Selection reason:** Rule B.
- **Template credit:** none stated; Bootstrap 5.2.2 with a custom `homepage.css`.
- **Measurement method:** values read from `homepage.css`, the inline style block and inline `style` attributes via `extract_style.py` and curl. Most Bootstrap palette colors in the frequency table (success green, danger red, and so on) are framework defaults and are not used on the page. Not rendered in a browser for this note.
