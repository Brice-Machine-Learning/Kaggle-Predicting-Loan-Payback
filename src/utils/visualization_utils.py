"""src/utils/visualization_utils.py"""

"""
===============================================================================
Module:         visualization_utils.py
Project:        Kaggle - Predict Loan Payback
Author:         Brice Nelson
Organization:   Kaggle Series | Brice Machine Learning Projects
Created:        2025-11-02
Last Updated:   2025-11-02
===============================================================================

Purpose:
--------
This module provides reusable visualization utilities for the Kaggle
"Predict Loan Payback" project. It standardizes plot styling and formatting
across all project notebooks, ensuring consistent, professional-quality figures.

Functions:
-----------
1. plot_categorical_distribution(dataframe, column, figsize, style, palette)
    Generates a standardized count plot for categorical features with
    consistent Seaborn styling and formatting.

Usage:
------
from src.utils.visualization_utils import plot_categorical_distribution

plot_categorical_distribution(loan_train_df, "gender")
===============================================================================
"""


import seaborn as sns
import matplotlib.pyplot as plt

def plot_categorical_distribution(dataframe, column, figsize=(8, 4), style="whitegrid", palette="pastel"):
    """
    Create a count plot for a categorical column with consistent styling.

    Parameters
    ----------
    dataframe : pd.DataFrame
        The dataframe containing the data
    column : str
        The name of the categorical column to plot
    figsize : tuple, optional
        Figure size (width, height)
    style : str, optional
        Seaborn style preset
    palette : str, optional
        Seaborn color palette
    """
    sns.set_theme(style=style, palette=palette)
    plt.figure(figsize=figsize)

    order = dataframe[column].value_counts().index
    sns.countplot(data=dataframe, x=column, order=order)

    plt.title(f"Distribution of {column}", fontsize=14, fontweight="bold")
    plt.xlabel(column.replace("_", " ").title())
    plt.ylabel("Count")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
