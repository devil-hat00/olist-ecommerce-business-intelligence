"""
Helper Functions
"""

from __future__ import annotations

import pandas as pd


def format_currency(value: float) -> str:
    """
    Format number as Brazilian Real.
    """

    return f"R$ {value:,.2f}"


def format_percentage(value: float) -> str:
    """
    Convert decimal to percentage.
    """

    return f"{value:.2f}%"


def format_number(value: int) -> str:
    """
    Format integers with comma separator.
    """

    return f"{value:,}"


def calculate_total_revenue(payments: pd.DataFrame) -> float:
    """
    Calculate total revenue.
    """

    return payments["payment_value"].sum()


def calculate_average_rating(reviews: pd.DataFrame) -> float:
    """
    Calculate average review score.
    """

    return reviews["review_score"].mean()


def calculate_average_delivery(orders: pd.DataFrame) -> float:
    """
    Calculate average delivery days.
    """

    return orders["delivery_days"].mean()


def calculate_total_orders(orders: pd.DataFrame) -> int:
    """
    Number of unique orders.
    """

    return orders["order_id"].nunique()


def calculate_total_customers(customers: pd.DataFrame) -> int:
    """
    Number of customers.
    """

    return customers["customer_id"].nunique()


def calculate_total_sellers(sellers: pd.DataFrame) -> int:
    """
    Number of sellers.
    """

    return sellers["seller_id"].nunique()