# Cars24 Photography Generation Guide
> Context document for image generation tools. Apply this in full whenever the visual style is **Image / photography / realistic** (Stage 4 option 2). Photographs generated for Cars24 must look *inspired by* the four brand photography moodboards — same lighting, same emotional register, same subject treatment — not generic stock.
>
> **Source of truth:** the four moodboards in `1_References/1_Brand Guidelines/05_Photography-Style/` and the clean single-frame exemplars cropped from them into this folder. Style rules here are derived directly from those references.

---

## Critical Output Rule — blog-cover photos are cutout heroes by default

For Maker Agent blog covers and image-led social creatives, photography follows the same hero discipline as illustration: the photographic subject is a clean cutout on the Cars24 canvas.

- **Default: photo cutout hero.** The car/person/service/hub subject is removed from its original environment and placed directly on the Cars24 themed canvas.
- **White outline required.** Add a crisp visible white accent outline around the complete cutout silhouette. The outline must trace the full car/person/group/key object, not just a glow behind it.
- **No photo boxes.** Do not use a rectangular photo frame, embedded photo panel, cropped scene window, or full-scene background by default.
- **Full-scene photo is an explicit exception only.** Use a full-bleed/full-scene photograph only when the user or row explicitly says `full-scene photo`, `full-bleed photo`, or the brief requires real hub/showroom context for credibility.
- **Theme harmonisation:** photographs keep their **natural lighting** always. The light/dark theme shows up in the surrounding canvas and a subtle colour grade — **never** as a purple/lavender tint baked onto the photo. A dark-theme photo slide grades slightly cooler/luminous; a light-theme slide grades slightly brighter/cleaner. The car and skin tones stay true.

---

## The Four Photography Layers

Every Cars24 photo belongs to exactly one layer. Pick the layer from the brief's emotional job, then attach that layer's exemplar.

| # | Layer | Emotional register | The subject is… | Exemplar (attach first) |
|---|---|---|---|---|
| 1 | **Product — Cars First** | **Desire** | the car, alone, as hero | `product-cars-first_exemplar.png` |
| 2 | **Assisted Experience** | **Reassurance** | the service moment — agent + customer + car | `assisted-experience_exemplar.png` |
| 3 | **Brand Lifestyle** | **Joy** | the life the car enables — people in/around it | `brand-lifestyle_exemplar.png` |
| 4 | **Hubs & Infrastructure** | **Credibility** | Cars24's physical scale — blue hubs, fleets | `hubs-infrastructure_exemplar.png` |

> All exemplars live in `1_References/5_Photography References/`. Each is one clean frame cropped from its moodboard — attach it as the primary 📸 PHOTO-STYLE reference. The full moodboard (`05_Photography-Style/0{2-5}_*.png`) may ride along for broader mood within the 3-ref cap; if you attach it, caption it "take only the lighting/mood, ignore the grid and labels."

---

## Universal Photography Style Rules

Derived from every frame across the four moodboards.

| Attribute | Rule |
|---|---|
| Lighting | Natural light or golden hour. Warm, dimensional, directional. **Never** overlit white-studio or flat fluorescent. |
| People | Diverse, relatable, real — not models. Specific genuine moments (a real smile, a glance, a hand on the wheel), never staged forced poses. |
| Car treatment | Full car in frame for Product; cabin / interior POV or car-as-context for Lifestyle; agent-with-car for Assisted; fleet/forecourt for Hubs. |
| Backgrounds | Aspirational real-world — suburban villas, scenic roads, urban architecture, branded hubs. **Never** plain white sweep or empty studio. |
| Colour grade | Warm, natural, slightly elevated. Brand blue appears in the world (a blue car, hub facades), not as a filter. |
| Composition | The car or human moment is the clear cutout hero on the Cars24 canvas. Clean, uncluttered, premium. Leave a calm zone for text. |
| Cutout treatment | Crisp photographic cutout with a visible white accent outline around the full silhouette; no rectangular frame or embedded panel. |
| Finish | Sharp, high-resolution, editorial. Cars gleam; surfaces read as real. |

**Antipatterns (reject these):** generic stock imagery · people ignoring the car · overlit interiors · forced/cheesy smiles · plain white backgrounds · a purple/lavender tint baked onto the photo · the car as an afterthought · missing white outline · rectangular photo frame · embedded photo panel · full-scene photo unless explicitly requested.

---

## Layer-by-Layer Spec & Prompts

> Prompt hygiene: `no text, no logos, no watermarks` on every photo prompt (text and logo are added in the design layer; for hub signage see the logo note below). Use colour/mood words, not hex codes.

### 1 — Product (Cars First) · *Desire*
**Look (from the exemplar):** a single clean vehicle as undisputed hero, 3/4 front angle, glossy paint, golden-hour light, an aspirational real-world backdrop (modern villa, scenic road, architecture). No people. The car gleams and looks desirable.
```
Cars24 product photography, [CAR — make/type/colour], clean 3/4 front exterior angle, glossy paintwork, golden-hour natural light, aspirational real-world backdrop [modern villa driveway / scenic coastal road / urban architecture], sharp editorial finish, the car is the sole hero and gleams, shallow depth of field. No people, no text, no logos.
For blog-cover output, render the car as a clean photographic cutout removed from its environment, placed directly on the Cars24 themed canvas, with a crisp visible white accent outline around the full car silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

### 2 — Assisted Experience · *Reassurance*
**Look:** a Cars24 agent in the branded blue/purple polo helping a South Asian customer around a car — inspection at an open hood, a doorstep handover, reviewing paperwork. Natural daylight, candid documentary feel. **The customer's confidence is the emotional centre; the agent supports but never dominates.**
```
Cars24 assisted-experience photography, a Cars24 agent in a branded blue polo shirt and a South Asian customer together at a car during [inspection at the open hood / doorstep handover / paperwork review], natural daylight, warm and professional, candid documentary moment, the customer looks confident and reassured, the agent is helpful but not dominant. Real relatable people, not models. No text, no logos.
For blog-cover output, render the agent/customer/car moment as a clean photographic cutout removed from its environment, placed directly on the Cars24 themed canvas, with a crisp visible white accent outline around the complete silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

