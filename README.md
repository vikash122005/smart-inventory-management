# Smart Inventory Management System

A data-driven inventory management system designed for small retail businesses to replace manual Excel-based inventory tracking with a structured, automated, and analytics-driven solution.

The system ingests historical sales and inventory data, validates and transforms it using Python and Pandas, stores the cleaned data in PostgreSQL, provides SQL-based analytics through a Streamlit dashboard, and supports live sales transactions with automatic stock updates and inventory alerts.

---

## Project Overview

Small retail businesses often manage products, sales, and inventory using spreadsheets. As the amount of data grows, this can lead to:

* Manual data entry errors
* Duplicate or inconsistent records
* Difficult inventory tracking
* Delayed identification of low-stock products
* Limited sales analysis
* Difficulty predicting the impact of increased demand

This project addresses these problems by building an end-to-end data pipeline and inventory management application.

### Core Workflow

```text
Excel / CSV Data
       ↓
Data Ingestion
       ↓
Data Validation
       ↓
Data Cleaning & Transformation
       ↓
PostgreSQL Database
       ↓
SQL Analytics
       ↓
Streamlit Dashboard
       ↓
Inventory Insights
```

Live sales follow a separate workflow:

```text
Sales Entry
     ↓
Validate Sale
     ↓
PostgreSQL
     ↓
Reduce Inventory
     ↓
Update Dashboard
     ↓
Low-Stock / Reorder Alert
```

---

## Features

### 1. Data Ingestion

* Loads product, sales, and inventory data from CSV files
* Supports structured historical datasets
* Provides a reusable ingestion pipeline

### 2. Data Validation

The validation layer checks for:

* Duplicate product IDs
* Duplicate sale IDs
* Missing product information
* Invalid product prices
* Invalid reorder levels
* Invalid lead times
* Invalid sales quantities
* Invalid inventory quantities
* Invalid product references
* Referential integrity issues

Invalid records are identified before entering the database.

### 3. Data Cleaning & Transformation

The pipeline performs:

* Column-name cleaning
* Invalid-row removal
* Duplicate removal
* Data-type conversion
* Data normalization
* Referential integrity checks

Clean data is then prepared for database storage.

### 4. PostgreSQL Database

The system uses PostgreSQL as the central database.

Main tables:

```text
Products
   │
   ├── Sales
   │
   └── Inventory
```

### Products

Stores:

* Product ID
* Product name
* Category
* Unit price
* Reorder level
* Lead time

### Sales

Stores:

* Sale ID
* Product ID
* Sale date
* Quantity sold

### Inventory

Stores:

* Product ID
* Current stock

Foreign-key relationships are used to maintain data integrity.

---

## SQL Analytics

The project contains a dedicated SQL analytics layer for extracting business insights.

Examples include:

* Total number of products
* Total sales
* Total quantity sold
* Current inventory
* Low-stock products
* Stock status
* Top-selling products
* Sales by category
* Product revenue
* Category revenue
* Inventory value
* Products requiring restocking
* High-stock / low-selling products

---

## Streamlit Dashboard

The Streamlit dashboard provides a visual interface for monitoring inventory and sales performance.

### Dashboard KPIs

* Total Products
* Total Sales
* Total Quantity Sold
* Inventory Value

### Visualizations

* Current inventory by product
* Top-selling products
* Sales by category
* Inventory status
* Low-stock alerts
* Reorder intelligence

> **Dashboard Screenshot**

<img width="1912" height="793" alt="Screenshot 2026-10-05 093647" src="https://github.com/user-attachments/assets/e539de4c-0766-48b3-a812-fa8715acad87" />
<img width="1217" height="519" alt="Screenshot 2026-10-05 093658" src="https://github.com/user-attachments/assets/f637dc58-8ab4-4388-bfac-1fddc904c569" />
<img width="1221" height="549" alt="Screenshot 2026-10-05 093712" src="https://github.com/user-attachments/assets/8a099fde-b57b-45a0-a6ae-89d7e2e703ce" />
<img width="1220" height="574" alt="Screenshot 2026-10-05 093721" src="https://github.com/user-attachments/assets/b9ea1336-7435-4e45-8fd3-60226b0e49a8" />

---

## Live Sales Management

The application supports recording sales directly through the Streamlit interface.

When a sale is recorded:

```text
Sale Created
     ↓
Validate Product
     ↓
Validate Quantity
     ↓
Check Available Stock
     ↓
Insert Sale
     ↓
Reduce Inventory
```

