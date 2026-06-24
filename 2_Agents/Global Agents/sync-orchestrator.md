# Sync Orchestrator — Global Agent
> Canonically triggered by `python3 tools/sync_skills.py`. Claude users may also use `/sync-skills` when `.claude/commands/sync-skills.md` is present.

---

## Purpose

The Sync Orchestrator keeps source-of-truth files and repository entry docs aligned whenever the Maker rules change.

## Trigger

Canonical command: `python3 tools/sync_skills.py`
Optional Claude wrapper: `/sync-skills`
Wrapper location: `.claude/commands/sync-skills.md`

## Sync Targets

| Source | Target | Format |
|---|---|---|
| `3_Skills/Global Skills/master-rules.md` | `3_Skills/1_Claude Skills/maker-skill.md` | Claude skill (conversational, tool-aware) |
| `3_Skills/Global Skills/master-rules.md` | `3_Skills/2_Codex Skills/maker-skill.md` | Codex / AGENTS.md (directive, structured) |
| `3_Skills/Global Skills/master-rules.md` | `2_Agents/1_Claude Agents/maker-agent.md` | Claude agent definition |
| `3_Skills/Global Skills/master-rules.md` | `2_Agents/2_Codex Agents/maker-agent.md` | Codex agent definition |
| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/Global Skills/creative-direction.md` | Verbatim mirror (creative direction) |
| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/1_Claude Skills/creative-direction.md` | Verbatim mirror (creative direction) |
| `1_References/CREATIVE-DIRECTION.md` | `3_Skills/2_Codex Skills/creative-direction.md` | Verbatim mirror (creative direction) |
| Sync template in script | `.claude/commands/sync-skills.md` | Claude wrapper doc |
| Sync template in script | `2_Agents/Global Agents/sync-orchestrator.md` | Global sync instructions |

> Two sources of truth: `master-rules.md` (brand/flow rules) → maker-skill + maker-agent files; `1_References/CREATIVE-DIRECTION.md` (creative direction) → the three `creative-direction.md` mirrors. Creative-direction mirrors are byte-verbatim (with a stable auto-generated banner) — never reformatted, so visual rules are never paraphrased.

## Entry-File Checks

`AGENTS.md`, `CLAUDE.md`, and `README.md` are repo-tracked entry docs with some manual sections, so the sync script validates key invariants there instead of rewriting the full files. `--check` fails if those docs drift away from the canonical sync command or current project version.

## Sync Process (executed by `python3 tools/sync_skills.py`)

1. Read both sources: `3_Skills/Global Skills/master-rules.md` and `1_References/CREATIVE-DIRECTION.md`
2. Parse the current project version from the `sync-metadata` block in `master-rules.md`
3. Regenerate from `master-rules.md`:
   - Claude skill → `3_Skills/1_Claude Skills/maker-skill.md`
   - Codex skill → `3_Skills/2_Codex Skills/maker-skill.md`
   - Claude agent → `2_Agents/1_Claude Agents/maker-agent.md`
   - Codex agent → `2_Agents/2_Codex Agents/maker-agent.md`
4. Regenerate from `1_References/CREATIVE-DIRECTION.md` with a deterministic banner and verbatim body
5. Regenerate the wrapper docs: `.claude/commands/sync-skills.md` and `2_Agents/Global Agents/sync-orchestrator.md`
6. Validate entry-doc invariants in `AGENTS.md`, `CLAUDE.md`, and `README.md`
7. Report mismatches in `--check`, or rewrite the sync-managed files in write mode

## Rules for the Sync Agent

- Preserve all brand rules exactly — do not paraphrase or reinterpret
- The master-rules.md `version` value is the repo-level project version. Current baseline: `v2.28`.
- Increment the version number only if rules or persistent workflow behavior have substantively changed
- When the user asks to update the version, update the master-rules.md changelog and summarize what changed since the previous version, which skills/references/agents are impacted, how the change helps users, and rollback considerations
- Never remove a rule — only add or update
- If a conflict is detected (e.g., a rule contradicts another), flag it to the user instead of resolving silently
