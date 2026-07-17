# Retail Orders: End-to-End Data Pipeline & Analytics

## Project Overview
This project represents a production-grade, industry-standard Python data engineering and analytics repository. It automates the ETL (Extract, Transform, Load) pipeline for retail order datasets, cleanses dirty raw data, ingests it into a MySQL database, and runs complex analytical queries with professional Jupyter notebook reporting.

## Key Features
1. **Automated Data Extraction**: Downloads datasets programmatically using the Kaggle API.
2. **Data Cleansing & Transformation**: Standardizes dirty headers into `snake_case`, handles missing values, and performs row-level feature engineering (`discount`, `sale_price`, and `profit`).
3. **Database Ingestion**: Modulary loads structured data into MySQL via SQLAlchemy.
4. **14 Analytical SQL Queries**: Includes window functions and CTEs to extract insights such as monthly sales trends, YoY growth, and top-selling products.
5. **Insights Visualizations**: Generates and saves visual reports into `outputs/figures/`.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: Pandas, SQLAlchemy, PyMySQL, Cryptography, Kaggle API, Python-dotenv, Matplotlib, Seaborn
- **Database**: MySQL

## Project Structure
```
sales-analysis/
│
├── data/
│   ├── raw/                  # Downloaded raw zip and extracted CSV
│   └── processed/            # Transformed dataset in CSV format
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb    # Ingestion and cleaning verification
│   ├── 02_sql_analysis.ipynb     # DB connection and 14 SQL queries execution
│   └── 03_visualizations.ipynb   # Visualization generation and saving
│
├── sql/                      # 14 extracted analytical SQL files
│
├── src/                      # ETL codebase package modules
│   ├── __init__.py
│   ├── config.py             # Reusable directory and dataset path configurations
│   ├── utils.py              # Log setups and utility helpers
│   ├── database.py           # Database connection and engine creation
│   ├── extract.py            # Extraction and validation
│   ├── transform.py          # Data cleansing and feature engineering
│   └── load.py               # SQL database loading
│
├── outputs/
│   ├── figures/              # Generated visualization charts (.png)
│   └── reports/              # Reports and exports
│
├── .env.example              # Database credential template
├── .gitignore                # Production git exclude list
├── README.md
├── requirements.txt          # Package dependencies
└── main.py                   # Reusable ETL pipeline orchestrator
```

## Setup & Ingestion

### 1. Prerequisites
Ensure your Kaggle API credentials file `kaggle.json` is located in your home `.kaggle/` directory.

### 2. Database Environment Setup
Copy the env template:
```bash
cp .env.example .env
```
Populate `.env` with your local MySQL database configurations.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run ETL Pipeline
Execute the pipeline to extract, transform, and load data into the database:
```bash
python main.py
```

## Analytics Notebooks
Run the Jupyter notebooks in order:
1. `notebooks/01_data_cleaning.ipynb` to verify data cleansing steps.
2. `notebooks/02_sql_analysis.ipynb` to execute the 14 SQL business questions.
3. `notebooks/03_visualizations.ipynb` to generate charts saved under `outputs/figures/`.
