def clean_data(df):
    # Remove leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Fill missing values with median
    df["Income"] = df["Income"].fillna(df["Income"].median())

    # Remove outliers
    df = df[df["Income"] < df["Income"].quantile(0.95)]

    # Convert integer columns to categorical columns
    df["Kidhome"] = df["Kidhome"].astype("category")
    df["Teenhome"] = df["Teenhome"].astype("category")
    df["AcceptedCmp1"] = df["AcceptedCmp1"].astype("category")
    df["AcceptedCmp2"] = df["AcceptedCmp2"].astype("category")
    df["AcceptedCmp3"] = df["AcceptedCmp3"].astype("category")
    df["AcceptedCmp4"] = df["AcceptedCmp4"].astype("category")
    df["AcceptedCmp5"] = df["AcceptedCmp5"].astype("category")
    df["Complain"] = df["Complain"].astype("category")
    return df
