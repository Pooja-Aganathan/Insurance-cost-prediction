# Insurance Cost Prediction

## Project Overview

This project aims to predict individual medical insurance charges using machine learning regression models. Insurance companies rely on predictive analytics to estimate healthcare expenses and determine pricing strategies.

The objective is to build and compare multiple machine learning models to accurately predict insurance costs based on customer demographics and health-related attributes.

---

## Problem Statement

Insurance providers need accurate cost prediction models to estimate future medical expenses and optimize premium pricing.

This project predicts medical insurance charges using features such as:

- Age
- Gender
- BMI (Body Mass Index)
- Smoking Status
- Number of Children
- Region

---

## Dataset Description

Dataset contains 1338 observations and multiple numerical and categorical features.

Features:

- age → Age of beneficiary
- sex → Gender
- bmi → Body Mass Index
- children → Number of dependents
- smoker → Smoking status
- region → Residential region
- charges → Medical insurance cost (Target Variable)

---

## Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Duplicate Handling
4. Outlier Analysis
5. Data Preprocessing
6. Feature Encoding
7. Feature Scaling
8. Model Training
9. Hyperparameter Tuning
10. Model Comparison
11. Model Evaluation

---

## Feature Engineering & Data Preparation

### Duplicate Removal

Duplicate records were identified and removed to improve data quality.

### Outlier Analysis

Outliers were analyzed carefully before modeling to maintain realistic healthcare cost patterns.

### Feature Encoding

Categorical variables were transformed using encoding techniques.

Examples:

- Sex
- Smoker
- Region

### Feature Scaling

StandardScaler was applied for numerical feature normalization.

---

## Models Used

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor
- LightGBM Regressor

---

## Hyperparameter Tuning

Model optimization techniques:

- GridSearchCV
- RandomizedSearchCV

These methods improved model performance by identifying optimal parameter configurations.

---

## Model Evaluation Metrics

Regression models were evaluated using:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Model Comparison

Multiple regression models were trained and compared to identify the best production-ready solution.

Tree-based ensemble methods demonstrated strong predictive capability for insurance charge estimation.

---

## Key Insights

- Smoking status significantly influences insurance charges
- BMI contributes strongly to healthcare expenses
- Age impacts insurance cost prediction
- Tree-based models outperform baseline regression approaches

---

## Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

XGBoost

LightGBM

---

## Project Structure

insurance-cost-prediction

├── README.md

├── requirements.txt

├── data/

├── notebooks/

├── src/

├── models/

└── reports/

---

## Business Impact

This solution can help insurance providers:

- Improve premium estimation
- Reduce pricing risk
- Enhance financial planning
- Support data-driven insurance decisions

---

## Future Improvements

- Advanced feature engineering
- Model deployment using APIs
- Explainable AI techniques
- Dashboard integration

---

## Conclusion

This project demonstrates how machine learning regression models can be applied to healthcare insurance pricing problems. Multiple models were evaluated and optimized to identify effective approaches for insurance charge prediction.

---

