#!/usr/bin/env python3
"""Run dependency-free static checks on a standalone HTML presentation."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


REQUIRED_FILES = ("index.html", "presentation-manifest.yml", "LANGUAGE-AUDIT.md")


class DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.anchor_targets: list[str] = []
        self.local_resources: list[str] = []
        self.external_runtime: list[str] = []
        self.slide_count = 0
        self.table_count = 0
        self.table_cell_depth = 0
        self.table_breaks = 0
        self.images_without_alt = 0
        self.unlabelled_buttons = 0
        self.has_viewport = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = {key: value or "" for key, value in attrs}
        if data.get("id"):
            self.ids.append(data["id"])
        classes = set(data.get("class", "").split())
        if tag == "section" and ("slide" in classes or "data-slide" in data):
            self.slide_count += 1
        if tag == "meta" and data.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "table":
            self.table_count += 1
        if tag in {"th", "td"}:
            self.table_cell_depth += 1
        if tag == "br" and self.table_cell_depth:
            self.table_breaks += 1
        if tag == "img" and "alt" not in data:
            self.images_without_alt += 1
        if tag == "button" and not (data.get("aria-label") or data.get("title")):
            self.unlabelled_buttons += 1
        if tag == "a" and data.get("href", "").startswith("#"):
            self.anchor_targets.append(data["href"][1:])

        resource = ""
        if tag in {"img", "script", "source", "video", "audio"}:
            resource = data.get("src", "")
        elif tag == "link" and set(data.get("rel", "").split()) & {"stylesheet", "icon", "preload"}:
            resource = data.get("href", "")
        if resource:
            parsed = urlparse(resource)
            if parsed.scheme in {"http", "https"}:
                self.external_runtime.append(resource)
            elif parsed.scheme not in {"data", "blob"} and not resource.startswith("#"):
                self.local_resources.append(resource)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"th", "td"} and self.table_cell_depth:
            self.table_cell_depth -= 1


def local_path(deck: Path, reference: str) -> Path:
    parsed = urlparse(reference)
    return deck / unquote(parsed.path)


def validate(directory: Path) -> tuple[list[str], list[str], dict[str, int]]:
    errors: list[str] = []
    warnings: list[str] = []
    for name in REQUIRED_FILES:
        if not (directory / name).is_file():
            errors.append(f"Missing required file: {name}")
    if not (directory / "assets").is_dir():
        errors.append("Missing assets directory")
    if errors and not (directory / "index.html").is_file():
        return errors, warnings, {}

    html_text = (directory / "index.html").read_text(encoding="utf-8")
    parser = DeckParser()
    parser.feed(html_text)

    if parser.slide_count < 2:
        errors.append("Presentation must contain at least two <section class=\"slide\"> elements")
    if not parser.has_viewport:
        errors.append("Missing responsive viewport meta tag")
    if parser.external_runtime:
        errors.append("External runtime assets are not allowed: " + ", ".join(parser.external_runtime))
    if parser.table_breaks:
        errors.append(f"Found {parser.table_breaks} <br> element(s) inside table cells")
    if parser.images_without_alt:
        errors.append(f"Found {parser.images_without_alt} image(s) without alt text")
    if parser.unlabelled_buttons:
        errors.append(f"Found {parser.unlabelled_buttons} button(s) without aria-label or title")
    if "data-placeholder" in html_text or "{{" in html_text or re.search(r"\bTODO\b", html_text):
        errors.append("Unresolved presentation placeholder found in index.html")
    if "@media print" not in html_text:
        warnings.append("No print stylesheet found")
    if parser.table_count:
        if not re.search(r"white-space\s*:\s*nowrap", html_text, re.IGNORECASE):
            errors.append("Tables exist but no white-space: nowrap rule was found")
        if not ("nth-child" in html_text or re.search(r"thead[^}]*background", html_text, re.DOTALL)):
            warnings.append("Tables do not appear to use structural row/header shading")

    duplicates = [item for item, count in Counter(parser.ids).items() if count > 1]
    if duplicates:
        errors.append("Duplicate HTML ids: " + ", ".join(sorted(duplicates)))
    missing_anchors = sorted(set(parser.anchor_targets) - set(parser.ids))
    if missing_anchors:
        errors.append("Broken internal anchors: " + ", ".join(missing_anchors))
    for reference in parser.local_resources:
        if not local_path(directory, reference).is_file():
            errors.append(f"Missing local asset: {reference}")

    manifest_path = directory / "presentation-manifest.yml"
    if manifest_path.is_file():
        manifest = manifest_path.read_text(encoding="utf-8")
        for key in ("presentation_id:", "input_mode:", "slides:", "claim_ledger:", "citation_registry:", "asset_registry:"):
            if key not in manifest:
                errors.append(f"Manifest missing key: {key[:-1]}")
        if "{{" in manifest or re.search(r"\bTODO\b", manifest):
            errors.append("Unresolved placeholder found in presentation-manifest.yml")
        manifest_slides = len(re.findall(r"^\s*-\s+number:\s*\d+", manifest, re.MULTILINE))
        if manifest_slides and manifest_slides != parser.slide_count:
            errors.append(
                f"Manifest lists {manifest_slides} slides but HTML contains {parser.slide_count}"
            )

    audit_path = directory / "LANGUAGE-AUDIT.md"
    if audit_path.is_file():
        audit = audit_path.read_text(encoding="utf-8")
        for heading in ("Canonical Terminology", "Claim Strength", "Prohibited Claims", "Final Consistency Check"):
            if f"## {heading}" not in audit:
                errors.append(f"Language audit missing section: {heading}")
        if re.search(r"\bTODO\b", audit):
            errors.append("Unresolved placeholder found in LANGUAGE-AUDIT.md")

    stats = {
        "slides": parser.slide_count,
        "tables": parser.table_count,
        "local_assets": len(parser.local_resources),
        "external_runtime_assets": len(parser.external_runtime),
    }
    return errors, warnings, stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("presentation", type=Path)
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()
    directory = args.presentation.expanduser().resolve()
    if directory.is_file():
        directory = directory.parent

    errors, warnings, stats = validate(directory)
    result = {
        "path": str(directory),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "stats": stats,
    }
    if args.json_output:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for item in errors:
            print(f"[error] {item}")
        for item in warnings:
            print(f"[warning] {item}")
        if stats:
            print(
                f"[summary] slides={stats['slides']} tables={stats['tables']} "
                f"local_assets={stats['local_assets']}"
            )
        print(f"[{'ok' if not errors else 'failed'}] {directory}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
