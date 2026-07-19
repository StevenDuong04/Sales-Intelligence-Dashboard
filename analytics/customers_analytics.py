# File: customers_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains customer analytics functions.

import pandas as pd
import numpy as np


def top_customers_by_revenue(df, top_n):
    if "customer_id" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' and 'revenue' columns.")

    top_customers = (
        df.groupby("customer_id")["revenue"].sum().nlargest(top_n).reset_index()
    )
    top_customers.columns = ["Customer ID", "Total Revenue"]
    return top_customers


def customer_average_order_value(df):
    if "customer_id" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' and 'revenue' columns.")

    average_order_value = df.groupby("customer_id")["revenue"].mean().reset_index()
    average_order_value.rename(columns={"revenue": "average_order_value"}, inplace=True)
    return average_order_value


def customer_repeat_rate(df):
    if "customer_id" not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' column.")

    total_customers = df["customer_id"].nunique()
    repeat_customers = df[df.duplicated("customer_id", keep=False)][
        "customer_id"
    ].nunique()
    repeat_rate = (repeat_customers / total_customers) * 100
    return repeat_rate


def top_customer_purchase_frequency(df):
    if "customer_id" not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' column.")

    purchase_frequency = (
        df.groupby("customer_id").size().nlargest(20).reset_index(name="purchase_count")
    )
    return purchase_frequency


def customer_most_recent_orders(df, top_n):
    if (
        "customer_id" not in df.columns
        or "transaction_id" not in df.columns
        or "order_date" not in df.columns
    ):
        raise ValueError(
            "DataFrame must contain 'customer_id', 'transaction_id', and 'order_date' columns."
        )

    customer_orders = (
        df[df["customer_id"].notnull()]
        .sort_values(by="order_date", ascending=False)
        .head(top_n)
    )
    return customer_orders[
        [
            "customer_id",
            "transaction_id",
            "order_date",
            "product_name",
            "quantity",
            "revenue",
        ]
    ]
