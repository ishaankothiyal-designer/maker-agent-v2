---
name: higgsfield-context-package
description: Operational guide for every Higgsfield generation call. Defines exactly which reference images to attach and what visual context to include in the prompt for each visual style. Load at Stage 8 alongside CREATIVE-DIRECTION.md.
---

# Higgsfield Context Package — Visual Reference Intelligence

> **When to load:** Stage 8 of the image generation pipeline, before firing any prompt to Higgsfield.
> **Prerequisite:** CREATIVE-DIRECTION.md must already be loaded (it defines the composition system this file extends).

This file is grounded in first-hand visual analysis of every reference image in the project. Each section describes exactly what that reference shows, so you can write accurate prompt context blocks and select the right attachments.

---

## How to use this file

1. Confirm the visual style (Stage 4) and theme (Stage 1)
2. Find the matching Package section below
3. Attach the reference files listed — in the priority order shown
4. Copy the Prompt Context Block into the opening of your prompt, before the scene description
5. Append the per-slide composition brief from Stage 7

The Context Block sets the visual register. The Stage 7 brief drives the specific scene and layout.

---

## Universal generation defaults — apply to EVERY style

These defaults are baked into every package below. They apply identically whether the style is illustration, photo, abstract pattern, abstract form, or infographic — that uniformity is what makes the format repeatable.

**Repeatable 3-reference recipe.** Within the hard 3-ref cap, every call is **[1] colour swatch (always) + [2] the one style-defining ref + [3] visible logo (only if logo gate = yes)**. If logo = no, slot 3 frees for the next-priority style ref; anything that doesn't fit goes into the prompt text. When logo gate = yes, slot [3] must be the actual visible logo PNG attached/shared as visual input; a relative path in the prompt is traceability only and never counts as the visual reference.

| Style | [2] Style-defining ref (mandatory) |
|---|---|
| Illustration | `3_Illustrations References/Main_reference.png` |
| Photo | the chosen `5_Photography References/*_exemplar.png` |
| Abstract pattern/form | clean pattern PNG from `2_Image References/Generated Patterns/` or best matching pattern crop from `Patterns in creatives/References/` |
| Infographic (3D / flat / polish) | `09_Icon-System/02_icon-system-overview.png` |
| Infographic (glass sub-style) | `4_Infographic Icon References/soft-dimensional-glass-icons-blue.png` |

**Style-purity default (v2.5).** Every call must have one primary style only. Do not combine illustration people, infographic flows, SaaS dashboards, 3D platform blocks, network maps, UI cards, and Cars24 service scenes in the same image unless the user explicitly approves that hybrid. Before firing, include the audit:

```
Primary style: [illustration / photo / abstract pattern-form / infographic-icon]
Secondary style allowed: [none / narrowly named exception]
Visual noun budget: [hero noun] + [support noun or none]
Rejected elements: [style contaminants removed]
Specific Cars24 moment: [one concrete moment or visual metaphor]
```

If a prompt includes more than one dominant visual system, simplify it before generation. Replace generic "AI workflow / connected ecosystem / intelligent platform" language with a specific Cars24 moment or a single abstract metaphor.

**Layout-selection default (v2.6).** Before any generation call, include the slide's layout plan in the assembled prompt context:

```
Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → framing mode (contained / intentional edge crop) → protected details → reason
```

For carousels and batches, do not use the same archetype or the same top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asked for a consistent repeated system. Batch visual territories must include layout + style, not style alone. If a layout reference cannot be attached because the colour swatch/logo/style ref consumes the 3-reference cap, keep the DT/LT layout ID and its layout traits in prompt text.

**1 — Colour anchor (always attach).** Attach `1_Brand Guidelines/02_Color-System/brand-blue-4736FE-swatch.png` on dark calls — caption *"match the whole empty background canvas to Cars24 Brand Blue #4736FE; do not render the swatch."* Attach `1_Brand Guidelines/02_Color-System/brand-blue-lavender-EBE9FF-swatch.png` on light calls — caption *"match the light background to exact pale lavender #EBE9FF derived from Cars24 brand blue; do not render the swatch."* Image models can blend colour cues across attached references, so without this the brand blue may drift to navy/indigo (verified Δ70–147). Always describe the hue with **exact hex + plain-language guardrails**: dark = *"Cars24 Brand Blue #4736FE as the dominant full-bleed canvas; add a subtle same-hue vertical or ambient gradient for premium depth, with an optional restrained radial glow around the hero/pattern zone. The gradient may drift slightly lighter or darker around #4736FE but must still read as bright Cars24 brand blue — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed AI-tech dark mode. Do not render the hex code as text."* Light = *"exact pale lavender #EBE9FF background derived from Cars24 Brand Blue; headline and short punch/tagline in #4736FE, descriptive body in #161616; do not render the hex codes as text."* Keep gradients controlled and same-hue; avoid "dark background", "deep blue", "midnight", "void", "black", "dramatic shadows", and "high-contrast dark field" for the canvas.

**2 — Visible logo context (attach if logo gate = yes).** On dark/brand-purple attach `1_Brand Guidelines/01_Brand-Identity-&-Logo/Logos/Logo - White-on-blue.png`; on light attach `Logo - Blue-on-white.png`; on high-contrast/print attach `Logo - Black.png`. The logo must be rendered inside the generated composite from this actual visual input. Also include the relative file path in the final prompt for traceability. Do not create a post-process/local logo overlay. For a carousel or batch, establish a theme-based logo lock: official colourway, placement, and optical size are fixed within each approved theme/background family, including white-on-brand, blue-on-light, white-on-dark-photo, and black-on-light/print. For a standalone image, use the correct colourway and balance it in the cleanest negative space. Preserve clear space and render it with no box/tile. The logo may overlap pattern, and may overlap hero only if readable, high-contrast, cleanly fitted, and fully uncropped. If the active provider/tool cannot attach the logo PNG as visual input, do not generate from text-only logo prompting; stop and ask the user to share/upload the logo so it can be used as visual input, or move to a reference-capable provider/workflow.

**3 — Typeface rendering (always, whenever the creative has baked-in text).** Image models **cannot read a font by name** — writing "Arapey" or "Geist" in a prompt does nothing, so the model defaults to a generic (almost always **sans-serif**) face; an Arapey-led dark headline silently renders as plain sans (verified, project 013). In every prompt with text, **describe each typeface visually and state its category (serif / sans-serif) explicitly**, append the font name only as a trailing hint, and spell the headline split out word-by-word:
- **Arapey (brand serif)** → *"an elegant high-contrast **serif** — refined thin strokes, classic bracketed serifs, editorial book-serif feel (in the spirit of Arapey)"*; Italic → *"a flowing **serif italic**"*; Regular → *"an upright **serif** (roman)"*.
- **Geist (brand sans)** → *"a clean modern geometric **sans-serif** (in the spirit of Geist)"* + weight.
- **Category guard in both themes:** append *"the headline is a SERIF typeface, not sans-serif"*. Body is always *"a clean modern sans-serif"*.

