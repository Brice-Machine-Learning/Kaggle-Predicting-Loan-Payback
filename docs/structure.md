## 🗂️ Project Structure

```plaintext
Kaggle-Predicting-Loan-Payback/
│
├── data/
│   ├── raw/                                    # Original Kaggle competition datasets
│   ├── processed/                              # Cleaned and feature-engineered datasets
│   └── external/                               # Supplementary datasets (if used)
│
├── notebooks/
│   ├── 01_eda.ipynb                            # Exploratory data analysis
│   ├── 02_data_cleaning.ipynb                  # Address missing values, inconsistent data, and outliers
│   ├── 03_feature_engineering.ipynb            # Create new features and derive ratios or flags
│   ├── 04_model_training.ipynb                 # Train baseline and tree-based models
│   ├── 05_model_evaluation.ipynb               # Evaluate model performance and tune hyperparameters
│   ├── 06_interpretation_reporting.ipynb       # Generate model interpretation reports and visualizations
│   └── 07_submission.ipynb                     # Generate final submission
│
├── figures/
│   ├── histograms/
│   ├── boxplots/
│   ├── countplots/
│   └── correlations/
│
├── src/
│   ├── __init__.py                             # initialization for src folder
│   ├── utils/                                  # Utility functions
│   │   ├── __init__.py                         # initialization of utils folder
│   │   └── visualization_utils.py              # Visualization function
│   ├── data_prep.py                            # Data loading and preprocessing scripts
│   ├── feature_engineering.py                  
│   ├── train_model.py
│   └── evaluate.py
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
├── environment.yml                             # Conda environment (optional)
├── kaggle.json                                 # API credentials (excluded from Git)
├── README.md
└── LICENSE
```