[Back to README](../../README.en.md) · [Russian Version](../legacy-spreadsheet-analysis.md)

# Legacy Spreadsheet Analysis

## Role in the Project

- lectures and XLSX files are already-used references
- they capture domain methodology, not runtime state

## Preserved Patterns

- chained prompt decomposition
- stage-specific artifacts
- value freezing after generation

## Rejected Patterns

- formulas as the source of truth
- implicit cell coupling
- accidental recalculation costs

## See Also

- [Google Sheets Mapping](google-sheets-mapping.md) - what exactly gets exported
- [Cost Safety](cost-safety.md) - why formulas are avoided
- [Export Mapping](export-mapping.md) - where final values go
