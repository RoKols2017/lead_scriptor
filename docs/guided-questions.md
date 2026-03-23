[Back to README](../README.md) · [English Version](en/guided-questions.md)

# Guided Questions Engine

## Поведение

- Сначала спрашиваем только о blockers.
- Группируем вопросы по блокам Product, Audience, Sales, Tone.
- Один проход ограничен 10 вопросами.
- Пропускаем факты, которые уже зафиксированы в normalized contracts.

## Приоритизация

1. Отсутствующие `required` поля для ближайшей целевой стадии.
2. Противоречия, которые блокируют readiness.
3. Weak fields, снижающие качество output.
4. Recommended enrichment questions только если остался лимит.

## See Also

- [Правила валидации](validation-rules.md) - откуда берутся blockers
- [Использование](usage.md) - как работать с follow-up answers
- [Оркестрация](orchestration.md) - состояние `awaiting_followup`
