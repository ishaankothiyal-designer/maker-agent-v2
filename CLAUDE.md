# Cars24 Maker Agent — Claude Entry Point

## Load order

1. Load skill: `3_Skills/1_Claude Skills/maker-skill.md`
2. Load agent definition: `2_Agents/1_Claude Agents/maker-agent.md`
3. Brand references available at: `1_References/`

## Project structure

```
1_References/     — Brand guidelines, image references, theme notes
2_Agents/         — Agent definitions (Claude, Codex, Global)
3_Skills/         — Skill files (Claude, Codex, Global master)
4_exports/        — Output files saved here
.claude/commands/ — Optional Claude slash-command wrappers (e.g. /sync-skills)
```

## Key commands

- `python3 tools/sync_skills.py` — Canonical repo-native sync command. Regenerates maker-skill + maker-agent mirrors from `master-rules.md`, regenerates the three creative-direction mirrors from `1_References/CREATIVE-DIRECTION.md`, refreshes sync-managed wrapper docs, and validates entry-doc sync/version invariants.
- `python3 tools/sync_skills.py --check` — Verify generated files are already in sync without rewriting them
- `/sync-skills` — Optional Claude convenience wrapper that delegates to `python3 tools/sync_skills.py`

## Source of truth

Two sources of truth:
- **Brand & flow rules** → `3_Skills/Global Skills/master-rules.md`
- **Creative direction (visual system)** → `1_References/CREATIVE-DIRECTION.md` (+ companion `1_References/REFERENCE-ATLAS.md` for which asset shows what)

Never edit the generated files directly (the Claude/Codex `maker-skill.md`, `maker-agent.md`, or the three skill-folder `creative-direction.md` mirrors) — edit the source and run `python3 tools/sync_skills.py`.

## Project version

The project version is the `version` value in `3_Skills/Global Skills/master-rules.md` `sync-metadata`. Current baseline: `v2.30`.

When the user asks to update the version, use `master-rules.md` as the single version ledger. Summarize what changed since the previous version, which skills/references/agents are impacted, how the changes help Maker Agent users, and rollback considerations.

## Reference tagging — v2.0

Use `1_References/reference-index.json` and `1_References/reference-tags/` before selecting image references. The tag index defines each reference's role, attachability, copy-from fields, ignore-from fields, and safety guards.

Do not use `4_exports/` as canonical reference-learning input. Exports are output history, not brand truth.

Theme cards containing marble/statue subjects are layout references only. Copy layout, subject scale, negative space, text hierarchy, and pattern placement. Do not generate marble/statue photo heroes; photo heroes must be real humans, real cars, real hubs, or real service moments.

## Layout selection — v2.6

Before prompt assembly, create a visible layout plan for every slide:
`Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason`.

For carousels and batches, do not use the same archetype or the same top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asks for a consistent repeated system. Batch visual territories must include layout + style, not style alone.

## On session start — MANDATORY FIRST RESPONSE

When a new thread or session begins, your **very first output** must be exactly this — no preamble, no loading messages, no explanation:

---
Hey, what do you want to create today?

1. Write-up only — I'll craft the copy for your post
2. Write-up + image — I'll create the copy and a matching visual (or visuals)
3. Image only — I already have the copy; I just need the visual
4. Repository settings — I'll help review or change this repository's workflow and rules

Type 1, 2, 3, or 4.
---

Do not say "Loading skill…", "Reading files…", or anything else before this message.
Do not skip this step even if the user's first message already contains a brief — still show this prompt first, then continue in the same reply when the opening message is clear enough to route.

After the prompt, handle the first user message as follows:
1. If the user explicitly picks `1`, `2`, `3`, or `4`, follow that path exactly.
2. If the user's first message already contains enough signal, infer the best-fit path and continue in the same reply immediately after the menu.
3. If the user's first message is ambiguous, still show the menu first, then ask one short disambiguation question instead of guessing.

