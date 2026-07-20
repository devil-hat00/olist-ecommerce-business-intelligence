# 🛒 Olist E-Commerce Business Intelligence & Predictive Analytics

An end-to-end Data Analytics and Machine Learning project built using the **Olist Brazilian E-Commerce Public Dataset**. This project demonstrates the complete analytics lifecycle—from raw data exploration and cleaning to business intelligence reporting, feature engineering, and predictive modeling.

---

## 📖 Project Overview

The Olist marketplace connects customers with sellers across Brazil. This project analyzes transactional, customer, seller, payment, review, and product data to uncover business insights and build a machine learning model for predicting delivery time.

The project follows an industry-standard analytics workflow suitable for data analyst and data science portfolios.

---

## 🎯 Objectives

- Understand and assess the quality of raw datasets.
- Clean and preprocess multi-table relational data.
- Perform Exploratory Data Analysis (EDA).
- Generate business insights using KPI-based reporting.
- Engineer meaningful features for predictive modeling.
- Train and evaluate a machine learning model to predict delivery time.
- Present actionable recommendations for business decision-making.

---

## 📂 Dataset

**Dataset:** Olist Brazilian E-Commerce Public Dataset

The dataset contains information on:

- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Order Items
- Geolocation
- Product Category Translation

Key characteristics:

- ~100,000 orders
- ~99,000 customers
- ~112,000 order items
- Multiple related tables linked using primary and foreign keys

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```text
olist-ecommerce-business-intelligence/
│
├── assets/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_quality_assessment.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_exploratory_data_analysis.ipynb
│   ├── 05_business_insights.ipynb
│   └── 06_feature_engineering.ipynb
├── reports/
├── src/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Project Workflow

```
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

# 📊 Key Analyses Performed

### Data Understanding
- Dataset inspection
- Schema exploration
- Relationship identification
- Primary and foreign key validation

### Data Quality Assessment
- Missing value analysis
- Duplicate detection
- Data integrity checks
- Consistency validation

### Data Cleaning
- Missing value handling
- Datetime conversion
- Dataset preprocessing
- Clean dataset generation

### Exploratory Data Analysis
- Order trends
- Revenue analysis
- Payment analysis
- Customer behavior
- Seller performance
- Product category analysis
- Delivery performance
- Review analysis

### Business Intelligence
- Executive KPIs
- Revenue by state
- Revenue by product category
- Seller performance
- Customer satisfaction
- Logistics performance
- Strategic recommendations

### Machine Learning
- Feature engineering
- Delivery time prediction
- Random Forest Regression
- Model evaluation
- Feature importance analysis

---

# 📈 Key Business Insights

- The marketplace generates significant revenue through a limited number of product categories.
- Credit cards are the dominant payment method.
- Customer demand is concentrated in a few Brazilian states.
- Delivery performance strongly influences customer satisfaction.
- Seller performance varies considerably across the marketplace.
- Seasonal purchasing patterns affect monthly revenue.

---

# 🤖 Machine Learning Model

**Model Used**

- Random Forest Regressor

**Prediction Target**

- Delivery Time (Days)

**Engineered Features**

- Payment Value
- Payment Installments
- Purchase Month
- Purchase Day
- Purchase Weekday
- Purchase Hour
- Approval Time

---

# 📊 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Feature importance analysis was performed to identify the variables contributing most to delivery time prediction.

---

# 💡 Business Recommendations

- Improve logistics efficiency to reduce delivery times.
- Increase inventory for high-demand product categories.
- Focus marketing efforts on high-revenue regions.
- Strengthen partnerships with top-performing sellers.
- Enhance customer satisfaction through faster order fulfillment.

---

# 🚀 Future Improvements

- Hyperparameter tuning
- XGBoost and LightGBM comparison
- Interactive Power BI dashboard
- Streamlit web application
- Real-time prediction API using FastAPI

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/olist-ecommerce-business-intelligence.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Run the notebooks sequentially from **01** to **06**.

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis
- Business Intelligence
- Data Visualization
- Feature Engineering
- Machine Learning
- Predictive Analytics
- Python Programming
- Git Version Control

---

# 👨‍💻 Author

**Your Name**

AI & Data Science Undergraduate

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## ⭐ If you found this project useful, consider giving it a star!