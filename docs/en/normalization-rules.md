[Back to README](../../README.en.md) · [Russian Version](../normalization-rules.md)

# Normalization Rules

## Core Principles

- Normalize conservatively.
- Prefer an empty string or empty array over invented content.
- Mark ambiguous input as weak if it cannot be validated.
- Keep `inferred` provenance explicit.

## Weak Patterns

- `для всех`
- `любой бизнес`
- `автоматизирует все`
- `дешево`, `быстро`, `качественно` without measurable detail

## Field Notes

- `product.market_type` accepts only `B2B`, `B2C`, `B2B2C`.
- `sales.auto_discover_titles=true` is allowed only when titles are unknown and company type is known.
- `tone` fields affect styling but do not rewrite validated business facts.

## See Also

- [Usage](usage.md) - workflow order
- [Validation Rules](validation-rules.md) - how readiness depends on fields
- [Provenance](provenance.md) - where values come from
