import logging
from extract import extract
from transform import transform
from load import load

logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Pipeline started")

    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
    