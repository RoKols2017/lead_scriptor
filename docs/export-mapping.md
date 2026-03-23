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

## Правила

- Все экспорты сохраняются только как значения.
- Каждый export route зависит только от артефактов своего профиля.
- Ни один export route не должен вводить runtime dependency на Google Sheets.
- Если profile не может быть собран без формулы или пересчета sheet-логики, export должен считаться blocked.

## See Also

- [Использование](usage.md) - когда запускать экспорт
- [Правила валидации](validation-rules.md) - что должно быть готово до экспорта
- [Карта provenance](provenance.md) - откуда берутся экспортируемые данные