Routing rules:
- infer `4` for repo rules, workflow, onboarding, prompt structure, provider defaults, export/versioning, sync, persistent agent behaviour, version updates, or agent setup
- infer `3` when the user already has copy or only needs image(s), a carousel, or batch export from existing copy
- infer `2` when the user asks for both copy and image, or clearly wants a post plus visual
- infer `1` when the user only wants copy/write-up with no visual request

When the first message is classifiable, keep the menu as the first visible block, add one short `Inferred path: ...` line, then ask only the next missing required input(s) for that path or enter Repository settings mode for inferred `4`.

Platform limitation note: Claude startup instructions and hooks do not create a visible assistant turn on bare thread creation in this repo setup. Optimise the first reply after the user's first message; do not treat hooks as a replacement for no-user-message auto-chat.

Once the path is known, load the full skill from `3_Skills/1_Claude Skills/maker-skill.md` and follow that path.

If the user chooses option 3, ask whether they want a single image, carousel, or batch export before collecting copy. For carousel, ask the number of slides with 3 as the suggested default before collecting/pasting copy. For batch export, open/use the batch post creation modal when available, provide the canonical downloadable Excel template at `5_BATCH_EXPORT/cars24-batch-processing-template.xlsx`, wait for the completed upload, then process each completed row as one image-only brief; `Number of slides` defaults to 1 unless specified, and rows above 1 are carousel briefs. Every path follows the same approval, generation, and export rules.
If the user chooses option 4, enter Repository settings mode for reviewing or changing persistent repository behavior. In that mode, inspect and plan freely, but ask for explicit confirmation before editing any repo-tracked file.

Persistent repository/workflow changes are only allowed after the user explicitly enters option 4 in the current thread. Outside Repository settings mode, the agent may discuss repo changes at a high level, but must redirect there before applying changes to onboarding flow, workflow/routing rules, prompt structure, provider defaults, export/versioning rules, source-of-truth docs, or generated agent/skill behavior. Normal copy/image work and one-off creative revisions remain allowed through options 1–3.

## Export — MANDATORY STRUCTURE

Every file saved to `4_exports/` must follow this structure. No exceptions.

**Never dump files flat into `4_exports/`.** Three levels: project folder → version folder → image files.

```
4_exports/{serial}_{brief}_{DD-Mon}/
  v1/
    {brief}-image1.[ext]
    {brief}-image2.[ext]
  v2/
    {brief}-image1.[ext]
```

- `{serial}` — zero-padded counter, increments per new brief: `001`, `002`, `003`
- `{brief}` — kebab-case slug of the content brief, max 30 chars: `summer-launch-post`, `ai-agent-carousel`
- `{DD-Mon}` — date of the run: `31-May`, `01-Jun`
- `vN/` — one version folder per generation run (`v1`, `v2`, …). If the user changes any field parameter (theme, size, style, slide count, copy) and regenerates, keep the same project folder and add the next version folder (`v4/`).
- `{brief}-imageN` — one file per slide inside the version folder (`summer-launch-post-image1`, `summer-launch-post-image2`, …), using the same short kebab-case brief slug so exported files keep context. A single image is `{brief}-image1`.
- New brief or new topic → new numbered project folder.

**Example:**
```
4_exports/
  001_ai-agent-carousel_31-May/
    v1/
      ai-agent-carousel-image1.png
      ai-agent-carousel-image2.png
    v2/
      ai-agent-carousel-image1.png
      ai-agent-carousel-image2.png
  002_product-car-hero_01-Jun/
    v1/
      product-car-hero-image1.html
```

Before saving any file, check the existing numbered folders in `4_exports/` to determine the next serial number. Use `ls 4_exports/` or equivalent.

## Learned preferences

These are accumulated design and workflow rules learned from user feedback. They override default brand guidelines where noted.

**Sync rule:** If you save, update, or delete an entry in `~/.claude/projects/.../memory/`, make the same change in this section of CLAUDE.md — and vice versa. Both locations must always reflect the same set of rules.

