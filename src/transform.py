import os
import pandas as pd
from src.config import PROCESSED_CSV_PATH, PROCESSED_DATA_DIR
from src.utils import ensure_dir

def transform_data(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    
    df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
    df['sale_price'] = df['list_price'] - df['discount']
    df['profit'] = df['sale_price'] - df['cost_price']
    
    df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")
    
    df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)
    
    ensure_dir(PROCESSED_DATA_DIR)
    df.to_csv(PROCESSED_CSV_PATH, index=False)
    
    return df
