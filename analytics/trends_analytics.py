# File: trends_analytics.py
# Author: Steven Duong
# Date: 2026-08-07
# Description: This file contains trend analysis functions for products and customers.

import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing


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


# Forcasting
def forecast_rev(df, forecast_months):
    """
    Forecasts future revenue using Holt-Winters Exponential Smoothing.

    Returns a dataframe containing history revenue and forecasted revenue.
    """

    if "order_date" not in df.columns or "revenue" not in df.columns:
        raise ValueError("Dataframe must contain 'order_date' and 'revenue' columns.")

    if forecast_months <= 0:
        raise ValueError("forecast_months must be greater than 0.")

    data = df.copy()
    data["order_date"] = pd.to_datetime(data["order_date"])

    monthly_revenue = data.set_index("order_date")["revenue"].resample("MS").sum()

    if len(monthly_revenue) < 24:
        raise ValueError(
            "At least 24 months of revenue data are recommended for seasonal forecasting."
        )

    # Holts-Winter Model
    model = ExponentialSmoothing(
        monthly_revenue,
        trend="add",
        seasonal="add",
        seasonal_periods=12,
    )

    fitted_model = model.fit()

    forecast = fitted_model.forecast(forecast_months)

    forecast_df = pd.DataFrame(
        {
            "date": forecast.index,
            "forecast": forecast.values,
        }
    )

    return monthly_revenue, forecast_df


def revenue_growth_analysis(df):
    """
    Calculates month-over-month revenue growth rate.

    Returns a dataframe containing monthly revenue and
    the percentage of change from the previous month
    """

    if "order_date" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'order_date' and 'revenue' columns.")

    data = df.copy()
    data["order_date"] = pd.to_datetime(data["order_date"])

    monthly_revenue = (
        data.groupby(data["order_date"].dt.to_period("M"))["revenue"]
        .sum()
        .reset_index()
    )

    monthly_revenue.columns = ["month", "total_revenue"]

    monthly_revenue["growth_rate"] = (
        monthly_revenue["total_revenue"].pct_change().mul(100)
    )

    monthly_revenue["month"] = monthly_revenue["month"].astype(str)

    return monthly_revenue


def revenue_seasonality(df):
    """
    Calculates average revenue for each calendar month to
    identify seasonal revenue patterns.
    """

    if "order_date" not in df.columns or "revenue" not in df.columns:
        raise ValueError("DataFrame must contain 'order_date' and 'revenue' columns.")

    data = df.copy()
    data["order_date"] = pd.to_datetime(data["order_date"])

    data["month_number"] = data["order_date"].dt.month
    data["month_name"] = data["order_date"].dt.month_name()

    seasonality = (
        data.groupby(["month_number", "month_name"])["revenue"].mean().reset_index()
    )

    seasonality = seasonality.sort_values("month_number")

    seasonality.columns = [
        "month_number",
        "month",
        "average_revenue",
    ]

    return seasonality