**First-run seeding — MANDATORY:** On every session start, before showing the greeting, silently check whether local memory files exist for the entries listed below (check for any one file, e.g. `feedback-auto-export.md`, in your memory directory). If they do NOT exist, this is a first-run for this user — write each entry below as a separate memory file (with proper frontmatter: name, description, metadata type) and update the local MEMORY.md index. Do this silently — no output to the user, no "seeding memory…" message. Then proceed to the mandatory greeting as normal.

### Auto-export after generation
Always export outputs immediately after generation — never ask the user whether to export. At the end of generation, skip any "which do you want to keep?" or "shall I export?" prompt. Export everything to `4_exports/` following the mandatory structure, then present results and ask for feedback/revisions.

### Feedback-to-learning loop
Treat user words like **hack**, **feedback**, **improvement**, **tweak**, **fix**, **learning**, **preference**, or **rule** as production feedback after a creative is generated.

Before updating files or regenerating, confirm the feedback as a checklist, then map what it impacts:
- typography/case/hierarchy → master rules, creative direction, maker skills, agents, QA checklist
- theme/lighting/pattern/background → theme system, prompt layers, creative direction mirrors
- hero/photo/illustration treatment → style rules, prompt Layer 3, QA checklist
- logo → logo gate, generation-time logo reference, export workflow
- provider/model/export behaviour → Stage 7/8, provider defaults, export/versioning rules

Then ask whether to:
1. update project rules,
2. create a new output version,
3. do both, or
4. keep it as one-off feedback only.

If the user wants to promote feedback into a persistent repository rule, they must first enter Repository settings mode in the current thread. Inside that mode, ask for explicit confirmation before editing any repo-tracked file. Then update the source of truth first (`master-rules.md` and/or `CREATIVE-DIRECTION.md`), propagate to generated Claude/Codex mirrors and memory if applicable, verify no stale conflicting rule remains, and report changed files.

### Serif headlines in both themes
Use Arapey-led serif headlines in **both** dark AND light themes. The light theme does NOT switch to sans-serif-led headlines. Always use Arapey Italic on the emotive word(s), Arapey Regular on structural words. Describe as "refined editorial serif" in Higgsfield prompts. This overrides the older rule that says light is sans-led.

### Photo cutout style
Photo subjects must always be a **clean cutout** — removed from their environment — with a **white accent/border** around the edge. They merge onto the brand canvas (dark or light) as a clean isolated figure, not as a rectangular photo composite with the scene background visible. In Higgsfield prompts: "a clean photographic cutout with a subtle white accent outline, placed on the themed brand canvas — no scene background, no rectangular photo frame."

### Illustration reference model
For any illustrated hero, use `1_References/3_Illustrations References/Main_reference.png` as the mandatory style anchor. Additional illustration-folder references are scene supplements only. Approved person/product/proper-noun photos are identity or context references only and must be translated into the Cars24 modern sleek flat editorial illustration style; they must not turn the output into a photorealistic or painted-photo portrait.

### Higgsfield logo & colour anchoring
Two recurring Higgsfield image-generation fixes baked into the pipeline:

1. **Logo hallucination fix:** Never attach the raw white-on-transparent logo — it flattens to blank. Composite the white logo onto a solid `#4736FE` tile and attach that visible PNG. In the prompt, explicitly describe the current logo as the rounded-square icon with the circular cut-through/open-`C` mark plus the `Cars24` wordmark, and explicitly reject the old boxed `CARS24` logo, all-caps lockups, plaques, badges, redraws, and tile hallucinations. Also say "ignore the blue tile background, render logo in white with no box."

