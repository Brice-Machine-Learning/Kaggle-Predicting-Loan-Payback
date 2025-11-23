# src/utils/ensure_directory.py
"""
Usage: Utility to ensure directory exists
"""


# ----------------------------------------------------
# Utility: ensure directories exist before saving files
# ----------------------------------------------------
from pathlib import Path

def ensure_dir(path: str | Path):
    """
    Create directory (and parents) if it does not exist.
    Safe to call repeatedly.
    """
    Path(path).mkdir(parents=True, exist_ok=True)
