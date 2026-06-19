# Cars24 Maker Agent — Codex Entry Point

## Load order

1. Load skill: 3_Skills/2_Codex Skills/maker-skill.md
2. Load agent definition: 2_Agents/2_Codex Agents/maker-agent.md
3. Brand references: 1_References/

## Project structure

1_References/   — Brand guidelines, image references, theme notes
2_Agents/       — Agent definitions (Claude, Codex, Global)
3_Skills/       — Skill files (Claude, Codex, Global master)
4_exports/      — Output files saved here

## Source of truth

All rules: 3_Skills/Global Skills/master-rules.md
Do not edit Claude or Codex skill files directly.
To sync rule changes: run `python3 tools/sync_skills.py`.
Claude users may also use `/sync-skills` via `.claude/commands/sync-skills.md`.

## Project version

The project version is the `version` value in `3_Skills/Global Skills/master-rules.md` `sync-metadata`.
`AGENTS.md` does not maintain an independent version number; it must always mirror the current `master-rules.md` version ledger.
Current mapped version: `v2.21` from `3_Skills/Global Skills/master-rules.md`.

When the user asks to update the version, use `master-rules.md` as the single version ledger. Summarize what changed since the previous version, which skills/references/agents are impacted, how the changes help Maker Agent users, and rollback considerations.

## Reference tagging — v2.0

Use `1_References/reference-index.json` and `1_References/reference-tags/` before selecting image references. The tag index defines each reference's role, attachability, copy-from fields, ignore-from fields, and safety guards.

Do not use `4_exports/` as canonical reference-learning input. Exports are output history, not brand truth.

Theme cards containing marble/statue subjects are layout references only. Copy layout, subject scale, negative space, text hierarchy, and pattern placement. Do not generate marble/statue photo heroes; photo heroes must be real humans, real cars, real hubs, or real service moments.

## Layout selection — v2.6

Before prompt assembly, create a visible layout plan for every slide:
`Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason`.

For carousels and batches, do not use the same archetype or the same top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asks for a consistent repeated system. Batch visual territories must include layout + style, not style alone.

## Codex image generation default

When working in Codex, default to Codex imagegen (`image_gen`) for image generation.
Use Higgsfield only when the user explicitly requests Higgsfield, Codex imagegen is unavailable/unsuitable, or a non-Codex session is running.
For every Higgsfield route, run `higgsfield account status` first. If authentication fails, stop and ask the user to run `higgsfield auth login`. After authentication succeeds, default to GPT Image 2 (`gpt_image_2`), attach the approved reference bundle in map order, and show any requested-to-provider aspect-ratio mapping before approval.
Still follow the Maker image pipeline: frozen copy, slide plan, reference-role map, composite prompt, explicit approval, generation-time logo reference when logo is needed, and export to `4_exports/`.

## Session start — MANDATORY FIRST RESPONSE

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
Do not skip this step even if the user's first message already contains a brief — still show this prompt first, then incorporate their brief into the chosen path.

After the user replies, load the full skill from 3_Skills/2_Codex Skills/maker-skill.md and follow the path for their chosen option.

If the user chooses option 3, ask whether they want a single image, carousel, or batch export before collecting copy. For carousel, ask the number of slides with 3 as the suggested default before collecting/pasting copy. For batch export, open/use the batch post creation modal when available, provide the canonical downloadable Excel template at `5_BATCH_EXPORT/cars24-batch-processing-template.xlsx`, wait for the completed upload, then process each completed row as one image-only brief; `Number of slides` defaults to 1 unless specified, and rows above 1 are carousel briefs. Every path follows the same approval, generation, and export rules.
If the user chooses option 4, enter Repository settings mode for reviewing or changing persistent repository behavior. In that mode, inspect and plan freely, but ask for explicit confirmation before editing any repo-tracked file.

Persistent repository/workflow changes are only allowed after the user explicitly enters option 4 in the current thread. Outside Repository settings mode, the agent may discuss repo changes at a high level, but must redirect there before applying changes to onboarding flow, workflow/routing rules, prompt structure, provider defaults, export/versioning rules, source-of-truth docs, or generated agent/skill behavior. Normal copy/image work and one-off creative revisions remain allowed through options 1–3.

## Export — MANDATORY STRUCTURE

Every file saved to `4_exports/` must follow this structure. No exceptions.

Never dump files flat into `4_exports/`. Three levels: project folder → version folder → image files.

```
4_exports/{serial}_{brief}_{DD-Mon}/
  v1/
    {brief}-image1.[ext]
    {brief}-image2.[ext]
  v2/
    {brief}-image1.[ext]
```

- `{serial}` — zero-padded counter, increments per new brief: `001`, `002`, `003`
- `{brief}` — kebab-case slug of the content brief, max 30 chars
- `{DD-Mon}` — date of the run, e.g. `31-May`
- `vN/` — one version folder per generation run
- `{brief}-imageN` — one file per slide inside the version folder, using the same short kebab-case brief slug so exported files keep context

