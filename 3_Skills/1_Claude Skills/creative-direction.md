---
name: creative-direction
description: Synced mirror of 1_References/CREATIVE-DIRECTION.md. Do not edit directly.
---

⚙️ **Auto-generated.** Synced mirror of `1_References/CREATIVE-DIRECTION.md` (single source of truth for creative direction). **Do not edit directly** — edit the primary and run `python3 tools/sync_skills.py`. Claude users may also use `/sync-skills` when the repo wrapper exists. Content is verbatim so brand rules are never paraphrased.

---


# Cars24 Creative Direction — Master Reference

> Source of truth: observed behaviour from reference creatives in `2_Image References/` cross-referenced with `1_Brand Guidelines/` and pattern system in `2_Image References/Patterns in creatives/`.
> Do not override this with brand guidelines alone — the creatives are the ground truth. Guidelines fill gaps.

---

## Brand Guidelines — Deep Reference (vision-verified `notes.md`)

Every brand-guideline section has a `notes.md` rewritten from the actual page images (vision-verified 2026-05-31). Open the matching one when you need exact specs, hex values, copy rules, or do/don'ts beyond what this doc summarises. Companion for the creatives/illustrations/patterns library: `1_References/REFERENCE-ATLAS.md`.

| Need | Open this `notes.md` |
|---|---|
| Logo versions, colorways, clear space, placement, misuse | `1_Brand Guidelines/01_Brand-Identity-&-Logo/notes.md` |
| **Logo files to hand Higgsfield (colorway → asset → background)** | `1_Brand Guidelines/01_Brand-Identity-&-Logo/Logos/higgsfield-logo-reference-map.md` |
| Exact hex values, gradients (Midnight Depth / Ethereal Glow), 60/30/10 ratio | `1_Brand Guidelines/02_Color-System/notes.md` |
| Type roles (Care Sans=logo · Geist=primary · Arapey=serif), weights, pairing | `1_Brand Guidelines/03_Typography/notes.md` |
| Trapezoid primary shape, 4-point star, shape usage | `1_Brand Guidelines/04_Brand-Shapes-&-Motion/notes.md` |
| Photography registers: product / service / lifestyle / hubs | `1_Brand Guidelines/05_Photography-Style/notes.md` |
| Voice, market tone (IN/UAE/AU), grammar, price formatting | `1_Brand Guidelines/06_Voice-Tone-&-Copy/notes.md` |
| Safe zones, logo specs, CTA button spec, templates | `1_Brand Guidelines/07_Digital-Composition-&-Templates/notes.md` |
| USP mnemonics/stamps (6 USPs, black + mint) | `1_Brand Guidelines/08_Campaign-Assets-&-USPs/notes.md` |
| Icon system — flat vs 3D specs (for infographics) | `1_Brand Guidelines/09_Icon-System/notes.md` |
| Luxury / Elite sub-brand palette (cream, gold, black — no blue) | `1_Brand Guidelines/10_Luxury-&-Elite-Sub-Brand/notes.md` |

> Quick topic→anchor lookups also live in `1_Brand Guidelines/INDEX.md`.

---

## The Three-Layer Composition System

Every Cars24 creative is built from exactly three layers, composited in this order:

```
┌─────────────────────────────────────┐
│  LAYER 3 — Hero image (cutout)      │  ← foreground, fully contained
│  LAYER 2 — Dot/particle pattern     │  ← atmosphere, sits under hero
│  LAYER 1 — Background color field   │  ← base field, single hue, subtle gradient/glow
└─────────────────────────────────────┘
```

**Layer 1 — Background**
A single-hue field — **not** a flat dead fill. The reference creatives use a *subtle vertical gradient/glow* in one colour family (never a multi-colour gradient):
- Dark theme: Cars24 Brand Blue `#4736FE` as the dominant full-bleed canvas, with a controlled same-hue vertical/ambient gradient for premium depth and, when useful, an optional restrained radial glow around the hero/pattern zone. "Dark" means white typography and luminous white pattern on brand blue; it does **not** mean a darkened background. It may drift slightly lighter or darker around `#4736FE`, but must still read immediately as bright Cars24 brand blue and must not drift to navy, indigo, black, midnight blue, dark violet, generic purple, or dim AI-tech dark mode.
- Light theme: exact pale lavender `#EBE9FF` tint derived from Brand Blue, with a soft same-hue glow. Lavender is intentional for light/dark distinction, but it must stay within the brand-blue family — NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out, NOT pink, NOT beige, NOT generic pastel purple. **"Light theme" means ONLY the background is pale — all foreground elements (headlines, body text, logo, icons) stay full-saturation Brand Blue `#4736FE` or near-black `#161616`.** Do not let the pale canvas drag text, logo, or icon elements into desaturated, grey-blue, or muted territory.
> Note: the *isolated* pattern PNGs in `Generated Patterns/` sit on a flat field — that is correct for an isolated asset. The *finished composite* gets the gentle gradient/glow above. Do not instruct the generator to produce a "flat, no-gradient" background — that flattens the premium look the references have.

**Layer 2 — Pattern**
The atmospheric dot/particle layer. Production output now uses a clean full-background pattern treatment: the pattern may flow across the full canvas, but it stays behind the text and hero, never as a foreground layer. The text area must remain clean and readable.

**Layer 3 — Hero image**
A cutout (no background) — a person, car, illustration, icon, or character — placed as the hero while staying fully contained inside the canvas. No edge bleed and no cropped heads, hands, cars, icons, or key objects.

