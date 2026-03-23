from __future__ import annotations

from pathlib import Path


RAW_FILES = {
    "product": "product.md",
    "company": "company.md",
    "audience": "audience.md",
    "tone": "tone.md",
    "constraints": "constraints.md",
}


def read_raw_inputs(raw_dir: Path) -> dict[str, str]:
    payload: dict[str, str] = {}
    for key, filename in RAW_FILES.items():
        path = raw_dir / filename
        payload[key] = path.read_text(encoding="utf-8") if path.exists() else ""
    return payload


def bullet_lines(text: str) -> list[str]:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("- "):
            lines.append(stripped[2:].strip())
        elif not stripped.startswith("#"):
            lines.append(stripped)
    return lines
