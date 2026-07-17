# File: customers.py
# Author: Steven Duong
# Date: 2026-07-17
# Description: This file contains the layout for the customer page.

import streamlit as st
import pandas as pd

import analytics.kpis_analytics as kpis
import analytics.trends_analytics as trends
import analytics.products_analytics as products
import analytics.customers_analytics as customers

import visualization.charts as charts

st.header("Customer Analysis", text_alignment="left")

if "dataset" not in st.session_state or st.session_state["dataset"] is None: # Make sure to check if dataset is None as well
    st.warning("Please upload a dataset first in Overview")

else:
    df = st.session_state["dataset"]

    st.subheader("Quick Customer Insight")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Customers", value=f"{kpis.calculate_customer_count(df):,}")
    with col2:
        st.metric(label="Average Spending", value=f"${kpis.calculate_average_order_value(df):,.2f}")
    with col3:
        st.metric(label="Repeat Rate", value=f"{customers.customer_repeat_rate(df):,.2f}%")
    
    # TODO: Customer Distribution (With Bar chart)
    # Customer distribution by purhcase frequency, revenue contribution, number of orders with tab to switch between each metric
    st.subheader("Customer Distribution")
    distribution_tabs = st.tabs(["Purchase Frequency", "Revenue Contribution", "Number of Orders"])
    
    
    # TODO: Customer Segmentation (With Pie/Bar chart)
    # TODO: Customer Lifetime Value (With Line chart)
    # TODO: Customer Order Table at bottom with recent orders

    