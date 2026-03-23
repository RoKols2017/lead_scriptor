# Project: Lead Scriptor Intake Helper

## Overview
Configuration-first project for OpenCode + AI Factory that formalizes an intake layer for marketing, custdev, and sales pipelines.

The system is designed to collect raw product and audience input, ask only for missing critical details, normalize the answers into strict machine-readable files, validate completeness and contradictions, and prepare reproducible inputs for downstream pipeline runs.

## Core Features
- Ingest raw business context from free-form files instead of relying on Google Sheets.
- Detect gaps, weak fields, and contradictions before pipeline execution.
- Ask a short, guided set of clarification questions only for missing critical data.
- Normalize validated inputs into stable YAML and JSON artifacts.
- Support reusable agent roles for intake, validation, research, interviewing, and sales script design.
- Produce deterministic input packages that can be reused across multiple runs.

## Tech Stack
- **Runtime/Platform:** OpenCode + AI Factory workspace
- **Primary Formats:** Markdown, YAML, JSON, XLSX reference files
- **Agent Model Strategy:** `openai/gpt-5.4`, `openai/gpt-5.4-mini`, `openai/gpt-5.4-nano`
- **Configuration Surface:** `.ai-factory.json`, `opencode.json`, `.mcp.json`
- **Current Codebase State:** specification, schemas, prompt templates, pipeline configs, reference docs, workspace scaffolding and a minimal Python runtime for normalization/validation exist

## Architecture Notes
- The project centers around staged data flow: `ingest -> gap-analysis -> guided-questions -> normalize-and-save`.
- The domain is structured around input artifacts, validation rules, pipeline definitions, and agent responsibilities.
- The intake layer must remain conservative: no guessing, explicit assumptions, and source tracing for every derived field.
- Reference spreadsheets are legacy inputs to study, not the primary runtime interface.
- Primary implementation surface is declarative and agent-driven: schemas, prompts, pipeline YAML, agent instructions, and AI context files.

## Non-Functional Requirements
- Logging: configurable by environment when implementation begins.
- Reproducibility: the same validated input should trigger the same pipeline path.
- Reliability: required fields block downstream stages; recommended fields emit warnings.
- Security: agent instructions and external skills must be reviewed for prompt injection risks.
- Maintainability: schemas, prompts, and validation logic should evolve independently.

## Architecture
See `.ai-factory/ARCHITECTURE.md` for detailed architecture guidelines.
Pattern: Modular Monolith.