> Every Prompt Context Block below carries the colour-lock + generation-time logo-reference lines. Append them verbatim to the assembled prompt. Do not apply any local logo overlay after generation.

---

## Package 1 — Illustration

### Illustration reference model — style anchor + context anchors

Every illustration call uses the illustration folder as the style source:

`1_References/3_Illustrations References/`

Use references by role:

1. **Style anchor:** `Main_reference.png` is mandatory. It controls the Cars24 illustration language — modern sleek flat editorial, clean vector-like shapes, minimal shading, crisp silhouette edges, warm South Asian skin tones, deep navy-black hair, and brand-blue discipline.
2. **Scene supplement:** choose one additional illustration-folder file when useful for the scene.
3. **Approved identity/context reference:** approved photos, screenshots, product images, or proper-noun references are factual context only. They can preserve identity cues or object details, but they must be translated into the Cars24 illustration style and must not make the output photorealistic.

For a named person such as Gajendra Jangid, use `Main_reference.png` as the style anchor, `Frame 2147228886.png` if portrait framing support is useful, and the approved person photo only for identity cues. Preserve face structure, hairline, glasses, expression, and outfit direction while rendering a clearly illustrated Cars24 editorial hero.

### What each reference shows (from direct visual analysis)

**`Main_reference.png`** — PRIMARY ANCHOR — always attach first
A South Asian woman at a car steering wheel, slight cinematic angle, adjusting her sunglasses with one hand. Brand blue (`#4736FE`) completely dominates: the car interior, her jacket, the dashboard, the background city glimpsed through the windshield — all rendered in electric brand blue. Minimal shading — clean flat colour zones with 1–2 tonal steps only. Hair is deep navy-black rendered as a bold silhouette shape, not individual strands. Skin is warm caramel. Zero orange. The scene is simplified to the essential elements — no clutter. This is the quality and style standard. It defines: modern, sleek, premium flat editorial, not bold/chunky cartoon.

**`Frame 2147228886.png`** — solo portrait supplement
Close-up bust portrait of a South Asian woman on a light sky-blue background. Treat the background as reference context only: render the generated hero directly in the final Cars24 composite, without a separate portrait panel or transparent/chroma-key output. Choose contained framing or a deliberate editorial edge crop while protecting face and key expression. Navy-black hair, warm caramel skin. Clean aspirational face — almond eyes, defined brows, subtle confident smile. The character fills ~60% of the frame. Use when the scene is a portrait or upper-body composition.

**`Frame 2147228890.png`** — dynamic road scene supplement
A South Asian woman leaning out of a white car window, right arm raised joyfully. Yellow jacket, sunglasses. The background is dramatic: purple/violet mountain peaks, a long highway receding to the vanishing point, open sky. The colour palette here (yellow, purple, beige road, white car) is diverse — this reference anchors MOOD and ACTION, not colour discipline. Use for driving scenes, road imagery, freedom/joy moments.

**`Group.png`** — multi-character panoramic supplement
Wide landscape banner showing multiple South Asian families and groups in car scenarios across vignettes: loading luggage into red cars, sitting together, driving, celebrating. Warm orange/golden sunset tones in some panels, purple/blue tones in others. Multi-generational cast. Use for group scenes, family scenes, road trip mood, or any creative that needs more than one character.

**`freepik__semi-closeup-waistup-illustration-of-two-women-sta__75910 1 [Vectorized].png`** — service/handover supplement
Two South Asian women standing in front of an open orange car door, against a blue city skyline with teal trees. One in yellow top + sunglasses (customer), one in a blue Cars24 service uniform (agent). Both confident, celebratory stances. High colour contrast. Use when the scene involves a handover, agent-customer interaction, or service moment. Note: the Cars24 agent wears blue — always match this in prompted scenes.

### Reference attachment protocol

| Scene type | Primary (always attach) | Secondary (also attach) |
|---|---|---|
| Inside-car / driver POV | `Main_reference.png` | — |
| Solo female portrait | `Main_reference.png` | `Frame 2147228886.png` |
| Driving / open road / freedom | `Main_reference.png` | `Frame 2147228890.png` |
| Group / family / road trip | `Main_reference.png` | `Group.png` |
| Two people / handover / agent-customer | `Main_reference.png` | `75910 [Vectorized].png` |
| Male character | `Main_reference.png` | `Frame 2147228886.png` |
| Abstract / no character | `Main_reference.png` | — |

### Prompt Context Block — paste at start of every illustration prompt

```
Style: modern sleek flat editorial illustration in Cars24 brand visual language. Electric brand blue dominant colour — approximately 60% of the subject. Warm caramel South Asian characters with deep navy-black hair. Clean flat colour shapes with minimal shading (1–2 tonal steps per zone only). No gradients or photorealistic textures. Clean silhouette edges. Render the subject directly in the themed brand canvas in this same generation — no separate box, panel, or background card. Framing: [contained OR intentional editorial edge crop]; protect faces, focal interaction, action-carrying hands, and meaning-carrying product detail. A supporting car, shoulder, clothing edge, or restrained contextual environment may meet an edge only when it improves the composition and preserves the text zone. No text, numbers, or labels drawn into the subject art. Aspirational, confident, premium mood.
CANVAS COLOUR LOCK: dark output uses Cars24 Brand Blue #4736FE as the dominant full-bleed canvas with white text and white dots; the theme is dark only because the type and dots are white. Add a subtle same-hue vertical or ambient gradient for premium depth, with an optional restrained radial glow around the hero/pattern zone. The gradient may drift slightly lighter or darker around #4736FE but must still read as bright Cars24 brand blue — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed AI-tech dark mode. Do not render the hex code as text. Light background field is exact pale lavender #EBE9FF derived from Cars24 Brand Blue; headline and short punch/tagline in #4736FE, descriptive body in #161616. Do not render the hex codes as text.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale — all foreground elements stay full-saturation. On light theme: headline text is vivid saturated Brand Blue #4736FE — NOT navy, NOT grey-blue, NOT darkened, NOT desaturated, NOT charcoal. Body text is near-black #161616. The Cars24 logo is vivid Brand Blue #4736FE — same saturated blue as the headline, never greyed or muted. Do not let the pale-lavender canvas drag text, logo, or subject elements into washed-out territory.
TYPOGRAPHY (describe visually, never by font name — image models ignore names and default to sans): both dark and light headlines → set them in a refined editorial SERIF (in the spirit of Arapey), the emotive word in a flowing serif italic vs structural words in upright serif roman — the headline is a SERIF typeface, NOT sans-serif. Subheading/body → a clean modern sans-serif. Spell the per-word split out explicitly so the model commits. Visible copy is sentence case only; never title case, camel case, or all caps. Dark theme: all text white #FFFFFF. Light theme: headline Brand Blue #4736FE, descriptive body near-black #161616, short forward tagline Brand Blue #4736FE Geist Bold.
LOGO (if requested): render the Cars24 logo from the attached visible logo reference at [approved theme-based logo lock position], inside clean negative space and at the approved optical size. Relative logo path for traceability: [path]. Reproduce the rounded-square icon mark + "Cars24" wordmark faithfully in the correct theme colourway — white on dark, vivid Brand Blue #4736FE on light (never greyed or muted). For a carousel or batch, keep official colourway, placement, and optical size fixed within every approved theme/background family; for a standalone image, balance the correct colourway to its own layout. The logo may overlap pattern; it may overlap hero only if readable, high-contrast, cleanly fitted, and fully uncropped. No box/tile, no placeholder, no decorative effect, no cropped/cut logo, no later local overlay.
```

