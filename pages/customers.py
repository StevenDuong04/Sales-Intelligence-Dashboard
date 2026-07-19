# File: customers.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains the layout for the customer page.

import streamlit as st
import pandas as pd

import analytics.kpis_analytics as kpis
import analytics.trends_analytics as trends
import analytics.products_analytics as products
import analytics.customers_analytics as customers

import visualization.charts as charts

st.header("Customer Analysis", text_alignment="left")

if (
    "dataset" not in st.session_state or st.session_state["dataset"] is None
):  # Make sure to check if dataset is None as well
    st.warning("Please upload a dataset first in Overview")

else:
    df = st.session_state["dataset"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Total Customers", value=f"{kpis.calculate_customer_count(df):,}"
        )
    with col2:
        st.metric(
            label="Average Spending",
            value=f"${kpis.calculate_average_order_value(df):,.2f}",
        )
    with col3:
        st.metric(
            label="Repeat Rate", value=f"{customers.customer_repeat_rate(df):,.2f}%"
        )

    st.subheader("Top Customers")
    top_customers = customers.top_customers_by_revenue(df, 10)
    st.table(top_customers)

    st.subheader("Customer Distribution")
    distribution_tabs = st.tabs(["Purchase Frequency", "Revenue Contribution"])

    with distribution_tabs[0]:
        purchase_frequency = customers.top_customer_purchase_frequency(df)
        st.plotly_chart(
            charts.create_bar_chart(
                data=purchase_frequency,
                x="customer_id",
                y="purchase_count",
                title="Customer Purchase Frequency",
            )
        )

    with distribution_tabs[1]:
        revenue_contribution = customers.top_customers_by_revenue(df, top_n=20)
        st.plotly_chart(
            charts.create_bar_chart(
                data=revenue_contribution,
                x="Customer ID",
                y="Total Revenue",
                title="Top Customers by Revenue",
            )
        )

    st.subheader("Most Recent Orders")
    most_recent_orders = customers.customer_most_recent_orders(df, top_n=10)
    st.table(most_recent_orders, hide_index=True)
