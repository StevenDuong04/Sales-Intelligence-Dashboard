# File: helpers.py
# Author: Steven Duong
# Date: 2026-07-20
# Description: This file contains the helper functions to help with small things.

import streamlit as st

def init_page(title):
    st.set_page_config(
        page_title=title, page_icon=":bar_chart:", layout="wide"
    )