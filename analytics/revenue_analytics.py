# File: revenue_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains revenue calculation functions.

import pandas as pd
import numpy as np
from analytics.kpis_analytics import calculate_total_revenue, calculate_total_orders


def revenue_growth_rate(df, date_column="order_date"):
    # Get first and latest year
    first_year = df[date_column].dt.year.min()
    latest_year = df[date_column].dt.year.max()

    # Revenue for each year
    beginning_revenue = df[df[date_column].dt.year == first_year]["revenue"].sum()
    latest_revenue = df[df[date_column].dt.year == latest_year]["revenue"].sum()

    if beginning_revenue == 0:
        raise ValueError(
            "Beginning year revenue is zero, cannot calculate growth rate."
        )

    growth_rate = (latest_revenue - beginning_revenue) / beginning_revenue

    return growth_rate * 100


# def net_profit_margin(df): Need to have a column for expenses in order to calculate net profit margin. This function is not implemented yet.


def average_revenue_per_customer(df):
    total_revenue = calculate_total_revenue(df)
    unique_users = df["customer_id"].nunique()

    if unique_users == 0:
        raise ValueError(
            "No unique users found, cannot calculate average revenue per user."
        )

    average_revenue = total_revenue / unique_users
    return average_revenue


def revenue_per_product(df):
    revenue_by_product = df.groupby("product_name")["revenue"].sum().reset_index()
    revenue_by_product.columns = ["product_name", "total_revenue"]
    return revenue_by_product


def revenue_per_category(df):
    revenue_by_category = df.groupby("category")["revenue"].sum().reset_index()
    revenue_by_category.columns = ["category", "total_revenue"]
    return revenue_by_category
