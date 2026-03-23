from __future__ import annotations

from pathlib import Path


EXPORT_PROFILES = {
    "marketing-homework": [Path("outputs/json/marketing-homework.json")],
    "custdev-simulated": [Path("outputs/json/custdev-simulated.json")],
    "interview-synthesis": [Path("outputs/json/interview-synthesis.json")],
    "lpr-discovery": [Path("outputs/json/lpr-discovery.json")],
    "sales-script": [Path("outputs/json/sales-script.json")],
    "sales-script-styled": [Path("outputs/json/sales-script-styled.json")],
}


def export_eligibility(root: Path) -> dict[str, bool]:
    eligibility: dict[str, bool] = {}
    for profile, required_files in EXPORT_PROFILES.items():
        eligibility[profile] = all((root / path).exists() for path in required_files)
    return eligibility
