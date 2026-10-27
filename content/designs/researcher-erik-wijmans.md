# Erik Wijmans — Style Reference

> A tidy research portfolio under a slate-navy bar: big airy Roboto headings, numbered research themes, and paper cards laid on alternating grey bands like files on a light table.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, DOM-order anatomy, loaded fonts, first-viewport color share), the 1440×900 and full-page screenshots, and the site's `/styles.css` (the Hugo Academic theme, 2020 era, on Bootstrap 3.3.7) and the markup read directly. Roboto loads only in 400, 400 italic and 700, so the theme's 500 headings and 300 portrait titles render in Roboto 400 and its 600 nav links render in 700. Every `.home-section` fades in with a 0.3s `intro` animation; the 1440×900 capture was taken mid-fade, so its text looks paler than it is, and the full-page shot shows the settled colors used below.

## Overview

A Bootstrap 3 page with a fixed 71px navigation bar in slate navy #2c3e50: "Erik Wijmans" in 20.4px bold off-white #ecf0f1 at the left, six bold 15px links at the right, the current one ("Home") in grey #7f8c8d. Sections run full width in alternating bands of white and #f7f7f7, each with 50px of vertical padding. The About band is a two-column profile: a 200px circular portrait centred over the name (29.75px, light) and affiliation in 54% black, with a row of 34px blue #2980b9 icons (envelope, Twitter, Google Scholar, GitHub, CV); to the right a 38.25px "About Me" heading in #313131, 17px body text in 80% black with blue links, and two sub-columns for Interests (bullets) and Education (graduation-cap list). "Select Publications" is grouped under numbered theme headings ("1) Characterizing Emergent Intelligence") at the same 38.25px size. Each paper is a white card with a 1px 9% black border and 3px corners: a 29.75px title in near-black, blue author line, green venue and acceptance-rate line, red award lines, small outlined blue buttons, and a teaser image up to 200px tall on the right. Talks, Press Coverage (logos beside one-line descriptions) and Awards follow, then a grey footer credit.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): #ffffff 67.6% (About band), #fdfdfd 12.2% (About band during the fade), #364758 7.7% (navigation bar #2c3e50), #e7e7e8 5.4% (faded text and portrait), #f9fafa 4.9% (top of the #f7f7f7 publications band). Blue #2980b9 is the only accent and covers under 1%.

Anatomy in DOM order (desktop 1440px; Bootstrap container 1170px, content x=150–1290):

