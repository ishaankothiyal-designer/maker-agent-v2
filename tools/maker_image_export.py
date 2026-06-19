#!/usr/bin/env python3
"""Generate Maker Agent production images directly into 4_exports.

This helper is intentionally project-local. It avoids relying on Codex's
user-level generated image cache, so exported files and chat previews can point
to the same bitmap.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPORT_ROOT = ROOT / "4_exports"
IMAGE_ENDPOINT = "https://api.openai.com/v1/images/generations"


def die(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def slugify(value: str, max_len: int = 30) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    slug = re.sub(r"-+", "-", slug)
    if not slug:
        slug = "maker-export"
    return slug[:max_len].strip("-") or "maker-export"


def run_date(value: str | None) -> str:
    if value:
        return value
    return dt.datetime.now().strftime("%d-%b")


def next_serial(export_root: Path) -> str:
    max_serial = 0
    if export_root.exists():
        for child in export_root.iterdir():
            if child.is_dir():
                match = re.match(r"^(\d{3})_", child.name)
                if match:
                    max_serial = max(max_serial, int(match.group(1)))
    return f"{max_serial + 1:03d}"


def next_version(project_dir: Path) -> str:
    max_version = 0
    if project_dir.exists():
        for child in project_dir.iterdir():
            if child.is_dir():
                match = re.match(r"^v(\d+)$", child.name)
                if match:
                    max_version = max(max_version, int(match.group(1)))
    return f"v{max_version + 1}"


def read_jobs(path: Path) -> list[dict[str, Any]]:
    jobs: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("{"):
            job = json.loads(line)
        else:
            job = {"prompt": line}
        prompt = str(job.get("prompt", "")).strip()
        if not prompt:
            die(f"Missing prompt on line {line_no}")
        jobs.append({"prompt": prompt, **job})
    if not jobs:
        die(f"No jobs found in {path}")
    return jobs


def call_image_api(*, api_key: str, payload: dict[str, Any]) -> bytes:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        IMAGE_ENDPOINT,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        die(f"Image API request failed ({exc.code}): {detail}")
    except urllib.error.URLError as exc:
        die(f"Image API request failed: {exc}")

    try:
        b64 = data["data"][0]["b64_json"]
    except (KeyError, IndexError, TypeError) as exc:
        die(f"Image API response did not include b64_json: {exc}")
    return base64.b64decode(b64)


def resize_if_requested(path: Path, size: str | None) -> None:
    if not size:
        return
    match = re.match(r"^(\d+)x(\d+)$", size)
    if not match:
        die("--resize must use WIDTHxHEIGHT, for example 1000x650")
    width, height = int(match.group(1)), int(match.group(2))
    try:
        from PIL import Image, ImageOps  # type: ignore
    except Exception as exc:
        die(
            "Pillow is required for --resize but is not available in this Python "
            f"environment: {exc}"
        )
    with Image.open(path) as image:
        converted = image.convert("RGB")
        fitted = ImageOps.fit(
            converted,
            (width, height),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        fitted.save(path)


def build_output_dir(args: argparse.Namespace) -> tuple[str, Path]:
    export_root = Path(args.export_root).resolve()
    brief_slug = slugify(args.brief)

    if args.project_dir:
        project_dir = Path(args.project_dir).resolve()
        version = args.version or next_version(project_dir)
    else:
        serial = args.serial or next_serial(export_root)
        project_dir = export_root / f"{serial}_{brief_slug}_{run_date(args.date)}"
        version = args.version or next_version(project_dir)

    return brief_slug, project_dir / version


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate production Maker images directly into 4_exports."
    )
    parser.add_argument("--input", required=True, help="JSONL prompts; one job per line.")
    parser.add_argument("--brief", required=True, help="Brief slug/title for export naming.")
    parser.add_argument("--export-root", default=str(DEFAULT_EXPORT_ROOT))
    parser.add_argument("--project-dir", help="Existing project folder for a new version.")
    parser.add_argument("--serial", help="Override serial, e.g. 025.")
    parser.add_argument("--version", help="Override version folder, e.g. v2.")
    parser.add_argument("--date", help="Override date suffix, e.g. 18-Jun.")
    parser.add_argument("--model", default="gpt-image-2")
    parser.add_argument("--size", default="1536x1024")
    parser.add_argument("--quality", default="medium")
    parser.add_argument("--output-format", default="png")
    parser.add_argument("--resize", help="Optional final crop/resize, e.g. 1000x650.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    jobs = read_jobs(Path(args.input))
    brief_slug, out_dir = build_output_dir(args)
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        die("OPENAI_API_KEY must be set for production export generation.")
    if not args.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for idx, job in enumerate(jobs, 1):
        output_name = job.get("out") or f"{brief_slug}-image{idx}.{args.output_format}"
        output_path = out_dir / Path(str(output_name)).name
        payload = {
            "model": job.get("model", args.model),
            "prompt": job["prompt"],
            "n": 1,
            "size": job.get("size", args.size),
            "quality": job.get("quality", args.quality),
            "output_format": job.get("output_format", args.output_format),
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        print(f"[{idx}/{len(jobs)}] {output_path}", file=sys.stderr)
        if args.dry_run:
            print(json.dumps({"output": str(output_path), "payload": payload}, indent=2))
            continue
        output_path.write_bytes(call_image_api(api_key=api_key or "", payload=payload))
        resize_if_requested(output_path, args.resize)
        written.append(output_path)

    if written:
        print("\nGenerated files:")
        for path in written:
            print(path)
        print("\nChat previews:")
        for path in written:
            print(f"![{path.name}]({path})")


if __name__ == "__main__":
    main()
