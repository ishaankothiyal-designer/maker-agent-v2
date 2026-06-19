---
name: reference-atlas
description: Vision-verified fingerprint of every real reference asset in the Cars24 Maker Agent library — what each image actually shows, what to draw from it, what to ignore, and which reference ROLE it plays when attached to Higgsfield. Load this before selecting --image references for any generation.
---

# Cars24 Reference Atlas

> **Ground truth.** Every entry below was written by looking at the actual pixels (vision pass, 2026-05-31), not from filenames. Where this Atlas disagrees with older docs, the Atlas wins for *what the assets contain*. `CREATIVE-DIRECTION.md` remains the source of truth for *rules*; this Atlas is the source of truth for *which file shows what*.
>
> **Purpose:** so we can attach **multiple, correctly-labeled references** to a single Higgsfield call and have them reinforce each other instead of fighting. See `higgsfield-prompt-builder.md` → *Multi-Reference Protocol*.
>
> **Companion:** this Atlas covers the `2_Image References/` + `3_Illustrations References/` creatives. For the **Brand Guidelines** library (logos, palette, type, shapes, photography, icons, USPs, luxury) — which of those are attachable, their roles/captions, and which skill pulls them — see `REFERENCE-SKILL-MAP.md`.
>
> **v2.0 tagging layer:** use `reference-index.json` and `reference-tags/` before selecting references. The Atlas describes what the files visibly contain; the tag index decides what the agent may copy, what it must ignore, and whether a file is safe to attach.
>
> **Marble/statue guard:** DT/LT layout cards that contain marble/statue subjects are layout references only. Copy their structure, scale, text hierarchy, negative space, and pattern placement. Never copy marble material, statue identity, classical sculpture texture, or statue styling into production output. Photo heroes must be real humans, real cars, real hubs, or real service moments.

---

## How to use this Atlas

1. Decide the **theme** (dark / light) and whether the slide has a **hero subject**.
2. Pick **one Layout reference** (Section A or B) that matches the slide's structure.
3. If there's an illustrated/photoreal subject, add **one Subject-style reference** (Section C).
4. If the slide needs a specific pattern, add **one Pattern-texture reference** (Section D) — prefer the *clean* Generated Patterns over the crops.
5. Attach them with the **role labels** in Section E so the model knows what each image is for.

**Hard cap: 3 references per call** (1 Layout + 1 Subject + 1 Pattern). More than three can cause image models to blend their signals into an incoherent average.

---

## Reference Roles (legend)

| Role | What the model should take from it | What it must IGNORE |
|---|---|---|
| 🟦 **LAYOUT** | Zone split, headline position & size, body placement, logo placement, overall premium finish | The specific subject, the exact copy, the exact pattern |
| 🟨 **SUBJECT-STYLE** | Rendering style, line/flat-vector quality, colour saturation, character treatment | The background/scene, the exact pose, any text |
| 🟪 **PATTERN-TEXTURE** | Dot density, glow/bokeh treatment, depth falloff, scale, placement | Any leftover colour cast or cropped edges from the source creative |

---

# Section A — Dark-Theme Layout References

**Location:** `2_Image References/Dark theme/` · **Format:** 4:5 portrait (1080×1350)
**Background (verified):** brand blue `#4736FE` field plus luminous same-hue glow where the pattern sits. Older references show a lighter periwinkle top, but current production prompts must keep the dominant field close to Cars24 brand blue — not navy, indigo, dark violet, or heavily darkened. (Event card DT-3 is the exception — near-black.)
**Headline type (verified):** **Arapey serif** — upright for structural words, *italic* on the emotive word(s). White. The "Out-of Tokens" lockup mixes Arapey ("Out-of") + Geist Bold ("Tokens"). Body = Geist Regular, white.

| ID | File | Structure | Subject | Pattern | Use as LAYOUT ref for |
|---|---|---|---|---|---|
| **DT-1** | `Visual Images.png` | "Out-of Tokens" lockup top, hero centre-lower | Marble statue in patterned streetwear blazer + hoodie + sunglasses, holding laptop, seated | White wave-field dot terrain glowing at bottom behind statue (mid) | Series cover / hero + big lockup |
| **DT-2** | `Visual Images-1.png` | Headline top-left, bullet list below, no hero | none | White wave-field dots bottom-right (micro) | Text + list, no hero |
| **DT-3** | `Visual Images-2.png` | Logo top, stacked headline, CTA pill, sponsor strip | none | none — near-black bg, perspective grid + glow rings | Event / hackathon / deadline ad (off-system, gaming energy) |
| **DT-4** | `Visual Images-3.png` | Headline top-left (4 lines), hero lower-right | Marble statue with laptop, seated | White wave-field dots bottom-left glow (mid) | Hero + question/hook |
| **DT-5** | `Visual Images-4.png` | Small body list top, large headline bottom | none | White wave-field dots bottom-right (micro) | Value list → big closing statement |
| **DT-6** | `Visual Images-5.png` | Full-bleed multi-line headline only | none | Faint white wave dots bottom-right (micro) | Pure brand statement, no hero |
| **DT-7** | `Visual Images-6.png` | Body top, headline bottom-left, hero lower-right | Female marble statue sipping coffee | White wave-field dots bottom edge (mid) | Newsletter / warm subscribe |
| **DT-8** | `Visual Images-7.png` | Centred white pill badge on pattern | none — Cars24 circle icon + "Out-of Tokens" logotype | Blue dot-sphere organic mesh w/ pink-teal iridescence (centre, large) | Logo identity / profile / stinger |
| **DT-9** | `Visual Images-8.png` | Small headline top-left, dark error card centre, hero lower-right | Marble statue in striped jacket holding phone, looking at it | White dot-wave right edge (mid) | Relatable dev-humour, with UI/error overlay slot |

