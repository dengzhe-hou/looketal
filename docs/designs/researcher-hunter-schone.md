# Hunter Schone — Style Reference

> An olive-drab field notebook: bold Montserrat capitals, a faint EMG trace scrolling behind the bio, and robotic hands reaching across a white band to announce the work.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles of every text node, loaded fonts, first-viewport color share), the 1440×900 shot, a full-page capture (12,835px tall), and the page's own inline Wix CSS read from the downloaded HTML (`#comp-…` variable blocks and the `--color_NN` palette). This is a Wix "classic" site: the h1 and h3 elements declare `helvetica-w01-bold` but every visible word is wrapped in spans set to Montserrat, so the rendered values below are probed on those spans. Wix serves phones a separately authored mobile layout chosen by user agent; that layout was not rendered.

## Overview

A long single page on white. A 71px dark olive bar (#2f3827) with no links caps the window. The hero sits on a pale grey EMG-like wave pattern (an image layer behind the whole intro and news area): left column with "HUNTER SCHONE" in 50px bold olive (#576947) Montserrat and an italic "PhD", a 24px "Neuroscientist" line, a 20px research statement with bold key phrases, and short lab history; right column a circular 399px portrait over three olive pill buttons (CV, Google Scholar, Github) and a centred contact line. Below runs a dense dated news list in 14px. A full-bleed photo band of two prosthetic hands reaching toward a centred "PROJECTS" heading opens the project section, where each project pairs a journal cover or figure (445px wide, left) with an uppercase 28px title and an 18px blurb (460px, right). A dark olive press-logo band then leads into "RESEARCH PUBLICATIONS" and "PRESENTATIONS", plain reference lists at 18px with the author's name bolded.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 55.8% plus near-whites #fdfdfc 3.9%, #fffffe 2.5%, #f7f7f7 7.2%; wave-pattern grey #efefee 12.2%; header olive #363929 11.2% (the #2f3827 bar as quantized); portrait/skin taupe #c3bbb4 7.1%.

Anatomy in DOM order (desktop 1440px; Wix stage 980px wide at x=230):

1. **Header bar** (`header#SITE_HEADER`, 0–71px): solid #2f3827 across the full width, empty (no nav, no logo). Next content starts at y=110 (39px gap).
2. **Name** (h1 > span.color_41, y=110, box 592×74, left x=230): "HUNTER SCHONE" Montserrat 50px/700, line-height 67px, #576947, typed in capitals. The trailing "PhD" is Montserrat 34px/400 italic #576947 on the same baseline.
3. **Role** (p.font_8, y=172): "Neuroscientist", Montserrat 24px/400 #181818, set tight under the name (its line box overlaps the h1 box). Gap 57px.
4. **Research statement** (p.font_7, y=258, 460px wide): Montserrat 20px/400, line-height 33.4px, #181818; key phrases in 700. Followed by an empty 30px spacer paragraph.
5. **Position line** (y=455): Montserrat 18px/400, line-height 30.06px; supervisor and lab names are underlined links in the same #181818. Empty 33px spacer.
6. **Previous labs** (y=609): label 16px underlined, then two 16px/26.72px lines with underlined PI names.
7. **Portrait** (right column, img at x=783, y=187, 399×399): circular crop of a photo on a light grey studio backdrop (the circle is in the image crop; no border-radius is set). Gap 22px.
8. **Pill buttons** (y=608, 35px tall): CV (85px), Google Scholar (138px), Github (67px), 11px and 21px apart; #576947 fill, white Futura 16px/700, radius 100px.
9. **Contact** (p.font_8, y=662, x=750, 460px, centred): email written as "schonehunter [at] gmail [dot] com" and "Currently living in Pittsburgh, PA, USA", Montserrat 16px/400, line-height 28px. Gap 81px.
10. **News** (from y=799): underlined label "Recent News (2-years):", then month lines ("Sept 2026") at x=230 and bulleted items at x=255, all Montserrat 14px/400, line-height 24.5px, #181818, with bold phrases and #4488f1 underlined links. The list continues below the fold to y≈1790.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Moss | #576947 | --color_41 / --color_48 | name, "PhD", section headings (PROJECTS, RESEARCH PUBLICATIONS, PRESENTATIONS), pill button fill |
| Fern Hover | #587f36 | --bgh on the button comps | pill button fill on hover (0.4s transition) |
| Forest Night | #2f3827 | --color_42 | 71px header bar, press-logo band at y=6388–6685 |
| Ink | #181818 | --color_45 | all body text, project titles, news, reference lists, links in prose |
| Paper | #ffffff | --color_44 | page and section backgrounds, button labels |
| Wave Grey | #efefee | (image) | the EMG-like wave pattern behind hero and news |
| Link Blue | #4488f1 | (literal, rich text) | underlined inline links inside news items ("dataset", "preprint", "paper") |
| Muted Grey | #525252 | --color_40 | declared palette grey; no visible element uses it |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display / text | `helvetica-w01-bold` / `helvetica-w01-roman` on the Wix text classes (`font_5`, `font_7`, `font_8`) | Montserrat 400, 400 italic, 700 from inner spans; the Helvetica faces load but no visible word uses them | Montserrat (Google Fonts) |
| Buttons | `futura-lt-w01-book` (button `--fnt`: normal normal 700 16px/1.41em) | Futura LT Book, synthesized bold | Jost 600 |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `h1.font_5 > span.color_41` | 50px / 700 / 67px | #576947 |
| Name suffix "PhD" | inner span | 34px / 400 italic / 67px | #576947 |
| Section heading | `h2.font_5 > span.color_41` | 50px / 700 / 67px, centred, capitals typed | #576947 |
| Role line | `p.font_8` span | 24px / 400 / normal | #181818 |
| Research statement | `p.font_7` span | 20px / 400 (key phrases 700) / 33.4px | #181818 |
| Bio paragraph | `p.font_7` span | 18px / 400 / 30.06px | #181818 |
| Project title | `h3.font_2` span | 28px / 400 with 700 keywords / 38.5px, capitals typed | #181818 |
| Project blurb / references | `h3.font_8` / `p.font_8` span | 18px / 400 (bold 700, venues italic) / 31.5px | #181818 |
| News | `p.font_8` span | 14px / 400 (bold 700) / 24.5px | #181818; links #4488f1 |
| Contact | `p.font_8` span | 16px / 400 / 28px, centred | #181818 |
| Footer email | `p.font_9` span | 15px / 400 / 28.125px, centred | #181818 |
| Pill button label | `span.wixui-button__label` | Futura 16px / 700 / 22.56px | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Pill buttons | 100px (35px tall) | 0px | none (`--shd: none`) |
| Portrait | circle baked into the image crop, 399×399 | none | none |
| Project covers / figures | 0 | none | none |
| Footer | 0 | top 1px rgba(255, 255, 255, 0.15) (invisible on white) | none |

No other radii, borders or shadows render on the page.

## Layout Metrics

- **Stage**: Wix fixed stage 980px wide, left edge x=230 at 1440 (centred: (1440 − 980) / 2). Text columns inside it are absolutely positioned, not a grid.
- **Hero**: two columns. Left text column x=230, 460px wide; right column x=750–1210 holding the portrait (x=783, 399px), the buttons and the contact block. Wave image section spans y=71–1818 including the news list.
- **News list**: x=230, 921px wide; bullets indented to x=255.
- **Projects photo band**: full bleed, y=1818–2184 (366px), "PROJECTS" centred at y=1969.
- **Project rows**: figure x=245, 445px wide; text x=750–754, 460px wide; rows about 700–850px apart (titles at y=2225, 3063, …), separated only by whitespace.
- **Press band**: full bleed #2f3827, y=6388–6685 (297px), logos 23–122px tall packed into the 980px stage.
- **References**: x=260, 924px wide, one paragraph per entry with about 20px between entries.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥980px | (width − 980) / 2, 230px at 1440 | 18px | 50px | two columns as above |
| <980px | 0; page scrolls horizontally (scrollWidth stays 980 at 800px) | 18px | 50px | none |
| Mobile user agent | Wix mobile layout (separate, not probed) | — | — | — |

## Components

- **Pill button** (`a.wixui-button`): 35px tall, width fits label (85 / 138 / 67px), background #576947, no border, radius 100px, label Futura 16px/700 white centred. Hover: background #587f36 with `transition: border-color 0.4s ease 0s, background-color 0.4s ease 0s`.
- **Circular portrait**: 399×399 image cropped to a circle, light grey backdrop, no frame or shadow.
- **News item**: month line ("August 2026") 14px/400 #181818 flush left, then a disc-bulleted list indented 25px, one sentence per bullet with the key noun phrase in 700 and links in #4488f1 underlined.
- **Photo section header**: a full-bleed 366px band with a cut-out photo on white (prosthetic hands from left and right) and the section word centred in 50px/700 #576947.
- **Project row**: left a 445px cover image (Nature Neuroscience cover, figure panels, lab photo); right a 28px/400 title in capitals with the key words in 700, an 18px/31.5px blurb with bold findings, then bracketed italic underlined links "[data + code] [doi] [pdf] [interview]", optionally followed by "Selected press coverage:" and partner logos.
- **Press band**: #2f3827 strip with a collage of white and colour media logos (Scientific American, NPR, BBC, Nature, New Scientist…), no captions.
- **Reference entry**: 18px/31.5px paragraph, own name "Schone, H.R." in 700, journal or talk title in italic, then bracketed underlined links in #181818.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top navigation | present but non-standard | a 71px #2f3827 bar with no links; the page is one long scroll |
| Hero name / role / bio | yes | 50px olive capitals, 24px role, 20px statement with bold phrases |
| Portrait | yes | 399px circle on the right |
| Link buttons | yes | three #576947 pills, Futura 16px/700 |
| News | yes | dated 14px bulleted list, two years deep |
| Projects | yes | photo band header, then image-left / text-right rows |
| Press logos | yes | dark olive logo band |
| Publications | yes | full reference list, 18px, own name bold |
| Talks | yes | "PRESENTATIONS" list in the same reference style |
| Teaching, blog, contact form | absent from the source | — |
| Footer | yes | centred 15px obfuscated email |

## Adapting to Other Content

- **More links**: add pills of the same 35px height and #576947 fill in the right column row; at 1440 three to four fit inside the 460px column with 11–21px gaps.
- **A results table or dataset list**: set it in 18px/31.5px #181818 Montserrat inside the 460px text column of a project row, header row in 700, with no fills or rules beyond what the page uses (it has none).
- **Long publication lists**: keep one 18px paragraph per entry across the 924px width; group by year with a 28px/700 #181818 capitals subheading rather than adding new colours.
- **More news**: keep the 14px month-line plus bullets pattern; the page caps it at "Recent News (2-years)", so move older items into an archive rather than lengthening the hero area.
- **A new section**: open it with a 50px/700 #576947 centred capitals heading; use a full-bleed photo band behind it only when there is a strong cut-out image.

## Do's and Don'ts

- Do keep one olive (#576947) for the name, section headings and buttons, and the darker #2f3827 for full-bleed bars.
- Do type headings in capitals at 50px/700; project titles in capitals at 28px with only the key words bold.
- Do put a pale texture image behind the hero; keep it under about 10% contrast against white so 20px text stays readable.
- Do use bracketed underlined text links ("[doi] [pdf]") under projects and references.
- Don't introduce rounded cards or shadows; the only rounded shapes are the pills and the circular portrait.
- Don't use blue for links outside the news list; elsewhere links stay #181818 and underlined.
- Don't center body text; only section headings and the contact line are centred.

## Surfaces

White page; a pale #efefee wave-texture image behind the hero and news (y=71–1818); a full-bleed white photo band for PROJECTS; dark olive #2f3827 for the top bar and the press-logo band. No cards or tinted panels.

## Imagery

A circular head-and-shoulders portrait; a full-bleed cut-out of two prosthetic hands reaching inward; journal covers (Nature Neuroscience, Nature Human Behaviour style), multi-panel data figures and lab photos at 445px in project rows; institutional logos under projects; a collage of media logos on the olive band. Images are square-cornered and unframed.

## Layout

Fixed 980px Wix stage centred in the window. Hero in two columns (text 460px left, portrait and buttons right), news full stage width, then alternating full-bleed bands (photo header, press logos) between long white sections. Generous 40–80px vertical gaps between blocks, but the news and reference lists themselves are dense.

## Agent Prompt Guide

Quick colors: olive #576947, olive hover #587f36, dark olive #2f3827, ink #181818, page #ffffff, wave texture #efefee, news link #4488f1.

1. "Build a two-column hero inside a 980px stage: a 71px #2f3827 bar on top; left column 460px with name 'FIRST LAST' in Montserrat 50px/700 #576947 line-height 67px plus an italic 34px/400 'PhD', role 24px/400 #181818, statement 20px/33.4px with bold key phrases; right column a 399px circular portrait above pill buttons 35px tall, #576947 fill, white Futura 16px/700, radius 100px, hover #587f36 over 0.4s."
2. "Create a project row: 445px figure on the left, 460px text on the right; title Montserrat 28px/400 in capitals with key words 700, line-height 38.5px, #181818; blurb 18px/31.5px; links '[data + code] [doi] [pdf]' italic, underlined, #181818."
3. "Make a section opener: full-bleed 366px white band with a cut-out photo, heading centred Montserrat 50px/700 #576947 in capitals; follow with a full-bleed #2f3827 band of press logos 297px tall."

## Similar Pages

- Wix and Squarespace personal sites of neuroscience postdocs that pair a circular portrait with pill buttons.
- Lab pages that use a full-bleed cut-out photo as a section header.

## Quick Start

```css
:root {
  --olive: #576947;
  --olive-hover: #587f36;
  --olive-dark: #2f3827;
  --ink: #181818;
  --paper: #ffffff;
  --texture: #efefee;
  --link-news: #4488f1;
  --font-text: "Montserrat", sans-serif;
  --font-button: "Futura", "Jost", sans-serif;
  --stage: 980px;
  --radius-pill: 100px;
}
body { background: var(--paper); color: var(--ink); font: 400 18px/31.5px var(--font-text); }
h1, h2 { font: 700 50px/67px var(--font-text); color: var(--olive); }
.pill { height: 35px; width: 85px; /* Wix sets each width: 85, 138, 67px */ border-radius: var(--radius-pill); background: var(--olive); color: #fff; font: 700 16px/1.41 var(--font-button); transition: background-color .4s ease; }
.pill:hover { background: var(--olive-hover); }
```

## Provenance

- **URL**: https://www.hunterschone.com/
- **Person**: Hunter Schone, neuroengineering (bionic limbs and body representation); postdoctoral fellow at the University of Pittsburgh per the page.
- **Award**: Glushko Dissertation Prize 2024.
- **Selection reason**: Rule B(2), Glushko Dissertation Prize 2024 winner per https://cognitivesciencesociety.org/glushko-dissertation-prize/ ; homepage linked from his own Bluesky profile (hunterschone.bsky.social).
- **Template credit**: built with Wix (Thunderbolt renderer, `wixui-*` classes); no template named.
- **Evidence used**: tools/computed_style.py render at 1440×900, a per-element style census and full-page capture from the same headless Chrome, a width check at 1000 and 800px, and the page's inline Wix CSS from the downloaded HTML, on 2026-10-28.
