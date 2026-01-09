# 🛒 Supermart Profit Prediction & Retail Analytics System

## 📌 Project Overview
This project focuses on building an end-to-end retail analytics and profit prediction system using historical supermarket sales data. The goal is to analyze business performance, understand key profit drivers, and deploy a machine learning model that enables real-time profit prediction for retail orders.

The solution combines **Excel, SQL, Python, Machine Learning, and Streamlit deployment**, simulating a real-world data science workflow.

---

Live Streamlit Link : https://supermart-profit-prediction-8mp7nhylbqu4vnjfozjbth.streamlit.app/

## 🎯 Business Problem
Retail businesses often struggle to estimate profit accurately due to:
- Varying discount strategies
- Seasonal demand
- Product and category differences
- Regional sales patterns

Incorrect pricing and discount decisions can directly impact profitability. Business teams need a predictive system to evaluate scenarios before execution.

---

## 🎯 Project Objectives
- Analyze historical supermarket sales data
- Identify factors influencing profitability
- Build machine learning models for profit prediction
- Compare baseline and advanced models
- Deploy an interactive dashboard for real-time business insights

---

## 📂 Dataset Description
The dataset includes supermarket transaction data with the following attributes:
- Order details (Order ID, Customer Name)
- Product information (Category, Sub-category)
- Location details (City, Region, State)
- Financial metrics (Sales, Discount, Profit)
- Time information (Order Date)

---

## 🛠 Tools & Technologies Used

| Tool | Purpose |
|---|---|
| Excel | Initial data understanding, validation, pivot analysis |
| SQL | Business-level aggregations and KPI analysis |
| Python (Pandas, NumPy) | Data cleaning, EDA, feature engineering |
| Scikit-learn | Machine learning model development |
| Random Forest | Profit prediction model |
| Streamlit | Interactive dashboard & deployment |
| GitHub | Version control and project hosting |

---

## 📊 Workflow & Methodology

### 1️⃣ Excel Analysis
- Reviewed raw data structure
- Checked missing values and outliers
- Created pivot tables for category-wise and region-wise performance
- Identified initial trends in sales, discount, and profit

### 2️⃣ SQL Analysis
- Performed grouped aggregations by category and region
- Identified top-performing and low-performing segments
- Validated business KPIs such as average discount and profit contribution

### 3️⃣ Data Cleaning & Preprocessing (Python)
- Standardized column names
- Converted data types
- Removed irrelevant columns
- Encoded categorical variables
- Prepared ML-ready dataset

### 4️⃣ Exploratory Data Analysis (EDA)
- Studied distributions of sales, profit, and discount
- Analyzed relationships such as discount vs profit
- Identified seasonal patterns

### 5️⃣ Feature Engineering
- Extracted year, month, and quarter
- Created weekend indicator
- One-hot encoded categorical variables

### 6️⃣ Machine Learning Models
- **Linear Regression** used as a baseline
- **Random Forest Regressor** used for non-linear relationships
- Models evaluated using MAE and R² score

### 7️⃣ Model Deployment
- Final model deployed using Streamlit Cloud
- Interactive UI allows users to input order details
- Real-time profit prediction with business insights

---

## 🚀 Streamlit Application Features
- Real-time profit prediction
- Scenario-based analysis (what-if discount changes)
- Business warnings for high discounts
- Clean, user-friendly dashboard for non-technical users

---

## 📈 Key Business Insights
- High discounts significantly reduce profit
- Certain categories consistently outperform others
- Sales volume is a major driver of profitability
- Profit prediction helps optimize pricing and promotions

---

## 🏁 Conclusion
This project demonstrates a complete data science lifecycle—from raw data analysis to model deployment. It highlights the importance of combining business understanding with technical skills to build practical, decision-support systems in retail analytics.

---

## 📎 Future Enhancements
- Add SHAP-based model explainability
- Improve prediction accuracy with additional cost data
- Extend dashboard with advanced analytics and charts
- Implement model monitoring and logging

---

## 📬 Contact
For feedback or collaboration, feel free to connect on LinkedIn.
