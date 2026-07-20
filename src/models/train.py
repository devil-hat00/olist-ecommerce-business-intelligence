"""
Model Training
"""

import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from src.config import RANDOM_STATE
from src.logger import get_logger

logger = get_logger(__name__)


def train_random_forest(
    df,
    feature_columns,
    target_column,
    save_path=None,
):

    logger.info("Preparing training data...")

    model_df = df.dropna(
        subset=feature_columns + [target_column]
    )

    X = model_df[feature_columns]

    y = model_df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=RANDOM_STATE,
    )

    logger.info("Training Random Forest...")

    model.fit(X_train, y_train)

    if save_path:

        joblib.dump(
            model,
            save_path,
        )

        logger.info(f"Model saved to {save_path}")

    return model, X_test, y_test