[Back to README](../README.md) · [English Version](en/legacy-spreadsheet-analysis.md)

# Анализ legacy spreadsheets

## Роль в проекте

- lectures и XLSX-файлы уже используются как references
- они фиксируют domain methodology, а не runtime state

## Сохраняемые паттерны

- chained prompt decomposition
- stage-specific artifacts
- value freezing после генерации

## Отвергнутые паттерны

- formulas как source of truth
- неявная cell coupling
- случайные recalculation costs

## See Also

- [Google Sheets Mapping](google-sheets-mapping.md) - что именно экспортируем
- [Контроль стоимости](cost-safety.md) - почему избегаем формул
- [Карта экспорта](export-mapping.md) - куда уезжают итоговые values
