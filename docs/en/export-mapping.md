[Back to README](../../README.en.md) · [Russian Version](../export-mapping.md)

# Export Mapping

Google Sheets remains an import/export compatibility layer only.

## Export Profiles

- `marketing-homework` -> `outputs/json/marketing-homework.json` -> spreadsheet-safe value export
- `custdev-simulated` -> `outputs/json/custdev-simulated.json` -> spreadsheet-safe value export
- `interview-synthesis` -> `outputs/json/interview-synthesis.json` -> spreadsheet-safe value export
- `lpr-discovery` -> `outputs/json/lpr-discovery.json` -> spreadsheet-safe value export
- `sales-script` -> `outputs/json/sales-script.json` -> spreadsheet-safe value export
- `sales-script-styled` -> `outputs/json/sales-script-styled.json` -> spreadsheet-safe value export

## Rules

- All exports are value-based only.
- Each export route depends only on artifacts required by its own profile.
- No export route may introduce a runtime dependency on Google Sheets.

## See Also

- [Usage](usage.md) - when to trigger export
- [Validation Rules](validation-rules.md) - what must be ready before export
- [Provenance](provenance.md) - where exported data comes from
