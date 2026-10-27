# Warm Carbon Terminal — Style Reference

> A late-night shell session: warm charcoal, one monospace at 13px, steel-blue links, copper numerals and a slow drift of particles behind everything.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), the 1440×900 and full-page screenshots, and the site's `warm-carbon.css`, `publications-native.css` and `tidal-background.css` read directly. The only web font that loads is IBM Plex Mono 400; every size and colour below comes from it at weight 400 (there is no bold anywhere). Two full-width `<canvas>` layers draw a faint animated particle field; the static capture shows it as scattered grey specks.

## Overview

A warm near-black #181715 page with everything set in IBM Plex Mono, mostly between 10px and 15px. A 1160px shell holds a 58px header (copper "~/" prompt before the "Tim Rocktäschel" wordmark on the left, 11px muted nav on the right with the current page underlined in copper), a topics strip ("Open-Endedness / Recursive Self-Improvement") with 10px "Scholar↗ Twitter↗ GitHub↗ LinkedIn↗" links, then numbered sections ("01 Short Bio", "02 Publications") divided by 1px #36322c rules. The bio puts a desaturated 180px square portrait next to a 12px paragraph at 1.9 line height, its steel-blue #a8bdcd links underlined with hairline borders. Publications are a searchable, year-grouped list of 127 entries: a search field and year select in #201e1b boxes with #665d50 borders, copper "▾ 2026" year summaries with a muted count, and entries with a 13px #d1ccc3 title, 11px muted authors, an 11px copper venue line, and "N citations  + BibTeX" links that expand a bordered BibTeX block.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): charcoal #181715 67.6% plus near-identical #1d1c19 13.1%, #161513 4.5%, #191715 3.7%, #181714 2.2%; mid grey #5c5956 7.7% (anti-aliased text, the portrait and particles). Accent colours are too thin to form clusters.

Anatomy in DOM order (desktop 1440px; shell 1160px at x=140 with 44px side padding, content 1072px at x=184):

