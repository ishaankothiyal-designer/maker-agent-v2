---
name: "source-command-sync-skills"
description: "Regenerate the tool-specific skill, agent, and creative-direction files from their sources."
---

# source-command-sync-skills

Use this skill when the user asks to run the migrated source command `sync-skills`.

## Command Template

# /sync-skills — propagate sources to generated files

You are running the Cars24 Maker Agent **sync**. There are two sources of truth and several generated files. Regenerate every generated file from its source, preserving rules **exactly** (never paraphrase, never drop a rule).

Follow the orchestrator spec in `2_Agents/Global Agents/sync-orchestrator.md`.

## Source A — `3_Skills/Global Skills/master-rules.md`
Regenerate these four, each in its own format (see Format rules below):
1. `3_Skills/1_Claude Skills/maker-skill.md` — Claude format (conversational, tool-aware)
2. `3_Skills/2_Codex Skills/maker-skill.md` — Codex format (terse, directive)
3. `2_Agents/1_Claude Agents/maker-agent.md` — Claude agent definition
4. `2_Agents/2_Codex Agents/maker-agent.md` — Codex agent definition

## Source B — `1_References/CREATIVE-DIRECTION.md` (single source for creative direction)
Regenerate these three as **verbatim mirrors** (creative rules must not be reworded):
5. `3_Skills/Global Skills/creative-direction.md`
6. `3_Skills/1_Claude Skills/creative-direction.md`
7. `3_Skills/2_Codex Skills/creative-direction.md`

Each mirror = its own frontmatter (`name`, `description`) + an auto-generated banner + a `---` + the **full body of the primary with its frontmatter stripped** (drop the primary's leading 4-line frontmatter; keep all `---` section dividers and everything else byte-for-byte). Banner text:
> ⚙️ **Auto-generated (DATE).** Synced mirror of `1_References/CREATIVE-DIRECTION.md` (single source of truth for creative direction). **Do not edit directly** — edit the primary and run `/sync-skills`. Content is verbatim so brand rules are never paraphrased.

Use the current date for DATE. A reliable way to write each mirror without manual copy is:
```bash
PRIMARY="1_References/CREATIVE-DIRECTION.md"
# write frontmatter + banner + "---\n\n", then: tail -n +5 "$PRIMARY" >> target
```

## Format rules (Source A only)
**Claude format:** markdown headings, tables, code blocks; conversational system-prompt tone; may reference Claude tool-use patterns; include the activation prompt and session flow.
**Codex format:** AGENTS.md-style; numbered/labelled fields; terse, machine-readable; no Claude-specific tool references.

## Hard rules
- Preserve every brand rule exactly — do not paraphrase, reinterpret, or remove. Add/update only.
- The mandatory first-response onboarding prompt must remain byte-identical across all files.
- If two rules conflict, **stop and flag it to the user** — do not resolve silently.
- After writing, update the sync metadata block at the top of `master-rules.md` (`last_updated`; bump version only on substantive rule changes, not cosmetic edits).
- Finish with a short summary listing each of the 7 files and what changed (or "no change").

## Verify before finishing
Confirm no generated file contains: post-headline "Care Sans" (Care Sans is logo-lockup only → headlines are Arapey), a "flat / no-gradient" *composite background* rule (backgrounds are single-hue with a subtle gradient/glow; only isolated pattern PNGs and flat icons are flat), or phantom illustration paths (only `Main_reference.png`, `Frame 2147228886.png`, `Frame 2147228890.png`, `Group.png`, and the `...75910...` two-women file exist).