**Safe framing — fully contained hero, protect everything meaningful.** Everything that carries meaning — the face, head, hands, the laptop, car, icon, or product the subject is using — stays inside the safe zone (inner ~85%) and is **never clipped at any edge or corner**. The failure mode to avoid: the generator frames the subject so large or so close that it gets sliced (top of head cut, shoulder cut, hands cut, car cropped). Fix it by composing the subject smaller with deliberate headroom and breathing room. State the framing explicitly in the prompt (e.g. "waist-up, full head and hands in frame with headroom, fully contained inside the canvas").

**Photo/image-led hero treatment.** Photo-led blog covers follow the same cutout discipline: the photographic subject is removed from its environment, placed directly on the Cars24 canvas, and given a crisp visible white accent outline around the full silhouette. Do not use a rectangular photo frame, embedded photo panel, or full-scene background unless the user explicitly selects `full-scene photo`. Natural lighting and real colour stay inside the cutout; the theme lives in the surrounding canvas, type, and pattern.

## Style Purity — one visual system per creative

Every generated creative commits to **one primary visual style**:

| Primary style | Allowed visual language | Reject by default |
|---|---|---|
| Illustration | One Cars24 modern sleek flat editorial hero, possibly with one supporting prop/car/service moment | Infographic flows, SaaS dashboards, 3D platform blocks, database icons, network maps, UI-card clusters, generic AI ecosystem visuals |
| Photo | One real photographic Cars24 cutout hero from the selected photo layer, natural light, visible white accent outline, theme via canvas/grade | Illustrated overlays, icon clusters, UI dashboards, purple/lavender tinting, generic stock staging, rectangular photo frames, full-scene photo unless explicitly selected |
| Abstract pattern/form | Contextual dot-form hero built from the Cars24 halftone/particle pattern language; one recognisable semantic silhouette is allowed (car, key, face, shield, road, etc.) when it stays abstract and metaphor-led | Literal people, rendered cars, photo scenes, UI cards, dashboards, icon clusters, process-flow icons, 3D platform blocks, generic default terrain |
| Infographic/icon | Icon system, steps, connectors, structured information hierarchy. Sub-styles: 3D (premium marketing), flat filled (dense/process), soft dimensional glass (when explicitly selected). **All icons brand-blue monochrome only** — no green, cyan, teal, or off-brand hues. | Cinematic character heroes, full service scenes, decorative illustration vignettes unless explicitly approved, polychromatic icon fills, semantic colour coding (green=approved, red=alert) |

**Visual noun budget:** one dominant hero noun plus at most one supporting noun. If a prompt contains people + car + app screen + nodes + icons + roadmap + database, it has already become generic. Reduce it to the clearest Cars24 moment before generation.

**Concrete Cars24 moment over generic AI language:** replace broad nouns like "AI workflow", "connected ecosystem", "intelligent platform", and "digital transformation" with visible, grounded scenes or one concrete abstract metaphor. Examples: "a Cars24 product team reviewing one prototype screen", "one inspection insight emerging as a shield-shaped brand-blue dot-form", "agent and customer at one car handover", or "three flat icons showing inspection → price → handover".

### Abstract Dot-Form Hero Default

When the selected style is **abstract pattern/form**, the default output is a contextual **abstract dot-form hero**. The Cars24 dot/pattern treatment is no longer just background atmosphere; it becomes the hero system itself.

- The hero is made entirely from Cars24 halftone/particle dots, point-cloud density, depth falloff, and bokeh, with no literal rendered object surface.
- The hero may form a recognisable semantic silhouette — for example a car, key, face, shield, road, document, funnel, or portal — when that silhouette supports the slide's meaning. It must remain abstract and metaphor-led, not become an illustration, photo, icon set, UI card, or infographic flow.
- Dense dots define the semantic silhouette. Lighter dots continue across the full canvas as atmosphere so the hero feels extracted from the pattern system, not pasted on top of it.
- The form must be contextual to the essay/slide content. Do not default to generic mountain terrain, a random sphere, a generic tech wave, or decorative wallpaper unless that exact metaphor is justified.
- **Dark theme:** white luminous dots on bright Cars24 Brand Blue `#4736FE`, with controlled bokeh depth, soft rim glow, and same-hue canvas depth. The canvas must not drift navy/indigo/black/dim.
- **Light theme:** brand-blue `#4736FE` halftone dots on exact pale lavender `#EBE9FF`. Soft bokeh depth is allowed inside/around the dot-form hero, but the look stays clean blue halftone with little or no glow. Outside the hero form, dots remain restrained at about 20-25% opacity.
- The text zone remains clean and readable. If the dot-form crosses behind text, reduce density and contrast there so the copy leads.
- Abstract style rejects literal people, rendered cars, real photo scenes, service scenes, UI dashboards, app cards, icon clusters, process-flow connectors, 3D platform blocks, and semantic colour coding.
- Visual noun budget: one semantic dot-form silhouette plus at most one supporting atmospheric motif.

Before approval, every prompt should pass this audit:

```
Primary style: [illustration / photo / abstract pattern-form / infographic-icon]
Secondary style allowed: [none / narrowly named exception]
Visual noun budget: [hero noun] + [support noun or none]
Rejected elements: [style contaminants removed]
Specific Cars24 moment: [one concrete moment or visual metaphor]
```

### Illustration Reference Model — Style Anchor + Context Anchors

Every illustrated hero must use the project illustration folder as its style source:

`1_References/3_Illustrations References/`

The model is:

