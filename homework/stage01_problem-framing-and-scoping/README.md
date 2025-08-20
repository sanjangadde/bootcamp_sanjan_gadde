# Stock Correlation Explorer  
**Stage:** Problem Framing & Scoping (Stage 01)  

## Problem Statement  
Retail investors often build portfolios without realizing that many of their stocks move together due to underlying sector or market-wide forces. This reduces diversification benefits and increases portfolio risk. The Stock Correlation Explorer helps investors identify hidden correlations between stocks by calculating and visualizing pairwise correlation coefficients. By surfacing these relationships, investors can make better diversification decisions and avoid overexposure.  

## Stakeholder & User  
- **Primary Stakeholder:** Retail investors managing their own stock portfolios.  
- **Secondary Stakeholders:** Financial advisors, investing clubs, and students learning portfolio theory.  
- **Context:** Used during portfolio construction or review, when choosing which new stocks to add or evaluating existing diversification.  

## Useful Answer & Decision  
- **Type:** Descriptive analysis.  
- **Output:** Correlation matrix and heatmap showing how closely different stocks move together.  
- **Artifact:** Notebook or report with visualizations and summary metrics (e.g., average correlation, most/least correlated stock pairs).  

## Assumptions & Constraints  
- Historical price data is available through Yahoo Finance (`yfinance` Python library) or Alpha Vantage (free API).  
- Analysis will use daily adjusted closing prices over a chosen time horizon (e.g., 1–5 years).  
- Only liquid, publicly traded equities are included; no private assets.  
- Computation is lightweight and should run in seconds for portfolios up to ~50 stocks.  

## Known Unknowns / Risks  
- Correlations can change over time; past relationships may not hold in the future.  
- Results depend on the selected time window (short vs. long term).  
- Market shocks (e.g., financial crises) may temporarily inflate correlations.  

## Lifecycle Mapping  
Goal → Stage → Deliverable  
- Define problem → Problem Framing & Scoping (Stage 01) → Scoping paragraph + README.md  
- Collect data → Data Collection (Stage 02) → Price history for selected tickers (CSV or API fetch)  
- Analyze relationships → Modeling (Stage 03) → Correlation coefficients + heatmap  
- Share results → Delivery (Stage 04) → Report or notebook with visuals and key takeaways  

## Repo Plan  
Folders: `/data/`, `/src/`, `/notebooks/`, `/docs/`  
Cadence: weekly commits aligned with lifecycle stages.  
