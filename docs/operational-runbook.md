[Back to README](../README.md)

# Operational Runbook

## Pilot entry sequence

1. Confirm the target scenario and expected downstream route.
2. Verify raw input files exist in `inputs/raw/`.
3. Run intake and review normalized contracts.
4. Run validation and inspect blockers.
5. If blocked, use guided questions and collect follow-up answers.
6. Re-run intake and validation.
7. Start the downstream route only after readiness is confirmed.
8. Run export only from validated artifacts.

## Go / No-Go checks

- `inputs/validation/completeness.json` shows the target route in `ready_for`
- no unresolved blocker contradictions remain
- required upstream artifacts exist for the route
- export profile has a matching validated JSON artifact

## No-Go conditions

- route still appears in `blocked_for`
- guided questions remain unanswered for required fields
- transcript input is malformed
- export route would require spreadsheet formulas or missing values

## Operator triage order

1. Check `inputs/validation/completeness.json`
2. Check `inputs/validation/contradictions.json`
3. Check `inputs/validation/guided-questions.json`
4. Check route-specific required inputs in `pipelines/*.yaml`
5. Check `docs/pilot-triage.md`
