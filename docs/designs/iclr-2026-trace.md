# TRACE Gilded Night — Style Reference

> An opera programme under a starfield: gold-leaf serif, velvet black, and a single spotlight on the name.

**Theme:** dark

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440-wide first-viewport and tall screenshots, and the page's `static/css/style.css` (its `:root` token block, hover rules and two media queries). Playfair Display, Source Sans 3 and JetBrains Mono all load from Google Fonts, so declared and rendered faces match. Elements carry `data-animate` and fade in with a 0.9s ease when they enter the viewport; in the 1440×900 snap the authors and buttons were still mid-fade, and in the full-page tall capture the `min-height: 100vh` hero stretched to the capture height and every lower section was still invisible. Positions below are the computed boxes, which do not depend on the fade. Color share is measured on the first viewport.

## Overview

A one-screen hero on near-black (#08080d) with a canvas of drifting gold particles, a faint gold radial glow at the top and a film-grain overlay at 1.8% opacity. Centered in it: a gold-outlined pill badge "ICLR 2026 ORAL PRESENTATION" flanked by two slowly spinning star icons, a 128px "TRACE" wordmark in Playfair Display ExtraBold with 10px tracking and a shimmering gold gradient fill, a 72px gold hairline with a glowing dot, a two-line italic Playfair subtitle in lavender grey, an acronym line where the letters T, R, A, C, E are picked out in gold, author names with dashed underlines, and a row of seven 10px-radius buttons of which only "Paper" is solid gold. A "SCROLL TO EXPLORE" hint sits at the bottom. Below the fold the page alternates #08080d and #0c0c14 bands, each 120px-padded, with numbered Playfair section titles ("01 Abstract"), a gold-edged Key Insight card, translucent contribution and result cards, and paper figures set on warm off-white frames with gold-tinted borders.

## First Viewport

Color share (1440×900, 8-color quantize): five near-black shades #0d0c0e 23.2%, #09090e 21.1%, #08080d 20.6%, #0b0a0e 18.5%, #09090d 8.8% (the background with its glow and grain), warm brown-gold #231f17 4.4% (the gold glow behind the wordmark and the badge), #08090e 3.3%. The gold wordmark and light text are each under 1% at quantization.

Anatomy in DOM order (all centered on x=720 inside `.hero-content`, max-width 900px; the hero is a flex column centered vertically in 900px with padding 80px 24px 60px):

1. **Badge** — `.oral-badge-inner`, Source Sans 3 13px / 600, uppercase, letter-spacing 2px, #d4af37 text and 1px #d4af37 border, fill gradient rgba(212,175,55,0.10)→0.04, pill radius 50px, padding 11px 30px, 13px star SVGs left and right; text line y=145–167, pill about y=134–178; a blurred gold glow pulses behind it. Margin-bottom 44px.
2. **Wordmark** — `h1 .title-trace`, "TRACE", Playfair Display 128px / 800, letter-spacing 10px, line-height 1.1, gold gradient fill (#f5e6a3 → #f0d060 → #d4af37 → #a68a2a → #d4af37, animated) (y=223–364). Margin-bottom 16px.
3. **Separator** — `.title-separator`, 72×1px gold line fading at both ends, with a 6px #d4af37 dot and 12px glow; margin 20px auto.
4. **Subtitle** — `.title-sub`, "Your Diffusion Model Is Secretly / an Instance Edge Detector", Playfair Display 32px / 400 italic, line-height 1.5, #a09caa, two lines (ends about y=500). `h1` margin-bottom 24px.
5. **Acronym line** — `p.hero-expand`, 16px Source Sans 3, letter-spacing 0.5px, #615d6c with `em` letters in #d4af37 / 600 (y=525–552). Margin-bottom 44px.
6. **Authors** — `.author a`, 17px / 500, #eae8e4, 1px dashed rgba(160,156,170,0.4) underline, row gap 6px 20px, superscripts 11px #615d6c (y=598–624); affiliations 15px #a09caa; contribution note 13px #615d6c. Block margin-bottom 48px.
7. **Buttons** — `.hero-actions`, seven buttons 48px tall with 10px gaps (y=739–787): Paper, Code, OpenReview, arXiv, Slides, Poster, Video. Source Sans 3 14px / 600, letter-spacing 0.3px, padding 11px 22px, radius 10px, Font Awesome icon left.
8. **Scroll hint** — `.hero-scroll-hint`, 11px uppercase, letter-spacing 1.5px, #615d6c, with a 28px gradient tick bouncing below (y=805–824); absolute, 40px from the hero bottom.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Velvet Black | #08080d | `--bg-primary` | `body` background, hero, light bands, step icon fill |
| Night Band | #0c0c14 | `--bg-secondary` | `.section-dark` bands (Contributions, Observation, Citation) |
| Card Ink | #131320 | `--bg-card-solid` | BibTeX block |
| Bone | #eae8e4 | `--text-primary` | body text, author names, button labels, section titles, card headings |
| Lavender Grey | #a09caa | `--text-secondary` | subtitle, abstract and card paragraphs, captions, affiliations, BibTeX code, nav links |
| Dusk Grey | #615d6c | `--text-muted` | acronym line, scroll hint, superscripts, footer text, highlight descriptions |
| Gold | #d4af37 | `--gold` | badge text and border, separator dot, acronym letters, section numbers, mono labels, step icons |
| Gold Light | #f0d060 | `--gold-light` | gradient stops, link hover |
| Gold Pale | #f5e6a3 | `--gold-pale` | wordmark gradient start |
| Gold Dark | #a68a2a | `--gold-dark` | gradient end, scrollbar hover |
| Button Ink | #0a0a0f | (literal) | text on the gold Paper button |
| Periwinkle | #7ba0e8 | `--accent` | inline links |
| Figure Paper | #f8f7f4 | `--frame-bg` | background behind paper figures |
| Card Wash | rgba(255,255,255,0.03) | `--bg-card` | contribution and highlight cards |
| Hairline | rgba(255,255,255,0.05) | `--border` | card borders, footer rule |
| Strong Hairline | rgba(255,255,255,0.10) | `--border-strong` | secondary button border, floating nav border, copy button |
| Gold Line | rgba(212,175,55,0.20) | `--border-gold` | Key Insight card border, card hover border, band top hairline |

## Tokens — Typography

- **Display:** `'Playfair Display', Georgia, serif`; renders Playfair Display 400, 400 italic, 600, 700, 800. Wordmark, subtitle, section titles, card headings, highlight numbers, nav and footer logo. Substitute: Bodoni Moda or DM Serif Display (high-contrast didone with similar width).
- **Body:** `'Source Sans 3', -apple-system, sans-serif`; renders Source Sans 3 400–700. Substitute: Source Sans Pro or Inter.
- **Mono:** `'JetBrains Mono', 'Fira Code', monospace`; renders 400/500. Section numbers, Key Insight label, metric labels, BibTeX. Substitute: IBM Plex Mono.
- Body size is fluid: `clamp(17px, 0.45vw + 12px, 20px)` renders 18.48px at 1440, line-height 1.7.

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Wordmark | `.title-trace` | clamp(68px, 10vw, 128px) → 128px / 800 / 1.1, tracking 10px |
| Subtitle | `.title-sub` | clamp(22px, 3.5vw, 32px) → 32px / 400 italic / 1.5 |
| Section title | `.section-title` | clamp(32px, 5vw, 44px) → 44px / 700, preceded by mono 13px gold number |
| Step heading | `.step-content h3` | clamp → 22.5px / 600 |
| Card heading | `.contrib-card h3` | clamp → 21px / 600 |
| Result heading | `.result-block h3` | 20px / 600 |
| Highlight number | `.highlight-value` | 42px / 800, gold gradient |
| Body | `body` | 18.48px / 400 / 1.7 |
| Abstract | `.abstract-content p` | 18.48px / 1.9, #a09caa |
| Key Insight text | `.tldr-text` | clamp → 20.2px / 1.85 |
| Authors | `.author` | 17px / 500 |
| Button | `.btn` | 14px / 600, tracking 0.3px |
| Badge | `.oral-badge-inner` | 13px / 600 uppercase, tracking 2px |
| Mono label | `.tldr-label`, `.highlight-metric` | 11–12px / 500 uppercase, tracking 1.5–2.5px |
| BibTeX | `.bibtex-code` | clamp → 15.3px / 1.8 |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Buttons | 10px radius, padding 11px 22px |
| Badge, floating nav | 50px pill radius |
| Key Insight card | 24px radius, padding 52px, 1px rgba(212,175,55,0.20) border, two 60px gold corner brackets (top-left, bottom-right) |
| Contribution / highlight cards | 18px radius, 1px rgba(255,255,255,0.05) border; hover lift 3–4px, gold border and a gold top line |
| Figure frame | 10px radius, #f8f7f4 fill, shadow `0 4px 24px rgba(0,0,0,0.35), 0 1px 3px rgba(0,0,0,0.2)`; `.figure-frame-glow` adds a 1px gold-gradient border |
| Step icon | 40px square, 12px radius, 1.5px #d4af37 border, glow `0 0 20px rgba(212,175,55,0.1)` |
| BibTeX block | 18px radius, #131320, header strip with 1px hairline |
| Gold button shadow | `0 4px 20px rgba(212,175,55,0.25)` plus a 1px inner top highlight |

## Layout Metrics

- **Container:** `.container` max-width 1180px, padding 0 24px; inner measure 1132px (x=154–1286 at 1440).
- **Hero:** full width, `min-height: 100vh`, flex-centered, padding 80px 24px 60px; content max-width 900px.
- **Section padding:** `--section-gap` 120px top and bottom; Key Insight section 80px.
- **Abstract column:** max-width 880px, left-aligned inside the container.
- **Grids:** contributions 3 × 1fr, 20px gap; result highlights 4 × 1fr, 16px gap; result tables 1fr 1fr at ≥900px (18px gap).
- **Method:** a vertical step list indented 48px with gold connector lines.
- **BibTeX:** max-width 960px, centered.

| Breakpoint | Gutter | Body | Wordmark | Grid change |
|---|---|---|---|---|
| ≥1280px | (viewport − 1132)/2 | 17.8–20px (18.48px at 1440) | 128px | 3-col contributions, 4-col highlights, 2-col tables |
| 900–1279px | 24px | 17–17.8px | 90–128px | none |
| 769–899px | 24px | 17px | 77–90px | result tables one column |
| 481–768px | 24px | 16px | 68–77px | all grids one column, section gap 80px, buttons padding 10px 16px at 13px, nav links hidden, Key Insight corners removed |
| ≤480px | 24px | 16px | 68px | highlights back to 2 columns with 32px numbers; badge 10px with 1px tracking |

## Components

- **Gold primary button:** fill `linear-gradient(135deg, #f0d060, #d4af37, #a68a2a)`, text #0a0a0f, 14px / 600, padding 11px 22px, radius 10px, shadow 0 4px 20px rgba(212,175,55,0.25); hover lifts 2px and the shadow grows to 0 8px 32px.
- **Glass secondary button:** fill rgba(255,255,255,0.04), 1px rgba(255,255,255,0.10) border, #eae8e4 text, `backdrop-filter: blur(8px)`; hover fill rgba(212,175,55,0.06), border #d4af37, text #f0d060, lift 2px.
- **Oral badge:** gold pill described in First Viewport, with a pulsing blurred halo and two rotating star icons.
- **Section title:** flex baseline row: mono 13px gold number ("01") at 0.8 opacity, 16px gap, Playfair 44px / 700 title in #eae8e4; margin-bottom 52px.
- **Key Insight card:** gold-washed gradient fill rgba(212,175,55,0.05)→0.015, 24px radius, 52px padding, centered; 56px rounded icon tile, mono 11px gold "KEY INSIGHT" label, 20px #a09caa text with `strong` in #eae8e4.
- **Contribution card:** translucent fill, 18px radius, padding 36px 28px; gold numeral glyph 28px, Playfair 21px heading, 16–17.5px #a09caa body; hover gold border, lift 4px, deep shadow and a gold top line.
- **Result highlight card:** centered, padding 36px 16px, gold-gradient 42px number ("+5.1", "+7.1", "81×"), mono 12px gold metric, 13px #615d6c description.
- **Figure frame:** paper figures on #f8f7f4 with 10px radius and dark shadow, optionally inside a 1px gold-gradient border; captions 14.5–17px #a09caa.
- **Floating nav:** appears after scrolling, fixed 16px from the top, pill with rgba(8,8,13,0.88) fill and 24px blur, 1px strong hairline, Playfair 18px gold "TRACE" logo with 3px tracking, 14px #a09caa links (hover #f0d060).
- **BibTeX block:** #131320, 18px radius, header strip with mono uppercase label and an outline copy button (hover gold), code JetBrains Mono #a09caa.
- **Footer:** 44px padding, hairline top rule, gold Playfair "TRACE" logo, venue in 13px #615d6c, credit "Template inspired by Nerfies".

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Venue / award badge | Yes | gold pill "ICLR 2026 Oral Presentation" |
| Title / authors / affiliations | Yes | gold serif wordmark, italic subtitle, dashed-underlined authors |
| Link buttons | Yes | seven 10px-radius buttons, Paper solid gold |
| Navigation | Present but non-standard | floating pill nav that appears only after scroll |
| TL;DR | Yes | "Key Insight" gold card |
| Teaser figure | No (absent from the source) | the hero is typographic only |
| Abstract | Yes | numbered section, 880px column |
| Contributions | Yes | three translucent cards on a darker band |
| Method | Yes | framed overview figure plus a vertical step list with gold icons |
| Results numbers | Yes | four gold-number highlight cards |
| Results tables | Present but non-standard | paper table images in white frames, not HTML tables |
| BibTeX | Yes | dark card with copy button |
| Video | Present but non-standard | link button only |
| Footer | Yes | logo, venue and template credit |

## Adapting to Other Content

- **More authors:** keep the flex-wrap row with 6px 20px gaps and dashed underlines; past two lines, drop the font to 15px rather than shrinking the wordmark.
- **Results table (HTML):** put it in a #131320 card with 18px radius; mono 12px gold uppercase headers, 15px #a09caa cells, rgba(255,255,255,0.05) row rules, your method's row in #eae8e4 with a gold left hairline; best values in #f0d060.
- **Teaser image or video:** place it in a figure frame directly under the Key Insight card, never inside the hero, so the hero stays a single typographic screen.
- **Long publication or news list:** a numbered section with rows on the translucent card wash, dates in mono 12px gold, titles in Source Sans 3 #eae8e4, 1px hairlines between rows.
- **No acronym:** replace the acronym line with a one-sentence tagline in the same 16px #615d6c style and highlight one key word in gold.

## Do's and Don'ts

- Do keep gold for the wordmark, the single primary button, numbers and small labels; everything else is grey on black.
- Do put white-background paper figures on the warm #f8f7f4 frame instead of placing them directly on black.
- Do number section titles with the mono gold index.
- Don't add a second accent hue in the chrome; periwinkle is only for inline links.
- Don't let fade-in animations be the only way content appears; provide a no-JS fallback (the full-page capture shows empty bands without it).
- Don't stretch the hero beyond one viewport with extra content; the scroll hint assumes a single screen.

## Surfaces

Velvet black page (#08080d) with a gold radial glow and grain; alternate #0c0c14 bands with a centered gold hairline at the top; translucent white-wash cards; one solid #131320 code card; warm off-white figure frames.

## Imagery

No imagery in the hero beyond the particle canvas. Below: method overview diagrams, edge-map comparison grids and paper table screenshots, all on white, framed in #f8f7f4 with soft dark shadows.

## Layout

A full-screen centered hero followed by alternating full-bleed bands with a 1180px container. Rendered height about 9,575px at 1440×900.

## Agent Prompt Guide

Quick colors: background #08080d, band #0c0c14, text #eae8e4, secondary #a09caa, muted #615d6c, gold #d4af37 (light #f0d060, pale #f5e6a3, dark #a68a2a), button text #0a0a0f, figure frame #f8f7f4.

1. "Build a one-screen dark hero on #08080d: a gold pill badge (13px Source Sans 3 600 uppercase, 2px tracking, 1px #d4af37 border, #d4af37 text, padding 11px 30px); a 128px Playfair Display 800 wordmark with 10px tracking filled by linear-gradient(135deg, #f5e6a3, #f0d060, #d4af37, #a68a2a); a 72px gold hairline with a 6px #d4af37 dot; a 32px italic Playfair subtitle in #a09caa at line-height 1.5; authors 17px/500 #eae8e4 with dashed underlines."
2. "Create button pairs: primary with linear-gradient(135deg, #f0d060, #d4af37, #a68a2a) fill, #0a0a0f 14px/600 text, padding 11px 22px, 10px radius, shadow 0 4px 20px rgba(212,175,55,0.25); secondary with rgba(255,255,255,0.04) fill, 1px rgba(255,255,255,0.10) border, #eae8e4 text, hover border #d4af37 and text #f0d060."
3. "Make a results highlight row: four cards in a 4-column grid with 16px gaps, rgba(255,255,255,0.03) fill, 1px rgba(255,255,255,0.05) border, 18px radius, padding 36px 16px; a 42px Playfair 800 gold-gradient number, a JetBrains Mono 12px #d4af37 uppercase metric, and a 13px #615d6c description."

## Similar Pages

- Luxury dark "keynote" project pages with serif wordmarks and particle heroes.
- Nerfies-derived pages that have been fully restyled (the footer credits Nerfies as inspiration only).

## Quick Start

```css
:root {
  --bg-primary: #08080d;
  --bg-secondary: #0c0c14;
  --bg-card: rgba(255, 255, 255, 0.03);
  --bg-card-solid: #131320;
  --text-primary: #eae8e4;
  --text-secondary: #a09caa;
  --text-muted: #615d6c;
  --gold: #d4af37;
  --gold-light: #f0d060;
  --gold-pale: #f5e6a3;
  --gold-dark: #a68a2a;
  --accent: #7ba0e8;
  --border: rgba(255, 255, 255, 0.05);
  --border-strong: rgba(255, 255, 255, 0.10);
  --border-gold: rgba(212, 175, 55, 0.20);
  --frame-bg: #f8f7f4;
  --font-display: 'Playfair Display', Georgia, serif;
  --font-body: 'Source Sans 3', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --container-width: 1180px;
  --section-gap: 120px;
  --btn-radius: 10px;
}
```

## Provenance

- **URL:** https://shjo-april.github.io/TRACE/
- **Paper:** TRACE: Your Diffusion Model is Secretly an Instance Edge Detector (arXiv 2503.07982), Sanghyun Jo et al.
- **Venue:** ICLR 2026, Oral (stated in the hero badge).
- **Selection reason:** the arXiv comment states "Accepted to ICLR 2026 (Oral)" and links this page; chosen for its starfield-dark hero with a gold serif wordmark, italic subtitle, acronym highlight and refined pill buttons. The "first 2,700px mostly empty" impression comes from full-page capture: the 100vh hero grows with the capture height and lower sections only fade in on scroll.
- **Template credit:** footer reads "Template inspired by Nerfies".
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share and loaded-font list, 1440 first-viewport and tall screenshots, `static/css/style.css`, page HTML; 2026-10-28.
