# Framed Card on Code — Style Reference

> A business card pinned to a pale-blue wall of source code: one teal frame, one portrait, three big links.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts and DOM boxes from `tools/computed_style.py`, plus a selector probe of the card, stripes and code columns), the 1440×900 screenshot from `snap.py`, a second screenshot taken 4.5 seconds after load, and `css/style.css`, `index.html` and `codebackground.js` read directly. The code texture is loaded by jQuery 200ms after DOM ready (`$('.code-wrapper').load('code.html')`), so the `snap.py` shot shows only the stripes; the later shot and the DOM show five columns of faint code, and the color share below is measured on that later shot. Only Lato 400 loads; bold runs are synthesized. The page is exactly one viewport (900px) tall.

## Overview

A landing page that is a single object. The background is a full-viewport field of vertical pinstripes, sky blue #84d9ea with four layered white stripe gradients, all at 20% opacity over white so it reads as a very pale blue (#e6f7fb to #effafc). Over the stripes, five 250px columns of real Cython/Python source in 8px black monospace at 20% opacity run the full height, giving a faint code texture. Centred on top is one white card (660×340px inside a 10px solid #77c3d2 border): the left half stacks "Aaron Defazio, PhD" in Lato 36px, three centred 16px lines in #333333 (role, a bold employer, an obfuscated email with bold "AT" and "DOT"), then three large 30px navigation links (Publications, Blog, Software) with no underline; the right half holds a 330px square high-key black-and-white portrait on white. No header, no footer, no other content on the home page.

## First Viewport

Color share (8-color quantization of the post-load 1440×900 shot): pale stripe blues #effafc 23.3%, #e5f3f5 22.2%, #ecf9fc 14.7%, #e9f9fc 11.3%, #edfafc 5.4%, #e9f6f8 5.1%; near-white #fafdfe 11.9% (card interior and portrait background); grey-blue #ccdadd 6.1% (card frame edge, code glyphs and text anti-aliasing). The frame itself is #77c3d2; nothing else carries colour.

Anatomy in DOM order (desktop 1440px; `body.page` is a full-height flex column centring the card):

1. **Stripe field** (`.stripe-container`, fixed, 1440×2000px, z-index -3): #84d9ea with stripes, opacity 0.2.
2. **Code texture** (`.code-wrapper`, fixed, 1250px wide at x=95, z-index -2): five `.back-code` columns 250px wide, monospace 8px, line-height 8px, black at opacity 0.2, `white-space: pre`, not selectable.
3. **Card** (`.center-box`, x=380, y=270, 680×360px including border): white fill, 10px solid #77c3d2 border, flex row of two equal halves, min-width 660px.
4. **Name** (`.title`, y=280, padding-top 18px, text at y≈298): Lato 36px/400, line-height 1, #000000, centred in the left half. Gap 0.
5. **Role lines** (`.subtitle`, y=334, padding 10px): Lato 16px/400, line-height 1, #333333, centred; "Member of Technical Staff", a blank line, "OpenAI" in bold, a blank line, the email with bold "AT" and "DOT". Ends at y=434. Gap 20px.
6. **Link stack** (`.linkblock a`, y=454, 504, 554): Lato 30px/400, line-height 1, #333333, centred, display block, margin 20px (collapsing to 20px between items), no underline.
7. **Portrait** (`#portrait`, x=720, y=285): 330×330px, no radius, no border; vertically centred in the right half.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Sky Stripe | #84d9ea | (literal) | stripe field base colour (shown at 0.2 opacity, so it renders near #e6f7fb) |
| Pale Field | #e6f7fb | (rendered mix) | what the stripe field looks like on screen |
| Frame Teal | #77c3d2 | (literal) | 10px card border |
| Card White | #ffffff | (literal) | card fill, page base under the stripes |
| Name Black | #000000 | (inherited) | name, code texture glyphs (at 0.2 opacity) |
| Soft Ink | #333333 | (literal) | role lines, bold employer, navigation links |

