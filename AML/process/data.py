import pandas as pd

df = pd.DataFrame()

def get_cols(path):
    df = pd.read_csv(path)
    cols = list(df.columns.values)
    print(cols)
    return cols

