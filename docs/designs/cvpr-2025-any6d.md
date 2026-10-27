# Any6D Style Reference

> A Google Doc pinned to a personal site, blue links in Lato bold.

**Theme:** light

Measurements come from the rendered Google Sites page (the vanity URL redirects there), its inline styles, and computed styles plus one reduced screenshot in a browser tab. Google Sites ships a large Material 3 chrome stylesheet; only values that apply to visible page content are listed. Values are normalized to hex; roles are interpreted.

## Overview

Any6D is a project subpage of the first author's Google Sites homepage, not a static GitHub page. It keeps the site's top bar (name "Taeyeop Lee" left, tagline right) and then lays the paper out like a well-formatted document: a centred Lato 900 title, "CVPR 2025" in bold, a single line of author names in Google-Docs link blue (#1155cc, bold) with superscript affiliations, and bracketed text links "[Paper] [Code]" instead of buttons. Sections (Abstract, Method, Experiments, BibTeX, Contact) are plain headings over full-width figures. All styling comes from the Sites theme and from text formatting applied in the editor.

## Tokens · Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Docs Link Blue | #1155cc | inline color | Author names, bracketed Paper/Code links, superscripts |
| Ink Black | #000000 | theme heading colour (rgba(0,0,0,1)) | Title, headings |
| Body Charcoal | #212121 | theme text rgba(33,33,33,1) | Paragraph text |
| Header Navy | #0b5394 | inline color | Site name in the top bar |
| Cornflower | #3c78d8 | inline color | One author-link variant |
| Arrow Red | #ff0000 | inline color | A single bold arrow glyph |
| Affiliation Grey | #4a4a4a | inline color | One superscript affiliation |
| Code Wash | rgba(0,0,0,0.059) | inline background | BibTeX block background |
| Page White | #ffffff | theme background rgba(255,255,255,1) | Page |
| Divider Grey | rgba(211,211,211,1) | theme | Theme dividers |

Material 3 colours in the stylesheet (#0b57d0, #c2e7ff, #1f1f1f and the --ws-sys-color-* set) belong to Google Sites' own controls and are not part of the page design.

## Tokens · Typography

- **Content**: Lato (Google Fonts, 400/400 italic/700/900), fallback Arial.
- **Site chrome**: Google Sans and Roboto (loaded by Sites).
- **Code**: Source Code Pro / Roboto Mono available from Sites; BibTeX appears as a Sites code block.
- **Responsive title classes**: Sites scales headings by breakpoint (for example 24pt to 32pt and 37pt to 55pt classes).

| Role | Size (measured) | Weight | Color |
|---|---|---|---|
| Paper title (h1) | 29.3px | 900 | #000000 |
| Venue line "CVPR 2025" | about 24px (inferred, h2-like) | 700 | #000000 |
| Section heading (h2) | 24px | 700 | #000000 |
| Author links | 17.3px | 700 | #1155cc |
| Affiliation superscripts | 9pt | 700 or 400 | #1155cc / #4a4a4a |
| Body paragraph | 16px | 400 | #212121, line-height 1.38 in code block |

## Tokens · Spacing & Shapes

| Element | Radius |
|---|---|
| Images | 0 |
| Code block | 0 (border-left/right 0.75pt translucent white) |
| Sites chrome controls | 4px, 8px, 9999px (not page content) |

- **Shadows**: none on content; Sites chrome shadows (`0 1px 3px rgba(60,64,67,.3) …`) only on its menus.
- **Layout**: Google Sites single-section layout with a centred content column; figures shown at full column width. Exact column width not measured (inferred about 1,000 to 1,280px from Sites defaults).

## Components

- **Site header**: top bar with "TAEYEOP LEE" (uppercase in render) and tagline "Making the World a Better Place" with a globe emoji.
- **Title block**: centred Lato 900 title, bold venue line.
- **Author line**: one row of blue bold names with superscripts, then "1 KAIST 2 NVIDIA".
- **Bracket links**: "[Paper]" and "[Code]" as bold blue text links.
- **Figure**: full-width image (teaser screenshot with objects and pose overlays).
- **BibTeX**: Sites code block on rgba(0,0,0,.059).
- **Contact**: closing section with author contact.

## Page Modules

- **Title/author block**: title, CVPR 2025, six authors, KAIST and NVIDIA.
- **Link "buttons"**: bracketed text links Paper and Code (no arXiv button, no data link).
- **Teaser figure**: wide qualitative image.
- **Abstract**.
- **Method figure**.
- **Experiments**: result figures (images; no HTML table).
- **BibTeX**.
- **Contact**.
- **Absent**: video, carousel, slider, 3D, demo.

## Do's and Don'ts

- Do keep the document voice: text links in brackets, bold blue names, no buttons.
- Do use one link colour (#1155cc) consistently.
- Don't expect CSS-level control; changes go through the Google Sites editor and theme.
- Don't mix in stray accent colours (red arrow, second blue) that the editor leaves behind.

## Surfaces

White page, no bands or cards; a faint grey wash for the BibTeX block.

## Imagery

Tabletop object photos with pose overlays, method diagram, benchmark figures.

## Layout

Single centred column under the site header. Rendered height about 4,800px.

## Agent Prompt Guide

Quick colors: links #1155cc, headings #000000, body #212121, code wash rgba(0,0,0,.059), page #ffffff.

1. "Make a document-style header: centred Lato 900 title at about 29px in black, a bold 'CVPR 2025' line, then authors as bold Lato links in #1155cc with superscript affiliation numbers."
2. "Instead of buttons, add bracketed bold links '[Paper] [Code]' in #1155cc, centred."
3. "Add a BibTeX block with background rgba(0,0,0,.059), monospace text, no radius, line-height 1.38."

## Similar Pages

- Other Google Sites project subpages of researcher homepages.
- Personal-site project pages that use bracketed text links.

## Quick Start

```css
:root {
  --link: #1155cc;
  --heading: #000000;
  --text: #212121;
  --page: #ffffff;
  --code-wash: rgba(0, 0, 0, 0.059);
  --site-name: #0b5394;
  --font-content: 'Lato', Arial, sans-serif;
  --font-chrome: 'Google Sans', Roboto, sans-serif;
}
```

## Provenance

- **URL**: https://taeyeop.com/any6d (redirects to https://sites.google.com/view/taeyeop-lee/any6d)
- **Paper**: Any6D: Model-free 6D Pose Estimation of Novel Objects (arXiv 2503.18673), Taeyeop Lee et al.
- **Venue**: CVPR 2025.
- **Selection reason**: the arXiv comment states CVPR 2025 acceptance and links this page.
- **Template credit**: Google Sites (new Sites) theme; no explicit credit.
- **Measurement method**: extract_style.py followed the redirect and parsed the Sites HTML; colour frequencies were dominated by Google Sites' Material 3 chrome, so roles were assigned only to inline content styles. Computed styles and one reduced screenshot in a browser tab on 2026-10-27.
