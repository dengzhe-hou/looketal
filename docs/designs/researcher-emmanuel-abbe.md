# Emmanuel Abbe — Style Reference

> A Lausanne faculty letterhead on dove-grey paper: bold Lora titles stacked like a calling card, folder tabs, and justified biography set as carefully as a journal page.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's `css/bootstrap.css` (a Bootstrap 3.0.0 build themed with Lora via `@import`) plus a short inline `<style>` and the markup, read directly. Lora loads in 400, 400 italic, 700 and 700 italic and renders everywhere. The page is a single HTML file whose tabs show and hide sections with JavaScript; the render shows the About tab, which is the default.

## Overview

An all-serif page on a dove-grey #f6f6f6 ground with no cards, bands or navbar. The header is a stack: "Emmanuel Abbe" in Lora 46px/700 charcoal #333333, then four 22px/700 lines (Professor at EPFL, Chair of Mathematical Data Science, the institute, Senior Research Scientist at Apple). Below sits a row of justified Bootstrap tabs (About, Publications, Teaching, Group, SwissCardIA, Deepfoundations, Bernoulli) in 17px Lora: the active tab is a #555555 label in a box with 1px #dddddd sides and 4px top corners, the others are #428bca blue on the shared #dddddd baseline. The About tab is a media object: a 195px portrait with 6px corners on the left, and on the right 22px/700 subheads ("Chair of Mathematical Data Science", "Biography", "Contact") over 17px justified, hyphenated paragraphs at line-height 1.43. The Contact block pairs a bold-name postal address with an embedded 400×300 Google Maps satellite view. Everything sits in a 870px column at the left of a 1170px container, leaving the right quarter of the screen empty.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #f6f6f6 70.3% (page), #dededf 9.7% (anti-aliased text and tab rules), #95938d 8.2% (charcoal type and portrait), #f9f9f9 5.7%, #f6f6f5 3.1% and #f6f6f7 2.0% (ground variants). The portrait's green and blue and the #428bca tab labels are the only color.

Anatomy in DOM order (desktop 1440px; container 1170px at x=135, content column col-lg-9 = 870px):

1. **Name** (`.page-header h1`, y=58): Lora 46px/700, line-height 1.1, #333333, left. Page header margin-top 48px (collapsing with the h1's 24px). Gap 12px.
2. **Title lines** (`h4` ×4, y=121, 157, 193, 229): Lora 22px/700, line-height 1.1, #333333, margins 12px. Gap 59px (page-header padding 11px and margin 24px).
3. **Tabs** (`ul.nav.nav-tabs.nav-justified a.menu`, y=300, 46px tall): table-cell links, padding 10px 15px, Lora 17px/400 centred; active "About" #555555 on #f6f6f6 with 1px #dddddd top and sides and 4px 4px 0 0 radius; inactive #428bca, each with a 1px #dddddd bottom border forming one baseline to x=1005. Then an empty paragraph with a `<br>` (36px).
4. **Portrait** (`img.media-object.img-rounded`, x=140, y=391): 195×260, max-width 215px, margin 8px 5px, radius 6px, in a col-lg-3 column.
5. **Subhead** (`h4.media-heading`, x=360, y=383): Lora 22px/700 #333333, margin 0 0 5px.
6. **Paragraphs** (`.hyphenate p`, y=412, 550, 805, 645px wide): Lora 17px/400, line-height 24.29px (1.4286), #333333, text-align justify with soft hyphens inserted by a hyphenation script, margin-bottom 12px; links #428bca. The Biography paragraph crosses the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Dove Ground | #f6f6f6 | (literal) | page background, active tab fill |
| Charcoal | #333333 | (literal) | name, title lines, subheads, paragraphs, address |
| Tab Grey | #555555 | (literal) | active tab label |
| Link Blue | #428bca | (literal) | inactive tab labels, inline links, publication titles |
| Tab Rule | #dddddd | (literal) | active tab border, tab baseline |
| Tab Hover | #eeeeee | (literal) | inactive tab background and border on hover |

