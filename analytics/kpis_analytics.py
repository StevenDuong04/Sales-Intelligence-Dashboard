# File: kpis_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains KPI calculation functions.

import pandas as pd
import numpy as np


def calculate_total_revenue(df):
    """
    Calculates the total revenue generated from all transactions.

    Sums the revenue column to determine the overall sales revenue.
    """

    if "revenue" not in df.columns:
        raise ValueError("Column 'revenue' is missing from the Dataframe.")
    total_revenue = df["revenue"].sum()
    return total_revenue


def calculate_total_orders(df):
    """
    Calculates the total number of orders made.

    Counts the number of transaction IDs to determine the total orders.
    """

    if "transaction_id" not in df.columns:
        raise ValueError("Column 'transaction_id' is missing from the Dataframe.")
    total_orders = df["transaction_id"].count()
    return total_orders


def calculate_average_order_value(df):
    """
    Calculates the average order value across all transactions.

    Divides total revenue by the total number of orders to determine
    the average amount spent per order.
    """

    total_revenue = df["revenue"].sum()
    total_orders = df["transaction_id"].count()
    if total_orders == 0:
        return 0
    avg_order = total_revenue / total_orders
    return avg_order


def calculate_customer_count(df):
    """
    Calculates the total number of unique customers.

    Counts distinct customer IDs to determine the number of customers.
    """

    if "customer_id" not in df.columns:
        raise ValueError("Column 'customer_id' is missing from the Dataframe.")
    total_customers = df["customer_id"].nunique()
    return total_customers
