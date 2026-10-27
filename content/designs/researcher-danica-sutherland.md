# Danica J. Sutherland — Style Reference

> A typeset CV left open on a seminar-room table.

**Theme:** light

Measurements are normalized from the static HTML and the single stylesheet (`style.css`); roles are interpreted from how each rule is used in the markup. Values marked (inferred) come from browser defaults rather than an explicit rule.

## Overview

A single, narrow, hand-written page with no framework and no web fonts. The whole site is one column of 43em in Palatino at 14px, opened by a centered name with a 2px black rule under it, followed by centered affiliation lines and a pink notice box about student recruiting. Everything else is lists: group members in a flex grid, courses, then a long grouped publication list (85 entries) and an invited-talks list (44 entries). The one piece of interaction is a floated "coauthors" box whose rounded pills filter the publication list with jQuery. Color is almost entirely classic hyperlink blue and red, plus an orange tint that marks the author's own students.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Hyperlink Blue | `blue` (#0000ff) | `--link` | Default link color sitewide (`a, a:visited`) |
| Ink Navy | #0000aa | `--paper-link` | Links inside `.paper` and `.talk`; coauthor pill border and active fill |
| Alarm Red | `red` (#ff0000) | `--link-hover` | Hover color for all links, with underline |
| Student Amber | rgb(200,100,0) = #c86400 | `--student` | Names of the author's own students in author lists |
| Equal-Contribution Brick | #cc3333 | `--equal` | Equal-contribution markers |
| Notice Blush | #ffd3d3 | `--alert-bg` | Background of the recruiting notice (`#alert`) |
| Anchor Cream | #ffffdd | `--target-bg` | Background of a paper or talk when it is the URL `:target` |
| Typewriter Grey | #444444 | `--mono-ink` | Obfuscated email addresses |
| Rule Black | black (#000000) | `--rule` | 2px rule under the h1; 1px border of the coauthor box |
| Paper White | #ffffff (inferred) | `--bg` | Page background (browser default; coauthor box sets `white` explicitly) |

## Tokens — Typography

- **Body:** `Palatino, Helvetica, Arial, sans-serif` at 14px. Substitute: Palatino Linotype, TeX Gyre Pagella, or URW P052.
- **Mono:** `Consolas, "Liberation Mono", Courier, monospace` for `.eml` and `.code`.
- **Weights:** only normal and the browser bold for headings; the pronoun span is set back to normal weight.
- **Italic:** paper titles (`.title`) and notes (`.note`) are italic; `.title .meta` returns to roman.

| Level | Element | Size | Notes |
|---|---|---|---|
| Display | h1 | 2em (inferred) | Centered, `border-bottom: 2px solid black` |
| Pronoun | `#pronouns` | `medium` | Normal weight, wrapped in parentheses via `::before/::after` |
| Section | h3 | 1.17em (inferred) | Group, Courses, Publications, Invited talks |
| Sub-section | h4 | 1em (inferred) | Publication groups (Preprints, Journal and Conference, ...) |
| Body | p, li | 14px | `li` has 5px bottom margin |
| Affiliation | `.group-members .affil` | 90% | max-width 18em |
| Info lines | `p.info` | 14px | Centered, line-height 130% |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| Pill radius | 7px | Coauthor filter items |
| Square | 0 | Everything else, including the alert box |

- **Shadows:** none.
- **Layout max-width:** `#content { max-width: 43em; width: 90%; margin: 5em auto; }`.
- **Rhythm:** `.paper, .talk { margin-top: 1em; padding: 5px; }`; group members `flex-basis: 19em; margin: 5px`.

## Components

- **Name header.** Role: page identity. `h1` centered with a 2px solid black bottom border; pronouns shown inline at `medium` size (block below 500px).
- **Info lines.** Role: affiliations, email, profile links. `p.info` centered, `margin-top: -10px; margin-bottom: 20px; line-height: 130%`; items inside `.bio-links` are inline-blocks separated by 0.4em side margins; `.spacer` adds 0.5em gaps.
- **Recruiting notice.** Role: one-line advice to applicants. `#alert` with `background-color: #ffd3d3`, 10px horizontal padding, 10px top padding on the first paragraph and bottom on the last. No border, no radius.
- **Paper entry.** Role: one publication. `div.paper` shown as `display: list-item; list-style-type: square`; children are block spans: italic `.title`, `.authors` (students in #c86400), `.venue`, optional italic `.note`, then `.links` right-aligned as bracketed text links `[arXiv] [code] [video]` in #0000aa.
- **Coauthor filter.** Role: filter the publication list by collaborator. Floated right, `border: 1px solid black; background: white; margin: 10px; padding: 5px`; each `li` is a centered pill with `border: 1px solid #00a; border-radius: 7px; padding: 2px`; active pills invert to white text on #0000aa.
- **Deep-link highlight.** Role: show which entry a shared link points to. `.paper:target, .talk:target { background-color: #ffd; }`.

## Page Modules

- **Title/author block:** centered h1 with name and pronouns, then three centered info lines (position, groups, contact). No photo; an `img#me` rule (float right, 220px tall) exists but the image tag is commented out.
- **Venue badge:** none. Venues are plain text in `.venue` blocks.
- **Link buttons:** bracketed text links on the right of each entry (`[arXiv]`, code, video, slides); no button styling.
- **Bio/photo:** text-only bio through the info lines; no photo.
- **Group:** flex-wrapped list of students and postdocs with small affiliation notes.
- **Courses:** plain list section.
- **Publication list:** grouped by type with h4 subheads, square bullets, no thumbnails, filterable by coauthor.
- **Talks:** same entry style as papers, with YouTube video links.
- **News, awards, BibTeX, teaser media:** not present on the page.
- **Contact:** obfuscated email in Consolas inside the info lines.

## Do's and Don'ts

- Do keep the column at 43em and the body at 14px Palatino; the density is the look.
- Do use pure link blue for navigation links and the darker #0000aa inside publication entries.
- Do mark the author's students with the amber tint rather than bold.
- Don't add cards, shadows, or rounded corners beyond the 7px coauthor pills.
- Don't add thumbnails; entries are text only.
- Don't center body paragraphs; only the header block is centered.

## Surfaces

One flat white surface. The only tinted surfaces are the blush recruiting box and the cream `:target` highlight. The coauthor box is the one bordered surface.

## Imagery

None on the page. No logos, icons, or thumbnails.

## Layout

Single centered column (43em max, 90% width) with 5em top and bottom margin. The coauthor box floats right inside the publications section and the list flows around it. Below 500px the pronouns drop to their own line; nothing else changes.

## Agent Prompt Guide

**Quick colors:** link `blue`, hover `red`, entry links #0000aa, students #c86400, notice #ffd3d3, target #ffffdd, rule black.

1. "Build a publication entry: a square-bulleted block with an italic title line, an author line where the owner's students are colored #c86400, a venue line, and right-aligned bracketed links `[arXiv] [code]` in #0000aa that turn red and underlined on hover. Palatino 14px, 5px padding, 1em top margin."
2. "Create a recruiting notice: full-width box with background #ffd3d3, 10px padding, no border or radius, plain Palatino text with a bold key phrase."
3. "Make a coauthor filter: a box floated right with 1px black border and white background; inside, a vertical list of centered pills with 1px #00a border and 7px radius that toggle to white on #00a when active."

## Similar Pages

- [Daniel Roy](https://danroy.org/) for another hand-made text-heavy theory page.
- [Kenji Kawaguchi](https://people.csail.mit.edu/kawaguch/) for a framework-free publication list.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #000000;
  --link: blue;
  --link-hover: red;
  --paper-link: #0000aa;
  --student: #c86400;
  --equal: #cc3333;
  --alert-bg: #ffd3d3;
  --target-bg: #ffffdd;
  --mono-ink: #444444;
  --font-body: Palatino, "Palatino Linotype", Helvetica, Arial, sans-serif;
  --font-mono: Consolas, "Liberation Mono", Courier, monospace;
  --radius-pill: 7px;
  --content-max: 43em;
}
body { font: 14px/normal var(--font-body); background: var(--bg); }
#content { max-width: var(--content-max); width: 90%; margin: 5em auto; }
h1 { text-align: center; border-bottom: 2px solid var(--text); }
a { color: var(--link); text-decoration: none; }
a:hover { color: var(--link-hover); text-decoration: underline; }
```

## Provenance

- **URL:** https://djsutherland.ml/
- **Venue/award:** ICLR 2025 Outstanding Paper (last author of "Learning Dynamics of LLM Finetuning"), per https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- **Selection reason:** Rule B; homepage taken from her GitHub profile link.
- **Template credit:** none; hand-written HTML and CSS with jQuery 3.6.0 slim for the coauthor filter.
- **Measurement method:** colors, sizes, radius and widths read from `style.css` and the static HTML via `extract_style.py` and curl. The page was not viewed in a browser, so heading sizes and the page background are browser defaults marked (inferred).
