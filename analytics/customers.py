# File: customers.py
# Author: Steven Duong
# Date: 2026-07-14
# Description: This file contains customer analytics functions.

import pandas as pd
import numpy as np

def top_customers_by_revenue(df, top_n=10):
    if 'customer_id' not in df.columns or 'revenue' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' and 'revenue' columns.")
    
    top_customers = df.groupby('customer_id')['revenue'].sum().nlargest(top_n).reset_index()
    return top_customers

def customer_most_bought_product(df, top_n=10):
    if 'customer_id' not in df.columns or 'product_name' not in df.columns or 'quantity' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id', 'product_name' and 'quantity' columns.")
    
    most_bought = df.groupby('product_name')[df['customer_id', 'quantity']].sum().nlargest(top_n, 'quantity').reset_index()
    return most_bought

def customer_most_bought_category(df, top_n=10):
    if 'customer_id' not in df.columns or 'category' not in df.columns or 'quantity' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id', 'category' and 'quantity' columns.")
    
    most_bought = df.groupby('category')[df['customer_id', 'quantity']].sum().nlargest(top_n, 'quantity').reset_index()
    return most_bought

def customer_average_order_value(df):
    if 'customer_id' not in df.columns or 'revenue' not in df.columns:
        raise ValueError("DataFrame must contain 'customer_id' and 'revenue' columns.")
    
    average_order_value = df.groupby('customer_id')['revenue'].mean().reset_index()
    average_order_value.rename(columns={'revenue': 'average_order_value'}, inplace=True)
    return average_order_value
