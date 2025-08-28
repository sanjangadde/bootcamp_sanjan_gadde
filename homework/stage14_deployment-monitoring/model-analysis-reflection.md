# Reflection

Our regression model, if deployed, faces several risks. Key failure modes include (1) schema drift if input features change without notice, (2) rising null rates or invalid values from upstream systems, (3) label delays leading to stale ground truth, and (4) model degradation if market or business dynamics shift. Another risk is over-reliance on linearity assumptions, which may understate nonlinear relationships in real-world data.

To mitigate these, monitoring must span four layers:

**Data Layer:** Track daily null rate (<2%), schema hash to detect unexpected column changes, and data freshness (max 15 minutes since last ingestion). Alerts trigger if thresholds are breached.

**Model Layer:** Monitor rolling RMSE and MAE over a 7-day window, with alerts if RMSE > 0.3 or R² < 0.05. Retraining is triggered if Population Stability Index (PSI) > 0.05 on core features or rolling error metrics degrade consistently.

**System Layer:** Track API p95 latency (<200ms), success rate (>99%), and resource utilization. On-call platform engineers receive alerts if jobs fail or latencies spike.

**Business Layer:** Monitor portfolio-adjusted return impact, ensuring model-driven signals do not reduce financial KPIs by more than 5% over baseline. Analysts review business KPIs weekly.

Ownership is divided as follows: Data engineering maintains schema and freshness checks; ML engineers own model metrics, retraining, and dashboards; platform engineers handle latency and uptime; analysts and business stakeholders review financial KPIs. Issues are logged in the shared incident tracker, and rollbacks require approval from the ML lead. Handoffs follow a runbook with first steps (validate inputs, check dashboards, rerun pipeline). Retraining cadence is quarterly, with earlier triggers if drift or performance issues are detected.
