# Marker and Olive Ledger — Style Reference

> A name scrawled in red marker on the door of a crowded statistics office, with the reading list pinned up in olive ink.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes and DOM dumps of the dark column and publication blocks, the 1440×900 and full-page screenshots, and `styles/screen.css` plus the inline `<style>` block read directly. Permanent Marker 400, Open Sans 700 and Lato 400 / 900 load from Google Fonts. The name is declared 60pt (80px) at `h1` weight 700, so its heavier strokes are a synthesized bold of the single 400 face. This v2 file replaces a v1 entry built from CSS alone.

## Overview

A hand-coded, absolutely positioned page on light grey #f2f2f2, max 1400px wide and never narrower than 968px. Top left, a dark #333333 block with a 30px bottom-right corner holds a smiling portrait filling its full 257px width and a "CONTACT" heading in #eeeeee with silver email and Twitter lines. To its right, starting at 20% of the width, "Dan Roy" in red #a21919 Permanent Marker at 80px, then 21px Lato lines: "CIFAR Canada AI Chair and Founding Faculty, Vector Institute", "Professor", indented department links, "Editorial Boards", and a note about joining Google DeepMind. Below sit two columns: a 28% justified, hyphenated column (Research, Group Members, Group Alumni, Probabilistic Programming) and a 48% column (Preprints and Working Papers, Thesis, Research Articles), both headed by 28px Open Sans bold uppercase titles in #333333. Every paper title is a bold 17.3px underlined olive #666600 link, followed by authors, an italic venue, and an underlined olive arXiv or DOI link; honours such as "Spotlight" are bold black and the thesis award is in the same red as the name.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): light grey #f2f2f2 68.2% plus #f5f5f6 4.6%, #f2f2f1 2.4%, #f2f2f3 2.0%; warm greys #d0cfc6 11.9% and #726157 9.7% (the portrait, the dark column and anti-aliased text). The red name, olive links and the #333333 column edge are too thin to form their own clusters.

Anatomy in DOM order (desktop 1440px; `.html` container 1400px at x=0):