---

# Section B — Light-Theme Layout References

**Location:** `2_Image References/Light theme/` · **Format:** 1:1 square (1080×1080)
**Background (verified):** pale lavender (`#EBE9FF`-range) with a soft glow + blue dot pattern — gentle, not pure-flat. (LT-7 recruitment is a blue colourway.)
**Headline type (verified):** **Geist Bold**, brand blue `#4736FE`, with the emphasis word in **Geist Bold *Italic***. Body = Geist Regular near-black `#161616`, key terms in Geist Bold. The "Out-of Tokens" lockup keeps Arapey on "Out-of" (logotype exception).

| ID | File | Structure | Subject | Pattern | Use as LAYOUT ref for |
|---|---|---|---|---|---|
| **LT-1** | `Visual Images.png` | "Out-of Tokens" lockup top-left, hero lower-right | Marble streetwear statue, lighter rendering, seated | Halftone dot bloom right + small bottom-left (mid) | Square series cover |
| **LT-2** | `Visual Images-1.png` | Headline top-left, body list left, hero lower-right | Marble statue with laptop | Blue dot-wave halo upper-right (mid) | Hero + list, square |
| **LT-3** | `Visual Images-2.png` | Headline top-left, hero right, dark error card bottom overlay | Female marble statue holding phone, frustrated | Blue dot field BOTH sides, full-width wave (NOT clean two-zone) | Drama / failure moment, full-field dots |
| **LT-4** | `Visual Images-3.png` | Headline top-left, body list left, footer, hero right | Female marble statue contemplating | Glowing purple-pink dotted **question-mark halo** behind figure (large) | Curiosity / value reveal |
| **LT-5** | `Visual Images-4.png` | Headline left, subtext, hero right | Male statue holding **green-screen** phone (chroma-key mockup), pointing at it | Faint dot halo bottom (micro) | Thought leadership + product/screen mockup slot |
| **LT-6** | `Visual Images-5.png` | Headline top-left, body mid-left, footer, hero right | Male statue thumbs-up holding folder/laptop | Faint blue dot-wave upper-right (micro) | Newsletter value, outcome-focused |
| **LT-7** | `Visual Images-6.png` | Headline left, hero right, CTA annotation bottom | Bearded statue (tee + gold key necklace + sunglasses) **pointing at viewer** | Blue colourway + bokeh dot glow | Recruitment / comment-bait engagement |

---

# Section C — Subject-Style References (Illustrations)

**Location:** `3_Illustrations References/`
> **Authoritative source for illustration generation = `3_Illustrations References/ILLUSTRATION-GENERATION-GUIDE.md`** (style, 60/30/10 palette, transparent-PNG rule, per-scene reference selection). This Atlas §C is a quick index; the guide supersedes it for generation rules.

**Style (verified):** modern sleek flat editorial vector, clean silhouette edges, 1–2 tonal steps, warm South Asian characters (caramel skin, navy-black hair). **Brand blue `#4736FE` dominant (60%); orange is a 10% car/clothing accent only — never dominant.** All five have FULL backgrounds (car interior, road, cityscape) — **none are transparent cutouts.** When used as a SUBJECT-STYLE ref, take *only* the rendering style + palette and **ignore the background**; output must be a transparent PNG cutout (or lime `#00FF00` chroma key).

> ⚠️ Two corrections: (1) The old `IMAGE-REFERENCE-MAP.md §4` listed phantom files (`Frame 2147228887/888/889`, `freepik 75904/75911/75912`) — they don't exist. (2) `freepik ...75907...` was renamed to **`Main_reference.png`** (same blue-suit driver image) and promoted to mandatory primary anchor. The five files below are the only real illustrations.

