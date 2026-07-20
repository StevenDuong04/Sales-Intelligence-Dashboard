# File: products.py
# Author: Steven Duong
# Date: 2026-07-20
# Description: This file contains the layout for the products page.

import streamlit as st

import analytics.products_analytics as products

import visualization.charts as charts

import utils.helpers as helps

helps.init_page("Sales Intelligence Dashboard")

st.header("Product Analysis", text_alignment="left")

if (
    "dataset" not in st.session_state or st.session_state["dataset"] is None
):  # Make sure to check if dataset is None as well
    st.warning("Please upload a dataset first in Overview")

else:
    df = st.session_state["dataset"]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Total Products Sold")
        st.metric(
            label="Total Products Sold", value=f"{products.total_products_sold(df):,}"
        )
    with col2:
        st.subheader("Best Sellers by Quantity Sold")
        top_products = products.top_performing_product(df, 3)
        st.table(top_products)
    with col3:
        st.subheader("Best Sellers by Revenue")
        top_revenue_products = (
            products.product_revenue_contribution(df)
            .sort_values(by="contribution_percentage", ascending=False)
            .head(3)
        )
        st.table(top_revenue_products, hide_index=True)

    # Product Revenue Contribution Chart
    st.subheader("Product Revenue Contribution")
    contribution = products.product_revenue_contribution(df)
    st.plotly_chart(
        charts.create_pie_chart(
            data=contribution,
            column="product_name",
            values="contribution_percentage",
            title="Revenue Contribution by Product",
        )
    )

    # Product Performance Summary
    st.subheader("Product Performance")
    product_summary = products.product_performance_summary(df).sort_values(
        by="total_quantity_sold", ascending=False
    )
    st.table(product_summary, hide_index=True)

    category_column, low_column = st.columns(2)
    with category_column:
        # Product Category Summary
        st.subheader("Category Performance")
        category_summary = products.product_category_performance(df)
        st.table(category_summary)
    with low_column:
        # Low Performers by Revenue
        st.subheader("Low Performers")
        low_performers = (
            products.product_revenue_contribution(df)
            .sort_values(by="contribution_percentage", ascending=True)
            .head(6)
        )
        st.table(low_performers, hide_index=True)
