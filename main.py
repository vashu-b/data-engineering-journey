import pandas as pd
import mysql.connector

def extract():
    try:
        df = pd.read_csv("sales.csv")
        print("Data extracted")
        return df
    except Exception as e:
        print("Error in extraction:", e)

def transform(df):
    try:
        df["revenue"] = df["revenue"] * 1.1
        print("Data transformed")
        return df
    except Exception as e:
        print("Error in transformation:", e)

def load(df):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vashup",
            database="ecommerce_analytics"
        )
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute(
                "INSERT INTO customers (first_name, revenue) VALUES (%s, %s)",
                (row["name"], row["revenue"])
            )

        conn.commit()
        print("Data loaded into MySQL")

    except Exception as e:
        print("Error in loading:", e)

def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()