import pandas as pd

from src.data.preprocessing import create_features


def test_create_features():

    df = pd.DataFrame({
        "order_purchase_timestamp": pd.to_datetime(["2018-01-01"]),
        "order_approved_at": pd.to_datetime(["2018-01-01 02:00"]),
        "order_delivered_customer_date": pd.to_datetime(["2018-01-05"]),
        "order_estimated_delivery_date": pd.to_datetime(["2018-01-04"])
    })

    result = create_features(df)

    assert "delivery_days" in result.columns
    assert "approval_hours" in result.columns
    assert "purchase_month" in result.columns
    assert "late_delivery" in result.columns