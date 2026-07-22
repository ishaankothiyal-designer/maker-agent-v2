# Cars24 Illustration Generation Guide
> Context document for image generation tools. Apply this in full whenever creating an illustration for any Cars24 creative.

---

## Critical Output Rule

**Every illustration is rendered inside the final Cars24 creative as one generated composite.**

- The final deliverable contains the themed canvas, pattern, intentionally framed illustrated hero, approved text, and optional logo together.
- Do not request transparent PNGs, chroma-key backgrounds, separate illustration exports, or post-process compositing.
- An illustration reference's environment is style/context only. The generated hero merges cleanly onto the Cars24 canvas and must not bring a rectangular scene panel or separate background. A restrained skyline, road, dealership, or local landmark silhouette may be integrated into the full canvas when it adds story depth while remaining subordinate to the hero and text.

---

## Primary Style Reference — Mandatory

**`Main_reference.png` is the primary style anchor. Always attach it to every Higgsfield generation call.**

What it establishes:
- Brand blue (`#4736FE`) as the dominant colour — car interior, jacket, environment
- Modern, sleek, premium quality — clean shapes, tight silhouettes, polished finish
- Flat vector rendering with minimal shading (1–2 tonal steps only)
- South Asian character with warm caramel skin, dark navy-black hair
- No orange — blue is the dominant

## Reference Model — Style Anchor + Context Anchors

Use this model for every illustrated output:

1. **Style anchor:** `Main_reference.png` is mandatory and controls the rendering style.
2. **Scene supplement:** add one illustration-folder supplement only when useful for the scene.
3. **Approved identity/context reference:** add any approved real person/product/tool/proper-noun reference only to preserve factual cues. It must be translated into the Cars24 illustration style.

Do not let an approved photo or screenshot become the style reference. A person photo can define identity cues such as face structure, hairline, glasses, smile, and outfit direction, but the output must still read as a modern sleek flat editorial Cars24 illustration.

Named-person example: for Gajendra Jangid, use `Main_reference.png` for style, `Frame 2147228886.png` if portrait framing is useful, and the approved Gajendra photo only for identity preservation. The result must not become photorealistic, painted-photo, oil-painted, 3D, or a generic vector portrait.

---

## Art Style

**Style name:** Modern sleek flat editorial illustration
**Visual character:** Premium, aspirational, clean — not cartoonish, not overly illustrative, not photorealistic
**Quality bar:** `Main_reference.png` — match its level of finish and colour discipline

| Attribute | Specification |
|---|---|
| Rendering | Flat vector — shapes define volume, not strokes |
| Line work | Minimal or absent; sharp silhouette edges only |
| Shading | Subtle — 1–2 tonal steps within each colour zone; no gradients or glow |
| Texture | None — all fills are clean flat colour |
| Detail level | Semi-detailed faces and hands; simplified clothing and environment |
| Perspective | Slight cinematic angle preferred; not purely frontal |
| Feel | Modern, sleek, premium — not bold/chunky/cartoon |

---

## Character Design

### Ethnicity & Representation
- Primary market: India — South Asian characters, warm skin tones
- Skin palette: Caramel (`#C68642`), warm tan (`#D4956A`), medium brown (`#A0522D`) — always use warm undertones
- Hair: Deep navy-black (`#1a1a3e` or `#0d1b3e`), rendered as bold flat shapes — never individual strands
- Facial features: Almond-shaped eyes, defined dark brows, subtle confident smile — expressive but not exaggerated
- Body type: Realistic proportions; aspirational but grounded

### Character Mood
- Confident, joyful, in-control — never passive or anxious
- Aspirational but relatable — everyday people in elevated moments

---

## Colour Palette — Brand-Accurate

**Reference files:**
- `1_References/1_Brand Guidelines/02_Color-System/03_brand-colors-digital.png` — official hex values
- `1_References/1_Brand Guidelines/02_Color-System/06_color-usage-ratio.png` — 60/30/10 ratio

**60/30/10 usage ratio for illustrated heroes:**
- **60% Brand Blue** `#4736FE` — the unmistakable dominant colour across large clothing, car, and scene-shape areas.
- **30% supporting tones** — Deep Navy `#2B2098`, near-black/Neutral 950, off-white/Neutral 100, and natural warm skin tones provide depth, contrast, and human realism without competing with the blue field.
- **10% total controlled accents** — Orange `#EF4523` and Mint `#63FFB1` are optional contextual details used to make the illustration feel more alive. Mint can signal freshness, product energy, EV/charging, cashback, completion, or campaign cues. Orange can appear on cars, clothing accents, or small emphasis details. Do not use both by default; together they must remain within the 10% allocation.

| Role | Colour | Hex |
|---|---|---|
| Primary brand (dominant) | Brand Blue | `#4736FE` |
| Depth / shadow | Deep Navy | `#2B2098` |
| Hair / dark elements | Near-black Navy | `#0D1B3E` |
| Nature / teal accents | Mint Green | `#63FFB1` |
| Highlights / off-white | Off-white | `#F5F5F5` |
| Skin base | Warm Caramel | `#C68642` |
| Skin shadow | Warm Brown | `#9B6B3A` |
| Car / clothing accent | Vivid Orange | `#EF4523` |

