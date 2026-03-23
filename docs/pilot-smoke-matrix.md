[Back to README](../README.md)

# Pilot Smoke Matrix

## Scenarios

| Scenario | Input Focus | Expected Route | Expected Status | Key Artifacts |
|----------|-------------|----------------|-----------------|---------------|
| `marketing-ready` | full marketing brief | `homework_marketing` | ready | `outputs/json/marketing-homework.json` |
| `blocked-needs-followup` | incomplete B2B brief | `guided_questions` then rerun | blocked -> rerun | `inputs/validation/guided-questions.json` |
| `custdev-interview-ingest` | product + audience + transcript | `interview_ingest_synthesis` | ready | `outputs/json/interview-synthesis.json` |
| `sales-route-with-export` | LPR-ready sales case | `lpr_discovery -> sales_script_generation -> script_styling -> export_google_sheets` | ready | `outputs/json/sales-script-styled.json` |

## Expected Checks

- route selection matches the scenario intent
- blocked scenarios point to a concrete next action
- rerun scenarios change readiness only after follow-up answers are added
- export scenarios remain values-only
