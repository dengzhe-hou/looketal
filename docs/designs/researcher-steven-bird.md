# Fieldwork Broadsheet — Style Reference

> A field photograph from a village bench, then a newspaper page: one centred name and three plain black columns of work.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and probes of rendered elements. The page is a Squarespace 7.1 site (the Aikuma Project) whose styles live in Squarespace's generated site CSS; values here are taken from the rendered elements rather than the stylesheet. The full-page screenshot was captured with a taller window, so its hero photo is taller than the 594px it renders at 1440×900.

## Overview

A short page, about 2,900px tall at 1440, built from four Squarespace sections. A full-bleed photograph (Steven Bird seated on a bench with a family in a green Amazonian clearing) fills the first 594px, with the Aikuma logo tile at the top left and thin white Poppins nav links at the top right floating over it. Below, on white, the name "Steven Bird" is centred in acumin-pro 47px/500, followed by three equal text columns headed "Research", "Highlights" and "Publications" in acumin-pro 26px/500. Column text is Poppins Light (300) 16px black with bold run-in subheads (Service, Keynotes, Recent, Manuscripts), bullet lists written as "•" characters, plain black underlined links and italic venue names. A pale olive (#f4f6ea) panel then holds three project blurbs in the same three-column rhythm, and the footer continues on the same olive ground. There is no accent color: the photograph supplies all the color.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 32.6% (the section below the photo); greens #628a5f / #2f4b3a / #505b4d / #97b58d together 40.7% (grass and palm foliage); dark tones #151e1e / #242726 / #362c2b together 26.7% (tree trunks, shadows, clothing and the bench).

Anatomy in DOM order:

1. **Header** (`header.header`, fixed, 0–151px, transparent over the photo): logo image 79×79px at (43, 36), a white rounded tile with the Aikuma mark. Nav at the right (x=865–1397, y=60): Home, About Us, Technologies, Language Learning, Get Involved in Poppins 16px/300 #ffffff, about 15px apart, right-aligned.
2. **Hero section** (0–594px): full-bleed image section on a #000000 background layer, image 1440×594px (object-fit cover); section padding-top 151px reserves room for the header. No text over the photo apart from the header.
3. **White section** (594–1975px, background #ffffff): the name block begins 95px into the section.
4. **Name** (y=689, 85px tall): "Steven Bird", acumin-pro 47.104px/500, line-height 1.8 (84.8px), #000000, centred across 1354px. Gap 40px.
5. **Three column titles** (y=814): "Research" (x=76), "Highlights" (x=534), "Publications" (x=992), acumin-pro 26.368px/500, line-height 1.3, #000000, left aligned inside 438px columns with 32.8px side margins.
6. **Column text** (from y=852): Poppins 16px/300, line-height 28.8px, #000000, left aligned; the first paragraph of Research runs below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Black | #000000 | (Squarespace theme text) | name, column titles, all body text, links, run-in subheads; hero background layer under the photo |
| White | #ffffff | (section background) | main three-column section; nav link text over the photo |
| Olive Paper | #f4f6ea | (body and section background) | project panel, footer section, page body behind sections |
| Clay | #e1ccbe | (primary button) | primary button fill (the hidden "Skip to Content" button) |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Headings | acumin-pro (Adobe Fonts) | acumin-pro 500, 500 italic, 700, 700 italic | Archivo |
| Body / nav | Poppins | Poppins 300, 300 italic, 500, 700 | Poppins (Google Fonts) |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | name paragraph (heading style) | acumin-pro 47.104px / 500 / 1.8, centred | #000000 |
| Column title | `h2.list-item-content__title` | acumin-pro 26.368px / 500 / 1.3 | #000000 |
| Project title / footer line | `h4` | acumin-pro 26.368px / 500 / 1.37 | #000000 |
| Body | `.list-item-content__description p` | Poppins 16px / 300 / 1.8 | #000000 |
| Run-in subhead | `p strong` | Poppins 16px / 700 | #000000 |
| Link | `.list-item-content__description a` | Poppins 16px / 300, underlined | #000000 |
| Venue / instrument | `em` | Poppins 16px / 300 italic | #000000 |
| Nav | `.header-nav-item a` | Poppins 16px / 300 | #ffffff |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Logo tile | rounded square inside the 79px image | none | none |
| Columns, panels, photo | 0 | none | none |
| Links | 0 | text underline | none |

The page has no borders, cards or shadows; structure comes from whitespace and the change from white to #f4f6ea.

## Layout Metrics

- **Gutters**: Squarespace site gutter 43.2px (3vw at 1440) on both sides, so content spans x=43–1397 (1354px).
- **Three-column list**: `user-items-list` grid, `grid-template-columns: 437.875px × 3`, gap 20px, padding 0 43.2px; each column's text inset 32.8px (titles and paragraphs run x=76–448, 534–906, 992–1364, 372px wide, with `max-width: 85%` on titles).
- **Hero**: 594px tall at 1440×900 (about 66% of the viewport height), full bleed; header 151px tall, fixed and transparent.
- **Section rhythm**: name at 95px below the photo; column titles 40px below the name; paragraphs 16px apart; section bottom padding 28.8px.
- **Project panel**: section padding 43.2px; olive inset background from x=43 to 1397 (1354×658px); three columns of 406px at x=86, 517, 948; titles 32px above their text.
- **Footer**: full-width #f4f6ea section, 181px tall, with a 26px acumin-pro line at x=43.

| Breakpoint | Gutter | Body size | Name size | Grid change |
|---|---|---|---|---|
| ≥768px | 3vw (43.2px at 1440) | 16px | 47.1px | three equal columns |
| <768px (Squarespace mobile) | 6vw | 16px | scales down with Squarespace's fluid heading sizes | columns stack; nav collapses to a burger menu |

## Components

- **Overlay header**: fixed, transparent, 151px tall; logo tile at left, white 16px/300 Poppins links at right with no underline or background; it sits directly on the photo.
- **Column block** (`.list-item`): acumin-pro 26.4px/500 title, then a description of stacked paragraphs. Each group starts with a bold Poppins 700 run-in label on its own line (Service, Qualifications, Creative Initiatives, Keynotes, Recent, Manuscripts), followed by "•"-prefixed lines in 16px/300 with underlined black links and italic venues.
- **Project panel**: a #f4f6ea block inset by the 43.2px gutter, three columns each with a 26.4px acumin-pro title (32px below) and a Poppins 300 paragraph.
- **Primary button** (theme default, seen on the skip link): #e1ccbe fill, #000000 Poppins 17.7px/500 text, padding 21.3px 35.5px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-bleed photo hero | yes | 594px field photograph, header floating over it |
| Name | yes | centred acumin-pro 47px |
| Research statement and service | yes | first column, run-in bold labels |
| Highlights (initiatives, keynotes) | yes | second column of bullet lines |
| Publications | yes | third column of bullet citations with italic venues |
| Project blurbs | yes | olive panel, three columns |
| Photo of the person as a portrait | present but non-standard | the person appears only in the group fieldwork photo |
| Contact / social links | absent from the source | none besides the footer line |
| Footer | yes | olive section with the project copyright and admin email |

## Adapting to Other Content

- **Long publication lists**: keep the bullet-line format in the third column ("•" + underlined title link + authors + italic venue) at 16px/300, grouped under bold run-in labels by year or type.
- **A results table**: place it full width inside the 1354px content area with no borders except 1px #000000 rules under the header row; 16px/300 Poppins cells, 700 for the header.
- **News**: add a fourth group in the Highlights column with a bold run-in label and dated bullet lines; do not add cards.
- **More projects**: extend the olive panel to more rows of three 406px columns with 26.4px acumin-pro titles.
- **No field photo**: keep the 594px full-bleed hero with any wide documentary photograph; the page relies on it for color.

## Do's and Don'ts

- Do open with a full-bleed documentary photograph and let the header float on it in white.
- Do keep all text black on white or #f4f6ea, with no accent color.
- Do use acumin-pro 500 for the name and column titles and Poppins Light 300 for everything else.
- Do write lists as plain "•" lines with underlined black links.
- Don't add cards, borders or shadows.
- Don't center column text; only the name is centred.
- Don't add color to links; underline is the only link signal.

## Surfaces

Photo hero on a #000000 layer, then a #ffffff section, then a #f4f6ea inset panel and a full-width #f4f6ea footer. Flat throughout.

## Imagery

One wide, candid fieldwork photograph in natural greens and browns, cropped to 1440×594 at the top. The only other image is the small Aikuma logo tile.

## Layout

A photograph band, a centred name, and an editorial three-column text grid across the full 1354px width, like a broadsheet page. The project panel repeats the three-column grid on a tinted ground.

## Agent Prompt Guide

Quick colors: text #000000, page #ffffff, olive panel #f4f6ea, nav over photo #ffffff, button #e1ccbe.

1. "Create a full-bleed hero: a 594px-tall documentary photograph (object-fit cover) on a #000000 layer, with a fixed transparent 151px header on top: a 79px logo tile at (43px, 36px) and right-aligned Poppins 16px/300 #ffffff nav links about 15px apart."
2. "Below on #ffffff, center the name in acumin-pro 47px/500, line-height 1.8, #000000. 40px below, a three-column grid (gap 20px, page gutter 43.2px, text inset 32.8px): each column has an acumin-pro 26.4px/500 title and Poppins 16px/300 text at line-height 1.8 with bold 700 run-in labels and '•' lines whose links are #000000 underlined."
3. "Add a project panel: #f4f6ea background inset by 43.2px, padding 43.2px, three 406px columns each with an acumin-pro 26.4px/500 title, 32px gap, and a Poppins 16px/300 paragraph; follow it with a #f4f6ea footer section."

## Similar Pages

- Squarespace project sites that open with a full-bleed photo and continue with multi-column text blocks.
- Personal pages of field linguists and anthropologists that lead with fieldwork imagery rather than a headshot.

## Quick Start

```css
:root {
  --text: #000000;
  --page: #ffffff;
  --panel: #f4f6ea;
  --button: #e1ccbe;
  --heading: "acumin-pro", "Archivo", sans-serif;
  --body: "Poppins", sans-serif;
  --gutter: 3vw;
}
body { margin: 0; background: var(--panel); color: var(--text); font: 300 16px/1.8 var(--body); }
.name { font: 500 47.104px/1.8 var(--heading); text-align: center; }
.columns { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding: 0 var(--gutter); }
.columns h2 { font: 500 26.368px/1.3 var(--heading); }
.columns a { color: var(--text); text-decoration: underline; }
```

## Provenance

- **URL**: https://www.aikuma.org/steven
- **Person**: Steven Bird (Charles Darwin University); field: language documentation, Indigenous and local languages.
- **Venue / award**: ACL 2024 Outstanding Paper, sole author of "Must NLP be Extractive?".
- **Selection reason**: Rule A; award listed at https://2024.aclweb.org/program/best_papers/ ; homepage from the GitHub stevenbird blog field, and the page lists the paper.
- **Template credit**: Squarespace 7.1 site of the Aikuma Project; fonts acumin-pro (Adobe Fonts) and Poppins.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and full-page screenshots, and element probes of the rendered Squarespace blocks, on 2026-10-28.
