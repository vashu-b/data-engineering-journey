# Azure Data Factory ETL Pipeline Project

## Project Overview
This project demonstrates an end-to-end ETL pipeline using Azure Data Factory, Azure Blob Storage, and Azure SQL Database.

The pipeline extracts CSV data from Azure Blob Storage, transforms and loads it into Azure SQL Database using Azure Data Factory Copy Activity.

---

## Architecture

Blob Storage (CSV)
        ↓
Azure Data Factory Pipeline
        ↓
Azure SQL Database

---

## Technologies Used

- Azure Data Factory
- Azure Blob Storage
- Azure SQL Database
- SQL
- ETL Pipeline
- Data Integration

---

## Project Workflow

### Step 1 — Upload Source Data
CSV file (`sales.csv`) uploaded into Azure Blob Storage container.

### Step 2 — Create Linked Services
Connected:
- Azure Blob Storage
- Azure SQL Database

### Step 3 — Create Datasets
Created:
- Source dataset (CSV)
- Sink dataset (Azure SQL)

### Step 4 — Build ETL Pipeline
Used Copy Data activity in Azure Data Factory.

### Step 5 — Execute Pipeline
Successfully copied data from Blob Storage to Azure SQL Database.

### Step 6 — Validate Data
Verified records using SQL queries.

---

## Screenshots

### Blob Storage Container
![Blob Storage](screenshots/blob_container.png)

### Linked Services
![Linked Services](screenshots/linked_services.png)

### Datasets
![Datasets](screenshots/datasets.png)

### Pipeline Success
![Pipeline Success](screenshots/pipeline_success.png)

### SQL Table Data
![SQL Table](screenshots/sql_table_data.png)

### SQL Count Validation
![SQL Count](screenshots/sql_count.png)

---

## SQL Validation Queries

```sql
SELECT * FROM customer_data;

SELECT COUNT(*) FROM customer_data;
```

---

## Learning Outcomes

- Built cloud-based ETL pipeline
- Connected Azure services
- Understood Linked Services and Datasets
- Performed data ingestion into Azure SQL
- Executed and monitored ADF pipelines
- Validated transformed data using SQL

---

## Author

Vashu Bhagat  
