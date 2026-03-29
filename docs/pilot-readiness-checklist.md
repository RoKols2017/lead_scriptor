[Back to README](../README.md)

# Pre-Pilot Readiness Checklist

## Audit Status

### Aligned

- `.ai-factory/DESCRIPTION.md` and `.ai-factory/ARCHITECTURE.md` define a declarative, agent-driven architecture.
- `.opencode/agents/*.md` keep agent count moderate and responsibilities separated.
- `schemas/*.json`, `pipelines/*.yaml`, `prompts/`, `inputs/`, and `docs/` already exist as the main workflow surface.
- `sales.auto_discover_titles` is present in the normalized sales contract, sales schema, validation docs, validator rules, and LPR pipeline blocking logic.

### Drifted

- `src/lead_scriptor/*.py` is support code only and must not become the primary workflow surface.
- `tests/test_runtime.py` verifies support runtime behavior, not the full OpenCode-native declarative workflow.

### Missing Before This Checkpoint

- `opencode.json` was missing even though docs and routes depended on it.
- Route-level audit detail was too implicit for pre-pilot review.

## Route Contract Checks

For every route in `opencode.json` and `pipelines/*.yaml`, confirm:

- route id matches the pipeline id
- assigned agent exists in `.opencode/agents/`
- `required_inputs` are explicit
- `produces` are explicit
- `blocking_conditions` are explicit
- `resume_from` is explicit
- `export_targets` are explicit or intentionally empty

## Route Matrix

| Route | Agent | Ready Gate | Produces | Main Blockers |
|------|-------|------------|----------|---------------|
| `intake_ingest` | `intake` | raw files present | `runs/intake-ingest.json` | missing raw inputs |
| `normalize_and_save` | `intake` | intake payload exists | `inputs/normalized/*.yaml`, `runs/latest-run.json` | intake payload missing |
| `validation` | `validator` | normalized contracts present | `inputs/validation/*` | normalized contract missing |
| `guided_questions` | `intake` | blockers or weak fields exist | `inputs/validation/guided-questions.json` | no blockers or weak fields |
| `homework_marketing` | `researcher` | `ready_for` contains `homework_marketing` | marketing homework artifacts | marketing required fields missing |
| `homework_custdev_simulated` | `interviewer` | `ready_for` contains `custdev` | simulated custdev artifacts | `product.core_value`, `audience.pains_or_needs` |
| `interview_ingest_synthesis` | `interviewer` | transcript files present | interview synthesis artifacts | no valid transcripts, schema failure |
| `lpr_discovery` | `sales-architect` | `ready_for` contains `lpr_chain` | LPR artifacts | `company.offer`, `company.industry`, `sales.target_company_types`, `sales.target_titles_or_auto_discover_titles` |
| `sales_script_generation` | `sales-architect` | `ready_for` contains `sales_script` | sales script artifacts | missing LPR output or sales/tone fields |
| `script_styling` | `sales-architect` | base script exists | styled script artifacts | base script missing, tone incomplete |
| `export_google_sheets` | `validator` | export artifact exists | values-only CSV/XLSX | missing required artifact, formula leakage |
| `expert_mode` | orchestration wrapper | validation report exists | route handoff in `runs/latest-run.json` | selected route not ready |

## Guided Questions Loop

- `inputs/validation/guided-questions.json` exists
- `inputs/raw/followup_answers.md` exists
- blockers map to explicit `field_path` values
- rerun path is `followup_answers -> intake -> validation`
- no pass contains more than 10 questions
- LPR blocker handling preserves the choice between `sales.target_titles` and `sales.auto_discover_titles=true`

## Export Gate

- `pipelines/export_google_sheets.yaml` remains values-only
- every export profile depends only on its own upstream artifact
- no spreadsheet formulas are introduced into `outputs/`

## Pilot Go/No-Go

- at least one successful downstream route is documented
- at least one blocked route with recovery path is documented
- operator can identify next action from run artifacts and docs alone
- `opencode.json` points to existing agents and pipelines only