1. **Mandatory style anchor:** `Main_reference.png` controls the illustration language — modern sleek flat editorial, clean vector-like shapes, minimal shading, crisp silhouette edges, warm South Asian skin tones, deep navy-black hair, and disciplined Cars24 brand-blue usage.
2. **Scene supplement:** choose one additional file from the same folder only when it helps the scene: `Frame 2147228886.png` for portrait/bust framing, `Frame 2147228890.png` for driving/road motion, `Group.png` for group scenes, or the `...75910...` two-women vectorized file for service/handover moments.
3. **Approved identity/context reference:** if the brief names a real person, product, tool, or proper noun and an approved reference photo/screenshot exists, use that reference only for factual identity/context cues. It does not replace `Main_reference.png` and must not change the output into photo, painted-photo, 3D render, or generic vector art.

For named-person illustration, preserve approved identity cues — face structure, hairline, glasses, expression, outfit direction — while translating the person into the Cars24 illustration style. The hero should clearly read as an illustration guided by the illustration folder, not as a photorealistic portrait.

Example: for Gajendra Jangid, use `Main_reference.png` as the style anchor, `Frame 2147228886.png` if portrait framing support is useful, and the approved Gajendra photo only for identity cues.

---

## The Layout System — a family of varied archetypes

**There is no single fixed layout.** The reference cards in `2_Image References/{Dark|Light} theme/` use a *family* of recurring structures, and the variety between them is intentional — that variety is what "better balance" means here. Pick the archetype that fits the slide's job; across a multi-slide set, **rotate archetypes and vertical anchors** so consecutive slides never repeat the same structure. The file-level map of which reference shows which structure is the **Reference Atlas** (`REFERENCE-ATLAS.md`, Sections A & B — IDs DT-1…DT-9 / LT-1…LT-7); attach the closest match as the 🟦 LAYOUT reference on the Higgsfield call.

**Mandatory layout plan before prompt assembly.** Every slide needs a visible layout plan before the final image prompt is written:

```
Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason
```

This is the selection mechanism, not optional rationale. If the plan repeats the same archetype or vertical anchor, the agent must say why. If there is no strong reason, revise the layout plan before prompting.

**Carousel and batch diversity guard.** No more than two consecutive slides may use the same archetype or the same top-left text / right-hero anchor unless the user explicitly asks for a consistent repeated system. Batch visual territories must include layout territory as well as visual style, e.g. `illustration + cover-lockup`, `photo + stacked-left`, `abstract + headline-dominant`, not only `illustration`, `photo`, or `abstract`.

### The archetypes (read off the references)

| # | Archetype | Structure | Use it for | Reference examples |
|---|---|---|---|---|
| 1 | **Cover / Lockup** | Big title or the "Out-of Tokens" lockup at top (or centred); hero centred-lower, or a centred logo pill. Pattern halo/wave behind. Symmetric. | Series cover, identity, opener | DT-1, DT-8, LT-1 |
| 2 | **Headline-left + Hero-right** | Headline fills the upper-left; hero sits fully contained on the right / lower-right. | Hook, statement-with-face | DT-4, LT-2, LT-5, LT-7 |
| 3 | **Stacked-left column + Hero-right** | Vertical text column on the left — kicker/body on top, large headline anchored low (or reversed) — hero on the right. | Newsletter, value → outcome | DT-7, LT-4, LT-6 |
| 4 | **Text-only** | No hero. Headline + body list; headline anchors TOP (list below) or BOTTOM (list above). Pattern carries the weight (bottom wave / full-bleed / corner). | List, value stack, relatable copy | DT-2, DT-5 |
| 5 | **Headline-dominant** | Headline fills nearly the whole canvas (4–6 lines); no hero; faint corner pattern only. | Pure brand statement | DT-6 |
| 6 | **Content-card overlay** | A UI element (error card, chat, product/screen mockup) as a mid-layer between headline and hero. | Dev-humour, product demo, failure moment | DT-9, LT-3, LT-5 |
| 7 | **Announcement / Event poster** | Off-system energy: logo top-centre, centred stacked headline, CTA pill, sponsor/footer strip; often near-black + neon. Symmetric. | Hackathon, deadline, event ad | DT-3 |

> The classic two-zone split (clean **text zone** on the left, **hero + pattern zone** on the right) is archetypes 2–3 — the most common, not the only one. Wherever a text zone exists, it stays clean: no pattern intrusion, maximum legibility.

### Balance principles — true for every archetype

This is *how* the references stay balanced. Apply all of them whichever archetype you pick:

1. **One dominant element.** The headline *or* the hero leads — never both at equal weight. With a hero (visually heavy on the right), the headline is the largest type mass on the left and counterbalances it. With no hero, the headline grows to fill the weight (archetype 5) or the pattern scales up to fill it (archetype 4). The headline still takes ~40–60% of canvas height when it leads.
2. **Commit to ONE vertical anchor** per slide — headline top, bottom, centred, or full-canvas — and hang everything else off it. Elements floating at arbitrary heights is the main cause of lopsided output. Carousel variety comes from *alternating* the anchor slide-to-slide, not from randomness.
3. **Text is left-set and left-aligned**, ragged-right — except Cover/Lockup and Event, which centre. Never justified.
4. **Generous negative space.** Text fills roughly half its zone; the quiet area is intentional framing, not space to fill. The references breathe — keep them breathing.
5. **Consistent outer margin (~6–8% inset)** for all text and the logo. The hero stays fully contained with the face/hands/key object inside the safe zone.
6. **Three-tier text rhythm** when copy is rich: eyebrow/kicker (small Geist) → headline (large Arapey×Geist mix) → body or CTA (small Geist), each tier separated by clear size and space. Bold keywords inline; a hand-drawn underline/arrow may spotlight a CTA (see LT-7).
7. **Pattern always recedes** behind both headline and hero (see Pattern Scale Rule below).

