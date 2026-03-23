[Back to README](../../README.en.md) · [Russian Version](../orchestration.md)

# Orchestration Contract

## Goal

OpenCode coordinates the workflow through files, agent roles, and declarative pipeline definitions. Runtime code remains a support layer only.

## Core Handoff Files

- raw brief: `inputs/raw/*.md`
- normalized contracts: `inputs/normalized/*.yaml`
- readiness and blockers: `inputs/validation/completeness.json`
- contradictions: `inputs/validation/contradictions.json`
- guided questions: `inputs/validation/guided-questions.json`
- follow-up answers: `inputs/raw/followup_answers.md`
- run state: `runs/latest-run.json`

## Route States

- `draft` - raw input exists but normalization has not been reviewed yet
- `ready_for_validation` - normalized contracts were updated
- `blocked` - validation found missing required fields or contradictions
- `awaiting_followup` - guided questions were generated and answers are still pending
- `route_ready` - a downstream route may start
- `completed` - route artifacts were produced

## Allowed Transitions

- `draft -> ready_for_validation`
- `ready_for_validation -> blocked`
- `blocked -> awaiting_followup`
- `awaiting_followup -> ready_for_validation`
- `ready_for_validation -> route_ready`
- `route_ready -> completed`

## Agent to Route Mapping

- `intake` -> raw ingest, follow-up merge, guided question planning
- `validator` -> completeness, contradictions, route gating
- `researcher` -> lecture 1 marketing route
- `interviewer` -> simulated custdev and real interview synthesis
- `sales-architect` -> LPR discovery, script generation, and script styling

## Run Metadata

Each route handoff should write:

- `route_id`
- `agent`
- `state`
- `required_inputs_checked`
- `artifacts_written`
- `blocked_reasons`
- `next_action`

## See Also

- [Usage](usage.md) - what the practical flow looks like
- [Run Artifacts](run-artifacts.md) - what is stored in `runs/`
- [Guided Questions](guided-questions.md) - how the blocked loop works
