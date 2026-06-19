# Cars24 Illustration Generation Guide
> Context document for image generation tools. Apply this in full whenever creating an illustration for any Cars24 creative.

---

## Critical Output Rule

**Every illustration is rendered as a clean cutout-style hero inside the single composed Cars24 creative.**

- The illustration subject does not carry its own scene background: no sky, cityscape, gradient box, or environmental fill unless the user explicitly asks for a full-scene illustration.
- The generator renders the subject directly onto the themed Cars24 canvas along with background, pattern, baked-in text, and any required logo.
- Do not ask for a transparent PNG, lime-green chroma-key, separate subject export, or local compositing step.
- Heroes must be fully contained inside the canvas: no cropped heads, hands, cars, icons, or key objects.
- If a reference image has a background, use it only for style/mood cues stated in the reference-role map; ignore the background unless the reference is explicitly selected as a layout reference.

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

**60/30/10 usage ratio:**
- **60% Brand Blue** `#4736FE` — car interiors, large clothing shapes, environments, dominant scene elements
- **30% Secondary** — Deep Navy `#2B2098`, Mint Green `#63FFB1`, Off-white `#F5F5F5`
- **10% Accents** — Orange `#EF4523` (cars and clothing accents ONLY), warm skin tones

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

**Orange rule:** Orange is a tertiary accent. It appears on cars and occasionally as clothing highlights. It is NEVER the dominant colour or used as an environment/background tone. `Main_reference.png` has zero orange — this is intentional.

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
Modern sleek flat editorial illustration, [SCENE DESCRIPTION], South Asian characters with warm caramel skin tones, electric brand blue dominant colour palette, clean flat colour shapes with minimal shading, no photorealistic textures, deep navy-black hair, clean crisp silhouette edges, aspirational and confident mood, no text, no numbers, no labels. Render the subject as a clean-edged cutout-style hero directly inside the themed Cars24 composite, fully contained with head, hands, car/icons, and key objects visible. The canvas background, atmospheric pattern, baked-in headline/subheading, and any required Cars24 logo are separate layers in the same generated composite. No sky, no cityscape, no environment fill, no gradient box behind the subject. Style: premium modern sleek flat editorial illustration.
```

**[SCENE DESCRIPTION] examples:**
- `confident South Asian woman driving, slight cinematic angle, inside-car POV at the wheel`
- `South Asian woman smiling, waist-up portrait, confident warm expression`
- `South Asian woman arm out of car window, joyful open-road scene`
- `two South Asian people in a celebratory car key handover moment`
- `South Asian family loading luggage into a car, warm celebratory scene`
- `South Asian man receiving car keys, excited and confident`

**When the scene includes an orange car** — add: `orange car as a secondary element`

**Prompt hygiene — always apply:**
- Use exact hex locks for the surrounding theme/canvas/text system when needed, always with "do not render the hex code as text." Use colour names inside the illustration subject block itself.
- Always include `no text, no numbers, no labels`
- Use `electric brand blue dominant` — do NOT write "electric blue and vivid orange colour palette"

---

## What to Avoid

| Avoid | Reason |
|---|---|
| Orange as dominant colour | Violates 60/30/10 — orange is 10% car/clothing accent only |
| "Vivid orange colour palette" in prompt | Produces orange-heavy output that breaks brand |
| Bold/chunky cartoon feel | Main_reference.png is the quality bar — modern and sleek |
| Subject-owned solid colour backgrounds | Breaks the single themed Cars24 canvas |
| Subject-owned gradients or environment boxes | Creates a fake panel instead of a cutout-style hero |
| Photorealistic rendering | Wrong style register |
| Drop shadows on characters | Edge artefacts when compositing |
| Western / non-South-Asian skin tones | Misrepresents India-primary market |
| Text or logos embedded in illustration | These belong in the design layer above |
| Environmental backgrounds (sky, cityscape) | Subject should sit directly on the themed Cars24 canvas unless full-scene illustration is explicitly selected |
| Referencing the 75907 file | `freepik__flat-vector-editorial-illustration-fully-illustrat__75907 1 [Vectorized]-1.png` no longer exists |

---

*Last updated: 2026-06-18 | Source: 1_References/3_Illustrations References/ | Supersedes prior transparent-PNG/chroma-key illustration delivery guidance*
