[Back to README](../../README.en.md) · [Russian Version](../domain-model.md)

# Domain Model

## Core Entities

- `product` - what is being sold, what problem it solves, and what value it creates.
- `company` - who sells, in which market context, and with which offer.
- `audience` - who buys, which pains, needs, and outcomes matter.
- `sales` - outreach strategy, target company types, target titles, call goal, and hard constraints.
- `tone` - language, politeness, confidence, banned phrases, and preferred patterns.
- `homework` - toggles for lecture-derived routes and export expectations.

## Stage Contracts

- `raw` stores user-authored free text.
- `normalized` stores machine-readable contracts.
- `validation` stores readiness, blockers, contradictions, and weak fields.
- `runs` stores execution metadata and stage outputs.

## Pipeline Families

- Marketing homework pipeline - lecture 1 artifacts.
- Simulated custdev pipeline - lecture 2 avatar-driven interviews.
- Real interview synthesis pipeline - transcript ingestion and correction proposals.
- LPR discovery pipeline - target company and decision-maker discovery.
- Sales script pipeline - script block generation.
- Script styling pipeline - tone adaptation and final export shape.

## Contract Rules

- Downstream pipelines read normalized contracts only.
- Missing `required` fields block execution.
- `recommended` gaps produce warnings, not hard blockers.
- Any inferred value must carry explicit provenance.

## See Also

- [Provenance](provenance.md) - where data comes from
- [Validation Rules](validation-rules.md) - what counts as a blocker
- [Orchestration](orchestration.md) - how entities move through stages
