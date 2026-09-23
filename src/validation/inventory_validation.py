import pandas as pd

def validate_inventory(incoming_data):
    invalid_rows = set()

    invalid_rows.update(incoming_data[incoming_data["product_id"].duplicated()].index)
    invalid_rows.update(incoming_data[incoming_data["product_id"].isnull()].index)
    invalid_rows.update(incoming_data[incoming_data["current_stock"].isnull()].index)
    invalid_rows.update(incoming_data[(incoming_data["current_stock"]< 0)].index)
    return invalid_rows