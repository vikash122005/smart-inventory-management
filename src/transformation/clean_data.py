import pandas as pd

def clean_data_rows(invalid_rows,incoming_data):
    cleaned_data = incoming_data.drop(index = invalid_rows)
    return cleaned_data