### 3 — Brand Lifestyle · *Joy*
**Look:** the car enabling life — a woman smiling at the wheel, a family loading the boot for a road trip, an arm out the window, a dog, friends with the tailgate up. Sun-drenched warm light, genuine joyful candid moments. The brand never competes with the human story.
```
Cars24 brand-lifestyle photography, [SCENE — woman smiling at the wheel of her car / family loading luggage into the boot for a road trip / friends with windows down on an open road / arm out the window in golden light], warm sun-drenched natural light, genuine joyful candid moment, specific human story, real relatable people not models, the car enables the moment. No text, no logos.
For blog-cover output, render the lifestyle subject as a clean photographic cutout removed from its environment, placed directly on the Cars24 themed canvas, with a crisp visible white accent outline around the complete silhouette. No rectangular photo frame, no embedded photo panel, no full-scene background unless explicitly requested.
```

### 4 — Hubs & Infrastructure · *Credibility*
**Look:** a Cars24 hub — vivid brand-blue facade with the green-stripe trim and Cars24 signage, a fleet of cars in the forecourt or a bright showroom interior, crisp daylight. Conveys operational scale and reliability. The blue buildings function as brand OOH.
```
Cars24 hub photography, a vivid brand-blue Cars24 retail hub with green-stripe trim and Cars24 signage, [a fleet of cars in the forecourt / a bright showroom interior with a single SUV / a large inspection facility], crisp clean daylight, professional and at scale, conveys credibility and operational strength. No text. [See logo note for the on-building Cars24 signage.]
For blog-cover output, default to a cutout of the key hub/fleet subject placed directly on the Cars24 themed canvas with a crisp visible white accent outline. Use a full-scene hub/showroom photo only when explicitly requested or when the real environment is essential to credibility.
```

---

## Logo note for Hub photography

Hub shots inherently show **Cars24 signage on the building** — but image models hallucinate the wordmark. Two options, never let the model freehand it:
1. Generate the hub **without** legible signage (blue facade + green trim only), then post-composite the real logo onto the building at the design stage; **or**
2. Attach the correct logo PNG (`Logo - White.png` for the blue facade) as a reference and instruct: "reproduce the Cars24 wordmark faithfully from the attached logo on the building fascia — do not approximate it."

Same rule as everywhere: never ask Higgsfield to invent the logo. (See `master-rules.md` Logo rule + memory `feedback_logo_higgsfield`.)

---

## Reference Selection

| Brief is about… | Attach as 📸 PHOTO-STYLE (primary) | Optional 2nd ref |
|---|---|---|
| A car, desirability, "look at this car" | `product-cars-first_exemplar.png` | source moodboard `05_.../02_*` |
| Inspection, doorstep, agent, "we handle it" | `assisted-experience_exemplar.png` | `05_.../03_*` |
| Family, freedom, road trip, "the life it enables" | `brand-lifestyle_exemplar.png` | `05_.../04_*` |
| Scale, hubs, showrooms, "we're real and big" | `hubs-infrastructure_exemplar.png` | `05_.../05_*` |

Attach order follows the Multi-Reference Protocol: SUBJECT/PHOTO-STYLE → LAYOUT → PATTERN. For default photo-cutout blog covers, preserve the mood/lighting from the PHOTO-STYLE exemplar but instruct the generator to remove the subject from its environment, add the white outline, and place it on the Cars24 canvas. Full-scene photo references are used as full-scene outputs only when explicitly selected.

---

## What to Avoid

| Avoid | Reason |
|---|---|
| Missing cutout / white outline | Default photo-led covers require a clean photographic cutout with a visible white accent outline |
| Rectangular photo frame / embedded panel | Photo heroes merge onto the Cars24 canvas; they do not sit inside a box |
| Full-scene photo by default | Full-scene photography is an explicit exception only |
| Plain white / studio sweep background | Off-brand — Cars24 photography is real-world aspirational |
| Overlit, flat, fluorescent lighting | Brand light is natural / golden-hour, warm and dimensional |
| Model-perfect forced smiles | Reads as stock; aim for genuine candid moments |
| People ignoring the car | The car must be part of the story |
| Purple/lavender tint baked onto the photo | Theme lives in the canvas + grade, never as a filter on the image |
| Letting the model render Cars24 signage/logo | Models hallucinate the wordmark — post-composite or attach the logo PNG |
| Generic "happy family with car" with no specificity | Specify the moment — a real action, a real place |

---

*Last updated: 2026-06-18 | Source: `1_References/1_Brand Guidelines/05_Photography-Style/` (4 moodboards) + cropped exemplars in this folder | Pairs with `REFERENCE-SKILL-MAP.md` and `master-rules.md §9 Photography Generation Rules`*
