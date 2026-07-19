# File: trends.py
# Author: Steven Duong
# Date: 2026-07-18
# Description: This file contains the layout for the trends page.

import streamlit as st
import pandas as pd

import analytics.trends_analytics as trends

import visualization.charts as charts

st.header("Trend Analysis", text_alignment="left")

if (
    "dataset" not in st.session_state or st.session_state["dataset"] is None
):  # Make sure to check if dataset is None as well
    st.warning("Please upload a dataset first in Overview")

else:
    df = st.session_state["dataset"]

    # TODO: Add a side panel that has filters for: Date range, metrics, etc
    # TODO: Time Series Analysis on different things
    # TODO: Seasonality, Correlations,
    # TODO: Potentially a Future trend