import pandas as pd
import logging

def extract():
    try:
        logging.info("Reading CSV file")
        df = pd.read_csv("sales.csv")
        return df
    except Exception as e:
        logging.error(f"Error in extraction: {e}")