Before saving any file, check the existing numbered folders in `4_exports/` to determine the next serial number.

## Learned production preferences

These are accumulated design and workflow rules learned from user feedback. They override default brand guidelines where noted.

### Auto-export after generation
Always export outputs immediately after generation. Do not ask whether to export. Export everything to `4_exports/` following the mandatory structure, then present results and ask for feedback/revisions.

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

If the user wants to promote feedback into a persistent repository rule, they must first enter Repository settings mode in the current thread. Inside that mode, ask for explicit confirmation before editing any repo-tracked file. Then update the source of truth first (`master-rules.md` and/or `CREATIVE-DIRECTION.md`), propagate to generated Claude/Codex mirrors, verify no stale conflicting rule remains, and report changed files.

### Serif headlines in both themes
Use Arapey-led serif headlines in **both** dark and light themes. The light theme does not switch to sans-led headlines. Use Arapey Italic on the emotive word(s), Arapey Regular on structural words. Describe the headline as a refined editorial serif in image prompts.

### Sentence case only
All visible creative copy must be sentence case. Never use title case for creative headlines, never camel case, and never all caps.

### Photo cutout style
Photo subjects must be a clean cutout removed from their environment, with a visible white accent outline. They merge onto the brand canvas, not into a rectangular photo frame.

### Illustration reference model
For any illustrated hero, use `1_References/3_Illustrations References/Main_reference.png` as the mandatory style anchor. Additional illustration-folder references are scene supplements only. Approved person/product/proper-noun photos are identity or context references only and must be translated into the Cars24 modern sleek flat editorial illustration style; they must not turn the output into a photorealistic or painted-photo portrait.

### Hero and pattern framing
Heroes must be fully contained inside the canvas. Do not crop heads, hands, cars, icons, or key objects, and do not bleed the hero off an edge.

Patterns may flow across the full background as a clean atmospheric layer, but they must stay behind text and hero and preserve text readability. Pattern must never appear on top of a photo cutout, illustration, or icon.

For abstract pattern/form, default to a contextual abstract dot-form hero: the Cars24 halftone/particle pattern treatment becomes the hero itself. Dense dots and bokeh falloff may form recognisable semantic silhouettes such as a car, key, face, shield, or road, while lighter dots continue across the full canvas as atmosphere. Keep it abstract and metaphor-led, not a literal illustration, photo, icon set, UI card, dashboard, or infographic flow. Never default to generic terrain unless that exact metaphor fits the slide.

### Light theme pattern opacity
Light theme dot patterns should sit at approximately 20–25% opacity: clear enough to register as a brand atmosphere, but still restrained.

For light-theme abstract dot-form heroes, soft bokeh depth is allowed inside/around the hero formation, but the visual must remain clean brand-blue halftone dots on pale lavender with little or no glow.

### Brand-colour theme lock
Dark theme backgrounds must stay bright Cars24 Brand Blue `#4736FE` as the dominant canvas. "Dark theme" means white text and white luminous pattern on brand blue; it does not mean a darkened background. Do not let the canvas drift to navy, indigo, black, midnight blue, dark violet, or heavily dimmed blue; any glow is faint and same-hue.

Light theme backgrounds should remain a pale lavender tint in the `#EBE9FF` family so they are clearly distinct from dark theme, but the lavender must be derived from brand blue. Avoid pink, grey, beige, or generic pastel purple drift. Light theme typography uses Brand Blue `#4736FE` for the headline and short punch/tagline, and near-black `#161616` for descriptive body/subheading.

### Logo generation reference
When a creative needs the Cars24 logo, share the correct theme-matched visible logo asset during image generation and render it inside the generated composite. Do not create a post-process/local superimpose step.

Use:
- Dark background → generation context `Logo - White-on-blue.png`
- Light background → generation context `Logo - Blue-on-white.png`
- High-contrast / print → generation context `Logo - Black.png`

Logo sizing should match the reference creatives, fit inside negative space, preserve clear space, and align to the layout axis. In Codex ImageGen, include the repo-relative logo path as the explicit source file to use, not merely traceability: tell the model to copy/use the official logo from that path exactly and never recreate, redraw, simplify, typeset, or modify it. For providers/workflows that support image references, attach/share the same visible logo PNG as visual input with the final generation prompt. Place the logo by layout axis and cleanest negative space. In carousels with the same theme/background family, keep logo placement and size exactly consistent across all logo-bearing slides. The logo may overlap pattern and may overlap hero only if readable, high-contrast, cleanly fitted, and uncropped. If the output changes the logo geometry, drops the icon, alters the wordmark, adds a box/tile, or crops the lockup, fail logo QA and regenerate through a visual-input-capable workflow or ask for a supported logo upload. Do not silently overlay the logo afterward.