### Critical avoid list (from observed references)
- Never write "bold flat editorial" — the style is `modern sleek flat editorial` (different quality register, less chunky)
- Never write "electric blue and vivid orange colour palette" — orange is a 10% accent on cars/clothing only; this phrase produces orange-heavy outputs that break the brand
- Never instruct the generator to keep sky, roads, buildings, or any background — the subject is a clean-edged cutout-style hero composited directly INTO the themed brand canvas in the same single generation (no transparent export, no chroma-key)
- Never use hex codes in the prompt — use colour names ("electric brand blue", "warm caramel", "deep navy-black")
- The `freepik__flat-vector-editorial-illustration-fully-illustrat__75907 1 [Vectorized]-1.png` file does NOT exist in this project — do not reference it

---

## Package 2 — Photography

### What each photography layer shows (from direct visual analysis)

**Layer 1 — Product: Cars First** (`05_Photography-Style/02_product-cars-first.png`)
Multiple real car photos: SUVs and sedans in clean 3/4 exterior shots at aspirational real-world settings — residential driveways, scenic roads, open countryside. Bright daylight or golden hour. Cars are sharp, gleaming, and desirable. Fleet shots showing scale. Most shots have no people — the car is the sole hero. Backgrounds are naturalistic and contextual (homes, roads, architecture), never plain studio white.

**Layer 2 — Assisted Experience** (`05_Photography-Style/03_assisted-experience.png`)
Cars24 agents in branded royal blue polo shirts with customers at real homes and garages. Scenes: agent reviewing clipboard at car hood inspection, agent and customer inside the car, doorstep handover in a residential street. The customer's confidence and relief is the emotional centre — the agent is present but supportive, not dominant. Cars are real used vehicles in various conditions. Warm natural light.

**Layer 3 — Brand Lifestyle** (`05_Photography-Style/04_brand-lifestyle.png`)
South Asian families and couples in cars: interior shots of families laughing in rear seats, couple with sunroof open and arm raised, woman driving alone with quiet confidence, family loading luggage into an SUV boot, pet in car. Multi-generational. Warm golden light — these feel like real holiday or family photos, not staged shoots. Cabin/interior perspective is prominent. The car enables the story; the people are the hero.

**Layer 4 — Hubs & Infrastructure** (`05_Photography-Style/05_hubs-infrastructure.png`)
Cars24 showrooms with vivid blue and green brand architecture — very distinctive, immediately recognisable. Large car yards displaying fleet. Interior consultation areas. Multiple locations across markets. The brand's blue architecture functions as OOH branding in itself.

### Reference attachment protocol

| Content brief | Attach layer | Emotional register |
|---|---|---|
| Car as hero, product quality, trust | `02_product-cars-first.png` | Desire |
| Agent + customer, service, inspection | `03_assisted-experience.png` | Reassurance |
| Family, lifestyle, freedom, joy | `04_brand-lifestyle.png` | Joy |
| Scale, credibility, showroom, fleet | `05_hubs-infrastructure.png` | Credibility |

**Share all four files with the user at Stage 4 selection.** They know the content brief and can identify which layer fits.

**Plus, every call (see Universal generation defaults):** the chosen layer exemplar is slot [2]; always add the theme colour swatch as slot [1], and the visible logo context (`Logo - White-on-blue.png` dark / `Logo - Blue-on-white.png` light) as slot [3] when logo gate = yes. Append the colour-lock + generation-time logo-reference lines below to each block.

### Prompt Context Blocks — per layer

> Append to every photo block: **CANVAS COLOUR LOCK** — dark output uses a bright saturated Cars24 brand-blue canvas with white text and white dots; the theme is dark only because the type and dots are white. Match the attached swatch across the empty background canvas (NOT navy/indigo/black/midnight/dark violet/dimmed); light canvas background is a pale lavender tint derived from Cars24 brand blue in the #EBE9FF family, visibly light/lavender for theme distinction but NOT pink, NOT grey, NOT beige, NOT generic pastel purple, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out. The photo's warm tones belong to the subject only, never the canvas; keep the photo naturally lit, grade to the theme, never a purple/lavender tint. **LIGHT-THEME ELEMENT COLOUR LOCK** — "light theme" means ONLY the background is pale. Headline text is vivid saturated Brand Blue #4736FE (NOT navy, NOT grey-blue, NOT desaturated). Body text is near-black #161616. Logo is vivid Brand Blue #4736FE. Do not let the pale canvas drag foreground elements into washed-out territory. **PHOTO HERO DEFAULT** — clean photographic cutout removed from its original environment, placed directly on the Cars24 canvas, with a crisp visible white accent outline around the complete silhouette; no rectangular photo frame or embedded photo panel. Use contained framing or intentional editorial edge crop while protecting the face, focal interaction, action-carrying hands, and meaning-carrying product detail. **LOGO (if requested)** — render the Cars24 logo from the attached visible logo reference as actual visual input, include the relative logo path for traceability, and apply the fixed official colourway, placement, and optical size for each approved theme/background family in a carousel or batch; balance the correct colourway to a standalone layout. Keep it readable and uncropped, and use no box/tile or later local overlay.

