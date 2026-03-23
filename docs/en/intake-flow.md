[Back to README](../../README.en.md) · [Russian Version](../intake-flow.md)

# Intake Flow

## Stages

1. Read `inputs/raw/*.md`.
2. Extract candidate facts by entity.
3. Attach provenance for each extracted field.
4. Normalize values into canonical contracts.
5. Run completeness and contradiction checks.
6. Generate guided questions only for blockers and weak fields.
7. Save normalized contracts and validation artifacts.

## Logging Expectations

- `INFO` on stage start and finish.
- `DEBUG` for field-level extraction and normalization trace.
- `WARN` for weak fields, contradictions, and missing required inputs.
- `ERROR` for serialization failures or invalid schema shape.

## See Also

- [Normalization Rules](normalization-rules.md) - how the normalization step works
- [Guided Questions](guided-questions.md) - how the follow-up loop is built
- [Run Artifacts](run-artifacts.md) - what gets persisted after a pass
