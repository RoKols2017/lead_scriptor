[Back to README](../../README.en.md) · [Russian Version](../guided-questions.md)

# Guided Questions Engine

## Behavior

- Ask about blockers first.
- Group questions by Product, Audience, Sales, and Tone.
- Limit one pass to 10 questions.
- Skip facts already captured in normalized contracts.

## Prioritization

1. Missing `required` fields for the nearest target stage.
2. Contradictions that block readiness.
3. Weak fields that reduce output quality.
4. Recommended enrichment questions only if budget remains.

## See Also

- [Validation Rules](validation-rules.md) - where blockers come from
- [Usage](usage.md) - how to work with follow-up answers
- [Orchestration](orchestration.md) - the `awaiting_followup` state
