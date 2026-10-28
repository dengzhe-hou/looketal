# Tiny Is Not Small Enough — Style Reference

> A studio title card: white headline type floating over a looping swirl of magenta and violet wire, then a quiet gray paper underneath.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share), extra computed-style probes of the cover, author lines, buttons, section containers and footer, the 1440×900 and full-page screenshots, and the page's own `index.html` (with a 100-line inline `<style>` block) and `static/css/index.css` read directly. The page is the Academic Project Page Template (Bulma 0.9, Nerfies lineage) with a custom full-bleed video cover. The cover height is `60vh`, so it renders 540px tall in a 900px window and grows in taller windows (the full-page shot was taken at a taller viewport and shows a taller cover). The "Real-time demo" video rendered as a black frame in the capture because its `<video>` has `controls muted loop` but no `autoplay` and an empty `poster`.

## Overview

A full-width 540px cover plays an Electronic Arts SEED brand video (a swirl of thin magenta, violet and deep-blue metallic strands on black). Over it, centred, sit a 500px white SEED logo mark and a two-part white title in Google Sans 48px/600: "TINY IS NOT SMALL ENOUGH:" on one line and the subtitle on two lines. Below the cover, on white, come centred sky-blue (#209cee) author names at 24px, a 24px gray (#4a4a4a) two-line affiliation and venue block, and three dark Bulma pill buttons with Font Awesome icons. A white teaser section shows a 912px "Real-time demo" video. From the Abstract down, every section uses Bulma's `is-light` hero, so the rest of the page is one long #f5f5f5 gray band: a justified 763px abstract, a 16:9 talk video with 10px rounded corners, a Pipeline section with 24px/600 stage headings and diagrams, a sequence of full comparison videos and related links. BibTeX sits on white in a #f5f5f5 code block, and the footer is #fafafa.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): white #ffffff 32.5% (plus #fdfffe 4.4%); black #000000 17.8% (the black demo-video frame and the cover's darkest areas); cover video tones plum #3e0340 15.2%, navy-black #000028 15.0%, #060123 7.9%, mauve #886391 7.1%. The cover is a video frame, so these tones shift as it plays.

Anatomy in DOM order (desktop 1440px, everything centred):

1. **Video cover** (`div.video-cover`, 0–540px): `height: 60vh`, overflow hidden; the `<video>` is absolutely centred with `min-width: 100%; min-height: 100%; transform: translate(-50%, -50%); object-fit: cover`, so it renders 1440×810 and is cropped top and bottom (top edge at y=-135).
2. **Overlay block** (`div.content-on-top`, y=72–468): absolutely centred with `transform: translate(-50%, -50%)`, max-width 90% (1296px), padding 0 16px, white, text-align centre.
3. **Logo** (`img.logo`, y=72, 500×154): white SEED glyph mark on a transparent PNG. Gap 56px (h1 inline margin-top 50px plus line-box offset).
4. **Title line 1** (`h1.title.is-1.publication-title`, y=282, 54px): "TINY IS NOT SMALL ENOUGH:" in Google Sans 48px/600, line-height 54px, #ffffff, uppercase as typed. Gap 24px (Bulma `.title` margin-bottom 1.5rem).
5. **Title lines 2–3** (second `h1`, y=360, 108px): "High quality, low-resource facial animation / models through hybrid knowledge distillation" in the same 48px/600 white, broken by a `<br>`. Cover ends at 540. Gap 10px.
6. **Authors** (`div.publication-authors.is-size-4`, y=550, 36px): four names in Google Sans 24px/400, links #209cee (`hsl(204, 86%, 53%) !important`), comma separators #4a4a4a; hover underline. Gap 10px.
7. **Affiliation and venue** (y=596, 72px): "SEED, Electronic Arts, Stockholm, Sweden" / "ACM Transactions on Graphics 2025", Google Sans 24px/400 #4a4a4a, two lines. Gap 17px.
8. **Buttons** (`a.button.is-dark.is-rounded`, y=685, 40px tall): Paper, Supplementary material, arXiv; #363636 fill, white 16px/400 Noto Sans, padding 7px 20px, fully rounded, 24px icon box with Font Awesome / Academicons glyph on the left; 4px between pills. Gap 17px.
9. **Teaser section** (`section.hero.teaser`, from y=742): "Real-time demo" h2 Google Sans 32px/600 #363636 at y=792 (inline margin-top 50px), then a 912×513 video at y=852.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Cover Plum | #3e0340 | (video frame) | darker magenta strands of the cover video |
| Cover Night | #000028 | (video frame) | deep navy-black right side of the cover video |
| Cover Mauve | #886391 | (video frame) | lit violet strands of the cover video |
| White | #ffffff | (Bulma `$white`) | page background above the abstract, cover title and logo, button text, BibTeX section |
| Author Sky | #209cee | `hsl(204, 86%, 53%)` | author name links |
| Body Gray | #4a4a4a | (Bulma `$text`) | body text, affiliation and venue lines, BibTeX text, footer text |
| Title Charcoal | #363636 | (Bulma `$text-strong`, `$dark`) | "Real-time demo" heading, button fills |
| Light Band | #f5f5f5 | (Bulma `$light`) | Abstract, video, Pipeline, Full videos and Related links sections; BibTeX code block |
| Band Ink | rgba(0,0,0,0.7) | (Bulma `.hero.is-light` text) | headings and body text inside the gray sections |
| Footer Gray | #fafafa | (Bulma `$scheme-main-bis`) | footer |
| Link Blue | #3273dc | (Bulma `$link`) | footer and in-text links |

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Display | 'Google Sans', sans-serif (`.publication-title`, `.publication-authors`, `.teaser`) | Google Sans 400 (bold weights are synthesized from the single loaded face) | Product Sans |
| Text | 'Noto Sans', sans-serif (`body`) | Noto Sans 400 | Noto Sans |
| Code | monospace | system monospace (Consolas on Windows) | JetBrains Mono |
| Icons | Font Awesome 6 Free, Academicons | Font Awesome 6 Free 900, Academicons 400 | — |
| Math | MathJax 3 | MJXTEX fonts | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Cover title (both h1) | `.title.is-1.publication-title` | 48px / 600 / 54px | #ffffff |
| Teaser heading | `.teaser h2.title.is-3` | 32px / 600 / 36px, Google Sans | #363636 |
| Section heading | `.hero.is-light h2.title.is-3` | 32px / 600 / 36px, Noto Sans | rgba(0,0,0,0.7) |
| Stage heading | `h2.title.is-4` | 24px / 600 / 27px, inline margin 0 0 -5px 20px | rgba(0,0,0,0.7) |
| Authors | `.publication-authors.is-size-4 a` | 24px / 400 / 36px, Google Sans | #209cee |
| Affiliation / venue | `.publication-authors .author-block` | 24px / 400 / 36px | #4a4a4a |
| Body | `.content p` | 16px / 400 / 24px, justified | #4a4a4a on white, rgba(0,0,0,0.7) in gray bands |
| Button | `.button.is-normal` | 16px / 400 / 24px | #ffffff |
| BibTeX | `pre` | 14px / 400 / 21px monospace | #4a4a4a |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Link buttons | 290486px (Bulma `is-rounded`) | 1px solid transparent | none |
| Talk video wrapper (`.publication-video`) | 10px `!important` | none | none |
| Demo and result videos | 0px | none | none |
| BibTeX `pre` | 0px | none | none |
| Cover | 0px, full bleed | none | none |

`video { margin-bottom: 20px }` in the inline style adds 20px under every video. A `.button.is-transparent` recipe (rgba(255,255,255,0.2) fill, 2px solid rgba(255,255,255,0.5)) is declared for buttons on the cover but not used; all rendered buttons are `is-dark`.

## Layout Metrics

- **Cover**: `height: 60vh` → 540px at 1440×900; overlay max-width 90% = 1296px, padding 0 16px; logo fixed at 500px wide by inline style.
- **Below the cover**: the author and affiliation blocks span the full 1440px width, centred, each with inline margin-top 10px; the button row is a Bulma `.column` (padding 12px), links with 5px top and bottom margins.
- **Teaser**: `.teaser .hero-body { padding-top: 0; padding-bottom: 3rem }` inside `.container.is-max-desktop` (960px) → 912px video at x=264.
- **Gray sections**: `section.section` padding 48px 24px; `section.hero.is-small .hero-body` padding 24px 24px (Bulma `is-small`). Container widths: abstract `is-max-desktop` 960px with an `is-four-fifths` column → 763px text at x=338; Video Presentation full container 1344px with a four-fifths column → 1070px video at x=185; Pipeline and Full videos 960px.
- **Pipeline**: stage headings indented 20px; the Overview row is a flex `.split-container` (text flex 0.6, image flex 1) with a 350px diagram; stage diagrams at 1000px and 900px inline widths, capped by the 912px column.
- **Section rhythm**: headings carry inline margins (Pipeline margin-top 80px, Full videos 40px); there is no separation between gray sections because they share #f5f5f5.
- **Footer**: padding 48px 24px 96px, text column about 888px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1408px | container max 1344px; is-max-desktop 960px | 16px | 48px | all columns side by side |
| 1216–1407px | container 1152px | 16px | 48px | same |
| 1024–1215px | container 960px | 16px | 48px | same |
| ≤768px | 24px section padding, columns full width | 16px | 48px | Bulma columns stack; `.split-container` stacks text over image |
| any height | — | — | — | cover is 60% of the viewport height, so a short window clips the logo and title block |

## Components

- **Video cover**: relative 60vh box, overflow hidden; background `<video autoplay muted loop playsinline>` absolutely centred and `object-fit: cover`; overlay block absolutely centred with `translate(-50%, -50%)`, white text, max-width 90%, padding 0 16px. Logo 500px wide, then two `h1.title.is-1` in Google Sans 48px/600 white, the first 50px below the logo.
- **Author line**: full-width centred `div.is-size-4.publication-authors`, Google Sans 24px/400, names #209cee with comma separators in #4a4a4a, hover underline; the affiliation and venue are a second 24px block in #4a4a4a, no italic or superscripts.
- **Dark pill button** (`.button.is-normal.is-rounded.is-dark`): #363636 fill, white 16px/400 Noto Sans, height 40px, padding 7px 20px, radius 290486px, 1px transparent border, 24px icon span (margin 0 4px 0 -9px) holding a Font Awesome `fa-file-pdf` / `fa-file-video` or Academicons `ai-arxiv` glyph. Bulma hover darkens the fill slightly.
- **Gray section band** (`section.hero.is-small.is-light`): #f5f5f5, padding 24px, h2 32px/600 rgba(0,0,0,0.7) centred, body text justified.
- **Stage heading** (`h2.title.is-4`): 24px/600 rgba(0,0,0,0.7), left-aligned with a 20px indent and -5px bottom margin, followed by a justified paragraph and a full-width diagram.
- **Talk video** (`.publication-video`): 16:9 padding box (padding-bottom 56.25%), 10px radius, iframe fills it.
- **BibTeX**: white section, h2 32px/600, then a Bulma `pre` with #f5f5f5 fill, padding 17.5px 21px, 14px monospace #4a4a4a.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Full-bleed video cover | yes | 60vh looping brand video with centred logo and white title |
| Title | yes | two white Google Sans 48px/600 h1s over the video |
| Authors / affiliations | yes | sky-blue 24px names; gray 24px affiliation and venue lines |
| Venue | present but non-standard | written as plain text "ACM Transactions on Graphics 2025" in the affiliation block; no badge |
| Link buttons | yes | three dark Bulma pills with icons |
| Teaser video | yes | 912px demo video on white (captured as a black frame) |
| Abstract | yes | gray band, 763px justified text |
| Talk video | yes | rounded 16:9 embed in a 1070px column |
| Method diagrams | yes | Pipeline section with indented stage headings and full-width figures |
| Results videos | yes | stacked comparison videos under 24px headings |
| Results tables | absent from the source | results are videos only |
| Related links | yes | short gray-band list |
| BibTeX | yes | Bulma `pre` on white |
| Footer | yes | #fafafa, template credit and CC BY-SA licence |

## Adapting to Other Content

- **More authors**: keep the full-width 24px #209cee line; it wraps centred at about six names per line at 1440. Add affiliation numbers as plain superscripts in #4a4a4a rather than a second colour.
- **A results table**: put it in a gray band (`section.hero.is-small.is-light`) inside the 960px container; header row 16px/600 rgba(0,0,0,0.7), 1px #dbdbdb rules (Bulma table borders), white cells so the table lifts off the #f5f5f5 band, best values bold.
- **Long publication or news lists**: a gray band with a 32px/600 centred heading and a left-aligned list at 16px, dates in 600 weight; no cards.
- **No brand video**: keep the 60vh full-bleed cover with any dark looping or still image set to `object-fit: cover`; the white 48px title needs a dark ground for contrast.
- **More links**: add more `is-dark` pills on the same centred row; at 1440 about seven fit on one line.

## Do's and Don'ts

- Do keep the cover full bleed, 60vh tall, dark, with the logo and title centred over it in white.
- Do set the title and author lines in Google Sans and everything below in Noto Sans.
- Do keep author names #209cee and the affiliation block #4a4a4a, both at 24px.
- Do put every content section from the Abstract on in the #f5f5f5 band; only the teaser and BibTeX sit on white.
- Don't add a background colour or gradient behind the title; the video is the only ground.
- Don't use the transparent cover-button recipe for the main links; the rendered buttons are #363636 pills below the cover.
- Don't round the result videos; only the talk embed has a 10px radius.

## Surfaces

A dark full-bleed video cover, then a white strip for authors, buttons and the teaser, then one continuous #f5f5f5 band for all content sections, a white BibTeX section and a #fafafa footer. No cards, no shadows.

## Imagery

An abstract generative-art brand loop (thin metallic strands in magenta #3e0340 to violet #886391 on navy-black #000028) as the cover; below, side-by-side facial-animation comparison videos, pipeline block diagrams on white, and a talk video. Media is shown at column width with no frames.

## Layout

A cinematic opener (60vh cover) followed by a centred, single-column Bulma page: full-width author lines, a 960px teaser, then gray sections whose columns range from 763px (abstract) to 1070px (talk video).

## Agent Prompt Guide

Quick colors: cover video tones #3e0340 / #000028 / #886391, title #ffffff, authors #209cee, body #4a4a4a, headings #363636, gray band #f5f5f5, footer #fafafa, links #3273dc.

1. "Build a full-bleed cover: a relative div with height 60vh and overflow hidden; a looping muted video absolutely centred with min-width and min-height 100%, translate(-50%, -50%) and object-fit cover; on top, an absolutely centred block (max-width 90%, padding 0 16px, white, centred) holding a 500px logo and two h1s in Google Sans 48px/600 line-height 54px #ffffff, 24px apart, the first 50px below the logo."
2. "Below the cover, centred on white: authors in Google Sans 24px/400 with names #209cee (hover underline) and commas #4a4a4a; then a 24px #4a4a4a two-line affiliation and venue block, each block 10px below the previous; then dark pill buttons: background #363636, white 16px Noto Sans, padding 7px 20px, radius 290486px, 24px icon on the left."
3. "Make content sections as gray bands: background #f5f5f5, padding 24px, a centred 32px/600 heading in rgba(0,0,0,0.7), a 960px container, justified 16px Noto Sans text, and 24px/600 stage subheadings indented 20px. Embed the talk video in a 16:9 box with 10px radius."

## Similar Pages

- Nerfies / Academic Project Page Template pages that replace the plain white hero with a full-bleed video banner.
- Industry research-lab pages (game studios, VFX labs) that open with a branded motion loop and logo.

## Quick Start

```css
:root {
  --cover-height: 60vh;
  --cover-plum: #3e0340;
  --cover-night: #000028;
  --title: #ffffff;
  --author: #209cee;
  --text: #4a4a4a;
  --text-strong: #363636;
  --band: #f5f5f5;
  --band-ink: rgba(0, 0, 0, 0.7);
  --footer: #fafafa;
  --link: #3273dc;
  --font-display: "Google Sans", sans-serif;
  --font-text: "Noto Sans", sans-serif;
  --radius-pill: 290486px;
  --radius-video: 10px;
  --container: 960px;
}
```

## Provenance

- **URL**: https://electronicarts.github.io/tiny-voice2face/
- **Paper**: Tiny is not small enough: High-quality, low-resource facial animation models through hybrid knowledge distillation (arXiv 2507.18352), Zhen Han, Mattias Teye, Derek Yadgaroff, Judith Bütepage (SEED, Electronic Arts).
- **Venue**: SIGGRAPH 2025 (ACM TOG journal track; the page itself says "ACM Transactions on Graphics 2025").
- **Selection reason**: the arXiv comment states "Accepted to ACM TOG 2025 (SIGGRAPH journal track)" and links this page; chosen as the only cinematic, poster-like opener in the pool, with a full-bleed generative-art cover and centred metadata below. Flaw: the demo video renders as a black frame until played.
- **Template credit**: footer credits the Academic Project Page Template, adapted from Nerfies (Bulma 0.9, Font Awesome, Academicons, MathJax 3).
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share), extra computed-style probes, the 1440×900 and full-page screenshots, and the page's `index.html` inline style and `static/css/index.css` read directly, on 2026-10-28.
