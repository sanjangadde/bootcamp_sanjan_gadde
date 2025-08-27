# Model Evaluation Memo

## Problem Setup
The task was to evaluate a regression model for predicting continuous outcomes from time series–like data. The model chosen was a **Linear Regression** within a standardized pipeline.  
We assessed model performance, tested assumptions, and visualized residuals to understand risks and limitations.

---

## Methods
- **Model:** Linear Regression (with `StandardScaler`)  
- **Validation:** Train/test split with regression metrics (MAE, MSE, RMSE, R²)  
- **Uncertainty Analysis:** Bootstrap confidence intervals and residual visualization  
- **Scenario Analysis:** Compared mean vs. median imputation and polynomial vs. linear fits  

---

## Results

### Performance Metrics
- MAE: **0.2145**  
- MSE: **0.0552**  
- RMSE: **0.2350**  
- R²: **0.0769**

Interpretation: Model predictions deviate by ~0.21 units on average. The R² score indicates weak explanatory power.

---

### Charts

**Predicted vs True**
![Predicted vs True](0ac0ff7c-a29e-4056-b328-202af216cf56.png)

**Predicted vs True (Hexbin Density)**
![Predicted vs True (Hexbin Density)](fceffd47-c3d8-4c3f-aa79-31a15f1b4399.png)

**Residual Distribution**
![Residual Distribution](41aa52dc-d104-4340-8380-dc474c748ce0.png)

**Residuals vs Predicted**
![Residuals vs Predicted](2b72a0d9-e81b-4219-bbf9-3ddb61b90c1d.png)

---

## Assumptions & Risks
- **Linearity:** Assumes linear relationships between predictors and target. Violations may explain low R².  
- **Homoscedasticity:** Residuals show mild heteroscedasticity—variance grows with predictions.  
- **Normality:** Residuals roughly bell-shaped, but outliers present in tails.  
- **Independence:** Assumed valid given dataset, though time-dependence may violate this.  

**Risks:**  
- Over-reliance on linear assumptions underrepresents nonlinear effects.  
- Small sample size undermines generalizability.  
- Imputation strategies strongly influence performance (median > mean).  

---

## Conclusions
- The linear regression provides interpretability but limited predictive power.  
- Outlier treatment and robust imputation improve stability.  
- Bootstrapped uncertainty shows that Gaussian residual assumptions underestimate risks.  

---

## Recommendations
- Add lagged/rolling features for time-series sensitivity.  
- Test nonlinear models (Ridge, SVR, tree-based) for better fit.  
- Validate on larger datasets.  
- Use stress tests and subgroup analyses to evaluate robustness.  

---

## Appendix (Optional)
- Scenario sensitivity: Median imputation and polynomial fits yield modest improvements, but at risk of overfitting.  
- Stakeholder framing: **“Data cleaning choices directly affect financial predictions. Results should be communicated as scenario-dependent rather than absolute forecasts.”**  
