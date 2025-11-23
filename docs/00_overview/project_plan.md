# 🧭 Project Plan — Predict Loan Payback (Kaggle Series)

**Competition Dates:** November 1 – November 30, 2025  
**Repository:** `Kaggle-Predict-Loan-Payback`  
**Goal:** Build and evaluate a machine learning model to predict whether a loan will be paid back using borrower and loan attributes.

---

## **Phase 1 — Project Setup & Environment (Nov 1–3)**

**Objectives:**
- Initialize environment, repo structure, and reproducibility.
- Set up tooling for data access and experiment tracking.

**Key Tasks:**
- [x] Create repo with `.gitignore`, `environment.yml`, and `requirements.txt`.
- [x] Add `README.md` and `docs/reference.md`.
- [x] Configure Kaggle CLI authentication.
- [x] Establish directory structure (`data/`, `notebooks/`, `src/`, `models/`, `docs/`).

---

## **Phase 2 — Data Understanding & Exploration (Nov 3–8)**

**Objectives:**
- Explore dataset characteristics, identify target distribution, and detect early data issues.

**Key Tasks:**
- [x] Load and inspect raw training and test datasets.
- [x] Summarize descriptive statistics and data types.
- [x] Visualize distributions, correlations, and feature relationships.
- [x] Document insights and plots in `notebooks/01_eda.ipynb`.

**Deliverable:**
- [x] EDA notebook + saved figures under `/figures/`.

---

## **Phase 3 — Data Cleaning & Preprocessing (Nov 9–12)**

**Objectives:**
- Transform raw data into a clean, validated, fully numeric format.

**Key Tasks:**
- [x] Handle missing values (N/A — dataset includes no nulls).
- [x] Split `grade_subgrade` into `grade` + `subgrade` and apply ordinal encoding.
- [x] One-Hot Encode categorical variables.
- [x] Scale numeric variables with StandardScaler:
  - `annual_income`
  - `debt_to_income_ratio`
  - `credit_score`
  - `loan_amount`
  - `interest_rate`
  - `grade`
  - `subgrade`
- [x] Verify train/test column alignment.
- [x] Export cleaned datasets to `/data/processed/`.

**Deliverable:**
- `loan_train_scaled.csv`  
- `loan_test_scaled.csv`

---

## **Phase 4 — Feature Engineering (Nov 13–15)**

**Objectives:**
- Enrich the dataset using domain knowledge and statistical transformations.

**Key Engineering Tasks:**
- [x] Loan-to-Income ratio
- [x] High DTI (debt-to-income) flag
- [x] Credit score buckets (very high, high, medium, low, very low)
- [x] Interaction terms (e.g., grade × loan_purpose)
- [x] Quantile transforms, binning
- [x] Validate correlations and feature impact
- [x] Export final feature-engineered dataset

**Deliverable:**
- `03_feature_engineering.ipynb`
- `loan_train_features.csv`, `loan_test_features.csv`

---

# ✅ Phase 5 — Model Development (Nov 16–23)

**Objective:**  
Develop, tune, validate, and finalize a production-grade loan repayment prediction model using engineered features. Ensure the entire pipeline is **reproducible**, **well-documented**, and **deployment-ready**.

---

## 🔧 Key Tasks

### **Model Training & Baselines**
- [x] Baseline Logistic Regression  
- [x] Random Forest  
- [x] Extra Trees Classifier  
- [ ] Support Vector Machine *(optional — skipped for compute constraints)*  
- [x] Gradient Boosting Models (XGBoost, LightGBM, CatBoost)

### **Model Optimization**
- [x] Hyperparameter tuning (Optuna)  
- [x] Evaluate models using ROC-AUC, PR-AUC, and F1-score  
- [x] Build and evaluate weighted model blending  
- [x] Threshold tuning to maximize F1  
- [x] Save best model + threshold metadata (joblib/json)

### **Model Validation & Reproducibility**
- [x] Add ROC Curve and PR Curve visualizations  
- [x] Add LightGBM feature importance plots  
- [x] Reproducibility test: load saved model + threshold and re-run metrics  
- [x] Validate Kaggle submission row count matches test set  
- [x] Confirm predictions remain identical after reload  
- [x] Final notebook cleanup (remove dead cells, warnings, stray prints)

### **Documentation**
- [x] Update `docs/project_plan.md` with final model results  
- [x] Add `docs/final_report.md` summarizing:
  - Best model  
  - Threshold selection  
  - Final metrics  
  - Feature importance  
  - Notes on blending and tuning  
- [x] Add `README_model_helper.md` (programmatic model loading)

---

## 📦 Final Deliverables
- Updated modeling notebook (`04_model_training.ipynb`)  
- Saved model artifacts under `/models/`:
  - `best_model.pkl`  
  - `threshold_metadata.json`  
  - Optional: `model_bundle.pkl`  
- Documentation under `docs/`, including `final_report.md`

---

## **Phase 6 — Validation, Submission & Documentation (Nov 23–28)**

**Objectives:**  
Validate model generalization, finalize predictions, create the Kaggle submission file, and document your methodology/results for portfolio use.

---

## **Key Tasks**

- [x] Validate model on hold-out or cross-validation folds  
- [x] Review metrics for overfitting / underfitting  
- [x] Finalize chosen model for competition submission  
- [x] Generate `submission.csv` in the exact Kaggle-required format  
- [x] Submit via Kaggle CLI and confirm the submission score  
- [x] Record the public leaderboard score  
- [ ] Update project README  
  - Method overview  
  - Final model choice  
  - Key metrics (train/validation/hold-out)  
  - Kaggle leaderboard result  
- [ ] Finalize summary sections in  
  - `04_model_training.ipynb`  
  - `05_interpretation_reporting.ipynb`

---

## **Deliverables**

- **Final Submission File:**  
  - `submission.csv`

- **Documentation Updates:**  
  - Updated README with results  
  - Completed interpretation/reporting notebook  
  - Final modeling summaries

---

## **Phase 7 — Review & Retrospective (Nov 29–30)**

**Objectives:**
- Reflect on modeling process, performance, and improvements.

**Key Tasks:**
- [ ] Record leaderboard score and ranking
- [ ] Summarize insights in `/docs/final_report.md`
- [ ] Note reproducibility or design improvements for future work

---

## ✅ **Milestones**

| Date (2025) | Milestone | Deliverable |
|-------------|-----------|-------------|
| Nov 3 | Environment setup complete | Repo initialized |
| Nov 8 | EDA completed | 01_eda.ipynb |
| Nov 12 | Preprocessing completed | Cleaned data |
| Nov 15 | Feature engineering completed | Engineered dataset |
| Nov 21 | Model training completed | 04_modeling.ipynb |
| Nov 28 | Submission ready | submission.csv |
| Nov 30 | Competition wrapped | final_report.md |

---

## **Optional Enhancements**
- Integrate MLflow or Weights & Biases for tracking.
- Add Dockerfile for reproducibility.
- Include Makefile for common workflows.
- Build a Streamlit dashboard for model interpretability.

---

**Author:** Brice Nelson  
**Last Updated:** November 15, 2025
