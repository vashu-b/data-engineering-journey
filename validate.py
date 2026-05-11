import logging

def validate_data(df):
    logging.info("Validating data")

    if df.empty:
        raise ValueError("Validation failed: CSV file is empty")

    if df["name"].isnull().any():
        raise ValueError("Validation failed: Missing customer name found")

    if df["revenue"].isnull().any():
        raise ValueError("Validation failed: Missing revenue found")

    if (df["revenue"] < 0).any():
        raise ValueError("Validation failed: Negative revenue found")

    logging.info("Data validation passed")
    return df