# Research Card Grid — Style Reference

> A product launch page for papers: white cards with 16:9 teasers, pastel topic chips and screenshots of the internet reacting.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, first-viewport anatomy, color share), the 1440×900 and full-page screenshots, and the single inline `<style>` block and markup read directly. No web fonts load (`fonts_loaded` is empty): the `system-ui` stack renders as Segoe UI on the capture machine and as SF Pro on macOS.

## Overview

A white page with near-black #111111 text in a system sans. The top is a two-column intro: a 320px square portrait with 22px rounded corners on the left, and on the right a 38.4px bold name, four short paragraphs whose links are the same #111111 with light #cccccc underlines, and a row of plain grey #555555 text links (X, GitHub, Google Scholar, CV, Email). Below, "Select AI research" introduces a two-column grid of white cards with 1px #eeeeee borders and 16px radius. Each card stacks a 16:9 preview (screenshot, YouTube still or logo) with a white "▶ Watch" or "▶ Technical Report" pill in the lower-left, a bold title, pastel topic chips (green posttraining, purple reasoning, blue pretraining, orange embedding, grey scaling-laws), a grey venue line, a "TL;DR:" sentence, small PDF / Code / Video links, and at the bottom a 190px-tall cropped screenshot of a reaction tweet with an "N more reactions" button. Contact and Other follow as plain paragraphs with bold run-in labels.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 63.7% (plus #f9fffc 2.4%, #fffffe 0.8%); dark preview fills #201e19 9.3% and #100f0d 4.6% (the Cursor logo card and the s1 talk still); light grey #ececec 7.8% (card borders, portrait sky and building); mid greys #b6b2ae 6.3% and #645744 5.1% (portrait stonework and hair).

Anatomy in DOM order (desktop 1440px; `main` 1180px at x=130 with 72px side padding, content 1036px at x=202):