### Logo Placement And Visual-Input Rule

When a generated creative includes the Cars24 logo, the same theme-matched visible logo PNG must be attached/shared as actual visual input, and the final prompt must include an explicit current-logo description. Describe the logo as the current Cars24 horizontal lockup: rounded-square icon, circular cut-through/open-`C` mark, plus the `Cars24` wordmark. Explicitly reject the old boxed `CARS24` logo, all-caps lockups, plaques, badges, redraws, and tile hallucinations. A repo-relative logo path in the prompt is traceability only, never sufficient by itself.

Logo placement follows the layout axis and the cleanest negative-space zone:
- Left-aligned layouts usually use a left-aligned logo, either top-left or bottom-left depending on negative space.
- Centre/symmetric layouts use centre-aligned logo placement, either top-centre or bottom-centre depending on negative space.
- Right-aligned layouts may use right-aligned logo placement if that is the cleanest safe zone.
- In carousels with the same theme/background family, logo placement and size stay exactly consistent across all logo-bearing slides.
- The logo may overlap pattern. It may overlap the hero only when it remains readable, high-contrast, cleanly fitted, and fully uncropped.
- The logo must never touch, bleed, crop, cut off, distort, sit in a box/tile, or be approximated from text.

If the active tool/workflow cannot attach the visible logo PNG as true visual input, do not use it for logo-bearing output. If the output changes the logo geometry, drops the icon, alters the wordmark, drifts to all caps, adds a box/tile, crops the lockup, or otherwise modifies the logo, the logo QA fails even if the rest of the creative is good. After a logo QA fail, regenerate through a visual-input-capable workflow or ask for a supported logo upload.

---

## Pattern Scale Rule

Pattern boldness is directly proportional to available negative space:

| Situation | Pattern scale | Why |
|---|---|---|
| Hero image present, right side | Mid — subtle, atmospheric | Hero carries the visual weight; pattern is support |
| No hero, open layout | Large — bold, dominant | Pattern fills the compositional weight |
| Dense text, minimal visual | Micro or none | Copy is the sole focus; pattern would compete |
| Hero + big headline, tight layout | Micro — barely visible glow | Two strong elements; pattern recedes |

**The pattern never competes with the headline or the hero. It always recedes behind both.**

**Opacity ceiling (read this).** Scale is *size*; opacity is *loudness* — control both. The pattern is atmosphere, never a feature:
- **Light theme:** ≈20–25% opacity. Blue-on-lavender should be visible enough to register as a brand atmosphere, while still restrained and readable.
- **Dark theme:** the luminous dots may glow, but still sit behind the hero — bloom, not a spotlight.
- If a viewer notices the pattern *before* the headline or hero, it is too loud — drop the opacity.

---

## Theme System

### Dark Theme
| Property | Value |
|---|---|
| Background | Cars24 Brand Blue `#4736FE` — full bleed dominant base; dark theme means white-on-brand-blue, so the canvas stays vivid. Use controlled same-hue vertical/ambient gradient depth, with optional restrained radial glow around the hero/pattern zone. Do not drift navy/indigo/black/midnight/dark violet/generic purple or dim AI-tech dark mode. |
| Pattern color | White luminous dots, optional pink/teal accent |
| Pattern glow | Luminous, rim-lit, bokeh bloom around edges |
| Headline font | **Arapey-led** — headline predominantly Arapey; **Arapey Italic** on the emotive word(s), Arapey Regular on structural words. A hard structural word may pair in **Geist Bold**. |
| Headline color | White `#FFFFFF` |
| Body font | Geist Regular (Geist Bold for keyword emphasis / forward taglines) |
| Body color | White `#FFFFFF` — single-colour text system; hierarchy via typeface, weight, and size, never colour |
| Format | 4:5 portrait — 1080×1350 |
| Use for | Campaign openers, editorial, newsletter, brand statements |

### Light Theme
| Property | Value |
|---|---|
| Background | Exact `#EBE9FF` pale lavender — full bleed; derived from Brand Blue so the light theme stays distinct but still on-brand |
| Pattern color | Brand blue `#4736FE` dots — no glow, clean |
| Pattern style | **Visible but restrained — low opacity (≈20–25%).** Blue-on-lavender should register as brand atmosphere while keeping text clean and readable. |
| Headline font | **Arapey-led** — same serif-led system as dark theme; Arapey Italic on emotive word(s), Arapey Regular on structural words. |
| Headline color | Brand Blue `#4736FE` — **vivid, full-saturation, never desaturated/greyed/navy** |
| Body font | Geist Regular (Geist Bold for keyword emphasis / forward taglines) |
| Body color | **Two roles:** descriptive body near-black `#161616` · short forward tagline / punch line Brand Blue `#4736FE` (Geist Bold). Use the blue line sparingly. |
| Logo colourway | Brand Blue `#4736FE` icon mark + wordmark — same vivid blue as headline. Reference asset: `Logo - Blue-on-white.png` |
| Icon fill colour | Brand Blue `#4736FE` monochrome family only — saturated blue fills, pale blue overlays, white accents. No green, cyan, teal, or off-brand hues. |
| Element saturation rule | **"Light theme" = pale background only.** All foreground elements (headline, body, logo, icons) stay full-saturation. The pale canvas must never drag elements into washed-out, grey-blue, or desaturated territory. |
| Format | 1:1 square — 1080×1080 |
| Use for | Instagram square, product posts, everyday social |

