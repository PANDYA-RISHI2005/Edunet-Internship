# World Sustainability Dataset – Data Cleaning and Analysis

## Project Overview

This project demonstrates the complete data preprocessing and analysis workflow using the **World Sustainability Dataset**. The dataset contains environmental, economic, and social sustainability indicators for countries across multiple years.

The objective of this project is to clean the dataset, handle missing values, perform feature engineering, visualize important patterns, encode categorical variables, scale numerical features, and prepare the data for further analysis or machine learning.

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Tasks Performed

- Imported the World Sustainability Dataset using Pandas.
- Explored the dataset using `head()`, `info()`, `shape()`, and `describe()`.
- Checked for duplicate records and removed them.
- Identified missing values and visualized them using a Seaborn heatmap.
- Filled missing numerical values using the median.
- Filled missing categorical values using the mode.
- Performed feature engineering by creating a **Trade Balance** feature.
- Visualized the dataset using Seaborn (Missing Value Heatmap and GDP Histogram).
- Encoded categorical columns using `pd.get_dummies()`.
- Applied `StandardScaler` to numerical columns.
- Analyzed relationships between important sustainability indicators.

## Feature Engineering

A new feature named **Trade Balance** was created using the formula:

```
Trade Balance = Exports (% of GDP) - Imports (% of GDP)
```

This feature provides a simple indicator of a country's trade performance.

## Missing Value Handling

- Numerical columns were filled using the **median**.
- Categorical columns were filled using the **mode**.

## Data Preprocessing

- Missing values handled
- Duplicate records removed
- Feature engineering completed
- Categorical variables encoded using `pd.get_dummies()`
- Numerical features standardized using `StandardScaler`


## Conclusion

The World Sustainability Dataset was successfully cleaned and preprocessed. Missing values were handled appropriately, categorical variables were encoded, numerical features were standardized, and a new feature (**Trade Balance**) was engineered. The processed dataset is now ready for further analysis and machine learning applications.
