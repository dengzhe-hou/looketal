# FlashAdventure — Style Reference

> An arcade lobby on a pale grey morning: one tomato-red game title, a big cartoon cutscene on the screen, and a shelf of cartridge thumbnails behind boxed tabs.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 and top-of-page tall screenshots, the inline `<style>` block of `index.html` layered on Bulma 0.9.4, and a browser probe at 1440px of the hero lines, abstract, tabs, game grid, boxes, table container, highlight box and BibTeX. Two values are set at render time and differ from the stylesheet: the hero title and author names compute to rgba(0,0,0,0.7) because Bulma's `.hero.is-light .title` and link rules outrank the page's `.title { color: #2c3e50 }`, and game tiles are 184px tall because a script equalises their heights over the declared 180px.

## Overview

A Bulma page in Inter. A minimal centred navbar (home icon, "More Research" dropdown) sits on white above a full-width pale grey (#f8f9fa) hero holding a three-line 48px / 800 title whose first word "FlashAdventure" is tomato red (#e74c3c), a row of 19.2px authors with small red superscripts, bold affiliations, an "Equal contribution" note, a 32px bold black "EMNLP 2025 Main" venue and two charcoal pill buttons. A white band follows with a two-line bold slate tagline and a 16:9 YouTube embed of gameplay. Then alternate white and #f8f9fa sections: an Abstract with justified text beside a shadowed figure, a Game Collection with Bulma boxed tabs over a white grid of game thumbnails, an observation-behaviour gap figure, CUA-as-a-Judge with a Bulma box table, the COAST framework in a shadowed white card of three boxes, results tables in a shadowed container, a purple-gradient "Key Findings" box and a grey BibTeX block. There is no footer.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): hero grey #f8f9fa 54.4%, white #ffffff 31.7% (navbar and tagline band), mid grey #a7a1a2 7.1% (antialiased title and text), #f8f9f7 3.0%, #fbfcfc 2.0%, #f9f9fa 1.1%, #f8f9fb 0.3%, #f6fafd 0.3%. The red "FlashAdventure" and charcoal buttons are too small to form clusters.

Anatomy in DOM order (desktop 1440px; `.container.is-max-widescreen` 1152px at x=144):

1. **Navbar** (`nav.navbar`, 0–52px): white, no border; centred home icon (Font Awesome solid) and "More Research" dropdown link, 16px #4a4a4a, Bulma blue chevron.
2. **Hero** (`section.hero.is-light`, 52–654px): #f8f9fa, `.hero-body` padding 48px 24px.
3. **Title** (`h1.publication-title`, y=100): Inter 48px / 800, line-height 57.6px (1.2), letter-spacing -0.96px (-0.02em), rgba(0,0,0,0.7), centred, three lines (173px). "FlashAdventure" in #e74c3c. Margin-bottom 16px.
4. **Authors** (`.publication-authors`, y=301): margin 24px 0, 19.2px / 500, names rgba(0,0,0,0.7) with 16px right margins; superscripts 12px / 600 #e74c3c with 2px left margin.
5. **Affiliations** (`.affiliation-block`, y=361): 19.2px, `strong` names in #555555, superscript numbers, spans 16px apart horizontally. Margin 8px 0.
6. **Equal contribution** (`.equal-first-author`, y=405): 15.2px / 400 #888888. Margin-top 8px.
7. **Venue** (`.publication-venue`, y=439): "EMNLP 2025 Main", 32px, `strong` 700, #000000, line-height 54.4px.
8. **Buttons** (`.publication-links`, y=526, margin 32px 0): arXiv (Academicons) and Code (GitHub), 40px tall, 12px apart (`.link-block` margin-right 8px plus a space).
9. **Tagline band** (`section.section.has-text-centered`, from y=654, padding 48px 48px 0): two `h2.title.is-4` lines at y=702 and y=753, 24px / 700 #2c3e50, centred. The YouTube embed (1152×648 at y=844) starts just below the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Tomato | #e74c3c | (inline span, `.author-block sup`) | "FlashAdventure" in the title, author superscripts, author-name hover |
| Slate | #2c3e50 | (body color, `.title`) | body base text, tagline, section headings (h2, h3, h4) |
| Hero Ink | rgba(0,0,0,0.7) | Bulma `.hero.is-light .title`, links | hero title, author names |
| Affiliation Grey | #555555 | `.affiliation-block` | affiliation names |
| Note Grey | #888888 | `.equal-first-author` | equal-contribution line |
| Venue Black | #000000 | `.publication-venue` | venue line |
| Text Grey | #444444 | `.content` | abstract and section paragraphs, figure captions inside `.content` |
| Subtitle Grey | #666666 | `.subtitle` | section intro lines ("Our benchmark includes…"), table-container swipe hint |
| Bulma Text | #4a4a4a | Bulma body | navbar links, inactive tabs, Bulma box text |
| Charcoal | #363636 | Bulma `is-dark` | pill buttons, table text |
| Tab Blue | #485fc7 | Bulma 0.9.4 `$link` | active tab label, navbar chevron |
| Hero Grey | #f8f9fa | `.hero.is-light`, inline section style | hero band, Game Collection and CUA-as-a-Judge bands |
| Code Grey | #f5f5f5 | `.bibtex-container` | BibTeX block, swipe-hint strip |
| Paper | #ffffff | (body) | page, navbar, game grid panel, boxes, framework card, active tab |
| Gradient Start | #667eea | `.highlight-box` | left of the Key Findings gradient |
| Gradient End | #764ba2 | `.highlight-box` | right of the Key Findings gradient |
| Charcoal Hover | #2f2f2f | Bulma `.button.is-dark:hover` | button hover fill |
| Tab Border | #dbdbdb | Bulma `.tabs.is-boxed` | active tab border and tab baseline |
| Thumb Placeholder | #f0f0f0 | `.game-item img` | thumbnail background while loading |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Text and headings | 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif | Inter 400, 500, 600, 700, 800 (Google Fonts) | Inter |
| BibTeX | 'Courier New', monospace | Courier New | Courier Prime |
| Icons | Font Awesome 6.4 (solid, brands), Academicons | Font Awesome 6 Free 900, Brands 400, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Paper title | `h1.publication-title` | 3rem = 48px / 800 / 1.2, letter-spacing -0.02em | rgba(0,0,0,0.7); lead word #e74c3c |
| Authors | `.publication-authors` / `.author-block` | 1.2rem = 19.2px / 500 / 1.7 | rgba(0,0,0,0.7) |
| Author marks | `.author-block sup` | 0.75rem = 12px / 600 | #e74c3c |
| Affiliations | `.affiliation-block strong` | 19.2px / 700 | #555555 |
| Venue | `.publication-venue strong` | 2rem = 32px / 700 / 1.7 | #000000 |
| Tagline | `h2.title.is-4` | 24px / 700 / 27px | #2c3e50 |
| Section heading | `h2.title.is-3` | 32px / 700 / 36px, margin-bottom 24px | #2c3e50 |
| Subsection | `h3.title.is-4` | 24px / 700 / 27px | #2c3e50 |
| Box heading | `h4` | 20px / 700 | #2c3e50 |
| Body | `.content p` | 1.05rem = 16.8px / 400 / 1.8 = 30.24px, justified, margin-bottom 16.8px | #444444 |
| Section intro | `.subtitle` | 1.1rem = 17.6px / 400 | #666666 |
| Caption | `figcaption` | 16px (16.8px inside `.content`), centred, bold "Figure N:" lead | #2c3e50 / #444444 |
| Tab label | `.tabs li a` | 16px / 400 | active #485fc7, others #4a4a4a |
| Game title | `.game-item p` | 0.85rem = 13.6px / 400 / 1.3, clamped to 3 lines | #2c3e50 |
| BibTeX | `.bibtex-container` | 13.6px / 1.7 | #2c3e50 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow / background |
|---|---|---|---|
| Pill buttons | 9999px | 1px solid transparent | none; Bulma `is-dark` hover #2f2f2f |
| Abstract figure image | 0 | none | `0 2px 10px rgba(0,0,0,0.1)` |
| Teaser image/video (`.teaser`) | 10px | none | `0 2px 8px rgba(0,0,0,0.1)` (declared for `.teaser`; the YouTube iframe sits in `.video-responsive` without it) |
| Boxed tabs | 4px 4px 0 0 (rendered; declared 6px 6px 0 0 is overridden by Bulma) | active: Bulma 1px #dbdbdb with white fill; inactive: transparent | none |
| Game grid panel | 8px, padding 24px | none | white on the #f8f9fa band |
| Game tile | 8px, padding 8px | none | hover `translateY(-2px)` and `0 4px 12px rgba(0,0,0,0.1)` |
| Game thumbnail | 6px, 60% width, 100px tall, `object-fit: cover` | none | #f0f0f0 placeholder |
| Bulma box | 6px, padding 20px | none | `0 0.5em 1em -0.125em rgba(10,10,10,0.1), 0 0 0 1px rgba(10,10,10,0.02)` (renders 0 8px 16px -2px …) |
| Framework card | 10px, padding 32px | none | `0 2px 10px rgba(0,0,0,0.1)` |
| Table container | 8px | none | `0 2px 4px rgba(0,0,0,0.1)`; swipe hint strip #f5f5f5, radius 0 0 8px 8px |
| Key Findings box | 10px, padding 32px | none | `linear-gradient(135deg, #667eea 0%, #764ba2 100%)` |
| BibTeX block | 8px, padding 16px | none | #f5f5f5 |

## Layout Metrics

- **Container**: `.container.is-max-widescreen` 1152px (x=144 at 1440) in every section.
- **Hero**: `.hero-body` padding 48px 24px; hero 602px tall (y=52 to 654).
- **Sections**: `section.section` padding 48px (Bulma 3rem 3rem at ≥1024px); the tagline section has padding-bottom 0; the video section 16px 48px. Bands alternate white and #f8f9fa (Game Collection, CUA-as-a-Judge).
- **Video**: `.video-responsive` 16:9 (padding-bottom 56.25%), full container width 1152×648.
- **Abstract**: `.abstract-container` flex with 48px gap; text column 585px, figure column 45% = 518px.
- **Game grid**: `repeat(auto-fill, minmax(150px, 1fr))`, gap 16px, padding 24px, margin 32px 0; renders six 170px tiles per row.
- **Framework**: three Bulma columns of boxes inside a 32px-padded white card.
- **Tables**: Bulma `table is-fullwidth is-striped` at 16px, cells padding 8px 12px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px (1440 renders this) | container 1152px | 16.8px | 48px | abstract side by side |
| ≤1200px | container 960px at ≥1024px | 16.8px | 48px | game grid minmax 140px, gap 12.8px, padding 19.2px |
| ≤1024px | — | 16.8px | 48px | abstract stacks; figure below with 32px top margin |
| ≤768px | container padding 0 16px; section padding 32px 0; hero-body 32px 0 | 16px, line-height 1.6 | 28.8px (1.8rem), line-height 1.3 | authors one per line at 16px; affiliations 16px; venue 24px; h2 24px; h3 20px; game grid minmax 120px |

## Components

- **Charcoal pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, #ffffff 16px / 400 Inter, padding 7px 20px, 40px tall, radius 9999px, leading icon in a 24px `.icon` span; hover #2f2f2f.
- **Accent title**: 48px / 800 Inter with -0.02em tracking; only the product name is coloured #e74c3c, the rest stays rgba(0,0,0,0.7).
- **Author row**: inline-block names at 19.2px / 500 with 16px right margins, red 12px / 600 superscripts; hover turns names #e74c3c (0.3s).
- **Boxed tabs** (`.tabs.is-centered.is-boxed`): centred row of Font Awesome icon + label + count, padding 12px 16px; active tab white with Bulma #dbdbdb border and #485fc7 text; inactive #4a4a4a; scrolls horizontally on overflow.
- **Game grid**: white 8px-radius panel, 24px padding, auto-fill tiles (min 150px); each tile has a 60%-wide, 100px-tall cover thumbnail with 6px radius and a centred 13.6px title clamped to three lines; hover lifts 2px with a soft shadow.
- **Bulma box**: white, 6px radius, padding 20px, Bulma two-layer shadow; holds an h4 and a small `table is-fullwidth`.
- **Key Findings box**: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`, white text, padding 32px, radius 10px, h3 24px / 700 white.
- **BibTeX block**: #f5f5f5, radius 8px, padding 16px, Courier New 13.6px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Navbar | yes | centred home icon and "More Research" dropdown |
| Title / authors / affiliations | yes | grey hero, red product name, red superscripts, bold affiliations |
| Venue | yes | 32px bold black line, no badge |
| Link buttons | yes | two charcoal pills |
| Tagline | yes | two bold slate lines in their own band |
| Video | yes | full-width 16:9 YouTube embed |
| Abstract | yes | justified text beside a shadowed overview figure |
| Game collection | yes | boxed tabs and thumbnail grid |
| Method / framework | yes | white card with three Bulma boxes |
| Results tables | yes | striped Bulma tables in a shadowed container |
| Highlight callout | yes | purple gradient Key Findings box |
| BibTeX | yes | grey Courier block |
| Footer | absent from the source | page ends after BibTeX |

## Adapting to Other Content

- **More authors**: keep `author-block` spans inline at 19.2px; they wrap within 1152px. Below 768px they stack one per line.
- **A teaser image instead of video**: use the declared `.teaser` style: full container width, radius 10px, shadow 0 2px 8px rgba(0,0,0,0.1).
- **A results table**: wrap Bulma `table is-fullwidth is-striped` (16px, cells 8px 12px) in the 8px-radius `.table-container` with its 0 2px 4px shadow; bold the best values rather than colouring them.
- **News or updates**: a white Bulma box per item (6px radius, 20px padding) inside a #f8f9fa band, date as a 20px / 700 #2c3e50 h4.
- **More stats or key points**: use the purple gradient box only once per page, for the main findings.

## Do's and Don'ts

- Do colour only the product name in the title #e74c3c; reuse the same red for author marks and hover.
- Do alternate white and #f8f9fa full-width bands between sections.
- Do use Bulma boxed tabs to split a large collection into categories with counts.
- Do keep buttons charcoal and fully rounded.
- Don't add a second accent to the hero; the purple gradient belongs to the Key Findings box only.
- Don't rely on `.title` colour inside the hero; Bulma's is-light rules render it rgba(0,0,0,0.7).
- Don't put borders on the game tiles; separation comes from padding and the hover lift.

## Surfaces

White page and navbar; #f8f9fa hero and alternate bands; white panels (game grid, boxes, framework card) on the grey bands; #f5f5f5 BibTeX; one purple gradient callout. Shadows are soft (2–10px blur, 10% black).

## Imagery

A YouTube gameplay video of a cartoon point-and-click adventure, square-cropped game cover thumbnails in vivid colours, paper figures (a collage of 34 games, a gameplay comparison), and charts. Icons from Font Awesome and Academicons.

## Layout

Centred hero, tagline and full-width video, then 1152px sections alternating white and pale grey; the abstract uses a two-column split, everything else is single column. About 7,300px tall.

## Agent Prompt Guide

Quick colors: accent #e74c3c, slate #2c3e50, hero ink rgba(0,0,0,0.7), text #444444, hero band #f8f9fa, button #363636, tab blue #485fc7, gradient #667eea → #764ba2.

1. "Build a pale grey hero (#f8f9fa, padding 48px 24px, container 1152px, centred): Inter 48px / 800 title, line-height 1.2, letter-spacing -0.02em, colour rgba(0,0,0,0.7), with the product name in #e74c3c; authors 19.2px / 500 with 12px / 600 #e74c3c superscripts; bold #555555 affiliations; a 15.2px #888888 note; a 32px / 700 #000000 venue; charcoal pills (#363636, #ffffff 16px, padding 7px 20px, radius 9999px, 40px tall)."
2. "Make a game collection: Bulma boxed tabs centred above a white panel (radius 8px, padding 24px) with grid repeat(auto-fill, minmax(150px, 1fr)) and 16px gap; tiles padding 8px, radius 8px, thumbnail 60% wide × 100px with 6px radius, title 13.6px #2c3e50 clamped to 3 lines; hover translateY(-2px) and box-shadow 0 4px 12px rgba(0,0,0,0.1)."
3. "Add a findings callout: background linear-gradient(135deg, #667eea 0%, #764ba2 100%), white text, padding 32px, radius 10px, heading 24px / 700."

## Similar Pages

- Bulma project pages that colour only the method name in the title.
- Game and agent benchmarks that present their environment set as a tabbed thumbnail grid.

## Quick Start

```css
:root {
  --accent: #e74c3c;
  --slate: #2c3e50;
  --hero-ink: rgba(0, 0, 0, 0.7);
  --text: #444444;
  --muted: #666666;
  --band: #f8f9fa;
  --code: #f5f5f5;
  --button: #363636;
  --tab-active: #485fc7;
  --grad-a: #667eea;
  --grad-b: #764ba2;
  --font: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --container: 1152px;
  --radius-card: 10px;
  --radius-panel: 8px;
}
```

## Provenance

- **URL**: https://ahnjaewoo.github.io/flashadventure/
- **Paper**: FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games (arXiv 2509.01052), Jaewoo Ahn, Junseo Kim, Heeseung Yun, Jaehyeon Son, Dongmin Park, Jaewoong Cho, Gunhee Kim.
- **Venue**: EMNLP 2025 Main.
- **Selection reason**: the arXiv comment states acceptance at EMNLP 2025 and links this project page.
- **Template credit**: none stated; Bulma 0.9.4 with an inline stylesheet in the Nerfies tradition.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440×900 and tall screenshots, a browser probe at 1440px, and the inline stylesheet and markup of `index.html` read directly, on 2026-10-28.
