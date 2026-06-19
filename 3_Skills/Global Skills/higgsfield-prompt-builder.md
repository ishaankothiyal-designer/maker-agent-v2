---
name: higgsfield-prompt-builder
description: Assembles complete per-slide Cars24 image-generation prompts. Handles single posts and multi-slide carousels. Covers background, logo placement, pattern, typography, subject, and reference instruction for each slide.
---

# Image Prompt Builder — Cars24

> Load **both** before using this builder:
> 1. `1_References/CREATIVE-DIRECTION.md` — composition system, pattern families, typography rules
> 2. `1_References/HIGGSFIELD-CONTEXT-PACKAGE.md` — visual intelligence for every reference image + Prompt Context Blocks per style
> 3. `1_References/reference-index.json` — v2.0 machine-readable reference tags for role-based selection, attachability, copy-from, ignore-from, and marble/statue guards
>
> For exact specs while filling a block, pull the matching vision-verified brand-guideline `notes.md` (index in CREATIVE-DIRECTION → *Brand Guidelines — Deep Reference*): colour hex → `02_Color-System/notes.md`; type roles/weights → `03_Typography/notes.md`; CTA + safe-zone specs → `07_Digital-Composition-&-Templates/notes.md`; icon specs → `09_Icon-System/notes.md`; USP stamps → `08_Campaign-Assets-&-USPs/notes.md`; luxury palette → `10_Luxury-&-Elite-Sub-Brand/notes.md`.
>
> Every slide gets its own fully assembled prompt. Generate in approved slide/row order; do not run carousel or batch slides in parallel unless the user explicitly asks for parallel execution after approving the risks.

---

## Step 0 — Pre-generation questions (ask in order, stop early if answers are obvious from the brief)

After copy is confirmed final:

1. **How many slides?** (1 = single post · 2–10 = carousel)
2. **Format?** Instagram portrait 4:5 · Instagram square 1:1 · LinkedIn 1.91:1 · X 16:9 · blog 16:9
3. **Theme?** Dark (`#4736FE` brand-blue field) or light (`#EBE9FF`-family pale brand-blue lavender) — infer from brief if clear (campaign/editorial → dark · everyday social → light)
4. **Subject type per slide?** Illustration · photo/realistic · abstract/text-only — can vary slide to slide

For carousels: confirm whether the same theme runs across all slides unless the user specifies otherwise. Keep the brand system and typography consistent, but vary layout archetype and vertical anchor across the set. Do not use the same archetype or top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asks for a repeated system.

---

## Model Selection

**Provider default**
- **Codex preview/exploration:** call Codex ImageGen / `image_gen`.
- **Codex production export:** use a file-producing project-local path from the start, preferably `tools/maker_image_export.py` or an approved provider CLI that writes directly into `4_exports/{serial}_{brief}_{DD-Mon}/vN/`.
- **Claude / non-Codex CLI:** use Higgsfield + GPT Image 2 (`gpt_image_2`) by default.
- Use Higgsfield in Codex only when the user explicitly requests it, Codex ImageGen is unavailable/unsuitable, or comparison/fallback is needed.

The assembled five-block prompt is identical regardless of which generator is used. Only the call mechanism changes.

**Higgsfield model chain (when using Higgsfield):**
1. `gpt_image_2` — default for Claude/non-Codex creative image generation
2. User-specified model — if the user names a model explicitly, use it; same assembled prompt applies

**Codex ImageGen:**
- Use the built-in Codex ImageGen / `image_gen` tool
- Pass the same fully assembled five-block prompt as the generation input
- Pass reference image paths alongside the prompt where the tool supports image inputs
- Same reference image selection logic applies
- Use this path for preview/exploration unless a local file handle can be verified. For production exports, prefer `tools/maker_image_export.py` so the generated file and chat preview are the same bitmap.

**Codex production export helper:**
```bash
python tools/maker_image_export.py \
  --input prompts.jsonl \
  --brief "[brief slug or title]" \
  --size 1536x1024 \
  --resize 1000x650
```

The helper prints absolute Markdown image links after generation. Use those links to preview the exact files saved in `4_exports/`.

---

## Per-Slide Prompt Assembly

For each slide, assemble these five blocks in order. All five must be present.

```
[BLOCK 1 — CANVAS, LAYOUT & LOGO]
[BLOCK 2 — BACKGROUND & PATTERN]
[BLOCK 3 — TYPOGRAPHY & COPY]
[BLOCK 4 — SUBJECT]
[BLOCK 5 — REFERENCE INSTRUCTION]
```

