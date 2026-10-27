# Qi Academicpages Typewriter — Style Reference

> A terminal notebook with a playful marker sidebar and oxblood paper titles.

**Theme:** light

Measurements come from the static HTML and the compiled `/assets/css/main.css` (101KB, the academicpages / Minimal Mistakes Sass build plus the author's overrides), with Google Fonts for Open Sans, Roboto and Roboto Mono, and Font Awesome 5. The extractor's text colors `#586e75`, `#2aa198`, `#22b3eb`, `#859900`, `#cb4b16` are Solarized syntax-highlighting rules (`.highlight .kd` etc.) and are excluded. Template greys (`#7a8288`, `#9ba1a6`, `#bdc1c4`, `#f2f3f3`) are kept only where they style visible chrome. Roles are interpreted, not declared. The rendered page was not viewed.

## Overview

Xiangyu Qi's page is the academicpages Jekyll template with three strong personal overrides. First, the main content column is set in `Roboto Mono` at 16px, so all prose reads like a terminal. Second, the template's navigation, sidebar and archive titles use `Comic Sans MS` (17 rules plus 5 more on the sidebar and author name), giving the chrome a handwritten feel. Third, paper titles are Georgia links in oxblood `#8B0000` that hover to `#3a598f`. A white masthead with a 1px `#f2f3f3` bottom border holds the greedy nav. The left sidebar shows a round 175px avatar with 5px padding and a `#f2f3f3` ring, the name "Xiangyu Qi (漆翔宇)", the role (Member of Technical Staff @ OpenAI, Ph.D. from Princeton), location and Follow links. The content shows a short bio, a News list, and a "Selected Research" heading prefixed with a microscope emoji. Each paper has a pinned-location emoji venue link, a trophy-emoji award in a pale yellow `#fff7cd` chip, the author list with the owner's name bold underlined in `#1E90FF`, and raised grey mono buttons (Paper, Code) with a heavy 4px drop shadow that turn orange `#d56e20` on hover.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Page White | `#ffffff` | `--bg` | `html` background, masthead |
| Body Graphite | `#494e52` | `--text` | Template body color |
| Oxblood Title | `#8B0000` | `--paper-title` | Paper title links; button text |
| Dusk Blue | `#3a598f` | `--paper-title-hover` | Paper title hover |
| Ember Orange | `#d56e20` | `--accent` | Content links, button hover fill, "Coverage:" label |
| Owner Blue | `#1E90FF` | `--highlight-name` | Owner's name in author lists, bold underlined |
| Award Butter | `#fff7cd` | `--award-bg` | `.highlight-oral` award chip |
| Button Fog | `#eaeaea` | `--btn-bg` | Content buttons |
| Button Edge | `#000000` | `--btn-border` | 1px button border |
| Template Teal | `#52adc8` | `--link-template` | Template default `a` color, outside `.page__content` |
| Nav Grey | `#7a8288` | `--nav` | Greedy nav links, overflow toggle background |
| Pager Grey | `#9ba1a6` / `#bdc1c4` | `--muted` | Pagination text and borders |
| Hairline | `#f2f3f3` | `--line` | Masthead border, h2 underline, avatar ring |

## Tokens — Typography

- **Content:** `'Roboto Mono', monospace`, 16px, weight 400 (Google Fonts, 100 to 900 loaded).
- **Chrome:** `"Comic Sans MS", sans-serif` / `'Comic Sans MS', 'Comic Sans', cursive` for greedy nav, sidebar, author name, pagination, archive titles and the Selected Research heading. Substitute where Comic Sans is unavailable: `Comic Neue`.
- **Paper titles:** `'Georgia', serif`.
- **Buttons:** `'Consolas', 'Courier New', Courier, monospace`, 14px, 600.
- **Headings (template):** `-apple-system, ".SFNSText-Regular", "San Francisco", Roboto, "Segoe UI", "Helvetica Neue", Arial, sans-serif`, bold, line-height 1.2.
- **Root size:** `html` 16px, 18px at the large breakpoint.

| Role | Size | Weight | Family |
|---|---|---|---|
| h2 section | 1.25em (template, inferred) | bold | system sans; underlined 1px `#f2f3f3` |
| Paper title | inherit (strong) | bold | Georgia |
| Content prose | 16px | 400 | Roboto Mono |
| Author name (sidebar) | 1em | 400 | Comic Sans |
| Nav list | 1.25rem | 400 | Comic Sans |
| Content button | 14px | 600 | Consolas |
| Template button | .75em | bold | system sans |
| Pagination | 14px | bold | Comic Sans |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons | 4px |
| Award chip | 3px |
| Avatar | 50% |
| Pagination links | 0 |

- **Shadows:** content buttons `0 4px 4px rgba(0,0,0,0.6)` (pressed `translateY(2px)`); template `0 1px 1px rgba(0,0,0,0.125)`; linked image hover `0 0 10px rgba(0,0,0,0.25)`.
- **Layout max-width:** masthead and main capped at 1280px (template), content width 925px at large breakpoints; `.page` 83.05% with the sidebar at 15.25%.
- **Paragraph spacing:** `.page__content p` margin 0 0 1.3em.

## Components

- **Masthead / greedy nav.** White, 1px `#f2f3f3` bottom border, Comic Sans links in `#7a8288` with an overflow button in `#7a8288`.
- **Sidebar author card.** 175px round avatar with 5px padding and 1px `#f2f3f3` border, Comic Sans name, bio, Follow list with Font Awesome icons.
- **Paper block.** `.paper-title` Georgia oxblood link, `.paper-subtitle` with 📍 venue link and 🏆 award chip (`#fff7cd`, bold, 2px 6px padding), author paragraph with `.highlight-name`.
- **Content button.** `#eaeaea`, oxblood text, 1px black border, 4px radius, 2px 12px padding, Consolas 14px/600, hard drop shadow; hover `#d56e20` with white text.
- **Coverage row.** 📰 "Coverage:" label in bold `#d56e20`, followed by buttons for press items.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Bio / photo | Yes | Round avatar sidebar, mono bio |
| News | Yes (one live item, older ones commented out) | Bracketed dates in mono |
| Publication list | Selected Research, no thumbnails | Georgia titles, emoji venue and award, raised buttons (Paper, Code) |
| Awards | Inline per paper | Butter chip with trophy emoji |
| Press coverage | Yes | Labelled button row |
| Contact | Sidebar links (Email, Twitter, LinkedIn, GitHub, Scholar) | Font Awesome icons |
| Math rendering | Template includes it | |

## Do's and Don'ts

- Do keep prose in Roboto Mono and paper titles in Georgia oxblood; the contrast is the signature.
- Do give content buttons the hard 4px drop shadow and orange hover.
- Do mark venues, awards and press with the emoji prefixes.
- Don't use the template's teal `#52adc8` inside the content; it is overridden to orange.
- Don't extend Comic Sans into body text; it belongs to navigation and sidebar chrome.

## Surfaces

White page; light grey `#eaeaea` buttons and a butter `#fff7cd` award chip are the only fills.

## Imagery

One avatar. No paper thumbnails, teasers or figures on the home page.

## Layout

academicpages two-column: floated sidebar (about 15%) and content (about 83%) inside a 1280px masthead width; the sidebar stacks above content on narrow screens.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, text `#494e52`, paper title `#8B0000` (hover `#3a598f`), accent `#d56e20`, owner name `#1E90FF`, award `#fff7cd`, button `#eaeaea`.

1. "Render a paper: Georgia bold title link in `#8B0000` (hover `#3a598f`), then a venue line '📍 ICLR, 2025' and a '🏆 Outstanding Paper Award' chip on `#fff7cd` with 3px radius."
2. "Make raised content buttons: `#eaeaea`, 1px black border, 4px radius, Consolas 14px/600, oxblood text, shadow `0 4px 4px rgba(0,0,0,.6)`, hover `#d56e20` with white text."
3. "Set the content column in Roboto Mono 16px on white, with navigation and sidebar labels in Comic Sans."

## Similar Pages

Any academicpages fork (academicpages.github.io); this one is distinguished by the mono body and Comic Sans chrome. The Joshua Ren page in this batch also uses topic-coded publication styling.

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #494e52;
  --paper-title: #8B0000;
  --paper-title-hover: #3a598f;
  --accent: #d56e20;
  --highlight-name: #1E90FF;
  --award-bg: #fff7cd;
  --btn-bg: #eaeaea;
  --line: #f2f3f3;
  --font-content: 'Roboto Mono', monospace;
  --font-chrome: 'Comic Sans MS', 'Comic Neue', cursive;
  --font-title: Georgia, serif;
  --font-btn: Consolas, 'Courier New', monospace;
  --radius-btn: 4px;
}
```

## Provenance

- **URL:** https://xiangyuqi.com/
- **Person:** Xiangyu Qi, AI safety and alignment
- **Venue / award:** ICLR 2025 Outstanding Paper (Safety Alignment Should be Made More Than Just a Few Tokens Deep, first author)
- **Selection reason:** Rule B, first author of an ICLR 2025 Outstanding Paper (https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/); unispac.github.io (GitHub profile link) redirects here.
- **Template credit:** academicpages (Minimal Mistakes fork), identified from `author__avatar`, `greedy-nav`, `page__content` and the outdated-browser notice; no footer credit line.
- **Measurement method:** `extract_style.py` on HTML plus `main.css`, then the custom rules (`.paper-title`, `.highlight-oral`, `.page__content .btn`) were read directly. Template heading sizes and breakpoint widths are inferred from Minimal Mistakes defaults. The rendered page was not viewed.
