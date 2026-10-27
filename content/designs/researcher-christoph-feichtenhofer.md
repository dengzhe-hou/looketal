# Blue Banner Publications — Style Reference

> A conference-hall banner in Facebook blue, then a long ledger of papers in red ink, green venues and justified grey abstracts.

**Theme:** light

Values come from a headless Chrome render at 1440×900 (computed styles, loaded fonts, first-viewport color share and DOM boxes from `tools/computed_style.py`, plus a selector probe of the header, publication entries, news rows and the timeline), the 1440×900 and full-page screenshots, and `css/style.css` and `index.html` read directly. The page uses Bootstrap 3 (`css/bootstrap.min.css`) for the grid, `img-circle` and link colours. Roboto loads in 300, 400 and 500. Media are lazy videos (`video.lazy-video`, sources set by an IntersectionObserver), so the first video renders as an almost blank white poster in the 1440×900 capture. The page is 23,742px tall at 1440 wide.

## Overview

A full-width solid blue (#3b5998) banner, 500px tall, carries the identity: a 240px circular portrait with a 4px white ring, and to its right the name in Roboto 42px white, two light 18px lines (title and lab), a 16px light email and three 45–48px white outline icons (GitHub, LinkedIn, Google Scholar). The banner content starts at 30% of the viewport width rather than being centred. Below, on white, a centred italic grey heading "Recent technical reports · Google Scholar" opens a long publication list: each entry is a Bootstrap row split in half, media on the left (autoplaying videos or figures at full column width) and text on the right, with a 22px black title, 18px dark-red #990000 author list (own name bold), a 16px green #009900 venue, an 18px light justified abstract in #444444 and a row of small boxed links (paper, website, demo, blog, code with a GitHub star badge). Entries are separated by 1px #dddddd rules. Later sections use 50px light centred h2s ("News & Highlights", "Publications"), news rows as single 20px lines with rules, and a two-sided vertical timeline with a 5px #333333 spine.

## First Viewport

Color share (8-color quantization of the 1440×900 shot): banner blue #3b5998 47.8% plus #3b5a9a 1.7%, #3b5997 1.4%, #395a99 0.1%; white #ffffff 38.6%; light grey #dcd5d8 6.9% (portrait ring edges, blank video poster, anti-aliasing); dark slate #354057 2.4% and #4d5c79 1.0% (portrait and text over blue). The red author text and green venue below y=600 are under 1% each.

Anatomy in DOM order (desktop 1440px):

1. **Banner** (`#header.bg2`, y=0, 1440×500px): `linear-gradient(to top, white 0%, #3b5998 0%)`, which renders as solid #3b5998; margin-bottom 40px. It is an empty block; the content is absolutely positioned over it.
2. **Header blob** (`#headerblob`, absolute, left 30% = 432px, top 100px, width 70%).
3. **Portrait** (`img.img-circle.imgme`, x=432, y=80): 240px wide (246px tall incl. ring), `border-radius: 50%`, 4px solid #ffffff border, floated left with margin -20px 10px -20px 0.
4. **Name** (`#htname`, x=572, y=110): Roboto 42px/400, line-height 60px, #ffffff, left aligned. Gap 0 (margin-top -6px on the next line).
5. **Title and lab** (`#htdesc`, y=164, two lines): Roboto 18px/300, line-height 25.7px, #ffffff.
6. **Email** (`#htem`, y=215): Roboto 16px/300, #ffffff, "_at_" obfuscation. Gap 2px.
7. **Icons** (`#icons .svgico`, x=682, y=238): three white outline SVG images at 45px, 48px, 48px, about 3px apart. The banner ends at y=500; gap 60px.
8. **Section heading** (`.quote2 h3`, y=560): Roboto 24px/500 italic, #777777, centred; "Google Scholar" link at 0.8em (19.2px) in #428bca. Gap 10px.
9. **First publication** (`.pubwrap`, y=596): media column x=150, 566px wide (lazy video, blank in the capture); text column x=735, 555px wide: title 22px/400 #000000 at y=596, authors 18px #990000 from y=628, venue 16px #009900 at y=859, abstract 18px/300 justified #444444 from y=882.

## Tokens — Colors

| Name | Value | Token | Applies to (rendered elements) |
|---|---|---|---|
| Banner Blue | #3b5998 | (literal, `.bg2`) | 500px header band |
| Ring White | #ffffff | (literal) | portrait ring, name, title, email, icons, page background |
| Body Grey | #444444 | (literal, `html, body`) | abstracts, news rows, timeline text, h2 |
| Heading Grey | #777777 | `.quote2` | italic section h3 ("Recent technical reports", "Timeline") |
| Title Black | #000000 | `.pubt` | paper titles |
| Author Red | #990000 | `.puba` | author lists, own name in bold |
| Venue Green | #009900 | `.pubv` | venue line |
| Award Pink | #ee2556 | `.pubaw` | award / note line under some papers ("Best Paper Honorable Mention Award") |
| Date Maroon | #840000 | `.tdate` | timeline dates |
| Link Blue | #428bca | Bootstrap 3 `a` | inline links, "Google Scholar", boxed link labels |
| Rule Grey | #dddddd | `.pubwrap` | 1px separator under each publication and news row |
| Box Grey | #cccccc | `.publ li` | 1px border of the small link boxes |
| Spine | #333333 | `.timelineitem` | 5px timeline spine and 11px dots |

Declared but not visible: `#sitefooter` (#f1f3f4), `.thigh` (#000266), `#topnav`, `#showmoreprojects` and the `.pp` project cards are defined but not used on the current page.

## Tokens — Typography

| Family | Declared | Rendered (fonts_loaded) | Substitute |
|---|---|---|---|
| Sans (everything) | 'Roboto', sans-serif (Google Fonts 300, 400, 500) | Roboto 300, 400, 500 | Inter |

| Role | Selector | Size / weight / line-height | Color |
|---|---|---|---|
| Name | `#htname` | 42px / 400 / 60px | #ffffff |
| Title / lab | `#htdesc` | 18px / 300 / 1.43 | #ffffff |
| Email | `#htem` | 16px / 300 / 1.43 | #ffffff |
| Section h2 | `h2` | 50px / 300 / 1.1, centred, padding 40px 0 60px | #444444 |
| Italic section h3 | `.quote2 h3` | 24px / 500 italic / 1.1, centred | #777777 |
| Paper title | `.pubt` | 22px / 400 / 1.43 | #000000 |
| Authors | `.puba` | 18px / 400 / 1.43; own name 700 | #990000 |
| Venue | `.pubv` | 16px / 400 / 1.43 | #009900 |
| Award note | `.pubaw` | 18px / 400 | #ee2556 |
| Abstract | `.pubd` | 18px / 300 / 1.43, justified | #444444 |
| Link box label | `.publ li a` | 14px / 400 | #428bca |
| News row | `.ttitle` | 20px / 400 / 1.43 | #444444 |
| Timeline date | `.tdate` | 18px / 400, margin-bottom -5px | #840000 |
| Timeline text | `#timeline`, `.tdesc` | 20px / 300; desc 18px / 300 | #444444 |

## Tokens — Spacing & Shapes

| Element | Radius | Border | Shadow |
|---|---|---|---|
| Portrait | 50% | 4px solid #ffffff | none |
| Link box | 0 | 1px solid #cccccc | none |
| Publication / news row | 0 | 1px solid #dddddd bottom | none |
| Timeline item | 0 | 5px solid #333333 on the spine side | none |
| Timeline dot | 5px (11px square, so nearly round) | none | none |
| Divider | 0 | `hr.soft` 1px gradient transparent → rgba(0,0,0,0.75) → transparent | none |

## Layout Metrics

- **Banner**: 100% × 500px, margin-bottom 40px; header content absolutely positioned at left 30%, top 100px, width 70%; name block margin-left 120px from the blob (text at x=572 beside the floated portrait).
- **Container**: Bootstrap 3 `.container`, 1170px at ≥1200 (1140px content, x=150 at 1440), padding 0 15px.
- **Publication entry**: `.pubwrap` padding-bottom 10px, margin-bottom 20px, bottom rule; inside a `.row` with two `.col-md-6` (570px each incl. padding); media at width 102% of the column (566px); `.pubimg img` max-width 95%, centred; stacks of `<br>`s vertically offset the media.
- **Link boxes**: `.publ` padding-top 10px; each `li` inline-block, padding 5px, margin 5px 2px.
- **Section headings**: h2 margin 20px 0 10px plus padding 40px 0 60px (155px block); h3 margin 20px 0 10px.
- **Timeline**: items 50% wide, padding 20px; odd items margin-left 50% with a left spine, even items margin-right 50% with a right spine, text aligned toward the spine; dots 11px at top 0, offset -8px.

| Breakpoint | Gutter | Body size | Title size | Grid change |
|---|---|---|---|---|
| <768px | 15px | 14px base; abstracts 18px | name 28px, title 16px | header blob centred at left 0, width 100%; portrait unfloated; timeline single-sided (5px left spine, margin-left 10px, padding 5px, 16px text); paper titles centred |
| 768–991px | container 750px | same | 42px | media and text still stacked (col-md) |
| 992–1199px | container 970px | same | 42px | `col-md-6` halves side by side |
| ≥1200px | container 1170px | same | 42px | halves side by side |

## Components

- **Banner identity**: solid #3b5998 band 500px tall; 240px circular portrait with 4px white ring floated left at 30% from the left edge; name Roboto 42px/400 white; two 18px/300 white lines; 16px/300 white email; three 45–48px white outline icon images (GitHub, LinkedIn, Google Scholar) without labels.
- **Publication entry**: two halves; left media (video at 102% or image at 95% width, centred); right text stack: title 22px/400 #000000, authors 18px #990000 with own name bold, venue 16px #009900, optional award line 18px #ee2556, abstract 18px/300 justified #444444, link boxes; 1px #dddddd rule below with 20px margin.
- **Link box**: inline-block, 1px solid #cccccc, padding 5px, margin 5px 2px, 14px #428bca label, square corners; the code box embeds a shields.io GitHub-stars badge image.
- **News row**: one 20px/400 sentence per `.pubwrap`, inline #428bca links, 1px #dddddd rule.
- **Two-sided timeline**: alternating halves joined by a 5px #333333 spine, 11px #333333 dots, 18px #840000 dates, 20px/300 text.
- **Link**: Bootstrap 3 #428bca, no underline; underlined on hover.

## Page Modules

| Module | Present | How it is styled |
|---|---|---|
| Name / title / contact | yes | white type on the blue banner |
| Portrait | yes | 240px circle with white ring |
| Social icons | yes | three white outline images |
| Recent technical reports | yes | media-left, text-right entries |
| News & highlights | yes | single-line rows with rules |
| Talks / challenge notes | yes | `.ttitle` + `.tdesc` rows |
| Career timeline | yes | two-sided spine |
| Full publication list | yes | same entry recipe, with abstracts |
| Navigation | absent from the source | no nav bar (a `#topnav` rule exists but is unused) |
| Footer | absent from the source | page ends after the last publication |

## Adapting to Other Content

- **Long author lists**: the 18px red author block simply wraps (the SAM 3 entry runs 9 lines); keep the own name bold and do not truncate.
- **Papers without media**: keep the left half empty or use a static figure at 95% width; do not collapse to a single column, the rhythm depends on the split.
- **A results table**: place it in the left media half as an image or a plain Bootstrap table (14px, #444444, 1px #dddddd rules); the page already has small `<table>`s for comparison stills.
- **News**: one sentence per row in `.ttitle`, newest first, under the 50px light h2.
- **Less text-heavy variant**: drop `.pubd` abstracts below the first few entries; the abstracts are what makes the page long.

## Do's and Don'ts

- Do keep the banner a single flat #3b5998 with only white content.
- Do keep the author red (#990000), venue green (#009900) and title black (#000000) triplet on every entry.
- Do justify the abstracts and keep them light (300).
- Don't centre the banner content; it starts at 30% of the viewport.
- Don't round the link boxes or give them fills.
- Don't add colour to section headings; h2 is 50px/300 grey, h3 italic #777777.

## Surfaces

Blue banner, then white everywhere. The only boxed surfaces are 1px grey link boxes; separation comes from #dddddd rules and large heading padding.

## Imagery

A circular, foliage-backed colour portrait; autoplaying research videos (segmentation masks, audio-visual demos) and method diagrams at half width beside each paper; small shields.io star badges.

## Layout

Full-width banner, then a 1140px Bootstrap column: recent reports (media left, text right), news, talks, timeline, full publication list. Very long (about 23,700px at 1440 wide) because every entry carries a full abstract.

## Agent Prompt Guide

Quick colors: banner #3b5998, banner text #ffffff, body #444444, h3 #777777, title #000000, authors #990000, venue #009900, award #ee2556, link #428bca, rule #dddddd, link box #cccccc, timeline #333333 with dates #840000.

1. "Build a banner: full width, 500px tall, solid #3b5998; at left 30% and top 100px a 240px circular photo with a 4px #ffffff border floated left; beside it the name in Roboto 42px/400 #ffffff (line-height 60px), two 18px/300 white lines, a 16px/300 white email and three 45–48px white outline icons."
2. "Make a publication entry in a 1140px container: a row of two halves; left a video at 102% width; right a 22px/400 #000000 title, 18px #990000 authors with your name bold, a 16px #009900 venue, an 18px/300 #444444 justified abstract, then inline link boxes (1px solid #cccccc, padding 5px, margin 5px 2px, 14px #428bca); end with a 1px #dddddd bottom rule, padding-bottom 10px, margin-bottom 20px."
3. "Add a section heading: Roboto 50px/300 #444444 centred with padding 40px 0 60px; for a sub-heading use 24px/500 italic #777777 centred with a 19.2px #428bca link after a middle dot."

## Similar Pages

- Bootstrap 3 academic homepages with a coloured banner and media-left publication rows (Karpathy-style template lineage).
- Video-heavy lab member pages that embed autoplaying demos beside each paper.

## Quick Start

```css
:root {
  --banner: #3b5998;
  --text: #444444;
  --muted: #777777;
  --title: #000000;
  --authors: #990000;
  --venue: #009900;
  --award: #ee2556;
  --link: #428bca;
  --rule: #dddddd;
  --box: #cccccc;
  --font-sans: 'Roboto', sans-serif;
}
body { font-family: var(--font-sans); color: var(--text); }
#header { height: 500px; background: var(--banner); margin-bottom: 40px; }
.imgme { border: 4px solid #ffffff; border-radius: 50%; float: left; margin: -20px 10px -20px 0; }
.pubt { font-size: 22px; color: var(--title); }
.puba { font-size: 18px; color: var(--authors); }
.pubv { font-size: 16px; color: var(--venue); }
.pubd { font-size: 18px; font-weight: 300; text-align: justify; }
.pubwrap { padding-bottom: 10px; margin-bottom: 20px; border-bottom: 1px solid var(--rule); }
.publ li { display: inline-block; border: 1px solid var(--box); padding: 5px; margin: 5px 2px; }
h2 { text-align: center; font-weight: 300; font-size: 50px; padding: 40px 0 60px; }
```

## Provenance

- **URL**: https://feichtenhofer.github.io/
- **Person**: Christoph Feichtenhofer (video understanding, computer vision).
- **Venue / award**: ICLR 2025 Outstanding Paper Honorable Mention, "SAM 2: Segment Anything in Images and Videos" (last author). https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- **Selection reason**: award rule (first/last author); chosen for the full-width blue banner header and a publications column with large media and abstracts.
- **Template credit**: no credit on the page; Bootstrap 3 with a custom `style.css` in the style of Andrej Karpathy's older academic homepage.
- **Evidence used**: tools/computed_style.py render at 1440×900 (computed styles, fonts_loaded, color share, DOM boxes), a selector probe of header, publication entries, news rows and timeline, the 1440×900 and full-page screenshots, and `style.css` and `index.html` read directly, on 2026-10-28.
