# Amir Bar — Style Reference

> A clean faculty prospectus in Imperial blue: Inter on white, pill links, and paper cards that lift a few pixels when you reach for them.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the page's inline `<style>` block (its own `:root` tokens) and inline script read directly. Inter loads from Google Fonts in 400, 500 and 600 and renders everywhere; bold author names use the 600 face because no 700 is loaded. The stylesheet calls its accent "gold" but sets it to the same Imperial blue #003e74 as the link color, so there is no gold anywhere on the rendered page.

## Overview

A single 800px column on pure white. The header is centred: "Amir Bar" in Inter 44.8px/600 with tight tracking in deep navy #002147, then a two-column profile row with a 230px portrait framed by 4px of white, a 1px #dde3e6 border, 4px corners and a soft navy shadow, beside two 16px bio paragraphs in slate #20313f with Imperial-blue #003e74 links. A row of seven outlined pill links (Email, Twitter, GitHub, Google Scholar, LinkedIn, CV, Bio) closes the header. Sections follow with 27.2px/600 blue headings over a full-width #dde3e6 hairline and a 52×3px blue accent bar at the left. News and talks are disc lists. Publications start with a segmented Selected/All pill toggle and then a stack of white cards with 12px corners: teaser image or autoplay video on the left (about a third of the card), title in blue 600, authors with "Amir Bar" in 600, venue in muted italic, and a one-line summary. Cards rise 3px and gain a blue border on hover; some teasers swap a still for a video on hover.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 82.9% (page), #b8bec1 5.6% and #7d7d7e 2.7% (portrait), #f7f8f9 3.1% and #fcfcfc 1.7% (portrait frame and shadow halo), #dee3e6 3.0% (pill outlines and heading hairlines). Navy text is under 1% each but carries all the hue.

Anatomy in DOM order (desktop 1440px; hero padding 56px 20px 20px, inner column 800px at x=320):

1. **Name** (`.hero h1`, y=56, 76px line box): Inter 44.8px/600, line-height 1.7, letter-spacing -0.896px (-0.02em), #002147, centred. Gap 6px.
2. **Portrait** (`.profile-image img`, x=330, y=138): 230px wide max, padding 4px on #ffffff, 1px #dde3e6 border, radius 4px, shadow 0 4px 14px rgba(0,33,71,0.1); the image column is flex 1 1 30%. Beside it:
3. **Bio** (`.profile-text p`, x=600, y=138, 500px wide): Inter 16px/400, line-height 1.65 (26.4px), #20313f, paragraph margin 7px 0; links #003e74; key phrase "perceive, reason, and act" in 600; a third line "Prospective students:" in 600 with a link. Gap 28px below the row.
4. **Pill links** (`.social-links a`, y=442, 31px tall, centred): seven pills, Inter 14.4px/400 #003e74, padding 6px 14px, 1px #dde3e6, radius 999px, margin 0 10px. Hero ends at y=512. Gap 35px.
5. **News heading** (`h2.section-heading`, y=547): Inter 27.2px/600 #003e74 with hairline and accent bar. Gap 24px.
6. **News list** (`.news-list`, y≈627): disc bullets, Inter 17px/400, line-height 1.6, #20313f, 6px between items; paper names as italic #003e74 links.
7. **Upcoming Talks heading** (y=795) and its list cross the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Imperial Blue | #003e74 | --navy (also --gold) | links, section headings, heading accent bar, pill text, active toggle fill, publication titles, award badges |
| Deep Navy | #002147 | --navy-deep | name (h1), pill hover text, portrait shadow tint |
| Sky Blue | #006eaf | --navy-soft / --gold-light | hero and news link hover, publication card hover border |
| Slate Ink | #20313f | --ink | body text, bio, list items, author lists |
| Muted Slate | #5e7186 | --muted | italic venue line in publication cards |
| Hairline | #dde3e6 | --line | heading underline, card borders, pill borders, portrait border, toggle track border |
| Toggle Track | #e9eef5 | (literal) | Selected/All toggle background |
| Pill Hover | #d4effc | (literal) | social pill hover fill and border |
| Card Shadow | rgba(20,40,70,0.05) | (literal) | resting shadow under publication cards |
| White | #ffffff | --bg / --card | page, hero, cards, portrait mat, active toggle text |

