import pandas as pd

def transform_products_data(incoming_data):

    incoming_data["reorder_level"] = incoming_data["reorder_level"].astype(int)
    incoming_data["lead_time_days"] = incoming_data["lead_time_days"].astype(int)
    incoming_data["unit_price"] = incoming_data["unit_price"].astype(float)

    return incoming_data

def transform_sales_data(incoming_data):

    incoming_data["quantity_sold"] = incoming_data["quantity_sold"].astype(int)

    return incoming_data

def transform_inventory_data(incoming_data):

    incoming_data["current_stock"] = incoming_data["current_stock"].astype(int)

    return incoming_data

