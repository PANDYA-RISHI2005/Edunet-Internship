# Sustainable Power Evaluation using Linear Regression

## Project Overview

This project analyzes a Sustainable Power Evaluation dataset to understand the factors affecting a company's Sustainability Score. The dataset contains financial, operational, environmental, and social indicators that are used to build a Linear Regression model for predicting sustainability performance.

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model building, and evaluation.

---

## Dataset Information

- **Dataset Name:** Sustainable Power Evaluation
- **Total Records:** 1000
- **Total Features:** 19
- **Target Variable:** Sustainability Score
- **Dataset Type:** Structured Tabular Data

### Features

- Company_ID
- Revenue (USD)
- Net Profit Margin (%)
- Investment in R&D (%)
- Market Share (%)
- Debt-to-Equity Ratio
- Energy Efficiency (%)
- Smart Grid Implementation Score
- Innovation Index
- Digitalization Level (%)
- Carbon Offset
- Renewable Energy Share (%)
- Emissions Intensity
- Waste Management Score
- Employee Satisfaction Score
- Community Development Investment
- Workforce Diversity Index
- Sustainability Certification
- Sustainability Score

---

## Project Objectives

- Understand the dataset and analyze feature relationships.
- Handle missing values using Mean Imputation.
- Perform exploratory data analysis using Seaborn.
- Apply feature engineering where necessary.
- Scale numerical features using StandardScaler.
- Split the dataset into training and testing sets.
- Build a Linear Regression model.
- Predict Sustainability Score.
- Evaluate model performance using regression metrics.

---

## Data Preprocessing

The following preprocessing steps were performed:

- Removed the Company_ID column since it is only an identifier.
- Handled approximately 10% missing values using Mean Imputation.
- Encoded categorical variables (if present).
- Applied StandardScaler to normalize numerical features.
- Split the dataset into 80% training data and 20% testing data.

---

## Exploratory Data Analysis

Several visualizations were created using the Seaborn library:

- Correlation Heatmap
- Distribution Plot
- Box Plot
- Pair Plot
- Histogram
- Actual vs Predicted Scatter Plot

These visualizations helped identify relationships among variables and detect possible outliers.

---

## Machine Learning Model

### Algorithm Used

- Linear Regression

The model predicts the Sustainability Score based on the remaining company features.

---

## Model Evaluation

The model performance was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

A higher R² Score and lower error values indicate better model performance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Project Structure

```
Project/
│
├── sustainable_power_evaluation.csv
├── Sustainable_Power_Regression_Analysis.ipynb
├── Linear_Regression_Predictions.csv
├── README.md
```

---

## Key Insights

- Energy Efficiency positively influences Sustainability Score.
- Renewable Energy Share has a strong positive relationship with sustainability.
- Carbon Offset contributes positively toward sustainability performance.
- Emissions Intensity negatively impacts Sustainability Score.
- Revenue and Net Profit Margin indirectly support sustainability through increased investment capacity.
- Company_ID does not contribute to prediction and was removed.

---

## Conclusion

The Sustainable Power Evaluation dataset was successfully analyzed using Linear Regression. Data preprocessing, visualization, feature scaling, and model evaluation were completed successfully. The developed model demonstrates how financial, operational, environmental, and social indicators collectively influence a company's Sustainability Score.

---

