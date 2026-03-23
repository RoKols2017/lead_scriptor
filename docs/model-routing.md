[Back to README](../README.md) · [English Version](en/model-routing.md)

# Маршрутизация моделей

## Маршруты

- `nano` - extraction, classification, checklist validation.
- `mini` - intake rewrite, normalization support, guided question generation.
- `gpt-5.4` - audience research, custdev synthesis, LPR discovery, script generation и styling.

## Детерминизм

- Модель фиксируется по типу задачи.
- Для structured outputs предпочитается низкая температура.
- Normalized artifacts переиспользуются вместо повторного upstream rerun.

## See Also

- [Контроль стоимости](cost-safety.md) - как экономим токены
- [Оркестрация](orchestration.md) - кто запускает route
- [Testing Strategy](testing-strategy.md) - как проверять стабильность выбора модели
