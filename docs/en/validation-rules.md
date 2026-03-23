[Back to README](../../README.en.md) · [Russian Version](../validation-rules.md)

# Validation Rules

## Readiness Stages

- `homework_marketing`
- `custdev`
- `lpr_chain`
- `sales_script`

## Required Fields by Stage

### Marketing

- `product.full_description`
- `product.problem_statement`
- `product.market_type`
- `audience.suspected_core_audience`

### Custdev

- all marketing requirements
- `audience.pains` or `audience.needs`
- `product.core_value`

### LPR

- `company.offer`
- `company.industry`
- `sales.target_company_types`
- `sales.target_titles` or `sales.auto_discover_titles=true`

### Sales Script

- `company.brand_name`
- `company.offer`
- `sales.outreach_channel`
- `sales.call_goal`
- `tone.language`
- `tone.politeness`

## Contradiction Examples

- `product.market_type=B2B` with only consumer roles in audience.
- `pricing_model=enterprise` with a low average check and no explanation.
- formal tone with aggressively conversational preferred patterns.

## See Also

- [Normalization Rules](normalization-rules.md) - how fields are filled
- [Provenance](provenance.md) - acceptable sources
- [Usage](usage.md) - when to trigger validation
