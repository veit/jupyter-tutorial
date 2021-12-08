import pandas as pd


def load_data(filename):
    """Documentation"""
    df = pd.read_csv(filename)
    return df
