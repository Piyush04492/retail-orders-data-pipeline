# Retail Orders: End-to-End Data Pipeline & Analytics

## 📋 Project Overview
This project demonstrates a full-cycle data engineering and analytics workflow. It handles the challenges of "dirty" raw data, automates ETL (Extract, Transform, Load) processes using Python, and utilizes SQL for complex business logic.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, SQLAlchemy, Kaggle API, Zipfile
- **Database:** Microsoft SQL Server (T-SQL)
- **Environment:** Jupyter Notebook / Anaconda

## 🚀 Key Features
1. **Automated Data Extraction:** Directly fetching datasets using the Kaggle API for a reproducible workflow.
2. **Data Cleaning & Preprocessing:** - Handling specialized null values (e.g., 'Not Available', 'Unknown').
   - Standardizing column headers to `snake_case`.
   - Dynamic data type conversion (e.g., Objects to Datetime).
3. **Feature Engineering:** Calculating new metrics like `Discount`, `Sale Price`, and `Profit` at the row level.
4. **Database Integration:** Loading cleaned data into SQL Server with optimized data types via SQLAlchemy.
5. **Advanced SQL Analytics:** - Month-over-Month (MoM) growth comparisons.
   - Using **CTEs** and **Window Functions** to find top-performing products by region and category.

## 📂 Project Structure
- `data_pipeline.ipynb`: Python script for API connection, data cleaning, and SQL loading.
- `analysis_queries.sql`: SQL scripts for solving core business questions.
- `requirements.txt`: Necessary Python libraries.

## 🔧 Setup & Usage
1. **Kaggle Credentials:** Ensure your `kaggle.json` is located in your `.kaggle` folder (typically `C:\Users\<User>\.kaggle\`).
2. **Database Connection:** Update the `create_engine` string in the Python script with your local SQL Server name.
3. **Execution:** - Run the Jupyter Notebook to download, clean, and export the data.
   - Run the SQL scripts in SQL Server Management Studio (SSMS) to generate insights.

## 📈 Sample Insights Included
- **Growth Analysis:** Which subcategories saw the highest profit increase from 2022 to 2023.
- **Regional Performance:** Identifying the top 5 highest-selling products specific to each geographic region.

---
*Inspired by the data engineering tutorials by Ankit Bansal.*
