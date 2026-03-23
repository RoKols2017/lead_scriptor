[Back to README](../../README.en.md) · [Russian Version](../lpr-pipeline.md)

# LPR Discovery Pipeline

- Starts only from validated product, company, and sales context.
- Builds target company profiles first.
- Then discovers up to `sales.desired_lpr_profiles` decision-maker profiles.
- Title auto-discovery is allowed only when `sales.auto_discover_titles=true`.

## See Also

- [Validation Rules](validation-rules.md) - when the route is considered ready
- [Script Generation](script-generation.md) - what consumes LPR output next
- [Interview Ingestion](interview-ingestion.md) - how real interviews affect profiles
