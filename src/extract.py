import os
import zipfile
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.config import RAW_ZIP_PATH, RAW_CSV_PATH, KAGGLE_DATASET, RAW_DATA_DIR
from src.utils import ensure_dir

def download_from_kaggle():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_file(
        dataset=KAGGLE_DATASET,
        file_name="orders.csv",
        path=RAW_DATA_DIR
    )

def extract_data(force_download=False):
    ensure_dir(RAW_DATA_DIR)
    if not os.path.exists(RAW_CSV_PATH) or force_download:
        if not os.path.exists(RAW_ZIP_PATH) or force_download:
            download_from_kaggle()
        with zipfile.ZipFile(RAW_ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(RAW_DATA_DIR)
    df = pd.read_csv(RAW_CSV_PATH, na_values=['Not Available', 'unknown'])
    return df