1. **Particle canvases** (absolute, full width, 960px tall each, behind content): grey specks, masked to fade at their top and bottom.
2. **Wordmark** (`a.wordmark`, y=16): 15px, letter-spacing -0.375px, #d1ccc3, preceded by "~/" 12px #c6a081 with a 9px gap.
3. **Nav** (right, y=14): Home (current: #a8bdcd, copper underline 6px below), Publications, CV, Blog in 11px #aaa194, 25px apart. Header bottom rule 1px #36322c at y=58. Gap 21px.
4. **Topics** (`.topics`, y=79): 11px #d1ccc3, items separated by a #aaa194 "/" with 17px spacing. Gap 8px.
5. **Hero links** (y=106): 10px #a8bdcd with a small "↗" stroke icon, 21px apart. Strip bottom rule at y=155. Gap 26px.
6. **Section label** (y=181): "01" 10px #c6a081, 15px gap, "Short Bio" 14px #d1ccc3. Gap 18px.
7. **Portrait** (`img.portrait`, y=222, 180×180): radius 2px, `filter: saturate(.35)`. 30px column gap.
8. **Bio** (`.bio-copy`, x=394, y=222): 12px / 22.8px (1.9), #d1ccc3, links #a8bdcd with 1px #36322c bottom borders. Section rule at y=455. Gap 26px.
9. **Publications label** (y=481) with right-aligned 10px "Google Scholar↗ dblp↗ Semantic Scholar↗". Gap 14px.
10. **Tools row** (y=523): "127 publications" 11px #aaa194 left; "Download BibTeX" 11px #a8bdcd right. Then search and year controls (44px tall) and the first "▾ 2026  8 publications" summary at y=663, then entries from y=700; the fold falls on the second entry.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Carbon | #181715 | `--bg` | page background, skip link |
| Surface | #201e1b | `--surface` | search input, year select, BibTeX `pre`, inline code |
| Ink | #d1ccc3 | `--ink` | wordmark, headings, bio, publication titles, topics |
| Muted | #aaa194 | `--muted` | nav links, counts, authors, labels, placeholders, footer, "/" separators |
| Line | #36322c | `--line` | header and section rules, entry dividers, bio link underlines, `pre` border, footer rule |
| Steel Blue | #a8bdcd | `--accent` | links, current nav item, "+ BibTeX" toggle, title hover |
| Copper | #c6a081 | `--warm` | "~/" prompt, section numbers, year summaries, venue lines, current-nav underline, link hover, focus ring, selection |
| Control Border | #665d50 | (literal) | 1px border of search, select and buttons |
| Code Sage | #b2bd9a | (literal) | strings in highlighted code (blog posts) |
| Code Lilac | #c1a9c7 | (literal) | numbers in highlighted code |
| Code Rose | #d8a5a0 | (literal) | errors / deletions in highlighted code |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Mono (everything) | 'IBM Plex Mono', 'SFMono-Regular', Consolas, monospace | IBM Plex Mono 400 (self-hosted woff2) | JetBrains Mono |

| Role | Selector | Size / line-height | Color |
|---|---|---|---|
| Base | `body` | 13px / 1.7 (22.1px) | #d1ccc3 |
| Wordmark | `.wordmark` | 15px, letter-spacing -0.025em | #d1ccc3; "~/" 12px #c6a081 |
| Nav | `.site-header nav` | 11px | #aaa194; current #a8bdcd |
| Topics | `.topics` | 11px / 1.7 | #d1ccc3 |
| Hero / scholar links | `.hero-links`, `.scholar-links` | 10px | #a8bdcd |
| Section number | `.section-number` | 10px | #c6a081 |
| Section title | `.section-label h2` | 14px / 23.8px | #d1ccc3 |
| Bio | `.bio-copy` | 12px / 1.9 | #d1ccc3 |
| Year summary | `.publication-year-label` | 13px; count 10px | #c6a081; count #aaa194 |
| Publication title | `.publication-title` | 13px / 1.75 | #d1ccc3; hover #a8bdcd underlined |
| Authors | `.publication-authors` | 11px / 1.8 | #aaa194 |
| Venue | `.publication-venue` | 11px / 1.8 | #c6a081 |
| Entry links | `.publication-links` | 11px | #a8bdcd; "+" #c6a081 |
| BibTeX | `.publication-bibtex pre` | 12px / 1.8 | #d1ccc3 |
| Footer | `.site-footer` | 9px / 1.8 | #aaa194 |

All weights are 400; hierarchy comes only from size and colour.

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 2px | none | none |
| Search / select / buttons | 3px | 1px solid #665d50; hover #c6a081 | none |
| BibTeX `pre` | 0 | 1px solid #36322c | none |
| Year summary | 0 | 1px #36322c top and bottom | none |
| Entry | 0 | 1px #36322c bottom | none |
| Header / sections / footer | 0 | 1px #36322c rules | none |
| Focus ring | 0 | 2px solid #c6a081, offset 3–4px | none |

## Layout Metrics

- **Shell**: `.site-header, .page-shell, .site-footer { max-width: 1160px; margin: 0 auto; padding: 0 44px }`; content 1072px.
- **Header**: flex, space-between, min-height 58px, 1px bottom rule; nav gap 4px 25px.
- **Intro strip**: padding 21px 0 22px, bottom rule; topics gap 5px 17px; hero links margin-top 8px, gap 4px 21px.
- **Sections**: padding 26px 0 with a bottom rule; label margin-bottom 18px (gap 15px between number and title).
- **Bio grid**: `180px minmax(0, 1fr)`, gap 30px.
- **Publications**: tools row margin-bottom 13px; filters gap 12px, margin-bottom 22px (search flex 1 1 280px, year 0 1 145px); controls min-height 44px, padding 9px 11px; year group margin-bottom 18px, summary padding 9px 0; entries padding 15px 0 14px; title margin 0 0 5px; links gap 3px 17px, margin-top 4px.
- **Footer**: padding 18px 44px 22px, top rule, "Pause background" text button on the right.
- **Page height**: about 18,800px with all 127 entries expanded by year.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >850px | (100% − 1160px)/2 + 44px | 13px (bio 12px) | 15px wordmark, 14px section titles | bio grid 180px + text, gap 30px |
| 561–850px | 28px | 13px | same | nav gap 18px; bio gap 25px; publication heading stacks its links under the label |
| ≤560px | 20px | 13px; small text raised to 12px | same | header wraps (nav full width, 12px); bio stacks; search full width; tap targets 32–44px; footer stacks |

## Components

- **Prompt wordmark**: `::before` "~/" in 12px #c6a081 with a 9px right margin, then the name in 15px #d1ccc3.
- **Current nav item**: #a8bdcd with a #c6a081 underline offset 6px; other items #aaa194.
- **Numbered section label**: 10px copper number, 15px gap, 14px ink title, baseline aligned.
- **External link**: 10–11px #a8bdcd followed by a 0.75em stroked arrow icon (1.5 stroke); hover #c6a081 with an underline offset 3px.
- **Bio link**: #a8bdcd text with a 1px #36322c bottom border instead of an underline.
- **Search and select**: #201e1b fill, 1px #665d50 border, 3px radius, 44px tall, padding 9px 11px, muted placeholder "Titles, authors, venues"; label above in 11px #aaa194.
- **Year group**: native `<details>` whose summary is a copper "▾ 2026" (10px marker) with a 10px muted count, ruled above and below in #36322c.
- **Publication entry**: 13px ink title link; 11px muted authors separated by semicolons; 11px copper venue; a links row with muted "N citations" and a "+ BibTeX" summary (copper "+" that turns into "−") that opens a 12px `pre` on #201e1b with a 1px #36322c border and 13px padding.
- **Particle background**: two absolutely positioned canvases inside `.tidal-page-field` (z-index -3), masked with a vertical gradient so the specks fade near their edges; a "Pause background" button in the footer stops the animation.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Header / nav | yes | prompt wordmark, 11px nav |
| Research topics | yes | slash-separated 11px strip |
| Social links | yes | 10px external links with arrows |
| Portrait | yes | 180px, desaturated, 2px radius |
| Bio | yes | 12px mono paragraph with underlined-by-border links |
| Publications | yes | search, year filter, collapsible year groups, BibTeX toggles |
| Awards | present but non-standard | mentioned inline in the bio ("two Best Paper Awards at ICML 2024") |
| News | absent from the source | none on the home page |
| Animated background | yes | particle canvases with a pause control |
| Footer | yes | 9px muted credit line with the template credit |

## Adapting to Other Content

- **News**: use the blog-list pattern already in the stylesheet: a grid of 120px muted 11px dates and 15px #a8bdcd titles, rows padded 18px with #36322c rules.
- **More sections**: continue the numbering ("03 Students", "04 Talks") with copper 10px numbers.
- **Results tables**: the page-content table style: 1px #36322c cell borders, 8px padding, header cells in #c6a081 at weight 400.
- **Awards**: a copper 11px line under the venue, never a badge or bold.
- **Light mode**: none in the source; keep the dark palette.

## Do's and Don'ts

- Do set everything in one monospace at weight 400 and build hierarchy from size (9–15px) and colour.
- Do keep the two accents distinct: steel blue #a8bdcd for things you click, copper #c6a081 for structure (numbers, years, venues, focus).
- Do divide sections with 1px #36322c rules instead of boxes.
- Don't use pure black or white; the ground is #181715 and text #d1ccc3.
- Don't add bold or large display type; the largest text is the 15px wordmark.
- Don't let the particle field compete with text; it stays a faint grey drift.

## Surfaces

Carbon #181715 page; #201e1b for inputs and code blocks; nothing else is filled. The particle canvases sit beneath the content.

## Imagery

One desaturated portrait (saturation 35%) on a white wall. No figures or thumbnails; the animated particle field is the only other visual.

## Layout

Header; topics and social links strip; 01 Short Bio (portrait and paragraph); 02 Publications (tools, filters, year groups); footer. About 18,800px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #181715, surface #201e1b, ink #d1ccc3, muted #aaa194, rule #36322c, link #a8bdcd, copper #c6a081, control border #665d50.

1. "Build a 1160px shell with 44px padding on #181715, everything in IBM Plex Mono 400 at 13px/1.7, text #d1ccc3. Header 58px tall with a 1px #36322c bottom rule: left a 15px wordmark preceded by a 12px #c6a081 '~/', right an 11px #aaa194 nav 25px apart, the current item #a8bdcd with a #c6a081 underline offset 6px."
2. "Make numbered sections: label row with a 10px #c6a081 number, 15px gap, 14px #d1ccc3 title, 18px below; sections padded 26px 0 with 1px #36322c rules. Bio grid 180px + 1fr, 30px gap: a 180px portrait with 2px radius and saturate(.35), and 12px/1.9 text whose #a8bdcd links have 1px #36322c bottom borders."
3. "Make a publication list: an #201e1b search input and year select, 44px tall, 1px #665d50 border, 3px radius; year groups as details summaries in #c6a081 13px with a 10px #aaa194 count, ruled top and bottom in #36322c; entries padded 15px 0 14px with a bottom rule: 13px #d1ccc3 title, 11px #aaa194 authors, 11px #c6a081 venue, 11px links with a '+ BibTeX' toggle opening a 12px pre on #201e1b with a 1px #36322c border."

## Similar Pages

- Terminal-styled researcher pages with monospace type and prompt glyphs.
- Personal sites with generative particle or flow-field backgrounds.

## Quick Start

```css
:root {
  color-scheme: dark;
  --bg: #181715;
  --surface: #201e1b;
  --ink: #d1ccc3;
  --muted: #aaa194;
  --line: #36322c;
  --accent: #a8bdcd;
  --warm: #c6a081;
  --mono: 'IBM Plex Mono', 'SFMono-Regular', Consolas, monospace;
}
body { margin: 0; background: var(--bg); color: var(--ink); font: 13px/1.7 var(--mono); }
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--warm); text-decoration: underline; text-underline-offset: 3px; }
.page-shell { max-width: 1160px; margin: 0 auto; padding: 0 44px; }
.wordmark::before { content: '~/'; margin-right: 9px; color: var(--warm); font-size: 12px; }
.section-number { color: var(--warm); font-size: 10px; }
.publication-entry { padding: 15px 0 14px; border-bottom: 1px solid var(--line); }
input, select { background: var(--surface); border: 1px solid #665d50; border-radius: 3px; min-height: 44px; padding: 9px 11px; color: var(--ink); }
```

## Provenance

- **URL**: https://rockt.ai/
- **Person**: Tim Rocktäschel, open-endedness and reinforcement learning.
- **Award**: ICML 2024 Best Paper, "Genie: Generative Interactive Environments" (last author). https://icml.cc/virtual/2024/awards_detail
- **Selection reason**: rule B (last author); chosen for the consistent dark monospace terminal aesthetic with searchable, year-grouped publications and accent colours.
- **Template credit**: the footer reads "HTML5 · Original design: TEMPLATED"; the current theme files are named warm-carbon and tidal and have moved far from that template.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `warm-carbon.css`, `publications-native.css` and `tidal-background.css` read directly, on 2026-10-28.
