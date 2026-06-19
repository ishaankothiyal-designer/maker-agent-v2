# Cars24 Maker Agent

Cars24 Maker Agent is a local creative-production system for generating brand-consistent Cars24 copy, prompts, references, and visual outputs.

## Versioning Model

This project uses two layers of versioning:

1. Git history tracks everyday file changes.
2. The Maker Agent product version lives in `3_Skills/Global Skills/master-rules.md` under `sync-metadata.version`.

When rules change, update `master-rules.md` first, then sync generated mirrors and commit the result. Use GitHub releases or tags for meaningful Maker Agent versions such as `v2.23`.

## What Belongs In Git

Track source-of-truth project files:

- `1_References/`
- `2_Agents/`
- `3_Skills/`
- `5_BATCH_EXPORT/`
- `tools/`
- `AGENTS.md`
- `CLAUDE.md`
- `skills-lock.json`

Generated production images in `4_exports/` are intentionally ignored because they are large output history, not the canonical rule source. Keep important final assets in external storage, GitHub Releases, or a separate archive flow.

## Everyday Workflow

1. Make edits locally.
2. Run checks or sync commands if a rule change requires them.
3. Review changes with `git status` and `git diff`.
4. Commit with a short message.
5. Push to GitHub.

Example:

```bash
git status
git add .
git commit -m "Update Maker Agent rule guidance"
git push
```

## Release Workflow

For a meaningful Maker Agent version update:

```bash
git tag v2.23
git push origin v2.23
```

Then create a GitHub Release from that tag and summarize what changed, who it helps, impacted files, and rollback notes.
