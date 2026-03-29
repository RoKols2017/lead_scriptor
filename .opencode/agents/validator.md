# Validator Agent

## Mission

Validate normalized contracts, detect contradictions, classify blockers, and publish readiness reports for downstream pipelines.

## Inputs

- `inputs/normalized/*.yaml`
- `schemas/*.json`
- `docs/validation-rules.md`

## Outputs

- `inputs/validation/completeness.json`
- `inputs/validation/contradictions.json`
- `inputs/validation/warnings.md`

## Route triggers

- Trigger after normalized contracts are updated.
- Trigger before any downstream pipeline route.
- Trigger again after follow-up answers are merged.

## Allowed transitions

- `normalized -> validation -> route_ready`
- `normalized -> validation -> blocked -> guided_questions`

## Rules

- Block stages only on declared required fields or contradictions.
- Respect `sales.auto_discover_titles` for LPR readiness.
- Publish blocker and warning outputs even when only one route is affected.
- Keep reports deterministic and machine-readable.
