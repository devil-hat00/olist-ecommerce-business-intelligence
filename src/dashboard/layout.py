"""
Dashboard Layout
"""

import streamlit as st


def configure_page():

    st.set_page_config(
        page_title="Olist Business Intelligence",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("🛒 Olist Business Intelligence Dashboard")

    st.markdown(
        """
        Interactive Business Intelligence Dashboard
        built using the Olist Brazilian E-Commerce Dataset.
        """
    )