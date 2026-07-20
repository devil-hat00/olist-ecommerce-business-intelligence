"""
loader.py

Loads all processed datasets used in the project.
"""

from pathlib import Path
import pandas as pd

from src.config import PROCESSED_DATA_DIR
from src.logger import get_logger

logger = get_logger(__name__)


DATE_COLUMNS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def _load_csv(filename: str, parse_dates=None) -> pd.DataFrame:
    """
    Load a CSV file from the processed data directory.

    Parameters
    ----------
    filename : str
        CSV filename.

    parse_dates : list | None
        Datetime columns.

    Returns
    -------
    pd.DataFrame
    """

    filepath = PROCESSED_DATA_DIR / filename

    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} not found.")

    logger.info(f"Loading {filename}")

    return pd.read_csv(
        filepath,
        parse_dates=parse_dates,
    )


def load_processed_data() -> dict:
    """
    Load every processed dataset.

    Returns
    -------
    dict
        Dictionary of DataFrames.
    """

    logger.info("Loading processed datasets...")

    datasets = {
        "customers": _load_csv("customers_clean.csv"),
        "geolocation": _load_csv("geolocation_clean.csv"),
        "order_items": _load_csv("order_items_clean.csv"),
        "payments": _load_csv("payments_clean.csv"),
        "reviews": _load_csv("reviews_clean.csv"),
        "orders": _load_csv(
            "orders_clean.csv",
            parse_dates=DATE_COLUMNS,
        ),
        "products": _load_csv("products_clean.csv"),
        "sellers": _load_csv("sellers_clean.csv"),
        "translation": _load_csv("translation_clean.csv"),
    }

    logger.info("All datasets loaded successfully.")

    for name, df in datasets.items():
        logger.info(f"{name:<15} Shape: {df.shape}")

    return datasets