# Presto Cinema Hero — Style Reference

> The lights go down, the film is already rolling, and the title card waits at left.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), the 1440×900 screenshot, a scrolled capture of the full 4,570px page, a 390px-wide render for the responsive check, the page's own `static/css/index.css` and its markup. The page is built on the Nerfies Bulma template (Bulma 0.9 with bulma-carousel), so Bulma defaults supply the body colors; the hero, nav and buttons are the authors' own CSS. Color share is measured on the first 1440×900 viewport, which is entirely video.

## Overview

The whole first screen is a generated video. A `header.video-header` is 100vh tall, an autoplay muted loop (`teaser_compress.mp4`, a boy cycling through a stone archway toward a sunlit courtyard) is set `object-fit: cover` behind a 30% white wash, and the left 30% of the screen carries a black 64px "Presto", a 24px bold tagline and three outlined pill buttons. A fixed, 85%-opaque white bar runs across the top with eight evenly spaced section links in Bulma blue, the first ("Presto") in a pink #ff6a83 bold. Scrolling past the video reveals a conventional Nerfies page: a centred 48px Google Sans paper title in #363636, sky-blue author links, two side-by-side teaser videos with a small-caps caption, a #f5f5f5 carousel band of six rounded video cards, then Abstract, Architecture, LongTake-HD, Long Video, Related Links and BibTeX in a 960px column, and a #fafafa footer.

## First Viewport

Color share (1440×900, 8-color quantize, all from the washed video frame): graphite #504d4d 21.5%, brown-grey #554f4d 15.4%, rosewood #604f4d 15.0%, umber #785f4e 14.8%, washed sky #ddd7ca 12.3%, taupe #625752 9.7%, sandstone #92816e 9.6%, shadow #393635 1.7%. The nav bar, text and buttons together are under 3%.

Anatomy in DOM order:

1. **Nav bar** — `nav#navbar`, fixed, full width, 32px tall (y=0–32), background #ffffff at opacity 0.85 (the whole bar, links included), padding 4px, shadow `0 3px 6px rgba(0,0,0,0.1)`, `display: flex; justify-content: space-around`. Links Noto Sans 16px / 400 #3273dc; the first link wraps its label in an inline span, bolder and #ff6a83.
2. **Background video** — `video.background-video`, absolute, 1440×900, `object-fit: cover`, z-index -1; `header::before` lays rgba(255,255,255,0.3) over it.
3. **Display name** — `.content-overlay h1`, "Presto", Noto Sans 64px (4rem) / 700 / line-height 96px, #000000, left aligned, x=72 (left 5%), y=405–501. The overlay box is positioned `top: 45%; left: 5%; right: 65%`, so it is 432px wide. Gap 0.
4. **Tagline** — `.content-overlay p`, Noto Sans 24px (1.5rem) / 700 / 36px, #000000, three lines in the 432px box, y=501–609. Gap 18px.
5. **Buttons** — three `a.cta-button` ("Paper" with Font Awesome file-pdf, "Code" and "Allegro" with the GitHub mark), 16px / 700 #000000, transparent fill, 1.5px solid #000000 border (renders 1px at 1×), radius 15px, padding 6px 12px, margin 2dvh 0 (18px at 900px), 4px inline gaps; y=627–667.
6. **Below the fold** — the paper title starts at y=948, 48px under the video.

## Tokens — Colors