**Product (Cars First):**
```
Cars24 product photography style. The car is the hero. Clean exterior shot, 3/4 angle, aspirational real-world setting — [suburban residential driveway / scenic open road / architectural backdrop]. Sharp, desirable, gleaming surface. Golden hour or clear bright daylight. No people unless specified. Cinematic depth of field. No text, no logos, no watermarks.
For blog-cover output, render the car as a clean photographic cutout removed from its environment, placed directly on the Cars24 canvas, with a crisp visible white accent outline around the complete car silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

**Assisted Experience:**
```
Cars24 assisted experience photography style. South Asian Cars24 agent in branded royal blue polo shirt and South Asian customer, [at car hood inspection / doorstep handover in residential street / inside the car reviewing paperwork]. Warm professional moment — customer's confidence and relief is the emotional centre. Genuine expression, not staged. Natural outdoor light. No text, no logos.
For blog-cover output, render the agent/customer/car moment as a clean photographic cutout removed from its environment, placed directly on the Cars24 canvas, with a crisp visible white accent outline around the complete silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

**Brand Lifestyle:**
```
Cars24 brand lifestyle photography style. [South Asian family laughing inside a moving SUV, golden light through windows / South Asian woman driving alone, sunroof open, warm evening light / South Asian couple loading luggage into car boot, excited road trip mood]. Warm golden light. Genuine joyful human moment — real, relatable, not model-perfect. Interior cabin perspective preferred. No text, no logos.
For blog-cover output, render the lifestyle subject as a clean photographic cutout removed from its environment, placed directly on the Cars24 canvas, with a crisp visible white accent outline around the complete silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

**Hubs & Infrastructure:**
```
Cars24 hub and infrastructure photography style. [Exterior showroom with vivid royal blue and green brand architecture, fleet displayed in forecourt / large car yard with rows of vehicles / interior consultation area, modern and professional]. Professional and at scale. Reinforces operational credibility. No text, no logos.
For blog-cover output, default to a cutout of the key hub/fleet subject placed directly on the Cars24 canvas with a crisp visible white accent outline. Use full-scene hub/showroom photography only when explicitly requested or when the real environment is essential to credibility.
```

---

## Package 3 — Abstract Pattern/Form (Dot-Form Hero)

### Pattern visual descriptions (from direct reference analysis)

When the user selects "Abstract pattern or form" (Style 3), default to a **contextual abstract dot-form hero**. In photo, illustration, and infographic styles, the dot pattern stays as background atmosphere behind the hero. In abstract style, the pattern treatment itself becomes the hero: dense Cars24 halftone/particle dots and bokeh falloff form one semantic silhouette, while lighter dots continue across the full canvas as atmosphere. The text area must remain readable.

The dot-form hero may form recognisable silhouettes such as a car, key, face, shield, road, document, funnel, or portal, as long as the result stays abstract and metaphor-led. Do not render a literal car/person/object surface. Do not create an illustration, photo scene, icon set, UI card, dashboard, 3D platform block, or infographic process flow. The silhouette must be contextual to the slide meaning, never a generic mountain, sphere, or tech wave by default.

#### Dark theme patterns (white luminous dots on #4736FE)

| CSS class | Reference file | What it looks like | Best for |
|---|---|---|---|
| `c24-pattern--mountain` | `mountain pattern dark theme.png` | Mountain/terrain silhouette formed from white luminous dot clusters. Dramatic twin peaks rising from the bottom-right corner. Dots are brightest at the ridgelines, softly dispersing into darkness above. | Launch posts, energy, forward momentum |
| `c24-pattern--circle-dark` | `large circle pattern dark theme.png` | Large luminous sphere arc. Sweeps from bottom-right toward upper-right. Very bright rim with particle bloom scatter around it. The sphere is mostly off-canvas — only the arc is visible. | Open layouts, depth and luminosity |
| `c24-pattern--side-mesh` | `side pattern dark theme.png` | Pink-magenta organic mesh blob on the right side. The ONLY dark pattern with a colour accent — pink/magenta gradient within the dot structure, not white. Sculptural, tactile, 3D-looking form. | Accent creative, editorial energy, pink-accented posts |
| `c24-pattern--wave-dark` | `full bleed pattern dark theme.png` | Regular grid of tiny white dots in flowing wave formation. Covers the full canvas. Subtle diagonal undulation. Even, atmospheric. | Text-only posts, pure type layouts |
| `c24-pattern--centre-mesh` | `Centre pattern dark thme.png` | Iridescent holographic organic mesh blob, centred. Multicolour within the dot structure (blue, teal, pink, violet). Used ONLY when there is no hero image. | Brand identity cards, logo lock-ups |
| `c24-pattern--bloom` | `Dark theme pattern large.png` | Scattered bokeh particles, soft and dispersed. Blue-teal tinted soft halos. Loose, atmospheric, like a starfield with colour. | Open airy layouts, breathing-room compositions |
| `c24-pattern--rhombus-dark` | `large rhombus pattern dark theme.png` | Rounded rectangle frame shape made of white luminous dots. Sweeps from the bottom-right corner, like a glowing border. Premium, contained feel. | Premium/aspirational posts, contained editorial frame |

#### Light theme patterns (brand blue #4736FE dots on #EBE9FF)

| CSS class | Reference file | What it looks like | Best for |
|---|---|---|---|
| `c24-pattern--circle-light` | `Circle pattern bottom light theme.png` | Blue halftone dot sphere dome. Rises from the bottom edge like a sunrise arc. Clean circle, no glow. Solid halftone dots, no blur. | Bottom-anchored editorial, aspirational upward mood |
| `c24-pattern--wave-full-light` | `Full bleed pattern light theme.png` | Blue dot wave grid, full canvas. Regular halftone wave undulation, diagonal flow from lower-left to upper-right. More visible than sparse variant. | Text-forward light posts |
| `c24-pattern--rhombus-light` | `Rhombus pattern in bottom.png` | Rounded corner rhombus shape, anchored bottom-right, blue halftone dots. Subtle containment frame. | Light editorial frame, contained bottom accent |
| `c24-pattern--side-light` | `Side Pattern light theme.png` | Purple-lavender sphere, partially visible on the right side. Has a colour accent (purple/violet) slightly deeper than the background. Soft, sculptural. | Side-accented editorial, organic side depth |
| `c24-pattern--wave-sparse` | `full bleed light pattern.png` | Very sparse, thin blue dots on near-white background. Almost invisible — present but delicate. | Minimal pure text posts, white-background layouts |
| `c24-pattern--face` | `human pattern light theme.png` | A human face in profile, rendered entirely from blue halftone dots on lavender. Very distinctive and specific. | AI identity posts, tech/digital theme creatives |

### Reference attachment protocol

Attach the clean pattern PNG for the pattern being used (slot [2]) — this anchors Higgsfield to the exact dot density, bokeh, depth falloff, and halftone language. If the needed family has no clean `Generated Patterns/` file, use the closest crop from `Patterns in creatives/References/` and explicitly tell the model to ignore cropped edges and colour cast. **Plus, every call (see Universal generation defaults):** the theme colour swatch as slot [1], and the visible logo context (`Logo - White-on-blue.png` dark / `Logo - Blue-on-white.png` light) as slot [3] when logo gate = yes.

### Prompt Context Block — paste at start of every abstract pattern/form prompt

```
Style: Cars24 abstract dot-form hero. Build the hero from the Cars24 halftone/particle pattern language itself — dense point-cloud dots, bokeh falloff, spatial depth, and lighter atmospheric dots flowing across the full canvas. The dot-form hero is one contextual semantic silhouette: [car / key / face / shield / road / document / funnel / portal / other brief-specific metaphor]. It must remain abstract and metaphor-led, made entirely of dots; do not render a literal object surface, illustration, photo, icon set, UI card, dashboard, 3D platform block, or infographic flow.
The hero formation is dense where the silhouette needs definition, then dissolves into lighter dots and soft bokeh around the edges. The surrounding canvas continues the same dot atmosphere at lower density, especially behind the hero zone. Keep the text zone clean and readable by reducing dot density and contrast behind all text.
Dark theme: white luminous dots on Cars24 Brand Blue #4736FE with controlled soft rim glow and bokeh depth; bloom is allowed but must not become a spotlight, and the canvas must stay bright Cars24 brand blue, not navy/indigo/black/dim.
Light theme: brand-blue #4736FE halftone dots on exact pale lavender #EBE9FF. Soft bokeh depth is allowed inside/around the dot-form hero, but keep the look clean blue halftone with little or no glow. Outside the hero form, keep dots restrained at approximately 20-25% opacity.
The abstract silhouette must be contextual to the slide's idea. Do not default to generic mountain terrain, generic sphere, generic tech wave, or decorative wallpaper unless that metaphor is explicitly the right one for the slide.
CANVAS COLOUR LOCK: dark output uses Cars24 Brand Blue #4736FE as the dominant full-bleed canvas with white text and white dots; the theme is dark only because the type and dots are white. Add a subtle same-hue vertical or ambient gradient for premium depth, with optional restrained radial depth around the dot-form hero. The gradient may drift slightly lighter or darker around #4736FE but must still read as bright Cars24 brand blue — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed AI-tech dark mode. Do not render the hex code as text. Light background field is exact pale lavender #EBE9FF derived from Cars24 Brand Blue; headline and short punch/tagline in #4736FE, descriptive body in #161616. Do not render the hex codes as text.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale — all foreground text/logo elements stay full-saturation. Headline text is vivid saturated Brand Blue #4736FE — NOT navy, NOT grey-blue, NOT darkened, NOT desaturated, NOT charcoal. Body text is near-black #161616. The Cars24 logo is vivid Brand Blue #4736FE, never greyed or muted.
TYPOGRAPHY: headline in a refined editorial SERIF (in the spirit of Arapey), emotive word in flowing serif italic, structural words in upright serif roman — the headline is a SERIF typeface, NOT sans-serif. Body in a clean modern sans-serif. Visible copy is sentence case only. Dark: all text white. Light: headline Brand Blue #4736FE, body near-black #161616, short forward tagline Brand Blue #4736FE.
LOGO (if requested): render the Cars24 logo from the attached visible logo reference as actual visual input. Relative logo path for traceability: [path]. For a carousel or batch, use the fixed official colourway, placement, and optical size for the approved theme/background family. For a standalone image, place the correct colourway in clean negative space to balance its individual layout. Reproduce the rounded-square icon mark + "Cars24" wordmark faithfully. The logo may overlap pattern and may overlap hero only if readable, high-contrast, cleanly fitted, and uncropped. No box/tile, no placeholder, no cropped/cut logo, no local overlay.
```

### Library-only isolated pattern prompt

Use the **Master Pattern Generation Prompt Formula** from `CREATIVE-DIRECTION.md` only when generating a reusable pattern texture asset for the library. It is not the prompt for final social creatives, because final creatives must include the themed canvas, dot-form hero, baked-in text, and logo when requested.

---

## Package 4 — Abstract Form (Legacy Colour Field / Brand Shapes)

This is now a legacy/special-case path. By default, Stage 4 "Abstract pattern or form" uses Package 3: the contextual abstract dot-form hero. Use this colour-field/brand-shape path only when the user explicitly asks for pure brand shapes with no dot-form hero. Abstract form uses Cars24 brand shapes — trapezoids (speed, momentum) and stars (trust, celebration) — as compositional heroes on a pure colour field. No character, no photography, no dot-form pattern hero. The shapes define the layout.

### Theme references to load

Load all reference images from the confirmed theme folder before designing:
- Dark: `2_Image References/Dark theme/` (9 files) — observe how text zone anchors upper-left, hero zone anchors right
- Light: `2_Image References/Light theme/` (7 files) — observe how the right half carries the visual

### Prompt Context Block

```
Cars24 brand abstract composition. [DARK / LIGHT] theme. Dark output uses Cars24 Brand Blue #4736FE as the dominant full-bleed canvas with white text/white accents; add a controlled same-hue vertical/ambient gradient for premium depth, with optional restrained radial glow around the hero/pattern zone. The gradient may drift slightly lighter/darker around #4736FE but must still read as bright Cars24 brand blue — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed AI-tech dark mode. Light background is exact pale lavender #EBE9FF derived from Cars24 brand blue so it remains distinct from dark while staying on-brand — NOT pink, NOT grey, NOT beige, NOT generic pastel purple, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out. Do not render hex codes as text. Bold geometric brand shapes: [trapezoid — conveys speed and forward momentum / star — conveys trust and celebration]. Clean flat colour fills, high contrast. No characters, no photography, no dot patterns, no environmental elements. Aspirational, premium, minimal. No text or logos baked into the shape art itself.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale — all foreground elements stay full-saturation. Headline text is vivid saturated Brand Blue #4736FE (NOT navy, NOT grey-blue, NOT desaturated). Body text is near-black #161616. Logo is vivid Brand Blue #4736FE. Do not let the pale canvas drag foreground elements into washed-out territory.
LOGO (if requested): reproduce the Cars24 logo from the attached visible logo reference as actual visual input — icon mark + "Cars24" wordmark — exactly, in white on dark, vivid Brand Blue #4736FE on light (never greyed or muted). Relative logo path for traceability: [path]. For a carousel or batch, use the fixed official colourway, placement, and optical size for the approved theme/background family; for a standalone image, balance the correct colourway to its layout. No cropped/cut logo or box/tile; ignore the logo reference background tile.
```

---

## Package 5 — Infographic / Icon

### What the references show (from direct visual analysis)

**`02_icon-system-overview.png`** — Overview of the full Cars24 icon vocabulary
Two rows: top row = 3D icons, bottom row = flat icons. Both systems cover the car service journey.

**Cars24 icon vocabulary — what exists in the system:**

| Concept | 3D icon | Flat icon |
|---|---|---|
| Car (product view) | Compact car, front 3/4 | Simplified car silhouette |
| Car + price tag | Car with hanging tag | Car + tag outline |
| Quality inspection | Car + magnifying glass | Car + magnifier |
| Trust / protection | Shield + checkmark | Shield + car |
| Documentation | Papers + car motif | Documents + car |
| Financing / payment | Car + coin/percentage | Car + rupee/dollar |
| Vehicle servicing | — | Car + wrench |
| Tyre service | — | Tyre + wrench |
| Car wash / detailing | — | Car + sparkle marks |
| Vehicle towing | — | Car on flatbed truck |
| Car comparison | — | Two cars side-by-side |
| Number plate check | Plate + magnifier | — |
| Payment terminal | POS terminal device | — |
| Wallet / money bag | Open wallet / coin bag | — |
| Gift / new car | Car with ribbon bow | — |
| Checklist + shield | Document + shield | — |
| Car keys | — | Key |

**`03_3d-icon-generator.png`** — 3D Icon style guide
Use for: product features, marketing callouts, landing pages. Visual rules: moderate 3D realism (not photoreal — like high-quality iOS app icons). Consistent blue-based colour system. Crisp highlights from top-left, controlled subtle shadow. Simple subjects — 1–2 elements per icon. Render directly on the themed composite, with no separate background/export.

**`04_flat-icon-generator.png`** — Flat Icon style guide
Use for: UI menus, dashboards, infographic flows, high-density layouts. Visual rules: solid brand blue fills only — no gradients, no shadows, no outlines. Bold clean silhouettes. Single-object concept per icon. High contrast for readability.

**`soft-dimensional-glass-icons-blue.png`** — Soft dimensional glass icon style anchor
Use for: premium marketing infographic slides, process flows, feature symbols, and icon-led explanations that should feel richer than flat UI icons but lighter than full 3D product icons. Visual rules: filled rounded geometric shapes, translucent pale-blue/frosted-glass front layers over saturated Cars24 brand-blue base layers, soft internal blur at overlaps, gentle top-left highlight, minimal details, no text inside icons.

**`soft-dimensional-glass-icons-mint.png`** — Soft dimensional glass secondary style anchor (internal reference only)
This file documents a mint/teal variant for internal reference. Do NOT attach it to generation calls and do NOT use mint, teal, or green tones in generated infographic icons. All generated icons must stay within the brand-blue monochrome family per the ICON COLOUR LOCK. If the user explicitly requests a mint accent, confirm before proceeding — it overrides the default brand-blue-only rule.

**Soft-reference rule** — when the user has NOT explicitly selected the glass sub-style, the soft-dimensional-glass images are optional finish inspiration only. They may teach softness, highlight discipline, rounded filled forms, and gentle depth. They must not replace the Cars24 icon system, create glass UI tiles, create one large glass slab, or push outputs toward generic app-icon sheets. When the user HAS explicitly selected the glass sub-style (at Stage 4), `soft-dimensional-glass-icons-blue.png` becomes the slot [2] style-defining reference — see conditional slot-2 rule in the Universal generation defaults table above.

### Reference attachment protocol

| Task | Always attach (slot [2]) | Also attach |
|---|---|---|
| Any infographic / icon brief (default) | `02_icon-system-overview.png` | — |
| Premium marketing / feature callout icons | `02_icon-system-overview.png` | `03_3d-icon-generator.png` when slot free |
| 3D style icons | `02_icon-system-overview.png` | `03_3d-icon-generator.png` |
| Flat style icons | `02_icon-system-overview.png` | `04_flat-icon-generator.png` |
| **Soft dimensional glass icons** | **`soft-dimensional-glass-icons-blue.png`** | — |
| Same icon type as a prior run | `02_icon-system-overview.png` | Matching file from `4_Infographic Icon References/` (this is the PRIMARY anchor for repeats) |

**Plus, every call (see Universal generation defaults):** slot [2] is the style-defining ref from the table above (icon-system overview for 3D/flat/polish, or soft-dimensional-glass-blue for glass sub-style); always add the `#4736FE` colour swatch as slot [1], and the visible logo context (`Logo - White-on-blue.png` dark / `Logo - Blue-on-white.png` light) as slot [3] when logo gate = yes.