### Theme governs every output format
The theme above is not just for card creatives — it governs illustrations, photographs/real human images, infographics, and USP layouts alike. **Theme drives the canvas, not the subject:** composited subjects (illustrations, photo cutout heroes, icons) sit on the Cars24 canvas and the theme lives behind them; photographs keep natural lighting with the theme expressed through grade + surrounding canvas (never a purple/lavender tint). Every exported creative — whatever its hero — must read as the same family as the dark/light reference cards.

The full per-theme, per-format rubric is the **Theme Fidelity Checklist** in `3_Skills/Global Skills/master-rules.md §4`, enforced by the **Stage 9 visual-match QA gate** (master-rules §6) before any export — the matching visual layer between generated outputs and the references.

---

## Typography System

**Font files:** `1_Brand Guidelines/03_Typography/fonts/`
- `Arapey-Italic.ttf` — brand serif, emotive/campaign tone
- `Arapey-Regular.ttf` — brand serif, product/factual tone
- Geist full family: `Geist-Thin.ttf` · `Geist-UltraLight.ttf` · `Geist-Light.ttf` · `Geist-Regular.ttf` · `Geist-Medium.ttf` · `Geist-SemiBold.ttf` · `Geist-Bold.ttf` · `Geist-Black.ttf` · `Geist-UltraBlack.ttf` · `Geist-Variable.ttf`

### Font Roles — read this first
- **Arapey** (serif) — the campaign/headline serif. Italic carries emotional weight; Regular is the calmer product/factual serif. Used in both themes, but its *role* differs by theme (see below).
- **Geist** (sans) — headline workhorse, subheadings, and body. The full weight range (Light → Bold) is a tool: weight contrast (Bold vs Light) is itself an emphasis device.
- **Care Sans** (geometric sans) — the **logo typeface ONLY**. Never use it for post headlines, subheadings, or body. It appears only inside the Cars24 logo lockup.

### Headline typeface dominance — Arapey-led in both themes
The current production rule is Arapey-led serif headlines in both dark and light themes. This overrides the older reference-read rule that light theme was sans-led.

**Dark theme → Arapey-led headlines.**
The headline is set **predominantly in Arapey** (serif). Emphasis lives *inside* the serif: **Arapey Italic on the emotive word(s)** vs **Arapey Regular on the structural words**. (Refs: "We've *all* been there", "But what *comes* out of *those* tokens?", "AI is *now part* of how we *build* at Cars24", "Brewed *every* week.", "New *way* of building".) A hard structural word may be set in **Geist Bold** to pair against the serif (ref: "Out-*of*" Arapey Italic / "**Tokens**" Geist Bold).

**Light theme → Arapey-led headlines.**
Use the same refined editorial serif system as dark theme: Arapey Italic on emotive word(s), Arapey Regular on structural words. Do not switch light theme headlines to a sans-led system.

> In short: **both themes = serif headline with italic emphasis.** Never set a whole headline in one uniform weight with no emphasis at all — there is always one device lifting the key word.

### Rendering the typefaces in image prompts (MANDATORY — image models don't know font names)
Image models **cannot reliably read a font by name**. Writing "Arapey" or "Geist" into a prompt can fall back to a generic, almost always **sans-serif**, face, so an Arapey-led headline may silently render as plain sans (verified, project 013). Always **describe the typeface visually and name its category (serif / sans-serif) explicitly**; append the font name only as a trailing hint.
- **Arapey (brand serif)** → *"an elegant high-contrast **serif** — refined thin strokes, classic bracketed serifs, editorial book-serif feel (in the spirit of Arapey)"*. **Italic** → *"a flowing, gently calligraphic **serif italic**"*. **Regular** → *"an upright refined **serif** (roman)"*.
- **Geist (brand sans)** → *"a clean modern geometric **sans-serif** (in the spirit of Geist)"* + weight.
- **Spell the split out word-by-word** so the model commits, e.g. *"'Winning isn't about being' in a refined editorial serif (roman), 'right' in a flowing serif italic — one elegant serif family throughout, NOT sans-serif."*
- **Add the category guard in both themes:** *"the headline is a SERIF typeface, not sans-serif"*. Body is always *"a clean modern sans-serif"*.

### Case rules for visible copy
All visible creative copy uses sentence case. Never use title case for creative headlines, never camel case, and never all caps.

### Subtext / body colour mapping (observed from the reference creatives)
Subtext colour is **theme-dependent**, and light theme runs **two** subtext roles:

| Role | Dark theme | Light theme |
|---|---|---|
| **Headline** | White `#FFFFFF` | Brand Blue `#4736FE` (Geist-Light structural words may sit in the same blue; the emphasis word is the strongest blue/weight) |
| **Descriptive body / subheading** (the explanatory sentence) | White `#FFFFFF`, Geist Regular | **Near-black `#161616`**, Geist Regular (refs: "Sharper ideas. Faster prototypes…", "Not just a side tool.", "Out of Tokens shares…") |
| **Forward tagline / punch-line subtext** (a short pointer line, often the last line) | White `#FFFFFF`, Geist Bold | **Brand Blue `#4736FE`**, Geist Bold (refs: "New ways of building…", "From tokens to outcomes.") |
| **Keyword emphasis inside body** | White, Geist Bold | Geist Bold in the same colour as that body line (near-black for descriptive, e.g. "**Out of Tokens** shares…") |

- **Dark theme is single-colour:** everything is white; hierarchy comes from typeface (Arapey vs Geist), weight, and size — never colour.
- **Light theme is two-colour for text:** brand blue for the headline and for short forward taglines; near-black for the descriptive body. Use brand-blue body sparingly — it is the punch line, not the paragraph.

