# File: loader.py
# Author: Steven Duong
# Date: 2026-07-08
# Description: This file contains the loader to load data from CSV or excel files.

import pandas as pd

def load_csv(file):
    df = pd.read_csv(file)
    return df

def load_excel(file):
    df = pd.read_excel(file)
    return df


def load_data(file):
    extension = file.split(".")[-1]

    if extension == "csv":
        return load_csv(file)
    
    elif extension in ["xlsx", "xls"]:
        return load_excel(file)
    
    else:
        ValueError("Unsupported file type")