# Sounding Object Tailwind Notes — Style Reference

> A Nerfies page rewritten as a calm Tailwind article, with a night mode carried over from the author's site.

**Theme:** both (light by default; dark when the site-wide `theme` preference is stored as `dark`)

Values come from the static HTML (Tailwind utility classes) and the compiled Astro/Tailwind v4 stylesheet `/_astro/global.BpnRDb_H.css`, whose `@theme` tokens define the palette. Gray steps are Tailwind's oklch defaults. Measurements are normalized; roles are interpreted.

## Overview

This page lives inside Tingle Li's Astro personal site and keeps the Nerfies section order (title, authors, venue, buttons, TL;DR, teaser, abstract, results, architecture, BibTeX, acknowledgements) but none of Bulma's look. Everything sits in a `max-w-4xl` (56rem) column with Tailwind spacing. The title is a modest `text-2xl sm:text-3xl` bold. The four link buttons are solid deep-blue `#004aae` pills that brighten to `#2563eb` on hover. Results are muted autoplay videos in a JS carousel with round white arrow buttons and small dot indicators; clicking a video toggles its sound. Sections are separated by thin `gray-200` rules and 3rem margins. A `dark:` variant exists for every color, switched by adding `.dark` to `<html>` when `localStorage.theme === 'dark'`.

## Tokens — Colors

| Name | Value | Token | Role |
|---|---|---|---|
| Deep Lab Blue | `#004aae` | `--color-primary` | Button fill, active carousel dot |
| Bright Accent | `#2563eb` | `--color-accent` | Button hover, link hover (`hover:text-accent`) |
| Night Link | `#3b6fd4` | `--color-primary-light` | Link color in dark mode |
| Ink | `oklch(21% .034 264.665)` | `--color-gray-900` | Body text and title (light); page background (dark) |
| Body Gray | `oklch(37.3% .034 259.733)` | `--color-gray-700` | TL;DR and prose |
| Author Gray | `oklch(44.6% .03 256.802)` | `--color-gray-600` | Authors, captions |
| Venue Gray | `oklch(55.1% .027 264.364)` | `--color-gray-500` | Venue line, small labels |
| Separator | `oklch(87.2% .01 258.338)` | `--color-gray-300` | `&nbsp;` spacers between authors, inactive dots |
| Rule | `oklch(92.8% .006 264.531)` | `--color-gray-200` | `<hr>` section rules |
| Footer Rule | `oklch(96.7% .003 264.542)` | `--color-gray-100` | Footer top border; night text |
| Code Paper | `oklch(98.5% .002 247.839)` | `--color-gray-50` | BibTeX `pre` background |
| Paper | `#ffffff` | `--color-white` | Page background (light) |
| Night Panel | `oklch(27.8% .033 256.848)` | `--color-gray-800` | BibTeX background and arrow buttons in dark mode |

## Tokens — Typography

