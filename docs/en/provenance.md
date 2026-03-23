[Back to README](../../README.en.md) · [Russian Version](../provenance.md)

# Provenance

## Sources

- `raw` - directly extracted from user-authored markdown or transcript input.
- `user_answer` - collected through guided questions after gap analysis.
- `inferred` - conservative derivation from existing data, always marked explicitly.
- `legacy_sheet` - imported from historic spreadsheet artifacts for reference only.
- `interview_transcript` - normalized from real interview transcripts.

## Provenance Record Shape

Each stored field may have a companion provenance record with:

- `field_path`
- `source_type`
- `source_ref`
- `confidence`
- `notes`
- `captured_at`

## Rules

- `inferred` values never satisfy missing required business facts silently.
- Pipeline outputs must not overwrite provenance from intake.
- Interview synthesis may suggest corrections but does not mutate normalized inputs automatically.

## See Also

- [Normalization Rules](normalization-rules.md) - how values enter contracts
- [Validation Rules](validation-rules.md) - how provenance affects readiness
- [Usage](usage.md) - when follow-up answers appear