### Alignment
- Use the dark/light image references to guide text placement rather than enforcing a fixed alignment.
- Prefer text on the left side, but allow the reference layout to determine whether the headline starts top-left, mid-left, or slightly lower.
- Body copy should support the headline and follow the compositional rhythm of the reference creative, not a hard-coded grid.

### Scale
- Headline: dominant — 40–60% of canvas height
- Subheading: clear step-down from headline
- Body: small — strong size contrast against headline

### Headline Size
- Headline is large — takes up 40–60% of the canvas vertically
- Body copy is small — creates deliberate size contrast
- Never equal weighting between headline and body

### Alignment
- Use the dark/light image references to guide text placement rather than enforcing a fixed alignment.
- Prefer text on the left side, but allow the reference layout to determine whether the headline starts top-left, mid-left, or slightly lower.
- Body copy should support the headline and follow the compositional rhythm of the reference creative, not a hard-coded grid.

---

## Pattern Family Reference

Six families. Each has a dark and light variant. Choose based on the composition need.

For abstract dot-form hero slides, use the families below as the **material system**, not as a standalone background asset. Pick the family whose dot behaviour supports the semantic silhouette: Wave Field for motion/road/terrain metaphors, Shell Halo for protection/portal/assurance, Organic Mesh for face/identity/data-surface, Edge Frame for shield/boundary/trust, Particle Bloom for insight/emergence, and Centre Halo for logo/identity/stinger moments.

### 1. Wave Field
- **What:** Rolling dot terrain, halftone waves, flowing dot curtains
- **Dark:** White luminous dots on `#4736FE` — terrain rises from bottom
- **Light:** Blue `#4736FE` dots on `#EBE9FF` — diagonal flow across canvas
- **Placement:** Bottom edge (dark) · full bleed diagonal (light)
- **Scale trigger:** Mid when hero present · large/full when text-only
- **Reference file:** `dark-wave-field-mid.png` · `light-wave-field-fullbleed.png`
- **Generation prompt base:** `wave field emerging from void, flowing dot curtains, transforming, point-cloud surface made from tiny white dots, soft spatial falloff, soft rim glow along wave crests, dense at base perspective falloff upward, blurred circular bokeh foreground, mid scale, open negative space upper two-thirds`

### 2. Shell Halo
- **What:** Partial sphere arc, luminous shell sweeping from a corner
- **Dark:** Bright white arc, sweeping from bottom-right, particle bloom scatter
- **Light:** Soft blue arc, bottom-center, half-sphere rising
- **Placement:** Bottom-right corner (dark) · bottom-center (light)
- **Scale trigger:** Large when open layout · mid when paired with hero
- **Reference file:** `dark-shell-halo-large.png`
- **Generation prompt base:** `shell halo emerging from launch field, wrapping, luminous shell made from tiny white dots, macro-photographic shallow depth, luminous outline rim glow, dense in the focal arc variable dot sizes, blurred circular bokeh, large scale, strong open negative space upper-left`

### 3. Organic Mesh
- **What:** Wrapped point-cloud blob, sculptural flowing form
- **Dark:** White + pink/magenta gradient blob on right side
- **Light:** Soft blue sphere-blob on right edge
- **Placement:** Right side (dark) · right edge (light)
- **Scale trigger:** Mid — always paired with a hero; never large
- **Reference file:** `dark-organic-mesh-mid.png`
- **Generation prompt base:** `organic mesh emerging from void, wrapping, holographic projection made from fine point mesh, macro depth of field, soft rim glow, dense in focal plane perspective falloff at edges, mid scale, open negative space left half, pink-magenta to white gradient within dot structure`

### 4. Edge Frame
- **What:** Rounded-corner glow frame, luminous border from a corner
- **Dark:** Bright white rounded-rectangle glow from bottom-right corner
- **Light:** Subtle blue rounded arc from bottom-right
- **Placement:** Bottom-right corner, sweeping inward
- **Scale trigger:** Large when framing an open composition
- **Generation prompt base:** `edge frame emerging from glow field, unfolding, luminous shell made from tiny white dots, layered perspective, luminous outline corner glow, dense at corner dispersing inward, blurred bokeh at corners, large scale, strong negative space upper-left and upper-right`

### 5. Particle Bloom
- **What:** Soft bokeh clusters, atmospheric drift, scattered spark field
- **Dark:** Glowing bokeh particles dispersed around the hero zone
- **Light:** Fine blue dot scatter, sparse, perimeter
- **Placement:** Perimeter scatter, concentrated near hero
- **Scale trigger:** Micro to mid — always supporting, never dominant
- **Generation prompt base:** `particle bloom emerging from haze, orbiting, point-cloud surface made from particle clusters, soft spatial falloff, halo ring edge bloom, variable dot sizes dispersed, soft particle bloom foreground, micro scale, minimal field, luminous editorial`

### 6. Centre Halo (Sphere)
- **What:** Full 3D dot-sphere floating in the centre
- **Dark:** White dot sphere, wrapping organic form
- **Light:** N/A — only used in dark theme
- **Placement:** Centre — used only when there is NO hero image (identity cards, logo cards)
- **Scale trigger:** Large — it IS the visual when no hero
- **Reference file:** `Centre pattern dark thme.png` (from existing library)
- **Generation prompt base:** `organic mesh emerging from void, analyzing, holographic projection made from fine point mesh, macro depth of field, soft rim glow all around, dense in focal plane, blurred circular bokeh, large scale, centred, strong negative space all sides, monochrome blue-violet`

---

## Master Pattern Generation Prompt Formula

Use this template to generate any pattern for the library via Higgsfield GPT Image 2:

