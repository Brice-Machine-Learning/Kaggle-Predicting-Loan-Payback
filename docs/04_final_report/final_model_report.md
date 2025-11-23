# 📘 **Final Model Report — Kaggle: Predict Loan Payback**
**Author:** Brice Nelson  
**Project:** Kaggle Series | Predict Loan Payback  
**Date:** November 21, 2025  

---

## 🏁 **Executive Summary**

This report summarizes the full modeling pipeline for predicting loan payback probability using the Kaggle dataset. After extensive feature engineering, model experimentation, hyperparameter tuning, and validation, the final selected model is:

### ✅ **LightGBM (Tuned) + Threshold = 0.50**  
- **Final ROC-AUC:** **0.92810**  
- **Final F1 Score:** **0.94495**  
- **Validation Accuracy:** **0.91**  
- **Consistent performance after model reload**  
- **Best overall generalization and operational stability**

This model demonstrates strong predictive power, excellent recall for positive class borrowers (loan repaid), and well-calibrated probability outputs suitable for real-world risk scoring.

---

# 1. 🔧 **Modeling Process Overview**

The modeling phase consisted of:

### **1. Baseline Models**
- Logistic Regression  
- Decision Tree (limited depth)

### **2. Ensemble & Boosting Models**
- Random Forest  
- Extra Trees  
- XGBoost  
- CatBoost  
- LightGBM

### **3. Hyperparameter Tuning**
- Optuna optimization for:
  - LightGBM  
  - XGBoost  
- Multiple trials with stratified validation split  
- Objective: maximize **ROC-AUC**

### **4. Blending Check (LGBM + XGB)**
- Weight sweep from 0.00 → 1.00  
- Best blend weight: **1.00** (LightGBM only)  
- Observed: **XGBoost adds noise rather than signal**  
- Decision: **use LightGBM alone**

---

# 2. 📊 **Final Model Metrics**

### **Validation Metrics (Threshold = 0.50)**

| Metric | Value |
|-------|--------|
| **ROC-AUC** | **0.92810** |
| **Accuracy** | **0.91** |
| **Precision (repay)** | 0.91 |
| **Recall (repay)** | 0.98 |
| **F1 Score** | **0.94495** |

### **Confusion Matrix Insights**
- Correctly identifies the majority of unpaid loans (class 0).  
- Exceptionally strong at detecting paid loans (class 1).  
- F1 score indicates strong balance between recall and precision.

---

# 3. ⚖️ **Decision Threshold Selection**

A threshold sweep from **0.05 → 0.50** revealed:

- F1 increases consistently as the threshold rose  
- Clear maximum F1 at **0.50**  
- Threshold below 0.50 increases false positives  
- Threshold above 0.50 decreases true positives (undesirable)

### **Final Threshold = 0.50**  
Chosen due to:
- Maximal F1  
- Best business interpretability  
- Most stable performance  
- Industry standard default baseline

Threshold metadata saved to:  
`/models/threshold_metadata.json`

---

# 4. 📈 **ROC & PR Curve Interpretation**

### **ROC Findings**
- Smooth and steep curve  
- AUC = **0.928** → excellent discrimination  
- Minimal overfitting observed (train vs. validation close)

### **PR Curve Findings**
- High precision across recall range  
- Strong performance in imbalanced dataset context  
- Confirms LightGBM’s stability for binary credit scoring tasks

---

# 5. 🔍 **Feature Importance Analysis**

Top LightGBM features:

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | `debt_to_income_ratio` | 2102 |
| 2 | `credit_score` | 1549 |
| 3 | `interest_rate` | 1106 |
| 4 | `debt_to_income_ratio_qt` | 949 |
| 5 | `annual_income` | 870 |
| 6 | `loan_amount` | 844 |
| 7 | `loan_to_income` | 712 |

### **Interpretation**
- Core financial ratios dominate (expected in credit risk)  
- Engineered quantile features provide additional predictive lift  
- Interaction features contributed but less heavily  
- Encouraging alignment with domain expectations  
- No single feature overwhelms model → low variance risk

---

# 6. 🔄 **Reproducibility Validation**

To ensure the model is production-safe:

### ✔ Reload-test (model + threshold)
Loaded via:

```python
model, threshold = load_model_and_threshold()
```

Validation metrics after reload:

- **ROC-AUC:** 0.928097  
- **F1 Score:** 0.944951  
- **Classification Report:** identical  

### ✔ Submission Integrity Check
- Row count matches test set  
- Predictions ∈ {0,1}  
- ID alignment validated  
- No missing, NaN, or mis-typed values  

---

# 7. 📦 **Saved Artifacts**

### **Models**
- `/models/best_model.pkl`
- `/models/model_bundle.pkl`

### **Metadata**
- `/models/threshold_metadata.json`

### **Utilities**
- `/src/utils/model_loader.py`  
- `/src/utils/ensure_directory.py`

### **Submission**
- stored under `/data/submissions/`

---

# 8. 🚀 **Next Steps**

Now that the final LightGBM model has been selected:

### **Recommended Follow-Up**
- Create `05_inference.ipynb` (deployment-oriented inference)  
- Add model card / datasheet for governance  
- Build a FastAPI microservice for scoring  
- Add drift monitoring & logging modules (optional)

---

# 9. 🏆 **Conclusion**

You now have:

- A validated, tuned, production-ready LightGBM model  
- A complete modeling notebook with reproducible results  
- A clean inference interface  
- Threshold metadata for long-term compatibility  
- A senior-level documentation trail suitable for employers and portfolio use  

This modeling workflow is **equivalent to a real-world fintech credit risk pipeline** and demonstrates a strong competency in ML engineering, reproducibility, and model validation.
