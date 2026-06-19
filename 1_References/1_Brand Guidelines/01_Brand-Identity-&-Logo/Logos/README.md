# Logos

Source of truth for Cars24 logo usage in this repository.

Use the assets in this folder together with `logo-types.md` before placing a logo in any creative, slide export, or image prompt.

## SVG Files (preferred for HTML/web — scale to any size)

| File | Fill | Colorway | When to use |
| --- | --- | --- | --- |
| [`Group-1.svg`](./Group-1.svg) | `#4736FE` | Blue — primary | Light / white / pale backgrounds |
| [`Group.svg`](./Group.svg) | `white` | White | Dark or brand-purple backgrounds |
| [`Group-2.svg`](./Group-2.svg) | `white` | White (alternate) | Dark or brand-purple backgrounds |
| [`Group-3.svg`](./Group-3.svg) | `#161616` | Black | High-contrast light / print / grayscale |

## PNG Files (use when SVG is not supported — e.g. image exports, email)

| File | Colorway | When to use |
| --- | --- | --- |
| [`Logo - Blue.png`](./Logo%20-%20Blue.png) | Blue — primary | Light / white / pale backgrounds |
| [`Logo - White.png`](./Logo%20-%20White.png) | White | Dark or brand-purple backgrounds |
| [`Logo - Black.png`](./Logo%20-%20Black.png) | Black | High-contrast light / print / grayscale |

## Rules
- See [`logo-types.md`](./logo-types.md) for colorway selection, placement, clear-space, and prohibited treatments.
- For HTML creatives: inline the SVG or use `<img src="Group-1.svg" ...>` — prefer SVG over PNG for resolution independence.
- For image generation prompts or raster exports: base64-encode and embed the matching PNG.