1. **Portrait** (`.avatar img`, y=72, 320×320): square photo, radius 22px, `object-fit: cover`, #f3f3f3 placeholder. Sits beside the text (32px column gap).
2. **Name** (`h1`, x=554, y=72): 38.4px / 700 / 43px, letter-spacing -0.77px, #111111, left. Gap 16px.
3. **Bio paragraphs** (`.top p`, y=131, 196, 287, 378): 16px / 400 / 26.4px, #111111, max-width 76ch (655.5px), 12px apart; inline links #111111 with #cccccc underlines 3px below. Gap 24px.
4. **Link row** (`.icons a`, y=429): X, GitHub, Google Scholar, CV, Email; 15.2px #555555, no underline, 20px apart. Gap 40px plus 8px section margin.
5. **Section heading** (`h2`, y=502): "Select AI research", 21.6px / 700, letter-spacing -0.32px, #111111. Gap 18px.
6. **Card row** (`.paper`, y=546, two cards 503px wide, 30px gap): previews 461×259 at y=567 with the white play pill; titles at y=838 (16.8px / 700); chips at y=870. The fold cuts through the chip row.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Ink | #111111 | `--text` | name, body, headings, card titles, inline links, hover color |
| White | #ffffff | `--bg`, `--card` | page and card background |
| Muted | #666666 | `--muted` | card venue line (`.meta`) |
| Soft | #888888 | `--soft` | "N more reactions" and "Show more research" buttons |
| Link Grey | #555555 | (literal) | social link row, card link row, neutral chip text |
| Underline Grey | #cccccc | (literal) | resting underline of all links |
| Border | #eeeeee | `--border` | card border, preview placeholder |
| Subtle | #f8f8f8 | `--subtle` | tweet screenshot frame |
| Portrait Placeholder | #f3f3f3 | (literal) | avatar background before load |
| Posttraining chip | #f0fdf4 / #dcfce7 / #166534 | `.tag.posttraining` | background / border / text |
| Reasoning chip | #fbf7ff / #f3e8ff / #6b21a8 | `.tag.reasoning` | background / border / text |
| Pretraining chip | #f0f4ff / #dbeafe / #1e40af | `.tag.pretraining` | background / border / text |
| Embedding chip | #fff7ed / #ffedd5 / #9a3412 | `.tag.embedding` | background / border / text |
| Scaling-laws chip | #f3f4f6 / #e5e7eb / #374151 | `.tag.scaling-laws` | background / border / text |
| Play Pill | rgba(255,255,255,0.94) | (literal) | "Watch" / "Technical Report" pill on previews |
| Preview Scrim | rgba(0,0,0,0.22) to transparent | `.preview::after` | bottom-up gradient over every preview |
| Dialog Grey | #f4f4f5 | (literal) | reactions dialog body and close button |
| Dialog Rule | #ebebeb | (literal) | 1px rule under the reactions dialog header |
| Default Chip Border | #e0e0e0 | `.tag` | base chip border before a topic class overrides it |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif | none loaded; Segoe UI on Windows, SF Pro on macOS | Inter |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Body | `body` | 16px / 400 / 1.65 (26.4px) | #111111 |
| Name | `h1` | clamp(2rem, 4vw, 2.4rem) = 38.4px / 700 / 1.12, letter-spacing -0.02em | #111111 |
| Section heading | `h2` | 1.35rem = 21.6px / 700 / 1.2, letter-spacing -0.015em | #111111 |
| Card title | `.title` | 1.05rem = 16.8px / 700 / 1.35, letter-spacing -0.01em | #111111 |
| Venue line | `.meta` | 0.85rem = 13.6px / 400 | #666666 |
| TL;DR | `.tldr` | 0.95rem = 15.2px / 400, "TL;DR:" in `<b>` | #111111 |
| Card links | `.links a` | 0.9rem = 14.4px / 500 | #555555 |
| Chip | `.tag` | 0.75rem = 12px / 500 / 1, letter-spacing -0.01em | per topic |
| Play pill | `.play` | 0.82rem = 13.12px / 500 | #111111 |
| Social links | `.icons a` | 0.95rem = 15.2px / 400 | #555555 |
| Reaction button | `.tweet-btn` | 0.9rem = 14.4px | #888888 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 22px (18px ≤700px) | none | none |
| Card (`.paper`) | 16px (14px ≤700px) | 1px solid #eeeeee | 0 1px 2px rgba(0,0,0,0.02) |
| Preview | 12px | none | 0 2px 5px rgba(0,0,0,0.05) |
| Play pill | 999px | none | none |
| Topic chip | 6px | 1px solid (per topic) | none |
| Tweet screenshot | 12px | 1px solid rgba(0,0,0,0.08) | 0 2px 6px rgba(0,0,0,0.04); hover 0 8px 22px rgba(0,0,0,0.08) |
| Reactions dialog | 18px | none | 0 24px 80px rgba(40,18,18,0.28) |
| Focus ring | 4px | 2px solid #111111, offset 3px | none |

## Layout Metrics

- **Container**: `main { width: min(1180px, 100%); padding: 72px clamp(20px, 6vw, 72px) 96px }`; at 1440 the content is 1036px wide at x=202.
- **Intro**: grid `320px minmax(0, 1fr)`, gap 32px, `align-items: start`; paragraphs max 76ch with 12px bottom margins; link row margin 24px 0 40px.
- **Research grid**: one column below 900px, `repeat(2, minmax(0, 1fr))` from 900px, gap 30px; cards stretch to equal height with the tweet pinned to the bottom (`margin-top: auto`, 16px top padding).
- **Card**: padding 20px; preview 16:9, 12px below it; title margin 0 0 8px; chips margin 2px 0 8px with 6px gaps; meta 10px below; TL;DR 12px below.
- **Tweet frame**: fixed 190px tall, image `object-fit: cover` anchored top.
- **Show more**: only four cards visible until "Show more research" adds the `expanded` class.
- **Section rhythm**: `h2` margin 44px 0 18px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1200px | (100% − 1180px)/2 + 72px | 16px | 38.4px | two-column cards |
| 900–1199px | 6vw (54–72px) | 16px | 36–38.4px (4vw, capped from 960px) | two-column cards |
| 701–899px | 6vw (42–54px) | 16px | 32–36px | one-column cards |
| ≤700px | 6vw, min 20px; top padding 44px | 16px | 32px | intro stacks; avatar 190px radius 18px; cards padding 16px; tweets auto height, max 220px |

