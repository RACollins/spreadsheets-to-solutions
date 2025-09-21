import streamlit as st
import pandas as pd
from utils import clean_data
import plotly.express as px


def main():
    st.title("Products")

    df = clean_data(pd.read_csv("data/marketing_data.csv"))

    # Drop MntTotal column
    df = df.drop(columns=["MntTotal"])

    # Convert to long format
    df = df.melt(
        id_vars=["Marital_Status", "Education"],
        value_vars=[
            "MntWines",
            "MntFruits",
            "MntMeatProducts",
            "MntFishProducts",
            "MntSweetProducts",
            "MntGoldProds",
        ],
        var_name="Product_Category",
        value_name="MntTotal",
    )

    # Plot total amount spent on products by marital status
    fig = px.sunburst(
        df,
        path=["Product_Category", "Marital_Status", "Education"],
        values="MntTotal",
        color="Product_Category",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )
    st.plotly_chart(fig, width="stretch")


if __name__ == "__main__":
    main()
