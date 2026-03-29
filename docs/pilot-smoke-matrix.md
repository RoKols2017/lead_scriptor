[Back to README](../README.md)

# Pilot Smoke Matrix

## Scenarios

| Scenario | Input Focus | Expected Route | Expected Status | Key Artifacts |
|----------|-------------|----------------|-----------------|---------------|
| `marketing-ready` | full marketing brief | `intake_ingest -> normalize_and_save -> validation -> homework_marketing` | ready | `inputs/validation/completeness.json`, `outputs/json/marketing-homework.json` |
| `blocked-needs-followup` | incomplete B2B brief without titles | `intake_ingest -> normalize_and_save -> validation -> guided_questions` then rerun | blocked -> rerun | `inputs/validation/guided-questions.json`, `inputs/raw/followup_answers.md` |
| `custdev-interview-ingest` | product + audience + transcript | `interview_ingest_synthesis` | ready | `outputs/json/interview-synthesis.json` |
| `sales-route-with-export` | LPR-ready sales case | `lpr_discovery -> sales_script_generation -> script_styling -> export_google_sheets` | ready | `outputs/json/sales-script-styled.json`, `outputs/xlsx/sales-script-styled.xlsx` |

## Scenario Details

### `marketing-ready`

- Inputs: complete `inputs/raw/*.md` marketing brief
- Expected readiness: `ready_for` includes `homework_marketing`
- Export expectation: optional values-only marketing export only after artifact generation

### `blocked-needs-followup`

- Inputs: B2B brief with missing `company.industry`, `sales.target_titles`, and `sales.call_goal`
- Expected readiness: `blocked_for` includes `lpr_chain` and `sales_script`
- Recovery: guided questions ask for exact blocker fields, then rerun intake and validation

### `custdev-interview-ingest`

- Inputs: transcript files in `inputs/interviews/` plus validated product/audience contracts
- Expected readiness: interview synthesis may run independently from simulated custdev flow
- Recovery: malformed transcripts return to `inputs/interviews/`, not to downstream routes

### `sales-route-with-export`

- Inputs: validated sales contracts, LPR output, and tone contract
- Expected readiness: downstream sales routes run in strict order, export stays values-only
- Export expectation: preserve manifest linkage from JSON artifact to CSV/XLSX output

## Expected Checks

- route selection matches the scenario intent
- blocked scenarios point to a concrete next action
- rerun scenarios change readiness only after follow-up answers are added
- export scenarios remain values-only
- no scenario depends on spreadsheet formulas as runtime behavior
