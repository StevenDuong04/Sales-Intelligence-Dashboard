# File: app.py
# Author: Steven Duong
# Date: 2026-07-16
# Description: This file contains the layout for the application for users to use.

import streamlit as st

if "raw_df" not in st.session_state:
    st.session_state["raw_df"] = None

if "dataset" not in st.session_state:
    st.session_state["dataset"] = None

page = st.navigation(["pages/overview.py", "pages/customers.py", "pages/products.py", "pages/revenue.py"], position="top")
page.run()