| Name | Value | Token | Applies to |
|---|---|---|---|
| Paper | #ffffff | Bulma `html` background | page background below the hero, nav bar fill (at 0.85 opacity) |
| Hero Ink | #000000 | `.content-overlay h1, p`, `.cta-button` | display name, tagline, button text and border |
| Body Grey | #4a4a4a | Bulma body color | abstract, captions, author line separators, affiliation, footer text, BibTeX |
| Heading Charcoal | #363636 | Bulma `.title` | paper title, section h2s |
| Bulma Link | #3273dc | Bulma `a` | nav links, Related Links list, footer links |
| Presto Pink | #ff6a83 | inline span in `#navbar` | first nav item "Presto" |
| Author Sky | #209cee | `.publication-authors a` (hsl(204,86%,53%)) | author names |
| Band Grey | #f5f5f5 | Bulma `.hero.is-light`, `pre` | gallery carousel band, BibTeX box |
| Footer Haze | #fafafa | Bulma `.footer` | footer band |
| Card Edge | #bbbbbb | `.results-carousel .item` border | 1px border of carousel video cards |
| Arrow Shadow | #323232 | bulma-carousel nav buttons | `0 2px 5px rgba(50,50,50,0.1)` under the white round arrows |
| Hero Wash | rgba(255,255,255,0.3) | `.video-header::before` | translucent layer over the hero video |
| Frame Graphite | #504d4d | (video frame) | dominant tone of the hero video in the first viewport |

## Tokens — Typography

- **Sans (body):** declared `'Noto Sans', sans-serif` on `body`. Rendered: Noto Sans 400 only (Google Fonts `css?family=Google+Sans|Noto+Sans|Castoro` requests no weights), so every 600/700 heading and the bold hero text is browser-synthesized bold. Substitute: Noto Sans with real 600/700.
- **Display (title block):** declared `'Google Sans', sans-serif` on `.publication-title`, `.publication-authors` and `.teaser`. Rendered: Google Sans 400. Substitute: Product Sans is unavailable, use Outfit.
- **Castoro:** requested, never applied.
- **Mono:** BibTeX `pre` uses the browser `monospace` at 14px. Substitute: JetBrains Mono.
- **Icons:** Font Awesome 5 (SVG via `fontawesome.all.min.js`).

| Role | Selector | Size / weight / line-height |
|---|---|---|
| Hero display name | `.content-overlay h1` | 64px / 700 / 96px, Noto Sans |
| Hero tagline | `.content-overlay p` | 24px / 700 / 36px, Noto Sans |
| Hero buttons | `.cta-button` | 16px / 700 / 24px |
| Nav links | `#navbar a` | 16px / 400 / 24px |
| Paper title | `h1.title.is-1.publication-title` | 48px / 600 / 54px, Google Sans, centred |
| Authors, affiliation | `.is-size-5.publication-authors` | 20px / 400 / 30px, Google Sans, centred |
| Teaser caption | `h2.subtitle span.dnerf` | 20px / 400 / 25px, `font-variant: small-caps`, Google Sans |
| Section titles | `h2.title.is-3` | 32px / 600 / 36px, Noto Sans; centred except Related Links and BibTeX (left) |
| Body | `.content p` | 16px / 400 / 24px, justified, 16px bottom margin |
| BibTeX | `pre` | 14px / 400 / 21px monospace |

## Tokens — Spacing & Shapes

| Element | Value |
|---|---|
| Hero buttons | radius 15px, 1.5px solid #000000, padding 6px 12px, no shadow |
| Carousel cards | radius 10px, 1px solid #bbbbbb, margin 5px, `overflow: hidden` |
| Carousel arrows | 42px white circles, 1px #ffffff border, shadow `0 2px 5px rgba(50,50,50,0.1)` |
| Nav bar | square, shadow `0 3px 6px rgba(0,0,0,0.1)` |
| BibTeX box | #f5f5f5, padding 17.5px 21px, square corners |
| Teaser videos, figures | square corners, no border |

## Layout Metrics

- **Hero:** `height: 100vh` (900px at 1440×900), full bleed; overlay `top: 45%; left: 5%; right: 65%` (x=72, width 432px at 1440).
- **Content container:** Bulma `.container.is-max-desktop`, max-width 960px, centred (x=240–1200 at 1440). The gallery uses the plain `.container` (max-width 1344px, margin 0 24px).
- **Title block:** `.hero-body` padding 48px 24px; title→authors 24px (title margin-bottom); authors and affiliation are stacked 30px lines.
- **Teaser pair:** `.video-container` flex, gap 10px, each `.media-wrapper` 50% (475×267 videos at 1440); caption follows, then `padding-bottom: 5rem` on the teaser hero body.
- **Gallery band:** `section.hero.is-light.is-small`, 305px tall, cards 438×247px, three visible, arrows at x=48 and the mirrored right edge.
- **Sections:** `section.section` padding 48px 24px; abstract sits in `.column.is-four-fifths` (787px wide incl. 12px padding, text 763px); h2 margin-bottom 24px; architecture figure 842px wide centred.
- **Footer:** padding 48px 24px 96px, text block 888px.