**Accent rule:** Use approved brand accents to enrich illustration context, not to recolour the brand system. Orange may appear on cars, clothing accents, or small emphasis details. Mint may appear as a fresh/product/energy cue, including EV charging, cashback, completion, or a campaign signal. Neither is a default, dominant colour, environment/background tone, dot pattern, logo colourway, or semantic colour-coding system. Brand Blue remains the correct dominant. Icon systems remain brand-blue monochrome under their separate, stricter rule.

---

## Reference Library

All files in `1_References/3_Illustrations References/`

| File | Role | Best for |
|---|---|---|
| `Main_reference.png` | **PRIMARY — always attach** | Style anchor, inside-car POV, brand blue dominant scene |
| `Frame 2147228886.png` | Scene supplement | Solo female portrait, bust crop, aspirational |
| `Frame 2147228890.png` | Scene supplement | Driving joy, open road, arm out window, dynamic angle |
| `Group.png` | Scene supplement | Diverse group, brand panoramic, road trip |
| `freepik__semi-closeup-waistup-illustration-of-two-women-sta__75910 1 [Vectorized].png` | Scene supplement | Two people, car handover, orange car + blue cityscape |

### Reference selection

| Scene | Always attach | Also attach |
|---|---|---|
| Solo female character | `Main_reference.png` | `Frame 2147228886.png` |
| Driving / open road | `Main_reference.png` | `Frame 2147228890.png` |
| Inside car / driver POV | `Main_reference.png` | — |
| Group or family | `Main_reference.png` | `Group.png` |
| Two people / handover | `Main_reference.png` | `freepik__semi-closeup-waistup-illustration-of-two-women-sta__75910 1 [Vectorized].png` |
| Generic / unclear | `Main_reference.png` | `Frame 2147228886.png` |

---

## Prompt Template

```
Modern sleek flat editorial illustration, [SCENE DESCRIPTION], South Asian characters with warm caramel skin tones, electric Cars24 brand blue dominant (60%), intentional supporting deep navy/off-white/near-black/natural skin tones (30%), and no more than 10% total fresh mint green and/or vivid orange contextual accents. Use the approved brand palette to add life and specificity without making the image orange- or mint-dominant. Clean flat colour shapes with 1–2 tonal steps, no photorealistic textures, deep navy-black hair, crisp silhouette edges, aspirational and confident mood. Render the hero directly into the final Cars24 branded composite; no separate panel, scene box, transparent export, or chroma-key background. Framing: [contained OR intentional editorial edge crop]. Keep faces, the focal interaction, action-carrying hands, and meaning-carrying product detail clear; permit a supporting car, shoulder, lower body, car body, clothing edge, or restrained contextual environment to continue behind a selected logo overlay when it makes the composition more stylish and preserves logo readability. Do not cut, fade, or truncate the bottom of the hero merely to reserve logo space. Style: premium modern sleek flat editorial illustration.
```

**[SCENE DESCRIPTION] examples:**
- `confident South Asian woman driving, slight cinematic angle, inside-car POV at the wheel`
- `South Asian woman smiling, waist-up portrait, confident warm expression`
- `South Asian woman arm out of car window, joyful open-road scene`
- `two South Asian people in a celebratory car key handover moment`
- `South Asian family loading luggage into a car, warm celebratory scene`
- `South Asian man receiving car keys, excited and confident`

**When the scene benefits from brand accents** — add a precise contextual cue, such as `fresh mint charging cue as a small accent`, `fresh mint cashback cue as a small accent`, `vivid orange car as a secondary element`, or `vivid orange clothing detail as a small accent`.

**Prompt hygiene — always apply:**
- No hex codes in provider prompts — use colour names only
- The wider composite prompt owns approved text and any optional logo; the illustration subject itself contains no labels or logos
- Use `electric brand blue dominant` — do NOT write "electric blue and vivid orange colour palette"
- If the selected logo overlaps the hero zone, describe it as the highest overlay layer and preserve natural hero continuity behind it instead of cropping the illustration away.

---

## What to Avoid

| Avoid | Reason |
|---|---|
| Orange as dominant colour | Violates 60/30/10 — orange is 10% car/clothing accent only |
| "Vivid orange colour palette" in prompt | Produces orange-heavy output that breaks brand |
| Bold/chunky cartoon feel | Main_reference.png is the quality bar — modern and sleek |
| Separate/boxed scene backgrounds | The hero must merge into the single final Cars24 composite; restrained contextual depth is allowed only when integrated into the canvas |
| Transparent or chroma-key output | Retired delivery workflow; never request it |
| Photorealistic rendering | Wrong style register |
| Heavy drop shadows on characters | Breaks the clean flat editorial silhouette |
| Western / non-South-Asian skin tones | Misrepresents India-primary market |
| Text or logos embedded in the illustration subject | These belong in the generated composite layer, only when approved |
| Dominant or boxed environmental background | Context must remain a restrained full-canvas layer, never a competing scene panel |
| Referencing the 75907 file | `freepik__flat-vector-editorial-illustration-fully-illustrat__75907 1 [Vectorized]-1.png` no longer exists |

---

*Last updated: 2026-05-31 | Source: 1_References/3_Illustrations References/ | Supersedes all prior illustration colour and style guidance*
