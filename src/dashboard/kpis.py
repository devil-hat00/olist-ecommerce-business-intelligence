"""
KPI Cards
"""

import streamlit as st


def show_kpis(
    revenue,
    orders,
    customers,
    sellers,
    rating,
    delivery,
):

    c1, c2, c3 = st.columns(3)

    c4, c5, c6 = st.columns(3)

    c1.metric(
        "Revenue",
        f"R$ {revenue:,.0f}",
    )

    c2.metric(
        "Orders",
        f"{orders:,}",
    )

    c3.metric(
        "Customers",
        f"{customers:,}",
    )

    c4.metric(
        "Sellers",
        f"{sellers:,}",
    )

    c5.metric(
        "Average Rating",
        f"{rating:.2f}",
    )

    c6.metric(
        "Avg Delivery",
        f"{delivery:.2f} Days",
    )