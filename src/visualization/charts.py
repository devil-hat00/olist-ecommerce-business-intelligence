"""
charts.py

Reusable Plotly visualizations for the
Olist Business Intelligence Dashboard.
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px  # type: ignore[reportMissingImports]

from src.logger import get_logger

logger = get_logger(__name__)

# =============================================================================
# Monthly Revenue Trend
# =============================================================================

def monthly_revenue_chart(df: pd.DataFrame):

    logger.info("Creating Monthly Revenue Chart")

    data = df.copy()

    data["Month"] = (
        data["order_purchase_timestamp"]
        .dt.to_period("M")
        .astype(str)
    )

    revenue = (
        data.groupby("Month")["payment_value"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue,
        x="Month",
        y="payment_value",
        markers=True,
        title="Monthly Revenue Trend",
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue (R$)",
        template="plotly_dark",
    )

    return fig


# =============================================================================
# Payment Methods
# =============================================================================

def payment_method_chart(payments: pd.DataFrame):

    logger.info("Creating Payment Method Chart")

    payment = (
        payments["payment_type"]
        .value_counts()
        .reset_index()
    )

    payment.columns = [
        "Payment Method",
        "Count",
    ]

    fig = px.bar(
        payment,
        x="Payment Method",
        y="Count",
        title="Payment Method Distribution",
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


# =============================================================================
# Review Distribution
# =============================================================================

def review_score_chart(reviews: pd.DataFrame):

    logger.info("Creating Review Score Chart")

    review = (
        reviews["review_score"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    review.columns = [
        "Review Score",
        "Count",
    ]

    fig = px.bar(
        review,
        x="Review Score",
        y="Count",
        title="Customer Review Scores",
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig


# =============================================================================
# Delivery Time
# =============================================================================

def delivery_distribution_chart(orders: pd.DataFrame):

    logger.info("Creating Delivery Distribution Chart")

    fig = px.histogram(
        orders,
        x="delivery_days",
        nbins=40,
        title="Delivery Time Distribution",
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Delivery Days",
    )

    return fig


# =============================================================================
# Top Product Categories
# =============================================================================

def top_category_chart(product_sales: pd.DataFrame):

    logger.info("Creating Top Product Categories Chart")

    category = (
        product_sales
        .groupby("product_category_name_english")["payment_value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        category,
        x="product_category_name_english",
        y="payment_value",
        title="Top Product Categories by Revenue",
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Category",
        yaxis_title="Revenue (R$)",
    )

    return fig


# =============================================================================
# Feature Importance
# =============================================================================

def feature_importance_chart(importance: pd.Series):

    logger.info("Creating Feature Importance Chart")

    df = (
        importance
        .reset_index()
    )

    df.columns = [
        "Feature",
        "Importance",
    ]

    fig = px.bar(
        df,
        x="Feature",
        y="Importance",
        title="Feature Importance",
    )

    fig.update_layout(
        template="plotly_dark",
    )

    return fig