1. **Navigation bar** (`nav.navbar-default`, fixed, y=0–71): #2c3e50, shadow 0 2.125px 4.25px rgba(0,0,0,0.11); brand (x=135) Roboto 20.4px/700 #ecf0f1, line-height 50px, padding 10px 15px; links Roboto 15px/700 #ecf0f1, padding 10px 15px; active "Home" #7f8c8d. Body margin-top 71px.
2. **About band** (`section.home-section`, y=71–790, #ffffff, padding 50px 0).
3. **Portrait** (`#profile .portrait`, left column, centred at x≈330, y≈150): 200×200, border-radius 50%, background-image cover.
4. **Name** (`.portrait-title h2`, y=371): Roboto 29.75px (declared 300, renders 400), #000000, centred, margin 20px 0 10px. Gap 10px.
5. **Affiliation** (`.portrait-title h3`, y=418): Roboto 17px, rgba(0,0,0,0.54), centred. Gap 53px.
6. **Icon row** (`ul.network-icon`, y=492): five 2rem (34px) icons in #2980b9, 10px apart, scale 1.2 on hover.
7. **"About Me"** (`h1`, right column x=540, y=141): Roboto 38.25px (declared 500, renders 400), line-height 1.25, #313131. Gap 8px.
8. **Bio** (`p`, y=197 and 327, 750px wide): Roboto 17px/400, line-height 1.65 (28.05px), rgba(0,0,0,0.8); links #2980b9. Gap 17px.
9. **Interests / Education** (`h3`, y=445): Roboto 21.25px, #313131, in a 5/7 split; Interests bullets 15.3px; Education uses graduation-cap icons in the body ink with 15.3px course and 12.75px rgba(0,0,0,0.6) institution lines. Band ends at y=790.
10. **"Select Publications"** (`h1`, y=840) on the #f7f7f7 band, at the fold.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Slate Navy | #2c3e50 | (literal) | navigation bar background |
| Cloud | #ecf0f1 | (literal) | brand and nav link text |
| Nav Grey | #7f8c8d | (literal) | active nav link, nav link hover |
| Link Blue | #2980b9 | (literal) | links, profile icons, publication author line, outlined buttons (border and text), button hover fill |
| Heading Ink | #313131 | (literal) | h1, h2, h3 headings |
| Title Ink | #151515 | (literal) | publication and talk titles |
| Body Ink | rgba(0,0,0,0.8) | (literal) | body text |
| Soft Ink | rgba(0,0,0,0.54) | (literal) | affiliation under the portrait name |
| Fine Ink | rgba(0,0,0,0.6) | (literal) | Education institution lines |
| Venue Green | #27ae60 | (literal) | publication venue and acceptance-rate line |
| Award Red | #e74c3c | (literal) | publication award lines (oral, outstanding paper) |
| Band Grey | #f7f7f7 | (literal) | even sections: Select Publications, Talks, Awards |
| Card Edge | rgba(0,0,0,0.09) | (literal) | publication card border |
| Footer Grey | #899596 | (literal) | footer text and back-to-top arrow |
| Name Black | #000000 | (literal) | name under the portrait |
| White | #ffffff | (literal) | odd sections, publication cards |

Declared but not visible: the theme's `.dark` palette (Dracula greys), `.card` image cards, `ul.share` circles (#b5c6ce) and the striped table colors.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Roboto', sans-serif (Google Fonts 400, 400italic, 700; Montserrat and Roboto Mono also requested) | Roboto 400, 400 italic, 700 | Heebo |
| Icons | Font Awesome 4.7, Academicons 1.8.6 | FontAwesome, Academicons 400 | — |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Brand | `.navbar-default .navbar-brand` | 1.2em = 20.4px / 700 / 50px | #ecf0f1 |
| Nav link | `.navbar-nav > li > a` | 15px / 600 declared, 700 rendered / 50px | #ecf0f1 (active #7f8c8d) |
| Section and theme heading | `h1`, `h1.section-heading` | 2.25rem = 38.25px / 500 declared, 400 rendered / 1.25 | #313131 |
| "All Publications »" | `.view-all h2` (inside the link) | 1.5rem = 25.5px / 400 rendered | #313131 (the h2 color beats the link); the second, plain-text instance is 18.7px #2980b9 |
| Sub-heading | `h3` | 1.25rem = 21.25px / 400 rendered | #313131 |
| Portrait name | `#profile .portrait-title h2` | 1.75em = 29.75px / 300 declared, 400 rendered | #000000 |
| Affiliation | `#profile .portrait-title h3` | 1rem = 17px / 400 rendered | rgba(0,0,0,0.54) |
| Body | `html`, `p` | 17px / 400 / 1.65 | rgba(0,0,0,0.8) |
| Publication title | `.pub-list-item h3.article-title` | 1.75rem = 29.75px / 400 rendered / 1.25 | #151515 |
| Authors | `.pub-list-item .pub-authors` | 0.9rem = 15.3px / 400 / normal; own name 700 | #2980b9 |
| Venue line | `.pub-list-item .pub-publication` | 15.3px / 400 / normal | #27ae60 |
| Award line | `.pub-list-item .pub-awards` | 15.3px / 400 | #e74c3c |
| Button | `.btn-xs.btn-outline` | 12px / 400 / 18px | #2980b9 |
| Footer | `footer p` | 0.75rem = 12.75px, centred | #899596 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Navigation bar | 0 | none | 0 2.125px 4.25px rgba(0,0,0,0.11) |
| Portrait | 50% | none | none |
| Publication card | 3px | 1px rgba(0,0,0,0.09) | 0 1px 4px rgba(0,0,0,0.04) |
| Outlined button | 3px | 1px #2980b9 | none |
| Teaser image | 0 | none | none |
| Sections | 0 | none | none |

## Layout Metrics

- **Container**: Bootstrap 3 `.container` 1170px at ≥1200px (15px gutters), content 1140px from x=150 at 1440.
- **Body offset**: margin-top 71px under the fixed bar (51px at ≤1200px).
- **Sections**: `.home-section` padding 50px 0, alternating #ffffff / #f7f7f7 by `:nth-of-type(even)`.
- **About**: `#profile` column (col-md-4) centred with padding 30px 10px; text column col-md-8 (750px); Interests col-sm-5, Education col-sm-7.
- **Publication card**: `.card-simple` padding 10px 15px, margin-top 10px; inner row col-md-8 text + col-md-3 teaser (`.pub-banner` max-height 200px, centred); links row padding-top 8.5px.
- **Talks / Press / Awards**: section heading in col-md-3 at left, content in col-md-9; press logos max-height 30px in col-xs-3.
- **Footer**: margin-top 68px (4rem), padding 34px 0. Page height 8,476px at 1440.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| ≥1201px | 15px in a 1170px container | 17px | h1 38.25px | full nav bar, two-column About, card text 8/12 + teaser 3/12 |
| 992–1200px | 15px in 970px | 17px | 38.25px | nav collapses to a hamburger (bar 50px tall, links 40px line-height); grid unchanged |
| 928–991px | 15px in 750px | 17px | 38.25px | col-md columns stack: portrait above About, teaser below card text, section headings above content |
| ≤927px (58em) | 15px | 15px root | 2.25rem = 33.75px | all rem sizes scale down from the 15px root |
| ≤768px | 15px, fluid | 15px | 33.75px | sections padding 60px 0 (first 40px top) |

## Components

- **Navy navbar**: fixed, #2c3e50, min-height 70px, shadow 0 2.125px 4.25px rgba(0,0,0,0.11); bold brand left; bold 15px #ecf0f1 links right, padding 10px 15px, hover and active #7f8c8d with a 0.2s transition; collapses to a hamburger at ≤1200px.
- **Profile column**: 200px circle, 29.75px name, 17px rgba(0,0,0,0.54) affiliation, inline-flex row of 34px #2980b9 icons (10px apart, scale 1.2 on hover), centred.
- **Education list**: Font Awesome graduation-cap bullets, 15.3px course line, 12.75px rgba(0,0,0,0.6) institution line.
- **Theme heading**: an `h1.section-heading` with a numbered label ("2) Large-scale Machine Learning") at 38.25px #313131, margin 20px 0 8.5px, directly above its cards.
- **Publication card** (`.pub-list-item.card-simple`): #ffffff, 1px rgba(0,0,0,0.09), 3px radius, shadow 0 1px 4px rgba(0,0,0,0.04), padding 10px 15px, 10px apart; left 8/12: 29.75px #151515 title (hover #2980b9, 0.6s), 15.3px #2980b9 authors with own name bold, 15.3px #27ae60 venue plus acceptance rate, optional 15.3px #e74c3c award lines, then outlined buttons; right 3/12: teaser up to 200px tall, centred.
- **Outlined button** (`.btn-primary.btn-outline.btn-xs`): transparent, 1px #2980b9, 3px radius, padding 1px 5px, 12px #2980b9 label (Paper, Code, Project, Video, Press Coverage); hover #ffffff text on #2980b9, 0.5s.
- **Press row**: logo up to 30px tall at left (col-xs-3), one-line text with the outlet as a #2980b9 link (col-xs-8); grouped under 38.25px headings with an `<hr>`.
- **Footer**: "© 2020 · Powered by the Academic theme for Hugo." in 12.75px #899596, centred, with a back-to-top chevron at the right.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Fixed navigation | yes | slate-navy bar with in-page anchors |
| Profile with portrait and icons | yes | circle portrait, light name, blue icon row |
| About, interests, education | yes | 17px text, bullet list, cap-icon list |
| Selected publications by theme | yes | numbered 38.25px theme headings over white cards |
| Acceptance rates and awards | yes | green venue line and red award lines inside cards |
| Talks | yes | title, date, Video button, title-slide image |
| Press coverage | yes | outlet logos with one-line descriptions |
| Awards | yes | list on a grey band |
| News | absent from the source | — |
| Footer | yes | grey theme credit |

## Adapting to Other Content

- **Long publication lists**: keep grouping by theme with numbered 38.25px headings; within a theme, cards stay 10px apart on the grey band so the band itself frames the group.
- **Papers without teasers**: leave the right column empty rather than stretching the text; the card height then follows the text.
- **News**: add a white-band section with the col-md-3 heading / col-md-9 content split used by Talks, one 17px line per item with a bold date.
- **More awards per paper**: stack additional #e74c3c lines; keep them above the buttons.
- **Students or collaborators**: reuse the press row pattern with a small square photo in place of the logo.

## Do's and Don'ts

- Do alternate full-width bands of #ffffff and #f7f7f7 for every section.
- Do keep #2980b9 as the single interactive color, with #27ae60 and #e74c3c reserved for venue and award lines inside cards.
- Do size headings large and light; weight comes from size, not boldness.
- Don't round the cards beyond 3px or deepen their shadow; they should read as flat sheets.
- Don't put color in the nav bar beyond #ecf0f1 and #7f8c8d.
- Don't load Roboto 500 if you want to match the render; the headings are Roboto 400.

## Surfaces

A slate-navy fixed bar, then full-bleed alternating white and #f7f7f7 bands; white publication cards with hairline borders sit on the grey bands.

## Imagery

A circular portrait, diagrammatic paper teasers (architecture figures, plots, simulator renders, top-down navigation maps), talk title slides, and press outlet logos.

## Layout

Fixed bar, About band, Select Publications (four numbered themes), Latest Publications, Talks, Press Coverage, Awards, footer. About 8,476px tall at 1440.

## Agent Prompt Guide

Quick colors: navbar #2c3e50 with #ecf0f1 text (active #7f8c8d), links #2980b9, headings #313131, titles #151515, body rgba(0,0,0,0.8), venue #27ae60, award #e74c3c, band #f7f7f7, card edge rgba(0,0,0,0.09), footer #899596.

1. "Build a fixed navbar: #2c3e50, 70px tall, box-shadow 0 2.125px 4.25px rgba(0,0,0,0.11); brand Roboto 20.4px/700 #ecf0f1 at left; links Roboto 15px/700 #ecf0f1, padding 10px 15px, line-height 50px, active and hover #7f8c8d."
2. "Make a publication card on a #f7f7f7 band: #ffffff, 1px solid rgba(0,0,0,0.09), 3px radius, box-shadow 0 1px 4px rgba(0,0,0,0.04), padding 10px 15px; left two-thirds: Roboto 29.75px/400 #151515 title, 15.3px #2980b9 authors with the owner bold, 15.3px #27ae60 venue and acceptance rate, optional 15.3px #e74c3c award line, outlined buttons (12px #2980b9, 1px #2980b9 border, 3px radius, padding 1px 5px; hover #ffffff on #2980b9); right quarter: teaser image up to 200px tall."
3. "Create a profile column: centred 200px circular portrait; name Roboto 29.75px/400 #000000 margin 20px 0 10px; affiliation 17px rgba(0,0,0,0.54); a row of 34px #2980b9 icons 10px apart that scale to 1.2 on hover."

## Similar Pages

- Hugo Academic theme sites from 2018–2020 with the classic navy bar and alternating section bands.
- Embodied AI researcher pages that group papers by research theme.

## Quick Start

```css
:root {
  --navbar: #2c3e50;
  --navbar-text: #ecf0f1;
  --navbar-active: #7f8c8d;
  --link: #2980b9;
  --heading: #313131;
  --title: #151515;
  --venue: #27ae60;
  --award: #e74c3c;
  --band: #f7f7f7;
}
html { font: 400 17px/1.65 'Roboto', sans-serif; color: rgba(0,0,0,0.8); }
h1, h2, h3 { font-weight: 400; line-height: 1.25; color: var(--heading); }
h1 { font-size: 2.25rem; }
.home-section { padding: 50px 0; background: #ffffff; }
.home-section:nth-of-type(even) { background: var(--band); }
.card-simple { background: #ffffff; border: 1px solid rgba(0,0,0,0.09); border-radius: 3px; box-shadow: 0 1px 4px rgba(0,0,0,0.04); padding: 10px 15px; margin-top: 10px; }
```

## Provenance

- **URL**: https://wijmans.xyz/
- **Person**: Erik Wijmans (embodied AI, navigation).
- **Venue / award**: ICLR 2023 Outstanding Paper, "Emergence of Maps in the Memories of Blind Navigation Agents".
- **Selection reason**: award rule (first/last author). https://blog.iclr.cc/2023/03/21/announcing-the-iclr-2023-outstanding-paper-award-recipients/
- **Template credit**: footer says "Powered by the Academic theme for Hugo".
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, anatomy, fonts_loaded, color share), the 1440×900 shot (captured during the section fade-in) and the full-page shot, and `/styles.css` and the markup read directly, on 2026-10-28.
