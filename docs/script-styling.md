[Back to README](../README.md) · [English Version](en/script-styling.md)

# Стилизация скрипта

- Styling является post-processing stage.
- Он читает base script и tone contract.
- Перед экспортом проверяет banned phrases.
- При необходимости использует interview synthesis для уточнения речевых паттернов.

## See Also

- [Script Generation](script-generation.md) - что именно стилизуется
- [Маршрутизация моделей](model-routing.md) - какая модель отвечает за styling
- [Карта экспорта](export-mapping.md) - куда идет финальный script
