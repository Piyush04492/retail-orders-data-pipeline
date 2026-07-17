import pandas as pd
from src.config import DB_TABLE_NAME

def load_data(df, engine):
    df.to_sql(
        name=DB_TABLE_NAME,
        con=engine,
        index=False,
        if_exists='replace'
    )