---

### Block 1 — Canvas, Layout & Logo

```
Cars24 brand creative. [DARK / LIGHT] theme. Slide [N] of [TOTAL].
Canvas: [FORMAT — see aspect ratios below].
Single composed generation rendered back to front: background → atmospheric pattern / abstract dot-form hero → typed subject → baked-in text → generation-time logo if needed.
Layout plan:
  Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason.
  Use the chosen archetype from the current master layout family; the classic left-text/right-hero split is common, not mandatory.
  Text zone must remain clean and readable. Illustration, photo, and infographic heroes are fully contained inside the canvas with full head, hands, car/icons, and key objects visible. Abstract pattern/form uses the dot pattern itself as the hero system.
Logo placement: [bottom-left / centre-bottom for centre layouts / none]. If logo is needed, render it from the attached theme-matched visible logo reference inside clean negative space, about 8–10% of canvas width, with no box/tile and no later local overlay.
Note: match logo alignment to the layout axis. Centre/symmetric layouts usually use centre-bottom.
```

**Aspect ratio reference:**
| Format | Ratio | Higgsfield aspect-ratio flag |
|---|---|---|
| Instagram portrait | 4:5 | `--aspect_ratio 4:5` |
| Instagram square | 1:1 | `--aspect_ratio 1:1` |
| LinkedIn banner | 16:9 | `--aspect_ratio 16:9` |
| X card | 16:9 | `--aspect_ratio 16:9` |
| Blog header | 16:9 | `--aspect_ratio 16:9` |
| Story / Reel | 9:16 | `--aspect_ratio 9:16` |

---

### Block 2 — Background & Pattern

**Background line (always):**
```
Background: [dark = Cars24 brand-blue field / light = #EBE9FF-family pale brand-blue lavender] single-hue field, full bleed, with a subtle same-hue glow. Dark must stay vivid electric brand blue, not navy/indigo/dark violet/heavily darkened. Light must remain visibly lavender for light/dark distinction while staying derived from brand blue, not pink/grey/beige/generic pastel purple. No multi-colour gradient, no harsh vignette.
```

**Pattern decision:**
- Does this slide have a hero subject AND a large open negative space zone? → include pattern, mid scale
- Is this slide text-only or does the hero fill the frame? → include pattern, large scale or full-frame
- Is the slide very copy-dense with minimal breathing room? → micro pattern or none

```
Pattern: [FAMILY] positioned at [PLACEMENT].
[PASTE PATTERN PROMPT BASE from CREATIVE-DIRECTION.md §Pattern Family Reference]
Scale: [mid / large / full-frame / micro / none].
Pattern may flow across the full background, but stays behind text and hero and preserves text readability.
Pattern color: [white luminous dots, soft glow / brand blue dots, no glow].
```

If no pattern needed:
```
Pattern: none. Background field only behind subject.
```

---

### Block 3 — Typography & Copy

**Step 1 — Determine this slide's text structure:**
- Headline + subheading + body present → **Scenario 1 (full layout)**
- Headline only, no subheading or body → **Scenario 2 (standalone)**
- Part of a carousel → **Creative direction decides per slide** — state which scenario applies explicitly in the prompt

**Step 2 — Select Arapey style (Scenarios 1 and 2 only):**
- Emotive/campaign tone → Arapey **Italic**
- Product/factual tone → Arapey **Regular**

---

**Scenario 1 — Full layout (headline + subheading + body):**

*Dark theme:*
```
Typography — dark theme (full layout):
Headline (top-left, white):
  Full Arapey [Italic / Regular] — [Italic: emotive/campaign · Regular: product/factual].
  Size: very large — 40–60% of canvas height.
Headline text: "[EXACT HEADLINE]"

Subheading (below headline, white, Geist Medium):
  Size: medium — clear step down from headline.
Subheading text: "[EXACT SUBHEADING]"

Body copy (white, Geist Regular, small):
  Size: small — strong size contrast against headline.
Body text: "[EXACT BODY]"
```

