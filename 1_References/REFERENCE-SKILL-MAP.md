---
name: reference-skill-map
description: Vision-verified audit of EVERY reference asset in the Cars24 library — what each shows, whether it can be attached to Higgsfield (and with what role + caption) or is rules-only guidance, and which skill/stage pulls it. Load this when selecting references for any generation, alongside REFERENCE-ATLAS.md.
---

# Cars24 Reference → Skill Map

> **What this is.** A full vision pass (2026-05-31, second pass) over the *entire* reference library — not just the layout/illustration/pattern creatives the [REFERENCE-ATLAS](REFERENCE-ATLAS.md) already covered, but the whole **Brand Guidelines** book (folders 01–10). Every asset is tagged with: an AI-written description of what it actually shows, an **attachability verdict**, a **reference role + paste-ready caption** if attachable, and the **skill/stage** that should pull it.
>
> **Why it exists.** When we attach a reference to Higgsfield, the model fuses it into the composition. That only helps if (a) the reference is a clean visual asset, not a diagram, and (b) we tell the model *what to take and what to ignore*. This map decides both, per asset. Attaching a do/don't chart or a spec sheet injects chart text and crossed-out examples into the output — so most of the brand book is deliberately marked **RULES-ONLY**.
>
> **Relationship to the other docs:**
> - [REFERENCE-ATLAS.md](REFERENCE-ATLAS.md) = source of truth for *observed layout / illustration / pattern asset facts* (DT-/LT- cards, Section C illustrations, Section D patterns). It does not override execution rules.
> - [CREATIVE-DIRECTION.md](CREATIVE-DIRECTION.md) = source of truth for the visual system (composition, theme, type, pattern families).
> - `3_Illustrations References/ILLUSTRATION-GENERATION-GUIDE.md` = source of truth for illustrated-hero execution, including the mandatory style anchor, final-composite delivery, and controlled 60/30/10 palette.
> - **This map** = source of truth for *which Brand-Guidelines asset is attachable, in what role, and which skill owns it.*
> - **v2.0 tag index** = `reference-index.json` + `reference-tags/`. Use it as the machine-readable retrieval layer before selecting references; this map remains the human audit behind brand-guideline attachability.

---

## How to use this map

1. Decide the brief's visual style (illustration / photo / pattern / icon / abstract) and theme.
2. Query `reference-index.json` for role, attachability, copy-from, ignore-from, and quality flags.
3. Resolve conflicts in this order: Creative Direction → Illustration Generation Guide → tag index → this map → Atlas. Then pull the **Layout + Subject + Pattern** refs from the Atlas as usual.
4. Then check **§2 (Skill → Reference matrix)** and **§3 (per-asset audit)** here for any *brand-guideline* asset that should ride along — a palette swatch, the tagline lockup, a photo-style moodboard, an icon-style anchor, a USP stamp, the logo PNG.
5. For every attached ref, paste its **caption** (each tells the model what to take and what to ignore) into Block 5 of the [higgsfield-prompt-builder](../3_Skills/Global%20Skills/higgsfield-prompt-builder.md).
6. **Hard cap still applies: 3 refs per call.** If a palette/photo-mood/USP ref would push past 3, prefer it over a weaker layout ref, or bake its intent into the prompt text instead of attaching it.

---

## §1 — Attachability legend

| Verdict | Meaning |
|---|---|
| 🟦 **LAYOUT** | Attach — copy composition/zone-split/finish only |
| 🟨 **SUBJECT-STYLE** | Attach — copy a hero's rendering style only |
| 🟪 **PATTERN-TEXTURE** | Attach — copy dot density/glow/scale only |
| 🎨 **PALETTE** | Attach — sample the brand colours/gradient; do not render the swatch chart |
| 🔤 **TYPE-SPECIMEN** | Attach — reproduce a pre-typeset lockup (e.g. the tagline) verbatim |
| ✦ **SHAPE** | Attach — use the trapezoid/star as a framing/accent motif |
| ⬢ **STYLE-ANCHOR** | Attach — match Cars24 icon proportions/finish (3D gloss or flat fill). Soft dimensional refs are optional finish inspiration only. |
| 📸 **PHOTO-STYLE** | Attach — match photography lighting/mood/subject treatment (these are *moodboards*, so caption must say "ignore the grid + labels") |
| 🏷️ **USP-STAMP** | Attach — reproduce ONE badge faithfully; ignore the rest of the sheet |
| 🅰️ **LOGO-ASSET** | Attach — reproduce the real wordmark faithfully |
| ⛔ **RULES-ONLY** | **Never attach.** Informs a copy/composition decision but carries headings, do/don't charts, measurement grids, or UI screenshots that would contaminate the output. |

