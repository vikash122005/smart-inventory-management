import pandas as pd

def validate_sales(incoming_data):
    if incoming_data["sale_id"].duplicated().any():
        return False
    if incoming_data["sale_id"].isnull().any():
        return False
    if incoming_data["product_id"].isnull().any():
        return False
    if pd.to_datetime(incoming_data["sale_date"], errors="coerce").isnull().any():
        return False
    if (incoming_data["quantity_sold"] <= 0).any() or incoming_data["quantity_sold"].isnull().any():
        return False
    return True