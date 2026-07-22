# Cars24 Maker Agent

This repository is a Cars24 Maker Agent workspace for copy, image-generation rules, brand references, and export history. It is not a conventional app service with a runtime server to install and boot.

## 5-minute quickstart

```bash
git clone https://github.com/ishaankothiyal-designer/maker-agent-v2.git
cd maker-agent-v2
python3 tools/sync_skills.py
python3 tools/sync_skills.py --check
```

Then:
- open the repo in Codex or Claude
- edit the source-of-truth files, not generated mirrors
- save outputs under `4_exports/`

## Required tooling

- `git`
- `python3`

Image-generation assumptions:
- In Codex, default to Codex ImageGen
- Use Higgsfield only as fallback, or when explicitly requested

## Source of truth

Edit these files directly:
- `3_Skills/Global Skills/master-rules.md`
- `1_References/CREATIVE-DIRECTION.md`

Generated or sync-managed files should not be edited directly:
- `3_Skills/1_Claude Skills/maker-skill.md`
- `3_Skills/2_Codex Skills/maker-skill.md`
- `2_Agents/1_Claude Agents/maker-agent.md`
- `2_Agents/2_Codex Agents/maker-agent.md`
- `3_Skills/*/creative-direction.md`
- `.claude/commands/sync-skills.md`
- `2_Agents/Global Agents/sync-orchestrator.md`

## Sync workflow

Canonical command:

```bash
python3 tools/sync_skills.py
```

Verification:

```bash
python3 tools/sync_skills.py --check
```

What the sync command manages:
- regenerates maker-skill and maker-agent mirrors from `master-rules.md`
- regenerates the three `creative-direction.md` mirrors from `1_References/CREATIVE-DIRECTION.md`
- refreshes the Claude sync wrapper and global sync orchestrator docs
- validates key sync/version invariants in `AGENTS.md`, `CLAUDE.md`, and `README.md`

If you use Claude and the repo includes `.claude/commands/sync-skills.md`, you can also use `/sync-skills`. The Python command is still the canonical workflow.

## Project structure

- `1_References/` — brand references, visual direction, and reference tagging
- `2_Agents/` — generated agent definitions plus global orchestration notes
- `3_Skills/` — source rules plus generated Claude/Codex skill mirrors
- `4_exports/` — generated output history
- `5_BATCH_EXPORT/` — batch spreadsheet template
- `tools/` — repo-native helper scripts

## Export rules

Do not use `4_exports/` as canonical reference-learning input. It is output history, not brand truth.

Every generated output should live under the required three-level structure:

```text
4_exports/{serial}_{brief}_{DD-Mon}/
  v1/
    {item-brief}-v1-image1.[ext]
```

## Batch template

To regenerate the batch-processing spreadsheet:

```bash
python3 tools/build_batch_processing_template.py
```

## Notes for teammates

- This repo works without Claude-specific setup.
- `.claude/commands/` is optional convenience, not a requirement.
- If `python3 tools/sync_skills.py --check` fails, rerun the sync command and review the resulting diff.
