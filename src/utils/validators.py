"""
Validation Utilities
"""

from __future__ import annotations

import pandas as pd


def validate_required_columns(
    df: pd.DataFrame,
    required_columns: list[str],
) -> None:
    """
    Validate required columns exist.
    """

    missing = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing columns: {missing}"
        )


def validate_empty_dataframe(
    df: pd.DataFrame,
) -> None:
    """
    Ensure DataFrame is not empty.
    """

    if df.empty:
        raise ValueError(
            "DataFrame is empty."
        )


def validate_null_target(
    df: pd.DataFrame,
    target: str,
) -> None:
    """
    Ensure target variable contains values.
    """

    if df[target].isna().all():
        raise ValueError(
            f"{target} contains only missing values."
        )


def validate_model_features(
    df: pd.DataFrame,
    features: list[str],
) -> None:
    """
    Validate model features.
    """

    validate_required_columns(
        df,
        features,
    )

    validate_empty_dataframe(df)