> **Golden rule:** a brand-book *page* (heading + body + diagram) is almost never attachable. Only the clean asset *inside* the system — the logo PNG, the swatch block, the tagline lockup, the icon grid, the photo, the badge — is. When in doubt, mark RULES-ONLY and put the intent into the prompt text.

---

## §2 — Skill → Reference matrix

Which references each skill / pipeline stage should load (read for context) vs attach (send to Higgsfield as `--image`).

| Skill / stage | Style | Load (context) | Attach (`--image`, with caption) |
|---|---|---|---|
| **Founder-voice / copy** (Path 1, Path 2 Step A) | n/a | All `06_Voice-Tone-&-Copy/*`, brand story/vision/purpose/persona | — (none — copy skill never attaches images) |
| **Image — Illustration** (Stage 4 opt 1) | illustration | Creative Direction + ILLUSTRATION-GENERATION-GUIDE + Atlas §C | `Main_reference.png` is mandatory. Add one scene/identity-context reference only if it does not displace the style anchor; use layout/pattern as available within the cap, otherwise describe those roles in prompt text. Final hero is rendered in the composite, never as transparent/chroma-key output. |
| **Image — Photography** (Stage 4 opt 2) | photo | `5_Photography References/PHOTOGRAPHY-GENERATION-GUIDE.md` | matching `5_Photography References/*_exemplar.png` as 📸 PHOTO-STYLE (primary) + optional source moodboard + Atlas LAYOUT |
| **Image — Abstract pattern/form** (Stage 4 opt 3) | pattern | Atlas §D + CREATIVE-DIRECTION abstract dot-form hero + pattern families | clean PNG from `Generated Patterns/` as 🟪 when available; otherwise best matching crop from `Patterns in creatives/References/`; Atlas LAYOUT in prompt text or attach when slot is free |
| **Image — Infographic / icon** (Stage 4 opt 4) | icon | 09_Icon-System + `4_Infographic Icon References/` | `09_Icon-System/02` (proportions) + `03`(3D) for premium marketing/feature callouts or `04`(flat) for dense/process/UI flows; soft dimensional refs from `4_Infographic Icon References/` are optional finish inspiration only |
| **USP / offer callout** (any slide) | overlay | This map §3 / 08_Campaign | `08_Campaign-Assets-&-USPs/03_usp-mnemonics.png` as 🏷️ (one badge) |
| **Tagline lockup** (campaign sign-off) | type | INDEX #tagline | `03_Typography/08_better-drives-lockup.png` as 🔤 |
| **Brand shapes** (campaign framing) | shape | 04_Brand-Shapes | `04_.../07_secondary-brand-shape-star-full.png` as ✦ |
| **Logo on slide** (Stage 8 logo gate) | — | master-rules Logo rule | theme-correct `Logos/Logo - White.png` / `Logo - Blue.png` as 🅰️ |
| **Luxury / Elite** mode | photo/type | 10_Luxury + Arapey | `10_.../01_luxury-elite-colors.png` as 🎨 + Atlas LAYOUT (no blue, no USP) |
| **Any creative** | all | 🎨 `02_Color-System/03_brand-colors-digital.png` for palette discipline | optional 🎨 palette ref if colours drift |

---

## §3 — Brand Guidelines per-asset audit (the gap the Atlas didn't cover)

> Verdicts below are from a direct vision pass on each PNG. `📎 path` is relative to `1_References/1_Brand Guidelines/`.

