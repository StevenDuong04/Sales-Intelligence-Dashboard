# File: revenue.py
# Author: Steven Duong
# Date: 2026-07-13
# Description: This file contains revenue calculation functions.

import pandas as pd
import numpy as np
from analytics.kpis import calculate_total_revenue, calculate_total_orders

def calculate_revenue(df):
    calculate_total_revenue(df)
    
def revenue_growth_rate(df, previous_period_df):
    current_revenue = calculate_total_revenue(df)
    previous_revenue = calculate_total_revenue(previous_period_df)
    
    if previous_revenue == 0:
        raise ValueError("Previous period revenue is zero, cannot calculate growth rate.")
    
    growth_rate = (current_revenue - previous_revenue) / previous_revenue
    return growth_rate

# def net_profit_margin(df): Need to have a column for expenses in order to calculate net profit margin. This function is not implemented yet.

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

def average_revenue_per_user(df):
    total_revenue = calculate_total_revenue(df)
    unique_users = df['customer_id'].nunique()
    
    if unique_users == 0:
        raise ValueError("No unique users found, cannot calculate average revenue per user.")
    
    average_revenue = total_revenue / unique_users
    return average_revenue

def revenue_per_product(df):
    revenue_by_product = df.groupby('product_name')['revenue'].sum().reset_index()
    revenue_by_product.columns = ['product_name', 'total_revenue']
    return revenue_by_product

def revenue_per_category(df):
    revenue_by_category = df.groupby('category')['revenue'].sum().reset_index()
    revenue_by_category.columns = ['category', 'total_revenue']
    return revenue_by_category