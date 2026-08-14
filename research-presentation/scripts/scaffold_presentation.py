#!/usr/bin/env python3
"""Create a standalone research-presentation directory from bundled templates."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS = SKILL_ROOT / "assets"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "research-presentation"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_revision(path: Path) -> str:
    root = path if path.is_dir() else path.parent
    try:
        revision = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        return f"{revision}{'-dirty' if dirty else ''}"
    except (FileNotFoundError, subprocess.CalledProcessError):
        return "unversioned"


def render(source: Path, destination: Path, replacements: dict[str, str]) -> None:
    text = source.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace("{{" + key + "}}", value)
    destination.write_text(text, encoding="utf-8")


def ensure_output(path: Path, force: bool) -> None:
    known = {
        "index.html",
        "presentation-manifest.yml",
        "LANGUAGE-AUDIT.md",
        "NARRATIVE-CONTRACT.md",
    }
    if path.exists() and any(path.iterdir()) and not force:
        raise SystemExit(f"Refusing to write into non-empty directory: {path}")
    path.mkdir(parents=True, exist_ok=True)
    if force:
        for name in known:
            target = path / name
            if target.is_file() or target.is_symlink():
                target.unlink()
    (path / "assets").mkdir(exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="Evidence-grounded research presentation")
    parser.add_argument("--input-mode", choices=("project", "pdf"), required=True)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--language", default="en")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    source = (args.source or Path.cwd()).expanduser().resolve()
    if args.input_mode == "pdf" and (not source.is_file() or source.suffix.lower() != ".pdf"):
        raise SystemExit("PDF mode requires --source to point to one .pdf file")
    if args.input_mode == "project" and not source.is_dir():
        raise SystemExit("Project mode requires --source to point to a directory")

    output = args.output.expanduser().resolve()
    ensure_output(output, args.force)

    date = datetime.now(timezone.utc).date().isoformat()
    is_project = args.input_mode == "project"
    replacements = {
        "TITLE": args.title,
        "TITLE_HTML": html.escape(args.title),
        "SUBTITLE_HTML": html.escape(args.subtitle),
        "SLUG": slugify(args.title),
        "DATE": date,
        "LANG": html.escape(args.language),
        "INPUT_MODE": args.input_mode,
        "PROJECT_ROOT": str(source) if is_project else "",
        "SOURCE_REVISION": git_revision(source) if is_project else "",
        "PDF_PATH": str(source) if not is_project else "",
        "PDF_SHA256": sha256(source) if not is_project else "",
        "NARRATIVE_REQUIRED": "true" if is_project else "false",
        "NARRATIVE_PATH": "NARRATIVE-CONTRACT.md" if is_project else "",
        "NARRATIVE_STATUS": "draft" if is_project else "not-required",
    }

    render(ASSETS / "html-deck" / "index.html", output / "index.html", replacements)
    render(
        ASSETS / "presentation-manifest.template.yml",
        output / "presentation-manifest.yml",
        replacements,
    )
    shutil.copyfile(ASSETS / "language-audit.template.md", output / "LANGUAGE-AUDIT.md")
    if is_project:
        render(
            ASSETS / "narrative-contract.template.md",
            output / "NARRATIVE-CONTRACT.md",
            replacements,
        )

    print(f"Created {args.input_mode} presentation scaffold at {output}")
    if is_project:
        print("Freeze NARRATIVE-CONTRACT.md before replacing slide placeholders.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
