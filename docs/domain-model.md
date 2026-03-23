[Back to README](../README.md) · [English Version](en/domain-model.md)

# Доменная модель

## Основные сущности

- `product` - что продается, какую проблему решает и какую ценность создает.
- `company` - кто продает, в каком рыночном контексте и с каким offer.
- `audience` - кто покупает, какие боли, потребности и outcomes важны.
- `sales` - outreach strategy, target company types, target titles, call goal и hard constraints.
- `tone` - язык, вежливость, уверенность, banned phrases и preferred patterns.
- `homework` - флаги для lecture-derived routes и export expectations.

## Контракты стадий

- `raw` хранит пользовательский свободный ввод.
- `normalized` хранит machine-readable contracts.
- `validation` хранит readiness, blockers, contradictions и weak fields.
- `runs` хранит execution metadata и stage outputs.

## Семейства pipeline

- Marketing homework pipeline - артефакты из лекции 1.
- Simulated custdev pipeline - avatar-driven интервью из лекции 2.
- Real interview synthesis pipeline - transcript ingestion и correction proposals.
- LPR discovery pipeline - target company и decision-maker discovery.
- Sales script pipeline - генерация script blocks.
- Script styling pipeline - tone adaptation и финальный export shape.

## Правила контрактов

- Downstream pipelines читают только normalized contracts.
- Отсутствующие `required` поля блокируют выполнение.
- `recommended` gaps дают warnings, а не hard blockers.
- Любое inferred value должно нести явный provenance.

## See Also

- [Provenance](provenance.md) - происхождение данных
- [Правила валидации](validation-rules.md) - что считается blocker
- [Оркестрация](orchestration.md) - как сущности движутся по стадиям
