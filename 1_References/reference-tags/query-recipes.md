# Reference Query Recipes — v2.0

Use these recipes to select references before building a Stage 7 reference map.

## Layout plan for any image or carousel

Build this plan before prompt assembly:

```text
theme: dark OR light
reference_role: layout
archetype/layout_archetype: cover-lockup OR headline-left-hero-right OR stacked-left-hero-right OR text-only OR headline-dominant OR content-card-overlay OR event-poster
format: 4:5 OR 1:1 OR requested format
```

Plan fields:

```text
Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason
```

Carousel/batch guard:

```text
Do not use the same archetype or the same top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asks for a consistent repeated system. Batch territories must include layout territory as well as style territory.
```

## Dark theme with real photo hero

Query:

```text
theme: dark
reference_role: layout
archetype/layout_archetype: cover-lockup OR headline-left-hero-right OR stacked-left-hero-right OR text-only OR headline-dominant OR content-card-overlay OR event-poster
copy-layout-only: true
do-not-generate-marble-hero: true
```

Add:

```text
reference_role: photo-style
photo_layer: product-cars-first OR assisted-experience OR brand-lifestyle OR hubs-infrastructure
hero: real-human OR real-car OR real-hub OR service-moment
```

Prompt guard:

```text
The layout reference contains a marble/statue placeholder. Copy only layout, scale, negative space, text hierarchy, and pattern placement. Do not generate a marble or statue hero. The photo hero must be real photographic Cars24-style imagery.
If the selected archetype has no hero, use the photo as a small proof/cutout only when the layout has a natural slot; otherwise keep it text/pattern-led. Do not force every photo slide into headline-left + hero-right.
```

## Light theme with full-background pattern

Query:

```text
theme: light
reference_role: pattern-texture
pattern_family: wave-field OR shell-halo OR organic-mesh
pattern_placement: full-background
quality_flags: clean-behind-text
```

Prompt guard:

```text
Pattern may flow across the full background, but it stays behind all text and hero elements and preserves text readability.
```

## Typography-led text-only slide

Query:

```text
reference_role: layout
layout_archetype: text-only OR headline-dominant
typography: Arapey-led-serif-headline
case: sentence-case
hero: no-hero
```

Prompt guard:

```text
No hero subject. Typography and pattern carry the slide. Use a refined editorial serif headline with sentence-case visible copy.
```

## Logo-bearing slide

Query:

```text
reference_role: logo-asset
theme: dark OR light
logo_usage: generation-time-logo-reference
```

Generation:

```text
For Codex ImageGen, name the theme-matched visible Cars24 logo PNG as the exact repo-relative source file to use, instruct the model to copy the official identity without recreating or modifying it, and apply strict logo QA. Providers/workflows that support image references must also receive the same PNG as actual visual input. Do not add a local logo overlay afterward.
If Codex changes, omits, boxes, or crops the logo, reject the output and move to a visual-input-capable workflow or ask for a supported logo upload. If a reference-capable provider cannot attach the PNG, stop and ask the user to share/upload it or choose another supported workflow.
Place the logo by layout axis and clean negative space. In a carousel, keep logo placement and size identical across logo-bearing slides with the same theme/background family. Logo may overlap pattern and may overlap hero only when readable, high-contrast, cleanly fitted, and uncropped.
```

## Illustration slide

Query:

```text
reference_role: subject-style
asset_role: illustration reference
illustration_style: modern flat editorial
```

Prompt guard:

```text
Copy only illustration style, palette discipline, and character treatment. Do not copy exact scene, pose, or background.
```

## Premium infographic icons

Default query:

```text
reference_role: icon-style-anchor
visual_style: icon OR infographic
icon_style: 3d-glossy OR flat-solid
hero: infographic-element OR icon-hero
```

Use:

```text
1_References/1_Brand Guidelines/09_Icon-System/02_icon-system-overview.png
1_References/1_Brand Guidelines/09_Icon-System/03_3d-icon-generator.png for premium/feature callouts
1_References/1_Brand Guidelines/09_Icon-System/04_flat-icon-generator.png for dense/process/UI flows
```

Optional finish inspiration only:

```text
1_References/4_Infographic Icon References/soft-dimensional-glass-icons-blue.png
1_References/4_Infographic Icon References/soft-dimensional-glass-icons-mint.png
```

Prompt guard:

```text
Start from the Cars24 icon system. Use 3D icons for premium marketing/feature callouts and flat filled icons for dense/process/UI flows. If the output risks looking too flat, add controlled dimensional polish: subtle fill depth, soft top-left highlight, slight shadow, rounded filled forms, and clean readable silhouettes. Do not render thin outline icons, plain white line art as the primary icon style, generic SaaS symbols, glass UI tiles, one large glass slab, app-icon sheets, abstract broken symbols, or heavy photorealistic 3D.
```

## Rules-only safety check

Before attaching any reference:

```text
attachability != rules-only
attachability != do-not-attach
quality_flags does not include diagram-contamination
```

If a needed file is rules-only, summarize its intent into prompt text instead of attaching the image.
