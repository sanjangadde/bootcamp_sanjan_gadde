# Model Communication Report

## 1. Model Performance Metrics
For the regression model (Linear Regression with standardized inputs), evaluation on the test set produced the following metrics:

- **MAE (Mean Absolute Error):** 0.2145  
- **MSE (Mean Squared Error):** 0.0552  
- **RMSE (Root Mean Squared Error):** 0.2350  
- **R² (Coefficient of Determination):** 0.0769  

**Interpretation:**  
- The MAE indicates that on average, predictions deviate from actual values by ~0.21 units.  
- The RMSE is slightly higher than MAE, showing some larger errors exist.  
- The R² score is low, suggesting the model explains only ~7.7% of the variance. This indicates limited predictive power under current assumptions and preprocessing.  

---

## 2. Uncertainty Visualizations

### Confidence Intervals (Bootstrap)
- Bootstrapped CIs around predictions highlight variability. Wider intervals appear in higher-variance regions, indicating more uncertainty.  
- Increasing bootstrap iterations (60 → 600 → 6000 → 60,000) stabilized interval estimates, improving confidence in the results.  

### Residual Plots
- Histogram of residuals approximates a normal distribution, though tails suggest outliers.  
- Residuals vs Predicted plot shows mild heteroscedasticity: variance increases slightly with prediction magnitude.  

### Side-by-Side Scenarios
**Scenario A:** Mean imputation of missing values → lower accuracy, higher RMSE.  
**Scenario B:** Median imputation → more stable, smaller errors.  
**Observation:** Outlier handling strongly influenced results; median imputation preserved predictive power better than mean imputation.  

---

## 3. Scenario & Sensitivity Analysis

- **Imputation Choice:**  
  - *Mean imputation* lowered returns and increased error variance.  
  - *Median imputation* provided more consistent, robust performance.  
- **Model Complexity:**  
  - *Linear regression* offered interpretability but limited fit.  
  - *Polynomial regression (2nd degree)* captured some nonlinearity but risked overfitting (slightly better R², but larger variance in bootstrap CI).  
- **Bootstrap vs Gaussian Residuals:**  
  - Gaussian assumptions understated tail risks.  
  - Bootstrapped CIs revealed wider uncertainty, especially in volatile regions.  

---

## 4. Written Discussion

### Key Assumptions
- Linearity between predictors and target.  
- Homoscedasticity (constant variance of residuals).  
- Normality of errors (approximate, but violated in tails).  
- Independence of observations (reasonable given dataset structure).  

### Risks & Limitations
- Low R² indicates limited explanatory power—model may not generalize well.  
- Imputation strategy has large influence; naive mean imputation biases outcomes.  
- Sharpe-like metrics may understate extreme risks (tail events).  
- Small sample size reduces robustness; results should be validated with larger data.  

### Scenario & Sensitivity Commentary
- Results show that preprocessing decisions (outlier handling, imputation) meaningfully affect financial conclusions.  
- Outlier treatment improves performance with little added volatility.  
- Median imputation balances robustness and predictive accuracy better than mean.  

### Subgroup Observations (Optional)
- No obvious subgroup risks found, but in applied contexts, subgroup imbalance (e.g., sector or demographic skew) could distort model performance.  

---

## 5. Stakeholder Communication (Optional, Plain-Language Summary)

- **Takeaway:** Data cleaning choices directly shape financial outcomes. Using mean imputation can understate performance and increase risk.  
- **Recommendation:** Use robust preprocessing (median imputation, outlier treatment) for better risk-adjusted results.  
- **Decision Framing:** If stakeholders rely on this model, they should view results as scenario-dependent, not absolute predictions. Transparency around assumptions is critical.  

---

## 6. Next Steps

- Incorporate lagged and rolling features for better time-series sensitivity.  
- Validate on a larger dataset to improve generalizability.  
- Explore advanced models (Ridge, SVR, tree-based regressors) while balancing interpretability.  
- Perform subgroup/stress testing to understand failure modes.  
