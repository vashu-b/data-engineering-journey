import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Pipeline started")

    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()