# 🛒 Olist E-Commerce Business Intelligence & Predictive Analytics

### End-to-End Data Analytics, Business Intelligence & Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📖 Project Overview

This project presents an end-to-end Business Intelligence and Predictive Analytics solution using the **Olist Brazilian E-Commerce Public Dataset**.

The objective is to transform raw relational e-commerce data into actionable business insights through professional data analysis, visualization, feature engineering, and machine learning.

The project follows an industry-standard Data Analytics workflow commonly used by Data Analysts, Business Intelligence Analysts, and Data Scientists.

---

# ⭐ Project Highlights

- End-to-End Data Analytics Pipeline
- Multi-table Relational Database Analysis
- Professional Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Business Intelligence Reporting
- Feature Engineering
- Machine Learning Pipeline
- Modular Python Project Architecture
- Unit Testing with Pytest
- Git & GitHub Version Control

---

# 🎯 Objectives

- Understand the structure of relational datasets
- Assess overall data quality
- Handle missing values and inconsistent data
- Perform exploratory data analysis
- Generate business insights using KPIs
- Engineer predictive features
- Train and evaluate a Machine Learning model
- Deliver business recommendations based on analytical findings

---

# 📂 Dataset

**Dataset Name**

Olist Brazilian E-Commerce Public Dataset

The dataset contains information about:

- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Order Items
- Geolocation
- Product Category Translation

### Dataset Statistics

| Metric | Value |
|---------|------:|
| Orders | ~100,000 |
| Customers | ~99,000 |
| Order Items | ~112,000 |
| Sellers | ~3,000 |
| Products | ~33,000 |
| Reviews | ~99,000 |

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Machine Learning | Scikit-learn |
| Development | Jupyter Notebook, VS Code |
| Testing | Pytest |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```text
olist-ecommerce-business-intelligence/
│
├── assets/
│
├── config/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_quality_assessment.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   ├── 05_business_insights.ipynb
│   └── 06_feature_engineering.ipynb
│
├── reports/
│
├── src/
│   ├── data/
│   ├── dashboard/
│   ├── models/
│   ├── utils/
│   ├── visualization/
│   ├── config.py
│   └── logger.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🔄 Project Workflow

```text
                  Raw Data
                      │
                      ▼
          Data Understanding
                      │
                      ▼
      Data Quality Assessment
                      │
                      ▼
            Data Cleaning
                      │
                      ▼
     Exploratory Data Analysis
                      │
                      ▼
       Business Intelligence
                      │
                      ▼
       Feature Engineering
                      │
                      ▼
        Machine Learning
                      │
                      ▼
    Business Recommendations
```

---

# 📊 Project Modules

## 1️⃣ Data Understanding

- Dataset inspection
- Schema exploration
- Relationship identification
- Primary Key validation
- Foreign Key validation

---

## 2️⃣ Data Quality Assessment

- Missing Value Analysis
- Duplicate Detection
- Data Integrity Checks
- Consistency Validation

---

## 3️⃣ Data Cleaning

- Missing value treatment
- Datetime conversion
- Data preprocessing
- Clean dataset generation

---

## 4️⃣ Exploratory Data Analysis

Analysis performed:

- Monthly Order Trend
- Revenue Analysis
- Payment Analysis
- Customer Distribution
- Seller Performance
- Product Category Analysis
- Review Analysis
- Delivery Performance

---

## 5️⃣ Business Intelligence

Executive KPIs

- Revenue Analysis
- Orders Analysis
- Customer Insights
- Seller Performance
- Product Performance
- Logistics Analysis
- Customer Satisfaction

---

## 6️⃣ Feature Engineering

Created Features

- Delivery Days
- Approval Hours
- Purchase Month
- Purchase Day
- Purchase Weekday
- Purchase Hour
- Weekend Indicator
- Late Delivery Flag

---

## 7️⃣ Machine Learning

### Model Used

Random Forest Regressor

### Prediction Target

Delivery Time (Days)

### Feature Set

- Payment Value
- Payment Installments
- Purchase Month
- Purchase Day
- Purchase Weekday
- Purchase Hour
- Approval Hours

---

# 📈 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Feature Importance analysis was also performed to understand which variables contribute most to delivery time prediction.

---

# 💡 Key Business Insights

- Credit Card is the dominant payment method.
- Revenue is concentrated in a limited number of product categories.
- Customer demand is highly concentrated in major Brazilian states.
- Delivery performance directly impacts customer satisfaction.
- Seasonal purchasing trends influence monthly revenue.
- Seller performance varies significantly across the marketplace.

---

# 📌 Business Recommendations

- Improve logistics efficiency to reduce delivery delays.
- Optimize inventory for high-demand product categories.
- Strengthen partnerships with top-performing sellers.
- Expand marketing campaigns in high-revenue regions.
- Improve customer experience through faster delivery.

---

# 🧪 Testing

The project includes automated unit testing using **Pytest**.

Implemented Tests

- Data Loader
- Data Preprocessing
- Dataset Merge Functions
- Machine Learning Pipeline

**Current Status**

```
==============================
4 Tests Passed
==============================
```

---

# 🚀 Future Improvements

- Hyperparameter Tuning
- XGBoost
- LightGBM
- Streamlit Interactive Dashboard
- Power BI Dashboard
- FastAPI Prediction API
- Docker Deployment
- CI/CD using GitHub Actions

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/devil-hat00/olist-ecommerce-business-intelligence.git
```

Move into the project folder

```bash
cd olist-ecommerce-business-intelligence
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

Run notebooks sequentially

```
01 → 02 → 03 → 04 → 05 → 06
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Relational Data Analysis
- Exploratory Data Analysis
- Business Intelligence
- Data Visualization
- Feature Engineering
- Machine Learning
- Predictive Analytics
- Python Programming
- Software Engineering
- Git & GitHub
- Unit Testing

---

# 📈 Repository Statistics

- 9 Relational Datasets
- 100,000+ Orders
- 6 Analysis Notebooks
- Modular Python Package
- Machine Learning Pipeline
- Automated Testing
- Professional Project Structure

---

# 📬 Contact

## Tarun Sharma

**AI & Data Science Undergraduate**

### GitHub

https://github.com/devil-hat00

### LinkedIn

https://www.linkedin.com/in/tarun-sharma-45340a324/

---

## ⭐ If you found this project useful, please consider giving it a Star!

It helps support the project and encourages future development.