*Light theme:*
```
Typography — light theme (full layout):
Headline (top-left, brand blue #4736FE):
  Full Arapey [Italic / Regular] — [Italic: emotive/campaign · Regular: product/factual].
  Size: very large — 40–60% of canvas height.
Headline text: "[EXACT HEADLINE]"

Subheading (below headline, near-black #161616, Geist Medium):
  Size: medium.
Subheading text: "[EXACT SUBHEADING]"

Body copy (near-black #161616, Geist Regular, small):
  Size: small.
Body text: "[EXACT BODY]"
```

---

**Scenario 2 — Standalone headline only:**

*Dark theme:*
```
Typography — dark theme (standalone headline):
Headline (top-left, white):
  Mixed font pairing — Arapey Italic for emotive/key words · Geist Bold for structural words.
  Arapey Italic: [IDENTIFY THE KEY EMOTIVE WORD(S)]
  Geist Bold: all remaining words.
  Size: very large — 40–60% of canvas height.
Headline text: "[EXACT HEADLINE]"

Subheading: none.
Body copy: none.
```

*Light theme:*
```
Typography — light theme (standalone headline):
Headline (top-left, brand blue #4736FE):
  Arapey-led serif headline — refined editorial serif, emotive word in flowing serif italic vs structural words in upright serif roman. The headline is a SERIF typeface, not sans-serif.
  Size: very large — 40–60% of canvas height.
Headline text: "[EXACT HEADLINE]"

Subheading: none.
Body copy: none.
```

---

### Block 4 — Subject

**Illustration:**
```
Subject: modern sleek flat editorial vector illustration.
[DESCRIBE: who, what they are doing, mood, clothing colors, environment]
Character: South Asian [woman/man/family] — warm caramel skin tones, deep navy-black hair, expressive, not stock-photo generic.
Palette: electric brand blue DOMINANT (~60% — interiors, large clothing shapes, environment) · deep navy + mint green secondary (~30%) · vivid orange ONLY on cars or an occasional clothing accent + warm skin (~10%). Brand blue leads; orange is never dominant or a background.
Lighting/mood harmonised to the [DARK → warmer, more luminous rim light / LIGHT → cleaner, brighter key light] theme — but do NOT recolour the subject to the canvas and do NOT bake any background in.
Rendered as a clean cutout with a visible edge definition, fully contained over the background and pattern.
Positioned right / bottom-right. Bleeds beyond the right canvas edge.
Match the rendering style, flat vector quality, and colour saturation of the attached illustration reference.
Do NOT reproduce the exact scene from the reference.
```

**Photo / photorealistic — Layer 1: Product (Cars First):**
```
Subject: Cars24 product photography style. The car is the sole hero — no people in frame.
Car: [DESCRIBE — e.g. "silver compact SUV", "red hatchback", "graphite-grey crossover"].
Framing: 3/4 front angle or clean side profile. Car fills lower-centre of frame. Glossy bodywork with crisp highlight reflections.
Setting: [suburban residential driveway / forecourt row at low oblique angle showing depth / highway flyover at golden hour / architectural backdrop such as a tiled gateway or modern villa] — NOT a plain white studio.
Lighting: natural daylight or golden-hour warm low-sun light. Slightly warm grade, true-to-life, not stylised. The car gleams.
Mood: sharp, premium, desirable, confident.
Clean photographic cutout with a visible white accent outline, composited over brand canvas. Positioned right / bottom-right, fully contained inside the canvas.
Do NOT reproduce the exact car or scene from the reference.
No text, no logos, no watermarks.
```

**Photo / photorealistic — Layer 2: Assisted Experience:**
```
Subject: Cars24 assisted experience photography style. Cars24 agent in royal-blue branded polo shirt + South Asian customer.
Scene: [agent and customer inspecting car with bonnet open / both seated in cabin reviewing a tablet checklist / agent standing with customer at a doorstep beside the car].
Framing: mid-shot, two-shot at eye level. Documentary, candid — NOT posed studio.
People: ordinary, relatable South Asians — not models. Agent guides; customer looks reassured and engaged.
Lighting: natural outdoor daylight or bright showroom interior. Clean, true colour. Royal-blue uniform pops against neutral surroundings.
Grade: true-to-life, slightly warm. Service feels transparent and hands-on (open bonnets, tablets, paperwork).
Mood: warm, professional, approachable. "We've got you covered."
Clean photographic cutout with a visible white accent outline, composited over brand canvas. Positioned right / bottom-right, fully contained inside the canvas.
No text, no logos.
```

