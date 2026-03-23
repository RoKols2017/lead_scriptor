[Back to README](../README.md)

# Pre-Pilot Readiness Checklist

## Route Contract Checks

For every route in `opencode.json` and `pipelines/*.yaml`, confirm:

- route id matches the pipeline id
- assigned agent exists in `.opencode/agents/`
- `required_inputs` are explicit
- `produces` are explicit
- `blocking_conditions` are explicit
- `resume_from` is explicit
- `export_targets` are explicit or intentionally empty

## Guided Questions Loop

- `inputs/validation/guided-questions.json` exists
- `inputs/raw/followup_answers.md` exists
- blockers map to explicit `field_path` values
- rerun path is `followup_answers -> intake -> validation`

## Export Gate

- `pipelines/export_google_sheets.yaml` remains values-only
- every export profile depends only on its own upstream artifact
- no spreadsheet formulas are introduced into `outputs/`

## Pilot Go/No-Go

- at least one successful downstream route is documented
- at least one blocked route with recovery path is documented
- operator can identify next action from run artifacts and docs alone