Declared but not visible: Bootstrap's dropdown, navbar, pagination and alert colors (e.g. #357ebd gradients, #d5d5d5) and the `.page-header` border, which is set to 0px.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Serif (everything) | "Lora", Georgia, "Times New Roman", Times, serif (Google Fonts @import) | Lora 400, 400 italic, 700, 700 italic | Gelasio |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.page-header h1` | 46px / 700 / 1.1 | #333333 |
| Title lines | `.page-header h4` | 22px / 700 / 1.1 | #333333 |
| Tab | `.nav-tabs.nav-justified > li > a` | 17px / 400 / 1.43, centred | #428bca (active #555555) |
| Subhead | `h4.media-heading` | 22px / 700 / 1.1 | #333333 |
| Body | `body`, `.hyphenate p` | 17px / 400 / 1.4286, justified | #333333 |
| Address | `address` | 17px / 400 / 1.4286; name `strong` 700 | #333333 |
| Publication item | `#publis-journal li` | 17px / 400; title `em a` italic; venue `strong` 700 | #333333, title #428bca |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Active tab | 4px 4px 0 0 | 1px #dddddd top and sides, bottom transparent | none |
| Inactive tab | 4px 4px 0 0 | 1px transparent, bottom 1px #dddddd | none |
| Portrait | 6px | none | none |
| Map iframe | 0 | none | none |

## Layout Metrics

- **Container**: Bootstrap 3 `.container` 1170px at ≥1200px, centred (x=135 at 1440); body padding 10px 0 20px.
- **Column**: everything in `col-sm-12 col-lg-9` (870px at ≥1200px); the right 300px stays empty.
- **Header**: `.page-header` margin 48px 0 24px, padding-bottom 11px, no border; h1 margin 24px 0 12px; h4 margins 12px.
- **Tabs**: justified table-cell tabs, padding 10px 15px, 46px tall, spanning the 870px column.
- **About media row**: portrait column col-lg-3 (about 218px), text column col-lg-9 (645px) with justified text; subhead margin-bottom 5px; paragraphs margin-bottom 12px.
- **Contact**: address col-lg-5, map col-lg-7 with a 400×300 iframe.
- **Page height**: 1,500px at 1440 (About tab).

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | 15px in a 1170px container | 17px | 46px | 9/12 content column; portrait 3/12 beside text 9/12 |
| 992–1199px | 15px in 970px | 17px | 46px | content column becomes full width (col-sm-12); portrait still beside text (col-md-3 / col-md-9) |
| 768–991px | 15px in 750px | 17px | 46px | portrait stacks above text; address stacks above map |
| <768px | 15px, fluid | 17px | 46px | justified tabs stop being table cells and stack as full-width rows |

## Components

- **Calling-card header**: name 46px/700 then four 22px/700 lines in the same #333333, left-aligned, with 12px between lines and no rule below.
- **Folder tabs**: Bootstrap justified `nav-tabs`; labels 17px Lora; inactive #428bca with a #dddddd baseline, hover fill #eeeeee; active #555555 on the page grey with a #dddddd box open at the bottom; 4px top corners only.
- **Media object**: 6px-rounded portrait (max 215px) on the left, 22px/700 subhead and justified 17px paragraphs on the right.
- **Justified prose**: `text-align: justify` plus script-inserted soft hyphens so lines stay even; links #428bca, underline on hover.
- **Contact block**: `<address>` with a bold name and plain lines, beside an embedded 400×300 Google Maps satellite iframe with no border.
- **Publication list** (Publications tab): disc bullets; author initials and surnames in regular, the paper title as an italic #428bca link ending in a comma, and the venue in bold ("NeurIPS'24").

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and titles | yes | 46px bold name, four 22px bold lines |
| Tab navigation | yes | Bootstrap justified folder tabs |
| Portrait | yes | 6px-rounded photo beside the text |
| Chair description and biography | yes | justified hyphenated paragraphs |
| Awards | present but non-standard | written as one semicolon-separated sentence in the biography |
| Contact with map | yes | address plus embedded Google Map |
| Publications | yes | disc list in a separate tab |
| Teaching, SwissCardIA, Bernoulli | yes | further tabs on the same page |
| Footer | absent from the source | — |

