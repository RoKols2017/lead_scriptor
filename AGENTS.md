# AGENTS.md

> Working guide for coding agents in `lead_scriptor`.
> Keep this file aligned with the actual repository, not generic Python defaults.

## Project Summary

This repository is a config-first workspace for intake, normalization, validation, and pipeline orchestration.

The primary implementation surface is declarative:
- `schemas/`
- `pipelines/`
- `prompts/`
- `.opencode/agents/`
- `.ai-factory/`
- `docs/`

Python under `src/lead_scriptor/` is support code, not the architectural center.

## Source Of Truth

When code and docs diverge, check these first:
1. `.ai-factory/DESCRIPTION.md`
2. `.ai-factory/ARCHITECTURE.md`
3. `TZ_input_structure_intake_helper_opencode_ai_factory.md`
4. `schemas/*.json`
5. `pipelines/*.yaml`

Design intent is conservative intake and validation:
- do not silently invent missing required fields
- preserve provenance from raw inputs
- block downstream stages when required data is missing
- treat Google Sheets as import/export compatibility, not runtime truth

## Repo Layout

- `src/lead_scriptor/`: minimal runtime helpers for normalization, validation, export manifest generation, and CLI entrypoints
- `tests/`: `unittest`-based runtime tests
- `inputs/raw/`: free-form source material
- `inputs/normalized/`: canonical normalized YAML contracts
- `inputs/validation/`: completeness and contradiction reports
- `outputs/`: generated export artifacts
- `runs/`: latest run metadata
- `schemas/`: JSON Schema contracts
- `pipelines/`: declarative workflow definitions
- `docs/`: operator and product documentation

## Environment Notes

- The repository does not currently define a root `pyproject.toml`, `Makefile`, `Taskfile.yml`, or `Justfile`.
- The repository does not currently define a root `package.json` for app tasks.
- `.opencode/package.json` exists only for local OpenCode plugin dependency management.
- Use `python3`, not `python`; `python` is not available in this workspace.
- For Python commands, set `PYTHONPATH=src` so `lead_scriptor` imports resolve.

## Build, Lint, And Test Commands

These are the commands that match the current repository state.

### Runtime command

Run the support runtime from the repo root:

```bash
PYTHONPATH=src python3 -m lead_scriptor --root .
```

This writes normalized contracts, validation reports, export manifest data, and `runs/latest-run.json`.

### Full test suite

Use discovery. Plain `python3 -m unittest` does not find tests here.

```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

### Single test file

```bash
PYTHONPATH=src python3 -m unittest tests.test_runtime
```

### Single test class

```bash
PYTHONPATH=src python3 -m unittest tests.test_runtime.RuntimeTests
```

### Single test method

```bash
PYTHONPATH=src python3 -m unittest tests.test_runtime.RuntimeTests.test_lpr_is_blocked_when_titles_missing_and_auto_discover_false
```

### Optional syntax smoke check

There is no configured build step. For a cheap syntax-only verification, use:

```bash
PYTHONPATH=src python3 -m compileall src tests
```

### Linting / formatting status

There is no configured repo-level linter or formatter at the moment.

That means:
- no verified `ruff` command
- no verified `black` command
- no verified `mypy` command
- no verified `pytest` command

Do not add or assume those tools unless the user asks for toolchain changes.

## Test Expectations

- Keep tests in `tests/`.
- Follow the current `unittest.TestCase` style unless the repo is intentionally migrated.
- Prefer narrow tests against observable file outputs and validation payloads.
- For runtime tests, isolate filesystem effects with `tempfile.TemporaryDirectory()`.
- Assert on concrete output fields, not broad snapshots.

## Python Style Observed In Repo

### Imports

- Use `from __future__ import annotations` in modules that already follow that pattern.
- Group imports in this order: standard library, third-party, local package imports.
- Use relative imports inside `src/lead_scriptor/` modules.
- Avoid unused imports and wildcard imports.

### Formatting

- Follow PEP 8 style and keep formatting simple.
- Prefer short, readable functions.
- Use 4-space indentation.
- Keep line length reasonable; optimize for readability over squeezing expressions.
- Preserve the repository's straightforward style instead of introducing heavy abstraction.

### Types

- Add type hints for function signatures.
- The existing code uses built-in generics like `list[str]` and `dict[str, Any]`; follow that style.
- Use `Any` sparingly and only where payloads are intentionally dynamic.
- Prefer concrete container shapes over vague typing when easy to express.

### Naming

- Functions and variables: `snake_case`.
- Constants: `UPPER_SNAKE_CASE`.
- Test methods: `test_<behavior>`.
- Use names that reflect domain concepts from schemas and contracts.
- Keep file names descriptive and aligned with the domain stage: `normalize`, `validate`, `extract`, `export_profiles`.

### Data And Contracts

- Match existing contract keys exactly; downstream logic depends on stable field names.
- Prefer editing schema, prompt, or pipeline files when changing behavior that is primarily declarative.
- Do not treat generated artifacts in `outputs/` or `runs/` as business inputs.
- `inputs/raw/` is source material; avoid mutating user-authored meaning.

### Error Handling

- Fail conservatively.
- Do not mask missing required inputs with guessed defaults.
- Use explicit checks like the existing `_missing()` helper style for validation logic.
- Raise or surface clear failures when behavior cannot be completed safely.
- When adding validation rules, make blocker vs warning severity obvious in code and outputs.

### Logging

- Follow the existing structured logging pattern in `logging_utils.py`.
- Emit machine-readable JSON log lines via `log_event()`.
- Keep event names stable and payloads compact.
- Use `ensure_ascii=True` behavior for JSON output consistency.

### File IO

- Use `pathlib.Path`.
- Always specify `encoding="utf-8"` for text file reads and writes.
- Create parent directories as needed before writing.
- Preserve the existing convention of newline-terminated output files.

## Architecture Rules For Agents

- Respect the modular boundaries in `.ai-factory/ARCHITECTURE.md`.
- Keep intake, validation, prompting, pipelines, and export concerns separate.
- Do not move business logic into prompts if it belongs in schemas or validation.
- Do not expand `src/` into the main architecture without explicit approval.
- Prefer the smallest correct change.

## Rule Files Check

Repository scan results:
- No `.cursorrules` file found.
- No `.cursor/rules/` directory found.
- No `.github/copilot-instructions.md` file found.

If those files are added later, merge their instructions into this guide and treat the repo-specific rule files as higher-priority operational guidance.

## Practical Agent Guidance

- Read surrounding schemas, prompts, and pipeline files before changing behavior.
- Expect the worktree to be dirty; do not revert unrelated user changes.
- Be careful running the runtime command in the repo root because it updates tracked generated artifacts.
- If you need a safe verification path, prefer the isolated unit tests first.
- When changing output structure, update tests in the same edit.
- When behavior is ambiguous, prefer explicit documentation over implicit inference.
