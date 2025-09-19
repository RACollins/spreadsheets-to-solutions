import pandas as pd
from sklearn.impute import KNNImputer


def clean_data(df):
    # Remove leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Fill missing values with KNN algorithm
    imputer = KNNImputer(n_neighbors=5)
    df[["Income"]] = imputer.fit_transform(df[["Income"]])

    # Convert to datetime
    df["Year_Birth"] = pd.to_datetime(df["Year_Birth"].astype("string"))
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"].astype("string"))

    # Clean up marital status categories BEFORE converting to categorical
    # Merge "YOLO", "Alone", and "Absurd" into "Single"
    replacement_dict = {"YOLO": "Single", "Alone": "Single", "Absurd": "Single"}
    df["Marital_Status"] = df["Marital_Status"].replace(replacement_dict)

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
    # Convert boolean to integer and back again
    df["AcceptedCmpTotal"] = df[CmpCols].astype(int).sum(axis=1).astype("category")

    # Calculate age
    df["Age"] = (df["Dt_Customer"] - df["Year_Birth"]).dt.days // 365

    # Remove outliers for income, amount columns, number columns, and age
    df = df.loc[df["Income"] < df["Income"].quantile(0.95), :]
    df = df.loc[df["Age"] < 100, :]
    df = df.loc[df["MntTotal"] < df["MntTotal"].quantile(0.95), :]
    df = df.loc[df["NumTotal"] < df["NumTotal"].quantile(0.95), :]
    df = df.loc[df["NumWebPurchases"] < df["NumWebPurchases"].quantile(0.95), :]
    df = df.loc[df["NumDealsPurchases"] < df["NumDealsPurchases"].quantile(0.95), :]

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
            "Age",
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
