# MAD Two-Tone Nerfies — Style Reference

> Two inks for two ideas: sky blue for merging, burnt orange for disentangling, carried from the title words into a hand-drawn robot diagram on an otherwise plain academic page.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, loaded fonts, color share), selector probes of the title spans, buttons, tab matrix, view cards and footer, the 1440×900 and full-page screenshots, and the page's `static/css/index.css`, Bulma 0.9 and `index.html`. The page's stylesheet sets `html { zoom: 0.9 }`, so every rendered size is 90% of the CSS value. This file lists rendered sizes at 1440 first and gives the CSS value in parentheses where it helps (for example, title 43.2px rendered from 48px). Videos in the comparison matrix autoplay, so the screenshot shows single frames.

## Overview

A Nerfies-template page (about 5,660px tall at 90% zoom) on white with Bulma's dark grey text. Its identity comes from two colours that encode the method: "Merging" in #0095ff and "Disentangling" in #b45f06 in the title, matching the blue and orange line-art robots, cameras and frame borders in the teaser diagram ("Merge" on the left, "Disentangle" on the right, split by a dashed grey line). The header is plain: a centred "Home" link with a house icon, a three-line Google Sans title, a bold black "CoRL 2025" line, sky-blue author links, "UC San Diego" and three dark rounded buttons. Below, sections alternate white and #f5f5f5 bands: Abstract, Videos (a rounded card with two rows of tabs over a method-by-camera video matrix), Method with MathJax equations, Setup (two white view cards), Results, Extensions, Citation, and a footer with a blue "Back to Top" button.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white family #ffffff / #fdffff / #fffffd 86.8%; warm brown #675448 3.4% (wood table in the camera thumbnails and dark text); pale blue #c7dae9 3.1% (blue robot fills); grey #a3a7a7 3.1% (thumbnail backgrounds, dashed divider, anti-aliasing); peach #f0e5d9 1.8% (orange robot fills); off-white #f8f9fa 1.8%. The two accent hues are line-thin and blend into these clusters.

Anatomy in DOM order (desktop 1440px, rendered values):

1. **Home link** (`a.navbar-item`, 0–36px, centred at x=678): house icon (Font Awesome `fa-home`) plus "Home", 14.4px (16px) #4a4a4a, padding 7.2px 10.8px. No bar, border or background.
2. **Hero** (`section.hero`, 36–423px): inline `padding-top: 2rem` (28.8px), Bulma 43.2px bottom padding; column 864px (`is-max-desktop`, 960px × 0.9) at x=288.
3. **Title** (`h1.title.is-1.publication-title`, y=65, 146px tall): Google Sans 43.2px (48px) / 600 (synthesized from the 400 face), line-height 48.6px, #363636, three lines forced by `<br>`; "Merging" #0095ff and "Disentangling" #b45f06 via inline spans. Margin-bottom 21.6px.
4. **Venue** (`.publication-venue a`, y=232): "CoRL 2025", 18px (20px) / 700 #000000, links to corl.org; hover #4d4d4d underlined.
5. **Authors** (`.publication-authors a`, y=259): Google Sans 18px #209cee, comma-separated inline blocks; hover underline.
6. **Affiliation** (y=286): "UC San Diego", 18px #4a4a4a.
7. **Buttons** (`.publication-links`, y=328, 32.4px tall): Paper, arXiv, Code; Bulma `is-dark is-rounded`, #363636 fill, #ffffff 14.4px text, radius 290486px, padding 6.3px 18px, icon left. Hero ends at y=423.
8. **Teaser diagram** (`section.hero.teaser img`, y=423, 821×283 at x=310): line-art illustration with "Merge" and "Disentangle" labels in the two accent colours; no frame. The Abstract h2 follows at y=756 (43.2px section padding).

