# File: products_analytics.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains product-related functions.

import pandas as pd
import numpy as np


def top_performing_product(df, nlargest):
    if "product_name" not in df.columns or "quantity" not in df.columns:
        raise ValueError(
            "DataFrame must contain 'product_name' and 'quantity' columns."
        )

    top_product = (
        df.groupby("product_name")["quantity"].sum().nlargest(nlargest).reset_index()
    )
    top_product.columns = ["Products", " Total Quantity Sold"]
    return top_product


def product_performance_summary(df):
    if "product_name" not in df.columns or "quantity" not in df.columns:
        raise ValueError(
            "DataFrame must contain 'product_name' and 'quantity' columns."
        )

    product_summary = (
        df.groupby("product_name")["quantity"]
        .agg(["sum", "mean", "count"])
        .reset_index()
    )
    product_summary.rename(
        columns={
            "sum": "total_quantity_sold",
            "mean": "average_quantity_ordered",
            "count": "total_order_count",
        },
        inplace=True,
    )

    if "revenue" in df.columns:
        avg_order_value = product_average_order_value(df)
        product_summary = product_summary.merge(
            avg_order_value, on="product_name", how="left"
        )

    if "customer_id" in df.columns:
        customer_count = product_customer_count(df)
        product_summary = product_summary.merge(
            customer_count, on="product_name", how="left"
        )

    return product_summary


def product_category_performance(df):
    if "category" not in df.columns or "quantity" not in df.columns:
        raise ValueError("DataFrame must contain 'category' and 'quantity' columns.")

    category_performance = df.groupby("category")["quantity"].sum().reset_index()
    category_performance.rename(
        columns={"quantity": "total_quantity_sold"}, inplace=True
    )
    return category_performance


def product_revenue_contribution(df):
    if "product_name" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'product_name' and 'revenue' columns.")

    total_revenue = df["revenue"].sum()
    revenue_contribution = df.groupby("product_name")["revenue"].sum().reset_index()
    revenue_contribution["contribution_percentage"] = (
        revenue_contribution["revenue"] / total_revenue
    ) * 100
    return revenue_contribution


def product_average_order_value(df):
    if "product_name" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'product_name' and 'revenue' columns.")

    average_order_value = df.groupby("product_name")["revenue"].mean().reset_index()
    average_order_value.rename(columns={"revenue": "average_order_value"}, inplace=True)
    return average_order_value


def product_customer_count(df):
    if "product_name" not in df.columns or "customer_id" not in df.columns:
        raise ValueError(
            "DataFrame must contain 'product_name' and 'customer_id' columns."
        )

    customer_count = df.groupby("product_name")["customer_id"].nunique().reset_index()
    customer_count.rename(
        columns={"customer_id": "unique_customer_count"}, inplace=True
    )
    return customer_count


def total_products_sold(df):
    if "quantity" not in df.columns:
        raise ValueError("DataFrame must contain 'quantity' column.")

    total_sold = df["quantity"].sum()
    return total_sold
