"""
Sidebar
"""

import streamlit as st


def render_sidebar():

    st.sidebar.title("Navigation")

    page = st.sidebar.radio(
        "",
        [
            "Executive Dashboard",
            "Sales Analytics",
            "Customer Analytics",
            "Logistics",
            "Machine Learning",
        ],
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
Built with

• Streamlit

• Plotly

• Scikit-Learn

• Pandas
"""
    )

    return page