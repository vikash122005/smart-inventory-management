import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path


# --------------------------------------------------
# SETTINGS
# --------------------------------------------------

random.seed(42)

PRODUCT_COUNT = 30
SALES_COUNT = 200


# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "data" / "test"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# PRODUCT DATA
# --------------------------------------------------

product_names = [
    "Notebook",
    "Pen",
    "Pencil",
    "Eraser",
    "School Bag",
    "Water Bottle",
    "Mouse",
    "Keyboard",
    "USB Cable",
    "Headphones",
    "Charger",
    "Power Bank",
    "Extension Box",
    "LED Bulb",
    "Torch",
    "Calculator",
    "Stapler",
    "Scissors",
    "Glue",
    "Tape",
    "T-Shirt",
    "Jeans",
    "Socks",
    "Cap",
    "Slippers",
    "Broom",
    "Mop",
    "Detergent",
    "Soap",
    "Shampoo"
]

categories = [
    "Stationery",
    "Electronics",
    "Household",
    "Clothing",
    "Personal Care"
]


# --------------------------------------------------
# GENERATE PRODUCTS
# --------------------------------------------------

products = []

for i in range(1, PRODUCT_COUNT + 1):

    products.append({
        "product_id": f"P{i:03d}",
        "product_name": product_names[i - 1],
        "product_category": random.choice(categories),
        "unit_price": round(random.uniform(20, 2000), 2),
        "reorder_level": random.randint(5, 30),
        "lead_time_days": random.randint(1, 10)
    })


products_df = pd.DataFrame(products)


# --------------------------------------------------
# GENERATE INVENTORY
# --------------------------------------------------

inventory = []

for product_id in products_df["product_id"]:

    inventory.append({
        "product_id": product_id,
        "current_stock": random.randint(5, 100)
    })


inventory_df = pd.DataFrame(inventory)


# --------------------------------------------------
# GENERATE SALES
# --------------------------------------------------

sales = []

start_date = datetime(2026, 1, 1)

for i in range(1, SALES_COUNT + 1):

    product_id = random.choice(
        products_df["product_id"].tolist()
    )

    sale_date = start_date + timedelta(
        days=random.randint(0, 270)
    )

    quantity_sold = random.randint(1, 10)

    sales.append({
        "sale_id": f"S{i:04d}",
        "product_id": product_id,
        "sale_date": sale_date,
        "quantity_sold": quantity_sold
    })


sales_df = pd.DataFrame(sales)


# --------------------------------------------------
# SAVE DATA
# --------------------------------------------------

products_path = OUTPUT_DIR / "Products_test.csv"
inventory_path = OUTPUT_DIR / "Inventory_test.csv"
sales_path = OUTPUT_DIR / "Sales_test.csv"


products_df.to_csv(products_path, index=False)
inventory_df.to_csv(inventory_path, index=False)
sales_df.to_csv(sales_path, index=False)


print("Test datasets generated successfully!")

print(f"Products:  {len(products_df)} rows")
print(f"Inventory: {len(inventory_df)} rows")
print(f"Sales:     {len(sales_df)} rows")

print()
print("Files created:")

print(products_path)
print(inventory_path)
print(sales_path)