# 🧭 Project Plan — Predict Loan Payback (Kaggle Series)

**Competition Dates:** November 1 – November 30, 2025  
**Repository:** `Kaggle-Predict-Loan-Payback`  
**Goal:** Build and evaluate a machine learning model to predict whether a loan will be paid back, based on borrower and loan attributes.

---

## **Phase 1 — Project Setup & Environment (Nov 1–3)**

**Objectives:**
- Initialize local development and version control.
- Set up consistent environments (pip / conda / uv).
- Connect CLI to Kaggle for dataset download and submission.

**Key Tasks:**
- [x] Create repo with `.gitignore`, `environment.yml`, `requirements.txt`.
- [x] Add `README.md` and `docs/reference.md` for competition metadata.
- [x] Configure Kaggle CLI and authenticate.
- [x] Create initial project structure:

---

## **Phase 2 — Data Understanding & Exploration (Nov 3–8)**

**Objectives:**
- Load and inspect training and test datasets.
- Identify missing values, categorical vs numerical columns, and potential data leakage.

**Key Tasks:**
- [x] Summarize key statistics (mean, median, skew, correlations).
- [x] Visualize distributions (loan amount, term, credit score, etc.).
- [x] Identify relationships between predictors and target variable.
- [x] Document findings in `notebooks/01_eda.ipynb`.

**Deliverable:**  
- [x] EDA notebook with clear narrative and saved plots (`/figures/`).

---

## **Phase 3 — Feature Engineering & Preprocessing (Nov 9–14)**

**Objectives:**
- Clean and transform data for model ingestion.

**Key Tasks:**
- [ ] Handle missing values (imputation or drop).
- [ ] Encode categorical features (One-Hot / Target Encoding).
- [ ] Scale or normalize numeric variables.
- [ ] Engineer derived features (e.g., loan-to-income ratio, age buckets).
- [ ] Split training and validation sets.

**Deliverable:**  
Processed dataset saved under `/data/processed/`.

---

## **Phase 4 — Model Development (Nov 15–21)**

**Objectives:**
- Train multiple models, evaluate, and tune.

**Key Tasks:**
- [ ] Baseline model (Logistic Regression).
- [ ] Gradient boosting models (XGBoost, LightGBM, CatBoost).
- [ ] Hyperparameter tuning (Optuna or GridSearchCV).
- [ ] Compare models on ROC-AUC / F1-score.
- [ ] Save best model with `joblib` or `pickle`.

**Deliverable:**  
Modeling notebook + saved model file in `/models/`.

---

## **Phase 5 — Validation, Documentation & Submission (Nov 22–28)**

**Objectives:**
- Validate on hold-out set and prepare Kaggle submission.

**Key Tasks:**
- [ ] Validate model generalization performance.
- [ ] Prepare `submission.csv` in Kaggle format.
- [ ] Run `kaggle competitions submit` via CLI.
- [ ] Document methodology and results in `README.md`.

**Deliverable:**  
Final submission file + updated documentation.

---

## **Phase 6 — Review & Retrospective (Nov 29–30)**

**Objectives:**
- Review approach, lessons learned, and potential improvements.

**Key Tasks:**
- [ ] Record competition leaderboard score and rank.
- [ ] Summarize key learnings in `/docs/final_report.md`.
- [ ] Reflect on reproducibility and potential code improvements.

---

## ✅ **Milestones**

| Date (2025) | Milestone | Deliverable |
|--------------|------------|--------------|
| Nov 3 | Environment setup complete | Repo initialized |
| Nov 8 | EDA completed | 01_exploration.ipynb |
| Nov 14 | Feature engineering complete | Processed data |
| Nov 21 | Model training complete | 02_modeling.ipynb |
| Nov 28 | Submission ready | submission.csv |
| Nov 30 | Competition end | final_report.md |

---

## **Optional Enhancements**
- Integrate MLflow or Weights & Biases for experiment tracking.
- Containerize with Docker for reproducibility.
- Add a `Makefile` for automated workflow steps.
- Create a small Streamlit dashboard for model insights.

---

**Author:** Brice Nelson 
**Last Updated:** November 2, 2025
