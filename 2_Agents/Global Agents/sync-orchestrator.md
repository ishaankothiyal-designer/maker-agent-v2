# Sync Orchestrator — Global Agent
> Triggered by `/sync-skills`. Reads master-rules.md and updates both Claude and Codex skill files in parallel.

---

## Purpose

The Sync Orchestrator ensures that any change made to `3_Skills/Global Skills/master-rules.md` is immediately reflected in both tool-specific skill files. It runs as two parallel subagents — one for Claude, one for Codex — so both are updated simultaneously.

## Trigger

Slash command: `/sync-skills`
Location of command definition: `.claude/commands/sync-skills.md`

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

> Two sources of truth: `master-rules.md` (brand/flow rules) → maker-skill + maker-agent files; `1_References/CREATIVE-DIRECTION.md` (creative direction) → the three `creative-direction.md` mirrors. Creative-direction mirrors are byte-verbatim (with an auto-generated banner) — never reformatted, so visual rules are never paraphrased.

## Format Differences

### Claude Format
- Written as a conversational system prompt
- Uses markdown headings, tables, and code blocks
- References Claude tool use patterns where relevant
- Includes activation phrase and session flow
- Tone: instructional but natural

### Codex Format
- Written as a directive AGENTS.md-style spec
- Structured as numbered/labelled fields
- No Claude-specific tool references
- Tone: terse, machine-readable where possible
- Filename: maker-skill.md (used as context file by Codex)

## Sync Process (executed by `/sync-skills`)

1. Read both sources: `3_Skills/Global Skills/master-rules.md` and `1_References/CREATIVE-DIRECTION.md`
2. Regenerate from `master-rules.md` (format per table):
   - **Agent A**: Claude format → `3_Skills/1_Claude Skills/maker-skill.md`
   - **Agent B**: Codex format → `3_Skills/2_Codex Skills/maker-skill.md`
   - **Agent C**: Claude agent → `2_Agents/1_Claude Agents/maker-agent.md`
   - **Agent D**: Codex agent → `2_Agents/2_Codex Agents/maker-agent.md`
3. Regenerate from `1_References/CREATIVE-DIRECTION.md` — write each of the three `creative-direction.md` mirrors as: own frontmatter + auto-generated banner + `---` + `tail -n +5` of the primary (verbatim body, frontmatter stripped).
4. Confirm all seven files updated with a summary of changes (or "no change" per file)

## Rules for the Sync Agent

- Preserve all brand rules exactly — do not paraphrase or reinterpret
- Update the "last_updated" date in the sync metadata block of master-rules.md
- The master-rules.md `version` value is the repo-level project version. Current baseline: `v2.8`.
- Increment the version number only if rules have substantively changed (not cosmetic edits)
- When the user asks to update the version, update the master-rules.md changelog and summarize what changed since the previous version, which skills/references/agents are impacted, how the change helps users, and rollback considerations.
- Never remove a rule — only add or update
- If a conflict is detected (e.g., a rule contradicts another), flag it to the user instead of resolving silently