### Prompt Context Blocks

**For 3D icons:**
```
Cars24 brand icon system, 3D icon style. Moderate 3D realism — like a high-quality iOS app icon, NOT photoreal or cinematic. Consistent blue-based colour system (#4736FE dominant body). Crisp highlights from top-left, controlled subtle shadow. Simple subject — 1–2 elements only. No micro-details. Icons render directly onto the themed brand canvas in the same single composite — no transparent export, no chroma-key, no background card. No text, no labels inside the icon.
ICON COLOUR LOCK: ALL icons use ONLY the Cars24 brand-blue colour family — saturated Brand Blue #4736FE fills, lighter periwinkle highlights, deeper navy shadows, and white reflective accents. NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow, NO multi-colour semantic coding. A "green approved stamp" is rendered in brand blue; a "tech/AI node" is rendered in brand blue. Colour hierarchy comes from tonal variation within blue (saturated vs highlight vs shadow), never from introducing a second hue.
CANVAS COLOUR LOCK: dark output uses a bright saturated Cars24 brand-blue canvas with white text — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed. Light background is a pale lavender tint in the #EBE9FF family — NOT pink, NOT grey, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale. Headline is vivid Brand Blue #4736FE (NOT desaturated). Body is near-black #161616. Logo is vivid Brand Blue #4736FE. Icons stay full-saturation brand blue, not washed out by the pale background.
LOGO (if requested): Cars24 logo in white on dark, vivid Brand Blue #4736FE on light (never greyed), bottom-left, no box/tile.
Icon to generate: [DESCRIBE ICON — e.g. "car with magnifying glass for vehicle inspection"].
Match the style, proportions, and finish of the attached icon system reference. Do NOT reproduce the exact icons shown in the reference.
```

