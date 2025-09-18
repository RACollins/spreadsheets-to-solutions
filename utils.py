import pandas as pd


def clean_data(df):
    # Remove leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Fill missing values with median
    df["Income"] = df["Income"].fillna(df["Income"].median())

    # Remove outliers
    df = df[df["Income"] < df["Income"].quantile(0.95)]

    # Convert to datetime
    df["Year_Birth"] = pd.to_datetime(df["Year_Birth"].astype("string"))
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"].astype("string"))

    # Convert columns to categorical columns (avoiding ID which has too many unique values)
    # Only convert columns with reasonable number of categories for better PyArrow compatibility
    categorical_columns = [
        "Education",
        "Marital_Status",
        "Kidhome",
        "Teenhome",
        "AcceptedCmp1",
        "AcceptedCmp2",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "Response",
        "Complain",
        "Country",
    ]

    for col in categorical_columns:
        if col in df.columns:
            df[col] = df[col].astype("category")

    # Add total amount spent on all purchases
    MntCols = [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds",
    ]
    df["MntTotal"] = df[MntCols].sum(axis=1)

    # Add total number of purchases
    NumCols = [
        "NumWebVisitsMonth",
        "NumCatalogPurchases",
        "NumStorePurchases",
    ]
    df["NumTotal"] = df[NumCols].sum(axis=1)

    # Add total campaign responses
    CmpCols = [
        "AcceptedCmp1",
        "AcceptedCmp2",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "Response",
    ]
    # Convert boolean to integer
    df["AcceptedCmpTotal"] = df[CmpCols].astype(int).sum(axis=1)

    # Reorder columns
    df = df[
        [
            "ID",
            "Year_Birth",
            "Dt_Customer",
            "Education",
            "Marital_Status",
            "Kidhome",
            "Teenhome",
            "Recency",
            "Income",
        ]
        + MntCols
        + ["MntTotal"]
        + NumCols
        + ["NumTotal", "NumWebPurchases", "NumDealsPurchases"]
        + CmpCols
        + ["AcceptedCmpTotal"]
        + ["Complain", "Country"]
    ]

    return df
