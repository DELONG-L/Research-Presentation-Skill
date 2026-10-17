#!/usr/bin/env python3
"""Package the bilingual interactive examples for GitHub Pages."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def build(destination: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    destination = destination.resolve()
    if destination == root or destination in root.parents:
        raise ValueError("The output directory must not contain the repository")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Use an empty output directory to avoid publishing stale files")
    destination.mkdir(parents=True, exist_ok=True)
    for language in ("", "zh"):
        source = root / "examples" / "demo" / language / "index.html"
        target = destination / language / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(root / "LICENSE", destination / "LICENSE")
    print(f"Packaged English and Chinese examples in {destination}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    build(parser.parse_args().destination)


if __name__ == "__main__":
    main()