**For flat icons:**
```
Cars24 brand icon system, flat icon style. Solid brand blue (#4736FE) filled silhouette — no gradients, no shadows, no outlines, no decorative elements. Bold clean shape. Single-object concept. High contrast for readability at small sizes. Icons render directly onto the themed brand canvas in the same single composite — no transparent export, no chroma-key, no background card. No text, no labels inside the icon.
ICON COLOUR LOCK: ALL icons use ONLY brand blue #4736FE filled shapes + white negative-space cuts. NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow. Monochrome brand blue only.
CANVAS COLOUR LOCK: dark output uses a bright saturated Cars24 brand-blue canvas with white text — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed. Light background is a pale lavender tint in the #EBE9FF family — NOT pink, NOT grey, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale. Headline is vivid Brand Blue #4736FE (NOT desaturated). Body is near-black #161616. Logo is vivid Brand Blue #4736FE. Icons stay full-saturation brand blue, not washed out.
LOGO (if requested): Cars24 logo in white on dark, vivid Brand Blue #4736FE on light (never greyed), bottom-left, no box/tile.
Icon to generate: [DESCRIBE ICON].
Match the style, proportions, and visual weight of the attached flat icon reference. Do NOT reproduce the exact icons shown in the reference.
```

**For soft dimensional glass icons (when explicitly selected as sub-style):**
```
Cars24 brand icon system, soft dimensional glass style. Filled rounded geometric shapes with translucent pale-blue frosted-glass front layers over saturated Cars24 brand-blue base layers. Soft internal blur at overlaps. Gentle top-left highlight. Minimal details — 1–2 elements per icon. No text inside icons. Each icon sits inside a rounded-rect glass tile with subtle depth. Icons render directly onto the themed brand canvas in the same single composite — no transparent export, no chroma-key, no background card.
ICON COLOUR LOCK: ALL icons use ONLY the Cars24 brand-blue colour family — saturated Brand Blue #4736FE base layers, translucent pale-blue frosted overlays, and white highlight accents. NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow, NO multi-colour semantic coding. Every icon is the same blue-family tone. Colour hierarchy comes from opacity and translucency within blue, never from a second hue.
CANVAS COLOUR LOCK: dark output uses a bright saturated Cars24 brand-blue canvas with white text — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed. Light background is a pale lavender tint in the #EBE9FF family — NOT pink, NOT grey, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale. Headline is vivid Brand Blue #4736FE (NOT desaturated). Body is near-black #161616. Logo is vivid Brand Blue #4736FE. Icons stay full-saturation brand blue, not washed out.
TYPOGRAPHY: headline in a refined editorial SERIF (in the spirit of Arapey), emotive word in flowing serif italic, structural words in upright serif roman — the headline is a SERIF typeface, NOT sans-serif. Body in a clean modern sans-serif. Dark: all text white. Light: headline Brand Blue #4736FE, body near-black #161616. Sentence case only.
LOGO (if requested): Cars24 logo from the attached visible logo reference as actual visual input, in white on dark, vivid Brand Blue #4736FE on light (never greyed). Relative logo path for traceability: [path]. For a carousel or batch, use the fixed official colourway, placement, and optical size for the approved theme/background family; for a standalone image, balance the correct colourway to its layout. No box/tile or cropped/cut logo.
Icon to generate: [DESCRIBE ICON].
Match the translucent layered glass depth of the attached soft-dimensional-glass reference. Do NOT reproduce the exact icons shown — generate contextual icons for the brief.
```

