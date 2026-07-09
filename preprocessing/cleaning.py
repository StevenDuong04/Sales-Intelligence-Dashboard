# File: cleaning.py
# Author: Steven Duong
# Date: 2026-07-08
# Description: This file contains preprocessing functions to clean data.

import pandas as pd
import numpy as np

def convert_dates(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

def handle_missing_values(df):
    # Remove empty rows
    df = df.dropna(how='all')
    # Fill missing values with mean for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        mean_value = df[col].mean()
        df[col] = df[col].fillna(mean_value)
    
    # Warn user about missing values being filled
    print("Missing values have been filled.")
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def standardize_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def clean_data(df):
    df = standardize_columns(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    return df