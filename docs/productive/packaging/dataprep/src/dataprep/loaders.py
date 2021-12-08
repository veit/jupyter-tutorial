import pandas as pd


def load_csv(filename):
    """Documentation"""
    df = pd.read_csv(filename)
    return df
