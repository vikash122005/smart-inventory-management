import pandas as pd

def load_csv(file_path):
    table = pd.read_csv(file_path)
    return table

