[Back to README](../../README.en.md) · [Russian Version](../usage.md)

# Usage

1. Fill `inputs/raw/*.md` with the initial business context.
2. Trigger the `intake` route defined in `opencode.json` and `pipelines/intake_ingest.yaml`.
3. Review and update `inputs/normalized/*.yaml` as canonical contracts.
4. Trigger `validation` and inspect `inputs/validation/*`.
5. If blocked, generate `inputs/validation/guided-questions.json`, answer in `inputs/raw/followup_answers.md`, then repeat intake and validation.
6. Trigger the needed downstream route from `pipelines/*.yaml` only after readiness is confirmed.
7. Export values to spreadsheet-compatible artifacts if needed.

Google Sheets stays optional and is used only after runtime artifacts already exist.

## See Also

- [Normalization Rules](normalization-rules.md) - how contracts are filled
- [Validation Rules](validation-rules.md) - what blocks routes
- [Export Mapping](export-mapping.md) - how values-only export works
