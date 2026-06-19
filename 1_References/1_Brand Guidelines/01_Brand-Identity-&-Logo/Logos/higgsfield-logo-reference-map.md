---
name: cars24-logo-higgsfield-reference-map
description: Maps the three approved Cars24 logo colorways to their asset files and background conditions, for upload as image references to Higgsfield alongside creative direction. Use whenever a Higgsfield generation must include the Cars24 logo.
metadata:
  type: reference
---

# Cars24 Logo — Higgsfield Reference Map

Purpose: when we hand creative direction to Higgsfield, **attach the matching logo file below as an image reference** so the model reproduces the real lockup instead of inventing one. This map tells you *which file to upload for which background*.

The logo is always the **horizontal lockup**: rounded-square icon (open "C" / refresh mark) + `Cars24` wordmark. Never redraw, recolor, stretch, rotate, or add effects — see Prohibited Treatments below.

---

## The map — 3 approved colorways

Pick **one** colorway by the background *directly behind the logo placement* (not the whole frame).

| Colorway | Upload this file (image ref) | SVG equivalent (HTML/web) | Use when the logo placement is… |
| --- | --- | --- | --- |
| **Neo Blue** `#4736FE` | [`Logo - Blue-on-white.png`](./Logo%20-%20Blue-on-white.png) (89KB high-vis composite) | [`Group-1.svg`](./Group-1.svg) | White, pale, or light-neutral backgrounds (`#FFFFFF`, `#E2E8F0`, pale lavender). **Default for light creatives.** |
| **White** | [`Logo - White-on-blue.png`](./Logo%20-%20White-on-blue.png) for brand-purple generation references; use [`Logo - White.png`](./Logo%20-%20White.png) only in deterministic non-generation layouts | [`Group.svg`](./Group.svg) / [`Group-2.svg`](./Group-2.svg) | Brand-purple fields (`#4737FE` + supporting violets) **or** dark/near-black photographic backgrounds. |
| **Black** `#161616` | [`Logo - Black.png`](./Logo%20-%20Black.png) | [`Group-3.svg`](./Group-3.svg) | White / light backgrounds where color must be avoided — print, grayscale, legal, high-contrast layouts. |

> `Logo - White.png` is **white ink on a transparent background** — it looks blank on a white page. That is correct; preview it on a dark swatch to confirm.

### Quick selection flow
1. Brand-purple placement → **White** (`Logo - White-on-blue.png` for generation reference)
2. White / pale editorial placement → **Neo Blue** (`Logo - Blue-on-white.png`), or **Black** when color must be avoided
3. Dark but not brand-purple (e.g. dark photo) → **White** (`Logo - White-on-blue.png` for generation reference)
4. Contrast still weak → switch colorway or move the logo. **Never** alter the logo's colors.

---

## How to attach in a Higgsfield request

1. **Upload the PNG** that matches the dominant logo-placement background (table above) as an **image reference**. PNG is used for the reference because image models take raster, not SVG.
   > **Critical:** For light backgrounds, always use `Logo - Blue-on-white.png` (89KB), NOT `Logo - Blue.png` (3.6KB). The raw blue logo is too small for the model to read — it consistently hallucinates wrong icons. The composite version places the blue logo on a white tile at high resolution, just like `Logo - White-on-blue.png` does for dark backgrounds.
2. In the prompt, state: *"Place the official Cars24 horizontal lockup exactly as in the attached reference — rounded-square icon with the circular cut-through/open-C mark plus the `Cars24` wordmark. Do not redraw or restyle it. This is not the old boxed `CARS24` logo, not an all-caps lockup, and not a plaque or badge. Ignore the background tile of the logo reference and render no box/tile around the logo."*
3. Name the placement and clear space (see below). For HTML/code exports instead of generated images, use the SVG equivalent.

---

## Placement & clear space (carry into the prompt)
- **Corner anchor** — bottom-left or top-left unless the layout needs another safe zone.
- **Clear space** ≥ half the icon width on all sides (brand book: the height of the lowercase "r"). Never crowd or press to an edge.
- **Generated slide size** should match the reference creatives: about 8–10% of canvas width for slide branding, smaller than the headline, and placed in clean negative space.
- Logo **smaller than the headline** — it signs the frame, it doesn't compete.
- On a carousel, keep **one colorway family** across slides while the background family stays the same; switch only when the background family changes.

## Prohibited treatments (state as negatives in the prompt)
No recoloring outside these three colorways · no gradient / glow / emboss / drop shadow · no stretch / skew / rotate · no blue logo on purple · no white logo on white/pale · never replace the lockup with typed "Cars24" or append legal wording ("Private Limited").

---

## Source of truth
- Colorway rules, lockup structure, full avoid-list → [`logo-types.md`](./logo-types.md)
- Asset inventory & format guidance → [`README.md`](./README.md)
- Pre-baked inline SVG + base64 PNG assets → [`logo-assets.md`](./logo-assets.md)
- Brand-book plates (vision-verified) → [`../notes.md`](../notes.md)

This map is for *routing the right file to Higgsfield*; if it ever conflicts with `logo-types.md`, `logo-types.md` wins.