**Photo / photorealistic — Layer 3: Brand Lifestyle:**
```
Subject: Cars24 brand lifestyle photography style. [South Asian family arriving at destination with luggage / woman in passenger seat, sipping coffee, smiling / children leaning joyfully out a rear window / couple in front seats with a dog between them / confident woman driving alone, calm and self-assured].
Framing: intimate, editorial. PREFER interior/cabin POV — looking out windows, from back seat, across front seats. Also exterior moments at open tailgates. Subjects mid-action, candid, never posed.
Lighting: warm, golden, backlit. Sun flare through glass. Warm alive skin tones. Grade is warm and lifestyle-editorial, never clinical.
Mood: joyful, free, warm, human. A specific moment of connection — not generic stock.
No Cars24 agent present. No overt brand markings.
Clean photographic cutout with a visible white accent outline, composited over brand canvas. Positioned right / bottom-right, fully contained inside the canvas.
No text, no logos.
```

**Photo / photorealistic — Layer 4: Hubs & Infrastructure:**
```
Subject: Cars24 hub and infrastructure photography style.
Scene: [Cars24 showroom exterior — distinctive royal-blue building fascia with white and green accent strip, cars displayed in forecourt / forecourt row of cars at low oblique angle showing scale and choice / professional interior consultation area — modern fit-out, screen and desk].
Lighting: clean natural daylight (exterior) or bright professional showroom lighting (interior).
Mood: at scale, established, trusted, credible. Reinforces operational strength.
[If foreground person: agent in royal-blue uniform, confident and professional.]
No text, no logos beyond brand architecture naturally in frame.
```

**Grading rule (all photo layers):** Grade to the creative theme — [DARK → deeper, moodier grade, richer shadows / LIGHT → brighter, airier grade, open highlights]. Keep the scene NATURALLY lit and real-coloured. The theme lives in the grade and the surrounding canvas — do NOT tint the photo purple/lavender to "match" the canvas background.

**No subject (text or abstract slide):**
```
Subject: none. Pattern and typography carry this slide.
For text-only slides, keep pattern atmospheric and subordinate. For abstract pattern/form slides, the Cars24 dot treatment becomes the hero: dense halftone/particle dots and bokeh falloff form one contextual semantic silhouette while lighter dots continue across the canvas as atmosphere.
```

**Abstract pattern/form — contextual dot-form hero (v2.16 default):**
```
Subject type: abstract pattern/form.
Hero: one contextual semantic silhouette made entirely from Cars24 halftone/particle dots and bokeh falloff — [car / key / face / shield / road / other metaphor only if it fits the slide].
Treatment: dense dot clusters define the hero form; lighter dots continue across the full canvas as atmospheric pattern.
Dark theme: white luminous dots with controlled glow/bokeh on bright Cars24 Brand Blue #4736FE.
Light theme: brand-blue #4736FE halftone dots at restrained 20-25% opacity outside the hero form; soft bokeh depth is allowed but little/no glow.
Do NOT create a literal illustration, real photo, icon set, UI card, dashboard, service scene, 3D platform block, process-flow connector system, or generic terrain unless terrain is explicitly the right metaphor.
```

**Infographic / icon-based — flat icon set:**
```
Subject: set of [N] flat brand icons arranged in a [row / grid]. Cars24 brand icon system style.
Icons: [list each — e.g. "magnifying glass for Inspection · price tag for Offer · bank transfer for Payment"]
Style: clean solid filled flat vector shapes, brand blue only, no stroke, no outline, no gradient.
Optical size: all icons identical visual weight, consistent padding.
Placement: icons sit on the themed brand canvas generated in the same composite — no background box of their own, no chroma-key, no separate icon export.
No text, no labels, no numbers inside the icons.
Match the flat icon proportions and colour treatment of the attached flat icon reference.
Do NOT reproduce the exact icons from the reference — generate the icons listed above.
```

**Infographic / icon-based — 3D icon set:**
```
Subject: set of [N] 3D rendered brand icons. Cars24 brand icon system style.
Icons: [list each]
Style: glossy 3D render, brand blue body, soft directional light from top-left, subtle shadow.
Optical size: all icons identical visual weight.
Placement: icons sit on the themed brand canvas generated in the same composite — no background box of their own, no chroma-key, no separate icon export.
No text, no labels inside the icons.
Match the 3D depth, gloss, and proportions of the attached 3D icon reference.
Do NOT reproduce the exact icons from the reference.
```

