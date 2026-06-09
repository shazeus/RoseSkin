#!/usr/bin/env python3
"""Summarize RoseSkin fork asset coverage without modifying files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESOURCES_DIR = ROOT / "resources"
SKINS_DIR = ROOT / "skins"


def count_files(pattern: str) -> int:
    return sum(1 for _ in SKINS_DIR.rglob(pattern))


def load_locale_files() -> dict[str, int]:
    locale_counts: dict[str, int] = {}
    for path in sorted(RESOURCES_DIR.glob("*/skin_ids.json")):
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        locale_counts[path.parent.name] = len(data)
    return locale_counts


def main() -> int:
    locale_counts = load_locale_files()
    champion_dirs = [path for path in SKINS_DIR.iterdir() if path.is_dir()]
    skin_dirs = [path for path in SKINS_DIR.rglob("*") if path.is_dir() and path.parent != SKINS_DIR]

    print("RoseSkin fork inventory")
    print(f"  champions: {len(champion_dirs)}")
    print(f"  skin directories: {len(skin_dirs)}")
    print(f"  rse packages: {count_files('*.rse')}")
    print(f"  preview images: {count_files('*.png')}")
    print(f"  locale files: {len(locale_counts)}")

    if locale_counts:
        largest = max(locale_counts.values())
        smallest = min(locale_counts.values())
        print(f"  locale entries: {smallest}..{largest}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
