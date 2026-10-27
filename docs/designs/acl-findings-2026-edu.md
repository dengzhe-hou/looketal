# Cream Serif Explorer — Style Reference

> A warm study desk: a cream gradient floor with a faint graph-paper grid, a heavy serif title beside a phone-like slide card, and an interactive viewer that sets a student's handwriting next to the model's transcript.

**Theme:** light

Measured on 2026-10-28 from a headless Chrome render at 1440×900 (`tools/computed_style.py`: computed styles of the sticky nav, nav pills, eyebrow, title spans, summaries, authors, metric row, buttons, hero carousel, section headings, sub-headings and footer, first-viewport anatomy, loaded fonts and color share), the first-viewport screenshot, the full-page capture, a 1440×3700 headless capture of the dataset and findings sections, and the page's hand-written `styles.css`, which defines its tokens as CSS custom properties. The page rewrites its URL to `?example=hw2-student31-q4-2-2&view=raw` on load, which selects the first interactive example. Positions are document coordinates at 1440px wide.

## Overview

EDU-CIRCUIT-HW is a custom single page with no framework. The body background layers a warm terracotta glow at the top left (rgba(171,93,43,.16)), a faint green glow at the top right, and a vertical cream gradient (#f8efe2 → #f7f2e8 → #f3ede3); a fixed 32px graph-paper grid of 2.5% ink lines fades out down the page. A 74px sticky translucent nav carries the bold "EDU-CIRCUIT-HW" brand and four pill links, the current one on a white wash. The hero is a two-column grid in a 1280px shell: on the left, a terracotta (#ab5d2b) uppercase eyebrow "ACL 2026 FINDINGS", a 61.6px Source Serif 4 bold wordmark with very tight tracking (-0.07em), a 26.6px serif subtitle at 80% ink, two justified 16.3px grey summaries, an underlined author line, a four-cell metric row of serif numerals above short grey labels separated by hairlines, and two pill buttons (ink-filled "View Code", white-wash "Read Paper"). On the right, a white 30px-radius card with a deep warm shadow frames a tall carousel of pipeline figures, with an uppercase caption kicker, a centered caption and dot controls. The "Interactive Examples" section is the centerpiece: a question selector, homework pills, a four-cell metadata strip with hairline dividers, then a side-by-side viewer with the handwritten image in a soft gradient frame on the left and the model transcript (KaTeX, with red-boxed recognition errors or green-boxed expert corrections and a segmented "Gemini raw / Expert rectified" toggle) on the right. Dataset and findings sections follow with serif headings, a rounded figure card, three-column detail lists and numbered insight circles.

## First Viewport

Color share of the 1440×900 first viewport (median-cut quantization of the render): peach cream #f0e2d2 24.6%, cream #f2e9dd 21.1%, grey cream #edebe5 11.0%, card white #faf7f2 10.6%, dusty cream #e3d8d0 10.5%, sand #e9e1d4 10.3%, warm grey #aca5a1 8.1% (text and figure lines), light peach #f7e9da 3.8%. There is no flat white or flat color field; the floor is a soft gradient everywhere.

Anatomy in DOM order (y = top of element box):

1. **Sticky nav** (`nav.top-nav`), y 0, 75px (74px min-height plus a 1px rgba(30,35,40,.08) bottom border), rgba(247,242,232,.82) with `backdrop-filter: blur(18px)`; inner width 1280px.
2. **Brand** (`a.nav-brand`), x 80, y 27, IBM Plex Sans 16px/700, letter-spacing -0.03em, #1e2328.
3. **Nav pills** (`a.nav-link`), y 16, 40px tall, 15.4px/400, padding 10px 12px, 999px radius, 8px gaps; current "A Quick Glance" #1e2328 on rgba(255,255,255,.62); others #66655f. Gap to eyebrow 72px (28px shell padding plus 44px hero padding).
4. **Eyebrow** (`p.eyebrow`), y 147, "ACL 2026 FINDINGS", 13.8px/700 uppercase, letter-spacing 0.16em, #ab5d2b. Gap 14px.
5. **Wordmark** (`h1 span.hero-brand`), y 179, Source Serif 4 61.6px weight 700, line-height 0.95, letter-spacing -4.3px (-0.07em), #1e2328, one line. Gap 18px.
6. **Subtitle** (`span.hero-title`), y 256, two lines, Source Serif 4 26.6px/30.4px weight 700, letter-spacing -0.03em, rgba(30,35,40,.8). Gap 24px.
7. **Summaries** (`p.hero-summary` ×2), y 340 and y 465, 588px (60ch), IBM Plex Sans 16.3px/28.4px #66655f, justified with the last line left. Gap 16px.
8. **Authors** (`p.authors`), y 566, 16.3px #66655f, "Authors:" then names with 1px rgba(30,35,40,.3) bottom borders instead of underlines. Gap about 60px (28px margin plus the metrics' 18px top margin and 12px padding).
9. **Metric row** (`.hero-metrics`, 4 columns, 12px gap), numerals y 654: Source Serif 4 35.2px #1e2328 (1,334 / 29 / 62 / 3.3%), labels 16px/24.8px #66655f below, each cell topped by a 1px rgba(30,35,40,.12) rule. Gap 26px.
10. **Buttons** (`a.primary-link`, `a.secondary-link`), y 797, 46px tall, padding 0 18px, 999px radius, 16px/600: "View Code" #1e2328 fill with #fff8f2 text; "Read Paper" rgba(255,255,255,.62) with a 1px rgba(30,35,40,.12) border and #1e2328 text; 12px gap.
11. **Hero carousel** (`figure.hero-carousel.is-portrait`), x 795, y 147, 520×907, rgba(255,255,255,.96), 30px radius, padding 12px, shadow 0 18px 38px rgba(57,42,26,.1); the slide image (494×638, 18px radius) sits in a 20px-radius frame; caption kicker "RECOGNITION ERRORS AND DOWNSTREAM IMPACT" at y 840, 12.2px/700 uppercase rgba(30,35,40,.58), centered; caption text 14.7px/23.6px #66655f centered, then 10px dots. The card runs past the fold.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Cream Top | #f8efe2 | body linear-gradient start | Page floor near the top |
| Cream | #f7f2e8 | `--bg`, gradient 42% | Page floor; nav base at 82% alpha |
| Cream Bottom | #f3ede3 | body gradient end | Page floor near the bottom |
| Terracotta Glow | #ab5d2b | `--accent`; radial glow at 16% alpha | Eyebrows, insight number text; top-left glow; active pill tint at 10–12% alpha |
| Sage Glow | #43725f | radial glow at 12% alpha | Top-right background glow |
| Ink | #1e2328 | `--ink` | Wordmark, headings, brand, current nav pill, metric numerals, primary button fill; hairlines at 8–14% alpha |
| Muted | #66655f | `--muted` | Summaries, authors, metric labels, nav links, captions, select label |
| Button Text | #fff8f2 | `.primary-link` color | "View Code" label |
| Shadow Brown | #392a1a | `--shadow-card`, `--shadow-soft` at 8–10% alpha | Card and figure shadows |
| Frame Cream | #f4efe6 | `.image-frame` gradient end at 74% alpha | Image and transcript panel gradient |
| Image Shadow | #14181b | `.image-frame img` shadow at 12% alpha | Shadow under the handwritten image |
| Error Red | #b72424 | `.diff-token`, `.line-diff`, `.legend-chip-red` (border and tint) | Recognition-error boxes and rules |
| Error Text | #9d2020 | `.legend-chip-red` | "Red marks" legend chip text |
| Fix Green | #2f8f4d | `.rectified-token`, `.line-rectified`, `.legend-chip-green` | Expert-correction boxes and rules |
| Fix Text | #246d39 | `.legend-chip-green` | Green legend chip text |
| White | #ffffff | surfaces at 54–99% alpha | Carousel card, nav pill wash, secondary button, select, pills, figure card |

## Tokens — Typography

- **Display**: declared `"Source Serif 4", serif` for `h1` and section `h2`s, metric numerals. Rendered: Source Serif 4 600 and 700 (`fonts_loaded`); the metric numerals ask for 400 and are drawn with the nearest loaded face (600). Substitute: Newsreader.
- **Text**: declared `"IBM Plex Sans", sans-serif`. Rendered: IBM Plex Sans 400, 600, 700. Substitute: Public Sans.
- **Math**: KaTeX in the transcript panel.

| Role | Selector | Size / line-height | Weight | Color |
|---|---|---|---|---|
| Wordmark | `.hero-brand` | 61.6px (clamp 2.65rem, 4.7vw, 3.85rem) / 0.95, -0.07em | 700 | #1e2328 |
| Section heading | `.section-heading h2` | 43.2px (clamp 1.9rem, 3vw, 2.95rem) / 1.04, -0.035em | 700 | #1e2328 |
| Metric numeral | `.hero-metrics span` | 35.2px / 1 | 400 requested | #1e2328 |
| Hero subtitle | `.hero-title` | 26.6px (clamp 1.32rem, 1.85vw, 1.9rem) / 1.14, -0.03em | 700 | rgba(30,35,40,.8) |
| Summary, authors, intro | `.hero-summary`, `.authors`, `.intro-copy p` | 16.3px / 1.74 | 400 | #66655f, justified |
| Detail heading | `.detail-list h3` | 16px | 700 | #1e2328 |
| Button | `.primary-link`, `.secondary-link` | 16px | 600 | #fff8f2 / #1e2328 |
| Nav link | `.nav-link` | 15.4px | 400 | #66655f, current #1e2328 |
| Pill | `.homework-pill` | 15.2px | 400 | #66655f, active #1e2328 |
| Caption text | `.hero-caption-text` | 14.7px / 1.6 | 400 | #66655f |
| Eyebrow | `.eyebrow` | 13.8px uppercase, 0.16em | 700 | #ab5d2b |
| Select label, meta label | `.select-label`, `.example-meta strong` | 13.4px / 13.1px uppercase, 0.12em / 0.08em | 700 | #66655f |
| Caption kicker | `.hero-caption-kicker` | 12.2px uppercase, 0.14em | 700 | rgba(30,35,40,.58) |
| Transcript note, chip | `.transcript-note`, `.legend-chip` | 12.2px | 400 / 600 | #66655f / chip colors |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Hero carousel card | 30px | none | 0 18px 38px rgba(57,42,26,.1) |
| Carousel frame | 20px | 1px solid rgba(30,35,40,.05) | none |
| Hero and figure images | 18px | none | none |
| Image frame, transcript body | 28px (22px ≤820px) | none | 0 18px 38px rgba(57,42,26,.1) |
| Handwritten image | 16px | none | 0 18px 32px rgba(20,24,27,.12) |
| Figure card (`.split-figure`) | 28px | none | 0 16px 40px rgba(57,42,26,.08) |
| Buttons, nav pills, homework pills, toggle | 999px | 1px solid rgba(30,35,40,.12) on secondary and pills | none; hover lift 1–2px |
| Select | 16px | 1px solid rgba(30,35,40,.12) | none |
| Diff and rectified tokens | 6px | 1.5px solid red or green at about 50% alpha | none |
| Insight number | 50% (42px circle) | none | none |

`--radius-xl` (36px) and `--radius-lg` (26px) are declared but not used by any rendered element.

## Layout Metrics

- **Shell**: `.page-shell` width `min(100% - 40px, 1280px)`, so x 80–1360 at 1440; padding 28px 0 48px. The nav inner row uses the same width.
- **Hero**: grid `minmax(0, 1.02fr) minmax(360px, 0.98fr)` with a 34px gap (left column about 635px, right about 611px with the 520px card centered); padding 44px 0 24px.
- **Metrics**: 4 equal columns, 12px gap, max-width 680px, margin 18px 0 26px; each cell padding 12px 4px 0 under a hairline.
- **Sections**: padding 56px 0 8px; consecutive sections add an 18px margin and a 1px top line that fades in from transparent to rgba(30,35,40,.14) between 15% and 85%.
- **Explorer**: intro row flex space-between (copy max 68ch, select cluster min 250px); pills 10px gap; meta strip 4 columns, 18px gap, 16px vertical padding between hairlines; viewer grid `0.92fr 1.08fr`, 24px gap; transcript body min-height 420px, max-height min(74vh, 980px), scrolls.
- **Dataset**: intro grid `1.12fr 0.88fr`, 34px gap; detail list 3 columns, 22px gap; figure card padding 18px.
- **Findings**: insight band 3 columns, 26px gap.
- **Footer**: margin-top 36px, padding-top 22px, hairline top.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >1180px | 80px at 1440 (shell 1280px) | 16.3px | 61.6px | as described |
| 821–1180px | 20px | 16.3px | 2.65rem–4.7vw | hero, intro and viewer stack to one column; metrics, details, insights and meta go to 2 columns; carousel frame 520px tall |
| ≤820px | 10px | 16.3px | clamp(2.2rem, 12vw, 3.35rem); subtitle 18.9px | nav stacks brand over links; all grids one column; pills scroll horizontally; carousel frame 400px; section h2 clamp(1.72rem, 8vw, 2.45rem) |

## Components

- **Translucent sticky nav**: 74px, rgba(247,242,232,.82) with blur(18px), 1px ink-8% bottom border; bold brand left; pill links right (padding 10px 12px, 999px radius, #66655f); hover and current state #1e2328 on rgba(255,255,255,.62) with a 1px lift.
- **Serif wordmark hero**: eyebrow (13.8px uppercase terracotta, 0.16em), a one-line 61.6px serif wordmark with -0.07em tracking, a two-line serif subtitle at 80% ink, justified grey summaries capped at 60ch.
- **Border-underlined author links**: inherit #66655f, no text decoration, 1px rgba(30,35,40,.3) bottom border; hover ink.
- **Metric row**: four cells with a 1px top hairline, 35.2px serif numeral, 16px grey label balanced over two or three lines.
- **Pill buttons**: 46px tall, padding 0 18px, 16px/600; primary #1e2328 with #fff8f2 text; secondary rgba(255,255,255,.62) with a 1px ink-12% border; hover lift 2px, 180ms.
- **Slide card carousel**: white card (30px radius, 12px padding, warm shadow) around a 640px-tall frame with cross-fading slides (opacity and scale 0.985 → 1 over 420ms), a hairline, an uppercase caption kicker, centered caption text and 10px dot buttons (ink at 20%, active 72%).
- **Example metadata strip**: four columns between top and bottom hairlines, each with a 13.1px uppercase muted label and a value, separated by 1px ink-8% vertical rules.
- **Side-by-side viewer**: left image frame (28px radius, white-to-cream gradient, warm shadow, 18px padding, image with 16px radius and its own shadow); right transcript body (same frame, 22px padding, scrollable) with KaTeX equations, red boxed tokens and 3px red left rules for errors, green for corrections; a segmented toggle (4px padded white pill, 34px buttons, active tint rgba(171,93,43,.12)); a legend chip ("Red marks") in red.
- **Homework pills and select**: pills padding 10px 14px, 1px ink-12% border, rgba(255,255,255,.54), active on rgba(171,93,43,.1) with a terracotta 30% border; select 48px tall, 16px radius, rgba(255,255,255,.66).
- **Insight item**: hairline top, a 42px circle in rgba(171,93,43,.1) with a bold #ab5d2b number ("01"), then a heading and justified grey text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navigation | yes | sticky translucent nav with pill links |
| Venue | yes | terracotta eyebrow above the title |
| Title, subtitle | yes | serif wordmark and serif subtitle |
| Summary | yes | two justified grey paragraphs |
| Authors | yes | one "Authors:" line with border-underlined names |
| Affiliations | absent from the source | the institution appears inside the summary |
| Stat row | yes | four serif numerals with labels |
| Link buttons | yes | two pills |
| Teaser | yes | slide-card carousel of pipeline figures |
| Interactive example viewer | yes | selector, pills, meta strip, image and transcript |
| Dataset overview | yes | text plus figure card, three-column details |
| Findings | yes | three numbered insights |
| Results table | present but non-standard | the statistics table is an image inside a figure card |
| BibTeX | absent from the source | |
| Footer | yes | hairline and one grey paragraph |

## Adapting to Other Content

- **More authors**: keep the single "Authors:" paragraph with border-underlined names; add superscripts and an affiliation sentence after it in the same 16.3px grey.
- **A results table**: place an HTML table inside a `.split-figure` card (28px radius, rgba(255,255,255,.68), shadow 0 16px 40px rgba(57,42,26,.08)), 15px IBM Plex Sans, uppercase 13px muted headers, 1px ink-12% row rules, best values in #1e2328 700 and the method row tinted rgba(171,93,43,.1).
- **News**: a short list under the eyebrow styled like the metric row: hairline-topped cells with a serif date and a grey line.
- **Long publication lists**: rows with a top hairline, a 16px/700 title and a justified grey description, three per row on desktop like the detail list.
- **More examples**: extend the homework pills and select options; the viewer and meta strip are data-driven and keep their layout.
- **A BibTeX block**: a white 28px-radius card with 18px padding and a monospace 14px #1e2328 `pre`.

## Do's and Don'ts

- Do keep the floor a soft cream gradient with the faint 32px grid; never a flat white page.
- Do use the serif only for the wordmark, subtitle, section headings and numerals.
- Do round every surface generously (16–30px) and shadow it in warm brown, not grey.
- Do mark diffs with outlined, lightly tinted boxes (red for errors, green for corrections).
- Don't use terracotta for body text or large fills; it stays on eyebrows, tints and numbers.
- Don't add borders to cards; shadows and gradients separate them.
- Don't center text blocks; only the carousel caption is centered.

## Surfaces

A cream gradient page (#f8efe2 → #f7f2e8 → #f3ede3) with terracotta and sage glows and a masked graph-paper grid; white surfaces at 54–99% alpha for nav pills, buttons, the carousel card and figure cards; white-to-#f4efe6 gradient frames for the example viewer; hairlines in ink at 5–14% alpha.

## Imagery

Scanned student handwriting (circuit diagrams, KCL equations, matrices) and a busy pipeline figure with speech-bubble panels, red error callouts, robot and student icons; a LaTeX statistics table in the dataset card. Images get 16–18px radii and soft shadows.

## Layout

A 1280px shell: a two-column hero (copy and metrics left, slide card right), then full-width sections whose headings run the shell width, with internal grids for the viewer (0.92 / 1.08), dataset intro (1.12 / 0.88) and three-column lists. Rendered height is about 3,690px at 1440px.

## Agent Prompt Guide

Quick colors: floor #f8efe2 → #f7f2e8 → #f3ede3, ink #1e2328, muted #66655f, terracotta #ab5d2b, button text #fff8f2, shadow rgba(57,42,26,.1), error #b72424, fix #2f8f4d.

1. "Build a hero on a cream gradient (linear-gradient(180deg, #f8efe2, #f7f2e8 42%, #f3ede3) with a radial rgba(171,93,43,.16) glow top-left), 1280px shell, two columns (1.02fr / 0.98fr, 34px gap): left a 13.8px uppercase #ab5d2b eyebrow with 0.16em tracking, a Source Serif 4 61.6px bold #1e2328 wordmark with -0.07em tracking, a 26.6px serif subtitle at rgba(30,35,40,.8), and 16.3px/1.74 justified #66655f summaries capped at 60ch; right a white card with 30px radius, 12px padding and shadow 0 18px 38px rgba(57,42,26,.1) holding a figure carousel with a 12.2px uppercase caption kicker and dot controls."
2. "Add a metric row and buttons: four columns with 12px gaps, each topped by a 1px rgba(30,35,40,.12) rule, a 35.2px Source Serif 4 numeral in #1e2328 and a 16px #66655f label; below, 46px pill buttons with 18px side padding, 16px/600: primary #1e2328 with #fff8f2 text, secondary rgba(255,255,255,.62) with a 1px rgba(30,35,40,.12) border; hover lifts 2px."
3. "Create an example viewer: a 4-column metadata strip between 1px rgba(30,35,40,.12) rules with 13px uppercase #66655f labels; then two panels (0.92fr / 1.08fr, 24px gap), each with 28px radius, linear-gradient(180deg, rgba(255,255,255,.84), rgba(244,239,230,.74)) and shadow 0 18px 38px rgba(57,42,26,.1); left the image with 16px radius, right a scrollable transcript where wrong tokens get a 1.5px rgba(183,36,36,.55) outline with 6px radius and corrected ones a rgba(47,143,77,.48) outline."

## Similar Pages

- Hand-built research microsites with serif display type over warm cream gradients and glassy sticky navs.
- Interactive dataset explorers that pair source images with model outputs and diff highlighting.

## Quick Start

```css
:root {
  --bg: #f7f2e8;
  --bg-gradient: linear-gradient(180deg, #f8efe2 0%, #f7f2e8 42%, #f3ede3 100%);
  --ink: #1e2328;
  --muted: #66655f;
  --accent: #ab5d2b;
  --accent-soft: rgba(171, 93, 43, 0.1);
  --line: rgba(30, 35, 40, 0.12);
  --surface-strong: rgba(255, 255, 255, 0.94);
  --shadow-soft: 0 16px 40px rgba(57, 42, 26, 0.08);
  --shadow-card: 0 18px 38px rgba(57, 42, 26, 0.1);
  --error: rgba(183, 36, 36, 0.55);
  --fix: rgba(47, 143, 77, 0.48);
  --radius-md: 18px;
  --font-sans: "IBM Plex Sans", sans-serif;
  --font-serif: "Source Serif 4", serif;
  --max-width: 1280px;
  --nav-height: 74px;
}
```

## Provenance

- **URL**: https://gt-learning-innovation.github.io/CIRCUIT_EDU_HW_ACL/
- **Paper**: EDU-CIRCUIT-HW: Evaluating Multimodal Large Language Models on Real-World University-Level STEM Student Handwritten Solutions (arXiv 2602.00095), Weiyu Sun et al., Georgia Institute of Technology.
- **Venue**: ACL 2026 Findings.
- **Selection reason**: the arXiv 2602.00095 comment states acceptance at ACL 2026 Findings and links the page. Chosen for the warm cream gradient, the strong serif title, the hero pairing a stat row with a framed phone-style carousel, and the interactive examples section with tabs, a metadata strip and a side-by-side image and transcript.
- **Template credit**: none; hand-written `styles.css`.
- **Evidence used**: `tools/computed_style.py` render at 1440×900 with color share and fonts, the first-viewport screenshot, full-page capture and a 1440×3700 headless capture, `styles.css` and the HTML. Date 2026-10-28.
