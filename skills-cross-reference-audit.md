# Skills Cross-Reference Audit

Audit date: 18 Jun 2026  
Workspace: `/Users/a39236/Desktop/maker agent v2`  
Current project baseline: `v2.23` from `3_Skills/Global Skills/master-rules.md`

## Scope

Checked:

- Entry files: `AGENTS.md`, `CLAUDE.md`
- Agent definitions: `2_Agents/**`
- Maker skills and generated mirrors: `3_Skills/**`
- Installed local agent skills: `.agents/skills/**/SKILL.md`
- Reference maps: `1_References/CREATIVE-DIRECTION.md`, `HIGGSFIELD-CONTEXT-PACKAGE.md`, `REFERENCE-ATLAS.md`, `REFERENCE-SKILL-MAP.md`, `reference-index.json`, `reference-tags/`
- Output history: `4_exports/`
- Skill lock: `skills-lock.json`

## Executive Finding

The active Maker output path is:

1. Entry file (`AGENTS.md` or `CLAUDE.md`)
2. Runtime-specific Maker skill and agent definition
3. `master-rules.md` as the rule/version ledger
4. `CREATIVE-DIRECTION.md` as the visual source
5. `reference-index.json` + `reference-tags/` as the first reference-selection layer
6. `REFERENCE-ATLAS.md` and `REFERENCE-SKILL-MAP.md` as human/audit confirmation
7. `HIGGSFIELD-CONTEXT-PACKAGE.md` as provider/reference prompt context
8. Runtime provider: Codex ImageGen by default in Codex; Higgsfield only for explicit, fallback, or non-Codex generation
9. `4_exports/README.md` for export structure and provenance notes

The repo should preserve original skills and assets, but route them clearly. Do not delete legacy logos or upstream Higgsfield skills. Instead, mark their role and attachability so agents do not misuse them.

## Active / Conditional / External

| File or skill | Status | Notes |
|---|---|---|
| `3_Skills/Global Skills/master-rules.md` | Source of truth | Single version ledger and canonical flow rules. |
| `1_References/CREATIVE-DIRECTION.md` | Source of truth | Visual system source. Mirrors are generated from this file. |
| `3_Skills/*/creative-direction.md` | Generated mirrors | Byte-identical mirrors with generated frontmatter/banner. |
| `3_Skills/1_Claude Skills/maker-skill.md` | Active in Claude | Generated surface for Claude. |
| `3_Skills/2_Codex Skills/maker-skill.md` | Active in Codex | Generated surface for Codex. |
| `2_Agents/1_Claude Agents/maker-agent.md` | Active in Claude | Claude runtime route. |
| `2_Agents/2_Codex Agents/maker-agent.md` | Active in Codex | Codex runtime route. |
| `3_Skills/*/founder-voice-skill.md` | Conditional | Used only for write-up paths; runtime-specific paths are now explicit in master rules. |
| `1_References/HIGGSFIELD-CONTEXT-PACKAGE.md` | Active | Loaded during Stage 7 assembly and Stage 8 generation for Codex ImageGen or Higgsfield fallback. |
| `1_References/reference-index.json` + `reference-tags/` | Active | First reference-selection layer. All on-disk reference images/SVGs are indexed as of this audit. |
| `1_References/REFERENCE-ATLAS.md` | Active | Confirms layout/illustration/pattern contents and copy/ignore intent. |
| `1_References/REFERENCE-SKILL-MAP.md` | Active | Confirms brand-guideline attachability and prevents rules-only contamination. |
| `3_Skills/Global Skills/higgsfield-prompt-builder.md` | Active supporting doc | Updated in place to match the current baseline; not a separate source of truth. |
| `.agents/skills/higgsfield-generate/SKILL.md` | External provider utility | Use only for explicit Higgsfield requests, fallback, or non-Codex after Maker Stage 1-9 approval. |
| `.agents/skills/higgsfield-product-photoshoot/SKILL.md` | External non-Maker utility | Keep installed, but do not route normal Maker output through it. |
| `.agents/skills/higgsfield-marketplace-cards/SKILL.md` | External non-Maker utility | Keep installed, but use only for explicit marketplace listing work. |
| `.agents/skills/higgsfield-soul-id/SKILL.md` | External non-Maker utility | Keep installed, but use only for explicit identity-model training tasks. |
| `.agents/skills/source-command-sync-skills/SKILL.md` | Sync utility | Updated to match Claude/Codex format labels. |

## Decisions From Cleanup

- Preserve all logo files. Unsafe/raw generation assets are indexed as preserved legacy/rules-only assets, not deleted.
- Preserve upstream Higgsfield skills. Do not edit their pinned skill files; route them through Maker rules instead.
- Preserve original local Maker docs, but update stale instructions in place.
- `4_exports/README.md` is the export source of truth. Do not create per-run manifests unless explicitly requested.
- `.DS_Store` is ignored for future git use; existing Finder metadata can remain until a separate workspace cleanup.

## Current Known Non-Issues

- `4_exports/` contains historical naming inconsistencies. They should not be renumbered; they are provenance.
- Historical version freeze tarballs are intentionally preserved under `4_exports/_version-freezes/`.
- `skills-lock.json` still lists the full upstream Higgsfield skill set. This is acceptable because Maker routing now limits when those skills apply.

## Verification Checklist For Future Changes

Before finishing any repo-rule update:

- `master-rules.md` top `sync-metadata` version matches `AGENTS.md`, `CLAUDE.md`, and `sync-orchestrator.md`.
- Generated creative-direction mirrors have identical SHA-256 hashes.
- `reference-index.json` includes every on-disk reference image/SVG, with unsafe assets marked non-attachable.
- Codex routing says Codex ImageGen is preview/exploration only, production exports use a project-local file-producing path, and Higgsfield is explicit/fallback/non-Codex.
- Export rules point to `4_exports/README.md`, not per-run manifests.
