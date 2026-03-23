from __future__ import annotations

import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

from .export_profiles import export_eligibility
from .io_utils import dump_json, dump_yaml
from .logging_utils import configure_logging, log_event
from .normalize import normalize_workspace
from .validate import validate_contracts


def run(root: Path) -> int:
    logger = configure_logging()
    log_event(logger, logging.INFO, "runtime_start", root=str(root))

    contracts, weak_fields = normalize_workspace(root)
    log_event(logger, logging.INFO, "normalized_contracts_ready", weak_fields=weak_fields)

    completeness, contradictions, warnings = validate_contracts(contracts, weak_fields)
    log_event(
        logger,
        logging.INFO,
        "validation_ready",
        ready_for=completeness["ready_for"],
        blocked_for=completeness["blocked_for"],
        auto_discover_titles=contracts["sales"]["sales"]["auto_discover_titles"],
    )

    normalized_dir = root / "inputs" / "normalized"
    for name, payload in contracts.items():
        dump_yaml(normalized_dir / f"{name}.yaml", payload)
        log_event(logger, logging.DEBUG, "normalized_written", contract=name)

    dump_json(root / "inputs" / "validation" / "completeness.json", completeness)
    dump_json(root / "inputs" / "validation" / "contradictions.json", contradictions)
    warnings_text = "# Validation Warnings\n\n" + "\n".join(f"- {item}" for item in warnings or ["Пока предупреждений нет."])
    (root / "inputs" / "validation" / "warnings.md").write_text(warnings_text + "\n", encoding="utf-8")

    eligibility = export_eligibility(root)
    dump_json(root / "outputs" / "json" / "export-manifest.json", {"profiles": eligibility, "values_only": True})

    run_payload = {
        "run_id": datetime.now(timezone.utc).strftime("run-%Y%m%dT%H%M%SZ"),
        "stage": "normalize-and-save",
        "input_hash": "raw-markdown-runtime",
        "model_route": "config-first",
        "updated_fields": sorted(completeness["missing_required"]),
        "blockers": completeness["blocked_for"],
        "artifacts": [
            "inputs/normalized/product.yaml",
            "inputs/normalized/company.yaml",
            "inputs/normalized/audience.yaml",
            "inputs/normalized/sales.yaml",
            "inputs/normalized/tone.yaml",
            "inputs/normalized/homework.yaml",
        ],
    }
    dump_json(root / "runs" / "latest-run.json", run_payload)
    log_event(logger, logging.INFO, "runtime_finish", export_profiles=eligibility)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Lead Scriptor runtime scaffold")
    parser.add_argument("command", choices=["run"], nargs="?", default="run")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if args.command == "run":
        return run(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