## Components

- **Research card**: white, 1px #eeeeee border, 16px radius, 20px padding, almost invisible 0 1px 2px rgba(0,0,0,0.02) shadow; content stacks preview, title, chips, venue, TL;DR, links, reaction.
- **Preview**: 16:9 link, 12px radius, #eeeeee placeholder, soft 0 2px 5px shadow, images slightly desaturated (`saturate(.95) contrast(.95)`), a bottom-up black 22% gradient overlay; hover scales the image to 1.03 over 0.3s (`.preview--zoom` starts at 1.12 and goes to 1.15).
- **Play pill**: absolute 10px from the bottom-left, rgba(255,255,255,0.94), fully round, padding 7px 9px, 14px filled play triangle (inline SVG) on the left, label 13.12px weight 500.
- **Topic chip**: 12px weight 500, padding 3px 8px, radius 6px, 1px border, pastel background and dark text per topic; 6px apart.
- **Reaction frame**: 190px crop of a tweet screenshot, 12px radius, 1px rgba(0,0,0,0.08) border, #f8f8f8 behind; hover deepens the shadow to 0 8px 22px rgba(0,0,0,0.08). Under it a text button "N more reactions" (14.4px #888888, underlines and turns #111111 on hover) that opens a 520px native `<dialog>` with an 18px radius, white header with a 1px #ebebeb rule, #f4f4f5 body and a blurred rgba(0,0,0,0.45) backdrop.
- **Links**: no colour; #111111 text with #cccccc underlines offset 3px that turn #111111 on hover.
- **Run-in paragraphs** (Contact, Other): `<b>Label:</b>` then 16px text.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Portrait | yes | 320px square, 22px radius |
| Bio with links | yes | four 16px paragraphs |
| Social links | yes | plain grey text row, no icons |
| Navigation bar | absent from the source | none |
| Publications | yes | card grid with previews, chips, TL;DR, links |
| Social proof | yes | tweet screenshot per card plus a reactions dialog |
| Awards | present but non-standard | inline in the bio and in card venue lines ("NeurIPS 2023 · Outstanding Paper Runner Up Award") |
| News | absent from the source | none |
| Contact | yes | run-in bold labels and an email link |
| Personal / Other | yes | Health, Languages, Arts paragraphs |
| Footer | absent from the source | page ends after Other |

## Adapting to Other Content

- **Long publication lists**: keep four to six featured cards, then a compact list below in the same type: 16.8px bold title, 13.6px #666666 venue, 14.4px #555555 links, no preview.
- **Papers without media**: use the #eeeeee placeholder with a centred 16.8px title or a cropped figure; keep the 16:9 slot so rows align.
- **New topics**: add a chip class with a 50-level pastel background, a 100-level border and a 800-level text color from the same Tailwind-like ramp.
- **News**: plain lines with a #666666 13.6px date before 16px text; no cards.
- **Talks**: cards with a YouTube still and the "▶ Watch" pill.

## Do's and Don'ts

- Do give each card a 16:9 preview with the white play pill and a one-line TL;DR.
- Do keep links uncoloured with light #cccccc underlines.
- Do keep chips pastel, small and lowercase.
- Don't add brand colours to headings or buttons; colour lives only in chips and imagery.
- Don't let card heights drift; pin the reaction to the bottom.
- Don't use heavy shadows; the strongest resting shadow is 0 2px 6px at 4%.

## Surfaces

White page and white cards, separated by #eeeeee hairlines; #f8f8f8 behind tweet screenshots; #eeeeee preview placeholders; dark imagery inside the previews provides contrast.

## Imagery

