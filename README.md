# Smart Inventory Management System

A data-driven inventory management system designed for small retail businesses to replace manual Excel-based inventory tracking with a structured database, automated data processing, analytics, and a web-based dashboard.

## Project Overview

Small retail businesses often manage products, sales, and inventory using spreadsheets. This can lead to duplicate records, inconsistent data, incorrect stock levels, and difficulty in analyzing business performance.

The Smart Inventory Management System addresses these problems by providing a centralized workflow for data ingestion, validation, cleaning, database storage, analytics, and inventory management.

The project is being developed incrementally as a Version 1 system, with future versions planned for more advanced analytics and deployment capabilities.

## Objectives

* Replace manual spreadsheet-based inventory management.
* Validate incoming product, sales, and inventory data.
* Clean and transform inconsistent datasets.
* Store structured data in PostgreSQL.
* Build SQL-based business analytics.
* Provide an interactive Streamlit dashboard.
* Automatically update inventory when a sale is recorded.
* Identify products that require restocking.
* Simulate demand shocks to analyze inventory behavior.
* Containerize and deploy the complete application.

## Technology Stack

| Technology       | Purpose                                |
| ---------------- | -------------------------------------- |
| Python           | Data processing, ETL, backend logic    |
| Pandas           | Data cleaning and transformation       |
| PostgreSQL       | Relational database                    |
| SQL              | Data analysis and business queries     |
| Streamlit        | Interactive dashboard                  |
| Git & GitHub     | Version control and project management |
| Docker           | Application containerization           |
| Jupyter Notebook | Data exploration and development       |

## System Architecture

```text
Historical Excel / CSV Data
          |
          v
     Data Ingestion
          |
          v
      Validation
          |
          v
 Cleaning & Transformation
          |
          v
       PostgreSQL
          |
          +--------------------+
          |                    |
          v                    v
    SQL Analytics       Streamlit Dashboard
                               |
                               v
                         Live Sales Entry
                               |
                               v
                     Automatic Stock Update
                               |
                               v
                        Low Stock Detection
```

## Version 1 Scope

The first version focuses on establishing a reliable end-to-end data pipeline and inventory management workflow.

### Completed

* Project structure and environment setup
* Database schema design
* Sample good and bad datasets
* Pandas data exploration
* Data validation
* Data cleaning and transformation
* PostgreSQL database setup
* Database connection from Python
* Product data insertion into PostgreSQL
* SQL analytics
* Initial Streamlit dashboard development

### In Progress

* Live sales entry
* Automatic inventory stock updates
* Low-stock alert functionality

### Planned

* Demand Shock Simulator
* Comprehensive testing and error handling
* Docker containerization
* GitHub repository cleanup
* Application deployment
* Complete project documentation

## Database Design

The V1 database consists of three primary tables:

### Products

Stores product information and inventory-related configuration.

* `product_id`
* `product_name`
* `product_category`
* `unit_price`
* `reorder_level`
* `lead_time_days`

### Sales

Stores individual sales transactions.

* `sale_id`
* `product_id`
* `sale_date`
* `quantity_sold`

### Inventory

Stores the current stock level for each product.

* `product_id`
* `current_stock`

The tables are connected using primary and foreign key relationships to maintain referential integrity.

## Data Pipeline

The project follows a structured ETL workflow:

```text
Raw Data
   |
   v
Data Ingestion
   |
   v
Validation
   |
   v
Cleaning
   |
   v
Transformation
   |
   v
PostgreSQL
   |
   v
Analytics / Dashboard
```

The validation layer checks for issues such as:

* Missing values
* Duplicate records
* Invalid identifiers
* Incorrect data types
* Invalid numerical values
* Referential integrity problems
* Inconsistent column names
* Invalid business rules

The cleaning and transformation stage prepares validated data for reliable database insertion and downstream analysis.

## Analytics

The SQL analytics component is designed to provide useful business information such as:

* Total sales
* Sales by product
* Sales by category
* Product performance
* Current inventory levels
* Products approaching their reorder level
* Other inventory-related business metrics

## Dashboard

The Streamlit dashboard provides a user-friendly interface for viewing inventory and sales information.

Planned dashboard capabilities include:

* Inventory overview
* Sales overview
* Product-level analysis
* Category-level analysis
* Low-stock products
* Sales transaction entry
* Inventory status

## Live Inventory Workflow

The live sales functionality will allow a user to record a sale through the application.

The intended workflow is:

```text
User Records Sale
       |
       v
Validate Transaction
       |
       v
Insert Sale Record
       |
       v
Reduce Current Stock
       |
       v
Check Reorder Level
       |
       v
Display Updated Inventory Status
```

This will connect the sales transaction system directly with the inventory table.

## Project Structure

```text
smart-inventory-management/
│
├── data/
│   └── raw/
│       ├── Sample good/
│       └── Sample bad/
│
├── notebooks/
│
├── src/
│   ├── validation/
│   ├── transformation/
│   ├── database/
│   └── analytics/
│
├── tests/
│
├── dashboard/
│
├── requirements.txt
├── .gitignore
└── README.md
```

The structure may evolve as additional V1 functionality is implemented.

## Development Progress

| Day    | Component                         | Status    |
| ------ | --------------------------------- | --------- |
| Day 1  | Project setup and database design | Completed |
| Day 2  | Sample datasets                   | Completed |
| Day 3  | Pandas and data inspection        | Completed |
| Day 4  | Data validation                   | Completed |
| Day 5  | Data cleaning and transformation  | Completed |
| Day 6  | PostgreSQL setup and tables       | Completed |
| Day 7  | Python to PostgreSQL ETL          | Completed |
| Day 8  | SQL analytics                     | Completed |
| Day 9  | Streamlit dashboard               | Completed |
| Day 10 | Live sales and stock update       | Planned   |
| Day 11 | Low-stock alerts                  | Planned   |
| Day 12 | Demand Shock Simulator            | Planned   |
| Day 13 | Testing and error handling        | Planned   |
| Day 14 | Docker and GitHub cleanup         | Planned   |
| Day 15 | Deployment and documentation      | Planned   |

## Future Improvements

Future versions may include:

* Automated data ingestion from external sources
* Advanced demand forecasting
* Machine learning-based inventory predictions
* Supplier management
* Purchase order management
* User authentication and role-based access
* Cloud database integration
* Automated notifications
* Advanced business intelligence dashboards

## Project Goal

The primary goal of this project is to demonstrate an end-to-end data engineering workflow, from raw business data to a functional database-backed application.

It combines data validation, ETL, SQL, database management, analytics, application development, testing, containerization, and deployment into a single practical business project.

## Author

Vikash A

Data Engineering / Cloud & Infrastructure Enthusiast

GitHub: `vikash122005`
