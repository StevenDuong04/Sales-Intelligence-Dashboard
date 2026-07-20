# File: revenue.py
# Author: Steven Duong
# Date: 2026-07-20
# Description: This file contains the layout for the revenue page.

import streamlit as st

import analytics.kpis_analytics as kpis
import analytics.trends_analytics as trends
import analytics.revenue_analytics as revenues

import visualization.charts as charts

import utils.helpers as helps

helps.init_page("Sales Intelligence Dashboard")

st.header("Revenue Analysis", text_alignment="left")

if (
    "dataset" not in st.session_state or st.session_state["dataset"] is None
):  # Make sure to check if dataset is None as well
    st.warning("Please upload a dataset first in Overview")

else:
    df = st.session_state["dataset"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Revenue", value=f"{kpis.calculate_total_revenue(df):,.2f}")
    with col2:
        st.metric(
            label="Average Spendings",
            value=f"${kpis.calculate_average_order_value(df):,.2f}",
        )
    with col3:
        st.metric(
            label="Revenue Growth Rate",
            value=f"{revenues.revenue_growth_rate(df):,.2f}%",
        )
    # TODO: After integrating multiple file uploads with business spendings
    # with col4:
    #     st.metric(
    #         label="Profit", value="
    #     )

    st.subheader("Revenue Trend")
    growth_trend = st.tabs(["Monthly", "Yearly"])
    with growth_trend[0]:
        revenue_growth_trend = trends.monthly_revenue_trend(df)
        st.plotly_chart(
            charts.create_line_chart(
                data=revenue_growth_trend,
                x="month",
                y="total_revenue",
                title="Monthly Revenue Trend",
            )
        )

    with growth_trend[1]:
        revenue_growth_trend_year = trends.yearly_revenue_trend(df)
        st.plotly_chart(
            charts.create_line_chart(
                data=revenue_growth_trend_year,
                x="year",
                y="total_revenue",
                title="Yearly Revenue Trend",
            )
        )

    product_revenue, category_revenue = st.columns(2)
    with product_revenue:
        st.subheader("Product Revenue")
        revenue_by_product = revenues.revenue_per_product(df).sort_values(
        by="total_revenue", ascending=False
        )
        st.table(revenue_by_product, hide_index=True)

    with category_revenue:
        st.subheader("Category Revenue")
        revenue_by_category = revenues.revenue_per_category(df).sort_values(
        by="total_revenue", ascending=False
        )
        st.table(revenue_by_category, hide_index=True)