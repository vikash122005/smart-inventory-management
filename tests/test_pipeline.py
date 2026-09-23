import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ingestion.load_data import load_csv
from validation.products_validation import validate_products
from validation.sales_validation import validate_sales
from validation.inventory_validation import validate_inventory
from transformation.clean_columns import clean_column_names
from validation.referential_integrity import validate_reference
from transformation.clean_data import clean_data_rows
from transformation.transform_data import transform_products_data
from transformation.transform_data import transform_sales_data
from transformation.transform_data import transform_inventory_data

# 1. Load raw data
products = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Products.csv")
sales = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Sales.csv")
inventory = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Inventory.csv")


# 2. Standardize column names
products = clean_column_names(products)
sales = clean_column_names(sales)
inventory = clean_column_names(inventory)


# 3. Validate data
invalid_product_rows = validate_products(products)
invalid_sales_rows = validate_sales(sales)
invalid_inventory_rows = validate_inventory(inventory)


# 4. Validate references
invalid_sales_rows = invalid_sales_rows.union(
    validate_reference(products, sales)
)

invalid_inventory_rows = invalid_inventory_rows.union(
    validate_reference(products, inventory)
)


# 5. Remove invalid rows
clean_products = clean_data_rows(invalid_product_rows, products)
clean_sales = clean_data_rows(invalid_sales_rows, sales)
clean_inventory = clean_data_rows(invalid_inventory_rows, inventory)


# 6. Transform data types
transformed_products = transform_products_data(clean_products)
transformed_sales = transform_sales_data(clean_sales)
transformed_inventory = transform_inventory_data(clean_inventory)


# 7. Final output
print("Final Products Data:")
print(transformed_products)

print("\nFinal Sales Data:")
print(transformed_sales)

print("\nFinal Inventory Data:")
print(transformed_inventory)