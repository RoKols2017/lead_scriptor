# AGENTS.md

> Project map for AI agents. Keep this file up-to-date as the project evolves.

## Project Overview
This workspace defines an AI-assisted intake layer for a marketing and sales content pipeline. The repository now contains project specifications plus concrete schemas, prompt templates, pipeline configs, reference docs, and export scaffolding for the planned workflow.

## Tech Stack
- **Platform:** OpenCode + AI Factory
- **Primary Formats:** Markdown, YAML, JSON, XLSX
- **Models:** `openai/gpt-5.4`, `openai/gpt-5.4-mini`, `openai/gpt-5.4-nano`
- **Architecture:** Modular Monolith (planned)

## Project Structure
```text
.
├── .ai-factory.json                              # Installed AI Factory skills and MCP flags
├── .ai-factory/                                  # AI project context files
│   ├── DESCRIPTION.md                            # Project specification for agents
│   ├── ARCHITECTURE.md                           # Architecture rules and module boundaries
│   ├── PLAN.md                                   # Active implementation plan
│   └── references/                               # Lecture and XLSX-derived knowledge layer
├── .mcp.json                                     # Project-level MCP configuration
├── .opencode/                                    # OpenCode local packages and installed skills
│   ├── agents/                                   # Project agent role instructions
│   ├── package.json                              # Local OpenCode dependency config
│   ├── bun.lock                                  # Dependency lockfile
│   ├── node_modules/                             # Installed packages
│   └── skills/                                   # Installed AI Factory skills
├── docs/                                         # Domain, validation, routing, export, and ops docs
├── inputs/                                       # Runtime source contracts and interview inputs
│   ├── raw/                                      # Free-form business input templates
│   ├── normalized/                               # Canonical YAML contracts
│   ├── validation/                               # Readiness and contradiction reports
│   └── interviews/                               # Real interview transcript inputs
├── outputs/                                      # Value-based export artifacts and manifests
├── src/                                          # Minimal runtime implementation
│   └── lead_scriptor/                            # Intake, normalization, validation and export logic
├── tests/                                        # Runtime unit tests
├── pipelines/                                    # Declarative pipeline definitions
├── prompts/                                      # Intake and pipeline prompt templates
├── runs/                                         # Per-run metadata and stage snapshots
├── schemas/                                      # JSON Schema contracts
├── README.md                                     # Project entry document
├── TZ_input_structure_intake_helper_opencode_ai_factory.md  # Main product and architecture spec
├── lecture_1_google_sheets_chatgpt.md            # Lecture 1 reference transcript
├── lecture_2_google_sheets_chatgpt.md            # Lecture 2 reference transcript
├── Google Sheets + ChatGPT 1.xlsx                # Reference spreadsheet input
└── Зерокодер _ Google Sheets + ChatGPT _ CustDev _ Скрипты.xlsx  # Reference spreadsheet input
```

## Key Entry Points
| File | Purpose |
|------|---------|
| `TZ_input_structure_intake_helper_opencode_ai_factory.md` | Main functional specification for the intake-helper concept |
| `opencode.json` | Runtime routing and agent registration config |
| `src/lead_scriptor/cli.py` | Current runtime entry point for normalization and validation |
| `pipelines/homework_marketing.yaml` | Declarative marketing homework pipeline |
| `pipelines/homework_custdev_simulated.yaml` | Declarative simulated custdev pipeline |
| `.ai-factory.json` | Declares installed skills and high-level MCP toggles |
| `.mcp.json` | Project MCP server configuration |
| `.opencode/package.json` | Local OpenCode dependency manifest |

## Documentation
| Document | Path | Description |
|----------|------|-------------|
| Main spec | `TZ_input_structure_intake_helper_opencode_ai_factory.md` | Detailed product, input model, and validation design |
| README (RU) | `README.md` | Russian landing page |
| README (EN) | `README.en.md` | English landing page |
| Usage (RU) | `docs/usage.md` | Russian workflow guide |
| Usage (EN) | `docs/en/usage.md` | English workflow guide |
| Normalization (RU) | `docs/normalization-rules.md` | Russian normalization rules |
| Normalization (EN) | `docs/en/normalization-rules.md` | English normalization rules |
| Validation (RU) | `docs/validation-rules.md` | Russian validation rules |
| Validation (EN) | `docs/en/validation-rules.md` | English validation rules |
| Provenance (RU) | `docs/provenance.md` | Russian provenance guide |
| Provenance (EN) | `docs/en/provenance.md` | English provenance guide |
| Export Mapping (RU) | `docs/export-mapping.md` | Russian export mapping |
| Export Mapping (EN) | `docs/en/export-mapping.md` | English export mapping |
| Usage Add-ons (RU) | `docs/orchestration.md` | Russian orchestration contract |
| Usage Add-ons (EN) | `docs/en/orchestration.md` | English orchestration contract |
| Testing (RU) | `docs/testing-strategy.md` | Russian testing strategy |
| Testing (EN) | `docs/en/testing-strategy.md` | English testing strategy |
| Pilot Checklist | `docs/pilot-readiness-checklist.md` | Pre-pilot contract checklist |
| Pilot Matrix | `docs/pilot-smoke-matrix.md` | Pilot smoke scenarios |
| Pilot Triage | `docs/pilot-triage.md` | Blocked route recovery guide |
| Pilot Runbook | `docs/operational-runbook.md` | Operator pilot procedure |

## AI Context Files
| File | Purpose |
|------|---------|
| `AGENTS.md` | This file - project structure map |
| `.ai-factory/DESCRIPTION.md` | Project specification and tech stack |
| `.ai-factory/ARCHITECTURE.md` | Architecture decisions and guidelines |

## Notes For Agents
- Treat the markdown spec as the source of truth until application code exists.
- Prefer normalized contracts and pipeline configs over legacy spreadsheet coupling.
- Treat schemas, prompts, agent instructions, and pipeline YAML as the primary implementation surface.
- Do not expand `src/` into the main architecture without explicit user approval.
- Prefer adding implementation work under the architecture rules in `.ai-factory/ARCHITECTURE.md`.
