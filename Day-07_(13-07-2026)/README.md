# Sustainable Energy Analysis using K-Means Clustering

## Project Overview

This project applies the **K-Means Clustering** algorithm to a global sustainable energy dataset to identify groups of countries with similar environmental and economic characteristics.

The analysis includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Selection
- Data Scaling
- K-Means Clustering
- Cluster Visualization
- Model Evaluation using the Silhouette Score

This project demonstrates how **unsupervised machine learning** can discover hidden patterns in sustainability data without requiring predefined labels.

---

## Dataset

**Dataset Name:** Global Data on Sustainable Energy

The dataset contains sustainability indicators for countries worldwide, including:

- Country
- Year
- Access to Electricity
- Renewable Electricity Generating Capacity
- Renewable Energy Share
- CO₂ Emissions
- GDP per Capita
- Population
- Density
- Land Area
- Latitude & Longitude

---

## Project Objectives

- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Select relevant sustainability indicators.
- Standardize the data using StandardScaler.
- Determine the optimal number of clusters using the Elbow Method.
- Apply K-Means Clustering.
- Evaluate the clustering performance using the Silhouette Score.
- Visualize and interpret the generated clusters.

---

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Machine Learning Algorithm

**Algorithm:** K-Means Clustering

**Learning Type:** Unsupervised Learning

K-Means automatically groups similar countries based on sustainability indicators without requiring labeled data.

---

## Features Used

The following features were selected for clustering:

- Access to electricity (% of population)
- Renewable electricity generating capacity per capita
- Renewable energy share in total final energy consumption (%)
- CO₂ emissions (kt)
- GDP per capita

These indicators represent the environmental, energy, and economic characteristics of each country.

---

## Exploratory Data Analysis (EDA)

The following visualizations were created:

- Correlation Heatmap
- Histograms
- Scatter Plot
- Cluster Count Plot

These visualizations helped understand relationships among features, detect outliers, and analyze data distributions before clustering.

---

## Data Preprocessing

The following preprocessing steps were performed:

- Removed duplicate records
- Handled missing values
- Selected relevant numerical features
- Standardized features using **StandardScaler**

Feature scaling ensures that all variables contribute equally during distance calculations in K-Means.

---

## Determining the Number of Clusters

The **Elbow Method** was used to determine the optimal number of clusters.

Based on the elbow curve, the optimal value was:

**K = 5**

---

## Model Training

The K-Means model was trained using:

- Number of Clusters: **5**
- Random State: **42**
- Feature Scaling: **StandardScaler**

---

## Model Evaluation

The clustering model was evaluated using the **Silhouette Score**.

**Silhouette Score:** **0.49**

A score of **0.49** indicates that the generated clusters are reasonably well separated and represent meaningful groupings within the dataset.

---

## Results

The K-Means algorithm successfully grouped countries into **five sustainability clusters** based on:

- Economic Development
- Renewable Energy Usage
- Electricity Access
- CO₂ Emissions
- GDP per Capita

These clusters help identify countries with similar sustainability characteristics and can support comparative environmental analysis and policy planning.


## Conclusion

This project demonstrates how **K-Means Clustering** can be applied to sustainability data to identify meaningful patterns among countries.

By analyzing indicators such as GDP per capita, renewable energy adoption, electricity access, and CO₂ emissions, countries were grouped into five distinct clusters representing different sustainability profiles.

The **Elbow Method** identified the optimal number of clusters, while the **Silhouette Score (0.49)** confirmed that the clustering quality is good.


