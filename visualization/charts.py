# File: charts.py
# Author: Steven Duong
# Date: 2026-07-15
# Description: This file contains visualization functions to create different kinds of charts and plots.

import pandas as pd
import numpy as np
import plotly.express as px

def create_line_chart(data, x, y, title):
    fig = px.line(
        data_frame=data,
        x=x,
        y=y,
        title=title,
        markers=True
    )

    fig.update_layout(
        template="plotly_white",
        hovermode="x unified"
    )

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

def create_pie_chart(data, column, title):
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