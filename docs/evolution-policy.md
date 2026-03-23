[Back to README](../README.md) · [English Version](en/evolution-policy.md)

# Политика эволюции

- Новые поля добавляются только через обновление схем и документации.
- По возможности сохраняется backward compatibility.
- Правила нормализации версионируются, если меняется логика weak-patterns.
- Prompts не должны становиться скрытым source of truth для схем.

## See Also

- [Правила нормализации](normalization-rules.md) - как меняется поведение полей
- [Стратегия тестирования](testing-strategy.md) - как ловить regressions
- [Security Notes](security-notes.md) - что проверять при изменениях