- **Sans (everything):** Tailwind `--font-sans`: `ui-sans-serif, system-ui, sans-serif` plus emoji fonts. A Google Fonts link loads Source Sans 3 (400–700), but no compiled rule references it, so it does not render (inferred). Substitute: Inter, system-ui.
- **Mono:** Tailwind `--font-mono`: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`.
- Weights: 500 (`font-medium` buttons), 600, 700 (`font-bold` headings).

| Role | Size | Weight | Line height |
|---|---|---|---|
| Title | 1.5rem → 1.875rem at `sm` | 700 | `leading-tight` 1.25 |
| Section h2 | 1.25rem → 1.5rem at `sm` | 700 | Tailwind default, centered |
| Authors | 1.125rem | 400 | 1.75/1.125 |
| Main text | 1rem → 1.125rem at `sm` | 400 | `leading-relaxed` 1.625 for abstract |
| Venue, buttons | 1rem | 400 / 500 | |
| Captions | 0.875rem | 400 | |
| BibTeX | 0.75rem mono | 400 | |

## Tokens — Spacing & Shapes

| Element | Radius |
|---|---|
| Buttons, carousel arrows, dots | `rounded-full` (Tailwind max radius) |
| BibTeX block | `rounded-lg` 0.5rem |
| Teaser and videos | 0 |

- **Shadows:** carousel arrows use Tailwind `shadow`; nothing else.
- **Layout:** `max-w-4xl` (56rem) column, `px-4 sm:px-6 lg:px-8`, `py-8 sm:py-12`; videos capped at `max-w-2xl` (42rem) and centered; section rhythm `mb-12` with `<hr class="mb-12">`.
- **Motion:** `transition-colors duration-200` on body for the theme switch.

## Components

- **Primary pill button.** `inline-flex items-center gap-1.5 px-5 py-2 rounded-full text-base font-medium bg-primary text-white hover:bg-accent`, with a small (`text-xs`) Font Awesome or Academicons icon. Labels: Paper, arXiv, Code, BibTeX.
- **Author line.** Flex-wrap centered row with `gap-x-3`; each name links and turns accent on hover; gray-300 non-breaking spacers between names.
- **TL;DR.** Centered gray-700 sentence with a bold "TL;DR:" label.
- **Video carousel.** Slides toggled with `hidden`; prev/next are 40px round `bg-white/80` buttons with a shadow, vertically centered and nudged outside the frame; 8px dots, active dot `bg-primary`.
- **Click-to-unmute video.** `autoplay loop muted playsinline` with a poster image; `onclick` toggles `muted`.
- **BibTeX.** `pre` with `bg-gray-50 p-4 rounded-lg text-xs overflow-x-auto`.

## Page Modules

| Module | Present | Styling |
|---|---|---|
| Title / author block | Yes | Centered header, `mb-10` |
| Venue badge | "ICML 2025" text line | gray-500, no chip |
| Link buttons | Paper, arXiv, Code, BibTeX | Blue pills |
| Teaser | Full-width image with left-aligned caption | |
| Abstract | Yes | gray-700, relaxed leading |
| Results | Compositional sound generation, texture adaptation, in-domain results | Video carousels (7 videos) |
| Method figure | "Model Architecture" | Image |
| Tables / sliders / 3D / HF | No | |
| BibTeX | Yes | Gray rounded `pre` |
| Acknowledgements | Yes | Thanks plus Nerfies template credit |
| Dark mode | Yes, via stored preference | Full `dark:` variants; no toggle on this page |

## Do's and Don'ts

- Do keep one blue for actions and a brighter blue for hover; everything else is gray.
- Do cap videos at 42rem inside the 56rem column so the reading width stays steady.
- Do provide `dark:` counterparts for every surface if the host site has a theme switch.
- Don't load a web font you never apply; either set `--font-sans` to Source Sans 3 or drop the link.
- Don't bring back Bulma's dark buttons; this page's pills are blue.

## Surfaces

Light: white page, gray-50 code block, gray-200 rules. Dark: gray-900 page, gray-800 code and arrow buttons, gray-700 rules.

## Imagery

Scene images with object masks, and videos with generated audio; posters shown before playback.

## Layout

Single centered 56rem column with a centered header; prose left-aligned; footer separated by a gray-100 top border.

## Agent Prompt Guide

**Quick colors:** bg `#ffffff`, ink gray-900, prose gray-700, muted gray-500, rule gray-200, primary `#004aae`, accent `#2563eb`, dark link `#3b6fd4`.

1. "Make Tailwind pill links: `inline-flex items-center gap-1.5 px-5 py-2 rounded-full font-medium text-white` on `#004aae`, hover `#2563eb`, each with an `text-xs` icon."
2. "Build a video carousel: slides toggled with `hidden`, 40px round `bg-white/80` prev/next buttons with a shadow at the vertical center, and 8px dots below where the active dot is `#004aae`."
3. "Lay out a project page in a `max-w-4xl` column with `py-8 sm:py-12`, a 1.5rem→1.875rem bold centered title, a gray-500 venue line, and sections divided by gray-200 `<hr>` with 3rem margins; add `dark:` variants using gray-900 and gray-100."

## Similar Pages

Project pages hosted inside Astro or Next.js personal sites that keep the Nerfies section order; FQL in this collection is another page hosted under the author's own domain.

## Quick Start

```css
:root {
  --color-primary: #004aae; --color-accent: #2563eb; --color-primary-light: #3b6fd4;
  --color-gray-50: oklch(98.5% .002 247.839); --color-gray-200: oklch(92.8% .006 264.531);
  --color-gray-500: oklch(55.1% .027 264.364); --color-gray-700: oklch(37.3% .034 259.733);
  --color-gray-900: oklch(21% .034 264.665);
  --font-sans: ui-sans-serif, system-ui, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  --radius-lg: .5rem; --page: 56rem; --media: 42rem;
}
body { background: #fff; color: var(--color-gray-900); font-family: var(--font-sans); }
.dark body { background: var(--color-gray-900); color: oklch(96.7% .003 264.542); }
.dark a { color: var(--color-primary-light); }
```

## Provenance

- **URL:** https://tinglok.netlify.app/files/avobject/
- **Paper:** Sounding that Object: Interactive Object-Aware Image to Audio Generation (arXiv 2506.04214), Tingle Li et al.
- **Venue:** ICML 2025 (text line in the header).
- **Selection reason:** arXiv comment states acceptance at ICML 2025; project page linked in the arXiv abstract.
- **Template credit:** acknowledgements thank "Nerfies for open sourcing this website template"; the actual implementation is Astro with Tailwind CSS v4.
- **Measurement method:** `extract_style.py` plus manual reading of Tailwind classes and the compiled `@theme` tokens. The extractor's `publication_list` flag is a false positive for this project page. Rendered page not viewed; dark mode was checked only in code (`.dark` class set from `localStorage`).
