import streamlit as st
import pandas as pd
import sys
import os
import math

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src")
    )
)

from database.connection import get_connection


st.title("Demand Shock Simulator")

st.write(
    "Simulate how increased demand could affect current inventory."
)


def run_query(query):

    connection = get_connection()

    dataframe = pd.read_sql(
        query,
        connection
    )

    connection.close()

    return dataframe


demand_shock = st.slider(
    "Demand Increase (%)",
    min_value=0,
    max_value=100,
    value=20,
    step=10
)


query = """
SELECT
    p.product_id,
    p.product_name,
    p.product_category,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days,
    COALESCE(SUM(s.quantity_sold), 0) AS historical_demand
FROM products p
JOIN inventory i
    ON p.product_id = i.product_id
LEFT JOIN sales s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.product_category,
    i.current_stock,
    p.reorder_level,
    p.lead_time_days
ORDER BY historical_demand DESC;
"""


data = run_query(query)


demand_multiplier = 1 + (demand_shock / 100)


data["projected_demand"] = (
    data["historical_demand"] * demand_multiplier
)


data["projected_demand"] = data[
    "projected_demand"
].apply(math.ceil)


data["projected_stock"] = (
    data["current_stock"] -
    data["projected_demand"]
)


data["units_short"] = (
    data["projected_demand"] -
    data["current_stock"]
).clip(lower=0)


def classify_risk(row):

    if row["projected_stock"] < 0:
        return "STOCKOUT RISK"

    elif row["projected_stock"] <= row["reorder_level"]:
        return "LOW STOCK"

    else:
        return "SAFE"


data["risk_status"] = data.apply(
    classify_risk,
    axis=1
)


stockout_count = (
    data["risk_status"] == "STOCKOUT RISK"
).sum()


low_stock_count = (
    data["risk_status"] == "LOW STOCK"
).sum()


safe_count = (
    data["risk_status"] == "SAFE"
).sum()


col1, col2, col3 = st.columns(3)


col1.metric(
    "Stockout Risk",
    stockout_count
)


col2.metric(
    "Low Stock",
    low_stock_count
)


col3.metric(
    "Safe Products",
    safe_count
)


if stockout_count > 0:

    st.error(
        f"{stockout_count} product(s) may run out of stock "
        f"under a {demand_shock}% demand increase."
    )

elif low_stock_count > 0:

    st.warning(
        f"{low_stock_count} product(s) may reach low-stock "
        f"levels under a {demand_shock}% demand increase."
    )

else:

    st.success(
        "Current inventory can handle the simulated demand increase."
    )


def format_risk(status):

    if status == "STOCKOUT RISK":
        return "🚨 STOCKOUT RISK"

    elif status == "LOW STOCK":
        return "🔴 LOW STOCK"

    return "🟢 SAFE"


data["risk_status"] = data[
    "risk_status"
].apply(format_risk)


st.subheader("Simulation Results")


st.dataframe(
    data[
        [
            "product_id",
            "product_name",
            "current_stock",
            "historical_demand",
            "projected_demand",
            "projected_stock",
            "units_short",
            "risk_status"
        ]
    ],
    use_container_width=True
)

st.subheader("Projected Stock")

chart_data = data[
    ["product_name", "projected_stock"]
].set_index("product_name")

st.bar_chart(chart_data)