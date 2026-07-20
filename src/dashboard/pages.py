"""
Dashboard Pages
"""

import streamlit as st

from src.data.loader import load_processed_data

from src.data.preprocessing import create_features

from src.data.merge import (
    build_sales_dataset,
    build_product_sales_dataset,
)

from src.dashboard.kpis import show_kpis

from src.visualization.charts import (
    monthly_revenue_chart,
    payment_method_chart,
    review_score_chart,
    delivery_distribution_chart,
    top_category_chart,
)


@st.cache_data
def load():

    data = load_processed_data()

    data["orders"] = create_features(
        data["orders"]
    )

    return data


def executive_dashboard():

    data = load()

    sales = build_sales_dataset(
        data["orders"],
        data["customers"],
        data["payments"],
    )

    revenue = data["payments"]["payment_value"].sum()

    orders = data["orders"]["order_id"].nunique()

    customers = data["customers"]["customer_id"].nunique()

    sellers = data["sellers"]["seller_id"].nunique()

    rating = data["reviews"]["review_score"].mean()

    delivery = data["orders"]["delivery_days"].mean()

    show_kpis(
        revenue,
        orders,
        customers,
        sellers,
        rating,
        delivery,
    )

    st.markdown("---")

    st.plotly_chart(
        monthly_revenue_chart(sales),
        use_container_width=True,
    )


def sales_dashboard():

    data = load()

    sales = build_sales_dataset(
        data["orders"],
        data["customers"],
        data["payments"],
    )

    st.header("Sales Analytics")

    st.plotly_chart(
        monthly_revenue_chart(sales),
        use_container_width=True,
    )

    st.plotly_chart(
        payment_method_chart(
            data["payments"]
        ),
        use_container_width=True,
    )


def customer_dashboard():

    data = load()

    st.header("Customer Analytics")

    st.plotly_chart(
        review_score_chart(
            data["reviews"]
        ),
        use_container_width=True,
    )


def logistics_dashboard():

    data = load()

    st.header("Logistics")

    st.plotly_chart(
        delivery_distribution_chart(
            data["orders"]
        ),
        use_container_width=True,
    )


def machine_learning_dashboard():

    data = load()

    product = build_product_sales_dataset(
        data["order_items"],
        data["products"],
        data["translation"],
        data["payments"],
    )

    st.header("Product Analytics")

    st.plotly_chart(
        top_category_chart(product),
        use_container_width=True,
    )

    st.success(
        "Machine Learning model integration coming next."
    )