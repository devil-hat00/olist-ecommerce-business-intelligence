"""
merge.py

Functions for merging Olist datasets into
analysis-ready DataFrames.
"""

from __future__ import annotations

import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


# =============================================================================
# Orders + Customers
# =============================================================================

def merge_orders_customers(
    orders: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge orders with customer information.
    """

    logger.info("Merging Orders + Customers")

    return orders.merge(
        customers,
        on="customer_id",
        how="left",
    )


# =============================================================================
# Orders + Payments
# =============================================================================

def merge_orders_payments(
    orders: pd.DataFrame,
    payments: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge orders with payment data.
    """

    logger.info("Merging Orders + Payments")

    return orders.merge(
        payments,
        on="order_id",
        how="left",
    )


# =============================================================================
# Orders + Reviews
# =============================================================================

def merge_orders_reviews(
    orders: pd.DataFrame,
    reviews: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge orders with customer reviews.
    """

    logger.info("Merging Orders + Reviews")

    return orders.merge(
        reviews,
        on="order_id",
        how="left",
    )


# =============================================================================
# Order Items + Products
# =============================================================================

def merge_order_items_products(
    order_items: pd.DataFrame,
    products: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge order items with product information.
    """

    logger.info("Merging Order Items + Products")

    return order_items.merge(
        products,
        on="product_id",
        how="left",
    )


# =============================================================================
# Products + Translation
# =============================================================================

def merge_product_translation(
    products: pd.DataFrame,
    translation: pd.DataFrame
) -> pd.DataFrame:
    """
    Add English category names.
    """

    logger.info("Adding Product Category Translation")

    return products.merge(
        translation,
        on="product_category_name",
        how="left",
    )


# =============================================================================
# Sales Dataset
# =============================================================================

def build_sales_dataset(
    orders: pd.DataFrame,
    customers: pd.DataFrame,
    payments: pd.DataFrame
) -> pd.DataFrame:
    """
    Build dataset for revenue analysis.
    """

    logger.info("Building Sales Dataset")

    sales = (
        orders
        .merge(customers, on="customer_id", how="left")
        .merge(payments, on="order_id", how="left")
    )

    logger.info(f"Sales Dataset Shape: {sales.shape}")

    return sales


# =============================================================================
# Product Sales Dataset
# =============================================================================

def build_product_sales_dataset(
    order_items: pd.DataFrame,
    products: pd.DataFrame,
    translation: pd.DataFrame,
    payments: pd.DataFrame
) -> pd.DataFrame:
    """
    Build dataset for product analytics.
    """

    logger.info("Building Product Sales Dataset")

    product_sales = (
        order_items
        .merge(products, on="product_id", how="left")
        .merge(
            translation,
            on="product_category_name",
            how="left",
        )
        .merge(payments, on="order_id", how="left")
    )

    logger.info(f"Product Dataset Shape: {product_sales.shape}")

    return product_sales


# =============================================================================
# Machine Learning Dataset
# =============================================================================

def build_model_dataset(
    orders: pd.DataFrame,
    customers: pd.DataFrame,
    payments: pd.DataFrame
) -> pd.DataFrame:
    """
    Build modeling dataset.
    """

    logger.info("Building Machine Learning Dataset")

    model = (
        orders
        .merge(customers, on="customer_id", how="left")
        .merge(payments, on="order_id", how="left")
    )

    logger.info(f"Model Dataset Shape: {model.shape}")

    return model