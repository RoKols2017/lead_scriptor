[Back to README](../README.md) · [English Version](en/run-artifacts.md)

# Артефакты запуска

Каждый run должен сохранять:

- `run_id`
- input hash
- triggered stage или pipeline
- model route used
- updated fields
- blocker summary
- output artifact list

Runs являются append-only snapshots. Они не мутируют raw input.

## See Also

- [Оркестрация](orchestration.md) - когда обновляется run state
- [Карта provenance](provenance.md) - что сохранять для traceability
- [Testing Strategy](testing-strategy.md) - какие run artifacts проверять в regression
