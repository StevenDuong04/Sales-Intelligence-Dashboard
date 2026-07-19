# File: kpis_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains KPI calculation functions.

import pandas as pd
import numpy as np


def calculate_total_revenue(df):
    if "revenue" not in df.columns:
        raise ValueError("Column 'revenue' is missing from the Dataframe.")
    total_revenue = df["revenue"].sum()
    return total_revenue


def calculate_total_orders(df):
    if "transaction_id" not in df.columns:
        raise ValueError("Column 'transaction_id' is missing from the Dataframe.")
    total_orders = df["transaction_id"].count()
    return total_orders


def calculate_average_order_value(df):
    total_revenue = df["revenue"].sum()
    total_orders = df["transaction_id"].count()
    if total_orders == 0:
        return 0
    avg_order = total_revenue / total_orders
    return avg_order


def calculate_customer_count(df):
    if "customer_id" not in df.columns:
        raise ValueError("Column 'customer_id' is missing from the Dataframe.")
    total_customers = df["customer_id"].nunique()
    return total_customers