A casual outdoor portrait in front of Stanford's sandstone arcade; card previews mix a Cursor logo on charcoal, talk-recording stills, a scaling-law figure and an MTEB title slide; black-mode tweet screenshots (Elon Musk, Ethan Mollick, Sundar Pichai and others) as social proof.

## Layout

Intro (portrait and bio); Select AI research (four cards, "Show more research"); Contact; Other. About 2,735px tall at 1440 wide.

## Agent Prompt Guide

Quick colors: text #111111, background #ffffff, muted #666666, soft #888888, link row #555555, underline #cccccc, card border #eeeeee, tweet frame #f8f8f8; chips posttraining #f0fdf4/#dcfce7/#166534, reasoning #fbf7ff/#f3e8ff/#6b21a8, pretraining #f0f4ff/#dbeafe/#1e40af, embedding #fff7ed/#ffedd5/#9a3412.

1. "Build an intro grid in a 1180px main with 72px side padding: a 320px square portrait with 22px radius on the left, 32px gap, then a system-ui 38.4px bold #111111 name (letter-spacing -0.02em), 16px/1.65 paragraphs with #111111 links underlined in #cccccc offset 3px, and a row of 15.2px #555555 text links 20px apart."
2. "Make a two-column card grid with 30px gaps: white cards with 1px #eeeeee border, 16px radius, 20px padding; inside, a 16:9 preview with 12px radius and a 0 2px 5px rgba(0,0,0,0.05) shadow, a white rgba(255,255,255,0.94) pill with a play icon and 13.12px label 10px from the bottom-left; then a 16.8px bold title, 12px pastel chips with 6px radius, a 13.6px #666666 venue line, a 15.2px 'TL;DR:' sentence and 14.4px weight-500 #555555 links."
3. "Pin a 190px-tall cropped tweet screenshot to the bottom of each card: 12px radius, 1px rgba(0,0,0,0.08) border, #f8f8f8 background, shadow 0 2px 6px rgba(0,0,0,0.04) growing to 0 8px 22px rgba(0,0,0,0.08) on hover; below it a 14.4px #888888 text button 'N more reactions'."

## Similar Pages

- Startup-style personal sites that present papers like product cards.
- Researcher pages with tweet embeds or screenshots as social proof.

## Quick Start

```css
:root {
  --text: #111111;
  --muted: #666666;
  --soft: #888888;
  --border: #eeeeee;
  --card: #ffffff;
  --bg: #ffffff;
  --subtle: #f8f8f8;
  --shadow: 0 2px 6px rgba(0,0,0,.04);
  --shadow-hover: 0 8px 22px rgba(0,0,0,.08);
}
body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; color: var(--text); background: var(--bg); line-height: 1.65; }
main { width: min(1180px, 100%); margin: 0 auto; padding: 72px clamp(20px, 6vw, 72px) 96px; }
a { color: inherit; text-decoration-color: #cccccc; text-underline-offset: 3px; }
.papers { display: grid; gap: 30px; }
@media (min-width: 900px) { .papers { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.paper { padding: 20px; border: 1px solid var(--border); border-radius: 16px; background: var(--card); }
.preview { aspect-ratio: 16/9; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,.05); }
.tag { padding: 3px 8px; border-radius: 6px; font-size: .75rem; font-weight: 500; border: 1px solid #e0e0e0; }
```

## Provenance

- **URL**: https://muennighoff.com/
- **Person**: Niklas Muennighoff, large language models.
- **Award**: NeurIPS 2023 Outstanding Paper Runner-up, "Scaling Data-Constrained Language Models" (first author). https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/
- **Selection reason**: rule B (first author); muennighoff.github.io, linked from his GitHub, redirects here. Chosen for the media card grid with teaser images, TL;DR lines and embedded social proof.
- **Template credit**: none stated; single hand-written HTML file with inline CSS and JS.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, empty fonts_loaded, color share), the 1440×900 and full-page screenshots, and the inline stylesheet and markup read directly, on 2026-10-28.
