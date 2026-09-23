import pandas as pd

def validate_reference(reference_data, incoming_data):

    invalid_rows = set()
    invalid_rows.update(incoming_data[~incoming_data["product_id"].isin(reference_data["product_id"])].index)
    return invalid_rows