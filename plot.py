import plotly.express as px


def plot_summary_scatter(
    df, selected_column_x, selected_column_y, selected_column_color
):
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


def plot_corr_heatmap(corr_df):
    fig = px.imshow(
        corr_df,
        labels=dict(x="X", y="Y", color="Correlation"),
        x=corr_df.columns,
        y=corr_df.columns,
        zmin=-1,
        zmax=1,
        color_continuous_scale="RdBu",
        text_auto=False,
        aspect="auto",
    )
    fig.update_xaxes(side="top")
    return fig