**For controlled dimensional polish icons (optional finish layer, not a sub-style):**
```
Cars24 brand icon system first. Use the 3D icon style for premium marketing/feature callouts, or the flat filled icon style for dense/process/UI flows. If the icon layer feels too flat, add controlled dimensional polish only: subtle fill depth, soft top-left highlight, slight shadow, rounded filled forms, and clear readable silhouettes. This is a finish layer on top of an existing icon style, not its own sub-style. Icons render directly onto the themed brand canvas in the same single composite — no transparent export, no chroma-key, no background card. No text, no labels inside the icon.
ICON COLOUR LOCK: ALL icons use ONLY the Cars24 brand-blue colour family — saturated Brand Blue #4736FE fills, lighter periwinkle highlights, deeper navy shadows, white reflective accents. NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow, NO multi-colour. Colour hierarchy from tonal blue variation only.
CANVAS COLOUR LOCK: dark = bright saturated Cars24 brand-blue canvas, NOT navy/indigo/black/midnight/dimmed. Light = pale lavender #EBE9FF family, NOT pink/grey/grey-white/cream/ice-blue/washed-out.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" = pale background only. Headline vivid Brand Blue #4736FE. Body near-black #161616. Logo vivid Brand Blue. Icons full-saturation brand blue.
LOGO (if requested): Cars24 logo in white on dark, vivid Brand Blue #4736FE on light, bottom-left, no box/tile.
Icon to generate: [DESCRIBE ICON].
Do NOT use thin outline icons, plain white line art as the primary icon style, glassmorphic app tiles, one large glass slab, generic SaaS symbols, abstract broken symbols, heavy photorealistic 3D, chrome/clay/toy rendering, or text inside icons.
```

**For infographic flow:**
```
Cars24 infographic icon flow. [N] steps, [left-to-right / top-to-bottom]. Icon style: [3D / flat / soft dimensional glass — as selected at Stage 4]. Steps: [list each step and icon concept]. Use thin brand-blue or white connectors between steps; dotted connectors are allowed when subtle. Step labels below each icon in a clean modern sans-serif. All icons identical optical weight. The whole flow renders directly onto the themed brand canvas in the same single composite — no transparent export, no chroma-key, no bounding box.
ICON COLOUR LOCK: ALL icons use ONLY the Cars24 brand-blue colour family — saturated Brand Blue #4736FE fills, pale translucent blue overlays, white highlight accents. NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow, NO multi-colour semantic coding. Every icon matches in blue-family tone and optical weight.
CANVAS COLOUR LOCK: dark output uses a bright saturated Cars24 brand-blue canvas with white text and white dots; the theme is dark only because the type and dots are white. Match the attached swatch across the empty background canvas — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed. Light background is a pale lavender tint in the #EBE9FF family — NOT pink, NOT grey, NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out; faint same-hue glow only.
LIGHT-THEME ELEMENT COLOUR LOCK: "light theme" means ONLY the background is pale. Headline is vivid Brand Blue #4736FE (NOT navy, NOT grey-blue, NOT desaturated). Body is near-black #161616. Logo is vivid Brand Blue #4736FE. Icons stay full-saturation brand blue, not washed out by the pale background.
TYPOGRAPHY: headline in a refined editorial SERIF, emotive word in flowing serif italic, structural words in upright serif roman — NOT sans-serif. Body in a clean modern sans-serif. Dark: all text white. Light: headline Brand Blue #4736FE, body near-black #161616. Sentence case only.
LOGO (if requested): Cars24 logo from the attached visible logo reference as actual visual input, in white on dark, vivid Brand Blue #4736FE on light (never greyed or muted). Relative logo path for traceability: [path]. For a carousel or batch, use the fixed official colourway, placement, and optical size for the approved theme/background family; for a standalone image, balance the correct colourway to its layout. No box/tile or cropped/cut logo; ignore the logo reference background tile.
```

