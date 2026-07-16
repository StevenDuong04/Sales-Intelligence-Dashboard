# File: overview.py
# Author: Steven Duong
# Date: 2026-07-15
# Description: This file contains the layout for the overview page.

import streamlit as st
import pandas as pd
import preprocessing.loader as loader
import preprocessing.cleaning as cleaning
import preprocessing.validation as validation
import analytics.kpis_analytics as kpis

st.set_page_config(page_title="Sales Intelligence Dashboard", page_icon=":bar_chart:", layout="wide")

st.header("Quick Business Summary", text_alignment="left")

st.sidebar.title("Sales Intelligence Dashboard")
with st.sidebar:
    uploaded_file =st.file_uploader("Upload your sales data", type=["csv", "xlsx", "xls"], key="file_uploader")
    if uploaded_file is not None:
        try:
            df = loader.load_data(uploaded_file)
            df = cleaning.clean_data(df)
            validation.full_validation(df)
            st.success("Data loaded and validated successfully!")
        except Exception as e:
            st.exception(e)


# KPI Calculations
if uploaded_file is not None:
    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    st.subheader("Key Performance Indicators (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Transactions", value=f"{kpis.calculate_total_orders():,}")
    with col2:
        st.metric(label="Total Customers", value=f"{kpis.calculate_customer_count():,}")
    with col3:
        st.metric(label="Total Revenue", value=f"${kpis.calculate_total_revenue():,.2f}")
    with col4:
        st.metric(label="Average Order Value", value=f"${kpis.calculate_average_order_value():,.2f}")

# TODO: Add Revenue Trend Chart
# TODO: Top products by revenue card
# TODO: Customer Summary