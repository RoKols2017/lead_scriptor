# Lead Scriptor Intake Helper

> Русская версия. English: `README.en.md`

Конфигурационный workspace для структурированного intake, валидации и оркестрации pipeline-маршрутов для маркетинга, custdev, поиска ЛПР и sales scripts.

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
