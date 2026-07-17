import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

RAW_ZIP_PATH = os.path.join(RAW_DATA_DIR, "orders.csv.zip")
RAW_CSV_PATH = os.path.join(RAW_DATA_DIR, "orders.csv")
PROCESSED_CSV_PATH = os.path.join(PROCESSED_DATA_DIR, "orders_processed.csv")

KAGGLE_DATASET = "ankitbansal06/retail-orders"
DB_TABLE_NAME = "df_orders"

SQL_DIR = os.path.join(BASE_DIR, "sql")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
FIGURES_DIR = os.path.join(OUTPUT_DIR, "figures")
REPORTS_DIR = os.path.join(OUTPUT_DIR, "reports")