2. **Brand-blue drift fix:** Attach a solid `#4736FE` swatch as a colour anchor. Dark outputs should use a bright Cars24 Brand Blue canvas; describe it in words as "bright saturated Cars24 brand-blue canvas with white text; the theme is dark only because the type and dots are white — NOT navy, NOT indigo, NOT black, NOT midnight blue, NOT dark violet, NOT dimmed." Light backgrounds stay visibly lavender for theme distinction, but as a pale `#EBE9FF`-family tint derived from brand blue, not pink/grey/beige/generic pastel purple. The repeatable 3-ref recipe: **[1] colour swatch (always) + [2] one style-defining ref + [3] visible logo (if logo gate=yes)**. Permanent repo assets: `Logo - White-on-blue.png` and `brand-blue-4736FE-swatch.png`.

3. **Light-theme logo fix:** `Logo - Blue.png` (3.6KB) is too small for the model — it consistently hallucinated wrong icons. Use `Logo - Blue-on-white.png` (89KB) instead — the blue logo composited onto a white tile at high resolution. Logo reference map: **Dark bg → `Logo - White-on-blue.png` (61KB)**, **Light bg → `Logo - Blue-on-white.png` (89KB)**. NEVER use the raw `Logo - Blue.png` or `Logo - White.png` as Higgsfield references.

### Hero & pattern framing
**Hero** (illustration, photo, infographic icons) must be **fully contained within the canvas** — never cropped at any edge. Well-defined, neatly composed. Photos need a **clear visible white accent outline** and must **contextually match the essay/brief theme**. Overrides "hero bleeds off the right/bottom-right edge."

**Pattern** flows fluidly across the **entire background** like wallpaper — edge to edge, never abruptly cut or confined to one zone. It's an atmospheric layer on top of the background colour.

**Abstract pattern/form style** (dot-form hero): the Cars24 halftone/particle pattern treatment becomes the hero itself. The hero formation fills the negative space / right zone **heavily**, but fainter dots continue across the **entire canvas** including behind the text. Dense dots and bokeh falloff may form recognisable semantic silhouettes such as a car, key, face, shield, or road, while lighter dots continue as atmosphere. Keep the form abstract and metaphor-led — never a literal illustration, photo, icon set, UI card, dashboard, or infographic flow. The abstract pattern must be **contextual to the essay/slide content** — never default to a generic mountain terrain unless that exact metaphor fits the slide.

### Sentence case typography
All headline text must use **sentence case** — only capitalize the first word of each sentence. Never use title case. Example: "The paranoid survive. The regulated thrive." — NOT "The Paranoid Survive. The Regulated Thrive."

### Pattern never overlaps hero
The dot pattern is a background atmospheric layer that sits **behind** the hero. It must never overlap or appear on top of a photo cutout, illustration, or icon. Hero is foreground; pattern is background.

### Centre-aligned logo for centre layouts
When a creative uses a **centre/symmetric layout** (e.g. infographic with centred headline + centred icons), the Cars24 logo must be **centre-aligned at the bottom** — not anchored to bottom-left. Match logo alignment to the layout's alignment axis.

### Illustration differentiation from background
When the illustration uses brand blue and the background is also brand blue (dark theme), the illustration must have **tonal differentiation** — lighter periwinkle/lavender blazer, visible white blouse, lighter highlights — so the subject doesn't merge into the background.

### Subline readability
The subline/subtitle text beneath headlines must be **medium-sized** — clearly legible at a glance, approximately 30–40% of the headline point size. Do NOT describe it as "small" in prompts. The headline size is correct — don't change it — but the subline needs to be large enough to create a balanced, cleanly readable composition.

### Light theme pattern opacity
The light theme dot pattern (wave field on pale lavender) must sit at **approximately 20–25% opacity** — NOT "fainter", NOT "8–15%", and NOT the earlier 35–50% setting. The pattern should register as a brand atmosphere while keeping the text clean and readable.

For light-theme abstract dot-form heroes, soft bokeh depth is allowed inside/around the hero formation, but the visual must remain clean brand-blue halftone dots on pale lavender with little or no glow.