1. **Name** (`h1.nameheader`, x=280, y=0): Permanent Marker 80px (60pt) / 700 synthesized / 112px, #a21919, left. Gap 0 (the next line has a -4px margin).
2. **Chair line** (`p.pos`, y=108): Lato 21px / 400 / 23.1px, #444444; "CIFAR Canada AI Chair" bold olive #666600 link, "Founding Faculty" bold #444444, "Vector Institute" olive link. Gap 8px.
3. **Professor** (y=139): 21px / 700, #444444. Gap 8px.
4. **Departments** (y=170–299, indented 42px): olive 21px links on separate lines with "(cross-appointment)" at 17.5px #444444; a second group 12px below. Gap 12px.
5. **Editorial Boards** (y=312) and "Action Editor, Journal of Machine Learning Research" (y=343, indented 42px). Gap 48px.
6. **Announcement** (y=414): 21px #444444 across 1120px with "Google DeepMind" and "Visiting Researcher" in bold. Gap 36px.
7. **Dark column** (`.recede`, absolute at x=0, y=0, 257×516): portrait 257×308 flush to the top-left; "CONTACT" in Open Sans 22px / 700 #eeeeee; `p.info` lines in #c0c0c0 with bold #808080 labels ("email:", "social media:") and the @roydanroy link in olive.
8. **Column headings** (y=512): "RESEARCH" at x=295 and "PREPRINTS AND WORKING PAPERS" at x=715, Open Sans 28px / 700, uppercase, #333333.
9. **Columns** (from y=566): research paragraphs 16px Lato justified (the 28% column renders blank in the 1440×900 capture, apparently before the hyphenation script finishes, and appears in the full-page capture); paper entries in the 48% column with 17.3px bold olive titles.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Workshop Grey | #f2f2f2 | `body` inline style | page background |
| Brick Marker | #a21919 | `.nameheader`, inline span | name; thesis award line |
| Olive Ink | #666600 | `a:link`, `.paper` | all links, paper titles, arXiv / DOI links, affiliation links |
| Olive Glow | #888800 | `a:hover` | link hover |
| Text Ink | #222222 | `body` | body text, authors, venues |
| Position Grey | #444444 | `.pos` | header lines (chair, professor, departments, announcement) |
| Charcoal | #333333 | `.recede`, `.bigheader` | dark column background; section headings |
| Contact White | #eeeeee | contact `h3.bigheader` in `.recede` | "CONTACT" heading on the dark column |
| Silver | #c0c0c0 | `p.info` | contact details on the dark column |
| Label Grey | #808080 | `.info b` | "email:", "social media:" labels |
| Alumni Grey | #555555 | inline `color` | alumni career-path notes |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Marker | 'Permanent Marker', serif | Permanent Marker 400 (700 synthesized on the `h1`) | Rock Salt |
| Text | 'Lato', sans-serif | Lato 400, 900 (700 requests map to 900) | Carlito |
| Headings | 'Open Sans', Helvetica, Arial, sans-serif | Open Sans 700 | Open Sans |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.nameheader` | 60pt = 80px / 700 / 112px | #a21919 |
| Position lines | `.pos` | 21px / 400 / 1.1em (23.1px); bold phrases 700 | #444444, links #666600 |
| Section heading | `h3.bigheader` | 28px / 700 / 39.2px, uppercase, text-indent -11px | #333333 |
| Contact heading | `.recede h3.bigheader` | 22px / 700, uppercase | #eeeeee |
| Body | `body` | 12pt = 16px / 400 / 1.4 (22.4px) | #222222 |
| Research text | `p.hyphenate.text` | 16px / 400 / 22.4px, justified, hyphenated | #222222 |
| Paper title | `a.paper` | 13pt = 17.33px / 700 / 24.3px, underlined | #666600 |
| Venue | `em` | 16px / 400 italic | #222222 |
| arXiv / DOI link | `a.plink` | 16px / 300 (renders as Lato 400), underlined | #666600 |
| Contact lines | `p.info` | 16px / 400; labels 700 | #c0c0c0, labels #808080 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Dark column | 0 0 30px 0 (bottom-right only) | none | none |
| Portrait | 0 | none | none |
| Links | 0 | text underline (default) | none |
| Everything else | 0 | none | none |

## Layout Metrics

- **Container**: `.html { max-width: 1400px; position: relative }`; `body { min-width: 968px }` with no margin, so the page starts at x=0 and scrolls horizontally below 968px.
- **Header block** (`#box1-4`): `padding-left: 20%` (280px at 1400) and 520px tall; `.pos` lines indented 42px for sub-items.
- **Dark column** (`#box2-4` / `.recede`): absolute, `width: 18%` (252px plus 5px padding), pulled up with `margin-top: -520px` so it starts at the top edge; overflow hidden, 30px bottom-right radius.
- **Left content column** (`#box3-4`): absolute, `left: 20%; width: 28%` (392px).
- **Right content column** (`#box4-4`): absolute, `left: 50%; width: 48%` (672px).
- **Headings**: `.bigheader` margin 2.5em 0 15px 15px (first ones -8px top), width 100%.
- **Paragraphs**: padding 0 4px 0 5px, margin-bottom 1.4em (22.4px); paper entries are one paragraph each with `<br>` line breaks.
- **Page height**: 13,810px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1400px | 0 left; columns fixed at 1400px | 16px | 80px | 18% / 28% / 48% columns of 1400px |
| 968–1399px | 0 | 16px | 80px | columns shrink with the viewport (percent widths) |
| <968px | 0 | 16px | 80px | none: `min-width: 968px` keeps the desktop layout and the page scrolls sideways |

## Components

- **Marker name**: Permanent Marker at 80px in brick red #a21919, set directly on the grey page with no box.
- **Position stack**: 21px Lato lines in #444444 with bold role words and olive affiliation links, sub-items indented 42px.
- **Dark contact tab**: #333333 block with a 30px bottom-right radius; full-bleed portrait on top; 22px uppercase #eeeeee heading; silver text with bold grey labels.
- **Paper entry**: one paragraph: bold 17.3px underlined olive title (two lines broken by hand when long); authors in 16px #222222; "To appear, *Venue* (Acronym), year." with the venue in italics; honours appended in bold black ("Spotlight") or in #a21919 for the thesis award; then an underlined olive `arXiv:…` or `doi:…` link.
- **Alumni list**: bulleted `li` items with an olive underlined name, a comma and an arrow-chained career path ("Ph.D., Stats → Postdoc → Assistant Prof."), some notes in #555555.
- **Section heading**: 28px Open Sans bold uppercase #333333 with a -11px text indent.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name header | yes | red marker logotype |
| Positions / affiliations | yes | 21px stacked lines with olive links |
| Portrait | yes | flush in the dark column |
| Contact | yes | silver lines in the dark column |
| Research statement | yes | justified hyphenated column |
| Group members and alumni | yes | bulleted lists with career arrows |
| Publications | yes | preprints, thesis, research articles, technical reports as paragraph entries |
| Awards | present but non-standard | bold or red words inside entries |
| News | absent from the source | a news block exists only as commented-out markup |
| Navigation | absent from the source | none |
| Responsive layout | absent from the source | fixed `min-width: 968px` |

