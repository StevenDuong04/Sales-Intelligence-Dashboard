# File: overview.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains the layout for the overview page.

import streamlit as st
import pandas as pd

import preprocessing.loader as loader
import preprocessing.cleaning as cleaning
import preprocessing.validation as validation

import analytics.kpis_analytics as kpis
import analytics.trends_analytics as trends
import analytics.products_analytics as products
import analytics.customers_analytics as customers

import visualization.charts as charts

st.set_page_config(
    page_title="Sales Intelligence Dashboard", page_icon=":bar_chart:", layout="wide"
)

st.header("Quick Business Summary", text_alignment="left")

st.sidebar.title("Sales Intelligence Dashboard")
with st.sidebar:
    uploaded_file = st.file_uploader(
        "Upload your sales data", type=["csv", "xlsx", "xls"], key="file_uploader"
    )
    if uploaded_file is not None:
        try:
            df = loader.load_data(uploaded_file)
            st.session_state["raw_df"] = df
            df = cleaning.clean_data(df)
            validation.full_validation(df)
            st.success("Data loaded and validated successfully!")
            st.session_state["dataset"] = df
        except Exception as e:
            st.exception(e)


# KPI Calculations
if "dataset" in st.session_state and st.session_state["dataset"] is not None:
    df = st.session_state["dataset"]

    st.subheader("Dataset Overview")
    st.dataframe(df.head())

    st.subheader("Key Performance Indicators (KPIs)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            label="Total Transactions", value=f"{kpis.calculate_total_orders(df):,}"
        )
    with col2:
        st.metric(
            label="Total Customers", value=f"{kpis.calculate_customer_count(df):,}"
        )
    with col3:
        st.metric(
            label="Total Revenue", value=f"${kpis.calculate_total_revenue(df):,.2f}"
        )
    with col4:
        st.metric(
            label="Average Order Value",
            value=f"${kpis.calculate_average_order_value(df):,.2f}",
        )

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

    product_col, customer_col = st.columns(2)
    with product_col:
        st.subheader("Top Products")
        top_products = products.top_performing_product(df, 5)
        st.table(top_products)
    with customer_col:
        st.subheader("Top Customers")
        top_customers = customers.top_customers_by_revenue(df, 5)
        st.table(top_customers)