| File (exact) | Scene | Mood | Use as SUBJECT-STYLE ref for |
|---|---|---|---|
| `Main_reference.png` | **PRIMARY — always attach.** Woman in blue suit driving, adjusting sunglasses, blue car interior, city ahead | Confident, in-control | Style anchor on every illustration call; driver POV / interior |
| `Frame 2147228886.png` | Close-up woman portrait, navy hair, cream top, flat light-blue bg | Clean, aspirational | Solo female portrait / buyer persona |
| `Frame 2147228890.png` | Woman driving, arm out window waving, sunglasses, yellow top, open highway, purple mountains, motion lines | Free, joyful, road-trip | Freedom / new-car-joy / open-road |
| `Group.png` | Wide panorama, multiple vignettes — diverse Indians with cars, family, music, sunset | Celebratory, brand story | Banner / campaign opener / brand panorama |
| `freepik__semi-closeup-waistup-illustration-of-two-women-sta__75910 1 [Vectorized].png` | Two women by an open-door orange car, blue cityscape | Social, stylish | Handover / two-person / C2C-B2C |

---

# Section D — Pattern-Texture References

## D1 — Clean generated patterns (PREFER THESE as `--image`)

**Location:** `2_Image References/Generated Patterns/` — isolated patterns on a *flat* field, no leftover text/edges. Best for attaching as a PATTERN-TEXTURE ref.

| File | Family | Placement | Scale | Notes |
|---|---|---|---|---|
| `dark-wave-field-mid.png` | Wave Field | Bottom third | Mid | White dot terrain, dense base → sparse up, on flat blue. Pairs with a hero. |
| `dark-shell-halo-large.png` | Shell Halo | Bottom-right arc | Large | White luminous dot-sphere arc, bright rim + bokeh scatter, on flat blue. Energetic. |
| `dark-organic-mesh-mid.png` | Organic Mesh | Right side | Mid | Pink-magenta → white dotted flowing blob, sculptural, on flat blue. Tactile. |
| `light-wave-field-fullbleed.png` | Wave Field | Full frame, diagonal | Full | Blue dots on pale lavender, low contrast. Editorial, text-forward. |

> **Gap:** no clean PNG yet for Edge Frame, Particle Bloom, Centre Halo, or most light variants. Until generated, fall back to the crops in D2 (and tell the model to ignore their colour cast/edges).

## D2 — Pattern crops from finished creatives (fallback refs)

**Location:** `2_Image References/Patterns in creatives/References/` — cropped out of real creatives, so they carry source gradient + cropped edges. Use only when D1 has no match.

**Dark:**
| File | Family / look (verified) |
|---|---|
| `Centre pattern dark thme.png` | Centre Halo — blue/iridescent dot sphere, centred |
| `Dark theme pattern large.png` | Particle Bloom — soft white **bokeh blur** (not crisp dots) bottom-right |
| `full bleed pattern dark theme.png` | Wave Field — full-frame white dotted flowing grid |
| `large circle pattern dark theme.png` | Shell Halo — bright dotted sphere arc, bottom-centre, luminous rim |
| `large rhombus pattern dark theme.png` | Edge Frame — luminous dotted rounded-corner frame |
| `mountain pattern dark theme.png` | Wave Field (terrain) — white dotted mountain peaks bottom-right |
| `side pattern dark theme.png` | Organic Mesh — pink-magenta dotted blob, right side |

**Light:**
| File | Family / look (verified) |
|---|---|
| `Circle pattern bottom light theme.png` | Shell Halo — faint blue dotted dome, bottom-centre |
| `Full bleed pattern light theme.png` | Wave Field — blue dots diagonal, full frame |
| `full bleed light pattern.png` | Wave Field — denser blue dot grid, full frame |
| `human pattern light theme.png` | Organic Mesh — blue dotted **human face profile**, left side (AI/identity posts) |
| `Rhombus pattern in bottom.png` | Edge Frame — faint purple dotted rounded frame, bottom-right |
| `Side Pattern light theme.png` | Organic Mesh / Shell — soft purple-pink dotted blob, right side |

---

# Section E — Paste-Ready Reference Instructions (per role)

Append the matching block to the prompt, in addition to attaching the `--image`. Tell the model which attached image is which by order ("first image / second image / third image").

**🟦 LAYOUT ref:**
```
The FIRST attached image is a LAYOUT reference. Copy ONLY its composition: the text-zone vs subject-zone split, headline position and dominant size, body placement, logo placement, and premium finish. Do NOT copy its subject, its exact words, or its pattern.
```

**🟨 SUBJECT-STYLE ref:**
```
The SECOND attached image is a SUBJECT-STYLE reference. Match ONLY its rendering style: flat bold vector line quality, colour saturation, and South-Asian character treatment. IGNORE its background and scene entirely. Render the subject described above as a clean cutout on a transparent background. Do NOT reproduce the reference's pose or scene.
```

**🟪 PATTERN-TEXTURE ref:**
```
The THIRD attached image is a PATTERN-TEXTURE reference. Match ONLY its dot density, glow/bokeh treatment, depth falloff, and scale. Place the pattern as described above. Ignore any colour cast or cropped edges from the reference.
```

---

## Change log
- **2026-05-31** — Created from full vision pass. Corrected: background is a subtle gradient/glow (not flat); dark headline is Arapey serif (not "Care Sans"); removed 6 phantom illustration files; flagged illustrations as full-scene (not cutouts); confirmed §3 pattern families.