```
Abstract generative background pattern only. No text, no characters, no objects, no scenes, no logos.
[PATTERN_DESCRIPTION from family above].
Positioned at [PLACEMENT: bottom edge / right side / bottom-right corner / full bleed / centre].
[NEGATIVE_SPACE_DESCRIPTION: upper two-thirds clean / left half clean / all sides open].
Background: solid flat [#4736FE brand-blue field for dark / #EBE9FF-family pale brand-blue lavender for light], fills entire frame.
Pattern color: [white luminous dots with soft glow for dark / brand blue #4736FE dots, no glow, for light].
[SCALE: mid scale, subtle / large scale, dominant / full-frame scale].
Cinematic abstract technology aesthetic. Pure graphic pattern, isolated element.
```

### Filled examples

**Dark — Wave Field — Mid — Bottom:**
```
Abstract generative background pattern only. No text, no characters, no objects, no scenes.
Wave field of tiny luminous white dots forming rolling undulating terrain, emerging from the bottom third of the frame, fading into darkness above. Fine point mesh in perspective, dense at the base becoming sparse and dispersed upward. Soft rim glow along wave crests, perspective falloff creates depth.
Positioned at bottom edge.
Upper two-thirds is clean open negative space.
Background: solid flat #4736FE, fills entire frame.
Pattern color: white luminous dots with soft glow.
Mid scale, subtle, supporting.
Cinematic abstract technology aesthetic. Pure graphic pattern, isolated element.
```

**Dark — Shell Halo — Large — Bottom-right:**
```
Abstract generative background pattern only. No text, no characters, no objects, no scenes.
Large luminous spherical shell arc emerging from the bottom-right corner, made entirely of tiny white glowing dots arranged in a partial sphere. The arc sweeps from lower-right toward upper-right, bright luminous rim with particle bloom and bokeh scatter around edges. Dense in the focal arc, dispersing outward.
Positioned at bottom-right corner.
Upper-left two-thirds is clean open negative space.
Background: solid flat #4736FE, fills entire frame.
Pattern color: white luminous dots with bright rim glow and particle bloom.
Large scale, dominant, energetic.
Premium launch visual aesthetic. Pure graphic pattern, isolated element.
```

**Light — Wave Field — Full bleed — Diagonal:**
```
Abstract generative background pattern only. No text, no characters, no objects, no scenes.
Full frame wave field of fine dots forming rolling undulating wave terrain. Tiny dot grid undulates in perspective creating topographic wave forms, flowing diagonally from lower-left toward upper-right. Denser in the center, dispersing at edges.
Positioned full bleed, diagonal flow.
Background: solid flat #EBE9FF-family pale lavender derived from Brand Blue, fills entire frame; keep it visibly lavender for light/dark distinction, but not pink, grey, beige, or generic pastel purple.
Pattern color: brand blue #4736FE dots, no glow, clean and subtle.
Mid scale, editorial, minimal contrast.
Soft editorial aesthetic. Pure graphic pattern, isolated element.
```

**Dark — Organic Mesh — Mid — Right side:**
```
Abstract generative background pattern only. No text, no characters, no objects, no scenes.
Organic mesh blob of wrapped point-cloud dots on the right half of the frame, tactile sculptural form made of fine white dots arranged in flowing curved surface with depth and dimension. Form is partially visible, cropped at the right edge. Soft pink-magenta to white gradient within the dot structure, glowing rim.
Positioned across the right side as part of the full-background atmospheric flow.
Left half is clean open negative space.
Background: solid flat #4736FE, fills entire frame.
Pattern color: white and pink-magenta tinted dots, sculptural glow.
Mid scale, tactile, supporting.
Cinematic abstract technology aesthetic. Pure graphic pattern, isolated element.
```

---

## Full Creative Brief Template

Use this to describe a complete three-layer creative (for image generation or design briefing):

```
Cars24 social creative — [DARK / LIGHT] theme, [FORMAT: 1080×1350 4:5 / 1080×1080 1:1].

LAYER 1 — Background:
[Dark: Cars24 Brand Blue #4736FE as the dominant full-bleed canvas / Light: exact #EBE9FF pale brand-blue lavender] single-hue field. Dark uses a controlled same-hue vertical/ambient gradient for premium depth, with optional restrained radial glow around the hero/pattern zone; it may drift slightly lighter/darker around #4736FE but must still read as bright Cars24 brand blue. Dark must not drift navy/indigo/black/midnight/dark violet/generic purple or look dimmed. Light must remain lavender for distinction but stay derived from the brand-blue family. No multi-colour gradient. Do not render the hex codes as text.

LAYER 2 — Pattern:
[PATTERN_FAMILY] pattern at [PLACEMENT], [SCALE].
[Color: white luminous dots / blue #4736FE dots].
[Specific glow/style description].
Pattern occupies the [right/bottom] zone.

LAYER 3 — Hero:
[Description of hero image — person/car/illustration].
Positioned [right / lower-right], bleeding from the right edge.
No background on the hero — clean cutout composited over layers 1+2.

TEXT:
Headline (top-left): "[HEADLINE TEXT]"
Font (describe VISUALLY by category — never font name alone; image models ignore names and default to sans): [BOTH DARK AND LIGHT → headline in a refined editorial SERIF (in the spirit of Arapey): emotive word(s) in flowing serif italic vs structural words in upright serif roman; a hard word may pair in clean sans-serif bold only when needed — "the headline is a SERIF typeface, not sans-serif"]. Body: clean modern sans-serif.
Color: [White for dark / exact Cars24 Brand Blue #4736FE for light headline and short punch/tagline]
Body color: [DARK → white | LIGHT → near-black #161616 for descriptive body; Brand Blue #4736FE Geist Bold for a short forward tagline]
Body (below headline or upper-left): "[BODY TEXT]"
Font: Geist Regular, small
Color: [White / #161616]
```

