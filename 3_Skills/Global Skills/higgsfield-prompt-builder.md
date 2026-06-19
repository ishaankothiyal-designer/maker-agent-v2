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
> Every slide gets its own fully assembled prompt and reference bundle. Generate carousels sequentially in slide order.

---

## Step 0 — Pre-generation questions (ask in order, stop early if answers are obvious from the brief)

After copy is confirmed final:

1. **How many slides?** (1 = single post · 2–10 = carousel)
2. **Format?** Instagram portrait 4:5 · Instagram square 1:1 · LinkedIn 1.91:1 · X 16:9 · blog 16:9
3. **Theme?** Dark (`#4736FE` brand-blue field) or light (`#EBE9FF`-family pale brand-blue lavender) — infer from brief if clear (campaign/editorial → dark · everyday social → light)
4. **Subject type per slide?** Illustration · photo/realistic · abstract/text-only — can vary slide to slide

For carousels: confirm that the same theme runs across all slides unless the user specifies otherwise. Vary only the pattern scale, subject, and copy per slide — keep background and typography treatment consistent across the set.

---

## Model Selection

**Provider default**
- **Codex:** call Codex ImageGen / `image_gen` by default.
- **Claude / non-Codex / CLI:** use Higgsfield + GPT Image 2 (`gpt_image_2`) after authentication succeeds.
- Use Higgsfield in Codex only when the user explicitly requests it, Codex ImageGen is unavailable/unsuitable, or comparison/fallback is needed.

The assembled five-block prompt is identical regardless of which generator is used. Only the call mechanism changes.

**Higgsfield preflight and model selection:**
1. Run `higgsfield account status` before cost preview or generation.
2. If authentication fails, stop and ask the user to run `higgsfield auth login`.
3. Use `gpt_image_2` by default for every Higgsfield image route.
4. Use another supported model only when the user explicitly names it; the same approved handoff bundle still applies.

**Codex ImageGen:**
- Use the built-in Codex ImageGen / `image_gen` tool
- Pass the same fully assembled five-block prompt as the generation input
- Attach the approved reference images where the tool supports local image inputs. Otherwise include each reference's role, source path, copy-from traits, and ignore-from traits in the prompt; do not claim a file was attached when it was not.
- Same reference image selection logic applies

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

### Required handoff bundle

Before generation, package each slide as one provider-neutral handoff:

1. **Slide contract:** frozen copy, requested size/ratio, theme, style, layout archetype, vertical anchor, dominant element, logo requirement, and visual noun budget.
2. **Reference map:** ordered rows containing file path, role, attachability, copy-from traits, ignore-from traits, provider transport, and selection reason. Select from `reference-index.json` + `reference-tags/` first; use the Atlas and Skill Map to validate.
3. **Composite prompt:** the exact five-block prompt, including frozen copy verbatim and one caption for every selected reference.
4. **Provider adapter:**
   - Codex ImageGen: attach each approved reference when supported; otherwise preserve its path, role, copy-from, and ignore-from instructions in the prompt and accurately mark it as prompt-described rather than attached.
   - Higgsfield: pass every approved attachable reference as `--image` in the same order as the reference map; authenticate first and use `gpt_image_2` by default.
5. **Execution metadata:** requested ratio, provider ratio, any visible ratio mapping, model, quality/resolution, estimated Higgsfield credits when applicable, and explicit approval status.

The gate fails if a required reference is selected but absent from the provider adapter, if an attached file lacks a role caption, if a rules-only asset is attached, or if frozen copy differs from the prompt.

---

### Block 1 — Canvas, Layout & Logo

```
Cars24 brand creative. [DARK / LIGHT] theme. Slide [N] of [TOTAL].
Canvas: [FORMAT — see aspect ratios below].
Three-layer composition rendered back to front: background → pattern → subject.
Two-zone layout:
  LEFT ZONE — text only. Flat background color, no pattern, no image.
    Headline: top-left anchor. Body: below or above headline.
  RIGHT / BOTTOM-RIGHT ZONE — subject + pattern composited here.
    Subject is fully contained inside the canvas with full head, hands, car/icons, and key objects visible.
Logo placement: [layout-derived placement / none]. If logo is needed, attach/share the theme-matched visible logo PNG as actual visual input and render it from that reference inside clean negative space, about 8–10% of canvas width, with no box/tile and no later local overlay. Include the relative logo path in the prompt for traceability; path text alone is not a visual reference. Choose placement from the layout axis and cleanest negative space (left layouts align left, centre layouts align centre, right layouts may align right). In carousels with the same theme/background family, keep logo placement and size identical across all logo-bearing slides. The logo may overlap pattern; it may overlap hero only when readable, high-contrast, cleanly fitted, and fully uncropped. If the active provider/tool cannot attach the logo PNG as visual input, do not generate from text-only logo prompting; stop and ask the user to share/upload the logo so it can be used as visual input, or move to a reference-capable provider/workflow.
Note: top-left is standard for social post templates. Use bottom-left only if top-left zone is compositionally blocked.
```

