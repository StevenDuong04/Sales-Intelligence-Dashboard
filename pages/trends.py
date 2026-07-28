# File: trends.py
# Author: Steven Duong
# Date: 2026-07-27
# Description: This file contains the layout for the trends page.

import streamlit as st
import pandas as pd

import analytics.trends_analytics as trends
import visualization.charts as charts
import utils.helpers as helps

helps.init_page("Sales Intelligence Dashboard")

st.header("Trend Analysis", text_alignment="left")


if "dataset" not in st.session_state or st.session_state["dataset"] is None:
    st.warning("Please upload a dataset first in Overview")

else:

    df = st.session_state["dataset"].copy()

    df["order_date"] = pd.to_datetime(df["order_date"])

    # ==========================
    # Sidebar
    # ==========================

    st.sidebar.header("Trend Filters")

    min_date = df["order_date"].min().date()
    max_date = df["order_date"].max().date()

    date_range = st.sidebar.date_input("Date Range", value=(min_date, max_date))

    metric = st.sidebar.selectbox(
        "Metric",
        ["Revenue", "Orders", "Average Order Value", "Product Sales", "Category Sales"],
    )

    forecast_period = st.sidebar.selectbox(
        "Forecast Period", ["3 Months", "6 Months", "12 Months"]
    )

    # ==========================
    # Filtering
    # ==========================

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_df = df[(df["order_date"] >= start_date) & (df["order_date"] <= end_date)]

    if metric == "Product Sales":

        product = st.sidebar.selectbox(
            "Product", sorted(filtered_df["product_name"].unique())
        )

    elif metric == "Category Sales":

        category = st.sidebar.selectbox(
            "Category", sorted(filtered_df["category"].unique())
        )

    # ==========================
    # Historical Trend
    # ==========================

    st.subheader("Historical Trend Analysis")

    if metric == "Revenue":

        trend = trends.monthly_revenue_trend(filtered_df)

        fig = charts.create_line_chart(
            trend, x="month", y="total_revenue", title="Monthly Revenue Trend"
        )

    elif metric == "Orders":

        trend = trends.monthly_order_trend(filtered_df)

        fig = charts.create_line_chart(
            trend, x="month", y="total_orders", title="Monthly Order Trend"
        )

    elif metric == "Average Order Value":

        trend = trends.monthly_aov_trend(filtered_df)

        fig = charts.create_line_chart(
            trend, x="month", y="average_order_value", title="Average Order Value Trend"
        )

    elif metric == "Product Sales":

        trend = trends.product_sales_trend(filtered_df, product)

        fig = charts.create_line_chart(
            trend, x="order_date", y="quantity", title=f"{product} Sales Trend"
        )

    elif metric == "Category Sales":

        trend = trends.product_category_sales_trend(filtered_df, category)

        fig = charts.create_line_chart(
            trend, x="order_date", y="quantity", title=f"{category} Sales Trend"
        )

    st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Forecasting Section
    # ==========================

    st.subheader("Revenue Forecast")

    st.info("Forecasting model will predict future sales based on historical trends.")

    forecast_placeholder = pd.DataFrame({"Date": [], "Prediction": []})

    st.plotly_chart(
        charts.create_line_chart(
            forecast_placeholder,
            x="Date",
            y="Prediction",
            title="Actual vs Predicted Revenue",
        ),
        use_container_width=True,
    )

    # ==========================
    # Trend Patterns
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Seasonality")

        if metric == "Revenue":

            best_month = trend.loc[trend["total_revenue"].idxmax(), "month"]

            best_value = trend["total_revenue"].max()

            st.metric("Highest Revenue Month", best_month, f"${best_value:,.0f}")

    with col2:

        st.subheader("Growth Analysis")

        st.info("Growth rate analysis will identify increases or declines over time.")

    # ==========================
    # Forecast Summary
    # ==========================

    st.subheader("Forecast Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Expected Growth", "Coming Soon")

    with col2:
        st.metric("Next Period Forecast", "Coming Soon")

    with col3:
        st.metric("Confidence", "Coming Soon")
