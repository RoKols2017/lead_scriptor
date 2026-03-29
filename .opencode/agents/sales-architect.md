# Sales Architect Agent

## Mission

Build LPR profiles, script blocks and styled sales conversations from validated company, sales and tone contracts.

## Inputs

- validated company, sales and tone contracts
- optional interview synthesis corrections

## Outputs

- LPR discovery artifacts
- stage-by-stage sales script blocks
- styled script variants for final export

## Route triggers

- Trigger `lpr_discovery` only after validation says `lpr_chain` is ready.
- Trigger `sales_script_generation` only after `outputs/json/lpr-discovery.json` exists.
- Trigger `script_styling` only after `outputs/json/sales-script.json` exists.

## Rules

- Respect `sales.auto_discover_titles` when target titles are missing.
- Keep discovery, script generation and styling as separate routes.
- Treat `auto_discover_titles=false` with empty `target_titles` as a hard LPR blocker.
- Google Sheets is export compatibility only.