**Aspect ratio reference:**
| Format | Requested ratio | GPT Image 2 ratio |
|---|---|---|
| Instagram portrait | 4:5 | `--aspect_ratio 3:4` (visible mapping required) |
| Instagram square | 1:1 | `--aspect_ratio 1:1` |
| LinkedIn banner | 16:9 | `--aspect_ratio 16:9` |
| X card | 16:9 | `--aspect_ratio 16:9` |
| Blog header | 16:9 | `--aspect_ratio 16:9` |
| Story / Reel | 9:16 | `--aspect_ratio 9:16` |

GPT Image 2 supports `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `3:2`, and `2:3`. Map `4:5` → `3:4`, `1.91:1` → `16:9`, `2:1` → `16:9`, and custom sizes → nearest supported ratio. Show requested and provider ratios in the Stage 7 handoff before approval; never silently change them.

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
Increase pattern to large or full-frame scale.
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

**Infographic / icon-based — controlled dimensional polish icon set (optional, not default):**
```
Subject: set of [N] Cars24 brand icons arranged in a [row / grid / flow].
Icons: [list each concept].
Base style: Cars24 icon system first — use 3D icon style for premium marketing/feature callouts, or flat filled icon style for dense/process/UI flows.
Polish: if the icon layer feels too flat, add controlled dimensional polish only: subtle fill depth, soft top-left highlight, slight shadow, rounded filled forms, and clean readable silhouettes.
Placement: icons sit directly on the themed Cars24 canvas or in the chosen infographic layout. Do not create separate glass UI tiles or one large glass slab.
Connectors: use thin brand-blue or white dotted/line connectors as appropriate to the theme; keep them light and subordinate to the icons.
No text, no labels inside the icons.
Do NOT use thin outline icons, plain white line art as the primary icon style, generic SaaS symbols, abstract broken symbols, glassmorphic app tiles, heavy photorealistic 3D, or text inside icons.
```

**Infographic / icon-based — full flow layout:**
```
Subject: infographic flow, [N] steps, [left-to-right / top-to-bottom].
Steps: [list each — e.g. "1: car + magnifying glass (Inspection) → 2: price tag (Offer) → 3: bank icon (Payment)"]
Icons: Cars24 brand icon system. Use 3D icon style for premium marketing/feature callouts; use flat filled icon style for dense/process/UI flows. If the flow feels too flat, apply controlled dimensional polish without changing the underlying Cars24 icon language.
Module: use the selected Cars24 composition/layout system. Do not create generic glass UI tiles, one large glass slab, or app-icon rows unless explicitly requested.
Connectors: thin brand-blue or white connectors between steps; dotted connectors are allowed when subtle. Keep connectors light, evenly spaced, and subordinate to the icons.
Step labels: [exact label text] — Geist Regular, small, below each icon.
Background: the themed brand canvas + pattern, rendered in the same composed generation — no chroma-key, no bounding card, no separate compositing step.
No background card, no bounding box, no environment fill.
Match icon proportions and visual weight from the attached Cars24 icon system overview reference. If using optional soft-finish inspiration, copy only the softness/highlight discipline, not the glass tile layout.
```

---

### Block 5 — Reference Instruction

Caption each attached reference **by its position** using `1_References/reference-index.json` first, then the role templates from the *Multi-Reference Protocol* below. Attach in the fixed order (SUBJECT-STYLE / PHOTO-STYLE → LAYOUT → PATTERN-TEXTURE, with logo/palette add-ons only when the cap allows) and write only the captions for refs you actually attached.

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
SUBJECT-STYLE — Image 1: match ONLY its flat bold vector style, colour saturation, and South-Asian character treatment. IGNORE its car-interior background. Render the Block 4 subject as a clean cutout on transparent background. Do NOT copy its pose.
LAYOUT — Image 2: copy ONLY its zone split, headline position/size, body placement, logo placement, subject scale, and negative-space balance. This reference contains a marble/statue placeholder: do NOT copy marble material, statue identity, sculpture texture, its words, or its pattern. For photo output, replace the placeholder with a real Cars24-style photographic subject.
PATTERN-TEXTURE — Image 3: match ONLY its white-dot density, rim glow, and bottom-edge falloff at mid scale. Ignore any colour cast.
Across ALL references, do NOT reproduce visible text, logos, or (except the LAYOUT ref) backgrounds.
Final output: single flat composited image. Print-ready. No watermarks, borders, or extra whitespace.
```

