[Back to README](../../README.en.md) · [Russian Version](../run-artifacts.md)

# Run Artifacts

Each run should persist:

- `run_id`
- input hash
- triggered stage or pipeline
- model route used
- updated fields
- blocker summary
- output artifact list

Runs are append-only snapshots. They do not mutate raw input.

## See Also

- [Orchestration](orchestration.md) - when run state is updated
- [Provenance](provenance.md) - what to keep for traceability
- [Testing Strategy](testing-strategy.md) - which run artifacts to verify in regression
