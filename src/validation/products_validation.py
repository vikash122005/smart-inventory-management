import pandas as pd

def validate_products(incoming_data):
    if incoming_data["product_id"].isnull().any():
        return False
    return True
