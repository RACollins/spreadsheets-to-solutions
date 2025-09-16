import streamlit as st
import pandas as pd
from utils import clean_data
from plot import plot_summary_histogram, plot_summary_scatter


def summary():
    st.title("Summary")

    df = clean_data(pd.read_csv("data/marketing_data.csv"))
    df_info = pd.read_csv("data/marketing_data_dictionary.csv")

    with st.expander("Marketing Data Dictionary"):
        st.dataframe(df_info)

    st.write(df.dtypes)

    # Plot scatter plot of two selected columns
    selected_column_x = st.selectbox(
        "Select a column to plot on the x-axis", df.columns, key="scatter_x"
    )
    selected_column_y = st.selectbox(
        "Select a column to plot on the y-axis", df.columns, key="scatter_y"
    )
    selected_column_color = st.selectbox(
        "Select a column to plot on the color", df.columns, key="scatter_color"
    )
    fig = plot_summary_scatter(df, selected_column_x, selected_column_y, selected_column_color)
    st.plotly_chart(fig)

    # Plot histogram of selected column
    selected_column = st.selectbox(
        "Select a column to plot", df.columns, key="histogram"
    )
    split_column = st.selectbox(
        "Select a column to split by", df.columns, key="histogram_split"
    )
    fig = plot_summary_histogram(df, selected_column, split_column)
    st.plotly_chart(fig)


def main():
    summary()


if __name__ == "__main__":
    main()