## Adapting to Other Content

- **Long publication lists**: keep the disc list with italic linked titles and bold short venue tags; split by year with 22px/700 subheads rather than adding cards.
- **News**: add a tab, and inside it a 17px list with the date in bold; keep it justified only if items are full sentences.
- **Students**: use the same media-object pattern per person with a smaller rounded photo.
- **Results or figures**: images at the full 645px text width with a 17px italic caption; no borders.
- **More titles**: add further 22px/700 lines under the name; the stack is the identity.

## Do's and Don'ts

- Do keep one serif (Lora) at two weights; hierarchy is 46 / 22 / 17px.
- Do justify body paragraphs and keep hyphenation on so the column edge stays clean.
- Do keep the ground #f6f6f6 and let the active tab share it.
- Don't add cards, shadows or rules beyond the tab baseline.
- Don't color headings; only links and inactive tabs are #428bca.
- Don't widen the content past 9/12 of the container; the empty right margin is part of the look.

## Surfaces

One flat #f6f6f6 surface; the active tab is cut from the same grey. The only inset content is the satellite map.

## Imagery

A warm colour portrait with rounded corners and an embedded satellite map of the EPFL campus; no figures or icons.

## Layout

Header stack, tabs, then the active tab's content: on About, the portrait-and-text media row and the contact block. About 1,500px tall at 1440 with much of the page empty below.

## Agent Prompt Guide

Quick colors: ground #f6f6f6, text #333333, links and inactive tabs #428bca, active tab #555555, tab rule #dddddd, tab hover #eeeeee.

1. "Build a calling-card header on #f6f6f6: name in Lora 46px/700, line-height 1.1, #333333; then four title lines in Lora 22px/700 #333333 with 12px margins; 24px below, a justified row of tabs."
2. "Make folder tabs: equal-width table-cell links, padding 10px 15px, Lora 17px; inactive #428bca with a 1px solid #dddddd bottom border and hover background #eeeeee; active #555555 on #f6f6f6 with 1px solid #dddddd top and sides, transparent bottom, radius 4px 4px 0 0."
3. "Create a media object: a portrait with max-width 215px, radius 6px, margin 8px 5px in a quarter-width column; beside it a Lora 22px/700 #333333 subhead (margin-bottom 5px) and 17px/1.4286 #333333 paragraphs with text-align justify, hyphens auto and #428bca links."

## Similar Pages

- Bootstrap 3 faculty pages with tabbed single-file navigation.
- European chair pages that use a serif-only, unboxed layout.

## Quick Start

```css
:root {
  --ground: #f6f6f6;
  --text: #333333;
  --link: #428bca;
  --tab-active: #555555;
  --tab-rule: #dddddd;
  --tab-hover: #eeeeee;
  --serif: 'Lora', Georgia, 'Times New Roman', Times, serif;
}
body { background: var(--ground); color: var(--text); font: 400 17px/1.428571429 var(--serif); padding: 10px 0 20px; }
h1 { font-size: 46px; font-weight: 700; line-height: 1.1; }
h4 { font-size: 22px; font-weight: 700; line-height: 1.1; margin: 12px 0; }
a { color: var(--link); text-decoration: none; }
.nav-tabs > li > a { padding: 10px 15px; border: 1px solid transparent; border-bottom-color: var(--tab-rule); border-radius: 4px 4px 0 0; }
.hyphenate { text-align: justify; hyphens: auto; }
```

## Provenance

- **URL**: https://sma.epfl.ch/~abbe/
- **Person**: Emmanuel Abbe (mathematical data science, learning theory).
- **Venue / award**: ICML 2023 Outstanding Paper, "Generalization on the Unseen, Logic Reasoning and Degree Curriculum".
- **Selection reason**: Rule B (first author); announcement https://icml.cc/virtual/2023/awards_detail. Personal tilde page that also serves as his chair page.
- **Template credit**: none visible; Bootstrap 3.0.0 with a Lora-themed stylesheet.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and `css/bootstrap.css`, the inline `<style>` and the markup read directly, on 2026-10-28.
