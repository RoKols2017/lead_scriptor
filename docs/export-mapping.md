[Back to README](../README.md) · [English Version](en/export-mapping.md)

# Карта экспорта

Google Sheets остается только слоем совместимости для импорта и экспорта.

## Профили экспорта

- `marketing-homework` -> `outputs/json/marketing-homework.json` -> безопасный value-based export
- `custdev-simulated` -> `outputs/json/custdev-simulated.json` -> безопасный value-based export
- `interview-synthesis` -> `outputs/json/interview-synthesis.json` -> безопасный value-based export
- `lpr-discovery` -> `outputs/json/lpr-discovery.json` -> безопасный value-based export
- `sales-script` -> `outputs/json/sales-script.json` -> безопасный value-based export
- `sales-script-styled` -> `outputs/json/sales-script-styled.json` -> безопасный value-based export

## Submission-ready пакеты

- `lecture-1-homework` -> `outputs/xlsx/lecture-1-homework.xlsx`
  - sheet `Демонстрация`
  - источник: `marketing-homework`
- `lecture-2-homework` -> `outputs/xlsx/lecture-2-homework.xlsx`
  - sheet `Описание ЦА + CustDev`
  - источники: `custdev-simulated`, опционально `interview-synthesis`
  - sheet `Определение ЛПР`
  - источник: `lpr-discovery`
  - sheet `Генерация скрипта`
  - источники: `sales-script`, `sales-script-styled`
- `full-homework-submission` -> `outputs/xlsx/homework-submission.xlsx`
  - объединяет листы лекции 1 и лекции 2 в один values-only workbook

## Правила

- Все экспорты сохраняются только как значения.
- Каждый export route зависит только от артефактов своего профиля.
- Ни один export route не должен вводить runtime dependency на Google Sheets.
- Если profile не может быть собран без формулы или пересчета sheet-логики, export должен считаться blocked.
- Submission workbook собирается только из уже сгенерированных JSON artifacts, а не из промежуточных spreadsheet расчетов.

## Manifest trail

- `outputs/json/export-manifest.json` остается точкой связи между pipeline artifacts и spreadsheet-compatible outputs.
- Export profile должен быть трассируем обратно к своему upstream JSON artifact.
- Оператор должен понимать, какой route произвел экспортируемый результат, без чтения spreadsheet formulas.
- Submission package должен позволять отдельно сдавать лекцию 1, отдельно лекцию 2, либо собирать единый workbook.

## See Also

- [Использование](usage.md) - когда запускать экспорт
- [Правила валидации](validation-rules.md) - что должно быть готово до экспорта
- [Карта provenance](provenance.md) - откуда берутся экспортируемые данные