**Infographic / icon-based — semantic-first dimensional polish icon set:**
```
Subject: set of [N] Cars24 brand icons arranged in a [row / grid / flow].
Icons: [list each concept].
Base style: Cars24 icon system first — choose the icon metaphor that best represents the slide subject. Prefer soft dimensional polish for premium/process icons when it improves output; use 3D when object depth clarifies the subject; use flat filled when dense/process clarity is more important.
Polish: subtle fill depth, soft top-left highlight, slight shadow, rounded filled forms, and clean readable silhouettes. If glass polish makes the icon generic, unclear, or app-tile-like, fall back to 3D or flat filled.
Placement: icons sit directly on the themed Cars24 canvas or in the chosen infographic layout. Do not create separate glass UI tiles or one large glass slab.
Connectors: use thin brand-blue or white dotted/line connectors as appropriate to the theme; keep them light and subordinate to the icons.
No text, no labels inside the icons.
Do NOT use thin outline icons, plain white line art as the primary icon style, generic SaaS symbols, abstract broken symbols, glassmorphic app tiles, heavy photorealistic 3D, or text inside icons.
```

**Infographic / icon-based — full flow layout:**
```
Subject: infographic flow, [N] steps, [left-to-right / top-to-bottom].
Steps: [list each — e.g. "1: car + magnifying glass (Inspection) → 2: price tag (Offer) → 3: bank icon (Payment)"]
Icons: Cars24 brand icon system. Each icon must semantically match its step. Prefer soft dimensional polish when it improves premium/process output; use 3D for simple product/feature objects that need depth; use flat filled for dense/process clarity. If glass becomes generic or unclear, fall back to 3D or flat filled without changing the underlying Cars24 icon language.
Module: use the selected Cars24 composition/layout system. Do not create generic glass UI tiles, one large glass slab, or app-icon rows unless explicitly requested.
Connectors: thin brand-blue or white connectors between steps; dotted connectors are allowed when subtle. Keep connectors light, evenly spaced, and subordinate to the icons.
Step labels: [exact label text] — Geist Regular, small, below each icon.
Background: the themed brand canvas + pattern, rendered in the same composed generation — no chroma-key, no bounding card, no separate compositing step.
No background card, no bounding box, no environment fill.
Match icon proportions and visual weight from the attached Cars24 icon system overview reference. If using optional soft-finish inspiration, copy only the softness/highlight discipline, not the glass tile layout.
```

---

### Block 5 — Reference Instruction

Caption each attached reference **by its position** using `1_References/reference-index.json` first, then the role templates from the *Multi-Reference Protocol* below. Use the current 3-reference recipe: [1] colour swatch always + [2] one style-defining reference + [3] visible logo only if logo gate = yes. When logo = no, slot 3 can hold the next-priority scene/layout/pattern reference. Any useful reference that does not fit must be described in prompt text, not attached.

Before showing the assembled prompt, present a reference map with:
- File
- Role
- Attachability
- Copy from reference
- Ignore from reference
- Reason

```
Reference images attached — use each ONLY for its stated role:
[SUBJECT-STYLE — Image 1: ...]      ← include if an illustration/photo subject ref is attached
[LAYOUT — Image 2: ...]             ← the composition card
[PATTERN-TEXTURE — Image 3: ...]    ← include if a pattern ref is attached

Across ALL references, do NOT reproduce:
  — Any text or copy visible in a reference
  — Any logo in a reference (logo is placed per Block 1)
  — A reference's background/scene unless that reference is the LAYOUT ref
Generate the subject from Block 4 against the background and pattern from Blocks 1–2.
Final output: single flat composited image. Print-ready. No watermarks, borders, or extra whitespace.
```

Example (illustration slide, 3 refs):
```
Reference images attached — use each ONLY for its stated role:
SUBJECT-STYLE — Image 1: match ONLY its flat editorial rendering style, colour saturation, and South-Asian character treatment. IGNORE its car-interior background. Render the Block 4 subject as a clean-edged cutout-style hero directly inside the themed composite. Do NOT copy its pose.
LAYOUT — Image 2: copy ONLY its zone split, headline position/size, body placement, logo placement, subject scale, and negative-space balance. This reference contains a marble/statue placeholder: do NOT copy marble material, statue identity, sculpture texture, its words, or its pattern. For photo output, replace the placeholder with a real Cars24-style photographic subject.
PATTERN-TEXTURE — Image 3: match ONLY its white-dot density, rim glow, and bottom-edge falloff at mid scale. Ignore any colour cast.
Across ALL references, do NOT reproduce visible text, logos, or (except the LAYOUT ref) backgrounds.
Final output: single flat composited image. Print-ready. No watermarks, borders, or extra whitespace.
```

