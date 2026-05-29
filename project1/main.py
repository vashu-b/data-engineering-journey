import logging
from extract import extract
from transform import transform
from validate import validate_data
from load import load

logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    try:
        logging.info("Pipeline started")

        df = extract()
        df = validate_data(df)
        df = transform(df)
        load(df)

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()