| Breakpoint | Gutter | Body | Title | Grid change |
|---|---|---|---|---|
| ≥1024px | auto (960px column) | 16px | 48px | teaser videos side by side, three carousel cards |
| 769–1023px | 24px | 16px | 48px | Bulma container goes fluid; carousel still three cards |
| ≤768px | 24px | 16px | 48px | carousel drops to two cards at ≤640px and one at ≤480px (bulma-carousel defaults); the nav wraps to two rows (56px at 390); the hero overlay keeps 30% width (117px at 390), so "Presto" overflows and the tagline breaks one word per line; teaser videos stay side by side at 190px |

## Components

- **Full-bleed video hero:** `header` 100vh, flex; `<video autoplay loop muted playsinline>` absolute, cover, z-index -1; `::before` rgba(255,255,255,0.3) wash at z-index 0; text block absolute at top 45%, left 5%, right 65%, z-index 1, all #000000.
- **Outlined pill CTA:** `a.cta-button`, transparent background, 1.5px solid #000000, #000000 Noto Sans 16px / 700, padding 6px 12px, radius 15px, icon left inside `span.icon`; hover fills #ffffff with #000000 text over a 0.3s transition.
- **Section nav bar:** fixed top, #ffffff at opacity 0.85, 4px padding, `space-around` links in #3273dc 16px, first label bolder #ff6a83, shadow `0 3px 6px rgba(0,0,0,0.1)`; anchor jumps only, no active-state tracking.
- **Teaser pair:** two equal videos with a 10px gap in the 960px column, then a 20px small-caps Google Sans caption in #4a4a4a.
- **Video card carousel:** bulma-carousel on a #f5f5f5 band; each card a looping video with 1px #bbbbbb border and 10px radius; white circular arrows with a faint shadow; dot pagination below.
- **Code box:** BibTeX `pre` on #f5f5f5, 14px monospace #4a4a4a, padding 17.5px 21px.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Section nav | Yes | fixed translucent white bar, eight anchor links |
| Video hero | Yes | 100vh full-bleed generated video with left text overlay |
| Link buttons | Yes | three outlined pills on the video (Paper, Code, Allegro) |
| Title / authors / affiliation | Yes | Nerfies centred block below the hero, Google Sans |
| Teaser videos | Yes | two side-by-side loops with small-caps caption |
| Gallery carousel | Yes | six bordered video cards on a grey band |
| Abstract | Yes | 4/5 column, justified 16px |
| Method figure | Yes | Architecture: one wide diagram, no caption |
| Dataset figure | Yes | LongTake-HD frames-and-captions figure with paragraph |
| Long video comparison | Yes | two videos side by side with paragraph |
| Related links | Yes | left-aligned h2 and bullet list |
| BibTeX | Yes | grey pre |
| Results table | No (absent from the source) | |
| Venue badge | No (absent from the source) | CVPR 2025 is not stated on the page |
| Footer | Yes | #fafafa, CC BY-SA licence line, template credit |

## Adapting to Other Content

- **More authors:** they live in the post-hero title block, which is plain centred Google Sans 20px and wraps freely; keep the hero to the project name and one sentence.
- **Venue or award:** add a 16px / 700 #000000 line between the tagline and the pills inside the overlay, or a pill styled like the CTAs; avoid adding color on the video.
- **Results table:** place it in the 960px column under a 32px / 600 #363636 h2; Bulma `.table` with #4a4a4a text and the #f5f5f5 band behind it if it needs separation.
- **More sections:** each new section gets an anchor in the nav; past eight links the `space-around` bar crowds, so shorten labels.
- **Dark footage:** the #000000 overlay text depends on the 30% white wash; with dark footage raise the wash to 0.5 or switch the overlay text to #ffffff with a white-outlined pill.
- **News:** a short list in the 960px column before the gallery; the hero should stay text-light.

