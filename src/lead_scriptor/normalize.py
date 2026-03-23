from __future__ import annotations

from pathlib import Path
from typing import Any

from .contracts import empty_contracts
from .extract import bullet_lines, read_raw_inputs


WEAK_PATTERNS = (
    "для всех",
    "любой бизнес",
    "автоматизирует все",
    "дешево",
    "быстро",
    "качественно",
)


def _first_nonempty(lines: list[str], index: int) -> str:
    return lines[index] if index < len(lines) else ""


def normalize_workspace(root: Path) -> tuple[dict[str, dict[str, Any]], list[str]]:
    raw = read_raw_inputs(root / "inputs" / "raw")
    lines = {name: bullet_lines(text) for name, text in raw.items()}
    contracts = empty_contracts()
    weak_fields: list[str] = []

    product = contracts["product"]["product"]
    product["full_description"] = " ".join(lines["product"])
    product["problem_statement"] = _first_nonempty(lines["product"], 2)
    product["solution_statement"] = _first_nonempty(lines["product"], 3)
    product["core_value"] = _first_nonempty(lines["product"], 4)
    product["name"] = _first_nonempty(lines["product"], 0)

    company = contracts["company"]["company"]
    company["description"] = " ".join(lines["company"])
    company["brand_name"] = _first_nonempty(lines["company"], 0)
    company["offer"] = _first_nonempty(lines["company"], 1)

    audience = contracts["audience"]["audience"]
    audience["suspected_core_audience"] = _first_nonempty(lines["audience"], 0)
    audience["pains"] = lines["audience"][2:3] if len(lines["audience"]) > 2 else []
    audience["current_customers"] = lines["audience"][3:4] if len(lines["audience"]) > 3 else []

    tone = contracts["tone"]["tone"]
    if lines["constraints"]:
        tone["language"] = "ru" if "рус" in raw["constraints"].lower() else tone["language"]
    if lines["tone"]:
        tone["preferred_patterns"] = lines["tone"][:1]

    sales = contracts["sales"]["sales"]
    company_text = raw["company"].lower()
    if "b2b" in company_text:
        product["market_type"] = "B2B"
    elif "b2c" in company_text:
        product["market_type"] = "B2C"
    sales["target_company_types"] = ["unknown-company-type"] if product["market_type"] == "B2B" else []
    sales["auto_discover_titles"] = False

    for field_path, value in [
        ("product.full_description", product["full_description"]),
        ("product.problem_statement", product["problem_statement"]),
        ("audience.suspected_core_audience", audience["suspected_core_audience"]),
    ]:
        text = value.lower() if isinstance(value, str) else ""
        if any(pattern in text for pattern in WEAK_PATTERNS):
            weak_fields.append(field_path)

    return contracts, sorted(set(weak_fields))