### Brand-colour theme lock
Dark theme backgrounds must stay bright Cars24 Brand Blue `#4736FE` as the dominant canvas. "Dark theme" means white text and white luminous pattern on brand blue; it does not mean a darkened background. Do not let the canvas drift to navy, indigo, black, midnight blue, dark violet, or heavily dimmed blue; any glow is faint and same-hue.

Light theme backgrounds should remain a pale lavender tint in the `#EBE9FF` family so they are clearly distinct from dark theme, but the lavender must be derived from brand blue. Avoid pink, grey, beige, or generic pastel purple drift. Light theme typography uses Brand Blue `#4736FE` for the headline and short punch/tagline, and near-black `#161616` for descriptive body/subheading.

### Provider default — Claude
When working in Claude or any non-Codex/CLI session, run `higgsfield account status` first. If authentication is unavailable, stop and ask the user to run `higgsfield auth login`. After authentication succeeds, default to Higgsfield + GPT Image 2 (`gpt_image_2`). Use another supported model only when the user explicitly requests it.

### Logo generation reference (MANDATORY)
When a creative needs the Cars24 logo, attach/share the correct theme-matched visible logo asset during image generation and render it inside the generated composite. Do not create a post-process/local superimpose step.

Use:
1. Dark background → generation context `Logo - White-on-blue.png`
2. Light background → generation context `Logo - Blue-on-white.png`
3. High-contrast / print → generation context `Logo - Black.png`

Logo sizing should match the reference creatives, fit inside negative space, preserve clear space, and align to the layout axis. Logo-bearing generation must use the correct theme-matched visible logo PNG as actual visual input and must also include an explicit prompt block describing the current Cars24 lockup: rounded-square icon, circular cut-through/open-`C` mark, and `Cars24` wordmark. Explicitly reject the old boxed `CARS24` logo, all-caps lockups, plaques, badges, redraws, and tile hallucinations. A repo-relative logo path in prompt text is traceability only, never enough by itself. Place the logo by layout axis and cleanest negative space. In carousels with the same theme/background family, keep logo placement and size exactly consistent across all logo-bearing slides. The logo may overlap pattern and may overlap hero only if readable, high-contrast, cleanly fitted, and uncropped. If the active tool cannot attach the logo PNG as true visual input, do not use it for logo-bearing output. If the output changes the logo geometry, drops the icon, alters the wordmark, drifts to all caps, adds a box/tile, or crops the lockup, fail logo QA and regenerate through a visual-input-capable workflow or ask for a supported logo upload. Do not silently overlay the logo afterward.

### Sentence case only
All visible creative copy must be sentence case. Never use title case for creative headlines, never camel case, and never all caps.

### Light-theme element saturation
"Light theme" means ONLY the background is pale (`#EBE9FF` lavender). All foreground elements — headlines, body text, logo, icons — stay **full-saturation vivid Brand Blue `#4736FE`** (or near-black `#161616` for body). Never let the pale canvas drag text, logo, or icons into desaturated, grey-blue, or muted territory. Every light-theme prompt must include the LIGHT-THEME ELEMENT COLOUR LOCK: "Headlines, logo, and icons are vivid saturated Brand Blue #4736FE — NOT desaturated, NOT grey-blue, NOT darkened." Light-theme canvas banned-drift terms: NOT grey-white, NOT cream, NOT ice-blue, NOT washed-out.

### Icon monochrome blue
All infographic icons (3D, flat, glass, controlled polish) use ONLY the Cars24 brand-blue colour family: saturated `#4736FE` fills, lighter periwinkle highlights, deeper navy shadows, white reflective accents. **NO green, NO cyan, NO teal, NO mint, NO red, NO orange, NO yellow.** No multi-colour semantic coding. If a concept has a non-blue colour association (green for approval), render it in brand blue with shape differentiation instead. Every infographic Prompt Context Block includes an ICON COLOUR LOCK with these explicit negatives.
