import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from ingestion.load_data import load_csv
from validation.products_validation import validate_products
from transformation.clean_columns import cleaning_columns

products_data = load_csv("C:/Users/admin/OneDrive/Desktop/smart-inventory/data/raw/Sample good/Products.csv")
products_data = cleaning_columns(products_data)
result  = validate_products(products_data)

print(result)