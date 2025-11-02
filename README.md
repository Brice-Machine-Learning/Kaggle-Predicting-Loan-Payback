# 🧮 Kaggle – Predicting Loan Payback

<p align="center">
  <img src="https://img.shields.io/badge/Competition-Nov%201%20→%20Nov%2030%2C%202025-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square">
  <img src="https://img.shields.io/badge/Focus-Machine%20Learning%20%7C%20Finance-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/Evaluation-ROC--AUC-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Platform-Kaggle-lightgrey?style=flat-square&logo=kaggle">
</p>

---

> **Competition:** [Predict Loan Payback](https://www.kaggle.com/competitions/predict-loan-payback)  
> **Duration:** November 1 → November 30, 2025  
> **Goal:** Predict the probability that a loan will be repaid in full.


**Competition Window:** November 1, 2025 → November 30, 2025  
**Competition Type:** Supervised Machine Learning (Binary Classification)  
**Primary Goal:** Predict the likelihood that a loan will be paid back in full based on applicant and loan features.

---

## 📘 Overview

This repository contains my work for the **Kaggle "Predict Loan Payback"** competition.  
The objective is to build and evaluate machine learning models that estimate the probability a loan applicant will repay their loan, helping financial institutions make informed lending decisions.

The project focuses on:
- Exploratory data analysis (EDA)
- Feature engineering and selection
- Model training and hyperparameter tuning
- Evaluation and leaderboard submission

---

## 🧠 Problem Definition

**Task:**  
Given a dataset of loan applicants, predict whether each loan will be **paid back (1)** or **default (0)**.

**Target Variable:**  
`loan_paid_back` → 1 = Yes, 0 = No

**Input Data:**  
A combination of numerical, categorical, and potentially time-based features such as:
- Applicant income
- Credit score
- Loan amount and duration
- Employment type
- Age, gender, and marital status
- Debt-to-income ratio, etc.

---

## 🗂️ Project Structure

```plaintext
Kaggle-Predicting-Loan-Payback/
│
├── data/
│   ├── raw/ # Original Kaggle competition datasets
│   ├── processed/ # Cleaned and feature-engineered datasets
│   └── external/ # Supplementary datasets (if used)
│
├── notebooks/
│   ├── 01_eda.ipynb # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
│   └── 05_submission.ipynb
│
├── src/
│   ├── data_prep.py # Data loading and preprocessing scripts
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/
│   ├── baseline_model.pkl
│   └── tuned_model.pkl
│
├── submissions/
│   ├── submission_01.csv
│   └── submission_02_tuned.csv
│
├── requirements.txt
├── environment.yml # Conda environment (optional)
├── kaggle.json # API credentials (excluded from Git)
├── README.md
└── LICENSE
```


---

## ⚙️ Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Language** | Python 3.11+ |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn, plotly |
| **Modeling** | scikit-learn, XGBoost, LightGBM |
| **Evaluation** | ROC-AUC, F1-score, Precision/Recall |
| **Environment** | Conda / Kaggle Notebooks |

---

## 🧩 Methodology

1. **Data Exploration**
   - Visualize distributions, missing values, and correlations.
   - Identify potential data leakage or imbalance.

2. **Data Cleaning & Feature Engineering**
   - Handle missing values, encode categorical features.
   - Create derived ratios or flags (e.g., DTI ratio, credit-to-loan amount).

3. **Model Development**
   - Start with baseline models (Logistic Regression, Random Forest).
   - Progress to ensemble methods (XGBoost, LightGBM, CatBoost).
   - Apply cross-validation for robustness.

4. **Evaluation**
   - Use stratified splits to preserve class balance.
   - Optimize ROC-AUC and F1-score.

5. **Submission**
   - Generate predictions for the test set.
   - Submit `.csv` via Kaggle API.

---

## 🏁 Current Progress

| Date | Stage | Notes |
|------|--------|-------|
| Nov 1, 2025 | ✅ Setup | Repo initialized, data downloaded |
| Nov 3–7, 2025 | 🚧 EDA | Feature insights and correlations |
| Nov 8–15, 2025 | 🧱 Modeling | Baseline and tree-based models |
| Nov 16–25, 2025 | ⚙️ Tuning | Grid/Optuna search for hyperparameters |
| Nov 26–30, 2025 | 🏆 Submission | Final submission and leaderboard review |

---

## 🧾 Evaluation Metric

**Primary metric:**  
> *ROC-AUC (Receiver Operating Characteristic - Area Under Curve)*  

Secondary metrics may include:
- F1-score
- Precision / Recall
- Log Loss

---

## 📤 Submissions

Each `.csv` file in `/submissions` follows Kaggle’s format:

| id | loan_paid_back |
|----|----------------|
| 1  | 0.84 |
| 2  | 0.32 |
| 3  | 0.91 |

---

## 📌 Future Enhancements

- Introduce feature selection with SHAP or permutation importance  
- Implement stacked or blended ensemble models  
- Automate training pipeline with MLflow or Prefect  
- Deploy best model via FastAPI endpoint or Streamlit dashboard  

---

## 📚 References

- [Kaggle Competition Page](https://www.kaggle.com/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)

---

## 🧑‍💻 Author

**Brice**  
Backend Developer & ML Engineer (Transitioning from Civil Engineering)  
🌐 [Portfolio](https://www.devbybrice.com)  
📬 [Email](brice@devbybrice.com)

---

## 📚 Citation

This project uses data from the Kaggle competition:

> Yao Yan, Walter Reade, Elizabeth Park. *Predicting Loan Payback.*  
> Kaggle, 2025. [https://www.kaggle.com/competitions/playground-series-s5e11](https://www.kaggle.com/competitions/playground-series-s5e11)

If you use or reference this work, please cite the dataset as:

```bibtex
@misc{playground-series-s5e11,
    author = {Yao Yan, Walter Reade, Elizabeth Park},
    title = {Predicting Loan Payback},
    year = {2025},
    howpublished = {\url{https://kaggle.com/competitions/playground-series-s5e11}},
    note = {Kaggle}
}
```