[Back to README](../../README.en.md) · [Russian Version](../model-routing.md)

# Model Routing

## Routes

- `nano` - extraction, classification, checklist validation.
- `mini` - intake rewrite, normalization support, guided question generation.
- `gpt-5.4` - audience research, custdev synthesis, LPR discovery, script generation, and styling.

## Determinism

- Fix the model by task type.
- Prefer low temperature for structured outputs.
- Reuse normalized artifacts instead of rerunning upstream prompts.

## See Also

- [Cost Safety](cost-safety.md) - how token spend is controlled
- [Orchestration](orchestration.md) - who triggers each route
- [Testing Strategy](testing-strategy.md) - how route stability is verified
