# File: charts.py
# Author: Steven Duong
# Date: 2026-08-07
# Description: This file contains visualization functions to create different kinds of charts and plots.

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def create_line_chart(data, x, y, title):
    fig = px.line(data_frame=data, x=x, y=y, title=title, markers=True)

    fig.update_layout(template="plotly_white", hovermode="x unified")

    return fig


def create_bar_chart(data, x, y, title):
    fig = px.bar(
        data_frame=data,
        x=x,
        y=y,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


def create_histogram(data, column, bins, title):
    fig = px.histogram(
        data_frame=data,
        x=column,
        nbins=bins,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


def create_scatter_plot(data, x, y, title):
    fig = px.scatter(
        data_frame=data,
        x=x,
        y=y,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


def create_count_pie_chart(data, column, title):
    counts = data[column].value_counts().reset_index()
    counts.columns = [column, "Count"]

    fig = px.pie(
        data_frame=data,
        names=column,
        values="Count",
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


def create_pie_chart(data, column, values, title):
    fig = px.pie(
        data_frame=data,
        names=column,
        values=values,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


# Forecasting plot
def create_forecast_chart(historical, forecast, title):
    """
    Creates a line chart showing historical revenue and forecasted revenue.
    """

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=historical.index,
            y=historical.values,
            mode="lines",
            name="Historical Revenue",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast["date"],
            y=forecast["forecast"],
            mode="lines",
            name="Forecast",
            line=dict(dash="dash"),
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Revenue",
        hovermode="x unified",
    )

    return fig