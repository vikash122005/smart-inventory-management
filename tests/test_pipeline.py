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

products_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Products.csv")
sales_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Sales.csv")
inventory_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Inventory.csv")
products_data = clean_column_names(products_data)
sales_data = clean_column_names(sales_data)
inventory_data = clean_column_names(inventory_data)


product_result  = validate_products(products_data)
sales_result = validate_sales(sales_data)
inventory_result = validate_inventory(inventory_data)
sales_result = sales_result = sales_result.union(validate_reference(products_data, sales_data))
inventory_result = inventory_result = inventory_result.union(validate_reference(products_data, inventory_data))
cleaned_products_data = clean_data_rows(product_result, products_data)
cleaned_sales_data = clean_data_rows(sales_result, sales_data)
cleaned_inventory_data = clean_data_rows(inventory_result, inventory_data)

print("Products: ", product_result)
print("Sales: ", sales_result)
print("Inventory: ", inventory_result)
print("Cleaned Products Data: ", cleaned_products_data)
print("Cleaned Sales Data: ", cleaned_sales_data)
print("Cleaned Inventory Data: ", cleaned_inventory_data)
