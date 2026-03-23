# Architecture: Modular Monolith

## Overview
This project is best served by a modular monolith: one workspace, one deployment surface, and explicit boundaries between intake, validation, prompting, pipelines, and export concerns.

That choice fits the current stage well. The domain is already split into clear responsibilities, but the implementation has not started yet, so microservices would add operational cost too early and a flat layered structure would make it too easy to mix rules from different pipeline stages.

Primary implementation surface is declarative and agent-driven: schemas, prompts, pipeline YAML, agent instructions, and project context files. Any code under `src/` is non-primary support and must not become the architectural center of gravity without explicit approval.

## Decision Rationale
- **Project type:** AI-assisted intake and pipeline orchestration workspace
- **Tech stack:** OpenCode + AI Factory with Markdown, YAML, JSON, and XLSX references
- **Key factor:** strong module boundaries are needed, but separate deployment units are not

## Folder Structure
```text
.
├── .ai-factory/
│   ├── DESCRIPTION.md
│   ├── ARCHITECTURE.md
│   ├── PLAN.md
│   └── references/
├── .opencode/
│   ├── agents/
│   ├── plugins/
│   └── skills/
├── inputs/
│   ├── raw/
│   ├── normalized/
│   ├── validation/
│   └── interviews/
├── schemas/
├── prompts/
│   ├── intake/
│   └── pipeline/
├── pipelines/
├── runs/
├── outputs/
│   ├── json/
│   ├── md/
│   ├── csv/
│   └── xlsx/
├── src/
│   └── lead_scriptor/
├── tests/
└── docs/
```

## Dependency Rules
- `inputs/raw` is source material only; downstream modules may read it but must not rewrite user-authored meaning.
- `schemas` defines allowed structure; intake and validation logic depend on schemas, not the other way around.
- `prompts/intake` may depend on input contracts and validation outputs.
- `pipelines` may consume normalized inputs and validation results, but must not bypass them.
- `outputs` and `runs` are terminal artifacts and should not be imported as business inputs.

- ✅ Intake can write normalized artifacts and validation reports.
- ✅ Validation can read raw and normalized inputs plus schema definitions.
- ✅ Pipeline execution can read normalized inputs, prompts, and pipeline definitions.
- ❌ Prompts must not become the source of truth for schema definitions.
- ❌ Pipeline stages must not infer missing required fields silently.
- ❌ Export logic must not mutate validated business meaning.

## Layer/Module Communication
- Intake produces structured candidates and provenance metadata.
- Validation evaluates completeness, contradictions, and weak fields against schemas and stage-specific rules.
- Guided-question flows consume validation gaps and ask only the smallest useful set of follow-up questions.
- Normalization publishes stable YAML or JSON contracts for downstream pipeline execution.
- Pipelines read contracts through module-level entry points, not by reaching into intermediate working files.

## Key Principles
1. Keep module boundaries explicit: intake, validation, prompting, pipelines, and export each own a distinct concern.
2. Preserve provenance: every important field should be traceable to raw input, user answer, or explicit inference.
3. Fail conservatively: missing required data blocks execution; weak data warns; nothing is guessed silently.

## Code Examples

### Validation Contract Example
```yaml
validation_result:
  status: partial
  ready_for:
    - homework_marketing
  blocked_for:
    - sales_script
  missing_required:
    - sales.call_goal
  weak_fields:
    - audience.suspected_core_audience
```

### Module Boundary Example
```json
{
  "rule": "pipeline modules read only normalized inputs",
  "allowed": [
    "inputs/normalized/product.yaml",
    "inputs/validation/completeness.json",
    "pipelines/homework_marketing.yaml"
  ],
  "forbidden": [
    "editing inputs/raw/product.md during pipeline execution",
    "inventing missing required fields inside pipeline prompts"
  ]
}
```

## Anti-Patterns
- ❌ Mixing intake questions, validation rules, and final marketing generation in one prompt or module.
- ❌ Letting spreadsheets become the runtime source of truth after normalized contracts exist.
- ❌ Allowing downstream pipeline logic to patch bad or missing inputs instead of sending them back to intake.