## Adapting to Other Content

- **News**: reuse the commented-out pattern: short paragraphs with a bold grey date span (`span.anndate`, #808080) at the start, in the 28% column.
- **Teaching**: a `.bigheader` section in the left column with bulleted course lines and olive links.
- **Long publication lists**: keep one paragraph per paper and add year sub-headings as 22px Open Sans bold uppercase lines.
- **Phones**: the source does not adapt; if needed, stack the dark tab, header and both columns at 100% width below 968px.
- **Awards list**: lines in #222222 with the award name in #a21919.

## Do's and Don'ts

- Do keep the name in Permanent Marker and brick red; it is the page's signature.
- Do use olive #666600 for every link and paper title, with default underlines.
- Do keep the dark #333333 contact tab with only its bottom-right corner rounded.
- Don't add a second accent colour; red is reserved for the name and award text.
- Don't centre anything; the layout is left-anchored and dense.
- Don't add cards or shadows; structure comes from absolute columns and uppercase headings.

## Surfaces

#f2f2f2 page; one #333333 tab at the top left; nothing else is filled.

## Imagery

A single bright, close-cropped portrait in the dark tab; no thumbnails or figures.

## Layout

Header (name and positions) to the right of the dark contact tab; then two columns: Research, Group Members, Group Alumni, Probabilistic Programming | Preprints and Working Papers, Thesis, Research Articles, Technical Reports. About 13,810px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: background #f2f2f2, name #a21919, links #666600, hover #888800, text #222222, positions #444444, headings and tab #333333, tab heading #eeeeee, contact text #c0c0c0, labels #808080.

1. "Build a 1400px max container on #f2f2f2 with min-width 968px. Header with padding-left 20%: the name in Permanent Marker 80px (bold) #a21919, then Lato 21px/1.1em #444444 lines with bold role words and #666600 affiliation links, sub-items indented 42px."
2. "Add an absolute dark tab at the top-left, width 18%, background #333333, border-bottom-right-radius 30px: a full-width portrait, a 22px Open Sans bold uppercase 'CONTACT' in #eeeeee, and 16px #c0c0c0 contact lines with bold #808080 labels."
3. "Make two absolute columns, left 20% width 28% and left 50% width 48%, each headed by 28px Open Sans bold uppercase #333333 titles. Paper entries are paragraphs: a bold 17.33px underlined #666600 title (hover #888800), 16px #222222 authors, an italic venue, and an underlined #666600 arXiv link; append honours in bold, or in #a21919 for awards."

## Similar Pages

- Long-running hand-coded faculty pages with absolute-positioned columns.
- Personal pages that use a handwriting font as a logotype.

## Quick Start

```css
:root {
  --bg: #f2f2f2;
  --name: #a21919;
  --link: #666600;
  --link-hover: #888800;
  --text: #222222;
  --pos: #444444;
  --tab: #333333;
  --tab-heading: #eeeeee;
  --info: #c0c0c0;
  --label: #808080;
}
body { margin: 0; min-width: 968px; background: var(--bg); color: var(--text); font: 12pt/1.4 'Lato', sans-serif; }
.nameheader { font-family: 'Permanent Marker', serif; font-size: 60pt; color: var(--name); margin: 0; }
.pos { font-size: 21px; line-height: 1.1em; color: var(--pos); }
.bigheader { font: 700 28px 'Open Sans', Helvetica, Arial, sans-serif; text-transform: uppercase; color: var(--tab); text-indent: -11px; }
a:link, a:visited { color: var(--link); }
a:hover { color: var(--link-hover); }
.paper { font-weight: bold; font-size: 13pt; color: var(--link); }
.recede { background: var(--tab); border-bottom-right-radius: 30px; overflow: hidden; }
```

## Provenance

- **URL**: https://danroy.org/
- **Person**: Daniel M. Roy, statistical learning theory.
- **Award**: ICML 2024 Best Paper, "Information Complexity of Stochastic Convex Optimization" (last author). https://icml.cc/virtual/2024/awards_detail
- **Selection reason**: rule B (last author); existing entry kept, chosen for the hand-brushed logotype and the olive / red accents over a dense two-column academic layout.
- **Template credit**: none stated; hand-written HTML with `styles/screen.css` and `hyphenate.js`.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes and DOM dumps, the 1440×900 and full-page screenshots, and `screen.css` and the inline styles read directly, on 2026-10-28.
