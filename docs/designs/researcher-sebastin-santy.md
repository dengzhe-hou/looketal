# Sebastin Santy — Style Reference

> A poster headline over a reading-room list: a black condensed name stamped at the top, a red pen flourish, then quiet grey rows of papers in Roboto Light.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of the rendered elements and pseudo-elements, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site's Vite bundle stylesheet `assets/index-BtUv-jb7.css` (Bootstrap 4 plus a short custom block) with the JS-rendered markup. The name and section headings use League Gothic with `font-display: swap`; the 1440×900 snap caught the fallback sans for the name, while the full-page shot and the computed style (League Gothic in `fonts_loaded`) show the settled state, which is what this file describes. There is no dark mode.

## Overview

A short (2,211px) single-column researcher homepage on warm off-white #fefdfc. There is no navigation, photo or sidebar at desktop. The identity rests on contrast: the name "SEBASTIN SANTY" stacked on two lines in League Gothic at 75.2px (synthesised bold, black), and section labels "RESEARCH" and "TALKS" in the same face at 38.4px, against body text in Roboto 300 at warm grey. Under RESEARCH a single red Font Awesome signature glyph (#e07057) acts as an ornament. Publications are grouped into themed subsections ("From English to the World", "Low Resource Language Systems", "Interfaces for x People") in Roboto 500 #222222. Each entry has a 7px rounded #f2f0ed bar at its left edge, a 17.6px black title, a grey author line with the owner's name dotted-underlined, a venue line with optional bold award flags (SPOTLIGHT, OUTSTANDING PAPER) and pale grey press links, and right-aligned dotted-underlined PDF • ABS • WEB link chips.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): off-white #fefdfc 85.7% plus #fffffe / #fefdfa / #fefdfd / #fffdfc / #fcfefe 6.4%; light grey #e9e8e7 5.1% (anti-aliased Roboto Light text and the #f2f0ed entry bars); mid grey #8a8989 3.0% (author lines, body text and the black name strokes blended). Black and the red ornament are too small in area to form clusters.

Anatomy in DOM order (desktop 1440px). Bootstrap `.container.allstuffp` is 1140px at x=150 with 24px top padding; `.row.allstuff` adds 48px top padding; the `col-lg-9 mx-auto about` column is 855px (75%) at x=293 with 48px top and 15px side padding, so content runs x=308–1133 (825px).

