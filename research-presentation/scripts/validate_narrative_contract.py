#!/usr/bin/env python3
"""Validate the structure and freeze state of NARRATIVE-CONTRACT.md."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_FIELDS = (
    "schema_version",
    "status",
    "input_mode",
    "project_root",
    "source_revision",
    "evidence_cutoff",
)
REQUIRED_SECTIONS = (
    "One-Sentence Pitch",
    "Audience And Purpose",
    "Problem And Deployment Scenario",
    "Trust And Threat Boundary",
    "Research Gap",
    "Method Identity",
    "Novelty Thesis",
    "Primary Claim",
    "Contributions",
    "Claim Boundaries",
    "Evidence Map",
    "Terminology",
    "Storyline",
    "Unresolved Risks",
)
PLACEHOLDERS = ("TODO", "Replace with", "<!--", "Contribution 1", "Story beat 1")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, text[match.end() :]


def sections(body: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##\s+(.+?)\s*$", body, re.MULTILINE))
    result: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        result[match.group(1).strip()] = body[match.end() : end].strip()
    return result


def validate(path: Path, require_frozen: bool) -> tuple[list[str], list[str], dict[str, str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not path.is_file():
        return [f"Contract not found: {path}"], warnings, {}

    text = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(text)
    if not metadata:
        errors.append("Missing YAML-style frontmatter")
    for field in REQUIRED_FIELDS:
        if not metadata.get(field):
            errors.append(f"Missing frontmatter field: {field}")

    if metadata.get("schema_version") != "1":
        errors.append("schema_version must be 1")
    if metadata.get("input_mode") != "project":
        errors.append("Narrative contracts are only valid with input_mode: project")
    status = metadata.get("status")
    if status not in {"draft", "frozen", "stale"}:
        errors.append("status must be draft, frozen, or stale")
    if require_frozen and status != "frozen":
        errors.append("Contract is not frozen")
    if status == "frozen":
        for field in ("confirmed_by", "confirmed_at"):
            if not metadata.get(field):
                errors.append(f"Frozen contract requires {field}")
    elif metadata.get("confirmed_by") or metadata.get("confirmed_at"):
        warnings.append("Non-frozen contract retains confirmation metadata")

    parsed_sections = sections(body)
    for heading in REQUIRED_SECTIONS:
        content = parsed_sections.get(heading, "")
        if not content:
            errors.append(f"Missing or empty section: {heading}")
            continue
        if any(token.lower() in content.lower() for token in PLACEHOLDERS):
            errors.append(f"Unresolved placeholder in section: {heading}")

    return errors, warnings, metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path)
    parser.add_argument("--require-frozen", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    errors, warnings, metadata = validate(args.contract, args.require_frozen)
    result = {
        "path": str(args.contract.resolve()),
        "status": metadata.get("status", "unknown"),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json_output:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for item in errors:
            print(f"[error] {item}")
        for item in warnings:
            print(f"[warning] {item}")
        print(f"[{'ok' if not errors else 'failed'}] {args.contract} ({result['status']})")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
