import pandas as pd

from src.models.train import train_random_forest


def test_model_training():

    df = pd.DataFrame({

        "payment_value": [10,20,30,40,50],

        "payment_installments":[1,2,1,3,2],

        "purchase_month":[1,2,3,4,5],

        "purchase_day":[1,2,3,4,5],

        "purchase_weekday":[1,2,3,4,5],

        "purchase_hour":[10,11,12,13,14],

        "approval_hours":[1,2,3,4,5],

        "delivery_days":[5,6,4,7,3]
    })

    model, _, _ = train_random_forest(

        df,

        feature_columns=[
            "payment_value",
            "payment_installments",
            "purchase_month",
            "purchase_day",
            "purchase_weekday",
            "purchase_hour",
            "approval_hours",
        ],

        target_column="delivery_days"

    )

    assert model is not None