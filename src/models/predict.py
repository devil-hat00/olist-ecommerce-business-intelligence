"""
Prediction utilities.
"""

import pandas as pd


def predict_delivery_time(
    model,
    payment_value,
    installments,
    purchase_month,
    purchase_day,
    purchase_weekday,
    purchase_hour,
    approval_hours,
):

    sample = pd.DataFrame({

        "payment_value": [payment_value],

        "payment_installments": [installments],

        "purchase_month": [purchase_month],

        "purchase_day": [purchase_day],

        "purchase_weekday": [purchase_weekday],

        "purchase_hour": [purchase_hour],

        "approval_hours": [approval_hours],
    })

    prediction = model.predict(sample)

    return float(prediction[0])