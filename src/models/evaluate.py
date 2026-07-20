"""
Model Evaluation
"""

import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from src.logger import get_logger

logger = get_logger(__name__)


def evaluate_model(
    model,
    X_test,
    y_test,
):

    prediction = model.predict(X_test)

    metrics = {

        "MAE": mean_absolute_error(
            y_test,
            prediction,
        ),

        "RMSE": np.sqrt(
            mean_squared_error(
                y_test,
                prediction,
            )
        ),

        "R2": r2_score(
            y_test,
            prediction,
        ),
    }

    logger.info(metrics)

    return metrics