---

## Quick Decision Flowchart

**Step 1 — Choose theme:**
- Brand statement, campaign, editorial, newsletter → Dark (`#4736FE`)
- Product post, everyday social, Instagram square → Light (`#EBE9FF`)

**Step 2 — Choose pattern family:**
- Need direction/sweep → Wave Field
- Need energy/launch feel → Shell Halo
- Need sculptural/tactile depth → Organic Mesh
- Need subtle atmosphere around hero → Particle Bloom
- Need a contained frame → Edge Frame
- No hero, identity card → Centre Halo

**Step 3 — Set pattern scale:**
- Hero present → Mid
- No hero, open layout → Large
- Dense text → Micro or none

**Step 4 — Place the pattern:**
- Pattern can flow across the full background
- Text zone stays clean and readable
- Pattern stays behind the hero and text, never as a foreground layer

**Step 5 — Typography:**
- Dark theme → **Arapey-led** headline (Arapey Italic on emotive word, Arapey Regular structural; Geist Bold may pair a hard structural word) · Geist Regular body · **all white** (single-colour text)
- Light theme → **Arapey-led** headline in Brand Blue (Arapey Italic on emotive word, Arapey Regular structural) · body **two-colour**: near-black `#161616` for descriptive, Brand Blue `#4736FE` Geist Bold for a short forward tagline
- Always have ONE emphasis device lifting the key word — never a flat uniform headline

**Step 6 — Verify composition:**
- Does the text have clean space? (left side, no pattern)
- Does the hero have atmospheric depth behind it? (pattern behind it, never over it)
- Is the pattern scale proportional to negative space?
- Is the headline the dominant element (40–60% of canvas)?

---

## What to Avoid

- Pattern that reduces text readability
- Pattern larger than the negative space warrants — it competes with copy
- **A loud / high-opacity pattern — especially in light theme.** The dot field is controlled atmosphere, never a foreground feature. Light-theme dots sit at ≈20–25% opacity.
- A *multi-colour* gradient in the background — the field stays in one hue family; only a subtle same-hue vertical gradient/glow is allowed (see Layer 1)
- Dark-theme background cues like "dark background", "deep blue", "midnight", "void", "black", "dramatic shadows", or "high-contrast dark field" — contrast belongs to the white text and white pattern, while the canvas stays anchored to Cars24 Brand Blue `#4736FE`. Controlled same-hue vertical/ambient gradient and restrained radial hero glow are allowed; navy/indigo/black/generic purple/dim AI-tech drift is not.
- A flat, uniform headline with no emphasis device — there is always one device lifting the key word (Arapey Italic vs Regular in both themes)
- Setting a **light-theme** headline in a sans-led system — current production output uses Arapey-led serif headlines in both themes.
- Using brand-blue body text for a full descriptive paragraph in light theme — brand blue is the headline + the short forward tagline only; descriptive body is near-black `#161616`
- Colour-coding text in **dark** theme — dark is a single-colour (white) system; emphasis comes from typeface, weight, and size, never colour
- Two competing emphasis words at equal prominence — one key word dominates
- Two pattern families in one creative — one family per creative, one scale variant
- Hero bleeding off an edge — it should be fully contained inside the canvas
- **Hero cropped at the wrong place — head, face, or key features cut off at a corner or the top edge.** Everything that carries meaning stays inside the safe zone. A subject framed so tightly that the generator clips it is wrong — pull the subject in and give it headroom.
- Mint green as the pattern color — it is a brand accent for product/campaign contexts (badges, CTAs, stars), not the dot pattern

---

## Cross-Reference Index

| Need | Go to |
|---|---|
| **What to attach + what prompt preamble to write for any Higgsfield call** | **`HIGGSFIELD-CONTEXT-PACKAGE.md`** ← load at Stage 8 |
| Visual description of every illustration reference image | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 1 |
| Visual description of every photography layer | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 2 |
| Pattern-to-reference-file mapping (all 13 patterns, with visual descriptions) | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 3 |
| Icon vocabulary + soft dimensional glass / 3D / flat style guides | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 5 |
| USP badge visual spec + attachment protocol | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 6 |
| Theme composition (what the dark/light template images actually show) | `HIGGSFIELD-CONTEXT-PACKAGE.md` Package 7 |
| Which real file shows what (vision-verified) | `REFERENCE-ATLAS.md` |
| Pattern generation prompt formula (Higgsfield) | Master Pattern Generation Prompt Formula above |
| Full creative brief (design handoff) | Full Creative Brief Template above |
| Which pattern family to use | Pattern Family Reference above |
| Dark vs light decision | Quick Decision Flowchart Step 1 |
| Headline font files | `1_Brand Guidelines/03_Typography/fonts/` |
| Generated pattern PNGs | `2_Image References/Generated Patterns/` |
| Reference creative PNGs | `2_Image References/Dark theme/` + `Light theme/` |
| Pattern reference PNGs | `2_Image References/Patterns in creatives/References/` |
| Brand colour values | `1_Brand Guidelines/02_Color-System/notes.md` |
| Illustration style + prompt template | `3_Illustrations References/ILLUSTRATION-GENERATION-GUIDE.md` |
| Logo placement rules | `1_Brand Guidelines/07_Digital-Composition-&-Templates/notes.md` |
| Logo file to upload to Higgsfield (per background) | `1_Brand Guidelines/01_Brand-Identity-&-Logo/Logos/higgsfield-logo-reference-map.md` |
