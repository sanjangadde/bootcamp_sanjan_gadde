# Stakeholder Memo — Stock Correlation Explorer  

## Problem  
Retail investors often buy multiple stocks believing they are diversifying, but many of those stocks may move together due to sector exposure or broader market forces. Without a clear view of correlations, portfolios may be riskier than they appear.  

## Why It Matters  
Hidden correlations reduce diversification benefits and can amplify losses during market downturns. By identifying how closely stocks move together, investors can construct more resilient portfolios and make smarter allocation choices.  

## Proposed Solution  
1. **Collect historical stock prices** for user-selected tickers (via Yahoo Finance or similar APIs).  
2. **Calculate pairwise correlation coefficients** to quantify how each stock relates to others.  
3. **Visualize correlations** in an easy-to-read heatmap and matrix.  
4. **Summarize insights**, such as the most and least correlated stock pairs and the average portfolio correlation.  

## Stakeholder Impact  
- **Retail Investors:** Gain actionable insights into diversification, reducing unintentional overexposure.  
- **Financial Advisors:** Can use the tool to illustrate diversification concepts to clients.  
- **Students & Educators:** Provides a practical way to learn about correlation, risk, and portfolio theory.  

## Next Steps  
- Implement data ingestion from Yahoo Finance (`yfinance` library).  
- Test correlation calculations on a sample portfolio (e.g., 10–20 stocks).  
- Build heatmap visualizations and highlight key findings.  
- Package results in a simple notebook/report for investor use.  