---

## Multi-Reference Protocol

Attaching several image references only helps if the model knows **what each one is for**. Un-labeled references can get averaged into mush. Label every reference by **role** and **position**, and keep the count tight.

### The three roles
| Role | Take from it | Ignore |
|---|---|---|
| 🎨 **PALETTE** | Background hue anchor only | The swatch as a visible object, hex text |
| 🟨 **SUBJECT-STYLE** | Rendering style, flat-vector line quality, colour saturation, character treatment | Its background/scene, exact pose, any text |
| 🟦 **LAYOUT** | Zone split, headline position & dominant size, body placement, logo placement, premium finish | Its subject, exact copy, its pattern |
| 🟪 **PATTERN-TEXTURE** | Dot density, glow/bokeh, depth falloff, scale, placement | Leftover colour cast / cropped edges |
| 🅰️ **LOGO-ASSET** | Exact logo proportions and approved colourway | The logo tile/background |

### Rules
1. **Cap = 3 references per call.** More than three degrades fidelity.
2. **Current attach order:** slot [1] colour swatch always → slot [2] one style-defining ref → slot [3] visible logo if logo gate = yes. If logo = no, slot [3] can hold the next-priority scene supplement, layout card, or pattern texture.
3. **Illustration slides:** the slot [2] SUBJECT-STYLE ref is **`Main_reference.png` (mandatory anchor)**. A scene supplement fits only when slot [3] is free; otherwise describe it in prompt text.
4. **Caption every attached ref by its position** in the prompt (Block 5), using the templates below. Only write captions for refs you actually attach.
5. Prefer the **clean** pattern PNGs in `Generated Patterns/` over crops (crops carry colour cast). Source files + fingerprints: `1_References/REFERENCE-ATLAS.md`.
6. **v2.0 tag check:** before attaching, check `1_References/reference-index.json`. Do not attach anything marked `rules-only`, `do-not-attach`, `unsafe-to-attach`, or `diagram-contamination`.
7. **Marble/statue guard:** if a layout reference contains a marble/statue subject, copy layout only. Never generate a marble/statue photo hero. Photo heroes must be real people, real cars, real hubs, or real service moments.

### Paste-ready captions (Block 5)
```
SUBJECT-STYLE — Image [N]: match ONLY its rendering style (flat editorial shape quality, colour saturation, South-Asian character treatment). IGNORE its background and scene. Render the subject described above as a clean-edged cutout-style hero inside the themed composite. Do NOT copy its pose or scene.
```
```
LAYOUT — Image [N]: copy ONLY its composition (text-zone vs subject-zone split, headline position and dominant size, body placement, logo placement, premium finish). Do NOT copy its subject, its words, or its pattern.
```
If the layout reference contains a marble/statue subject, append:
```
This layout reference contains a marble/statue placeholder. Copy only layout, subject scale/placement, negative space, text hierarchy, and pattern placement. Do NOT copy marble material, statue identity, or classical sculpture styling. For photo output, replace the placeholder with real Cars24-style photographic subject matter.
```
```
PATTERN-TEXTURE — Image [N]: match ONLY its dot density, glow/bokeh treatment, depth falloff, and scale. Place the pattern as described above. Ignore any colour cast or cropped edges.
```

---

## Reference Image Selection

Pass as `--image` flags, in the fixed order above. Select based on the v2.0 tag index first, then confirm details against the source maps. Full file list: `1_References/reference-index.json` (machine-readable v2.0 tags) + `1_References/REFERENCE-ATLAS.md` (layout/illustration/pattern creatives) + `1_References/REFERENCE-SKILL-MAP.md` (every Brand-Guidelines asset — which are attachable, in what role, with paste-ready captions).

**Query order:**
1. Theme and format
2. Visual style
3. Layout archetype
4. Subject/hero needs
5. Pattern family and placement
6. Typography and logo needs
7. Attachability and contamination risk

Do not use `4_exports/` as source references for this selection. Exports are output history and audit material only.

