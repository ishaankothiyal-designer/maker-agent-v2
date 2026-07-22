#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER_RULES = ROOT / "3_Skills/Global Skills/master-rules.md"
CREATIVE_DIRECTION = ROOT / "1_References/CREATIVE-DIRECTION.md"
AGENTS_MD = ROOT / "AGENTS.md"
CLAUDE_MD = ROOT / "CLAUDE.md"
README_MD = ROOT / "README.md"
SYNC_COMMAND = ROOT / ".claude/commands/sync-skills.md"
SYNC_ORCHESTRATOR = ROOT / "2_Agents/Global Agents/sync-orchestrator.md"


RULE_DERIVED_TARGETS = {
    ROOT / "3_Skills/1_Claude Skills/maker-skill.md": "Maker Skill — Claude Format",
    ROOT / "3_Skills/2_Codex Skills/maker-skill.md": "Maker Skill — Codex / AGENTS.md Format",
    ROOT / "2_Agents/1_Claude Agents/maker-agent.md": "Maker Agent — Claude Definition",
    ROOT / "2_Agents/2_Codex Agents/maker-agent.md": "Maker Agent — Codex Definition",
}


CREATIVE_DIRECTION_TARGETS = {
    ROOT / "3_Skills/Global Skills/creative-direction.md": "Synced mirror of 1_References/CREATIVE-DIRECTION.md. Do not edit directly.",
    ROOT / "3_Skills/1_Claude Skills/creative-direction.md": "Synced mirror of 1_References/CREATIVE-DIRECTION.md. Do not edit directly.",
    ROOT / "3_Skills/2_Codex Skills/creative-direction.md": "Synced mirror of 1_References/CREATIVE-DIRECTION.md. Do not edit directly.",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return text
    return parts[1].lstrip("\n")


def extract_version(source_text: str) -> str:
    match = re.search(r"^version:\s*([0-9.]+)\s*$", source_text, flags=re.MULTILINE)
    if not match:
        raise ValueError("Could not find sync-metadata version in master-rules.md")
    return match.group(1)


def build_rule_derived(title: str, source_text: str) -> str:
    return (
        f"# {title}\n"
        f"> Auto-generated from `3_Skills/Global Skills/master-rules.md`\n"
        f"> Do not edit directly. Run `python3 tools/sync_skills.py` to regenerate.\n"
        f"> Claude users may also use `/sync-skills` when `.claude/commands/sync-skills.md` is present.\n\n"
        "---\n\n"
        "## Sync Note\n\n"
        "This file is a generated mirror of the Maker Agent rules for tool-specific loading. "
        "The single source of truth remains `3_Skills/Global Skills/master-rules.md`.\n\n"
        "---\n\n"
        f"{source_text.rstrip()}\n"
    )


def build_creative_direction(description: str, source_text: str) -> str:
    body = strip_frontmatter(source_text).rstrip()
    return (
        "---\n"
        "name: creative-direction\n"
        f"description: {description}\n"
        "---\n\n"
        "⚙️ **Auto-generated.** Synced mirror of `1_References/CREATIVE-DIRECTION.md` "
        "(single source of truth for creative direction). **Do not edit directly** — edit the primary "
        "and run `python3 tools/sync_skills.py`. Claude users may also use `/sync-skills` when the "
        "repo wrapper exists. Content is verbatim so brand rules are never paraphrased.\n\n"
        "---\n\n\n"
        f"{body}\n"
    )


def build_sync_command() -> str:
    return (
        "Run the canonical repo sync command:\n\n"
        "```bash\n"
        "python3 tools/sync_skills.py\n"
        "```\n\n"
        "Use `python3 tools/sync_skills.py --check` to verify that generated files are already in sync without rewriting them.\n"
    )


def build_sync_orchestrator(version: str) -> str:
    return (
        "# Sync Orchestrator — Global Agent\n"
        "> Canonically triggered by `python3 tools/sync_skills.py`. Claude users may also use `/sync-skills` when `.claude/commands/sync-skills.md` is present.\n\n"
        "---\n\n"
        "## Purpose\n\n"
        "The Sync Orchestrator keeps source-of-truth files and repository entry docs aligned whenever the Maker rules change.\n\n"
        "## Trigger\n\n"
        "Canonical command: `python3 tools/sync_skills.py`\n"
        "Optional Claude wrapper: `/sync-skills`\n"
        "Wrapper location: `.claude/commands/sync-skills.md`\n\n"
        "## Sync Targets\n\n"
        "| Source | Target | Format |\n"
        "|---|---|---|\n"
        "| `3_Skills/Global Skills/master-rules.md` | `3_Skills/1_Claude Skills/maker-skill.md` | Claude skill (conversational, tool-aware) |\n"
        "| `3_Skills/Global Skills/master-rules.md` | `3_Skills/2_Codex Skills/maker-skill.md` | Codex / AGENTS.md (directive, structured) |\n"
        "| `3_Skills/Global Skills/master-rules.md` | `2_Agents/1_Claude Agents/maker-agent.md` | Claude agent definition |\n"
        "| `3_Skills/Global Skills/master-rules.md` | `2_Agents/2_Codex Agents/maker-agent.md` | Codex agent definition |\n"
        "| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/Global Skills/creative-direction.md` | Verbatim mirror (creative direction) |\n"
        "| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/1_Claude Skills/creative-direction.md` | Verbatim mirror (creative direction) |\n"
        "| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/2_Codex Skills/creative-direction.md` | Verbatim mirror (creative direction) |\n"
        "| Sync template in script | `.claude/commands/sync-skills.md` | Claude wrapper doc |\n"
        "| Sync template in script | `2_Agents/Global Agents/sync-orchestrator.md` | Global sync instructions |\n\n"
        "> Two sources of truth: `master-rules.md` (brand/flow rules) → maker-skill + maker-agent files; "
        "`1_References/CREATIVE-DIRECTION.md` (creative direction) → the three `creative-direction.md` mirrors. "
        "Creative-direction mirrors are byte-verbatim (with a stable auto-generated banner) — never reformatted, "
        "so visual rules are never paraphrased.\n\n"
        "## Entry-File Checks\n\n"
        "`AGENTS.md`, `CLAUDE.md`, and `README.md` are repo-tracked entry docs with some manual sections, so the sync "
        "script validates key invariants there instead of rewriting the full files. `--check` fails if those docs drift "
        "away from the canonical sync command or current project version.\n\n"
        "## Sync Process (executed by `python3 tools/sync_skills.py`)\n\n"
        "1. Read both sources: `3_Skills/Global Skills/master-rules.md` and `1_References/CREATIVE-DIRECTION.md`\n"
        "2. Parse the current project version from the `sync-metadata` block in `master-rules.md`\n"
        "3. Regenerate from `master-rules.md`:\n"
        "   - Claude skill → `3_Skills/1_Claude Skills/maker-skill.md`\n"
        "   - Codex skill → `3_Skills/2_Codex Skills/maker-skill.md`\n"
        "   - Claude agent → `2_Agents/1_Claude Agents/maker-agent.md`\n"
        "   - Codex agent → `2_Agents/2_Codex Agents/maker-agent.md`\n"
        "4. Regenerate from `1_References/CREATIVE-DIRECTION.md` with a deterministic banner and verbatim body\n"
        "5. Regenerate the wrapper docs: `.claude/commands/sync-skills.md` and `2_Agents/Global Agents/sync-orchestrator.md`\n"
        "6. Validate entry-doc invariants in `AGENTS.md`, `CLAUDE.md`, and `README.md`\n"
        "7. Report mismatches in `--check`, or rewrite the sync-managed files in write mode\n\n"
        "## Rules for the Sync Agent\n\n"
        "- Preserve all brand rules exactly — do not paraphrase or reinterpret\n"
        "- The master-rules.md `version` value is the repo-level project version. Current baseline: `v"
        f"{version}`.\n"
        "- Increment the version number only if rules or persistent workflow behavior have substantively changed\n"
        "- When the user asks to update the version, update the master-rules.md changelog and summarize what changed since the previous version, which skills/references/agents are impacted, how the change helps users, and rollback considerations\n"
        "- Never remove a rule — only add or update\n"
        "- If a conflict is detected (e.g., a rule contradicts another), flag it to the user instead of resolving silently\n"
    )


def build_readme() -> str:
    return (
        "# Cars24 Maker Agent\n\n"
        "This repository is a Cars24 Maker Agent workspace for copy, image-generation rules, brand references, and export history. "
        "It is not a conventional app service with a runtime server to install and boot.\n\n"
        "## 5-minute quickstart\n\n"
        "```bash\n"
        "git clone https://github.com/ishaankothiyal-designer/maker-agent-v2.git\n"
        "cd maker-agent-v2\n"
        "python3 tools/sync_skills.py\n"
        "python3 tools/sync_skills.py --check\n"
        "```\n\n"
        "Then:\n"
        "- open the repo in Codex or Claude\n"
        "- edit the source-of-truth files, not generated mirrors\n"
        "- save outputs under `4_exports/`\n\n"
        "## Required tooling\n\n"
        "- `git`\n"
        "- `python3`\n\n"
        "Image-generation assumptions:\n"
        "- In Codex, default to Codex ImageGen\n"
        "- Use Higgsfield only as fallback, or when explicitly requested\n\n"
        "## Source of truth\n\n"
        "Edit these files directly:\n"
        "- `3_Skills/Global Skills/master-rules.md`\n"
        "- `1_References/CREATIVE-DIRECTION.md`\n\n"
        "Generated or sync-managed files should not be edited directly:\n"
        "- `3_Skills/1_Claude Skills/maker-skill.md`\n"
        "- `3_Skills/2_Codex Skills/maker-skill.md`\n"
        "- `2_Agents/1_Claude Agents/maker-agent.md`\n"
        "- `2_Agents/2_Codex Agents/maker-agent.md`\n"
        "- `3_Skills/*/creative-direction.md`\n"
        "- `.claude/commands/sync-skills.md`\n"
        "- `2_Agents/Global Agents/sync-orchestrator.md`\n\n"
        "## Sync workflow\n\n"
        "Canonical command:\n\n"
        "```bash\n"
        "python3 tools/sync_skills.py\n"
        "```\n\n"
        "Verification:\n\n"
        "```bash\n"
        "python3 tools/sync_skills.py --check\n"
        "```\n\n"
        "What the sync command manages:\n"
        "- regenerates maker-skill and maker-agent mirrors from `master-rules.md`\n"
        "- regenerates the three `creative-direction.md` mirrors from `1_References/CREATIVE-DIRECTION.md`\n"
        "- refreshes the Claude sync wrapper and global sync orchestrator docs\n"
        "- validates key sync/version invariants in `AGENTS.md`, `CLAUDE.md`, and `README.md`\n\n"
        "If you use Claude and the repo includes `.claude/commands/sync-skills.md`, you can also use `/sync-skills`. "
        "The Python command is still the canonical workflow.\n\n"
        "## Project structure\n\n"
        "- `1_References/` — brand references, visual direction, and reference tagging\n"
        "- `2_Agents/` — generated agent definitions plus global orchestration notes\n"
        "- `3_Skills/` — source rules plus generated Claude/Codex skill mirrors\n"
        "- `4_exports/` — generated output history\n"
        "- `5_BATCH_EXPORT/` — batch spreadsheet template\n"
        "- `tools/` — repo-native helper scripts\n\n"
        "## Export rules\n\n"
        "Do not use `4_exports/` as canonical reference-learning input. It is output history, not brand truth.\n\n"
        "Every generated output should live under the required three-level structure:\n\n"
        "```text\n"
        "4_exports/{serial}_{brief}_{DD-Mon}/\n"
        "  v1/\n"
        "    {item-brief}-v1-image1.[ext]\n"
        "```\n\n"
        "## Batch template\n\n"
        "To regenerate the batch-processing spreadsheet:\n\n"
        "```bash\n"
        "python3 tools/build_batch_processing_template.py\n"
        "```\n\n"
        "## Notes for teammates\n\n"
        "- This repo works without Claude-specific setup.\n"
        "- `.claude/commands/` is optional convenience, not a requirement.\n"
        "- If `python3 tools/sync_skills.py --check` fails, rerun the sync command and review the resulting diff.\n"
    )


def build_agents(version: str) -> str:
    return (
        "# Cars24 Maker Agent — Codex Entry Point\n\n"
        "## Load order\n\n"
        "1. Load skill: 3_Skills/2_Codex Skills/maker-skill.md\n"
        "2. Load agent definition: 2_Agents/2_Codex Agents/maker-agent.md\n"
        "3. Brand references: 1_References/\n\n"
        "## Project structure\n\n"
        "1_References/   — Brand guidelines, image references, theme notes\n"
        "2_Agents/       — Agent definitions (Claude, Codex, Global)\n"
        "3_Skills/       — Skill files (Claude, Codex, Global master)\n"
        "4_exports/      — Output files saved here\n\n"
        "## Source of truth\n\n"
        "All rules: 3_Skills/Global Skills/master-rules.md\n"
        "Do not edit Claude or Codex skill files directly.\n"
        "To sync rule changes: run `python3 tools/sync_skills.py`.\n"
        "Claude users may also use `/sync-skills` via `.claude/commands/sync-skills.md`.\n\n"
        "## Project version\n\n"
        "The project version is the `version` value in `3_Skills/Global Skills/master-rules.md` `sync-metadata`.\n"
        "`AGENTS.md` does not maintain an independent version number; it must always mirror the current `master-rules.md` version ledger.\n"
        f"Current mapped version: `v{version}` from `3_Skills/Global Skills/master-rules.md`.\n\n"
        "When the user asks to update the version, use `master-rules.md` as the single version ledger. "
        "Summarize what changed since the previous version, which skills/references/agents are impacted, how the "
        "changes help Maker Agent users, and rollback considerations.\n\n"
        "## Reference tagging — v2.0\n\n"
        "Use `1_References/reference-index.json` and `1_References/reference-tags/` before selecting image references. "
        "The tag index defines each reference's role, attachability, copy-from fields, ignore-from fields, and safety guards.\n\n"
        "Do not use `4_exports/` as canonical reference-learning input. Exports are output history, not brand truth.\n\n"
        "Theme cards containing marble/statue subjects are layout references only. Copy layout, subject scale, negative space, "
        "text hierarchy, and pattern placement. Do not generate marble/statue photo heroes; photo heroes must be real humans, "
        "real cars, real hubs, or real service moments.\n\n"
        "## Layout selection — v2.6\n\n"
        "Before prompt assembly, create a visible layout plan for every slide:\n"
        "`Slide → archetype → DT/LT layout ref → vertical anchor → dominant element → text zone → hero/pattern zone → reason`.\n\n"
        "For carousels and batches, do not use the same archetype or the same top-left text / right-hero anchor on more than "
        "two consecutive slides unless the user explicitly asks for a consistent repeated system. Batch visual territories must "
        "include layout + style, not style alone.\n\n"
        "## Codex image generation default\n\n"
        "When working in Codex, default to Codex imagegen (`image_gen`) for image generation.\n"
        "Use Higgsfield only when the user explicitly requests Higgsfield, Codex imagegen is unavailable/unsuitable, or a non-Codex session is running.\n"
        "For every Higgsfield route, run `higgsfield account status` first. If authentication fails, stop and ask the user to run `higgsfield auth login`. "
        "After authentication succeeds, default to GPT Image 2 (`gpt_image_2`), attach the approved reference bundle in map order, "
        "and show any requested-to-provider aspect-ratio mapping before approval.\n"
        "Still follow the Maker image pipeline: frozen copy, slide plan, reference-role map, composite prompt, explicit approval, "
        "generation-time logo reference when logo is needed, and export to `4_exports/`.\n\n"
        "## Session start — MANDATORY FIRST RESPONSE\n\n"
        "When a new thread or session begins, your **very first output** must be exactly this — no preamble, no loading messages, no explanation:\n\n"
        "---\n"
        "Hey, what do you want to create today?\n\n"
        "1. Write-up only — I'll craft the copy for your post\n"
        "2. Write-up + image — I'll create the copy and a matching visual (or visuals)\n"
        "3. Image only — I already have the copy; I just need the visual\n"
        "4. Repository settings — I'll help review or change this repository's workflow and rules\n\n"
        "Type 1, 2, 3, or 4.\n"
        "---\n\n"
        "Do not say \"Loading skill…\", \"Reading files…\", or anything else before this message.\n"
        "Do not skip this step even if the user's first message already contains a brief — still show this prompt first, then continue in the same reply when the opening message is clear enough to route.\n\n"
        "After the prompt, handle the first user message as follows:\n"
        "1. If the user explicitly picks `1`, `2`, `3`, or `4`, follow that path exactly.\n"
        "2. If the user's first message already contains enough signal, infer the best-fit path and continue in the same reply immediately after the menu.\n"
        "3. If the user's first message is ambiguous, still show the menu first, then ask one short disambiguation question instead of guessing.\n\n"
        "Routing rules:\n"
        "- infer `4` for repo rules, workflow, onboarding, prompt structure, provider defaults, export/versioning, sync, persistent agent behaviour, version updates, or agent setup\n"
        "- infer `3` when the user already has copy or only needs image(s), a carousel, or batch export from existing copy\n"
        "- infer `2` when the user asks for both copy and image, or clearly wants a post plus visual\n"
        "- infer `1` when the user only wants copy/write-up with no visual request\n\n"
        "When the first message is classifiable, keep the menu as the first visible block, add one short `Inferred path: ...` line, then ask only the next missing required input(s) for that path or enter Repository settings mode for inferred `4`.\n\n"
        "Platform limitation note: do not claim Codex can send a visible assistant message on bare thread creation in this repo setup. Thread automations may wake an existing thread later, but they do not replace first-message onboarding.\n\n"
        "Once the path is known, load the full skill from 3_Skills/2_Codex Skills/maker-skill.md and follow that path.\n\n"
        "If the user chooses option 3, ask whether they want a single image, carousel, or batch export before collecting copy. "
        "For carousel, ask the number of slides with 3 as the suggested default before collecting/pasting copy. For batch export, "
        "open/use the batch post creation modal when available, provide the canonical downloadable Excel template at "
        "`5_BATCH_EXPORT/cars24-batch-processing-template.xlsx`, wait for the completed upload, then process each completed row as one image-only brief; "
        "`Number of slides` defaults to 1 unless specified, and rows above 1 are carousel briefs. Every path follows the same approval, generation, and export rules.\n"
        "If the user chooses option 4, enter Repository settings mode for reviewing or changing persistent repository behavior. In that mode, inspect and plan freely, but ask for explicit confirmation before editing any repo-tracked file.\n\n"
        "Persistent repository/workflow changes are only allowed after the user explicitly enters option 4 in the current thread. "
        "Outside Repository settings mode, the agent may discuss repo changes at a high level, but must redirect there before applying "
        "changes to onboarding flow, workflow/routing rules, prompt structure, provider defaults, export/versioning rules, source-of-truth docs, or generated agent/skill behavior. "
        "Normal copy/image work and one-off creative revisions remain allowed through options 1–3.\n\n"
        "## Export — MANDATORY STRUCTURE\n\n"
        "Every file saved to `4_exports/` must follow this structure. No exceptions.\n\n"
        "Never dump files flat into `4_exports/`. Three levels: project folder → version folder → image files.\n\n"
        "```\n"
        "4_exports/{serial}_{brief}_{DD-Mon}/\n"
        "  v1/\n"
        "    {item-brief}-v1-image1.[ext]\n"
        "    {item-brief}-v1-image2.[ext]\n"
        "  v2/\n"
        "    {item-brief}-v2-image1.[ext]\n"
        "```\n\n"
        "- `{serial}` — zero-padded counter, increments per new brief: `001`, `002`, `003`\n"
        "- `{brief}` — kebab-case slug of the content brief, max 30 chars\n"
        "- `{DD-Mon}` — date of the run, e.g. `31-May`\n"
        "- `vN/` — one version folder per generation run\n"
        "- `{item-brief}-vN-imageN` — one file per slide inside the version folder; use the batch row's kebab-case blog-title slug for `{item-brief}`, or the short project brief slug for non-batch work. `vN` must match the enclosing version folder.\n\n"
        "Before saving any file, check the existing numbered folders in `4_exports/` to determine the next serial number.\n\n"
        "## Learned production preferences\n\n"
        "These are accumulated design and workflow rules learned from user feedback. They override default brand guidelines where noted.\n\n"
        "### Auto-export after generation\n"
        "Always export outputs immediately after generation. Do not ask whether to export. Export everything to `4_exports/` following the mandatory structure, then present results and ask for feedback/revisions.\n\n"
        "### Feedback-to-learning loop\n"
        "Treat user words like **hack**, **feedback**, **improvement**, **tweak**, **fix**, **learning**, **preference**, or **rule** as production feedback after a creative is generated.\n\n"
        "Before updating files or regenerating, confirm the feedback as a checklist, then map what it impacts:\n"
        "- typography/case/hierarchy → master rules, creative direction, maker skills, agents, QA checklist\n"
        "- theme/lighting/pattern/background → theme system, prompt layers, creative direction mirrors\n"
        "- hero/photo/illustration treatment → style rules, prompt Layer 3, QA checklist\n"
        "- logo → logo gate, generation-time logo reference, export workflow\n"
        "- provider/model/export behaviour → Stage 7/8, provider defaults, export/versioning rules\n\n"
        "Then ask whether to:\n"
        "1. update project rules,\n"
        "2. create a new output version,\n"
        "3. do both, or\n"
        "4. keep it as one-off feedback only.\n\n"
        "If the user wants to promote feedback into a persistent repository rule, they must first enter Repository settings mode in the current thread. "
        "Inside that mode, ask for explicit confirmation before editing any repo-tracked file. Then update the source of truth first "
        "(`master-rules.md` and/or `CREATIVE-DIRECTION.md`), propagate to generated Claude/Codex mirrors, verify no stale conflicting rule remains, and report changed files.\n\n"
        "### Serif headlines in both themes\n"
        "Use Arapey-led serif headlines in **both** dark and light themes. The light theme does not switch to sans-led headlines. Use Arapey Italic on the emotive word(s), Arapey Regular on structural words. Describe the headline as a refined editorial serif in image prompts.\n\n"
        "### Sentence case only\n"
        "All visible creative copy must be sentence case. Never use title case for creative headlines, never camel case, and never all caps.\n\n"
        "### Photo cutout style\n"
        "Photo subjects must be a clean cutout removed from their environment, with a visible white accent outline. They merge onto the brand canvas, not into a rectangular photo frame.\n\n"
        "### Illustration reference model\n"
        "For any illustrated hero, use `1_References/3_Illustrations References/Main_reference.png` as the mandatory style anchor. Additional illustration-folder references are scene supplements only. Approved person/product/proper-noun photos are identity or context references only and must be translated into the Cars24 modern sleek flat editorial illustration style; they must not turn the output into a photorealistic or painted-photo portrait.\n\n"
        "### Illustration palette and reference precedence\n"
        "Illustrated heroes use a 60/30/10 colour budget: 60% Cars24 Brand Blue `#4736FE`; 30% restrained supporting deep-blue, off-white, and natural skin tones; and no more than 10% total optional orange/mint accents. Orange is a contextual car or small clothing detail; mint is a deliberate product/campaign cue. Neither is a default, dominant, background, or dot-pattern colour. Icon systems remain brand-blue monochrome under their stricter rule.\n\n"
        "Reference precedence is: `CREATIVE-DIRECTION.md` for the visual system, `ILLUSTRATION-GENERATION-GUIDE.md` for illustrated-hero execution, `reference-index.json` plus `reference-tags/` for eligible selection and attachability, `REFERENCE-SKILL-MAP.md` for the brand-book asset audit, and `REFERENCE-ATLAS.md` only for observed layout/asset facts. A layout reference, scene supplement, or identity/context photo must never override the canonical illustration system.\n\n"
        "### Hero and pattern framing\n"
        "Use intentional editorial framing: declare each hero as `contained` or `intentional editorial edge crop` in the layout plan. Faces, focal interactions, action-carrying hands, and meaning-carrying product detail must remain clear and uncut. A supporting car, shoulder, clothing edge, or environmental form may exit an edge only when it is a deliberate, stylish crop that improves hierarchy and preserves the text zone. Do not allow accidental clipping.\n\n"
        "Patterns may flow across the full background as a clean atmospheric layer, but they must stay behind text and hero and preserve text readability. Pattern must never appear on top of a photo cutout, illustration, or icon.\n\n"
        "For abstract pattern/form, default to a contextual abstract dot-form hero: the Cars24 halftone/particle pattern treatment becomes the hero itself. Dense dots and bokeh falloff may form recognisable semantic silhouettes such as a car, key, face, shield, or road, while lighter dots continue across the full canvas as atmosphere. Keep it abstract and metaphor-led, not a literal illustration, photo, icon set, UI card, dashboard, or infographic flow. Never default to generic terrain unless that exact metaphor fits the slide.\n\n"
        "### Light theme pattern opacity\n"
        "Light theme dot patterns should sit at approximately 20–25% opacity: clear enough to register as a brand atmosphere, but still restrained.\n\n"
        "For light-theme abstract dot-form heroes, soft bokeh depth is allowed inside/around the hero formation, but the visual must remain clean brand-blue halftone dots on pale lavender with little or no glow.\n\n"
        "### Brand-colour theme lock\n"
        "Dark theme backgrounds must stay bright Cars24 Brand Blue `#4736FE` as the dominant canvas. \"Dark theme\" means white text and white luminous pattern on brand blue; it does not mean a darkened background. Do not let the canvas drift to navy, indigo, black, midnight blue, dark violet, or heavily dimmed blue; any glow is faint and same-hue.\n\n"
        "Light theme backgrounds should remain a pale lavender tint in the `#EBE9FF` family so they are clearly distinct from dark theme, but the lavender must be derived from brand blue. Avoid pink, grey, beige, or generic pastel purple drift. Light theme typography uses Brand Blue `#4736FE` for the headline and short punch/tagline, and near-black `#161616` for descriptive body/subheading.\n\n"
        "### Logo generation reference\n"
        "When a creative needs the Cars24 logo, share the correct theme-matched visible logo asset during image generation and render it inside the generated composite. Do not create a post-process/local superimpose step.\n\n"
        "Use:\n"
        "- Dark background → generation context `Logo - White-on-blue.png`\n"
        "- Light background → generation context `Logo - Blue-on-white.png`\n"
        "- High-contrast / print → generation context `Logo - Black.png`\n\n"
        "Logo sizing should match the reference creatives, fit inside negative space, preserve clear space, and align to the layout axis. For a carousel, establish a theme-based logo lock before generation: within each approved theme/background family, the official colourway, placement, and optical size are fixed across every logo-bearing slide. For a batch, establish one batch-wide placement-and-size lock: every logo-bearing output uses the exact same placement zone and optical size across all themes/backgrounds, while the official colourway changes only as required by each output background. For a standalone image, use the correct colourway and place the logo to balance that individual layout. Logo-bearing generation must use the correct theme-matched visible logo PNG as actual visual input and must also include an explicit prompt block describing the current Cars24 lockup: rounded-square icon, circular cut-through/open-C mark, and `Cars24` wordmark. Explicitly reject the old boxed `CARS24` logo, all-caps lockups, plaques, badges, redraws, and tile hallucinations. A repo-relative logo path in prompt text is traceability only, never enough by itself. The logo may overlap pattern and may overlap hero only if readable, high-contrast, cleanly fitted, and uncropped. If the active tool cannot attach the logo PNG as true visual input, do not use it for logo-bearing output. If the output changes the logo geometry, drops the icon, alters the wordmark, drifts to all caps, adds a box/tile, or crops the lockup, fail logo QA and regenerate through a visual-input-capable workflow or ask for a supported logo upload. Do not silently overlay the logo afterward.\n"
    )


def replace_line(text: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, replacement, text, flags=re.MULTILINE)
    if count != 1:
        raise ValueError(f"Expected exactly one match for pattern: {pattern}")
    return updated


def build_claude_updated(source_text: str, version: str) -> str:
    updated = source_text
    updated = replace_line(
        updated,
        r"^- `python3 tools/sync_skills\.py` — .*$",
        "- `python3 tools/sync_skills.py` — Canonical repo-native sync command. Regenerates maker-skill + maker-agent mirrors from `master-rules.md`, regenerates the three creative-direction mirrors from `1_References/CREATIVE-DIRECTION.md`, refreshes sync-managed wrapper docs, and validates entry-doc sync/version invariants.",
    )
    updated = replace_line(
        updated,
        r"^The project version is the `version` value in `3_Skills/Global Skills/master-rules\.md` `sync-metadata`\..*$",
        f"The project version is the `version` value in `3_Skills/Global Skills/master-rules.md` `sync-metadata`. Current baseline: `v{version}`.",
    )
    return updated


def validate_contains(text: str, pattern: str, label: str, problems: list[str]) -> None:
    if not re.search(pattern, text, flags=re.MULTILINE):
        problems.append(label)


def validate_entry_docs(version: str, agents_text: str, claude_text: str, readme_text: str) -> list[str]:
    problems: list[str] = []
    validate_contains(
        agents_text,
        rf"^Current mapped version: `v{re.escape(version)}` from `3_Skills/Global Skills/master-rules\.md`\.$",
        "AGENTS.md version line is stale",
        problems,
    )
    validate_contains(
        agents_text,
        r"^To sync rule changes: run `python3 tools/sync_skills\.py`\.$",
        "AGENTS.md canonical sync command is stale",
        problems,
    )
    validate_contains(
        claude_text,
        rf"^The project version is the `version` value in `3_Skills/Global Skills/master-rules\.md` `sync-metadata`\. Current baseline: `v{re.escape(version)}`\.$",
        "CLAUDE.md version line is stale",
        problems,
    )
    validate_contains(
        claude_text,
        r"^- `python3 tools/sync_skills\.py` — Canonical repo-native sync command\..*$",
        "CLAUDE.md sync command description is stale",
        problems,
    )
    validate_contains(
        readme_text,
        r"^- regenerates maker-skill and maker-agent mirrors from `master-rules\.md`$",
        "README.md sync workflow bullets are stale",
        problems,
    )
    validate_contains(
        readme_text,
        r"^- validates key sync/version invariants in `AGENTS\.md`, `CLAUDE\.md`, and `README\.md`$",
        "README.md entry-doc validation note is stale",
        problems,
    )
    return problems


def expected_outputs() -> tuple[dict[Path, str], list[str]]:
    rules_text = read_text(MASTER_RULES)
    creative_text = read_text(CREATIVE_DIRECTION)
    version = extract_version(rules_text)
    outputs: dict[Path, str] = {}
    for path, title in RULE_DERIVED_TARGETS.items():
        outputs[path] = build_rule_derived(title, rules_text)
    for path, description in CREATIVE_DIRECTION_TARGETS.items():
        outputs[path] = build_creative_direction(description, creative_text)
    outputs[SYNC_COMMAND] = build_sync_command()
    outputs[SYNC_ORCHESTRATOR] = build_sync_orchestrator(version)
    outputs[README_MD] = build_readme()
    outputs[AGENTS_MD] = build_agents(version)
    outputs[CLAUDE_MD] = build_claude_updated(read_text(CLAUDE_MD), version)
    entry_problems = validate_entry_docs(
        version,
        outputs[AGENTS_MD],
        outputs[CLAUDE_MD],
        outputs[README_MD],
    )
    return outputs, entry_problems


def run_check() -> int:
    mismatches: list[Path] = []
    outputs, entry_problems = expected_outputs()
    for path, expected in outputs.items():
        actual = read_text(path) if path.exists() else None
        if actual != expected:
            mismatches.append(path)
    if mismatches or entry_problems:
        if mismatches:
            print("Out-of-sync files:")
            for path in mismatches:
                print(path.relative_to(ROOT))
        if entry_problems:
            print("Entry-doc validation failures:")
            for problem in entry_problems:
                print(problem)
        return 1
    print("All generated files are in sync.")
    return 0


def run_write() -> int:
    outputs, entry_problems = expected_outputs()
    for path, expected in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8")
        print(f"Synced {path.relative_to(ROOT)}")
    if entry_problems:
        print("Validated entry-doc invariants after rewrite.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync generated Maker Agent mirrors from source files.")
    parser.add_argument("--check", action="store_true", help="Check whether generated files are in sync.")
    args = parser.parse_args()

    required = [MASTER_RULES, CREATIVE_DIRECTION]
    missing = [path for path in required if not path.exists()]
    if missing:
        print("Missing required source files:", file=sys.stderr)
        for path in missing:
            print(path, file=sys.stderr)
        return 2

    return run_check() if args.check else run_write()


if __name__ == "__main__":
    raise SystemExit(main())
