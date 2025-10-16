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

    # Set up columns
    left_column, left_arrow, middle_column, right_arrow, right_column = st.columns(
        [10, 1, 10, 1, 10]
    )

    # Choose inner, middle, and outer variables
    all_vars = ["Product_Category", "Marital_Status", "Education"]
    with left_column:
        inner_var = st.selectbox("Inner Variable", all_vars)
        all_vars.remove(inner_var)

    with left_arrow:
        st.write("→")

    with middle_column:
        middle_var = st.selectbox("Middle Variable", all_vars)
        all_vars.remove(middle_var)

    with right_arrow:
        st.write("→")

    with right_column:
        outer_var = st.selectbox("Outer Variable", all_vars)

    # Plot total amount spent on products by marital status
    fig = px.sunburst(
        df,
        path=[inner_var, middle_var, outer_var],
        values="MntTotal",
        color="Product_Category",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )
    st.plotly_chart(fig, width="stretch")


if __name__ == "__main__":
    main()
