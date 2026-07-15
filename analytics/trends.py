# File: trends.py
# Author: Steven Duong
# Date: 2026-07-14
# Description: This file contains trend analysis functions for products and customers.

import pandas as pd
import numpy as np


# Product Trends
def product_sales_trend(df, product_name):
    if 'product_name' not in df.columns or 'order_date' not in df.columns or 'quantity' not in df.columns:
        raise ValueError("DataFrame must contain 'product_name', 'order_date', and 'quantity' columns.")
    
    product_df = df[df['product_name'] == product_name]
    sales_trend = product_df.groupby('order_date')['quantity'].sum().reset_index()
    return sales_trend

def product_category_sales_trend(df, category):
    if 'category' not in df.columns or 'order_date' not in df.columns or 'quantity' not in df.columns:
        raise ValueError("DataFrame must contain 'category', 'order_date', and 'quantity' columns.")
    
    category_df = df[df['category'] == category]
    sales_trend = category_df.groupby('order_date')['quantity'].sum().reset_index()
    return sales_trend

# Customer Trends
def customer_purchase_trend(df, customer_id):
    if 'customer_id' not in df.columns or 'order_date' not in df.columns or 'quantity' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id', 'order_date', and 'quantity' columns.")
    
    customer_df = df[df['customer_id'] == customer_id]
    purchase_trend = customer_df.groupby('order_date')['quantity'].sum().reset_index()
    return purchase_trend

def customer_order_frequency(df):
    if 'customer_id' not in df.columns or 'order_date' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' and 'order_date' columns.")
    
    order_frequency = df.groupby('customer_id')['order_date'].nunique().reset_index()
    order_frequency.rename(columns={'order_date': 'order_frequency'}, inplace=True)
    return order_frequency

# Revenue Trends
def monthly_revenue_trend(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    monthly_revenue = df.groupby(df['order_date'].dt.to_period('M'))['revenue'].sum().reset_index()
    monthly_revenue.columns = ['month', 'total_revenue']
    return monthly_revenue

def yearly_revenue_trend(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    yearly_revenue = df.groupby(df['order_date'].dt.to_period('Y'))['revenue'].sum().reset_index()
    yearly_revenue.columns = ['year', 'total_revenue']
    return yearly_revenue

def revenue_growth_trend(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['year'] = df['order_date'].dt.year
    yearly_revenue = df.groupby('year')['revenue'].sum().reset_index()
    yearly_revenue['growth_rate'] = yearly_revenue['revenue'].pct_change()
    return yearly_revenue