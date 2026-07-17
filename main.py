import logging
from src.utils import setup_logging
from src.extract import extract_data
from src.transform import transform_data
from src.database import get_db_engine
from src.load import load_data

def main():
    setup_logging()
    
    logging.info("Starting ETL Pipeline")
    
    df = extract_data()
    logging.info("Data extracted successfully")
    
    df = transform_data(df)
    logging.info("Data transformed successfully")
    
    engine = get_db_engine()
    load_data(df, engine)
    logging.info("Data loaded to database successfully")
    
    logging.info("ETL Pipeline completed successfully")

if __name__ == "__main__":
    main()
