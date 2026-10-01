import streamlit as st
import pandas as pd

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from database.connection import get_connection
connection = get_connection()

def run_query(query):
    connection = get_connection()
    dataframe = pd.read_sql(query, connection)
    connection.close()
    return dataframe

st.title("Smart Inventory Management Dashboard")
st.write("Inventory and sales overview")

###KPI Metrics

total_products = run_query("""
    SELECT COUNT(*) AS total_products
    FROM products;
""")

total_sales = run_query("""
    SELECT COUNT(*) AS total_sales
    FROM sales;
""")

total_quantity = run_query("""
    SELECT SUM(quantity_sold) AS total_quantity
    FROM sales;
""")

inventory_value = run_query("""
    SELECT SUM(i.current_stock * p.unit_price) AS inventory_value
    FROM products p
    JOIN inventory i
        ON p.product_id = i.product_id;
""")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Products",
    total_products.iloc[0]["total_products"]
)

col2.metric(
    "Total Sales",
    total_sales.iloc[0]["total_sales"]
)

col3.metric(
    "Quantity Sold",
    total_quantity.iloc[0]["total_quantity"]
)

col4.metric(
    "Inventory Value",
    f"₹{inventory_value.iloc[0]['inventory_value']:,.2f}"
)

###Low-stock products

low_stock = run_query("""
    SELECT
        p.product_id,
        p.product_name,
        i.current_stock,
        p.reorder_level
    FROM products p
    JOIN inventory i
        ON p.product_id = i.product_id
    WHERE i.current_stock <= p.reorder_level
    ORDER BY i.current_stock ASC;
""")

st.subheader("Low Stock Products")

st.dataframe(
    low_stock,
    use_container_width=True
)

###Best-selling products

best_selling = run_query("""
    SELECT
        p.product_name,
        SUM(s.quantity_sold) AS total_quantity_sold
    FROM products p
    JOIN sales s
        ON p.product_id = s.product_id
    GROUP BY
        p.product_id,
        p.product_name
    ORDER BY total_quantity_sold DESC
    LIMIT 5;
""")

st.subheader("Top 5 Best-Selling Products")

st.bar_chart(
    best_selling.set_index("product_name")
)

###Current inventory

inventory = run_query("""
    SELECT
        p.product_name,
        i.current_stock
    FROM products p
    JOIN inventory i
        ON p.product_id = i.product_id
    ORDER BY i.current_stock DESC;
""")

st.subheader("Current Inventory")

st.bar_chart(
    inventory.set_index("product_name")
)

###category sales section

category_sales = run_query("""
    SELECT
        p.product_category,
        SUM(s.quantity_sold) AS total_quantity_sold
    FROM products p
    JOIN sales s
        ON p.product_id = s.product_id
    GROUP BY p.product_category
    ORDER BY total_quantity_sold DESC;
""")

st.subheader("Sales by Category")

st.bar_chart(
    category_sales.set_index("product_category")
)

###Stock alert section

alert_query = """
SELECT
    p.product_id,
    p.product_name,
    p.product_category,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days,
    CASE
        WHEN i.current_stock <= p.reorder_level
         AND p.lead_time_days >= 5
            THEN 'URGENT REORDER'
        WHEN i.current_stock <= p.reorder_level
            THEN 'LOW STOCK'
        ELSE 'REORDER SOON'
    END AS stock_status
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
WHERE i.current_stock <= p.reorder_level * 1.5
ORDER BY i.current_stock ASC;
"""

alert_data = run_query(alert_query)

def format_status(status):
    if status == "URGENT REORDER":
        return "🚨 URGENT REORDER"
    elif status == "LOW STOCK":
        return "🔴 LOW STOCK"
    elif status == "REORDER SOON":
        return "🟡 REORDER SOON"
    return "🟢 OK"

alert_data["stock_status"] = alert_data["stock_status"].apply(
    format_status
)

st.subheader("Inventory Alerts")

if alert_data.empty:
    st.success("All products have sufficient stock.")
else:
    st.warning(
        f"{len(alert_data)} product(s) require inventory attention."
    )

st.dataframe(
    alert_data,
    use_container_width=True
)

urgent_count = sum(
    alert_data["stock_status"] == "🚨 URGENT REORDER"
)

low_count = sum(
    alert_data["stock_status"] == "🔴 LOW STOCK"
)

soon_count = sum(
    alert_data["stock_status"] == "🟡 REORDER SOON"
)

col1, col2, col3 = st.columns(3)

col1.metric("Urgent Reorders", urgent_count)
col2.metric("Low Stock", low_count)
col3.metric("Reorder Soon", soon_count)
