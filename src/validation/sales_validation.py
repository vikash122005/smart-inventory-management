import pandas as pd

def validate_sales(incoming_data):
    invalid_rows = set()
    invalid_rows.update(incoming_data[incoming_data["sale_id"].duplicated()].index)
    invalid_rows.update(incoming_data[incoming_data["sale_id"].isnull()].index)
    invalid_rows.update(incoming_data[incoming_data["product_id"].isnull()].index)
    invalid_rows.update(incoming_data[pd.to_datetime(incoming_data["sale_date"], errors="coerce").isnull()].index)
    invalid_rows.update(incoming_data[(incoming_data["quantity_sold"] <= 0) | (incoming_data["quantity_sold"].isnull())].index)
    return invalid_rows