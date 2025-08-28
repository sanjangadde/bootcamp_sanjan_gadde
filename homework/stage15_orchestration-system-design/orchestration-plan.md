# Orchestration Plan (Project DAG)

This plan converts the current notebook workflow into a reproducible pipeline with clear jobs, dependencies, inputs/outputs, logging, and checkpoints.

## Overview DAG (ASCII)
```
fetch_data ──► validate_schema ──► preprocess ──► feature_engineering ──► split_data
                                                                      └────────────► train_models ─► evaluate ─► scenario_compare ─► reports
                                                                                                      └──────────────────────────────► plots
```
Parallelizable: `train_models` can fan-out by scenario/model; `evaluate` can run per scenario in parallel; `plots` generate per-scenario figures concurrently.

## Jobs / Tasks

### 1) fetch_data
- Purpose: Pull source data (prices/returns) from local CSV or API.
- Idempotent: Yes (file named by content hash/date; re-run produces same file)
- Logging: `logs/fetch_data.log` (rows pulled, time span)
- Checkpoint: `artifacts/fetch_data.done` + SHA256 of file

### 2) validate_schema
- Purpose: Enforce schema, ranges, and freshness.
- Inputs: `data/raw/*.parquet`, `schemas/base_schema.json`
- Outputs: `artifacts/validation_report.json`
- Idempotent: Yes
- Logging: `logs/validate_schema.log` (null rates, freshness minutes)
- Checkpoint: fail if schema hash mismatch; write `artifacts/validation.ok`

### 3) preprocess  (scenarios: mean_impute, median_impute, outlier_treatment)
- Purpose: Clean NAs, handle outliers (winsorize/IQR), normalize dates/tickers.
- Inputs: `data/raw/*.parquet`, `config.yaml` (`preprocess.*`)
- Outputs: `data/processed/{scenario}.parquet`
- Idempotent: Yes (deterministic transforms + versioned config)
- Logging: `logs/preprocess_{scenario}.log` (NA rate before/after)
- Checkpoint: `artifacts/preprocess_{scenario}.ok`

### 4) feature_engineering
- Purpose: Build lagged and rolling features (e.g., `ret_lag_1..k`, `ret_roll_7..28`).
- Inputs: `data/processed/{scenario}.parquet`
- Outputs: `features/{scenario}.parquet`
- Idempotent: Yes
- Logging: `logs/feature_eng_{scenario}.log`
- Checkpoint: `artifacts/feature_eng_{scenario}.ok`

### 5) split_data
- Purpose: Time-aware split into train/test (and CV folds).
- Inputs: `features/{scenario}.parquet`
- Outputs: `splits/{scenario}_{split_id}.parquet`
- Idempotent: Yes (seeded deterministic split + date cut)
- Logging: `logs/split_{scenario}.log`
- Checkpoint: `artifacts/split_{scenario}.ok`

### 6) train_models  (models: linear, ridge, svr, poly2)
- Purpose: Fit pipelines with `StandardScaler` + regressor.
- Inputs: `splits/{scenario}_train.parquet`
- Outputs: `models/{scenario}_{model}.pkl`, `artifacts/{scenario}_{model}_cv.json`
- Idempotent: Yes (fixed seed & config)
- Logging: `logs/train_{scenario}_{model}.log` (CV scores, duration)
- Checkpoint: `artifacts/train_{scenario}_{model}.ok`

### 7) evaluate
- Purpose: Compute MAE, MSE, RMSE, R² on test; bootstrap CIs.
- Inputs: `models/{scenario}_{model}.pkl`, `splits/{scenario}_test.parquet`
- Outputs: `metrics/{scenario}_{model}.json`, `metrics/{scenario}_{model}_bootstrap.json`
- Idempotent: Yes (bootstrap seed stored in config)
- Logging: `logs/eval_{scenario}_{model}.log`
- Checkpoint: `artifacts/eval_{scenario}_{model}.ok`

### 8) plots
- Purpose: Generate figures (pred-vs-true, hexbin, residual hist, residuals vs predicted).
- Inputs: `metrics/*.json`, predictions cached at `preds/{scenario}_{model}.parquet`
- Outputs: `reports/figs/{scenario}_{model}_*.png`
- Idempotent: Yes
- Logging: `logs/plots_{scenario}_{model}.log`
- Checkpoint: `artifacts/plots_{scenario}_{model}.ok`

### 9) scenario_compare
- Purpose: Side-by-side metrics and CIs across scenarios/models.
- Inputs: `metrics/*.json`
- Outputs: `reports/scenario_table.csv`, `reports/scenario_summary.md`
- Idempotent: Yes
- Logging: `logs/scenario_compare.log`
- Checkpoint: `artifacts/scenario_compare.ok`

### 10) reports
- Purpose: Compose Markdown: model report, memo, reflection.
- Inputs: `reports/figs/*`, `reports/scenario_table.csv`
- Outputs: `reports/model_communication_report.md`, `reports/model_evaluation_memo.md`, `reports/reflection.md`
- Idempotent: Yes (templated Jinja/Markdown)
- Logging: `logs/reports.log`
- Checkpoint: `artifacts/reports.ok`

## Failure Points & Retry Policy
- Data/API outage → retry with exponential backoff (3 attempts, 1m/2m/4m); fall back to most recent cached file.
- Schema drift / high null rate → hard fail; notify Data Eng on-call; require upstream fix.
- Training failure (convergence) → auto-switch to simpler model (linear/ridge) and alert ML channel.
- Plotting I/O errors → retry write once; if persists, continue pipeline but mark plots missing.

## Logging & Checkpoints
- Central log: `logs/pipeline.log` (Python `logging` + JSON lines).
- Per-task logs as above; each task writes a `.ok` checkpoint and a metadata JSON (hashes, rows, timings).
- Metrics pushed to `metrics/` and optionally to a lightweight SQLite/duckdb `artifacts/metrics.db`.

## Automation vs Manual
- Automate now: steps 1–9 via `make` or `tox`/`nox` sessions or a simple `orchestrate.py`.
- Keep manual (for now): stakeholder write-ups/edits and business KPI interpretation (requires human judgment).
- Rationale: deterministic compute is best automated; narrative and strategy decisions remain human-in-the-loop.

## Interfaces & CLI Hints
- All tasks accept `--config config.yaml --scenario median_impute --model ridge`.
- Each task reads/writes Parquet/CSV to the paths listed above.
- Exit codes: `0` success; `1` recoverable error; `2` validation hard fail.

## Ownership
- Data Eng: `fetch_data`, `validate_schema`
- ML Eng: `preprocess`, `feature_engineering`, `split_data`, `train_models`, `evaluate`, `scenario_compare`
- Platform: job orchestration, storage, alerts
- Analyst: `reports` review and business KPI alignment
