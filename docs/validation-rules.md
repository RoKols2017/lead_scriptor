[Back to README](../README.md) · [English Version](en/validation-rules.md)

# Правила валидации

## Стадии готовности

- `homework_marketing`
- `custdev`
- `lpr_chain`
- `sales_script`

## Обязательные поля по стадиям

### Marketing

- `product.full_description`
- `product.problem_statement`
- `product.market_type`
- `audience.suspected_core_audience`

### Custdev

- все требования marketing
- `audience.pains` или `audience.needs`
- `product.core_value`

### LPR

- `company.offer`
- `company.industry`
- `sales.target_company_types`
- `sales.target_titles` или `sales.auto_discover_titles=true`

### Sales script

- `company.brand_name`
- `company.offer`
- `sales.outreach_channel`
- `sales.call_goal`
- `tone.language`
- `tone.politeness`

## Примеры противоречий

- `product.market_type=B2B`, но в audience только consumer roles.
- `pricing_model=enterprise` при низком average check без объяснения.
- формальный tone вместе с агрессивно разговорными preferred patterns.

## See Also

- [Правила нормализации](normalization-rules.md) - как заполняются поля
- [Provenance](provenance.md) - какие источники считаются допустимыми
- [Использование](usage.md) - когда запускать validation