Arithmetic check: 36 + 28.8 ≈ 65; 65 + 146 + 21.6 ≈ 232; 232 + 27 = 259; 259 + 27 = 286; 286 + 27 + 10.8 + 4.5 ≈ 328; 328 + 36 + 4.5 + 10.8 + 43.2 − 10.8 ≈ 423; 423 + 290 = 713; 713 + 43.2 ≈ 756.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Paper | #ffffff | (Bulma `$white`) | page, tab content, active tabs, view cards |
| Title Ink | #363636 | (Bulma `$grey-darker`) | h1, h2 in white sections, `strong`, dark button fill |
| Body Ink | #4a4a4a | (Bulma `$text`) | body text, Home link, affiliation, footer text |
| Merge Blue | #0095ff | (inline span) | "Merging" in the title; blue strokes in the teaser |
| Disentangle Orange | #b45f06 | (inline span) | "Disentangling" in the title; orange strokes in the teaser |
| Author Blue | #209cee | (`hsl(204, 86%, 53%)`) | author links |
| Venue Black | #000000 | (literal) | "CoRL 2025", method names in the matrix |
| Band Grey | #f5f5f5 | (Bulma `hero.is-light`) | Videos, Setup and Extensions bands; comparison card; `pre` |
| Band Title | rgba(0,0,0,0.7) | (Bulma `.hero.is-light .title`) | h2 inside grey bands |
| Tab Bar | #f0f0f0 | (literal, `.tab-header`) | tab strip background |
| Env Tab | #d1e0ff | (literal, `#env-tabs .tab`) | inactive Meta-World / ManiSkill3 tab |
| Task Tab | #f0f3fa | (literal, `.tab`) | inactive task tabs |
| Tab Blue | #3498db | (literal) | active tab underline; Back to Top button |
| Tab Hover Red | #ca1111 | (literal, `.tab:hover`) | inactive tab hover fill, with white text |
| Rule | #dddddd | (literal) | tab strip bottom border, matrix header rule |
| Frame Black | #000000 | (literal, `.video-container`) | 0.25em mat around each matrix video |
| Thumb Grey | #f0f0f0 | (literal, `.view-image-container`) | camera-view image wells |
| View Title | #555555 | (literal) | "First Person", "Third Person A/B" |
| Card Title | #333333 | (literal) | "Meta-World", "ManiSkill3" card titles |
| Footer | #fafafa | (Bulma `.footer`) | footer band |
| Button Hover | #2980b9 | (literal) | Back to Top hover |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Title / authors | 'Google Sans', sans-serif (Google Fonts link, regular only) | Google Sans 400; 600 is synthesized | Product Sans / Outfit |
| Body | 'Noto Sans', sans-serif | Noto Sans 400 | Noto Sans |
| Bold runs | `strong { font-family: 'Lato Bold', sans-serif }` | Lato Bold is never loaded, so bold runs fall back to the system sans (Arial Bold on Windows) | Arial Bold |
| UI (tabs, buttons) | Bulma system stack: BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto… | Segoe UI on Windows | Inter |
| Math | MathJax 3 CHTML | MJXTEX fonts loaded | — |

