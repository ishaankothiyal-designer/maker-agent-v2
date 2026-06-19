# Reference Query Recipes — v2.0

Use these recipes to select references before building a Stage 7 reference map.

## Layout plan for any image or carousel

Build this plan before prompt assembly:

```text
theme: dark OR light
reference_role: layout
archetype/layout_archetype: cover-lockup OR headline-left-hero-right OR stacked-left-hero-right OR text-only OR headline-dominant OR content-card-overlay OR event-poster OR no-text-balanced-hero
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

## No visible text / no subtext layout

Use this whenever the user asks for no text, no headline, no subtext, or the batch field `Visible image text` is `None`.

Query:

```text
reference_role: layout
layout_archetype: no-text-balanced-hero
visible_text: none
typography: no-visible-text
format: requested format
```

Prompt guard:

```text
Use Archetype 8 / NT-1. No visible text, no subtext, no labels, and no dormant text zone. Rebalance the whole canvas around a centred or near-centred hero/form/icon system, with comparable left/right breathing room, no edge-crowded cutout, and full-canvas brand pattern/atmosphere behind it. Applies to photo, illustration, infographic, and abstract styles.
```

## Dark theme with real photo hero

Query:

```text
theme: dark
reference_role: layout
archetype/layout_archetype: cover-lockup OR headline-left-hero-right OR stacked-left-hero-right OR text-only OR headline-dominant OR content-card-overlay OR event-poster OR no-text-balanced-hero
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
Attach/share the theme-matched visible Cars24 logo reference and render it inside the generated composite. Do not add a local logo overlay afterward.
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
icon_style: semantic-first OR soft-dimensional-glass OR 3d-glossy OR flat-solid
hero: infographic-element OR icon-hero
```

Use:

```text
1_References/1_Brand Guidelines/09_Icon-System/02_icon-system-overview.png
1_References/4_Infographic Icon References/soft-dimensional-glass-icons-blue.png for premium/process polish when it improves clarity
1_References/1_Brand Guidelines/09_Icon-System/03_3d-icon-generator.png when object depth communicates the subject better
1_References/1_Brand Guidelines/09_Icon-System/04_flat-icon-generator.png for dense/process/UI flows or when clarity beats polish
```

Prompt guard:

```text
Start from the Cars24 icon system. The icon must semantically match the slide subject first. Prefer soft dimensional glass polish for premium/process output when it improves clarity; use 3D when object depth communicates the subject better; use flat filled for dense/process/UI flows or when clarity beats polish. If glass output becomes generic, broken, app-tile-like, or unclear, fall back to 3D or flat filled. Do not render thin outline icons, plain white line art as the primary icon style, generic SaaS symbols, glass UI tiles, one large glass slab, app-icon sheets, abstract broken symbols, or heavy photorealistic 3D.
```

## Rules-only safety check

Before attaching any reference:

```text
attachability != rules-only
attachability != do-not-attach
quality_flags does not include diagram-contamination
```

If a needed file is rules-only, summarize its intent into prompt text instead of attaching the image.
