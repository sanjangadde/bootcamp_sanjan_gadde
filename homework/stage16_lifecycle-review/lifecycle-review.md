# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **1. Problem Framing & Scoping** | Stocks move together in correlation. I assumed that stocks of the same sector would have similar movements over a 3-month period. | Making a prediction based on three months of data was quite ambitious | Success was defined on a working model that provides a rough estimate with decent MSAE | Framing the project to include more input output usability would suit its goals better |
| **2. Tooling Setup** | python environment, sklearn, numpy & pandas. Essentially python libraries | Some issues with pyarrow compatibility with pip | switched to conda for a more advanced environment manager | The data collection was automated |
| **3. Python Fundamentals** | Data parsing and cleaning. | Using numpy and pandas was challenging | Learning numpy and pandas | Getting more familiar with numpy and pandas |
| **4. Data Acquisition / Ingestion** | Yahoo finance | The data came in all as multiple file | parsed data based on ticker and cleanly appeneding everything to one dataframe to output to csv | Definitely data formatting |
| **5. Data Storage** | CSV file | Reading data after storage was tricky since the data was organzied poorly | Keep everything in one csv file | Vertically seperating based on ticker |
| **6. Data Preprocessing** | Normalized data | The dates where in an improper format | Based on which would suit my model the based and preserving the data type (float64) | Organization better |
| **7. Outlier Analysis** | Using z-score and IQR | Certain sporadic volatile movements | Based on z-scoring and IQR | Possibly more advanced or statistically refined outlier definition |
| **8. Exploratory Data Analysis (EDA)** | Ratios of values in movement | Correlation was misleading since a 3-month period isn't long enough | Clarified based on industry practices | A longer time frame would help to get relative correlation |
| **9. Feature Engineering** | Correlation matrices | The correlation matrix was difficult to add since it didn't show a strong correlation which would have been better for the model | Validated features via use-cases in later stages | Possibly adding a volatility measure |
| **10. Modeling (Regression / Time Series / Classification)** | Time series (SVR) and linear regression | Had some overfitting with linear regression | Based on accuracy | A classification model that just classifies if the stocks will move with a greater correlation than X or not |
| **11. Evaluation & Risk Communication** | R^2 and MAE and MASE | Assuming a sector wide commonality and disregarding company independence | Via markdown files and acknowledgment | Evaluating based on metrics with binary output |
| **12. Results Reporting, Delivery Design & Stakeholder Communication** | Markdown files | The reason behind model choice | Charts and graphs of model performance | Adding a slide deck |
| **13. Productization** | Adding user friendly flask app | Broken pipe error and adding inputs from once machine to another | Pkl file instead of continously retraining model | A streamlit dashboard |
| **14. Deployment & Monitoring** | Via flask | Receiving metrics based on individual predictions and outputs | Based on logs | Continous retraining if the logs show poor performance |
| **15. Orchestration & System Design** | By considering which areas needed the most maintanence | packages being deprecated | Assigning certain teams for specific parts of the corresponding skillset and dependency of the pipeline | More logs and metric based solutions |
| **16. Lifecycle Review & Reflection** | Biggest takeaway: technical and non technical skills are equally important | non technical delivarables | Placing myself in perspective of the user | Definitely more thought out goal and framework from the start |

---

## Reflection Prompts

- Which stage was the most **difficult** for you, and why?  
Productization, requires knowing how the user is going to think
- Which stage was the most **rewarding**?  
Modeling, finally getting an output
- How do the stages **connect** — where did one stage’s decisions constrain or enable later stages?  
Data storage and processing influences your ability to use certain models
- If you repeated this project, what would you **do differently across the lifecycle**?  
Add more logs along the way to track progress and continously add more non-technical material
- Which skills do you most want to **strengthen** before your next financial engineering project?  
My UI/UX and basic presentation skills
---