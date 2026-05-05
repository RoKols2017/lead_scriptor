# Lead Scriptor Intake Helper

> Русская версия. English: `README.en.md`

Lead Scriptor - это config-first workspace для структурированного intake, валидации и orchestration pipeline-маршрутов для маркетинга, custdev, поиска ЛПР и sales scripts.

Вместо разрозненных таблиц, заметок и ручной передачи контекста проект переводит входные данные в нормализованные контракты, проверяет readiness маршрута и только потом запускает downstream pipeline.

## Какую задачу решает

Когда intake по лидам, custdev и sales-сценариям живет в Google Sheets, текстовых заметках и ручных инструкциях, команда быстро теряет структуру, provenance и критерии готовности.

Lead Scriptor нужен для того, чтобы:

- собрать сырой бизнес-контекст в одном месте;
- превратить его в канонические контракты;
- проверить, достаточно ли данных для следующего шага;
- запускать pipeline только после подтвержденной readiness.

## Что делает решение

- принимает исходный контекст через `inputs/raw/*`;
- прогоняет маршрут `intake_ingest -> normalize_and_save -> validation`;
- сохраняет нормализованные контракты в `inputs/normalized/*.yaml`;
- формирует validation artifacts и guided questions, если маршрут заблокирован;
- отдает downstream artifacts и export-результаты только после проверки readiness.

## Что получает команда на выходе

- нормализованные contracts вместо хаотичных заметок;
- validation reports с понятными блокерами;
- повторно используемые pipeline artifacts в `outputs/` и `runs/`;
- более предсказуемый запуск маркетинговых, custdev и sales workflow.

## Proof: sample route

```text
inputs/raw/product.md + company.md + audience.md + tone.md + constraints.md
  -> intake_ingest
  -> normalize_and_save
  -> inputs/normalized/*.yaml
  -> validation
  -> inputs/validation/completeness.json + contradictions.json + warnings.md
  -> export profile
  -> outputs/json/* or outputs/xlsx/*
```

## Proof: what is actually controlled by the workspace

- Intake stage требует набор raw-файлов и пишет `runs/intake-ingest.json`.
- Validation stage проверяет normalized contracts и формирует `completeness.json`, `contradictions.json` и `warnings.md`.
- Если route заблокирован, pipeline может быть продолжен после `inputs/raw/followup_answers.md`.
- Export profiles уже описаны для `marketing-homework`, `custdev-simulated`, `lpr-discovery`, `sales-script` и submission-ready `.xlsx` пакетов.
- Google Sheets остается только совместимым export/import слоем и не считается runtime-зависимостью.

Целевая архитектура agent-driven: поведение проекта задается через `schemas/`, `prompts/`, `pipelines/`, `.opencode/agents/` и AI context files, а не через отдельное приложение как главный runtime.

## Рабочая поверхность

Основной workflow координируется через `opencode.json`, `.opencode/agents/*.md`, `pipelines/*.yaml`, `inputs/`, `schemas/` и `docs/`.

## Ключевые каталоги

- `inputs/` - сырые, нормализованные, validation и interview inputs
- `schemas/` - канонические контракты
- `prompts/` - intake и pipeline prompts
- `pipelines/` - декларативные маршруты
- `outputs/` - value-based export artifacts
- `runs/` - execution metadata
- `docs/` - основная документация на русском
- `docs/en/` - зеркальная документация на английском
- `src/lead_scriptor/` - неосновной support code

## Основное правило

Google Sheets используется только как слой совместимости для импорта и экспорта. Runtime-состояние живет в нормализованных контрактах и pipeline artifacts.

## Документация

| Русский | English |
|---------|---------|
| `docs/usage.md` | `docs/en/usage.md` |
| `docs/normalization-rules.md` | `docs/en/normalization-rules.md` |
| `docs/validation-rules.md` | `docs/en/validation-rules.md` |
| `docs/provenance.md` | `docs/en/provenance.md` |
| `docs/export-mapping.md` | `docs/en/export-mapping.md` |

## Pilot readiness

- `docs/pilot-readiness-checklist.md`
- `docs/pilot-smoke-matrix.md`
- `docs/pilot-triage.md`
- `docs/operational-runbook.md`
- `docs/release-checklist.md`