### 01 — Brand Identity & Logo

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `01_logo-colorways.png` | Spec page: heading + 4 logo treatments (blue/white/black on light/dark) | ⛔ RULES-ONLY | — informs logo colorway choice |
| `03_our-logo.png` | Identity page: heading, paragraph, "repository" button + big blue logo | ⛔ RULES-ONLY | clean logo lives in `Logos/` |
| `04_logo-primary-secondary.png` | Two labelled cards: horizontal (primary) vs stacked (secondary) | ⛔ RULES-ONLY | informs orientation choice |
| `05_logo-clear-space.png` | Measurement diagram with grids + clear-space guides | ⛔ RULES-ONLY | grid lines must never enter a creative |
| `06_logo-regional.png` | 12-script logo contact sheet (Tamil…Arabic) with captions | ⛔ RULES-ONLY | pull a single clean regional lockup if needed |
| `07_logo-lockups-services.png` | Sub-brand lockup table (Online/Offline/Dealer) | ⛔ RULES-ONLY | naming/usage only |
| `08_logo-lockups-partners.png` | Partner co-brand cards with third-party logos | ⛔ RULES-ONLY | would inject foreign marks |
| `09_logo-avoid.png` | Misuse chart — 12 wrong logos, red strike-throughs | ⛔ RULES-ONLY | **never** reproduce these |
| `Logos/Logo - Black.png` | Clean black wordmark + mark, transparent bg, no chrome | 🅰️ **LOGO-ASSET** | "Reproduce this exact Cars24 logo (arrow mark + 'Cars24' wordmark) faithfully in solid black; match proportions/letterforms exactly; do not recolor, restyle, add effects, or distort." |
| `Logos/Logo - Blue.png` | Clean neo-blue wordmark + mark, transparent bg | 🅰️ **LOGO-ASSET** | "Reproduce this exact Cars24 logo faithfully in brand neo-blue; match proportions/letterforms exactly; do not recolor or distort." |
| `Logos/Logo - White.png` | Clean white wordmark + mark, transparent bg (**looks blank in a viewer — it's white-on-transparent, confirmed valid, 4063 opaque white px**) | 🅰️ **LOGO-ASSET** | "Reproduce this exact Cars24 logo faithfully in solid white for dark/blue backgrounds; match proportions/letterforms exactly; do not recolor or distort." |

### 02 — Colour System

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `03_brand-colors-digital.png` | Swatch sheet: Brand Blue 300 `#4736FE` (dominant), Mint `#63FFB1`, Brand Blue 700 `#2B2098`, Neutrals `#F5F5F5`/`#161616`, + tertiary swatches (⚠️ see §4 flag) | 🎨 **PALETTE** | "Sample the exact Cars24 palette from these swatches — electric Brand Blue `#4736FE` dominant, with Mint `#63FFB1`, deep blue `#2B2098`, neutrals; do not render the swatch chart itself." |
| `05_gradient-system.png` | Two gradient panels — historical palette reference only; current production uses Brand Blue `#4736FE` as the dark dominant field and `#EBE9FF`-family pale brand-blue lavender as the light field + DO/DON'T text | 🎨 **PALETTE** (crop to swatches) | "Use the Cars24 colour family only: dark = vivid electric Brand Blue `#4736FE` dominant field, not navy/indigo/darkened; light = pale `#EBE9FF`-family lavender derived from Brand Blue, not pink/grey/beige. Ignore the DO/DON'T text." |
| `06_color-usage-ratio.png` | 60/30/10 ratio bar diagram, heavy text + big numerals | ⛔ RULES-ONLY | drives colour balance, not pixels |

### 03 — Typography

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `01_care-sans-typeface.png` | Care Sans specimen — A–Z car-brand pangram | ⛔ RULES-ONLY | logo-only font; informs only |
| `02_care-sans-usage-rules.png` | All-text do/don't rules | ⛔ RULES-ONLY | — |
| `04_primary-typeface-geist.png` | Geist metric specimen with dimension annotations | ⛔ RULES-ONLY | — |
| `05_type-weights.png` | Weight chart 01–06 (Light 100 … Black 600) | ⛔ RULES-ONLY | informs weight choice |
| `06_setting-type-alignment.png` | Alignment do/don't (justified/right struck out) | ⛔ RULES-ONLY | — |
| `07_pairing-weights.png` | Weight-pairing demo cards with placeholder labels | ⛔ RULES-ONLY | — |
| `08_better-drives-lockup.png` | Pre-typeset tagline lockup — "Better drives, better lives." stacked + single-line, clean Geist on white | 🔤 **TYPE-SPECIMEN** | "Reproduce the tagline lockup 'Better drives, better lives.' exactly as shown (stacked or single-line) in this weight; ignore the page title and the '2 line / Single line' labels." |

### 04 — Brand Shapes & Motion

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `03_brand-shapes-intro.png` | Intro page — trapezoid + star concept cards | ⛔ RULES-ONLY | — |
| `04_primary-shape-inspiration-grid.png` | Photo moodboard (mirrors, windshields) | ⛔ RULES-ONLY | rationale only |
| `05_primary-brand-shape-intro.png` | Narrative intro, photo-in-trapezoid + headline | ⛔ RULES-ONLY | — |
| `06_trapezoid-system.png` | 5-stage trapezoid evolution + corner-radius/do-don't charts | ⛔ RULES-ONLY | drives framing rules |
| `07_secondary-brand-shape-star-full.png` | Clean full-bleed tile of blue four-point concave stars, no diagram chrome on the motif | ✦ **SHAPE** | "Use the blue four-point concave star with these exact curved proportions as a framing/accent motif; ignore the heading and body text on the left panel." |
| `08_secondary-shape-usage.png` | Star usage do/don't + product mockups | ⛔ RULES-ONLY | — |

### 05 — Photography Style  *(all four pages are labelled moodboard collages — attach for mood, never composition)*

> **Primary attachable assets now live in `1_References/5_Photography References/`** — one clean single-photo exemplar cropped from each moodboard below. **Attach the exemplar first** (it's a clean photo, no grid/labels); optionally add the full moodboard for broader mood within the 3-ref cap. Full style rules + per-layer Higgsfield prompts: `5_Photography References/PHOTOGRAPHY-GENERATION-GUIDE.md`.
>
> | Layer | Primary exemplar (attach) | Source moodboard |
> |---|---|---|
> | Product / desire | `5_Photography References/product-cars-first_exemplar.png` | `05_.../02_product-cars-first.png` |
> | Assisted / reassurance | `5_Photography References/assisted-experience_exemplar.png` | `05_.../03_assisted-experience.png` |
> | Lifestyle / joy | `5_Photography References/brand-lifestyle_exemplar.png` | `05_.../04_brand-lifestyle.png` |
> | Hubs / credibility | `5_Photography References/hubs-infrastructure_exemplar.png` | `05_.../05_hubs-infrastructure.png` |

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `02_product-cars-first.png` | 9-image grid: glossy solo cars, golden-hour, architectural backdrops, **no people**; register = **desire** | 📸 **PHOTO-STYLE** | "Match this car-hero photography mood — warm dimensional lighting, glossy clean vehicle as the sole subject, no people; take only lighting + subject treatment; ignore the grid, text, and white slide frame." |
| `03_assisted-experience.png` | 8-image grid: Cars24 staff in blue/purple polos + customers around cars, natural daylight, documentary feel; register = **reassurance** | 📸 **PHOTO-STYLE** | "Reproduce this service-in-action mood — Cars24 staff in branded polos helping a customer around a car in natural daylight, warm/trustworthy; take only lighting, mood, and people-with-car treatment; ignore the grid, labels, white frame." |
| `04_brand-lifestyle.png` | 9-image grid: families/solo drivers, joy, road-trip, arm-out-window, sun-drenched; register = **joy** | 📸 **PHOTO-STYLE** | "Match this aspirational lifestyle mood — joyful people/families with their car in bright sun-drenched light, candid emotional moments; take only lighting, warmth, emotional treatment; ignore the grid, text, white frame." |
| `05_hubs-infrastructure.png` | 9-image grid: brand-blue facades w/ green-stripe trim + Cars24 signage, fleets, showrooms, crisp daylight; register = **credibility** | 📸 **PHOTO-STYLE** | "Reproduce this hub/infrastructure mood — brand-blue facades with green trim + Cars24 signage, vehicle fleets/showrooms in crisp daylight conveying scale; take only architecture, palette, scale; ignore the grid, text, white frame." |

### 06 — Voice, Tone & Copy  *(entire folder supports the founder-voice / copy skill, not the image pipeline)*

| Asset | Shows | Verdict | Supports |
|---|---|---|---|
| `01_brand-story.png` | Brand story + messaging pillars (text) | ⛔ RULES-ONLY | founder-voice — narrative source |
| `02_brand-vision.png` | "Better drives, better lives" + Scale/Simplicity/Sustainability | ⛔ RULES-ONLY | founder-voice — positioning |
| `03_brand-purpose.png` | Six purpose principles (text/icons) | ⛔ RULES-ONLY | founder-voice — voice principles |
| `04_tone-of-voice-principles.png` | Confident/Warm/Sharp cards | ⛔ RULES-ONLY | founder-voice — tone |
| `05_tone-universal-do-dont.png` | Universal + India DO/DON'T tables | ⛔ RULES-ONLY | founder-voice — universal + India tone |
| `06_tone-uae-australia.png` | UAE + Australia DO/DON'T tables | ⛔ RULES-ONLY | founder-voice — UAE + AU tone |
| `07_brand-persona.png` | 5-trait persona cluster diagram | ⛔ RULES-ONLY | founder-voice — persona |
| `09_copy-grammar-rules-1.png` | Grammar rules 1–5 (British spelling, sentence case, name) | ⛔ RULES-ONLY | founder-voice — mechanics |
| `10_copy-grammar-rules-2.png` | Rules 6–7: dates, Oxford comma, per-market currency | ⛔ RULES-ONLY | founder-voice — formatting |

### 07 — Digital Composition & Templates

| Asset | Shows | Verdict | Caption / supports |
|---|---|---|---|
| `01_logo-placement-social.png` | Safe-area wireframes + unsafe-zone pixel callouts | ⛔ RULES-ONLY | composition — logo placement/safe zones |
| `02_video-reels-safe-zones.png` | Reels safe-area wireframes + annotated IG screenshot | ⛔ RULES-ONLY | video composition — safe zones |
| `03_video-intro-frames.png` | Finished intro-frame creative wrapped in annotation/guide chrome | ⛔ RULES-ONLY | intro-frame hierarchy (chrome makes it unattachable) |
| `04_digital-assets-templates.png` | **Actual finished creatives** — "30 Day Return" photo banners + blue square social templates, minimal chrome | 🟦 **LAYOUT** | "Match the layout/finish of these Cars24 templates — bold brand-blue square posts and clean photo-led banners, confident headline, logo top-left, one clear message; do not copy the exact copy or photos." |
| `05_cta-button-guidelines.png` | CTA proportional-scaling spec + placeholder mockups | ⛔ RULES-ONLY | composition — CTA sizing |

### 08 — Campaign Assets & USPs

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `03_usp-mnemonics.png` | 6 USP badge lockups (icon + wordmark each) in **black outline + neon lime-green fill**: Lifetime Warranty, Kavach+ RC Transfer, Easy Financing, 300+ Quality Checks, 30 Day Free Repair, 30 Day Return | 🏷️ **USP-STAMP** | "Reproduce ONLY the single USP badge specified (e.g. '300+ Quality Checks') exactly as drawn — black outline, neon lime-green fill, icon + wordmark — and ignore all other badges, the card frames, the body text, and the white slide background." |

### 09 — Icon System

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `02_icon-system-overview.png` | Two clean grids — top "3d icons" (glossy dimensional), bottom "Flat icons" (solid blue), small labels + left copy | ⬢ **STYLE-ANCHOR** | "Match the icon proportions/rendering shown — glossy blue 3D icons (top set) and bold solid-blue flat icons (bottom set); ignore the heading, body text, and the '3d/Flat icons' labels." |
| `03_3d-icon-generator.png` | Top grid of glossy 3D blue icons + a dark ChatGPT-UI screenshot below | ⬢ **STYLE-ANCHOR** | "Match the moderate-realism glossy blue 3D icon style/proportions in the top icon row; ignore the left-panel rules text and the dark screenshot panel." |
| `04_flat-icon-generator.png` | Top grid of bold solid-blue flat icons + a dark ChatGPT-UI screenshot below | ⬢ **STYLE-ANCHOR** | "Match the bold solid-blue flat icon style (no gradients/shadows, high contrast) and proportions in the top icon row; ignore the left-panel rules text and the dark screenshot panel." |
| `4_Infographic Icon References/soft-dimensional-glass-icons-blue.png` | Blue-dominant translucent glass icon reference sheet: rounded filled forms, frosted pale-blue overlays, soft internal blur | ⬢ **STYLE-ANCHOR** | "Optional finish inspiration only: copy soft highlights, gentle depth, rounded filled geometry, and polish discipline. Ignore exact icons, white background, grid, text, app-icon layout, glass tiles, one large glass container, and generic UI styling." |
| `4_Infographic Icon References/soft-dimensional-glass-icons-mint.png` | Blue/mint translucent glass icon reference sheet: overlapping rounded forms, restrained mint accent, soft dimensional blur | ⬢ **STYLE-ANCHOR** | "Optional finish inspiration only: copy restrained mint accent, soft highlights, gentle depth, and rounded filled geometry. Ignore exact icons, labels, white background, grid, UI chrome, app-icon layout, glass tiles, one large glass container, and generic UI styling." |

### 10 — Luxury & Elite Sub-Brand

| Asset | Shows | Verdict | Caption (if attach) |
|---|---|---|---|
| `01_luxury-elite-colors.png` | Luxury swatch sheet: Cream Beige `#FFFDFB`/`#FEF8EB`/`#FDF2DC`/`#B3AA96`, Neutral `#737373`/`#0A0A0A`, beige→tan + charcoal→black gradients | 🎨 **PALETTE** | "Constrain the palette to these luxury colours — warm cream beiges (`#FFFDFB`,`#FEF8EB`,`#FDF2DC`,`#B3AA96`) with deep charcoal/black (`#737373`,`#0A0A0A`) + the beige→tan / charcoal→black gradients. **No brand blue.** Ignore the swatch labels and hex text." |

---

## §4 — Findings & data flags

1. ✅ **RESOLVED — canonical orange is `#EF4523`** (the documented brand-book value). The digital swatch page (`02_Color-System/03_brand-colors-digital.png`) has **corrupted text labels** on its two tertiary swatches (Orange was labelled `#63FFB1` = Mint's hex; Bright Blue `#2B2098` = Brand Blue 700's hex), so the page text can't be trusted for those two. The brand-book documentation records Orange 600 as **`#EF4523`** — that documented value is canonical and is propagated to `INDEX.md`, `02_Color-System/notes.md`, `master-rules.md §8.2`, the illustration guide, and both skill files (it replaces the stray `#FF6B35` that was in the illustration palette). Orange remains a 10% car/clothing accent only. **"Bright Blue 100" has no separately documented hex** (only the corrupted label) and is treated as a minor UI accent, not a tracked palette colour — not worth chasing.
2. **`Logo - White.png` reads as blank in any image viewer** because it's white-on-transparent. It is valid (confirmed at the pixel level). Don't "fix" or regenerate it; when used on a light background in a tool that previews white-on-white, trust the file.
3. ✅ **RESOLVED — clean photography exemplars cropped.** One clean single frame was cropped from each `05_Photography-Style/*` moodboard and saved to `1_References/5_Photography References/` as a dedicated attachable asset (see §3 Photography rows + `PHOTOGRAPHY-GENERATION-GUIDE.md`). Attach the **exemplar** as the primary 📸 PHOTO-STYLE ref; the full moodboard can still ride along for broader mood (caption: "ignore the grid + labels").
4. **Icon-generator pages carry a ChatGPT-UI screenshot.** `03_3d-icon-generator.png` and `04_flat-icon-generator.png` include a dark screenshot panel. The top icon grid is the usable anchor — the caption tells the model to ignore the screenshot. The cleaner `02_icon-system-overview.png` is the safer proportions anchor. For premium marketing/process infographic icons, pair it with the `soft-dimensional-glass` refs in `4_Infographic Icon References/`.
5. **No clean isolated trapezoid asset exists.** The star has a clean full-bleed tile (`07_...star-full.png` → ✦ attachable). The trapezoid only appears inside spec diagrams, so it stays RULES-ONLY — describe it in the prompt rather than attaching it.

---

## §5 — What stayed in the Atlas (not re-audited here)

The layout/illustration/pattern creatives in `2_Image References/` and `3_Illustrations References/` are fully fingerprinted in [REFERENCE-ATLAS.md](REFERENCE-ATLAS.md) (Sections A–E). Use that file for DT-/LT- layout cards, the five illustration subject refs, and the pattern PNGs/crops. This map covers everything in `1_Brand Guidelines/` that the Atlas did not.

---

## Change log
- **2026-05-31** — Created from a second full vision pass over `1_Brand Guidelines/` (folders 01–10). Classified all ~50 brand-book assets as attachable (13, with roles + captions) vs RULES-ONLY (the rest). Added Skill→Reference matrix. Flagged the orange-hex inconsistency and the white-logo viewer artefact. Complements REFERENCE-ATLAS.md (Image References) — together they cover the whole library.