---

## Package 6 — USP Badges

### What the badges look like (from direct visual analysis)

From `08_Campaign-Assets-&-USPs/03_usp-mnemonics.png`:

**Visual treatment (corrected from vision analysis of 03_usp-mnemonics.png):** The badges are displayed on **white / light-grey tiles** in the brand guidelines — not on a solid black background. The badge artwork itself is **two-tone: black structural elements + bright neon green** as the highlight/energy colour. Green is used as a highlight block, glow, or fill behind key elements (e.g. "WARRANTY" sits on a green bar; Kavach+ and Easy Financing show a green halo/burst behind the icon). The numerals ("300+", "30") are oversized and act as the visual hook. Wordmarks are **heavy, condensed, all-caps** — bold and stamp-like. Two sizes per badge: icon-only compact stamp and horizontal icon + full text lockup.

**Six badges:**

| USP | Icon element | Visual notes |
|---|---|---|
| **Lifetime Warranty** | Shield + infinity (∞) loop | Green infinity loop on black shield outline |
| **Kavach+ RC Transfer Guarantee** | Shield + car + checkmark | Shield with small car motif and tick mark |
| **Easy Financing** | Rupee coin (₹) + checkmark | Circular coin with check, mint green |
| **300+ Quality Checks** | "300+" bold numeral | Large number dominates, badge border |
| **30 Day Free Repair** | "30" large + wrench + calendar arc | "30" numeral very large, wrench and arc circle |
| **30 Day Return Guarantee** | "30" large + circular arrows | "30" numeral very large, recycling/return arrows |

**Icon-only size:** Compact. For corner stamps, inline callouts, small UI.
**Full-text size:** Large. For hero stamp overlays on a creative — the text lockup is readable at social media sizes.

### Attachment protocol

- Load and share `03_usp-mnemonics.png` with the user when USP badges are needed
- Ask which badge(s) and which size (icon-only or full-text)
- Attach the file to the Higgsfield call when generating creatives that incorporate USP elements

### Position rules (compositing, not generation)

- USP badges are overlays — never integrated into the illustration or photography
- Position: corner stamp (bottom-right or bottom-left of the canvas), or anchored to the hero zone
- They sit above the pattern layer and below the logo
- Never place USP badges in the text zone

### Generating new USP-style elements via Higgsfield

If a new badge is needed (not one of the six existing):
```
Cars24 USP badge stamp. Two-tone: black structural elements + bright neon green as the highlight and energy colour. [ICON ELEMENT — e.g. shield with checkmark]. [USP TEXT — e.g. "INSTANT PAYMENT" in all-caps, heavy condensed letterforms]. Bright green used as highlight block or glow behind the key element; black for structure and typography. Bold stamp authority — stamp-like, high-contrast, more aggressive than the main brand. Render as an overlay inside the final composite, with no separate transparent export. No other colours — only black and bright neon green.
```

---

## Package 7 — Theme Composition Context

### Dark theme composition (from analysis of 9 template images)

**What the templates confirm:**

| Element | Observed behaviour |
|---|---|
| Background | Bright Cars24 Brand Blue `#4736FE` with subtle luminous glow in the pattern zone — not a flat dead fill, but also not a darkened/navy canvas. A very gentle same-hue light shift where the pattern sits. |
| Text zone | Upper-left. Always clean — no pattern intrusion. Headline is large (40–60% of canvas height). Mixed Arapey Italic (emotive word/s) + Geist Bold (structural words). All white. |
| Hero zone | Right side or bottom-right. Use contained framing or an intentional editorial edge crop. Protect the face, focal interaction, action-carrying hands, and meaning-carrying product detail; only supporting forms may exit an edge. Scale varies: 40–60% of canvas. |
| Pattern zone | Bottom-right. White luminous dots. Mid scale when hero is present. The pattern sits behind the hero — they coexist in the same zone. |
| Format | 4:5 portrait — 1080×1350 |
| Typography note | Body copy is small Geist Regular, white. Strong size contrast with headline. |

**Composition law:** text zone is clean upper-left → pattern + hero occupy the lower-right → the two zones never mix.

### Light theme composition (from analysis of 7 template images)

**What the templates confirm:**

| Element | Observed behaviour |
|---|---|
| Background | `#EBE9FF`-family pale lavender derived from Cars24 brand blue — flat, soft, visibly distinct from dark while staying closer to brand blue than pink/grey/beige/generic pastel purple. |
| Text zone | Left half of the square canvas. Headline in brand blue with Arapey-led serif dominance. Body in near-black `#161616`. |
| Hero zone | Right side. Character takes the right 40–60% of the canvas. In the square format, characters are often more dominant and centred than in the dark 4:5 format. |
| Pattern zone | Right side or bottom-right. Blue halftone dots, no glow. More restrained than dark — the blue on lavender creates lower contrast. Sometimes full-bleed but at very low opacity. |
| Format | 1:1 square — 1080×1080 |
| Typography note | Arapey-led serif headlines in light theme, same refined editorial serif system as dark; brand blue headlines, near-black body. |

**The `face` pattern** (halftone dot face in profile) appears only in light theme — it is highly specific. Only use it for AI/tech/digital identity content.

---

## Quick Reference — Attachment Checklist

Before firing any Higgsfield call, confirm:

```
□ COLOUR ANCHOR (EVERY call) → dark: brand-blue-4736FE-swatch.png / light: brand-blue-lavender-EBE9FF-swatch.png as slot [1] 🎨; describe hue with exact hex + plain-language guardrails and say not to render hex codes as text
□ VISIBLE LOGO CONTEXT (if logo gate = yes) → Logo - White-on-blue.png (dark) / Logo - Blue-on-white.png (light) — logo is rendered during generation; no local overlay
□ Illustration style → Main_reference.png (always) + scene supplement (if a slot is free)
□ Photography style → matching layer exemplar (share all 4 with user first)
□ Abstract pattern/form → contextual dot-form hero by default + matching clean pattern PNG from Generated Patterns/ or best matching pattern crop
□ Abstract form legacy special-case → Atlas dark/light LAYOUT card only when the user explicitly asks for pure brand shapes
□ Infographic → 02_icon-system-overview.png + 3D or flat generator file
□ USP on any slide → 03_usp-mnemonics.png (load and confirm with user)
□ 3-ref recipe → [1] swatch + [2] one style-defining ref + [3] visible logo (if logo=yes); overflow → prompt text
□ Theme references → load Dark theme/ or Light theme/ folder before Stage 6
□ Prompt Context Block → paste the matching block (incl. its colour-lock + faithful-logo lines) at the top of the prompt
□ Stage 7 brief → append the per-slide composition brief after the Context Block
```
