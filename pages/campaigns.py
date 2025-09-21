import streamlit as st
import pandas as pd
import plotly.express as px
from utils import clean_data


def color_cell(v, vmin=0.0, vmax=1.0):
    cmap = px.colors.sequential.Pinkyl
    n_colors = len(cmap)
    # Handle both scalar values and pandas Series
    if hasattr(v, "iloc"):
        v = v.iloc[0]
    idx = int((v - vmin) / (vmax - vmin) * (n_colors - 1))
    return f"background-color: {cmap[idx]}"


def main():
    st.title("Campaigns")

    # Plot convevrtion rate by campaign per country
    df = clean_data(pd.read_csv("data/marketing_data.csv"))

    # Convert campaign columns to int
    CmpCols = [
        "AcceptedCmp1",
        "AcceptedCmp2",
        "AcceptedCmp3",
        "AcceptedCmp4",
        "AcceptedCmp5",
        "Response",
        "AcceptedCmpTotal",
    ]
    df[CmpCols] = df[CmpCols].astype(int)

    # Which country performed the best over all campaigns?
    summary_df = (
        df.groupby("Country", observed=False)
        .agg({"ID": "count", "AcceptedCmpTotal": "sum"})
        .reset_index()
    )
    summary_df = summary_df.rename(
        columns={
            "ID": "Total Customers",
            "AcceptedCmpTotal": "Total Campaign Responses",
        }
    )
    summary_df["Conversion Rate"] = (
        summary_df["Total Campaign Responses"] / summary_df["Total Customers"]
    )

    # Format background color of conversion rate column
    summary_df_styled = summary_df.style.map(color_cell, subset=["Conversion Rate"])
    st.dataframe(summary_df_styled, width="stretch")

    # What was the average conversion rate per campaign per country?
    average_df = (
        df[CmpCols + ["Country"]]
        .groupby("Country", observed=False)
        .mean()
        .reset_index()
    )

    # Remove Mexico since there are so few customers
    average_df = average_df[average_df["Country"] != "Mexico"]

    # Format background color of average conversion rate column
    # Conditional formatting per column, not whole dataframe
    # Keep the original DataFrame and build styling separately
    average_df_styled = average_df.style
    for col in CmpCols:
        col_vmin = float(average_df[col].min())  # Ensure scalar value
        col_vmax = float(average_df[col].max())  # Ensure scalar value
        average_df_styled = average_df_styled.map(
            color_cell, vmin=col_vmin, vmax=col_vmax, subset=[col]
        )
    st.dataframe(average_df_styled, width="stretch")


if __name__ == "__main__":
    main()
