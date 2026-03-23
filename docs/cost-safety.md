[Back to README](../README.md) · [English Version](en/cost-safety.md)

# Контроль стоимости

- Не используем Google Sheets как runtime execution surface.
- Экспортируем только значения, никогда не формулы.
- Повторно используем normalized contracts и run snapshots.
- Останавливаем guided questions после 10 пунктов за проход.
- Держим структурированные задачи по умолчанию на `nano` и `mini`.

## See Also

- [Маршрутизация моделей](model-routing.md) - какие модели используются
- [Карта экспорта](export-mapping.md) - values-only export
- [Оркестрация](orchestration.md) - где происходят route handoffs
