import streamlit as st
import pandas as pd
from utils import clean_data
from plot import summary_scatter, corr_heatmap


def main():
    st.title("Summary")

    df = clean_data(pd.read_csv("data/marketing_data.csv"))
    df_info = pd.read_csv("data/marketing_data_dictionary.csv")

    with st.expander("Marketing Data Dictionary"):
        st.dataframe(df_info)

    # Display DataFrame info safely without PyArrow serialization issues
    dtypes_df = pd.DataFrame(
        {
            "Column": df.columns,
            "Data Type": [str(dtype) for dtype in df.dtypes],
            "Non-Null Count": [df[col].notna().sum() for col in df.columns],
        }
    )
    with st.expander("Data Types"):
        st.dataframe(dtypes_df)

    # Plot scatter plot of two selected columns
    # get only category columns
    cat_cols = [col for col in df.columns if df[col].dtype == "category"]
    non_cat_cols = [col for col in df.columns if df[col].dtype != "category"]

    left_column, middle_column, right_column = st.columns([1, 1, 1])
    with left_column:
        selected_column_x = st.selectbox("X", non_cat_cols, key="scatter_x")
    with middle_column:
        selected_column_y = st.selectbox("Y", non_cat_cols, key="scatter_y")
    with right_column:
        selected_column_color = st.selectbox("Colour", cat_cols, key="scatter_color")
    fig = summary_scatter(
        df, selected_column_x, selected_column_y, selected_column_color
    )
    st.plotly_chart(fig)

    # Plot correlations between all columns
    corr_df = df[non_cat_cols].corr()
    fig = corr_heatmap(corr_df)
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
