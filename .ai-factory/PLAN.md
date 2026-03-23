# План: pre-pilot readiness

- Дата: 2026-03-23
- Режим: fast
- Фокус: readiness перед первым pilot-запуском, а не общий roadmap
- Основание: `.ai-factory/DESCRIPTION.md`, `.ai-factory/ARCHITECTURE.md`, `opencode.json`, `pipelines/*.yaml`, `prompts/**/*.md`, `schemas/*.json`, `.opencode/agents/*.md`, `docs/usage.md`

## Settings

- Testing: yes - включить contract checks и file-based smoke на реальных кейсах
- Logging: standard - логировать route selection, blocked reasons, rerun decisions, export verification и run manifest events
- Docs: yes - обновить только runbook и pilot-readiness критерии

## Текущее состояние

- Declarative/agent-driven контур уже собран: есть `schemas/`, `prompts/`, `pipelines/`, `.opencode/agents/`, `opencode.json`
- Документация уже bilingual, значит до pilot не нужен docs-first rewrite, нужен readiness-proof
- Python runtime остается thin support layer; source of truth остается в file contracts и orchestration config

## Цель

- Доказать, что workspace стабильно проходит путь `raw -> validation -> guided questions -> rerun -> downstream route -> values-only export` на реальных файловых кейсах и дает понятный operational triage при блокировках

## Tasks

### Фаза 1. Verify declarative contracts

1. Проверить route и pipeline contracts на полноту pre-pilot инвариантов.
   - Файлы: `opencode.json`, `pipelines/*.yaml`, `.opencode/agents/*.md`, `schemas/*.json`
   - Результат: для каждого route явно подтверждены `requires`, `produces`, blocked conditions, readiness gate, rerun entrypoint и export handoff; все несоответствия сведены в один readiness checklist
   - Logging: логировать missing contract fields, route/schema mismatches, ambiguous handoff points и unsupported resume semantics

2. Проверить guided-questions rerun loop как отдельный контракт, а не как побочный сценарий.
   - Файлы: `pipelines/guided_questions.yaml`, `prompts/intake/question_planner.md`, `prompts/intake/question_writer.md`, `schemas/guided-questions.schema.json`, `docs/usage.md`
   - Результат: зафиксировано, как blockers превращаются в вопросы, куда кладутся ответы, как выполняется повторный прогон и что считается resolved vs still blocked
   - Logging: логировать blocker-to-question mapping, unanswered required fields, rerun trigger и readiness delta после повторного прогона
   - Зависимости: после задачи 1

### Фаза 2. Smoke на реальных файловых кейсах

3. Собрать короткую матрицу pilot smoke scenarios на реальных типах входных файлов.
   - Файлы: `inputs/raw/`, `inputs/interviews/`, `inputs/normalized/`, `inputs/validation/`, новый `docs/pilot-smoke-matrix.md`
   - Результат: минимум 4 кейса - `marketing-ready`, `blocked-needs-followup`, `custdev-interview-ingest`, `sales-route-with-export`; для каждого описаны входы, expected route, blocked/ready статус и артефакты
   - Logging: логировать scenario id, selected route, expected artifacts и mismatch между ожиданием и фактом
   - Зависимости: после задач 1-2

4. Прогнать smoke scenarios end-to-end и зафиксировать triage для blocked routes.
   - Файлы: `runs/`, `inputs/validation/*`, `outputs/`, новый `docs/pilot-triage.md`
   - Результат: по каждому кейсу есть run evidence, список типовых failure modes, правило "куда возвращать маршрут" и минимальный операторский action для unblock
   - Logging: логировать blocked reason, next allowed action, rerun prerequisites и artifact trace per run
   - Зависимости: после задачи 3

### Фаза 3. Export и ops readiness

5. Верифицировать export layer только как values-only deliverable.
   - Файлы: `pipelines/export_google_sheets.yaml`, `docs/export-mapping.md`, `outputs/`, при необходимости `runs/latest-run.json`
   - Результат: подтверждено отсутствие formulas/derived spreadsheet logic, обязательные поля покрыты, export опирается только на validated artifacts и оставляет manifest trail
   - Logging: логировать export target, uncovered required values, values-only violations и manifest linkage
   - Зависимости: после задачи 4

6. Собрать короткий operational runbook для pilot и финальный go/no-go gate.
   - Файлы: `README.md`, `docs/usage.md`, новый `docs/operational-runbook.md`
   - Результат: описаны pilot entry steps, readiness checks, blocked-route triage, rerun loop, export verification и финальный checklist "можно/нельзя запускать pilot"
   - Logging: логировать config version, route matrix version и missing pilot prerequisites
   - Зависимости: после задач 4-5

## Commit Plan

1. `chore: align pre-pilot pipeline contracts`
   - После задач 1-2

2. `test: add pilot smoke scenarios and route triage`
   - После задач 3-4

3. `docs: add pilot runbook and export readiness gates`
   - После задач 5-6

## Критерии завершения

- Для каждого pilot route понятны required inputs, produced artifacts, blocked reasons и rerun path
- Guided-questions loop подтвержден на реальном blocked кейсе, а не только описан в docs
- Есть file-based smoke evidence по реальным сценариям, включая минимум один blocked и один successful downstream flow
- Export проходит values-only verification и не вносит spreadsheet logic в source of truth
- Оператор может по runbook понять, запускать ли pilot, что делать при блокировке и как безопасно повторить маршрут

## Следующий шаг

- Для исполнения этого readiness-плана: `/aif-implement`
