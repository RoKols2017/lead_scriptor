[Back to README](../README.md) · [English Version](en/usage.md)

# Использование

1. Заполните `inputs/raw/*.md` исходным бизнес-контекстом.
2. Запустите `intake_ingest`, заданный в `opencode.json` и `pipelines/intake_ingest.yaml`.
3. Запустите `normalize_and_save`, чтобы сохранить канонические контракты в `inputs/normalized/*.yaml`.
4. Запустите `validation` и проверьте `inputs/validation/*`.
5. Если маршрут заблокирован, сгенерируйте `inputs/validation/guided-questions.json`, ответьте в `inputs/raw/followup_answers.md`, затем повторите `intake_ingest -> normalize_and_save -> validation`.
6. Запускайте downstream route из `pipelines/*.yaml` только после подтвержденной readiness.
7. Используйте `expert_mode` только как orchestration wrapper, а не как mega-pipeline.
8. Для сдачи ДЗ экспортируйте либо `lecture-1-homework`, либо `lecture-2-homework`, либо единый `full-homework-submission`.
9. Для повторного использования сохраняйте normalized contracts, validation reports и run artifacts как source of truth, а Google Sheets используйте только как deliverable.

Google Sheets остается опциональным и используется только после появления validated downstream artifacts.

## See Also

- [Правила нормализации](normalization-rules.md) - как заполняются контракты
- [Правила валидации](validation-rules.md) - что блокирует маршруты
- [Экспорт](export-mapping.md) - как устроен values-only export
