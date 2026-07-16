# File: validation.py
# Author: Steven Duong
# Date: 2026-07-15
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
        "transaction_id": "integer",
        "order_date": "datetime",
        "customer_id": "integer",
        "product_name": "string",
        "category": "string",
        "quantity": "integer",
        "unit_price": "float",
        "revenue": "float"
    }

    for column, expected_type in expected_types.items():

        if column not in df.columns:
            continue

        dtype = df[column].dtype

        if expected_type == "integer":
            valid = pd.api.types.is_integer_dtype(dtype)

        elif expected_type == "float":
            valid = pd.api.types.is_float_dtype(dtype)

        elif expected_type == "datetime":
            valid = pd.api.types.is_datetime64_any_dtype(dtype)

        elif expected_type == "string":
            valid = pd.api.types.is_string_dtype(dtype)

        else:
            valid = True

        if not valid:
            raise TypeError(
                f"Column '{column}' has incorrect data type. "
                f"Expected {expected_type}, got {dtype}."
            )
        
def full_validation(df):
    try:
        check_required_columns(df)
        data_type_validation(df)
        print("Dataset is valid. No errors found.")
    except (ValueError, TypeError) as e:
        print(f"Validation error: {e}")