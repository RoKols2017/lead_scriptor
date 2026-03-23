[Back to README](../README.md) · [English Version](en/security-notes.md)

# Заметки по безопасности

- External skills и prompt bundles должны проходить review на prompt injection.
- Interview transcripts могут содержать чувствительные business data и должны считаться restricted inputs.
- Экспортируйте только value-based artifacts, чтобы избежать скрытого recalculation behavior в spreadsheet tools.

## See Also

- [Карта provenance](provenance.md) - какие источники требуют осторожности
- [Политика эволюции](evolution-policy.md) - как вносить изменения без скрытых рисков
- [Контроль стоимости](cost-safety.md) - как избежать лишних пересчетов
