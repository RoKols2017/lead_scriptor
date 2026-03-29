[Back to README](../README.md) · [English Version](en/google-sheets-mapping.md)

# Маппинг Google Sheets

Google Sheets используется только как target для совместимости.

## Профили экспорта

- `marketing-homework` -> артефакты лекции 1
- `custdev-simulated` -> simulated interview artifacts из лекции 2
- `interview-synthesis` -> findings из transcript clustering
- `lpr-discovery` -> profiles компаний и decision-makers
- `sales-script` -> сырой stage-by-stage script
- `sales-script-styled` -> финальный script text

Каждый профиль экспортирует только значения.

## Листы для сдачи ДЗ

- Лекция 1 -> sheet `Демонстрация`
- Лекция 2 -> sheet `Описание ЦА + CustDev`
- Лекция 2 -> sheet `Определение ЛПР`
- Лекция 2 -> sheet `Генерация скрипта`

## Пакеты сдачи

- `lecture-1-homework.xlsx` -> только `Демонстрация`
- `lecture-2-homework.xlsx` -> три листа лекции 2
- `homework-submission.xlsx` -> все четыре листа в одном values-only workbook

## Источники листов

- `Демонстрация` <- `outputs/json/marketing-homework.json`
- `Описание ЦА + CustDev` <- `outputs/json/custdev-simulated.json` и при наличии `outputs/json/interview-synthesis.json`
- `Определение ЛПР` <- `outputs/json/lpr-discovery.json`
- `Генерация скрипта` <- `outputs/json/sales-script.json` и `outputs/json/sales-script-styled.json`

## See Also

- [Карта экспорта](export-mapping.md) - связь профилей с JSON artifacts
- [Legacy Spreadsheet Analysis](legacy-spreadsheet-analysis.md) - откуда пришла логика таблиц
- [Контроль стоимости](cost-safety.md) - почему формулы запрещены