Declared but not visible on the home page: `.circles` (dot pattern), `.hr` #888888, `.footer` rgba(132,217,234,0.25) band and the publication-page `.main` and `.bibtex` rules belong to the sub-pages.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (card) | 'Lato', sans-serif (Google Fonts; also requests Open Sans Condensed 300, Ubuntu, Bitter, unused here) | Lato 400 only; bold is synthesized | Source Sans 3 |
| Mono (texture) | monospace | system monospace (Consolas on Windows) | DejaVu Sans Mono |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `.title` | 36px / 400 / 1, centred | #000000 |
| Role lines | `.subtitle` | 16px / 400 / 1, centred | #333333 |
| Emphasis | `.subtitle strong` | 16px / 700 (synthetic) | #333333 |
| Navigation link | `.linkblock a` | 30px / 400 / 1, centred, block | #333333 |
| Code texture | `.back-code` … `.back-code5` | 8px / 400 / 8px, pre | #000000 at opacity 0.2 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Card | 0 | 10px solid #77c3d2 | none |
| Portrait | 0 | none | none |
| Links | 0 | none | none |

## Layout Metrics

- **Centring**: `body.page` is `display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 100vh`, so the card sits in the exact middle of the viewport (x=380, y=270 at 1440×900).
- **Card**: `flex: 0 0 330px` along the column axis (so 330px content height plus 10px borders), min-width 660px; two children with `flex: 1` each (330px). Left half margin 0 10px.
- **Name block**: title padding-top 0.5em (18px); subtitle padding 10px; links margin 20px.
- **Background layers**: stripe field fixed 100% × 2000px; code wrapper fixed, `left: 50%; margin-left: -625px`, max-width 1250px, five 250px columns in a flex row.
- **Stripe recipe**: background-size 13px, 29px, 37px, 53px for four `linear-gradient(90deg, …)` layers of white at 0.07, 0.13, 0.17 and 0.19.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≤700px | none (card shrinks to content, min-width 100px) | 16px | 20px; links 20px with margin 10px 5px | card becomes `flex-direction: column-reverse` (portrait on top, 150×150 with 5px padding), card pulled up 50px |
| >700px | card centred in the viewport | 16px | 36px; links 30px | two halves side by side |

## Components

- **Framed card**: white box, 10px solid #77c3d2 border, no radius, no shadow, two equal 330px halves; centred in the viewport by the body flexbox.
- **Big link stack**: block links in Lato 30px/400 #333333, centred, 20px margins, no underline; underline appears on hover. No icons, no buttons.
- **Obfuscated email**: plain 16px text with "AT" and "DOT" in bold, no link.
- **Code wallpaper**: five fixed 250px columns of real source code in 8px monospace black at 0.2 opacity, over a 0.2-opacity pinstripe field; both are behind the card (z-index -2 and -3) and not selectable.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / role | yes | Lato 36px name, 16px role lines in the card |
| Portrait | yes | 330px square, right half of the card |
| Navigation | present but non-standard | three 30px links stacked inside the card, no nav bar |
| Contact | yes | obfuscated email line |
| Decorative background | yes | pinstripes plus faint code columns |
| Bio / about | absent from the source | none on the home page |
| Publications | absent from the source | on the separate `pubs.html` page |
| News | absent from the source | none |
| Footer | absent from the source | none on the home page |

## Adapting to Other Content

- **A short bio**: put one or two 16px #333333 centred lines in `.subtitle`; anything longer belongs on a sub-page, since the card's height is fixed at 330px.
- **More links**: the stack holds three 30px links in 330px; for five, drop to 22px (the sub-page header size) or move extra links to a second card page.
- **A publication list**: use the sub-page pattern from the same stylesheet: a white `.main` column with 10px #77c3d2 side borders on the same stripe field, Lato 16px paper titles and 14px authors at 0.8 opacity.
- **News**: not suited to the landing card; add it on a sub-page in the `.main` column.
- **A results table**: not part of this style; on a sub-page use plain Lato 14px with 1px #333333 rules.

