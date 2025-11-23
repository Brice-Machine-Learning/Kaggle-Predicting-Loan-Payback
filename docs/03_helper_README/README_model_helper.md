# 🧠 Model Loader & Prediction Helper — README

## 1. Purpose
This document explains how to use the model loading and prediction utilities in:

```
src/utils/model_loader.py
```

These utilities make inference reproducible and consistent across environments.

---

## 2. Import the Helper

```python
from src.utils.model_loader import (
    load_model_and_threshold,
    predict_probabilities,
    predict_with_threshold,
)
```

---

## 3. Load Model + Threshold

```python
model, threshold = load_model_and_threshold(
    model_path="../../models/best_lgbm_model.pkl",
    threshold_path="../../models/threshold_metadata.json"
)
```

---

## 4. Predict Probabilities

```python
test_probs = predict_probabilities(model, X_test)
```

---

## 5. Predict Final Labels (0/1)

```python
final_preds = predict_with_threshold(model, X_test, threshold)
```

---

## 6. Full Kaggle Pipeline Example

```python
model, threshold = load_model_and_threshold()
test_probs = predict_probabilities(model, X_test)
final_preds = predict_with_threshold(model, X_test, threshold)

submission = pd.DataFrame({
    "id": test["id"],
    "loan_paid_back": final_preds
})

submission.to_csv("../data/submissions/submission.csv", index=False)
```

---

## 7. Reproducibility Benefits

- Consistent thresholding  
- Swappable models  
- Clean probability handling  
- Notebook-state independent  

---

## 8. File Placement

Recommended location:

```
src/utils/README_model_helper.md
```