| Role | Selector | Rendered size (CSS) / weight / line-height | Color |
|---|---|---|---|
| Paper title | `.title.is-1.publication-title` | 43.2px (48px) / 600 / 48.6px | #363636; keywords #0095ff, #b45f06 |
| Venue | `.publication-venue` | 18px (20px) / 700 | #000000 |
| Authors / affiliation | `.publication-authors` (`is-size-5`) | 18px (20px) / 400 | links #209cee, text #4a4a4a |
| Section heading | `h2.title.is-3` | 28.8px (32px) / 600 / 32.4px; padding 3.6px 0 7.2px | #363636; rgba(0,0,0,0.7) in grey bands |
| Body | `body`, `.has-text-justified` | 14.4px (16px) / 400 / 21.6px, justified | #4a4a4a |
| Bold phrase | `strong` | 14.4px / 700 Arial (fallback) | #363636 |
| Button | `.button.is-normal` | 14.4px (16px) / 400 | #ffffff |
| Env / task tab | `.tab` | 12.6px (14px) / 600 (task tabs 500, active 600) | #000000 |
| Matrix header | `.header-cell` | 12.6px (14px) / 700 | rgba(0,0,0,0.7) |
| Method name | `.method-name` | 12.6px (14px) / 900 | #000000 |
| Card title | `.environment-title` | 21.6px (1.5rem) / 600 | #333333 |
| View title | `.view-title` | 14.4px (1rem) / 500 | #555555 |
| Citation | `pre code` | 12.6px (14px) monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px (pill) | 1px transparent | none |
| Comparison card | 1em = 14.4px | none | `0 0 10px rgba(0, 0, 0, 0.1)` |
| Tabs | 1em top corners (12.6px rendered) | active: 3px #3498db bottom (renders 2px) | active hover `0 0 5px rgba(52, 152, 219, 0.3)` |
| Matrix videos | 0 | 0.25em black mat (padding on #000000 container) | none |
| View cards | 8px (7.2px rendered) | none | `0 2px 6px rgba(0, 0, 0, 0.1)` |
| Camera thumbnails | 0 | none | none |
| Back to Top | 4px | none | `0 2px 5px rgba(0, 0, 0, 0.2)` |
| Teaser and result images | 0 | none | none |

## Layout Metrics

- **Zoom**: `html { zoom: 0.9 }`; all values here are rendered unless a CSS value is given in parentheses.
- **Container**: Bulma `.container.is-max-desktop` max-width 960px → 864px rendered, x=288–1152 at 1440. Hero columns centre within it.
- **Hero**: padding 28.8px 21.6px 43.2px (inline 2rem top, Bulma 3rem bottom, 1.5rem sides); rendered 36–423px.
- **Teaser**: `.hero-body` padding 0 21.6px; image 821px wide.
- **Sections**: Bulma `.section` padding 3rem 1.5rem → 43.2px 21.6px. Abstract text sits in `.column.is-four-fifths` (687px rendered); other sections use the full 864px.
- **Video matrix**: card 864px wide; grid columns `100px minmax(0, 2.9fr) 1fr 1fr 1fr` (90, 353, 122, 122, 122px rendered), gap 7.2px; rows 126px (`--row-height: 140px`); tab content padding 13.5px.
- **Setup cards**: two `.environment-views` 419px wide, 27px gap (30px CSS), padding 14.4px; inside, three 121px square thumbnails 13.5px apart.
- **Footer**: Bulma `.footer` padding 43.2px 21.6px 86.4px on #fafafa; "Back to Top" centred with 18px vertical padding around it.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1216px (1440 render) | 21.6px section padding, 864px column | 14.4px | 43.2px | full matrix, two setup cards side by side |
| 1024–1215px | same | 14.4px | 43.2px | container still 960px CSS max |
| 769–1023px | same | 14.4px | 43.2px | container fluid within padding |
| ≤768px | Bulma columns stack | 14.4px | 43.2px | columns stack; the custom grids (matrix, setup row) keep their layout because `index.css` has no media queries |

## Components

- **Two-tone title**: Google Sans 43.2px/600 #363636, three manual lines; key words wrapped in spans coloured #0095ff and #b45f06. The same two colours appear only in the teaser illustration.
- **Dark pill button** (Bulma `.button.is-dark.is-rounded`): #363636 fill, #ffffff 14.4px text, 32.4px tall, padding 6.3px 18px, pill radius, Font Awesome or Academicons icon on the left; 4.5px vertical margin; hover Bulma darkens the fill.
- **Tabbed comparison card** (`.comparison-container`): #f5f5f5 card with radius 14.4px and `0 0 10px rgba(0, 0, 0, 0.1)`; first tab row (environments) inactive #d1e0ff, second row (tasks) inactive #f0f3fa, both on a #f0f0f0 strip with a #dddddd bottom rule; active tab #ffffff with a #3498db underline; inactive hover #ca1111 with white text. Below, a white panel with a bold header row and rows of black-matted videos labelled MAD (Ours), MVD, VIB, Single Camera in 900-weight black.
- **View card** (`.environment-views`): #ffffff, radius 7.2px, `0 2px 6px rgba(0, 0, 0, 0.1)`, padding 14.4px; 21.6px/600 #333333 title, then three square #f0f0f0 wells with view titles in 14.4px/500 #555555.
- **Back to Top button**: #3498db, #ffffff 14.4px, padding 9px 18px, radius 4px, shadow `0 2px 5px rgba(0, 0, 0, 0.2)`; hover #2980b9.
- **Citation**: Bulma `.content pre` on #f5f5f5, padding 15.75px 18.9px, 12.6px monospace.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Home link | yes | single centred icon link, no bar |
| Title / venue / authors | yes | two-tone title, bold black venue, sky-blue author links |
| Link buttons | yes | three dark pills |
| Teaser | yes | custom two-colour merge/disentangle line illustration |
| Abstract | yes | four-fifths column, justified, bold sentence runs |
| Video comparison | yes | tabbed card with a method × camera video matrix |
| Method | yes | justified text with MathJax equations |
| Setup / camera views | yes | two white cards with square view thumbnails on a grey band |
| Results | yes | full-width plot image with a bold-led caption |
| Extensions | yes | white card holding a modality figure on a grey band |
| Citation | yes | grey `pre` block, no copy button |
| Footer | yes | blue Back to Top button and a Nerfies credit line |
| Results table | absent from the source | results are plot images |

## Adapting to Other Content

- **More authors**: keep them in the 18px Google Sans line with `.author-block` inline spans; at 864px it fits about five names per line. Add affiliation markers as superscripts and keep "UC San Diego"-style affiliations on their own 18px line.
- **A results table**: put it inside a white band at the 864px width; header 12.6px/700 rgba(0,0,0,0.7) over a 1px #dddddd rule like `.header-cell`; body 14.4px #4a4a4a; highlight the method's row with the 900-weight black name, not a fill.
- **More comparisons**: add tabs to the existing strips; keep environment tabs #d1e0ff and task tabs #f0f3fa so the two levels stay distinct.
- **Long publication or news lists**: a justified 14.4px list in a white section, items led by bold (#363636) dates, links #209cee.
- **Another concept pair**: reuse the two-tone rule: one word per concept in #0095ff and #b45f06, echoed in the figure strokes.

## Do's and Don'ts

- Do tie the title colours to the figure: #0095ff for one concept, #b45f06 for the other.
- Do alternate white and #f5f5f5 bands for sections.
- Do frame comparison videos in black mats inside one rounded, softly shadowed card.
- Do keep the header bare: a Home link only, no navigation bar.
- Don't introduce the accent colours anywhere outside the title and illustrations; UI blue (#3498db) is reserved for tabs and Back to Top.
- Don't remove the 0.9 zoom without scaling sizes back: the page is designed to read at 90%.
- Don't box the teaser; it sits directly on white.

## Surfaces

White page; #f5f5f5 bands for Videos, Setup and Extensions; a #f5f5f5 rounded comparison card with a white tab panel; white view cards with light shadows; black mats around videos; #fafafa footer.

## Imagery

A custom flat line illustration of a robot arm with cameras, drawn twice in blue and orange with pale fills; camera-view thumbnails of Meta-World and ManiSkill3 scenes (wood tables, red Sawyer arms, grey backgrounds); simulation videos in the matrix; plot images for results and the modality extension.

## Layout

Centred single column (864px rendered) inside alternating full-width bands. Text is justified; headings are centred. The video matrix is the one dense, grid-based element; everything else is stacked.

## Agent Prompt Guide

Quick colors: page #ffffff, band #f5f5f5, title #363636, text #4a4a4a, merge #0095ff, disentangle #b45f06, authors #209cee, tab blue #3498db, tab hover #ca1111, env tab #d1e0ff, task tab #f0f3fa.

1. "Build a centred hero in an 864px column: a 36px-tall 'Home' link with a house icon in 14.4px #4a4a4a; a Google Sans 43.2px/600 #363636 title over three lines with one keyword in #0095ff and another in #b45f06; an 18px/700 #000000 venue line; 18px #209cee author links; three #363636 pill buttons with #ffffff 14.4px text, 32.4px tall, padding 6.3px 18px."
2. "Create a tabbed comparison card: #f5f5f5, radius 14.4px, shadow 0 0 10px rgba(0,0,0,0.1). Two tab rows on a #f0f0f0 strip with a #dddddd bottom rule: inactive environment tabs #d1e0ff, inactive task tabs #f0f3fa, active #ffffff with a #3498db underline, hover #ca1111 with white text; tab text 12.6px/600 #000000 with rounded top corners. Below, a #ffffff panel with a grid of columns 90px / 2.9fr / 1fr / 1fr / 1fr, 7.2px gap, and videos in black mats."
3. "Make view cards: two #ffffff cards side by side, 27px gap, padding 14.4px, radius 7.2px, shadow 0 2px 6px rgba(0,0,0,0.1); title 21.6px/600 #333333; three square #f0f0f0 wells labelled in 14.4px/500 #555555."

## Similar Pages

- Nerfies-template project pages (Bulma, Google Sans titles, dark rounded buttons, alternating light hero bands).
- Visual RL and manipulation pages that use a tabbed method × environment video matrix.

## Quick Start

```css
html { zoom: 0.9; }
:root {
  --paper: #ffffff;
  --band: #f5f5f5;
  --title: #363636;
  --text: #4a4a4a;
  --merge: #0095ff;
  --disentangle: #b45f06;
  --author: #209cee;
  --tab-active: #3498db;
  --tab-hover: #ca1111;
  --tab-env: #d1e0ff;
  --tab-task: #f0f3fa;
  --rule: #dddddd;
  --font-title: 'Google Sans', sans-serif;
  --font-body: 'Noto Sans', sans-serif;
  --column: 960px; /* 864px after zoom */
}
.comparison-container { background: var(--band); border-radius: 1em; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); overflow: hidden; }
```

## Provenance

- **URL**: https://aalmuzairee.github.io/mad/
- **Paper**: Merging and Disentangling Views in Visual Reinforcement Learning for Robotic Manipulation (arXiv 2505.04619), Abdulaziz Almuzairee, Rohan Patil, Dwait Bhatt, Henrik I. Christensen (UC San Diego).
- **Venue**: CoRL 2025.
- **Selection reason**: the arXiv comment states acceptance at CoRL 2025 and links this project page.
- **Template credit**: footer reads "Website template based off Nerfies website" (Bulma 0.9, Font Awesome, Academicons, MathJax 3).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), selector probes at 1440, the 1440×900 and full-page screenshots, and `static/css/index.css` and `index.html` read directly, on 2026-10-28.