## Do's and Don'ts

- Do let the generated video fill the first viewport edge to edge with nothing but a short left overlay.
- Do keep the overlay monochrome (#000000 text, outlined pills) so the footage carries all the color.
- Do keep the translucent nav so section jumps are always one click away.
- Don't size the overlay with a percentage `right` inset alone; at phone width it collapses to 117px. Give it a min-width or let it go full width below 768px.
- Don't rely on synthesized bold; load Noto Sans 600/700 if the headings stay bold.
- Don't add borders or shadows to the teaser videos; only carousel cards are framed.

## Surfaces

A full-bleed video under a 30% white wash, then a white page with one #f5f5f5 carousel band, a #f5f5f5 BibTeX box and a #fafafa footer. The nav is translucent white with a soft drop shadow.

## Imagery

Generated 15-second clips: warm, sunlit stone archways, forest paths, waterfalls, cherry blossoms. Below the fold, a pastel transformer diagram with coloured token rows and a frames-plus-captions dataset figure with red highlighted phrases.

## Layout

A cinematic 100vh hero, then a standard Nerfies stack: centred title block, 960px column for teaser, abstract, figures and BibTeX, one full-width grey carousel band between them. Rendered height about 4,570px.

## Agent Prompt Guide

Quick colors: hero text and pill borders #000000 on video with a rgba(255,255,255,0.3) wash, nav links #3273dc with the brand label #ff6a83, title #363636, body #4a4a4a, authors #209cee, bands #f5f5f5, footer #fafafa.

1. "Build a 100vh hero: an autoplay muted looping video, object-fit cover, under a rgba(255,255,255,0.3) layer; at top 45% and left 5% (432px wide at 1440) place a 64px bold Noto Sans name in #000000, a 24px bold tagline (line-height 36px), and outlined pills: transparent, 1.5px solid #000000, radius 15px, padding 6px 12px, 16px bold, icon left, hover fill #ffffff."
2. "Add a fixed top nav: full width, #ffffff at opacity 0.85, padding 4px, shadow 0 3px 6px rgba(0,0,0,0.1), flex with space-around, 16px Noto Sans links in #3273dc, the first label bold in #ff6a83."
3. "Under the hero, put a centred 48px Google Sans title in #363636, 20px author links in #209cee, then a #f5f5f5 band with a carousel of looping video cards, each with a 1px #bbbbbb border and 10px radius."

## Similar Pages

- Nerfies-template pages that replace the teaser with a full-viewport background video.
- Product-style landing pages for video generation models (Sora-like hero video with left overlay copy).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --hero-ink: #000000;
  --hero-wash: rgba(255, 255, 255, 0.3);
  --text: #4a4a4a;
  --heading: #363636;
  --link: #3273dc;
  --brand: #ff6a83;
  --author: #209cee;
  --band: #f5f5f5;
  --footer: #fafafa;
  --card-border: #bbbbbb;
  --font-sans: 'Noto Sans', sans-serif;
  --font-display: 'Google Sans', sans-serif;
  --hero-name: 64px;
  --hero-tagline: 24px;
  --title-size: 48px;
  --h2-size: 32px;
  --body-size: 16px;
  --radius-pill: 15px;
  --radius-card: 10px;
  --column: 960px;
}
```

## Provenance

- **URL:** https://presto-video.github.io/
- **Paper:** Long Video Diffusion Generation with Segmented Cross-Attention and Content-Rich Video Data Curation (arXiv 2412.01316), Xin Yan et al., 01.AI.
- **Venue:** CVPR 2025.
- **Selection reason:** arXiv 2412.01316 comment states acceptance at CVPR 2025; project page linked in the abstract.
- **Template credit:** footer says the template is borrowed from Nerfies ("here") with some element designs from ContPhy.
- **Evidence used:** `tools/computed_style.py` render at 1440×900 with screenshot color share, the 1440×900 screenshot, scrolled full-page captures, a 390px render, `static/css/index.css`, page HTML; 2026-10-28.