The inventory is automatically updated after a successful sale.

### Business Rules

The system prevents:

* Invalid products
* Duplicate sale IDs
* Zero or negative quantities
* Sales exceeding available stock

---

## Inventory Alerts

The system automatically identifies products that require attention.

### Stock Status

```text
Current Stock > Reorder Level × 1.5
        ↓
       OK
```

```text
Current Stock ≤ Reorder Level × 1.5
        ↓
  REORDER SOON
```

```text
Current Stock ≤ Reorder Level
        ↓
   LOW STOCK
```

Products with low stock and longer lead times can additionally be classified as:

```text
URGENT REORDER
```

This helps store owners prioritize inventory replenishment.

> **Inventory Alert Screenshot**

<img width="1271" height="625" alt="Screenshot 2026-10-05 093730" src="https://github.com/user-attachments/assets/79a8995f-6067-43ee-b85a-33b052be27c2" />

---

# 🔮 Demand Shock Simulator

The Demand Shock Simulator allows users to test how increased demand could affect current inventory.

Users can simulate demand increases such as:

```text
0%
20%
50%
100%
```

The system calculates:

```text
Projected Demand
        ↓
Projected Stock
        ↓
Units Short
        ↓
Risk Classification
```

### Risk Categories

| Risk             | Meaning                                   |
| ---------------- | ----------------------------------------- |
| 🟢 SAFE          | Inventory can handle the projected demand |
| 🔴 LOW STOCK     | Projected stock reaches the reorder level |
| 🚨 STOCKOUT RISK | Projected demand exceeds available stock  |

This feature provides a simple **what-if analysis** for inventory planning.

> **Demand Simulator Screenshot**

<img width="1487" height="831" alt="Screenshot 2026-10-05 093802" src="https://github.com/user-attachments/assets/232c1040-3f68-4e1c-83d9-680e4bd76546" />

---

# Testing

The project was tested using both predefined datasets and randomly generated datasets.

The test dataset generator can create:

* 30 products
* 30 inventory records
* 200 sales records

This allows the pipeline to be tested with larger and more realistic datasets.

### Validation Testing

Tested scenarios include:

* Duplicate IDs
* Missing values
* Invalid prices
* Negative quantities
* Invalid product references
* Invalid inventory values
* Referential integrity violations

### Live Sales Testing

Tested scenarios include:

* Valid sales
* Duplicate Sale IDs
* Invalid Product IDs
* Zero quantity
* Negative quantity
* Sales exceeding available stock
* Automatic inventory reduction

### Demand Simulator Testing

Tested with multiple demand increases to verify that:

* Projected demand changes correctly
* Projected stock changes correctly
* Units short are calculated correctly
* Risk status changes correctly
* Charts update dynamically

---

# Tech Stack

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| Python     | Data processing and application logic |
| Pandas     | Data cleaning and transformation      |
| PostgreSQL | Relational database                   |
| SQL        | Data analysis and business queries    |
| Streamlit  | Interactive dashboard and application |
| psycopg2   | PostgreSQL connection                 |
| Git        | Version control                       |
| GitHub     | Source code and project hosting       |

---

# Project Structure