Declared but not visible: `.researchers-section` (#eef3f9 panel with a 3px left bar) is commented out in the markup, and `.coming-soon-badge` (#006eaf) is not used. The `highlighted` class on the Navigation World Models card has no rule, so it looks like every other card.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif (both --serif and --sans) | Inter 400, 500, 600 | Inter Tight |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.hero h1` | 2.8rem = 44.8px / 600 / 1.7, letter-spacing -0.02em, centred | #002147 |
| Section heading | `.section-heading` (h2 and one div) | 1.7rem = 27.2px / 600 / 1.7 | #003e74 |
| Bio | `.hero .profile-text` | 1rem = 16px / 400 / 1.65 | #20313f |
| Body and lists | `body`, `.news-list li`, `.talks-list li` | 17px / 400 / 1.6 (lists), 1.7 (body) | #20313f |
| Pill link | `.hero .social-links a` | 0.9rem = 14.4px / 400 | #003e74 |
| Toggle button | `.pub-toggle-btn` | 0.92rem = 14.72px / 500 | #003e74; active #ffffff |
| Publication title | `.publication-details a strong` | 17px / 600 | #003e74 |
| Own name | `.publication-details strong` | 17px / 600 | #20313f |
| Venue | `.publication-details em` | 17px / 400 italic | #5e7186 |
| Award badge | `.badge` | 17px / 600, bracketed italic text | #003e74 |
| Patents | `.patents-list li` | 16px / 400 / 1.5 | #20313f |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 4px | 1px #dde3e6, 4px white padding | 0 4px 14px rgba(0,33,71,0.1) |
| Social pill | 999px | 1px #dde3e6 | none |
| Toggle track | 999px | 1px #dde3e6 | none |
| Toggle button | 999px | none | none |
| Publication card | 12px | 1px #dde3e6 (hover #006eaf) | 0 1px 3px rgba(20,40,70,0.05); hover 0 10px 24px rgba(0,33,71,0.1) |
| Card media | 8px (overflow hidden) | none | none |
| Section heading | 0 | bottom 1px #dde3e6 plus 52×3px #003e74 bar | none |

## Layout Metrics

- **Column**: `.container` and `.hero-inner` max-width 800px, centred; `.container` padding 12px 20px 20px, so content runs x=320–1120 at 1440.
- **Hero**: padding 56px 20px 20px; profile row is flex-wrap, image column 30%, text column 60% with 20px side padding; social row margin-top 22px.
- **Sections**: margin-bottom 40px; heading margin 22.6px 0 24px, padding-bottom 10px.
- **Publication card**: padding 18px, margin-bottom 18px, flex with 24px gap; media flex 1 1 35% (about 274px of the 762px inner width), details flex 1 1 60%; teaser media uses object-fit contain inside the stretched box.
- **Toggle**: inline-flex, padding 4px, gap 4px, margin-bottom 26px; buttons padding 7px 22px.
- **Page height**: 6,482px at 1440 in Selected mode.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| >768px | auto around 800px, 20px padding | 17px | 44.8px | portrait beside bio; card media left of details |
| ≤768px | 20px | 17px | 44.8px | profile row stacks centred (portrait above bio); cards stack media over details at full width |

## Components

- **Outlined pill link**: Inter 14.4px/400 #003e74, padding 6px 14px, 1px solid #dde3e6, radius 999px, 10px side margins, no icons; hover fill #d4effc, border #d4effc, text #002147, 0.2s.
- **Section heading**: Inter 27.2px/600 #003e74, padding-bottom 10px, full-width 1px #dde3e6 underline and an absolutely positioned 52×3px #003e74 bar at left, bottom -1px.
- **Segmented toggle**: track #e9eef5 with 1px #dde3e6 and 999px radius, 4px padding; buttons transparent, 14.72px/500 #003e74, padding 7px 22px; active button #003e74 fill with #ffffff text. Default is Selected (script hides unselected cards via `body.filter-selected`).
- **Publication card**: #ffffff, 1px #dde3e6, radius 12px, padding 18px, shadow 0 1px 3px rgba(20,40,70,0.05); left media box with 8px radius showing a GIF, still or muted autoplay video; right column with a blue 600 title link, author line (own name 600), italic #5e7186 venue and year, optional bracketed #003e74 award badge and a "Project Page" or "Code" link, then a one-sentence summary paragraph (margin 10px 0). Hover: translateY(-3px), border #006eaf, shadow 0 10px 24px rgba(0,33,71,0.1), 0.25s ease. Cards with `.one`/`.two` media cross-fade from still to video on hover (0.3s).
- **Framed portrait**: 230px max width, 4px white mat, 1px #dde3e6, 4px radius, 0 4px 14px rgba(0,33,71,0.1).

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name and bio | yes | centred 44.8px name, portrait beside two 16px paragraphs |
| Social links | yes | seven outlined pills, text only |
| News | yes | disc list, italic blue paper names |
| Upcoming talks | yes | disc list |
| Publications | yes | Selected/All toggle plus teaser cards |
| Award badges | yes | bracketed italic text in blue 600 inside the venue line |
| Invited talks | yes | long disc list with optional [Recording] links |
| Patents | yes | disc list at 16px/1.5 |
| Collaborators | absent from the source | the styled `.researchers-section` is commented out |
| Navigation bar | absent from the source | — |
| Footer | absent from the source | page ends after Patents |

## Adapting to Other Content

- **Long publication lists**: keep the Selected/All toggle and add `.selected` by title as the script does; every card keeps the same 18px padding so long lists stay even.
- **Papers without a teaser**: keep the media box and show a muted still or the paper's first figure on white; do not collapse the card to text only, or the column rhythm breaks.
- **News with many items**: keep the 17px disc list and add a year heading in the section-heading style only when it exceeds about 10 items.
- **Students or collaborators**: use the already-written `.researchers-section` panel (#eef3f9 is not in the rendered palette, so stay with a white card in the publication-card recipe instead).
- **More links**: add more outlined pills; they wrap and stay centred.

## Do's and Don'ts

- Do keep one hue family: #003e74 for links and headings, #002147 only for the name, #006eaf only on hover.
- Do use 999px pills for links and toggles, 12px cards for papers, 4px for the portrait.
- Do keep weight 600 as the heaviest; Inter 700 is not loaded.
- Don't fill the pills at rest; they are outlined and only fill #d4effc on hover.
- Don't add a navbar or footer; the page is a single column read top to bottom.
- Don't let teasers fill the card; they sit in about a third of it with object-fit contain.

## Surfaces

White page and white cards separated only by #dde3e6 hairlines and very soft navy shadows; the toggle track in #e9eef5 is the only tinted surface.

## Imagery

A colour portrait, then paper teasers: robot and navigation frames, feature-map visualisations, trajectory plots, GIFs and muted autoplay videos. Teasers sit on white inside 8px-rounded boxes.

## Layout

Centred hero, then an 800px column of News, Upcoming Talks, Publications (toggle and cards), Invited Talks and Patents. About 6,482px tall at 1440 in Selected mode.

## Agent Prompt Guide

Quick colors: text #20313f, links and headings #003e74, name #002147, hover #006eaf, muted #5e7186, hairline #dde3e6, toggle track #e9eef5, pill hover #d4effc, page #ffffff.

1. "Build a centred hero: name in Inter 44.8px/600, letter-spacing -0.02em, #002147; below, a flex row with a 230px portrait (4px white padding, 1px solid #dde3e6, 4px radius, box-shadow 0 4px 14px rgba(0,33,71,0.1)) and a 16px/1.65 #20313f bio with #003e74 links; then centred outlined pills in Inter 14.4px #003e74, padding 6px 14px, 1px #dde3e6, radius 999px, hover background #d4effc."
2. "Make a section heading: Inter 27.2px/600 #003e74, padding-bottom 10px, border-bottom 1px solid #dde3e6, and a 52×3px #003e74 bar positioned at left, bottom -1px; margin-bottom 24px."
3. "Create a publication card: #ffffff, 1px solid #dde3e6, radius 12px, padding 18px, gap 24px, box-shadow 0 1px 3px rgba(20,40,70,0.05); left media at 35% with 8px radius and object-fit contain; right column with a #003e74 600 title, authors in #20313f with the owner in 600, italic #5e7186 venue, one-sentence summary; on hover translateY(-3px), border #006eaf, box-shadow 0 10px 24px rgba(0,33,71,0.1)."

## Similar Pages

- Single-column faculty homepages with card-based publication lists and a Selected/All filter.
- Inter-only academic pages that take their accent from a university brand color.

## Quick Start

```css
:root {
  --navy: #003e74;
  --navy-deep: #002147;
  --navy-soft: #006eaf;
  --ink: #20313f;
  --muted: #5e7186;
  --line: #dde3e6;
  --track: #e9eef5;
  --pill-hover: #d4effc;
  --bg: #ffffff;
  --sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
body { font: 400 17px/1.7 var(--sans); color: var(--ink); background: var(--bg); margin: 0; }
.container { max-width: 800px; margin: auto; padding: 12px 20px 20px; }
a { color: var(--navy); text-decoration: none; }
.publication { display: flex; gap: 24px; border: 1px solid var(--line); border-radius: 12px; padding: 18px; margin-bottom: 18px; }
```

## Provenance

- **URL**: https://www.amirbar.net/
- **Person**: Amir Bar (world models, visual prompting).
- **Venue / award**: CVPR 2025 Best Paper Honorable Mention, "Navigation World Models".
- **Selection reason**: award rule (first/last author); the TCPAMI list files it under 2024 by mistake, it is a CVPR 2025 paper. https://tc.computer.org/tcpami/awards/cvpr-paper-awards/
- **Template credit**: none visible; hand-written HTML with an inline stylesheet and filter script.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 and full-page screenshots, and the inline `<style>`, markup and script read directly, on 2026-10-28.
