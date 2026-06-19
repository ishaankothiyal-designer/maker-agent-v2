---
name: cars24-logo-system
description: Official Cars24 logo lockup and colorway rules. Use whenever a creative, slide, export, or image prompt includes the Cars24 logo or brand mark.
---

# Cars24 Logo Types

This folder is the **source of truth** for every Cars24 logo used in this repository.

Study the PNG assets in this folder before placing a logo in any creative.

- `Logo - Blue.png`
- `Logo - Black.png`
- `Logo - White.png`

Do not redraw, approximate, or typeset the wordmark. Use the correct colorway for the background. Do not recolor, stretch, rotate, outline, shadow, or apply effects to the lockup.

## Lockup Structure

The logo is always a **horizontal lockup** of two parts:

1. **Icon** — Rounded square containing a circular refresh-style mark (two curved segments with gaps at top and bottom).
2. **Wordmark** — `Cars24` in a clean geometric sans-serif: capital `C`, lowercase `ars`, numerals `24`.

Rules:

- Keep icon and wordmark together unless an approved icon-only asset is explicitly provided (this repo only documents the full lockup).
- Preserve the gap between icon and wordmark; do not tighten or separate the parts.
- Keep icon and wordmark vertically centered with each other.
- Do not substitute another typeface for the wordmark in layouts that require the brand logo.

## Logo Colorways

Choose **one** colorway based on the background. Never invent a fifth treatment.

| ID | Name | Background | Logo treatment | When to use |
| --- | --- | --- | --- | --- |
| `primary-on-light` | Primary on light | White or very light neutral (`#FFFFFF`, `#E2E8F0`, pale lavender-white fields) | Icon and wordmark in brand purple | Default on light-theme creatives, editorial fields, and pale slides |
| `inverted-on-brand` | Inverted on brand | Brand purple field (`#4737FE` and close supporting violets) | White icon and white wordmark | Headers, launch slides, dark-theme hero fields, and any saturated brand-violet background |
| `mono-black-on-light` | Monochrome black | White or very light neutral | Solid black icon and wordmark (`#000000`) | Print, grayscale, legal, or high-contrast light layouts where color logo is not appropriate |
| `mono-white-on-dark` | Monochrome white | Near-black or dark charcoal (`#1A1A1A` and deep photo overlays) | White icon and wordmark; icon reads as white rounded square with mark cut out to background | Dark photography, dark UI strips, and dark-theme slides that are not brand-purple |

### Selection flow

1. Identify the **dominant background** behind the logo placement (not the whole poster— the local area where the logo sits).
2. If the area is **brand purple**, use `inverted-on-brand`.
3. If the area is **white or pale editorial**, use `primary-on-light` (default) or `mono-black-on-light` when color must be avoided.
4. If the area is **dark but not brand purple**, use `mono-white-on-dark`.
5. If contrast is insufficient, switch colorway or move the logo—do not alter logo colors.

## Color Values

Align logo purple with the repository color system:

- **Logo / brand purple (primary lockup):** `#4737FE` (canonical; matches `1_skills/Creative guidelines/references/color-system.md`)
- **Neutrals:** `#FFFFFF`, `#000000`, near-black `#1A1A1A` for dark mono placements

The reference sheet may read slightly bluer on screen; treat `#4737FE` as the implementation anchor for generated assets and layouts.

## Placement And Clear Space

- Prefer a **corner anchor** (typically bottom-left or top-left) unless the slide layout requires another safe zone.
- Maintain clear space around the full lockup of at least **half the icon width** on all sides; do not crowd with headlines, motifs, or crop lines.
- Keep the logo **smaller than the main headline** on founder/editorial slides; it signs the frame, it does not compete with the message.
- On carousels, use the **same colorway family** across the set when the background family stays consistent; switch colorway only when the slide background family changes.

## Prohibited Treatments

- Recoloring the lockup outside the four approved colorways
- Gradients, glow, emboss, or drop shadow on the logo
- Stretching, skewing, or rotating the lockup
- Placing primary purple logo on brand-purple backgrounds (fails contrast)
- Placing white mono logo on white or pale fields
- Replacing the lockup with plain text “Cars24” in campaign typography (`Arapey` / `Geist` are for editorial copy, not the brand mark)

## Asset Format — SVG vs PNG

| Context | Format | File to use |
| --- | --- | --- |
| HTML / web creatives | **SVG (preferred)** — resolution-independent, scales to any size | `Group-1.svg` / `Group.svg` / `Group-3.svg` |
| Illustrations placed inside a creative | SVG inline or `<img>` | Same as above |
| Image exports, raster composites, email | **PNG** — base64-encode for HTML, or embed directly | `Logo - Blue.png` / `Logo - White.png` / `Logo - Black.png` |
| Image generation prompts | PNG reference | Specify colorway and describe the lockup per this doc |

SVG colorway ↔ PNG colorway mapping:

| SVG | Equivalent PNG |
| --- | --- |
| `Group-1.svg` (fill `#4736FE`) | `Logo - Blue.png` |
| `Group.svg` or `Group-2.svg` (fill `white`) | `Logo - White.png` |
| `Group-3.svg` (fill `#161616`) | `Logo - Black.png` |

## Image Generation And Exports

When prompting image models:

- Specify which colorway applies to the logo placement.
- State that the logo is the official Cars24 horizontal lockup (icon + wordmark), not a generic wordmark.
- For light-theme slides: default to `primary-on-light`.
- For dark electric-violet slides: use `inverted-on-brand`.
- For dark photographic slides: use `mono-white-on-dark`.

When exporting finished slides from this repo, prefer placing logo assets from this folder (or faithful reproduction per this spec) in the export bundle under `3_export assets/output/`.

## Related Skills

Read this file (and the reference image) whenever any of these skills run:

- `1_skills/Creative guidelines/creative-direction.md`
- `1_skills/Images in creatives/Images.md`
- `1_skills/Patterns in creatives/Patterns.md`
- `AGENTS.md` creative phases

If logo rules conflict with a one-off user request, follow this document unless the user explicitly overrides with approved alternate brand assets.
