#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER_RULES = ROOT / "3_Skills/Global Skills/master-rules.md"
CREATIVE_DIRECTION = ROOT / "1_References/CREATIVE-DIRECTION.md"


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
    date = dt.date.today().isoformat()
    body = strip_frontmatter(source_text).rstrip()
    return (
        "---\n"
        "name: creative-direction\n"
        f"description: {description}\n"
        "---\n\n"
        f"⚙️ **Auto-generated ({date}).** Synced mirror of `1_References/CREATIVE-DIRECTION.md` "
        "(single source of truth for creative direction). **Do not edit directly** — edit the primary "
        "and run `python3 tools/sync_skills.py`. Claude users may also use `/sync-skills` when the "
        "repo wrapper exists. Content is verbatim so brand rules are never paraphrased.\n\n"
        "---\n\n\n"
        f"{body}\n"
    )


def expected_outputs() -> dict[Path, str]:
    rules_text = read_text(MASTER_RULES)
    creative_text = read_text(CREATIVE_DIRECTION)
    outputs: dict[Path, str] = {}
    for path, title in RULE_DERIVED_TARGETS.items():
        outputs[path] = build_rule_derived(title, rules_text)
    for path, description in CREATIVE_DIRECTION_TARGETS.items():
        outputs[path] = build_creative_direction(description, creative_text)
    return outputs


def run_check() -> int:
    mismatches: list[Path] = []
    for path, expected in expected_outputs().items():
        actual = read_text(path) if path.exists() else None
        if actual != expected:
            mismatches.append(path)
    if mismatches:
        print("Out-of-sync files:")
        for path in mismatches:
            print(path.relative_to(ROOT))
        return 1
    print("All generated files are in sync.")
    return 0


def run_write() -> int:
    for path, expected in expected_outputs().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8")
        print(f"Synced {path.relative_to(ROOT)}")
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
