# Customer Data Pipeline

## Overview
This project demonstrates an end-to-end data pipeline built using Python, Pandas, and MySQL. The pipeline reads raw data from a CSV file, performs transformations, and loads the processed data into a structured database.

## Problem
Raw CSV data is not directly usable for analysis. It needs cleaning, structuring, and storage in a database.

## Approach
ETL process:
- Extract: Read CSV using Pandas  
- Transform: Clean data and adjust revenue  
- Load: Insert into MySQL  

## SQL Analysis

The following query was used to analyze customer revenue:

SELECT first_name, SUM(revenue) AS total_revenue
FROM customers
GROUP BY first_name
ORDER BY total_revenue DESC;

This analysis identifies top-performing customers based on total revenue, enabling better business decision-making.

### Output

![SQL Output](sql_output.png.png)

## Tech Stack
- Python  
- Pandas  
- MySQL  
- SQL  
- Git  

## Implementation Details

### Data Extraction
Read CSV using Pandas into a DataFrame.

### Data Transformation
Adjusted revenue and cleaned dataset.

### Data Loading
Inserted processed data into MySQL using connector.

## Project Structure
project1/
│── extract.py  
│── transform.py  
│── load.py  
│── main.py  
│── sales.csv  
│── sql_analysis.png  
│── README.md  

## SQL Analysis

```sql
SELECT 
    SUM(revenue) AS total_revenue,
    AVG(revenue) AS avg_revenue
FROM customers;