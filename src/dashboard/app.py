"""
Main Streamlit Application
"""

import sys
from pathlib import Path

# Add project root to Python path BEFORE importing src
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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


def main():
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


if __name__ == "__main__":
    main()