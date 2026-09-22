import pandas as pd

def validate_reference(reference_data, incoming_data):

    if (~incoming_data["product_id"].isin(reference_data["product_id"])).any():
        return False
    return True