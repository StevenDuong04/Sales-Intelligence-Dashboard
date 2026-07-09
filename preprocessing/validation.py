# File: validation.py
# Author: Steven Duong
# Date: 2026-07-08
# Description: This file constains preprocessing functions to validate data.
import pandas as pd
import numpy as np

required_columns = ["transaction_id", "order_date", "customer_id", "product_name", "category", "quantity", "unit_price", "revenue"]

def check_required_columns(df):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")
    
# TODO: Add data type validation, and full validation that checks everything and lets user know dataset is valid and no errors. If errors, let user know what the errors are and how to fix them.