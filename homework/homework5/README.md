# ESG Fund Transparency Analyzer  
**Stage:** Problem Framing & Scoping (Stage 01)  

## Problem Statement  
Many ESG-labeled (Environmental, Social, Governance) funds hold companies that conflict with their stated sustainability goals — such as firms with high carbon emissions, significant fossil fuel revenue, or repeated controversies. Investors who want their portfolios to reflect their values often cannot easily verify whether a fund’s holdings are consistent with its ESG label. This project addresses that gap by creating a tool that ingests fund holdings and benchmarks them against clear ESG metrics, producing a transparency score and flagging potential “greenwashing.”  

## Stakeholder & User  
- **Primary Stakeholder:** Socially conscious retail investors deciding which funds to purchase.  
- **Secondary Stakeholders:** Financial advisors, fintech apps, and analysts concerned with sustainable investing.  
- **Context:** Used when investors compare funds during portfolio selection or conduct periodic ESG reviews.  

## Useful Answer & Decision  
- **Type:** Descriptive scoring with prescriptive signals (e.g., red flags).  
- **Output:** A transparency score (0–100) with sub-scores for carbon intensity, controversies, and excluded sectors.  
- **Artifact:** Scorecard and report (CSV/PDF) showing fund alignment and highlighting problematic holdings.  

## Assumptions & Constraints  
- Input data: fund holdings with tickers/weights; metrics joined from public ESG datasets.  
- Analysis is holdings-based (no live market data needed).  
- ESG definitions vary by jurisdiction; rubric focuses on transparency, not compliance with regulations.  
- Must run quickly (seconds) on portfolios of ~1,000 holdings.  
- Some data may be missing or stale between disclosure dates.  

## Known Unknowns / Risks  
- Inconsistent disclosure frequency across funds may reduce accuracy.  
- Data quality varies across regions and vendors.  
- Ticker/identifier mismatches may cause gaps in scoring.  
- Shifts in ESG standards (e.g., new exclusions) may require rubric updates.  

## Lifecycle Mapping  
Goal → Stage → Deliverable  
- Define problem → Problem Framing & Scoping (Stage 01) → Scoping paragraph + README.md  
- Build data pipeline → Data Collection (Stage 02) → Holdings + ESG metrics schema  
- Design scoring rubric → Modeling (Stage 03) → Fund transparency scoring system  
- Deliver results → Delivery (Stage 04) → Scorecard reports and stakeholder memo  

## Repo Plan  
Folders: `/data/`, `/src/`, `/notebooks/`, `/docs/`  
Cadence: weekly commits aligned with lifecycle milestones.  

## Data Storage
Folders: `/data/raw/`, `/data/processed/`  
Format: descriptor_date_time  
Important to differentiate between testing and used data. 
Reads and writes using .env file paths specified.