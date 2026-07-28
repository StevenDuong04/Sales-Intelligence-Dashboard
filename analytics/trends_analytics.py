# File: trends_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains trend analysis functions for products and customers.

import pandas as pd
import numpy as np


# Product Trends
def product_sales_trend(df, product_name):
    """
    Calculates the sales trend for a specific product over time.

    Filters transactions for the selected product and aggregates
    quantity sold by order date to show changes in product sales.
    """

    if (
        "product_name" not in df.columns
        or "order_date" not in df.columns
        or "quantity" not in df.columns
    ):
        raise ValueError(
            "DataFrame must contain 'product_name', 'order_date', and 'quantity' columns."
        )

    product_df = df[df["product_name"] == product_name]
    sales_trend = product_df.groupby("order_date")["quantity"].sum().reset_index()
    return sales_trend


def product_category_sales_trend(df, category):
    """
    Calculates the sales trend for a specific product category over time.

    Filters transactions by category and aggregates quantity sold
    by order date to analyze category performance trends.
    """

    if (
        "category" not in df.columns
        or "order_date" not in df.columns
        or "quantity" not in df.columns
    ):
        raise ValueError(
            "DataFrame must contain 'category', 'order_date', and 'quantity' columns."
        )

    category_df = df[df["category"] == category]
    sales_trend = category_df.groupby("order_date")["quantity"].sum().reset_index()
    return sales_trend


# Revenue Trends
def monthly_revenue_trend(df):
    """
    Calculates monthly revenue trends.

    Groups transaction revenue by month to show how revenue
    changes over time.
    """

    df["order_date"] = pd.to_datetime(df["order_date"])
    monthly_revenue = (
        df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum().reset_index()
    )
    monthly_revenue.columns = ["month", "total_revenue"]
    monthly_revenue["month"] = monthly_revenue["month"].astype(str)
    return monthly_revenue


def yearly_revenue_trend(df):
    """
    Calculates yearly revenue trends.

    Groups transaction revenue by year to analyze long-term
    revenue growth and performance.
    """

    df["order_date"] = pd.to_datetime(df["order_date"])
    yearly_revenue = (
        df.groupby(df["order_date"].dt.to_period("Y"))["revenue"].sum().reset_index()
    )
    yearly_revenue.columns = ["year", "total_revenue"]
    yearly_revenue["year"] = yearly_revenue["year"].astype(str)
    return yearly_revenue

# TODO: