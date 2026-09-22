import pandas as pd

def cleaning_columns(incoming_data):
    incoming_data.columns = incoming_data.columns.str.strip()
    return incoming_data