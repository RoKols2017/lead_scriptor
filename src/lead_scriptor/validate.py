from __future__ import annotations

from typing import Any


def _missing(value: Any) -> bool:
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, list):
        return len(value) == 0
    return value is None


def validate_contracts(contracts: dict[str, dict[str, Any]], weak_fields: list[str]) -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    product = contracts["product"]["product"]
    company = contracts["company"]["company"]
    audience = contracts["audience"]["audience"]
    sales = contracts["sales"]["sales"]
    tone = contracts["tone"]["tone"]

    blockers: dict[str, list[str]] = {
        "homework_marketing": [],
        "custdev": [],
        "lpr_chain": [],
        "sales_script": [],
    }
    warnings: list[str] = []
    contradictions: list[dict[str, Any]] = []

    marketing_required = {
        "product.full_description": product["full_description"],
        "product.problem_statement": product["problem_statement"],
        "product.market_type": product["market_type"],
        "audience.suspected_core_audience": audience["suspected_core_audience"],
    }
    for field_path, value in marketing_required.items():
        if _missing(value):
            blockers["homework_marketing"].append(field_path)

    blockers["custdev"].extend(blockers["homework_marketing"])
    if _missing(product["core_value"]):
        blockers["custdev"].append("product.core_value")
    if _missing(audience["pains"]) and _missing(audience["needs"]):
        blockers["custdev"].append("audience.pains_or_needs")

    for field_path, value in {
        "company.offer": company["offer"],
        "company.industry": company["industry"],
        "sales.target_company_types": sales["target_company_types"],
    }.items():
        if _missing(value):
            blockers["lpr_chain"].append(field_path)
    titles_missing = _missing(sales["target_titles"])
    auto_discover = bool(sales.get("auto_discover_titles", False))
    if titles_missing and not auto_discover:
        blockers["lpr_chain"].append("sales.target_titles_or_auto_discover_titles")

    for field_path, value in {
        "company.brand_name": company["brand_name"],
        "company.offer": company["offer"],
        "sales.outreach_channel": sales["outreach_channel"],
        "sales.call_goal": sales["call_goal"],
        "tone.language": tone["language"],
        "tone.politeness": tone["politeness"],
    }.items():
        if _missing(value):
            blockers["sales_script"].append(field_path)

    if product["market_type"] == "B2B" and not sales["target_company_types"]:
        contradictions.append(
            {
                "rule_id": "b2b_requires_company_targets",
                "severity": "blocker",
                "fields": ["product.market_type", "sales.target_company_types"],
                "message": "B2B product requires target company types for downstream LPR discovery.",
            }
        )

    for field_path in weak_fields:
        warnings.append(f"Weak field detected: {field_path}")

    ready_for = [stage for stage, items in blockers.items() if not items]
    blocked_for = [stage for stage, items in blockers.items() if items]
    completeness = {
        "status": "ready" if not blocked_for else "partial",
        "ready_for": ready_for,
        "blocked_for": blocked_for,
        "missing_required": sorted({item for items in blockers.values() for item in items}),
        "weak_fields": weak_fields,
        "notes": warnings,
    }
    contradiction_report = {
        "status": "blocker" if contradictions else "clear",
        "items": contradictions,
    }
    return completeness, contradiction_report, warnings
