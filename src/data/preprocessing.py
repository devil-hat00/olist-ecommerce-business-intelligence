"""
preprocessing.py

Data preprocessing and feature engineering utilities
for the Olist E-Commerce Business Intelligence project.
"""

from __future__ import annotations

import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


# =============================================================================
# Delivery Features
# =============================================================================

def create_delivery_days(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create delivery duration feature.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Creating delivery_days feature...")

    data = df.copy()

    data["delivery_days"] = (
        data["order_delivered_customer_date"]
        - data["order_purchase_timestamp"]
    ).dt.days

    return data


# =============================================================================
# Approval Features
# =============================================================================

def create_approval_hours(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate approval time in hours.
    """

    logger.info("Creating approval_hours feature...")

    data = df.copy()

    data["approval_hours"] = (
        data["order_approved_at"]
        - data["order_purchase_timestamp"]
    ).dt.total_seconds() / 3600

    return data


# =============================================================================
# Purchase Date Features
# =============================================================================

def create_purchase_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Extract date related features.
    """

    logger.info("Creating purchase date features...")

    data = df.copy()

    purchase = data["order_purchase_timestamp"]

    data["purchase_year"] = purchase.dt.year
    data["purchase_month"] = purchase.dt.month
    data["purchase_day"] = purchase.dt.day
    data["purchase_hour"] = purchase.dt.hour
    data["purchase_weekday"] = purchase.dt.weekday
    data["purchase_week_name"] = purchase.dt.day_name()
    data["purchase_quarter"] = purchase.dt.quarter

    return data


# =============================================================================
# Weekend Feature
# =============================================================================

def create_weekend_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create weekend indicator.
    """

    logger.info("Creating weekend feature...")

    data = df.copy()

    data["is_weekend"] = (
        data["purchase_weekday"] >= 5
    ).astype(int)

    return data


# =============================================================================
# Delivery Status
# =============================================================================

def create_delivery_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Determine whether an order was delivered late.
    """

    logger.info("Creating delivery status feature...")

    data = df.copy()

    data["late_delivery"] = (
        data["order_delivered_customer_date"]
        >
        data["order_estimated_delivery_date"]
    ).astype(int)

    return data


# =============================================================================
# Pipeline
# =============================================================================

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Execute the complete feature engineering pipeline.
    """

    logger.info("Running feature engineering pipeline...")

    data = create_delivery_days(df)

    data = create_approval_hours(data)

    data = create_purchase_features(data)

    data = create_weekend_feature(data)

    data = create_delivery_status(data)

    logger.info("Feature engineering completed.")

    return data