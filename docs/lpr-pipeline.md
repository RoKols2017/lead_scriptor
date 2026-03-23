[Back to README](../README.md) · [English Version](en/lpr-pipeline.md)

# Pipeline поиска ЛПР

- Стартует только от validated product, company и sales context.
- Сначала строит target company profiles.
- Затем находит до `sales.desired_lpr_profiles` decision-maker profiles.
- Auto-discovery должностей допустим только при `sales.auto_discover_titles=true`.

## See Also

- [Правила валидации](validation-rules.md) - когда route считается ready
- [Script Generation](script-generation.md) - что использует LPR output дальше
- [Interview Ingestion](interview-ingestion.md) - как real interviews влияют на profiles
