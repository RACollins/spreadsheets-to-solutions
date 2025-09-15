
def clean_data(df):
    df.columns = df.columns.str.strip()
    df["Income"] = df["Income"].fillna(df["Income"].median())
    return df
