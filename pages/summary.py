import streamlit as st
import pandas as pd
import plotly.express as px
from utils import clean_data


def summary():
    st.title("Summary")

    df = clean_data(pd.read_csv("data/marketing_data.csv"))
    df_info = pd.read_csv("data/marketing_data_dictionary.csv")

    with st.expander("Marketing Data Dictionary"):
        st.dataframe(df_info)

    # Plot histogram of selected column
    selected_column = st.selectbox("Select a column to plot", df.columns)
    fig = px.histogram(df, x=selected_column)
    st.plotly_chart(fig)


def main():
    summary()


if __name__ == "__main__":
    main()