---

## Multi-Reference Protocol

Attaching several image references only helps if the model knows **what each one is for**. Unlabelled references can be blended into an incoherent average. Label every reference by **role** and **position**, and keep the count tight.

### The three roles
| Role | Take from it | Ignore |
|---|---|---|
| 🟨 **SUBJECT-STYLE** | Rendering style, flat-vector line quality, colour saturation, character treatment | Its background/scene, exact pose, any text |
| 🟦 **LAYOUT** | Zone split, headline position & dominant size, body placement, logo placement, premium finish | Its subject, exact copy, its pattern |
| 🟪 **PATTERN-TEXTURE** | Dot density, glow/bokeh, depth falloff, scale, placement | Leftover colour cast / cropped edges |

### Rules
1. **Cap = 3 references per call.** More than three degrades fidelity.
2. **Fixed attach order** so positions are predictable:
   `--image` 1 = SUBJECT-STYLE (if any) → 2 = LAYOUT → 3 = PATTERN-TEXTURE (if any).
3. **Illustration slides:** the SUBJECT-STYLE slot is **`Main_reference.png` (mandatory anchor)**; add a scene supplement only if it fits within the cap (anchor still counts as the one subject ref — don't exceed 3 total).
4. **Caption every attached ref by its position** in the prompt (Block 5), using the templates below. Only write captions for refs you actually attach.
5. Prefer the **clean** pattern PNGs in `Generated Patterns/` over crops (crops carry colour cast). Source files + fingerprints: `1_References/REFERENCE-ATLAS.md`.
6. **v2.0 tag check:** before attaching, check `1_References/reference-index.json`. Do not attach anything marked `rules-only`, `do-not-attach`, `unsafe-to-attach`, or `diagram-contamination`.
7. **Marble/statue guard:** if a layout reference contains a marble/statue subject, copy layout only. Never generate a marble/statue photo hero. Photo heroes must be real people, real cars, real hubs, or real service moments.

### Paste-ready captions (Block 5)
```
SUBJECT-STYLE — Image [N]: match ONLY its rendering style (flat bold vector line quality, colour saturation, South-Asian character treatment). IGNORE its background and scene. Render the subject described above as a clean cutout on a transparent background. Do NOT copy its pose or scene.
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
| Photography-style slide | matching `5_Photography References/*_exemplar.png` (primary; full guide: `PHOTOGRAPHY-GENERATION-GUIDE.md`) | 📸 PHOTO-STYLE (clean single frame; full-scene output, not a cutout) |
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

### Infographic / Icon-based (always attach all three icon system references + any matching prior icon)
| When generating | File(s) to attach |
|---|---|
| Any infographic or icon brief | `1_References/1_Brand Guidelines/09_Icon-System/02_icon-system-overview.png` |
| Flat-style icons | + `1_References/1_Brand Guidelines/09_Icon-System/04_flat-icon-generator.png` |
| 3D-style icons | + `1_References/1_Brand Guidelines/09_Icon-System/03_3d-icon-generator.png` |
| Same icon type created before | + matching file from `1_References/4_Infographic Icon References/` as primary anchor |

---

## CLI Call Template

Attach refs in the fixed Multi-Reference Protocol order (SUBJECT-STYLE → LAYOUT → PATTERN-TEXTURE), max 3, captioned by position in Block 5.

```bash
higgsfield account status

higgsfield generate create gpt_image_2 \
  --prompt "[FULLY ASSEMBLED FIVE-BLOCK PROMPT — Block 5 captions each image by position]" \
  --image "[PATH — SUBJECT-STYLE: Main_reference.png (illustration) — omit for photo/text slides]" \
  --image "[PATH — LAYOUT: matching DT-/LT- card from REFERENCE-ATLAS]" \
  --image "[PATH — PATTERN-TEXTURE: clean PNG from Generated Patterns/ — omit if no pattern]" \
  --aspect_ratio [3:4 / 1:1 / 16:9 / 9:16] \
  --quality high --resolution 2k \
  --wait
```

If `higgsfield account status` fails, do not continue. Ask the user to run `higgsfield auth login`. GPT Image 2 does not support `4:5`; expose the `4:5` → `3:4` mapping in the approval handoff.

**For carousels — run sequentially in slide order:**
```bash
higgsfield generate create gpt_image_2 --prompt "[SLIDE 1 PROMPT]" --image "[ref]" --aspect_ratio 3:4 --quality high --resolution 2k --wait
higgsfield generate create gpt_image_2 --prompt "[SLIDE 2 PROMPT]" --image "[ref]" --aspect_ratio 3:4 --quality high --resolution 2k --wait
# Continue one approved slide at a time.
```

---

## Worked Example — 2-Slide Dark Theme Carousel

**Scenario:** Instagram portrait carousel. India. "Sell your car in 30 minutes."
- Slide 1: Hero illustration + headline hook
- Slide 2: Text-only outcome list

---

**Slide 1 prompt (hero + wave field, mid scale):**

```
Cars24 brand creative. Dark theme. Slide 1 of 2.
Canvas: 1080×1350, 4:5 portrait.
Three-layer composition rendered back to front: background → pattern → subject.
Two-zone layout:
  LEFT ZONE — text only. Flat brand blue. No pattern intrusion.
    Headline top-left. Body below.
  RIGHT / BOTTOM-RIGHT ZONE — subject + pattern composited.
    Subject fully contained inside the canvas.
Logo zone: reserve top-left, 260px wide, clear space maintained; final logo is overlaid from the original PNG.

Background: Cars24 brand-blue single-hue field, full bleed, with only faint same-hue glow. Keep the dominant field vivid electric brand blue; do not drift to navy, indigo, dark violet, or a heavily darkened gradient. No multi-colour gradient.

Pattern: wave field positioned at bottom edge.
Rolling terrain of tiny luminous white dots rising from the bottom third, fading upward.
Fine point mesh, dense at base, sparse upward. Soft rim glow along wave crests.
Scale: mid. Pattern flows as background atmosphere but keeps the text area readable.
Pattern color: white luminous dots, soft glow.

Typography — dark theme:
Headline (top-left, white):
  Arapey Italic: "30 minutes"
  Arapey Regular: "Sell your car in" and the full stop.
  Size: very large, ~50% of canvas height.
Headline text: "Sell your car in 30 minutes."
Body copy (white, Geist Regular, small):
Body text: "Inspection. Offer. Payment. Done at your doorstep."

Subject: bold flat editorial vector illustration.
Confident South Asian woman, yellow jacket, standing beside an open-door orange car, arm resting on the roof, relaxed smile, sunglasses.
Warm skin tones, expressive, not stock-photo.
Brand blue car interior, orange car body.
Clean cutout, transparent background, composited over background and pattern.
Positioned right side, fully contained inside the canvas with full head, hands, car, and key objects visible.
Match the flat vector quality and colour saturation of the attached illustration reference. Do NOT reproduce the scene from the reference.

Reference images attached — use each ONLY for its stated role:
SUBJECT-STYLE — Image 1: match ONLY the flat bold vector style, colour saturation, and South-Asian character treatment. IGNORE its background. Render the Block 4 woman-and-car as a clean cutout on transparent background. Do NOT copy its pose.
LAYOUT — Image 2: copy ONLY its zone split, headline position/size, body placement, and logo placement. Do NOT copy its statue subject, its words, or its pattern.
PATTERN-TEXTURE — Image 3: match ONLY its white-dot density, rim glow, and bottom-edge falloff at mid scale. Ignore any colour cast.
Across ALL references, do NOT reproduce visible text, logos, or (except the LAYOUT ref) backgrounds.
Final output: single flat composited image. No watermarks, borders, or extra whitespace.
```

**CLI:** (fixed order — SUBJECT-STYLE → LAYOUT → PATTERN-TEXTURE)
```bash
higgsfield generate create gpt_image_2 \
  --prompt "[Slide 1 prompt above]" \
  --image "1_References/3_Illustrations References/Main_reference.png" \
  --image "1_References/2_Image References/Dark theme/Visual Images.png" \
  --image "1_References/2_Image References/Generated Patterns/dark-wave-field-mid.png" \
  --aspect_ratio 3:4 --quality high --resolution 2k --wait
```

---

**Slide 2 prompt (text-only, wave field large scale):**

```
Cars24 brand creative. Dark theme. Slide 2 of 2.
Canvas: 1080×1350, 4:5 portrait.
Three-layer composition: background → pattern → no subject.
Layout: text fills the full canvas. No subject.
Logo: white Cars24 logo, top-left, 260px wide.

Background: Cars24 brand-blue single-hue field, full bleed, with only faint same-hue glow. Keep the dominant field vivid electric brand blue; do not drift to navy, indigo, dark violet, or a heavily darkened gradient. No multi-colour gradient.

Pattern: wave field positioned at bottom edge.
Same dot terrain style as slide 1. Scale: large — wave occupies bottom third prominently since no subject.
Pattern color: white luminous dots, soft glow.

Typography — dark theme:
Headline (top-left, white):
  Arapey Italic: "doorstep"
  Geist Bold: all other words.
  Size: very large, ~55% canvas height.
Headline text: "Delivered to your doorstep."
Body copy (white, Geist Regular, small):
Body text: "Inspection at home. Best price guaranteed. Transfer handled end to end."

Subject: none. Pattern and typography carry this slide.

Reference images attached — use each ONLY for its stated role:
LAYOUT — Image 1: copy ONLY its zone split, headline position/size, and type hierarchy. Do NOT copy its subject, words, or pattern.
PATTERN-TEXTURE — Image 2: match ONLY its white-dot density, rim glow, and falloff — at large scale here (no subject). Ignore any colour cast.
Do NOT reproduce any visible text or logos from the references.
Final output: single flat composited image. No watermarks, borders, or extra whitespace.
```

**CLI:**
```bash
higgsfield generate create gpt_image_2 \
  --prompt "[Slide 2 prompt above]" \
  --image "1_References/2_Image References/Dark theme/Visual Images-1.png" \
  --aspect_ratio 3:4 --quality high --resolution 2k --wait
```

---

## Per-Slide Checklist

Before generating each slide, confirm:

- [ ] Slide N of total noted in Block 1
- [ ] Theme consistent with other slides in the set
- [ ] Background flat color stated
- [ ] Pattern: family chosen · scale set · or explicitly "none"
- [ ] Scenario identified: full layout (Scenario 1) · standalone headline (Scenario 2) · carousel per-slide decision made
- [ ] Arapey style chosen: Italic (emotive/campaign) or Regular (product/factual)
- [ ] Actual headline copy inserted — emotive word(s) identified if Scenario 2 mixed pairing
- [ ] Actual body copy inserted — or "none"
- [ ] Subject type decided: illustration · photo · none
- [ ] Subject described specifically (not generically)
- [ ] Composition reference selected
- [ ] Illustration reference selected (if illustration)
- [ ] Requested ratio and provider ratio are both shown; any mapping is explicit
- [ ] Provider/model: Codex uses Codex ImageGen / `image_gen`; every Higgsfield route passes authentication and uses `gpt_image_2` unless the user explicitly requested another supported model

---

## After generation — Visual-match QA (mandatory, master-rules Stage 9)

Generation is not done until each slide passes the theme-fidelity gate. **Do not export a slide that fails.**

For every generated slide:
1. Open the output next to the **same theme reference creative** used to select its layout (the `Dark theme/` or `Light theme/` file from Reference Image Selection above).
2. Score it against the **Theme Fidelity Checklist** in `master-rules.md` §4 — background hue, pattern colour/glow, headline colour, body colour, clean readable text area, fully contained hero, aspect ratio, mood, and generated logo fidelity if logo=yes. Apply the format note (illustration / photo / infographic / USP).
3. If any row fails → regenerate with a corrected prompt naming the exact deviation (see master-rules Stage 9 antipatterns), then re-check. The same checklist binds photos and illustrations equally — never tint a photo to fake a match.
4. Report a one-line verdict per slide (e.g. `Slide 2 ✓ matched LT-1`) before export.