> **Before attaching ANY Brand-Guidelines page, check `REFERENCE-SKILL-MAP.md`.** Most brand-book pages are **RULES-ONLY** (spec sheets, do/don't charts, measurement diagrams, UI screenshots) — attaching them injects chart text and crossed-out examples into the output. Only the clean assets inside the system are attachable.

### Brand-Guideline reference add-ons (from REFERENCE-SKILL-MAP §3)
Within the 3-ref cap, optionally add ONE of these and paste its caption from the map:
| Need | Attach | Role |
|---|---|---|
| Photography-style slide | matching `5_Photography References/*_exemplar.png` (primary; full guide: `PHOTOGRAPHY-GENERATION-GUIDE.md`) | 📸 PHOTO-STYLE (style anchor; default output is a clean cutout hero on the themed composite unless `full-scene photo` is explicitly selected) |
| Colours drifting off-brand | `02_Color-System/03_brand-colors-digital.png` | 🎨 PALETTE |
| Brand gradient background | `02_Color-System/05_gradient-system.png` | 🎨 PALETTE (crop to swatches) |
| Tagline sign-off | `03_Typography/08_better-drives-lockup.png` | 🔤 TYPE-SPECIMEN |
| Star framing/accent | `04_Brand-Shapes-&-Motion/07_secondary-brand-shape-star-full.png` | ✦ SHAPE |
| USP/offer badge | `08_Campaign-Assets-&-USPs/03_usp-mnemonics.png` | 🏷️ USP-STAMP (one badge) |
| Finished-template look | `07_Digital-Composition-&-Templates/04_digital-assets-templates.png` | 🟦 LAYOUT |
| Luxury/Elite | `10_Luxury-&-Elite-Sub-Brand/01_luxury-elite-colors.png` | 🎨 PALETTE (no blue) |
| Logo on slide | generation context `Logo - White-on-blue.png` / `Logo - Blue-on-white.png`; render inside the generated composite, no local overlay | 🅰️ LOGO-ASSET |
| Icon/infographic | `09_Icon-System/02_icon-system-overview.png` + `03`/`04` | ⬢ STYLE-ANCHOR |

### Dark theme
| Slide layout | Reference file |
|---|---|
| Hero right + dominant headline | `1_References/2_Image References/Dark theme/Visual Images.png` |
| Text list + no hero | `1_References/2_Image References/Dark theme/Visual Images-1.png` |
| Hero right + question/hook | `1_References/2_Image References/Dark theme/Visual Images-3.png` |
| Text-only, minimal statement | `1_References/2_Image References/Dark theme/Visual Images-5.png` |
| Hero right + body paragraph | `1_References/2_Image References/Dark theme/Visual Images-6.png` |

### Light theme
| Slide layout | Reference file |
|---|---|
| Hero right + large headline | `1_References/2_Image References/Light theme/Visual Images.png` |
| Hero right + body list | `1_References/2_Image References/Light theme/Visual Images-1.png` |
| Hero right + value reveal | `1_References/2_Image References/Light theme/Visual Images-3.png` |
| Direct statement + hero | `1_References/2_Image References/Light theme/Visual Images-4.png` |

### Illustration (add alongside the composition reference)
> **Always attach `Main_reference.png` first** as the mandatory style anchor, then add the scene supplement below. Full rules: `3_Illustrations References/ILLUSTRATION-GENERATION-GUIDE.md`.

| Scene | Always attach | Also attach |
|---|---|---|
| Inside car / driver POV | `1_References/3_Illustrations References/Main_reference.png` | — |
| Woman portrait, aspirational | `Main_reference.png` | `1_References/3_Illustrations References/Frame 2147228886.png` |
| Driving / open road / arm-out-window | `Main_reference.png` | `1_References/3_Illustrations References/Frame 2147228890.png` |
| Group or family, brand panoramic | `Main_reference.png` | `1_References/3_Illustrations References/Group.png` |
| Two people, car handover | `Main_reference.png` | `1_References/3_Illustrations References/freepik__semi-closeup-waistup-illustration-of-two-women-sta__75910 1 [Vectorized].png` |
| Unclear scene (default) | `Main_reference.png` | `Frame 2147228886.png` |

### Infographic / Icon-based (choose one slot [2] style-defining reference)
| When generating | File(s) to attach |
|---|---|
| Default infographic or icon brief | `1_References/1_Brand Guidelines/09_Icon-System/02_icon-system-overview.png` |
| Flat-style icons | `1_References/1_Brand Guidelines/09_Icon-System/04_flat-icon-generator.png` only when it is the chosen style-defining ref or slot [3] is free |
| 3D-style icons | `1_References/1_Brand Guidelines/09_Icon-System/03_3d-icon-generator.png` only when it is the chosen style-defining ref or slot [3] is free |
| Soft dimensional glass sub-style | `1_References/4_Infographic Icon References/soft-dimensional-glass-icons-blue.png` |
| Same icon type created before | matching file from `1_References/4_Infographic Icon References/` as primary anchor only when it beats the default style ref |

---

## CLI Call Template

Attach refs in the current Maker order (colour swatch → style-defining ref → visible logo if needed, otherwise next-priority ref), max 3, captioned by position in Block 5.

```bash
higgsfield generate create gpt_image_2 \
  --prompt "[FULLY ASSEMBLED FIVE-BLOCK PROMPT — Block 5 captions each image by position]" \
  --image "[PATH — PALETTE: brand-blue or brand-lavender swatch]" \
  --image "[PATH — STYLE-DEFINING: Main_reference / photo exemplar / pattern PNG / icon ref]" \
  --image "[PATH — LOGO-ASSET if logo=yes, otherwise next-priority layout/pattern/scene ref]" \
  --aspect_ratio [3:4 / 1:1 / 16:9 / 9:16] \
  --quality high --resolution 2k --wait
```

Note: GPT Image 2 does not support `4:5` — use `3:4` as the closest substitute.

**For carousels and batches:** generate in approved slide/row order. Do not run slides in parallel by default; ordered generation makes drift and feedback easier to catch before it spreads across a batch.

---

## Worked Examples

Worked examples are intentionally not embedded here. The live prompt shape changes with the current `master-rules.md` version, the selected provider, and the approved reference-role map. Use the block templates above plus the current Stage 7 approval bundle instead of copying an old example.

For current examples, use recent output folders only as audit history, never as canonical reference input, and record reusable export/process notes in `4_exports/README.md`.

---

## Per-Slide Checklist

Before generating each slide, confirm:

- [ ] Slide N of total noted in Block 1
- [ ] Theme chosen per slide and layout diversity checked across the set
- [ ] Background colour lock stated with current dark/light guardrails
- [ ] Pattern: family chosen · scale set · or explicitly "none"
- [ ] Abstract pattern/form slide uses contextual dot-form hero when selected
- [ ] Layout plan stated: archetype · DT/LT ref · vertical anchor · dominant element · text zone · hero/pattern zone · reason
- [ ] Scenario identified: full layout · standalone headline · carousel per-slide decision made
- [ ] Arapey style chosen: Italic (emotive/campaign) or Regular (product/factual)
- [ ] Actual headline copy inserted — emotive word(s) identified if Scenario 2 mixed pairing
- [ ] Actual body copy inserted — or "none"
- [ ] Subject type decided: illustration · photo · abstract pattern/form · infographic/icon · none
- [ ] Subject described specifically (not generically)
- [ ] Reference map selected via `reference-index.json` first, then Atlas/Skill Map
- [ ] Attachment recipe respected: swatch + style-defining ref + visible logo if needed
- [ ] `--aspect_ratio` matches the format
- [ ] Provider/model: Codex preview uses Codex ImageGen / `image_gen`; Codex production export uses a file-producing project-local path; Higgsfield/Claude uses `gpt_image_2` unless user-specified

---

## After generation — Visual-match QA (on-demand, master-rules Stage 9)

Stage 9 QA is not a mandatory gate for every run. Use it when the user flags an output as wrong, when a new rule is being validated, or when a batch test is intentionally auditing fidelity.

When QA is invoked:
1. Open the output next to the **same theme reference creative** used to select its layout (the `Dark theme/` or `Light theme/` file from Reference Image Selection above).
2. Score it against the **Theme Fidelity Checklist** in `master-rules.md` §4 — background hue, pattern colour/glow, headline colour, body colour, clean readable text area, fully contained hero, aspect ratio, mood, and generated logo fidelity if logo=yes. Apply the format note (illustration / photo / infographic / USP).
3. If any row fails → regenerate with a corrected prompt naming the exact deviation (see master-rules Stage 9 antipatterns), then re-check. The same checklist binds photos and illustrations equally — never tint a photo to fake a match.
4. Report a one-line verdict per slide (e.g. `Slide 2 ✓ matched LT-1`) before export.
