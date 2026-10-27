# ContextDialog · Chat-Bubble Transcript — Style Reference

> A voice-assistant transcript laid out like a messaging app.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9 and the stock Nerfies `index.css`, plus inline styles); roles are interpreted from markup and one rendered viewport. Bulma's palette appears in the frequency scan; listed colors are the ones the markup uses.

## Overview

The page is a Nerfies shell (Google Sans title, two dark pill buttons) whose body is a dialogue demo. A powder-blue notification announces the Findings acceptance; an overview pipeline figure follows; then a tabbed set of samples renders each conversation as chat bubbles. User turns sit in grey `#e8e8e8` bubbles, assistant turns in pale cyan `#d1f0f7`, each bubble 15px-rounded and capped at 65% width, with 40px avatar icons and native `<audio>` players inside Bulma boxes. There is no abstract or BibTeX on the page; it works as a listening demo.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Powder Notice | `#aec6cf` | `--notice-bg` | Acceptance notification |
| Notice Ink | `#363636` | `--notice-fg` | Notification text; Bulma heading color |
| User Bubble Grey | `#e8e8e8` | `--bubble-user` | User turns (44 bubbles) |
| Assistant Cyan | `#d1f0f7` | `--bubble-assistant` | Model turns (44 bubbles) |
| Box Light | `#f5f5f5` | `--box-a` | `box has-background-light` audio panels |
| Primary Mint | `#ebfffc` (inferred, Bulma `primary-light`) | `--box-b` | `box has-background-primary-light` audio panels |
| Body Grey | `#4a4a4a` | `--text` | Bulma body text |
| Tab Blue | `#3273dc` | `--tab-active` | Active tab underline and text (Bulma `tabs`) |
| Hairline | `#dbdbdb` | `--border` | Tab rail, card borders |

## Tokens — Typography

- **Display:** Google Sans for title.
- **Body:** Noto Sans.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-1`) | 3rem | 600 | 1.125 |
| Section heading (`title is-3`) | 2rem | 600 | 1.125 |
| Card header title | 1rem | 700 (`has-text-weight-bold`) | 1.5 |
| Bubble text | 1rem | 400 | 1.5 |
| Notification | 1rem | 400 | 1.5 |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Chat bubbles | 15px |
| Link buttons | 290486px pill |
| Notification, box, card | 4px / 6px (Bulma defaults) |
| Avatars | square PNG icons, 40×40 |

Bubble padding 15px; audio boxes padding 20px; audio element margin-bottom 15px. Shadows: Bulma card/box shadow `0 .5em 1em -.125em rgba(10,10,10,.1), 0 0 0 1px rgba(10,10,10,.02)`. Container `is-max-desktop` (960px desktop).

## Components

- **Acceptance notification:** full-width centered, `#aec6cf` background, `#363636` text, link to the Findings volume.
- **Sample tabs:** Bulma `tabs is-centered`, "Sample 1..n", toggling cards.
- **Dialogue card:** `card` with `card-header-title` "Sample n"; `card-content` lists turns.
- **Chat bubble:** `div` with background `#e8e8e8` or `#d1f0f7`, padding 15px, radius 15px, max-width 65%; assistant bubble has margin-right 10px next to its avatar.
- **Audio panel:** Bulma `box` in light grey or primary-light, holding native audio controls for spoken questions and answers.
- **Link buttons:** dark pills with image icons (Hugging Face logo, arXiv PNG at 20px).

## Page Modules

- **Title/author block:** large title; authors are not in the visible header of the rendered viewport.
- **Venue badge:** a powder-blue notification banner instead of a badge.
- **Link buttons:** Dataset (Hugging Face), arXiv.
- **Teaser/method figure:** "Overview of ContextDialog Generation Pipeline" image (`overview.png`, max-width 100%).
- **Results:** none in tables; the "ContextDialog Demo" is the main module, with 12 audio players.
- **Abstract / BibTeX:** absent.
- **Footer:** one line crediting nerfies.github.io.

## Do's and Don'ts

- Do keep user and assistant colors fixed across every sample.
- Do cap bubbles at 65% so the alternating sides read as a conversation.
- Don't put audio inside bubbles; it sits in separate boxes.
- Don't add borders to bubbles; flat fill only.

## Surfaces

White page, one tinted notification, Bulma cards containing flat colored bubbles and light boxes.

## Imagery

One pipeline diagram drawn in matching blue and grey bubble styles, small person and robot avatar icons.

## Layout

960px column; demo cards use `columns is-multiline` with `is-half` and `is-full` columns.

## Agent Prompt Guide

Quick colors: bg `#ffffff`, notice `#aec6cf`, user bubble `#e8e8e8`, assistant bubble `#d1f0f7`, text `#363636`.

1. "Build a chat bubble pair: user bubble `#e8e8e8`, assistant `#d1f0f7`, both padding 15px, radius 15px, max-width 65%, 40px avatar beside each."
2. "Build an acceptance banner: Bulma notification, centered, background `#aec6cf`, text `#363636`, venue name as a link."
3. "Build a sample switcher: centered Bulma tabs 'Sample 1..4' controlling cards with a bold header and audio boxes in `#f5f5f5`."

## Similar Pages

Nerfies; spoken-dialogue demo pages that pair audio players with transcripts.

## Quick Start

```css
:root {
  --bg: #ffffff; --text: #363636;
  --notice-bg: #aec6cf;
  --bubble-user: #e8e8e8; --bubble-assistant: #d1f0f7;
  --box: #f5f5f5;
  --radius-bubble: 15px; --radius-pill: 290486px;
  --font-display: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --max-width: 960px;
}
.bubble { padding: 15px; border-radius: var(--radius-bubble); max-width: 65%; }
```

## Provenance

- **URL:** https://contextdialog.github.io/
- **Paper:** Does Your Voice Assistant Remember? Analyzing Conversational Context Recall and Utilization in Voice Interaction Models (arXiv 2502.19759), Heeseung Kim et al.
- **Venue:** ACL 2025 Findings.
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 Findings and links this page.
- **Template credit:** footer says the template was sourced from github.com/nerfies/nerfies.github.io.
- **Measurement method:** extract_style.py scan, manual reading of inline styles (bubble colors counted 44 each), and one rendered viewport. The primary-light mint is the Bulma 0.9 default for that class (inferred); author list placement was not checked below the first viewport.