```text
smart-inventory/
│
├── app/
│   ├── dashboard.py
│   └── pages/
│       ├── sales.py
│       └── demand_simulator.py
│
├── data/
│   ├── raw/
│   │   ├── Sample good/
│   │   └── Sample bad/
│   │
│   ├── processed/
│   └── test/
│
├── docs/
│   ├── database-design.md
│   └── v2-database-tables.png
│
├── src/
│   ├── ingestion/
│   │   └── load_data.py
│   │
│   ├── validation/
│   │   ├── products_validation.py
│   │   ├── sales_validation.py
│   │   ├── inventory_validation.py
│   │   └── referential_integrity.py
│   │
│   ├── transformation/
│   │   ├── clean_columns.py
│   │   ├── clean_data.py
│   │   └── transform_data.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── insert_data.py
│   │
│   └── analytics/
│       └── inventory_analysis.sql
│
├── tests/
│   ├── test_pipeline.py
│   └── generate_test_data.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/vikash122005/smart-inventory-management.git
cd smart-inventory-management
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure PostgreSQL

Create a PostgreSQL database:

```text
smart_inventory
```

Create the required tables using the SQL schema provided in the project documentation.

> **Important:** Database credentials should be stored using environment variables and should never be committed to GitHub.

## 5. Run the Streamlit application

```bash
streamlit run app/dashboard.py
```

The application will open in your browser.

---

# Sample Dataset

The project includes:

### Good Dataset

Clean data that should successfully pass the validation and transformation pipeline.

### Bad Dataset

Intentionally corrupted data containing issues such as:

* Duplicate records
* Missing values
* Invalid prices
* Invalid references
* Invalid quantities

These datasets are used to demonstrate the validation layer.

---

# Generate Test Data

The project also includes a test-data generator.

Run:

```bash
python tests/generate_test_data.py
```

It generates randomized datasets containing:

```text
30 Products
30 Inventory Records
200 Sales Records
```

The generated data can be used to test the ingestion, validation, transformation, database, dashboard, and demand simulation layers.

---

# Data Integrity

The PostgreSQL database uses constraints and relationships to protect data quality.

Examples include:

* Primary keys
* Foreign keys
* Unique identifiers
* NOT NULL constraints
* CHECK constraints
* Referential integrity

This ensures that invalid data cannot easily enter the database even if application-level validation is bypassed.

---

# Project Screenshots

## Dashboard

<img width="1912" height="793" alt="Screenshot 2026-10-05 093647" src="https://github.com/user-attachments/assets/e539de4c-0766-48b3-a812-fa8715acad87" />
<img width="1217" height="519" alt="Screenshot 2026-10-05 093658" src="https://github.com/user-attachments/assets/f637dc58-8ab4-4388-bfac-1fddc904c569" />
<img width="1221" height="549" alt="Screenshot 2026-10-05 093712" src="https://github.com/user-attachments/assets/8a099fde-b57b-45a0-a6ae-89d7e2e703ce" />
<img width="1220" height="574" alt="Screenshot 2026-10-05 093721" src="https://github.com/user-attachments/assets/b9ea1336-7435-4e45-8fd3-60226b0e49a8" />

## Inventory Alerts

<img width="1271" height="625" alt="Screenshot 2026-10-05 093730" src="https://github.com/user-attachments/assets/7cbad279-faed-44a9-9e4d-ce43563a76a6" />


## Sales Management

<img width="990" height="662" alt="Screenshot 2026-10-05 093906" src="https://github.com/user-attachments/assets/3a0d5d6e-aa55-4297-8c1e-d10609f4f8e5" />
<img width="982" height="697" alt="Screenshot 2026-10-05 093913" src="https://github.com/user-attachments/assets/0ca29e1a-e2ff-4d41-88ad-c7a8a095e30f" />



## Demand Shock Simulator

<img width="1487" height="831" alt="Screenshot 2026-10-05 093802" src="https://github.com/user-attachments/assets/247a452b-d7d2-4004-abf4-a7f671f09524" />
<img width="1058" height="622" alt="Screenshot 2026-10-05 093817" src="https://github.com/user-attachments/assets/b709465e-3369-44e9-bb2a-14f7bdf070dc" />



## Database Design

<img width="1498" height="938" alt="v2-database-tables" src="https://github.com/user-attachments/assets/994a5f4f-bf72-4aaf-8a24-38292e29bbd1" />



# 🎯 Project Objectives

The main objectives of this project are to demonstrate practical experience with:

* Data ingestion
* Data validation
* Data cleaning
* ETL pipelines
* Relational database design
* SQL analytics
* Python data processing
* Business logic implementation
* Data visualization
* Interactive dashboards
* Inventory management
* Testing
* Git/GitHub workflow

---

# Future Improvements

Potential future improvements include:

* Cloud database deployment
* User authentication
* Automated scheduled data ingestion
* REST API integration
* Advanced demand forecasting
* Machine-learning-based inventory forecasting
* Automated supplier/reorder recommendations
* Email or notification-based alerts
* Docker containerization
* Cloud deployment
* Multi-store inventory management

---

# Key Learning Outcomes

This project provided practical experience in building an end-to-end data application rather than working with isolated scripts.

The complete workflow covers:

```text
Raw Data
   ↓
Ingestion
   ↓
Validation
   ↓
Cleaning
   ↓
Transformation
   ↓
PostgreSQL
   ↓
SQL Analytics
   ↓
Streamlit
   ↓
Business Decisions
```

The project demonstrates how raw business data can be transformed into actionable inventory insights through a complete data engineering workflow.

---

# Author

**Vikash A**

Data Engineering | Python | SQL | PostgreSQL | Pandas

GitHub:
https://github.com/vikash122005

---

## If you found this project useful

Feel free to explore the repository, provide feedback, or suggest improvements.
