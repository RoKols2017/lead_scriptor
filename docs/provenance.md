[Back to README](../README.md) · [English Version](en/provenance.md)

# Provenance

## Источники

- `raw` - напрямую извлечено из пользовательского markdown или transcript input.
- `user_answer` - получено через guided questions после gap analysis.
- `inferred` - осторожный вывод из уже существующих данных, всегда явно помеченный.
- `legacy_sheet` - импортировано из исторических spreadsheet artifacts только для справки.
- `interview_transcript` - нормализовано из реальных интервью.

## Структура provenance record

У каждого сохраненного поля может быть companion provenance record со следующими атрибутами:

- `field_path`
- `source_type`
- `source_ref`
- `confidence`
- `notes`
- `captured_at`

## Правила

- Значения с `inferred` не закрывают молча отсутствующие обязательные бизнес-факты.
- Pipeline outputs не должны затирать provenance, полученный на intake.
- Interview synthesis может предлагать corrections, но не меняет normalized inputs автоматически.

## See Also

- [Правила нормализации](normalization-rules.md) - как значения попадают в контракты
- [Правила валидации](validation-rules.md) - как provenance влияет на readiness
- [Использование](usage.md) - когда появляются follow-up answers
