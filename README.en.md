# Lead Scriptor Intake Helper

> English version. Russian: `README.md`

Lead Scriptor is a config-first workspace for structured intake, validation, and pipeline orchestration for marketing, custdev, decision-maker discovery, and sales scripts.

Instead of leaving business context scattered across spreadsheets, notes, and manual instructions, the project turns raw inputs into normalized contracts, checks route readiness, and only then allows downstream pipelines to run.

## What problem it solves

When lead research, custdev, and sales intake live in Google Sheets and ad hoc notes, teams lose structure, provenance, and clear readiness criteria.

Lead Scriptor is designed to:

- collect raw business context in one place;
- convert it into canonical contracts;
- validate whether the route is ready for the next step;
- run downstream pipelines only after readiness is confirmed.

## What the solution does

- accepts source context through `inputs/raw/*`;
- runs the `intake_ingest -> normalize_and_save -> validation` route;
- stores normalized contracts in `inputs/normalized/*.yaml`;
- generates validation artifacts and guided questions when a route is blocked;
- exposes downstream artifacts and export outputs only after readiness checks pass.

## What the team gets

- normalized contracts instead of fragmented notes;
- validation reports with explicit blockers;
- reusable pipeline artifacts in `outputs/` and `runs/`;
- more predictable marketing, custdev, and sales workflows.

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

- The intake stage requires a defined raw input set and writes `runs/intake-ingest.json`.
- The validation stage checks normalized contracts and produces `completeness.json`, `contradictions.json`, and `warnings.md`.
- If a route is blocked, the pipeline can resume after `inputs/raw/followup_answers.md`.
- Export profiles are already defined for `marketing-homework`, `custdev-simulated`, `lpr-discovery`, `sales-script`, and submission-ready `.xlsx` packages.
- Google Sheets remains a compatibility layer for import/export and is not treated as a runtime dependency.

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
