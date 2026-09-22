import pandas as pd

def validate_products(incoming_data):
    if incoming_data["product_id"].duplicated().any():
        return False
    if incoming_data["product_id"].isnull().any():
        return False
    if incoming_data["product_name"].isnull().any():
        return False
    if incoming_data["product_category"].isnull().any():
            return False
    if (incoming_data["unit_price"] < 0).any() or incoming_data["unit_price"].isnull().any():
         return False
    if (incoming_data["reorder_level"] < 0).any() or incoming_data["reorder_level"].isnull().any():
         return False
    if (incoming_data["lead_time_days"] < 0).any() or incoming_data["lead_time_days"].isnull().any():
         return False
    return True