1. **Name** (`.title_text`, y=120, 144px tall): "SEBASTIN" / "SANTY", League Gothic 75.2px (4.7rem) / 700 synthesised, line-height 72px (54pt), #000000, left.
2. **Email** (y=264): "ssanty@cs.washington.edu", Roboto 18.13px/300 #58554f, padding-top 2px.
3. **Intro** (`p.mainpara.subpara`, y=335, 40px below): Roboto 17.44px/300, line-height 27.9px, #525252, justified across 825px; linked names (University of Washington, Sewoong Oh) 400 #444444 with a near-invisible dotted underline; margin-bottom 16px.
4. **Section label** (`.subtitle_text`, y=435 incl. 30px padding-top): "RESEARCH", League Gothic 38.4px / 700, line-height 61.44px, #000000.
5. **Ornament** (`h4.voidtitle`, y=539, margin 12.8px 0 8px): a 27.2px Font Awesome `fa-signature` glyph in #e07057.
6. **First entry** (`.talk`, y=588): 7×72px #f2f0ed bar at the left (radius 10px); title at x=322 17.6px/400 #000000; authors 16px/300 #888888; venue line 15.2px/300 #000000 "Position Paper ● ICML 2025"; PDF ● ABS right-aligned at x=1056–1132, 13.6px/400 #000000 dotted-underlined.
7. **Theme heading** (`h4.theme.lingtitle`, y=701): "From English to the World", Roboto 20.8px/500 #222222, margin 24px 0 8px; entries continue below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #fefdfc | (body) | page background |
| Body Warm Grey | #58554f | (body) | email line, default text |
| Intro Grey | #525252 | `.mainpara` | intro paragraph |
| Link Grey | #444444 | `a` | intro links, ● separators between link chips |
| Ink | #000000 | (literal) | name, RESEARCH/TALKS labels, paper titles, venue lines, award flags, PDF/ABS chips, link hover |
| Theme Ink | #222222 | `.lingtitle`, `.uititle` | themed subsection headings |
| Entry Grey | #909090 | `.talk` | entry container text |
| Author Grey | #888888 | `.authors` | author lines |
| Venue Dot | #555555 | `.positionsep` | ● between paper type and venue |
| Press Grey | #bbbbbb | `.article` | press and coverage links (CMU ML Blog, US FTC, …) |
| Entry Bar | #f2f0ed | `.talk:before` | 7px rounded bar at the left of every entry |
| Coral | #e07057 | `.voidtitle` | signature ornament under RESEARCH |
| Hidden Underline | #fbfbfb | `a` text-decoration-color | dotted underline of plain links at rest (turns #111111 on hover) |
| Hover Underline | #111111 | `a:hover` | dotted underline on hover |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | League Gothic, sans-serif | League Gothic 400 (self-hosted, swap); set at 700 so it is synthesised bold | Oswald |
| Text | Roboto, sans-serif | Roboto 300, 400, 500, 700 (self-hosted) | Inter |
| Serif (italic x) | STIX Two Text | STIX Two Text 400 and 700 italic; renders the 600-weight italic "x" in "Interfaces for x People" | STIX Two |
| Icons | Font Awesome 5 Free | Font Awesome 5 Free 900 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.title_text` | League Gothic 75.2px / 700 / 72px | #000000 |
| Section label | `.subtitle_text` | League Gothic 38.4px / 700 / 61.44px, padding-top 30px | #000000 |
| Theme heading | `h4.theme` | Roboto 20.8px / 500 / 1.2, margin 24px 0 8px | #222222 |
| Ornament | `h4.voidtitle` | Font Awesome 27.2px | #e07057 |
| Intro | `.mainpara.subpara` | Roboto 17.44px / 300 / 27.9px, justified | #525252 |
| Column base | `.about` | 18.13px (13.6pt) / 300 / 1.6 | #58554f |
| Paper title | `.papertitle` | 17.6px / 400 / 1.55 | #000000 |
| Authors | `.authors` | 16px / 300 / 1.55; own name dotted underline | #888888 |
| Venue line | `.conf` | 15.2px / 300 | #000000 |
| Award flag | `.award` | 12px / 600 uppercase, Font Awesome icon before, margin-left 11.52px | #000000 |
| Press link | `.article` | 14.4px / 300, dotted underline | #bbbbbb |
| Link chip | `.tag` | 13.6px / 400, uppercase text, dotted underline, padding-right 3px | #000000 |
| Chip separator | `.tagsep` | 12.8px ●, padding 0 6px | #444444 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Entry bar (`.talk:before`) | 10px | none (7px-wide #f2f0ed fill from top 3.2px to bottom 5.6px) | none |
| Links | 0 | dotted underline, 1px, offset 2.5px | none |
| Everything else | 0 | none | none |

## Layout Metrics

- **Column**: Bootstrap `.container` 1140px (x=150) → `.row` → `.col-lg-9.mx-auto` 855px (75%) centred at x=293 with 15px padding → content 825px at x=308.
- **Top spacing**: container padding-top 24px + row 48px + column 48px → name at y=120.
- **Header rhythm**: name 144px (two 72px lines) → email 31px → intro 40px below → section label 16px below (plus its own 30px padding-top).
- **Entries**: `.talk` margin 8px 0, padding-left 14.4px; title, authors and venue stacked at line-height 1.55; link chips right-aligned on the venue row (`.tagspan`, `text-align: right`).
- **Themes**: subsection headings 24px above, 8px below.
- **Sections**: RESEARCH and TALKS labels 30px padding-top each; the page ends after the talks list with no footer.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px (incl. 1440) | container 1140px, column 75% | 18.13px | 75.2px | link chips shown at the right |
| 992–1199px | container 960px, column 75% (720px) | 18.13px | 75.2px | — |
| ≤1000px | — | 18.13px | 75.2px | `.tagspan` link chips hidden |
| 768–991px | container 720px, column 100% | 18.13px | 75.2px | — |
| ≤768px | column padding-left 1rem; top paddings removed | 16px (`.about`) | 75.2px | — |

## Components

- **Condensed name**: League Gothic 75.2px, all caps, black, line-height 72px, stacked one word per line; no other decoration.
- **Section label**: League Gothic 38.4px caps in black with 30px top padding; RESEARCH is followed by a coral `fa-signature` glyph at 27.2px as an ornament.
- **Publication entry** (`.talk`): position relative, padding-left 14.4px, margin 8px 0; a 7px #f2f0ed rounded bar (`::before`, radius 10px) runs the height of the entry at the left; contents: black 17.6px title link, #888888 16px author line with the owner's name dotted-underlined, a black 15.2px venue line, optional award flag (Font Awesome icon + 12px/600 uppercase text) and #bbbbbb dotted press links separated by small dots, and at the right PDF ● ABS ● WEB chips in 13.6px black with dotted underlines.
- **Theme heading**: Roboto 20.8px/500 #222222, sentence case; may contain an italic STIX Two Text "x".
- **Links**: inherit #444444 (or black for chips) with a dotted underline that is #fbfbfb (almost invisible) at rest and turns #111111 with text #000000 on hover, 0.15s.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name header | yes | League Gothic two-line black name |
| Contact | yes | plain email line under the name |
| Bio | yes | one justified Roboto Light paragraph |
| Photo | absent from the source | `.sideimg` (1px #cccccc border, hidden at ≤768px) is declared in CSS but no element uses it |
| Navigation | absent from the source | — |
| Publications | yes | themed groups of entries with left bars and right-aligned link chips |
| Awards | yes | inline bold uppercase flags with icons on the venue line |
| Press coverage | yes | pale grey dotted links on the venue line |
| Talks | yes | same entry style under a TALKS label |
| News | absent from the source | — |
| Footer | absent from the source | page ends after the talks |

## Adapting to Other Content

- **Long publication lists**: keep one `.talk` per paper with 8px gaps, group by theme with 20.8px/500 #222222 headings 24px above; never add cards or borders.
- **News items**: use the same entry: date as the 15.2px/300 black venue line, headline as the 17.6px title, details in #888888 16px.
- **A photo**: if one is added, place it right of the name in the `.teaser` row at about 25% width with a 1px #cccccc border (the declared `.sideimg` style), hidden at ≤768px.
- **More sections** (Teaching, Service): add another League Gothic 38.4px label with 30px top padding, optionally followed by the coral glyph ornament.
- **Many link types**: add chips to the right-aligned group (13.6px, dotted underline, ● #444444 separators); they disappear below 1000px, so keep the title linked too.

## Do's and Don'ts

- Do keep display type to the name and section labels only, in black League Gothic caps.
- Do set all running text in Roboto 300 on #fefdfc with greys #525252, #888888 and #bbbbbb.
- Do mark each entry with the 7px rounded #f2f0ed left bar.
- Do use dotted underlines for every link and underline the owner's name in author lists.
- Don't add color besides the single coral ornament.
- Don't use boxes, shadows or dividers; spacing and the left bars carry the structure.
- Don't put the link chips on their own line at desktop; they sit right-aligned on the venue row.

## Surfaces

One warm off-white surface (#fefdfc) for the whole page. The only drawn shapes are the 7px #f2f0ed entry bars.

## Imagery

None besides icons: a coral Font Awesome signature glyph and small award icons. No portrait or logos render at desktop.

## Layout

A single centred 825px column inside Bootstrap's 1140px container: name and email, bio, RESEARCH with an ornament and three themed lists, TALKS with one entry. Ample top whitespace (120px before the name) and no footer.

## Agent Prompt Guide

Quick colors: background #fefdfc, display #000000, intro #525252, body #58554f, authors #888888, press #bbbbbb, theme headings #222222, entry bar #f2f0ed, ornament #e07057.

1. "Build a researcher header in an 825px column starting 120px from the top: the name in League Gothic 75.2px bold caps, line-height 72px, #000000, one word per line; an 18px Roboto 300 #58554f email line; 40px below, a justified Roboto 17.44px/300 #525252 bio with 400-weight links in #444444 and dotted underlines that are #fbfbfb at rest and #111111 on hover."
2. "Make a section label 'RESEARCH' in League Gothic 38.4px bold caps #000000 with 30px top padding, followed by a 27.2px Font Awesome signature icon in #e07057, and themed subheadings in Roboto 20.8px/500 #222222 with margin 24px 0 8px."
3. "Style a publication entry: position relative, padding-left 14.4px, margin 8px 0, with a ::before bar 7px wide, background #f2f0ed, border-radius 10px, from top 3.2px to bottom 5.6px. Inside: a 17.6px/400 #000000 title, a 16px/300 #888888 author line with the owner's name dotted-underlined, a 15.2px/300 #000000 venue line with optional 12px/600 uppercase award flags and 14.4px #bbbbbb dotted press links, and right-aligned 13.6px #000000 dotted-underlined PDF ● ABS chips."

## Similar Pages

- Minimal researcher homepages that pair one bold condensed display face with a light sans body and no navigation.
- NLP and HCI personal sites that group publications by research theme rather than by year.

## Quick Start

```css
:root {
  --bg: #fefdfc;
  --ink: #000000;
  --body: #58554f;
  --intro: #525252;
  --link: #444444;
  --theme: #222222;
  --authors: #888888;
  --press: #bbbbbb;
  --bar: #f2f0ed;
  --ornament: #e07057;
  --font-display: "League Gothic", sans-serif;
  --font-text: Roboto, sans-serif;
  --column: 825px;
  --entry-bar: 7px;
}
```

## Provenance

- **URL**: https://sebastinsanty.com/
- **Person**: Sebastin Santy, PhD student at the University of Washington (advised by Sewoong Oh); NLP design biases and HCI.
- **Award**: first author of "NLPositionality: Characterizing Design Biases of Datasets and Models", ACL 2023 Outstanding Paper (https://2023.aclweb.org/program/best_papers/).
- **Selection reason**: Rule A (first author of an ACL 2023 Outstanding Paper); homepage found via Semantic Scholar and GitHub SebastinSanty; JS-rendered page.
- **Template credit**: none stated; a custom Vite/React build on Bootstrap 4 with Fontsource fonts (Roboto, League Gothic, STIX Two Text, Ubuntu Mono) and Font Awesome 5.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), additional computed-style probes of the name, labels, ornament, entries and their `::before` bars, authors, venue lines, awards, press links and chips, the 1440×900 and full-page screenshots, and the bundle stylesheet read directly, on 2026-10-28.
