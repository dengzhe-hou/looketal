# GAMEBoT · Violet Arcade Gradient — Style Reference

> A tournament bracket printed on a lavender arcade cabinet.

**Theme:** light

Measurements are normalized from static HTML and CSS (Bulma 0.9, a heavily extended `index.css` and a small `bargaining.css`); roles are interpreted from markup and one rendered viewport. Bulma palette colors in the frequency scan are listed only where the page uses them.

## Overview

GAMEBoT starts from Nerfies but repaints it as a game arena. Heroes carry a 135° `#667eea → #764ba2` violet gradient with a faint white dot-grain overlay; a mascot logo with drop shadow sits above the title; the venue is a Bulma `tag is-info is-light` pill. Below, alternating hero bodies switch between white and a `#f8f9fa → #e9ecef` grey gradient, each holding a game task (Othello, Pong, Surround, Checkers, TicTacToe, Connect4...) with rounded, shadowed replay videos. The leaderboard table reuses the violet gradient in its header. The container is widened to 1200px.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Arcade Indigo | `#667eea` | `--grad-start` | Hero and table-header gradient start |
| Cabinet Plum | `#764ba2` | `--grad-end` | Gradient end |
| Pressed Indigo / Plum | `#5a6fd8` / `#6a4190` | `--grad-hover` | Table header hover gradient |
| Paper White | `#ffffff` | `--bg` | Odd hero bodies, cards |
| Cloud Grey | `#f8f9fa` → `#e9ecef` | `--bg-band` | Even hero bodies, last section (gradient) |
| Steel Mist | `#f5f7fa` → `#c3cfe2` | `--bg-light` | `section is-light` gradient |
| Midnight Slate | `#2c3e50` | `--text-heading` | Section titles |
| Slate Grey | `#5a6c7d` | `--text-sub` | Subtitles, line-height 1.7 |
| Divider Fog | `#e0e6ed` | `--border` | Table borders, fading section rules |
| Header Pewter | `#e5e7ea` | `--th` | Plain table header |
| Row Haze | `#e8f4fd` | `--row-hover` | Table row hover |
| Model Cocoa | `#574848` | `--model-name` | Model-name column text |
| Warning Butter | `#ffeaa7` | `--notice-border` | Warning notification border |
| Info Tag | Bulma `is-info is-light` (`#eef6fc` bg, `#1d72aa` text, inferred) | `--venue` | Venue pill |
| Author Sky | `#209cee` | `--link-author` | Author links (`hsl(204,86%,53%)`) |

## Tokens — Typography

- **Display:** Google Sans for title and authors.
- **Body:** Noto Sans. The bargaining SVG widget uses Arial.

| Role | Size | Weight | Line height |
|---|---|---|---|
| Paper title (`title is-2`) | 2.5rem | 600, text-shadow `0 2px 4px rgba(0,0,0,.1)` | 1.125 |
| Task heading (`title is-3`) | 2rem | 600 | 1.125 |
| Game description (`subtitle`) | 1.25rem | 400 | 1.7 |
| Leaderboard header | 1rem uppercase, letter-spacing .5px | 600 | — |
| Body | 1rem | 400 | 1.5 |
| SVG labels | 12–16px | 400–700 | — |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Notification (news) | 15px |
| Leaderboard table | 15px, overflow hidden |
| News cards, warning notice | 12px |
| Replay videos | 12px |
| Link buttons | 290486px pill |

Shadows: notification and table `0 8px 25px rgba(0,0,0,.1)`; video `0 8px 25px rgba(0,0,0,.15)` rising to `0 12px 35px rgba(0,0,0,.2)` on hover; buttons `0 4px 6px rgba(0,0,0,.1)`; logo `drop-shadow(0 10px 20px rgba(0,0,0,.2))`. Max width 1200px.

## Components