## Do's and Don'ts

- Do keep the home page to exactly one centred card and nothing else.
- Do keep the background at 20% opacity so the code reads as texture, not content.
- Do keep the frame a flat 10px #77c3d2 border with square corners.
- Don't add shadows, radii or a second accent colour.
- Don't make the code texture legible or interactive; it is decoration.
- Don't add a header or footer to the landing view.

## Surfaces

Three layers: the pale pinstripe field (#84d9ea at 0.2), the faint black code columns (0.2), and the white card with its teal frame.

## Imagery

One high-key black-and-white headshot, square, on white so it melts into the card. The code wallpaper is the only other "image".

## Layout

A single centred 680×360px card on a full-bleed decorative background, exactly one viewport tall; no scrolling.

## Agent Prompt Guide

Quick colors: stripe base #84d9ea at 0.2 opacity (renders near #e6f7fb), frame #77c3d2, card #ffffff, name #000000, text and links #333333.

1. "Make a full-viewport background: a fixed layer of #84d9ea with four white vertical stripe gradients (0.07, 0.13, 0.17, 0.19 alpha; sizes 13, 29, 37, 53px) at opacity 0.2, and above it five fixed 250px columns of source code in 8px monospace #000000 at opacity 0.2, not selectable."
2. "Centre one card with flexbox: white, 10px solid #77c3d2 border, no radius, no shadow, 660px wide and 330px tall inside the border, split into two equal halves; right half a 330px square portrait."
3. "In the left half, centred: name in Lato 36px/400 #000000 with 18px top padding; three 16px #333333 lines (role, bold employer, email with bold AT and DOT) in a 10px-padded block; then three block links in Lato 30px/400 #333333 with 20px margins, no underline, underline on hover."

## Similar Pages

- Single-card researcher landing pages that route to separate publication and blog pages.
- Early-2010s personal sites with a decorative textured background and a centred framed panel.

## Quick Start

```css
:root {
  --stripe: #84d9ea;
  --frame: #77c3d2;
  --card: #ffffff;
  --name: #000000;
  --ink: #333333;
  --font-sans: 'Lato', sans-serif;
}
.stripe-container { position: fixed; inset: 0; height: 2000px; background-color: var(--stripe);
  background-image: linear-gradient(90deg, rgba(255,255,255,.07) 50%, transparent 50%), linear-gradient(90deg, rgba(255,255,255,.13) 50%, transparent 50%), linear-gradient(90deg, transparent 50%, rgba(255,255,255,.17) 50%), linear-gradient(90deg, transparent 50%, rgba(255,255,255,.19) 50%);
  background-size: 13px, 29px, 37px, 53px; opacity: .2; z-index: -3; }
.page { display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 100vh; }
.center-box { flex: 0 0 330px; min-width: 660px; display: flex; background: var(--card); border: 10px solid var(--frame); }
.title { padding-top: .5em; font: 400 36px/1 var(--font-sans); color: var(--name); text-align: center; }
.linkblock a { display: block; margin: 20px; font: 400 30px/1 var(--font-sans); color: var(--ink); text-decoration: none; }
.linkblock a:hover { text-decoration: underline; }
```

## Provenance

- **URL**: https://www.aarondefazio.com/
- **Person**: Aaron Defazio (optimization).
- **Venue / award**: ICML 2023 Outstanding Paper, "Learning-Rate-Free Learning by D-Adaptation" (first author). https://icml.cc/virtual/2023/awards_detail
- **Selection reason**: Rule B (first author); chosen for its single framed card floating over a faint code-texture background.
- **Template credit**: hand-written HTML with `css/reset.css`, `css/style.css` and a jQuery loader for `code.html`; no template credited.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, DOM boxes), a selector probe of the card, stripe field and code columns, the snap.py screenshot (pre-texture) and a post-load screenshot (used for color share), and `style.css`, `index.html` and `codebackground.js` read directly, on 2026-10-28.
