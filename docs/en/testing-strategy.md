[Back to README](../../README.en.md) · [Russian Version](../testing-strategy.md)

# Testing Strategy

## Coverage Targets

- Contract checks for all JSON schemas.
- Smoke checks for pipeline configs and prompt file presence.
- Regression checks for normalized fixtures and expected readiness results.
- Real interview synthesis fixtures alongside simulated custdev fixtures.

## Fixture Groups

- `minimal-marketing`
- `custdev-ready`
- `lpr-auto-discover`
- `sales-script-ready`
- `contradiction-b2b-consumer`
- `interview-synthesis-basic`

## Expected Assertions

- readiness stage result
- missing required fields
- weak fields
- contradiction severity
- export profile eligibility

## See Also

- [Orchestration](orchestration.md) - which route transitions to verify
- [Run Artifacts](run-artifacts.md) - which snapshots must persist
- [Evolution Policy](evolution-policy.md) - how to keep tests current