- **Gradient hero:** violet gradient, grain overlay at opacity .3, content at z-index 2.
- **Venue pill:** `tag is-medium is-info is-light` "ACL 2025 Main Conference".
- **Dark pill buttons:** `button is-dark is-rounded` with soft shadow and lift on hover.
- **News notification:** `notification is-info is-light`, 15px radius, inner cards with `#e8f4fd` border.
- **Replay video:** 12px radius, deep shadow, captioned with matchup ("gpt-4o (black) vs llama3.1-405b-instruct (white)") and a "Watch Battle Replay" button.
- **Leaderboard:** sortable, gradient header, white uppercase labels, 18px cell padding, `#e0e6ed` row rules.

## Page Modules

- **Title/author block:** mascot logo ("GAMEBOT ARENA"), title, sky-blue authors, affiliations (HKU, Cambridge, PKU).
- **Venue badge:** info-light tag pill.
- **Link buttons:** Paper, Code, arXiv.
- **News:** "🚀 Latest News & Updates" notification.
- **Teaser video:** yes, game replays per task (8–11 videos).
- **Method:** "Introduction" and "Involved Tasks", each task with "Required Abilities" line.
- **Results tables:** 3 tables including the sortable leaderboard.
- **Interactive widget:** SVG bargaining game (`bargaining.css`, proposal colors `#a8d5ff` / `#ffd5a8`).
- **BibTeX:** present.
- **Footer:** Academic Project Page Template credit, CC BY-SA 4.0.

## Do's and Don'ts

- Do apply the same violet gradient to the hero and the table header.
- Do give every video the 12px radius and deep shadow.
- Don't use the gradient for body sections; those alternate white and pale grey.
- Don't recolor author links; they keep Nerfies sky blue.

## Surfaces

Gradient hero, then alternating white and grey-gradient bands, shadowed cards and tables floating on top.

## Imagery

Game-board replay videos, a cartoon robot mascot logo, SVG game widgets.

## Layout

1200px container, task sections with a two-column video row (`is-vcentered`, `is-offset-1`), centered text.

## Agent Prompt Guide

Quick colors: gradient `#667eea → #764ba2`, heading `#2c3e50`, subtext `#5a6c7d`, border `#e0e6ed`, band `#f8f9fa → #e9ecef`.

1. "Build a hero: background `linear-gradient(135deg,#667eea,#764ba2)`, centered logo with drop-shadow, Google Sans 2.5rem title, an `is-info is-light` venue tag, dark pill buttons."
2. "Build a leaderboard: radius 15px, shadow `0 8px 25px rgba(0,0,0,.1)`, header with the violet gradient and white uppercase 600 labels, rows hover `#f8f9fa`."
3. "Build a replay card: video radius 12px, shadow `0 8px 25px rgba(0,0,0,.15)`, caption naming both models, a small dark pill 'Watch Battle Replay'."

## Similar Pages

Nerfies and Academic Project Page Template; PRMBench (also leaderboard-led).

## Quick Start

```css
:root {
  --grad: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --bg: #ffffff; --band: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  --heading: #2c3e50; --sub: #5a6c7d; --border: #e0e6ed;
  --radius-lg: 15px; --radius-md: 12px;
  --shadow-lg: 0 8px 25px rgba(0,0,0,.1);
  --font-display: 'Google Sans', sans-serif; --font-body: 'Noto Sans', sans-serif;
  --max-width: 1200px;
}
```

## Provenance

- **URL:** https://visual-ai.github.io/gamebot/
- **Paper:** GAMEBoT: Transparent Assessment of LLM Reasoning in Games (arXiv 2412.13602), Wenye Lin et al.
- **Venue:** ACL 2025 (main conference).
- **Selection reason:** the arXiv comment states acceptance at ACL 2025 and the abstract links this page.
- **Template credit:** footer credits the Academic Project Page Template, adopted from Nerfies.
- **Measurement method:** extract_style.py scan, manual reading of `index.css` (about 13.7 KB of overrides) and `bargaining.css`, one rendered viewport. In the render the top band looked pale lavender rather than saturated violet; which layer softens it was not traced. The info-tag colors are Bulma 0.9 defaults (inferred).
