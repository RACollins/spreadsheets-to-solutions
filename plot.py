import plotly.express as px


def plot_summary_histogram(df, selected_column, split_column):
    fig = px.histogram(
        df,
        x=selected_column,
        color=split_column,
        color_discrete_sequence=px.colors.qualitative.Vivid,
        marginal="box",
    )
    return fig


def plot_summary_scatter(df, selected_column_x, selected_column_y, selected_column_color):
    fig = px.scatter(
        df,
        x=selected_column_x,
        y=selected_column_y,
        color=selected_column_color,
        color_discrete_sequence=px.colors.qualitative.Vivid,
        marginal_x="box",
        marginal_y="box",
    )
    return fig
