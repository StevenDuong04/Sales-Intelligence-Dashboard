# File: validation.py
# Author: Steven Duong
# Date: 2026-07-013
# Description: This file constains preprocessing functions to validate data.
import pandas as pd
import numpy as np

required_columns = ["transaction_id", "order_date", "customer_id", "product_name", "category", "quantity", "unit_price", "revenue"]

def check_required_columns(df):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

def data_type_validation(df):
    expected_types = {
        "transaction_id": np.integer,
        "order_date": np.datetime64,
        "customer_id": np.integer,
        "product_name": str,
        "category": str,
        "quantity": np.integer,
        "unit_price": np.float64,
        "revenue": np.float64
    }

    for column, expected_type in expected_types.items():
        if column in df.columns:
            if not np.issubdtype(df[column].dtype, expected_type):
                raise TypeError(f"Column '{column}' has incorrect data type. Expected {expected_type}, got {df[column].dtype}.")
            
def full_validation(df):
    try:
        check_required_columns(df)
        data_type_validation(df)
        print("Dataset is valid. No errors found.")
    except (ValueError, TypeError) as e:
        print(f"Validation error: {e}")