# Lead Scriptor Intake Helper

> English version. Russian: `README.md`

Config-first workspace for structured intake, validation, and pipeline orchestration for marketing, custdev, LPR discovery, and sales scripts.

The intended architecture is agent-driven. Project behavior is defined primarily through `schemas/`, `prompts/`, `pipelines/`, `.opencode/agents/`, and AI context files rather than through an application runtime.

## Workflow Surface

Primary workflow is coordinated through `opencode.json`, `.opencode/agents/*.md`, `pipelines/*.yaml`, `inputs/`, `schemas/`, and `docs/`.

## Key Folders

- `inputs/` - raw, normalized, validation, and interview inputs
- `schemas/` - canonical contracts
- `prompts/` - intake and pipeline prompt templates
- `pipelines/` - declarative routes
- `outputs/` - value-based export artifacts
- `runs/` - execution metadata
- `docs/` - primary Russian documentation
- `docs/en/` - English mirror documentation
- `src/lead_scriptor/` - non-primary support code

## Core Rule

Google Sheets is a compatibility layer only. Runtime state lives in normalized contracts and pipeline artifacts.

## Documentation

| Russian | English |
|---------|---------|
| `docs/usage.md` | `docs/en/usage.md` |
| `docs/normalization-rules.md` | `docs/en/normalization-rules.md` |
| `docs/validation-rules.md` | `docs/en/validation-rules.md` |
| `docs/provenance.md` | `docs/en/provenance.md` |
| `docs/export-mapping.md` | `docs/en/export-mapping.md` |
