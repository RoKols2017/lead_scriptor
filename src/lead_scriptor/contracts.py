from __future__ import annotations

from copy import deepcopy
from typing import Any


DEFAULT_CONTRACTS: dict[str, dict[str, Any]] = {
    "product": {
        "product": {
            "name": "",
            "one_liner": "",
            "full_description": "",
            "category": "",
            "market_type": "",
            "problem_statement": "",
            "solution_statement": "",
            "core_value": "",
            "usp_candidates": [],
            "features": [],
            "benefits": [],
            "pricing_model": "",
            "price_range": "",
            "delivery_model": "",
            "geography": [],
            "competitors_known": [],
            "evidence_available": False,
        }
    },
    "company": {
        "company": {
            "brand_name": "",
            "description": "",
            "industry": "",
            "business_model": "",
            "offer": "",
            "deal_type": "",
            "average_check": "",
            "sales_cycle": "",
            "target_regions": [],
            "proof_assets": [],
            "next_step_goal": "",
        }
    },
    "audience": {
        "audience": {
            "suspected_core_audience": "",
            "current_customers": [],
            "buyer_type": "",
            "decision_context": "",
            "languages": [],
            "regions": [],
            "income_level_hint": "",
            "roles_or_professions": [],
            "interests": [],
            "pains": [],
            "fears": [],
            "needs": [],
            "desired_outcomes": [],
        }
    },
    "sales": {
        "sales": {
            "target_company_types": [],
            "target_titles": [],
            "auto_discover_titles": False,
            "desired_lpr_profiles": 3,
            "outreach_channel": "",
            "objection_sensitivity": "",
            "call_goal": "",
            "hard_constraints": [],
        }
    },
    "tone": {
        "tone": {
            "language": "ru",
            "politeness": "formal",
            "person": "2nd",
            "confidence_level": "measured",
            "verbosity": "short",
            "banned_phrases": [],
            "preferred_patterns": [],
            "examples_good": [],
            "examples_bad": [],
        }
    },
    "homework": {
        "homework": {
            "need_marketing_sheet": True,
            "need_custdev_chain": True,
            "need_lpr_chain": True,
            "need_sales_script": True,
            "export_google_sheets_ready": True,
            "replace_formulas_with_values": True,
        }
    },
}


def default_contract(name: str) -> dict[str, Any]:
    return deepcopy(DEFAULT_CONTRACTS[name])


def empty_contracts() -> dict[str, dict[str, Any]]:
    return {name: default_contract(name) for name in DEFAULT_CONTRACTS}
