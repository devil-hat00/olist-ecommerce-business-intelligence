import pandas as pd

from src.data.merge import build_sales_dataset


def test_sales_merge():

    orders = pd.DataFrame({
        "order_id": ["1"],
        "customer_id": ["A"]
    })

    customers = pd.DataFrame({
        "customer_id": ["A"]
    })

    payments = pd.DataFrame({
        "order_id": ["1"],
        "payment_value": [200]
    })

    df = build_sales_dataset(
        orders,
        customers,
        payments
    )

    assert df.shape[0] == 1

    assert "payment_value" in df.columns