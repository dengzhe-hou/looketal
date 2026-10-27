# Palatino Video Wall — Style Reference

> A DreamFusion-style lab page: light Source Sans headings, Palatino captions, a wall of thirty-four videos.

**Theme:** light

*Measurements are normalized from static HTML and CSS (frequency-ranked by a script, then filtered by reading the page's own stylesheet and inline styles). Roles are interpreted, not declared by the authors.*

Built from the DreamFusion/MVDream template on Bootstrap 4.5 with a Webflow-exported stylesheet. The voice is quiet: Source Sans Pro at weight 300 for headings, Palatino for paragraphs and captions, everything centered in 768px columns separated by `hr.divider`. The page is dominated by video, with 34 lazy-loaded clips in Bootstrap `col-3` and `col-4` grids under small Palatino compare titles. The header is minimal: a 33px bold-name title, author links, affiliations, a 22px "ICLR, 2025" line, and a single light button.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Paper White | `#ffffff` | `--bg` | Page background |
| Bootstrap Ink | `#212529` | `--text` | Bootstrap 4 body text |
| Bootstrap Gray | `#6c757d` | `--muted` | Secondary text |
| Superscript Slate | `#313436` | `--sup` | `.authors sup` |
| Light Button | `#f8f9fa` | `--btn-light` | `btn btn-light` fill (Bootstrap default) |
| Primary Blue | `#007bff` | `--primary` | `btn-primary btn-lg btn-search` toggles and links (Bootstrap default) |
| Glow Sky | `#5fb7f7` | `--glow` | `.shadowed_text` 4px text-shadow halo (white text) |
| Select Blue | `#055ada` | `--select` | Selected span text, on rgb(194, 247, 215) mint |
| Disabled Gray | `#cccccc` | `--disabled` | `.btn-light.disabled` |

Most Bootstrap 4 palette colors in the counts are framework defaults; only the light button and primary button colors are visibly used.

## Tokens — Typography

**Families.** Headings and body: "Source Sans Pro", Calibri, Candara, Arial, weight 300. Paragraphs, captions, compare titles: Palatino, "Palatino Linotype", "Book Antiqua", Georgia. Substitutes: Source Sans 3 and TeX Gyre Pagella or EB Garamond.

| Role | Size | Weight | Family |
|---|---|---|---|
| Title (`h1`, inline) | 33px | 300 (method name bold) | Source Sans Pro |
| Venue line (`h1`, inline) | 22px | 300 | Source Sans Pro |
| Section heading (`h2`) | 2rem (Bootstrap), line-height 1.1 | 300 | Source Sans Pro |
| Paragraph / caption | 16px desktop, 12px under 575px | 400 | Palatino |
| Compare title / caption | 16px desktop, 12px mobile | 400 | Palatino |

## Tokens — Spacing & Shapes

| Token | Value | Used on |
|---|---|---|
| --radius-sm | .25rem | Bootstrap buttons |
| --radius-lg | .3rem | `btn-lg` |
| --radius-xl | 1rem | Webflow-derived elements (inferred) |
| --radius-round | 50% | small icons |

**Shadows.** None designed. Bootstrap focus shadows only.

**Layout width.** Header containers `max-width: 1024px`; content containers `max-width: 768px` (13 inline uses); videos 100% wide (62 inline uses).

## Components

- **Header.** `.highlight-clean` with 20px top padding; centered 33px title with the method name in `<b>`; authors as plain links with superscripts; affiliations as spans.
- **Link button.** One `btn btn-light` labeled Code (its href points to the arXiv abstract in the current source).
- **Show-more toggles.** Twelve `btn btn-primary btn-lg btn-search` buttons (Bootstrap blue).
- **Captioned video row.** `.row.captioned_videos` of `col-3` or `col-4` cells, each a `video.lazy` with autoplay, loop, muted, playsinline.
- **Compare title.** `.compare-title` Palatino 16px centered above each column.
- **Divider.** `hr.divider` between every section.
- **Video container.** `.video-container` 56.25% padding box for embeds.

## Page Modules

- **Title/author block.** Centered, minimal.
- **Link buttons.** One light button.
- **Teaser video.** A 720px teaser clip followed by a TL;DR paragraph.
- **Abstract and method.** Text plus method figure.
- **Results videos.** Object motion control, camera motion control, VIPSeg, comparison with supervised baselines.
- **Ablations and hyperparameters.** Modified self-attention, high-frequency preservation, U-Net layers, denoising timesteps, each as video grids.
- **Citation.** BibTeX under the heading "Citation".
- Not present: Bulma components, slider, 3D viewer, demo, results table.

## Do's and Don'ts

**Do**

- Pair light sans headings with Palatino body for a calm academic tone.
- Keep content at 768px and let video grids fill it.
- Lazy-load every video.

**Don't**

- Don't use heavy heading weights; headings are 300.
- Don't mislabel buttons (the only Code button links to arXiv).
- Don't mix more than two column counts in one grid.

## Surfaces

Flat white; no wells or cards beyond Bootstrap defaults.

## Imagery

Generated video clips with drawn bounding-box trajectories, side-by-side comparisons, ablation grids.

## Layout

Single centered 768px column, `hr` between sections, Bootstrap rows for video grids.

## Agent Prompt Guide

**Quick color reference**

- Background #ffffff
- Text #212529
- Light button #f8f9fa
- Toggle #007bff
- Glow #5fb7f7

**Example component prompts**

1. Create a centered header: 33px Source Sans Pro weight 300 title with the method name bold, author links with superscripts, and a 22px 'ICLR, 2025' line, max-width 1024px.
2. Create a captioned video row of four columns at 768px, each with a 16px Palatino compare title and an autoplay muted looping video at 100% width.
3. Create a section with a weight-300 Source Sans h2 'Abstract' and Palatino 16px paragraph, separated from the next section by a thin hr.

## Similar Pages

- DreamFusion project page (credited template).
- MVDream project page (credited template).

## Quick Start

```css
:root {
  --bg: #ffffff;
  --text: #212529;
  --muted: #6c757d;
  --sup: #313436;
  --btn-light: #f8f9fa;
  --primary: #007bff;
  --glow: #5fb7f7;
  --font-head: 'Source Sans Pro', Calibri, Candara, Arial, sans-serif;
  --font-text: Palatino, 'Palatino Linotype', 'Book Antiqua', Georgia, serif;
  --content-max: 768px;
  --header-max: 1024px;
}
body { font-family: var(--font-head); font-weight: 300; }
p, .caption, .compare-title { font-family: var(--font-text); }
```

## Provenance

- URL: https://kmcode1.github.io/Projects/SG-I2V/
- Paper: SG-I2V: Self-Guided Trajectory Control in Image-to-Video Generation (Koichi Namekata et al.), arXiv 2411.04989.
- Venue: ICLR 2025 (per the arXiv comment and the page's venue line). Field: video generation.
- Selection reason: arXiv comment states acceptance at ICLR 2025 and links the project page.
- Template credit: footer says the template is from DreamFusion and MVDream.
- Measurement: Measured from static HTML and CSS only (tools/extract_style.py plus a direct read of the page's own stylesheets and inline styles). The page was not rendered in a browser for this entry, so computed styles, actual font fallback, and video framing are not verified.
