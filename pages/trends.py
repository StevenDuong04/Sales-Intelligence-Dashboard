# File: trends.py
# Author: Steven Duong
# Date: 2026-08-07
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
        ["Revenue", "Product Sales", "Category Sales"],
    )

    forecast_period = st.sidebar.selectbox(
        "Forecast Period", ["3 Months", "6 Months", "12 Months"]
    )

    forecast_months = {
        "3 Months": 3,
        "6 Months": 6,
        "12 Months": 12,
    }[forecast_period]

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

    try:
        historical_revenue, forecast = trends.forecast_rev(
            filtered_df,
            forecast_months,
        )

        forecast_fig = charts.create_forecast_chart(
            historical_revenue,
            forecast,
            title="Historical vs Forecasted Revenue",
        )

        st.plotly_chart(
            forecast_fig,
            use_container_width=True,
        )

    except ValueError as e:
        st.warning(str(e))

    # ==========================
    # Trend Patterns
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Revenue Seasonality")

        years = filtered_df["order_date"].dt.year.nunique()

        if years >= 2:

            seasonality = trends.revenue_seasonality(filtered_df)

            if not seasonality.empty:

                best_month = seasonality.loc[
                    seasonality["average_revenue"].idxmax(),
                    "month"
                ]

                best_value = seasonality["average_revenue"].max()

                st.metric(
                    "Strongest Seasonal Month",
                    best_month,
                    f"${best_value:,.0f} avg. revenue",
                )
            else:
                st.info("Not enough data to identify seasonality.")

        else:
            st.info("At least 2 years of data are recommended for seasonality analysis.")

    with col2:

        st.subheader("Growth Analysis")

        growth = trends.revenue_growth_analysis(filtered_df)

        if len(growth) >= 2:

            first_revenue = growth["total_revenue"].iloc[0]
            latest_revenue = growth["total_revenue"].iloc[-1]

            overall_growth = (latest_revenue - first_revenue) / first_revenue * 100

            latest_growth = growth["growth_rate"].iloc[-1]

            st.metric(
                "Overall Revenue Growth",
                f"{overall_growth:+.1f}%",
                f"{latest_growth:+.1f}% vs previous month",
            )

        else:
            st.info("Not enough data to calculate growth.")
    # ==========================
    # Forecast Summary
    # ==========================

    st.subheader("Forecast Summary")

    next_forecast = forecast["forecast"].iloc[0]

    last_actual = historical_revenue.iloc[-1]

    expected_growth = (next_forecast - last_actual) / last_actual * 100

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Expected Growth",
            f"{expected_growth:+.1f}%",
        )

    with col2:

        st.metric(
            "Next Period Forecast",
            f"${next_forecast:,.0f}",
        )

    with col3:

        st.metric(
            "Forecast Period",
            f"{forecast_months} months",
        )
