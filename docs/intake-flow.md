[Back to README](../README.md) · [English Version](en/intake-flow.md)

# Intake Flow

## Стадии

1. Читаем `inputs/raw/*.md`.
2. Извлекаем candidate facts по сущностям.
3. Добавляем provenance для каждого извлеченного поля.
4. Нормализуем значения в canonical contracts.
5. Запускаем completeness и contradiction checks.
6. Генерируем guided questions только для blockers и weak fields.
7. Сохраняем normalized contracts и validation artifacts.

## Ожидания по логированию

- `INFO` на старт и завершение стадии.
- `DEBUG` для field-level extraction и normalization trace.
- `WARN` для weak fields, contradictions и missing required inputs.
- `ERROR` для serialization failures или invalid schema shape.

## See Also

- [Правила нормализации](normalization-rules.md) - как выглядит normalization step
- [Guided Questions](guided-questions.md) - как строится follow-up loop
- [Run Artifacts](run-artifacts.md) - что сохраняется по результату прохода
