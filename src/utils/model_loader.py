# src/utils/model_loader.py
"""
Universal model loading + prediction utility for the Predict Loan Payback project.
Supports LightGBM, XGBoost, CatBoost, and scikit-learn models.
"""

import json
from pathlib import Path
from typing import Any, Tuple, Optional

import joblib
import numpy as np
import pandas as pd


# ------------------------------------------------------------
# Load Model + Threshold Metadata
# ------------------------------------------------------------

def load_model_and_threshold(
    model_path: str = "../models/best_model.pkl",
    threshold_path: str = "../models/threshold_metadata.json",
    fallback_threshold: float = 0.50,
) -> Tuple[Any, float]:
    """
    Loads any trained model (LightGBM, XGBoost, CatBoost, sklearn)
    plus its optimal threshold metadata.

    Parameters
    ----------
    model_path : str
        Path to a joblib-serialized model.
    threshold_path : str
        Path to threshold metadata JSON file.
    fallback_threshold : float
        Threshold used if file not found.

    Returns
    -------
    model : Any
        Loaded ML model.
    threshold : float
        Classification threshold.
    """

    # ---- Load model ----
    model_file = Path(model_path)
    if not model_file.exists():
        raise FileNotFoundError(f"Model file not found: {model_file}")

    model = joblib.load(model_file)

    # ---- Load threshold ----
    threshold_file = Path(threshold_path)
    if threshold_file.exists():
        try:
            with open(threshold_file, "r") as f:
                meta = json.load(f)
                threshold = meta.get("threshold", fallback_threshold)
        except Exception:
            threshold = fallback_threshold
    else:
        threshold = fallback_threshold

    return model, threshold


# ------------------------------------------------------------
# Predict Probabilities (Model-Agnostic)
# ------------------------------------------------------------

def predict_probabilities(model: Any, X: pd.DataFrame) -> np.ndarray:
    """
    Produces probability estimates from any model that supports:
    - predict_proba()
    - predict() returning probabilities (fallback)
    - CatBoost predict() which returns raw preds for classification

    Parameters
    ----------
    model : Any
        Trained model with predict_proba() or predict().
    X : pd.DataFrame
        Feature matrix.

    Returns
    -------
    np.ndarray
        Probability of class 1.
    """

    # Preferred method
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)[:, 1]

    # CatBoost: model.predict(X) may return probabilities directly
    if hasattr(model, "predict"):
        raw = model.predict(X)
        raw = np.array(raw).squeeze()

        # If predictions are logits or raw scores, try to sigmoid-transform them
        if raw.ndim == 1:
            # Case: Already probabilities (0–1)
            if raw.min() >= 0 and raw.max() <= 1:
                return raw

            # Otherwise apply sigmoid
            return 1 / (1 + np.exp(-raw))

        # If CatBoost outputs shape (n_samples, 2)
        if raw.ndim == 2 and raw.shape[1] == 2:
            return raw[:, 1]

        raise ValueError(
            "Model.predict() returned unexpected shape. Cannot derive probabilities."
        )

    raise ValueError("Model does not have predict_proba() or usable predict().")


# ------------------------------------------------------------
# Predict Final Labels Using Threshold
# ------------------------------------------------------------

def predict_with_threshold(model: Any, X: pd.DataFrame, threshold: float) -> np.ndarray:
    """
    Predicts 0/1 class labels using model + threshold.

    Parameters
    ----------
    model : Any
        Trained classifier model.
    X : pd.DataFrame
        Feature matrix.
    threshold : float
        Decision threshold.

    Returns
    -------
    np.ndarray
        Binary class predictions.
    """

    probs = predict_probabilities(model, X)
    preds = (probs >= threshold).astype(int)
    return preds
