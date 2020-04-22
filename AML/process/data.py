import pandas as pd

def get_cols(path):
    df = pd.read_csv(path)
    cols = list(df.columns.values)
    print(cols)
    return cols
