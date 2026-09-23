import pandas as pd

def validate_products(incoming_data):
    invalid_rows = set()

    invalid_rows.update(incoming_data[incoming_data["product_id"].duplicated()].index)
    invalid_rows.update(incoming_data[incoming_data["product_id"].isnull()].index)
    invalid_rows.update(incoming_data[incoming_data["product_name"].isnull()].index)
    invalid_rows.update(incoming_data[incoming_data["product_category"].isnull()].index)
    invalid_rows.update(incoming_data[(incoming_data["unit_price"] < 0) | (incoming_data["unit_price"].isnull())].index)
    invalid_rows.update(incoming_data[(incoming_data["reorder_level"] < 0) | (incoming_data["reorder_level"].isnull())].index)
    invalid_rows.update(incoming_data[(incoming_data["lead_time_days"] < 0) | (incoming_data["lead_time_days"].isnull())].index)

    return invalid_rows
