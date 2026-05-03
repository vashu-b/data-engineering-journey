import logging

def transform(df):
    try:
        logging.info("Transforming data")
        df["revenue"] = df["revenue"] * 1.1
        return df
    except Exception as e:
        logging.error(f"Error in transformation: {e}")