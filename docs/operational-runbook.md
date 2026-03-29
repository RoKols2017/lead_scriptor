[Back to README](../README.md)

# Operational Runbook

## Pilot entry sequence

1. Confirm the target scenario and expected downstream route.
2. Verify `opencode.json` points to the correct agent and pipeline for that route.
3. Verify raw input files exist in `inputs/raw/`.
4. Run `intake_ingest`, then `normalize_and_save`, and review normalized contracts.
5. Run `validation` and inspect blockers.
6. If blocked, use `guided_questions` and collect follow-up answers.
7. Re-run `intake_ingest -> normalize_and_save -> validation`.
8. Start the downstream route only after readiness is confirmed.
9. Run export only from validated artifacts.

## Go / No-Go checks

- `inputs/validation/completeness.json` shows the target route in `ready_for`
- no unresolved blocker contradictions remain
- required upstream artifacts exist for the route
- export profile has a matching validated JSON artifact
- route handoff is visible in `runs/latest-run.json`

## No-Go conditions

- route still appears in `blocked_for`
- guided questions remain unanswered for required fields
- transcript input is malformed
- export route would require spreadsheet formulas or missing values
- `opencode.json` and `pipelines/*.yaml` disagree on the route contract

## Operator triage order

1. Check `inputs/validation/completeness.json`
2. Check `inputs/validation/contradictions.json`
3. Check `inputs/validation/guided-questions.json`
4. Check route-specific required inputs in `opencode.json` and `pipelines/*.yaml`
5. Check `docs/pilot-triage.md`

## Export verification

- confirm the profile exists in `pipelines/export_google_sheets.yaml`
- confirm the upstream JSON artifact exists and is complete
- confirm the export is values-only and does not depend on formulas
- confirm the manifest trail remains readable for operators
