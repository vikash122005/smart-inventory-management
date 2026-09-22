import pandas as pd

def clean_column_names(incoming_data):
    incoming_data.columns = incoming_data.columns.str.strip()
    return incoming_data