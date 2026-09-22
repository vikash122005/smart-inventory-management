import pandas as pd

def validate_inventory(incoming_data):
    if incoming_data["product_id"].duplicated().any():
        return False
    if incoming_data["product_id"].isnull().any():
        return False
    if incoming_data["current_stock"].isnull().any():
        return False
    if (incoming_data["current_stock"]< 0).any():
        return False
    return True