[Back to README](../README.md)

# Pilot Triage

## Common blocked states

| Blocked Reason | Meaning | Next Allowed Action |
|----------------|---------|---------------------|
| missing marketing fields | route cannot start because product/audience context is incomplete | generate guided questions and answer in `inputs/raw/followup_answers.md` |
| `sales.target_titles_missing_and_auto_discover_false` | LPR route has no titles and auto-discovery is disabled | either add `sales.target_titles` or set `sales.auto_discover_titles=true` |
| transcript schema failure | interview route input is malformed | fix transcript file in `inputs/interviews/` |
| formula leakage detected | export route found non-value spreadsheet logic | regenerate export from validated JSON artifacts only |

## Route return points

- Intake issues -> return to `inputs/raw/*.md`
- Validation blockers -> return through `guided_questions`
- LPR blocker -> return to `inputs/normalized/sales.yaml`
- Export blocker -> return to upstream route artifact, not Google Sheets
