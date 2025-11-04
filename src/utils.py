"""
Utility functions for data analysis
"""

import pandas as pd
from pathlib import Path


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        DataFrame containing the data
        
    Example:
        >>> df = load_data('data/raw/sample.csv')
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    return pd.read_csv(filepath)


def save_data(df: pd.DataFrame, filepath: str) -> None:
    """
    Save DataFrame to a CSV file.
    
    Args:
        df: DataFrame to save
        filepath: Path where to save the CSV file
        
    Example:
        >>> save_data(df, 'data/processed/cleaned_data.csv')
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filepath, index=False)
