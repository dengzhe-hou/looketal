# M-plicits Amber Serif — Style Reference

> A night lab with a lamp on: an italic amber word in a serif title, a white specimen card under glass, then warm cream pages.

**Theme:** both

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share) and the 1440 screenshots, checked against the page's single inline `<style>` block. The page is a navy hero and navy footer band around a warm cream body, so the theme is "both".

## Overview

M-plicits is a compact, single-file page in a 1120px wrapper. The navy (#0b1020) hero carries two soft radial glows (amber at right, indigo at top left), a white rounded NeurIPS badge, and an Instrument Serif title at 56px whose first word, "M-plicits", is italic amber (#f59e0b). Beside it a white card holds a drag-to-compare slider with a red "iNGP — absorbs noise" tag and a green "M-plicits — filters it" tag, plus a pill tab set. A four-up serif stat strip closes the hero. Below, the body turns cream (#faf9f6): small uppercase amber eyebrow labels, 42px serif section titles, an embedded explainer video, a figure beside three numbered steps with an amber-bordered note, a method toggle over a 4-up result grid, a real-time band on #f1efe9, and a navy footer band with resource cards and BibTeX.

## First Viewport

Color share of the 1440×900 viewport: #0b1020 39% (hero navy), #c6c6c7 21% (the grey cherub render inside the white card), #161728 20% and #0c101e, #090d1d, #0c1021, #0b1023 (together about 20%, the glow-shifted navy). The first screen is navy with one white card; amber shows only in the title word, the Paper button and superscripts.

Anatomy in DOM order (wrapper x 160–1280, content x 184–1256):

1. **Nav** `nav .in`: in-flow, padding 18px 0. Logo "M‑plicits" Inter 16px/800, #ffffff, left. Links (How it works, Results, Video 1, Video 2, Real time, Resources, BibTeX) Inter 14px/500, #c7cbd6, 22px left margin each, right-aligned; hover #f59e0b. Gap to badge 44px (grid padding-top).
2. **Venue badge** `a.badge`: white #ffffff pill-card, radius 14px, padding 8px 18px 8px 10px, shadow 0 12px 32px rgba(0,0,0,.35); conference logo 40px tall, a 1px #dfe2ea divider, "NeurIPS 2026" Inter 19px/800 #0b1020 over "40th Conference on Neural Information Processing Systems" 12px/500 #5b6170. Gap 24px.
3. **Title** `h1.display`: Instrument Serif 56px/400, line-height 1.03, letter-spacing -.015em, #ffffff, left, three lines; "M-plicits" in italic #f59e0b. Gap 24px.
4. **Authors** `.authors`: Inter 15.5px/500, line-height 1.55, #eef0f5, max-width 600px, names with a 1px rgba(255,255,255,.28) bottom border and amber superscripts. Affiliations below at 13.5px/400 #9ba1b3 with 6px gap. Gap 22px.
5. **Tagline** `.tagline`: Instrument Serif 25px, line-height 1.25, #d7dae4, with "clean" in italic amber; 1px rgba(255,255,255,.12) rule above with 18px padding-top. Gap 8px.
6. **Lede** `.lede`: Inter 15.5px, #a9aec0, max-width 540px. Gap 26px.
7. **Buttons** `.btns`: Paper (filled amber), Code, Models, Data, Video 1, Video 2 (outlined), 44px tall, 8px gaps, wrapping to a second row.
8. **Compare card** (right column, x 753): white card radius 18px, padding 12px, shadow 0 30px 80px rgba(0,0,0,.45); 4:3 slider (479×359) with a 3px navy bar and a 46px navy knob ringed in white; tags 11.5px/800 uppercase in pills; footer line "Drag. Same scan, 1% noise, both methods." 13px #5b6170 and a pill tab set (Cherub, Armadillo, Lucy).
9. **Stat strip** `.stats` (at the bottom of the fold, about y 815–885): 4 columns, 1px rgba(255,255,255,.12) top rule, padding 22px 0 30px; numbers Instrument Serif 38px #ffffff; labels 12.5px #9aa0b3; 1px vertical dividers.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Night Navy | #0b1020 | --navy | hero and footer band, compare bar and knob, active tab fill, video ground |
| Navy Card | #121a33 | --navy2 | resource cards and BibTeX block in the footer band |
| Lamp Amber | #f59e0b | --amber | italic title word, tagline accent, Paper button fill, author superscripts, nav and button hover, note left border |
| Amber Hover | #fbbf24 | (literal) | Paper button hover fill |
| Button Ink | #1a1200 | (literal) | Paper button label on amber |
| Amber Ink | #b45309 | --amber-ink | eyebrow labels, step numerals on cream |
| Cream Paper | #faf9f6 | --paper | body background |
| Cream Band | #f1efe9 | --paper2 | real-time band, compare tab track |
| Ink | #15171c | --ink | body text, h2, h3 on cream |
| Body Grey | #3b404c | (literal) | paragraphs `p.body`, step text, note text |
| Muted | #5b6170 | --muted | captions, inactive tabs, badge subline, card footer |
| Line | #e6e3dc | --line | card and figure borders on cream |
| Nav Grey | #c7cbd6 | (literal) | hero nav links |
| Author White | #eef0f5 | (literal) | author names |
| Tagline Grey | #d7dae4 | (literal) | hero tagline |
| Lede Grey | #a9aec0 | (literal) | hero lede |
| Affil Grey | #9ba1b3 | (literal) | affiliations, stat labels (#9aa0b3) |
| Badge Rule | #dfe2ea | (literal) | divider inside the venue badge |
| Bad Red | #dc2626 | --bad | "iNGP" tag, iNGP toggle when on |
| Good Green | #059669 | --good | "M-plicits" tag, M-plicits toggle when on |
| Code Text | #e6e8ef | (literal) | BibTeX text |
| Card Desc | #a7adbe | (literal) | resource card descriptions |
| Footer Grey | #8b91a3 | (literal) | venue line at the page foot |
| Indigo Glow | rgba(99,102,241,.22) | (literal) | top-left radial glow in the hero |

## Tokens — Typography

- **Display serif**: declared `'Instrument Serif', Georgia, 'Times New Roman', serif`; renders Instrument Serif 400 and 400 italic. Substitute: Newsreader Display at weight 400 (similar condensed, high-contrast proportions).
- **Sans**: declared `'Inter', system-ui, 'Segoe UI', Helvetica, Arial, sans-serif`; renders Inter 400, 500, 600, 800. Substitute: Inter is free; if unavailable use Geist Sans.

| Role | Selector | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Title | `.display` | 56px (48px ≤920px, 38px ≤520px) | 400 serif | 1.03 | -.015em |
| Section title | `h2` | 42px (32px ≤520px) | 400 serif | 1.08 | -.01em |
| Stat number | `.stat .n` | 38px serif | 400 | 1 | 0 |
| Step numeral | `.step .num` | 34px serif | 400 | 1 | 0 |
| Footer h2 | `.foot h2` | 34px serif | 400 | 1.08 | -.01em |
| Tagline | `.tagline` | 25px serif | 400 | 1.25 | 0 |
| Badge venue | `.badge .v b` | 19px | 800 | 1.15 | -.01em |
| Step heading | `.step h3` | 17px | 700 | 1.6 | 0 |
| Body | `p.body` | 16.5px | 400 | 1.6 | 0 |
| Authors, lede | `.authors`, `.lede` | 15.5px | 500 / 400 | 1.55 / 1.6 | 0 |
| Step text | `.step p` | 15px | 400 | 1.6 | 0 |
| Buttons, nav, tabs | `.btn`, `nav .links a`, `.seg button` | 14px | 600 / 500 / 600 | 1.6 | 0 |
| Captions | `.howvid figcaption`, `.gcap` | 13.5px | 400 | 1.6 | 0 |
| Eyebrow | `.sec-k` | 12.5px uppercase | 700 | 1.6 | .16em |
| Compare tags | `.cmp .tag` | 11.5px | 800 | 1.6 | .06em |

## Tokens — Spacing & Shapes

- **Radius**: 999px for buttons, tabs, segmented toggle and tags; 18px for the compare card and video card; 14px for the badge, result tiles, real-time tiles and resource cards; 12px for figures, the YouTube frame and BibTeX; 10px for the slider inside the card and the note; 7px for tile labels.
- **Shadows**: badge 0 12px 32px rgba(0,0,0,.35) (hover turns it amber, rgba(245,158,11,.4)); compare card 0 30px 80px rgba(0,0,0,.45); knob 0 8px 22px rgba(0,0,0,.35). Cream-section cards have no shadow, only a 1px #e6e3dc border.
- **Borders**: hero rules 1px rgba(255,255,255,.12); outlined buttons 1.5px rgba(255,255,255,.28); note left border 3px #f59e0b.

## Layout Metrics

- **Container**: `.wrap` max-width 1120px, padding 0 24px, centered: content width 1072px at 1440 (x 184–1256).
- **Hero grid**: `.hgrid` columns 1.02fr / 1fr, gap 56px, padding 44px 0 40px, items vertically centered. Compare card about 500px wide.
- **Stat strip**: 4 equal columns, padding 22px 0 30px; each stat padding 6px 18px 6px 0 with 18px right margin and a 1px divider.
- **Sections**: `section` padding 72px 0 8px; eyebrow, then h2 with 10px top and 12px bottom margins, then body text max-width 720px.
- **How it works**: video max-width 960px, 16:9; then grid 400px figure + 1fr steps, gap 48px; steps 44px numeral column + 1fr, 14px gap, 18px between steps.
- **Results grid**: 4 columns, 14px gap, square tiles; segmented toggle 22px above.
- **Real-time band**: full-bleed #f1efe9, margin-top 72px, padding 64px 0 72px, 4-column tile grid with 14px gap.
- **Footer band**: navy, padding 64px 0 36px; resource cards in 3 columns, 14px gap.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| >920px | 24px | 16.5px | 56px | hero 2 columns; stats 4; results 4; resources 3 |
| ≤920px | 24px | 16.5px | 48px | hero stacks (gap 34px); stats 2×2 without dividers; how-it-works stacks (figure max 420px); results and real-time 2 columns; resources 1 column; nav links 14px apart |
| ≤520px | 24px | 16.5px | 38px | nav links hidden; badge subline hidden; tagline 21px; h2 32px |

## Components

- **Primary button** `.btn.primary`: padding 10px 13px, radius 999px, #f59e0b fill and 1.5px border, #1a1200 Inter 14px/600, emoji icon left with 7px gap; hover fill #fbbf24.
- **Outline button** `.btn`: same size, transparent, 1.5px rgba(255,255,255,.28) border, #ffffff text; hover border and text #f59e0b.
- **Venue badge**: see First Viewport; hover shadow turns amber.
- **Compare card**: white, radius 18px, padding 12px, deep shadow; inner 4:3 slider radius 10px; divider 3px #0b1020; knob 46px circle #0b1020 with 2px #ffffff border and "↔"; corner tags 11.5px/800 uppercase white on #dc2626 (left) and #059669 (right), padding 6px 12px.
- **Pill tabs** `.tabs`: #f1efe9 track, padding 3px; buttons 13px/600 #5b6170, padding 6px 13px; active #0b1020 fill, #ffffff text.
- **Method toggle** `.seg`: #ffffff track with 1px #e6e3dc border, padding 4px; buttons 14px/600 padding 9px 18px with a 9px dot; active fills navy, red (iNGP) or green (M-plicits).
- **Eyebrow + title**: `.sec-k` 12.5px/700 uppercase .16em #b45309, then h2 42px serif #15171c.
- **Numbered step**: Instrument Serif 34px #b45309 numeral, 17px/700 heading, 15px #3b404c text.
- **Note**: #ffffff, 1px #e6e3dc border with 3px #f59e0b left border, radius 10px, padding 14px 16px, 14.5px #3b404c.
- **Result tile** `.g`: square, #ffffff, 1px #e6e3dc border, radius 14px; label bottom-left 12px/600 white on rgba(21,23,28,.82), radius 7px; images cross-fade .35s.
- **Resource card** `.rcard`: #121a33, 1px rgba(255,255,255,.1) border, radius 14px, padding 20px; title 700, description 13.5px #a7adbe; hover border #f59e0b.
- **BibTeX**: #121a33, 1px rgba(255,255,255,.1) border, radius 12px, padding 18px, 13px/1.55 mono #e6e8ef.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Top nav | yes | in-flow nav inside the navy hero, not sticky |
| Venue badge | yes, non-standard | white card with conference logo above the title |
| Title block | yes | serif title with an italic amber first word |
| Authors / affiliations | yes | 12 underlined names with amber superscripts, numbered affiliations |
| Link buttons | yes | one amber filled pill, the rest outlined |
| Teaser | yes, non-standard | drag-compare slider card with method tags and shape tabs |
| Stat strip | yes | four serif numbers with dividers |
| Method | yes | explainer video, figure plus numbered steps, note callout |
| Results | yes | method toggle over a 4-column image grid |
| Videos | yes | video in a white rounded card |
| Real-time section | yes | cream band with 4 tiles |
| Results table | absent from the source | none |
| Resources | yes | navy cards |
| BibTeX | yes | navy code block |
| Footer | yes | venue line with logo and hairline |

## Adapting to Other Content

- **More authors**: keep the inline underlined list at 15.5px/500 with amber superscripts; max-width 600px lets it wrap to four lines before it competes with the title.
- **Results table**: put it in a white card (1px #e6e3dc, radius 14px) on cream; header 12.5px/700 uppercase #b45309 like the eyebrow, cells 15px #3b404c, hairlines #e6e3dc, best numbers 700 #15171c, the proposed row tinted with 8% #f59e0b.
- **Long publication list**: on cream, one row per item with a serif 34px #b45309 year on the left (the step pattern), title 17px/700, venue 15px #5b6170.
- **News**: an eyebrow "NEWS", then a list of note callouts (white, 3px amber left border) or plain rows with a 13.5px #5b6170 date.
- **No compare slider**: place a teaser image or video in the same white 18px-radius card with 12px padding and the deep shadow; keep a caption line in 13px #5b6170.

## Do's and Don'ts

- Do set one key word of the title in italic amber; nothing else in the title is colored.
- Do pair Instrument Serif for display and numbers with Inter for everything else.
- Do label every cream section with a small uppercase amber eyebrow before the serif h2.
- Do sit media in white rounded cards with 1px #e6e3dc borders on cream.
- Do keep exactly one filled button (Paper) and outline the rest.
- Don't use shadows on cream; shadows are for the navy hero only.
- Don't spread amber into backgrounds; it is a text, border and single-button color.
- Don't exceed the 1120px wrapper; full-bleed is only for band backgrounds.

## Surfaces

Navy #0b1020 hero with an amber radial glow at right and an indigo glow at top left; white #ffffff cards; cream #faf9f6 body; #f1efe9 real-time band and tab tracks; navy footer band with #121a33 cards.

## Imagery

Grey shaded surface renders (cherub, armadillo, Lucy) on white, noisy vs. clean comparisons, a cartoon-style YouTube explainer, a multiscale method diagram with colored SDF slices, and real-time render tiles.

## Layout

Two-column hero (text left, compare card right) over a 4-up stat strip, then a single 1120px column of sections with internal grids (400px figure + steps, 4-up tiles), a full-bleed cream band and a navy footer band. About 5,400px tall.

## Agent Prompt Guide

Quick colors: navy #0b1020, navy card #121a33, amber #f59e0b, amber ink #b45309, cream #faf9f6, cream band #f1efe9, ink #15171c, body #3b404c, muted #5b6170, line #e6e3dc, red #dc2626, green #059669.

1. "Build a hero title: Instrument Serif 56px weight 400, line-height 1.03, letter-spacing -.015em, #ffffff on #0b1020; the first word italic #f59e0b; below it, authors in Inter 15.5px/500 #eef0f5 with 1px rgba(255,255,255,.28) underlines and #f59e0b superscripts."
2. "Build link pills: padding 10px 13px, radius 999px, Inter 14px/600; primary has #f59e0b fill and border with #1a1200 text, hover #fbbf24; others are transparent with a 1.5px rgba(255,255,255,.28) border and #ffffff text, hover border and text #f59e0b; 8px gaps."
3. "Build a cream section: padding 72px 0 8px on #faf9f6; eyebrow Inter 12.5px/700 uppercase, letter-spacing .16em, #b45309; h2 Instrument Serif 42px/400 #15171c, margin 10px 0 12px; paragraph 16.5px/1.6 #3b404c, max-width 720px; a note with #ffffff fill, 1px #e6e3dc border, 3px #f59e0b left border, 10px radius, padding 14px 16px."

## Similar Pages

- Single-file project pages with a dark hero, a light serif title and a comparison slider card.
- Editorial landing pages that use small uppercase eyebrows over serif section titles on a warm paper ground.

## Quick Start

```css
:root {
  --navy: #0b1020;
  --navy2: #121a33;
  --ink: #15171c;
  --body: #3b404c;
  --muted: #5b6170;
  --line: #e6e3dc;
  --paper: #faf9f6;
  --paper2: #f1efe9;
  --amber: #f59e0b;
  --amber-hover: #fbbf24;
  --amber-ink: #b45309;
  --bad: #dc2626;
  --good: #059669;
  --sans: 'Inter', system-ui, 'Segoe UI', Helvetica, Arial, sans-serif;
  --serif: 'Instrument Serif', Georgia, 'Times New Roman', serif;
  --wrap: 1120px;
}
```

## Provenance

- **URL**: https://dsilvavinicius.github.io/m-plicits/
- **Paper**: M-plicits: Neural Implicit Surfaces via Nested Multiscale Residuals (arXiv 2609.28684), Vinícius da Silva et al.
- **Venue**: NeurIPS 2026.
- **Selection reason**: the arXiv comment states acceptance at NeurIPS 2026 and links this page.
- **Template credit**: custom single-file page; no template credit shown.
- **Evidence used**: computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), the 1440 screenshot and tall capture, and the inline stylesheet read directly. Captured 2026-10-28.
