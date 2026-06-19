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
To sync rule changes: run /sync-skills (Claude Code slash command).

## Project version

The project version is the `version` value in `3_Skills/Global Skills/master-rules.md` `sync-metadata`. Current baseline: `v2.23`.

When the user asks to update the version, use `master-rules.md` as the single version ledger. Summarize what changed since the previous version, which skills/references/agents are impacted, how the changes help Maker Agent users, and rollback considerations.

## Reference tagging — v2.0

Use `1_References/reference-index.json` and `1_References/reference-tags/` before selecting image references. The tag index defines each reference's role, attachability, copy-from fields, ignore-from fields, and safety guards.
Resolve `reference-index.json` asset paths relative to `1_References/` (`path_base`), not repo root.

Do not use `4_exports/` as canonical reference-learning input. Exports are output history, not brand truth.

Theme cards containing marble/statue subjects are layout references only. Copy layout, subject scale, negative space, text hierarchy, and pattern placement. Do not generate marble/statue photo heroes; photo heroes must be real humans, real cars, real hubs, or real service moments.

## Layout selection — v2.6

Before prompt assembly, create a visible layout plan for every slide:
`Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason`.

For carousels and batches, do not use the same archetype or the same top-left text / right-hero anchor on more than two consecutive slides unless the user explicitly asks for a consistent repeated system. Batch visual territories must include layout + style, not style alone.

Batch rows may contain legacy/user-friendly style or layout names. Before prompt approval, map every row into one of four primary styles — illustration, photo, abstract pattern/form, infographic/icon — and one of the eight layout archetypes. Keep the original label as context, but prompt from the canonical mapping.

When the user asks for no visible text, no subtext, or a batch row has `Visible image text = None`, use the dedicated `No-text balanced hero` layout. This is a real layout archetype, not a text layout with copy removed, and it applies to photo, illustration, infographic, and abstract outputs.

## Codex image generation default

When working in Codex, use Codex imagegen (`image_gen`) for preview/exploration.
For production outputs that must auto-export to `4_exports/`, use a file-producing project-local path from the start, preferably `tools/maker_image_export.py` or an approved provider CLI that writes directly into the version folder.
If a production job needs a colour swatch, style reference, or visible logo reference for fidelity, the actual generation path must preserve that approved Stage 7 reference bundle. Do not silently degrade a logo/style-critical job to prompt-only generation; switch to a reference-capable provider path or ask.
Use Higgsfield only when the user explicitly requests Higgsfield, Codex imagegen is unavailable/unsuitable, the current provider cannot satisfy required references/logo handling, or a non-Codex session is running.
When Higgsfield is used in Claude or any non-Codex CLI session, default to GPT Image 2 (`gpt_image_2`).
Still follow the Maker image pipeline: frozen copy, slide plan, reference-role map, composite prompt, explicit approval, generation-time logo reference when logo is needed, and export to `4_exports/`.
Never regenerate from the same prompt just to export a chat-visible image. If built-in imagegen shows an image in chat but no local file can be verified, stop and ask before regenerating. In production export mode, preview the saved `4_exports/.../{brief}-imageN` file in chat so preview and export are the same bitmap.

## Session start — MANDATORY FIRST RESPONSE

When a new thread or session begins, your **very first output** must be exactly this — no preamble, no loading messages, no explanation:

---
Hey, what do you want to create today?

1. Write-up only — I'll craft the copy for your post
2. Write-up + image — I'll create the copy and a matching visual (or visuals)
3. Image only — I already have the copy; I just need the visual

Type 1, 2, or 3.
---

Do not say "Loading skill…", "Reading files…", or anything else before this message.
Do not skip this step even if the user's first message already contains a brief — still show this prompt first, then incorporate their brief into the chosen path.

After the user replies, load the full skill from 3_Skills/2_Codex Skills/maker-skill.md and follow the path for their chosen option.

If the user chooses option 3, ask whether they want a single image, a carousel, or batch create before collecting copy. For single image, set slides per post to `1`. For carousel, ask the number of slides and create one slide plan/prompt per slide. For batch create, ask whether they have a completed template to upload or need the default template; provide `5_BATCH_EXPORT/cars24-batch-processing-template.xlsx` when needed, wait for the completed upload, then process each ready row as one post/request. In the sheet, `Slides per post = 1` means one image and `Slides per post = 2–10` means a carousel for that row.

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

Export fidelity rule: export means saving the exact generated bitmap, except for deterministic rename/copy/resize operations. It must never mean running a second image generation from the same prompt. In Codex production export mode, generate directly into `4_exports/` and then show the saved file in chat with an absolute Markdown image path.

## Learned production preferences

These are accumulated design and workflow rules learned from user feedback. They override default brand guidelines where noted.

### Auto-export after generation
Always export production outputs immediately after generation. Do not ask whether to export. Export everything to `4_exports/` following the mandatory structure, then present the exact saved files in chat and ask for feedback/revisions.

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

If approved as a rule, update the source of truth first (`master-rules.md` and/or `CREATIVE-DIRECTION.md`), propagate to generated Claude/Codex mirrors, verify no stale conflicting rule remains, and report changed files.

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

No-text variants must use the `No-text balanced hero` layout. Do not simply remove the headline/body from a text-led layout and leave the old text zone empty. Recompose around hero, pattern, logo/stamp if any, and intentional negative space; keep a blank text-safe zone only when the brief explicitly asks for external/manual text later. For hero-led no-text layouts, check optical centring: the cutout/form/icon system should have comparable left/right breathing room and should not touch or crowd one edge unless a deliberate visual counterweight is named.

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

Logo sizing should match the reference creatives, fit inside negative space, preserve clear space, and align to the layout axis. For centre or symmetric layouts, align the logo to the layout axis, usually centre-bottom. If a selected provider cannot accept the logo reference, switch provider or ask; do not silently overlay the logo afterward.

### Infographic icons — semantic-first
Infographic icons must first communicate the slide subject correctly. Prefer soft dimensional glass polish for premium/process icons when it improves output, but use Cars24 3D or flat filled styles when those communicate the subject better or when glass output becomes generic, broken, or unclear. All icon colours stay in the Cars24 brand-blue monochrome family.

### Prompt colour locks
Use exact hex codes for theme/canvas/text/logo/icon colour locks when useful, always paired with "do not render the hex code as text." Illustration subject art should use descriptive colour language so colour codes are not drawn into the artwork.
