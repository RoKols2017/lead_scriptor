[Back to README](../README.md) · [English Version](en/testing-strategy.md)

# Стратегия тестирования

## Цели покрытия

- Проверки контрактов для всех JSON schemas.
- Smoke checks для pipeline configs и наличия prompt files.
- Regression checks для normalized fixtures и expected readiness results.
- Real interview synthesis fixtures вместе с simulated custdev fixtures.

## Группы фикстур

- `minimal-marketing`
- `custdev-ready`
- `lpr-auto-discover`
- `sales-script-ready`
- `contradiction-b2b-consumer`
- `interview-synthesis-basic`

## Ожидаемые проверки

- readiness stage result
- missing required fields
- weak fields
- contradiction severity
- export profile eligibility

## See Also

- [Оркестрация](orchestration.md) - что проверять по route transitions
- [Run Artifacts](run-artifacts.md) - какие snapshots должны сохраняться
- [Политика эволюции](evolution-policy.md) - как держать тесты в актуальном состоянии
