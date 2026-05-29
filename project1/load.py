import mysql.connector
import logging

def load(df):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vashup",
            database="ecommerce_analytics"
        )

        cursor = conn.cursor()

        for index, row in df.iterrows():
            cursor.execute(
                "INSERT INTO customers (first_name, revenue) VALUES (%s, %s)",
                (row["name"], row["revenue"])
            )

        conn.commit()
        logging.info("Data loaded into MySQL")

    except Exception as e:
        logging.error(f"Error loading data: {e}")