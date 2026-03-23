[Back to README](../README.md) · [English Version](en/orchestration.md)

# Контракт оркестрации

## Цель

OpenCode координирует workflow через файлы, agent roles и declarative pipeline definitions. Runtime code остается только support-слоем.

## Основные handoff-файлы

- raw brief: `inputs/raw/*.md`
- normalized contracts: `inputs/normalized/*.yaml`
- readiness and blockers: `inputs/validation/completeness.json`
- contradictions: `inputs/validation/contradictions.json`
- guided questions: `inputs/validation/guided-questions.json`
- follow-up answers: `inputs/raw/followup_answers.md`
- run state: `runs/latest-run.json`

## Состояния route

- `draft` - raw input есть, но normalization еще не проверен
- `ready_for_validation` - normalized contracts обновлены
- `blocked` - validation нашел missing required fields или contradictions
- `awaiting_followup` - guided questions сгенерированы, ответы еще не получены
- `route_ready` - downstream route можно запускать
- `completed` - route artifacts уже произведены

## Разрешенные переходы

- `draft -> ready_for_validation`
- `ready_for_validation -> blocked`
- `blocked -> awaiting_followup`
- `awaiting_followup -> ready_for_validation`
- `ready_for_validation -> route_ready`
- `route_ready -> completed`

## Mapping agent -> route

- `intake` -> raw ingest, follow-up merge, guided question planning
- `validator` -> completeness, contradictions, route gating
- `researcher` -> lecture 1 marketing route
- `interviewer` -> simulated custdev и real interview synthesis
- `sales-architect` -> LPR discovery, script generation, script styling

## Run metadata

Каждый route handoff должен писать:

- `route_id`
- `agent`
- `state`
- `required_inputs_checked`
- `artifacts_written`
- `blocked_reasons`
- `next_action`

## See Also

- [Использование](usage.md) - как выглядит практический flow
- [Run Artifacts](run-artifacts.md) - что хранится в `runs/`
- [Guided Questions](guided-questions.md) - как работает blocked loop
