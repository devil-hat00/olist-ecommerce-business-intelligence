"""
Main Streamlit Application
"""

import streamlit as st

from src.dashboard.layout import configure_page
from src.dashboard.sidebar import render_sidebar
from src.dashboard.pages import (
    executive_dashboard,
    sales_dashboard,
    customer_dashboard,
    logistics_dashboard,
    machine_learning_dashboard,
)

configure_page()

page = render_sidebar()

if page == "Executive Dashboard":
    executive_dashboard()

elif page == "Sales Analytics":
    sales_dashboard()

elif page == "Customer Analytics":
    customer_dashboard()

elif page == "Logistics":
    logistics_dashboard()

elif page == "Machine Learning":
    machine_learning_dashboard()