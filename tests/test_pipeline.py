import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ingestion.load_data import load_csv
from validation.products_validation import validate_products
from validation.sales_validation import validate_sales
from validation.inventory_validation import validate_inventory
from transformation.clean_columns import clean_column_names
from validation.referential_integrity import validate_reference

products_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Products.csv")
sales_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Sales.csv")
inventory_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample bad/Inventory.csv")
products_data = clean_column_names(products_data)
sales_data = clean_column_names(sales_data)
inventory_data = clean_column_names(inventory_data)
product_result  = validate_products(products_data)
sales_result = validate_sales(sales_data)
inventory_result = validate_inventory(inventory_data)
sales_reference_result = validate_reference(products_data, sales_data)

print("Products: ", product_result)
print("Sales: ", sales_result)
print("Inventory: ",inventory_result)
print("Sales Reference: ", sales_reference_result)