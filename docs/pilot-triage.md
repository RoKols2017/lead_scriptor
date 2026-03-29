[Back to README](../README.md)

# Pilot Triage

## Common blocked states

| Blocked Reason | Meaning | Next Allowed Action |
|----------------|---------|---------------------|
| missing marketing fields | route cannot start because product/audience context is incomplete | generate guided questions and answer in `inputs/raw/followup_answers.md` |
| `sales.target_titles_missing_and_auto_discover_false` | LPR route has no titles and auto-discovery is disabled | either add `sales.target_titles` or set `sales.auto_discover_titles=true` |
| transcript schema failure | interview route input is malformed | fix transcript file in `inputs/interviews/` |
| formula leakage detected | export route found non-value spreadsheet logic | regenerate export from validated JSON artifacts only |

## Failure mode to return path

| Failure Mode | Return To | Why |
|-------------|-----------|-----|
| missing raw business context | `inputs/raw/*.md` | intake must preserve original source meaning |
| unresolved guided question blockers | `inputs/raw/followup_answers.md` | follow-up answers are the only allowed unblock path |
| normalized contract gap | `inputs/normalized/*.yaml` | canonical contract must be corrected before downstream routes |
| transcript issue | `inputs/interviews/` | real interview ingestion is isolated from simulated flows |
| export artifact issue | upstream `outputs/json/*.json` | export cannot invent missing values |

## Route return points

- Intake issues -> return to `inputs/raw/*.md`
- Validation blockers -> return through `guided_questions`
- LPR blocker -> return to `inputs/normalized/sales.yaml`
- Export blocker -> return to upstream route artifact, not Google Sheets

## Operator triage sequence

1. Read `inputs/validation/completeness.json` for route-level blockers.
2. Read `inputs/validation/contradictions.json` for hard conflicts.
3. If blocked, inspect `inputs/validation/guided-questions.json` for the next question batch.
4. Confirm the route contract in `opencode.json` and `pipelines/*.yaml`.
5. Return only to the closest allowed upstream artifact.
