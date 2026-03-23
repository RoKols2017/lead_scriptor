[Back to README](../README.md) · [English Version](en/usage.md)

# Использование

1. Заполните `inputs/raw/*.md` исходным бизнес-контекстом.
2. Запустите маршрут `intake`, заданный в `opencode.json` и `pipelines/intake_ingest.yaml`.
3. Проверьте и при необходимости обновите `inputs/normalized/*.yaml` как канонические контракты.
4. Запустите `validation` и проверьте `inputs/validation/*`.
5. Если маршрут заблокирован, сгенерируйте `inputs/validation/guided-questions.json`, ответьте в `inputs/raw/followup_answers.md`, затем повторите intake и validation.
6. Запускайте downstream route из `pipelines/*.yaml` только после подтвержденной readiness.
7. При необходимости экспортируйте результаты в spreadsheet-compatible artifacts.

Google Sheets остается опциональным и используется только после появления runtime artifacts.

## See Also

- [Правила нормализации](normalization-rules.md) - как заполняются контракты
- [Правила валидации](validation-rules.md) - что блокирует маршруты
- [Экспорт](export-mapping.md) - как устроен values-only export
