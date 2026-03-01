"""
Quick Start Script for Auto EDA
Run this with your dataset - Super Simple!
"""

import sys
sys.path.append('./src')

from eda_engine import AutoEDA
import pandas as pd

def quick_eda(filepath, target_column=None, separator=','):
    """
    One-line EDA for any dataset
    
    Parameters:
    -----------
    filepath : str
        Path to your dataset (CSV, Excel, etc.)
    target_column : str, optional
        Name of target column for ML tasks
    separator : str, default=','
        Separator for CSV files
    
    Example:
    --------
    >>> quick_eda('data.csv', target_column='price')
    >>> quick_eda('sales.xlsx', target_column='revenue')
    """
    
    print(f"📂 Loading dataset from: {filepath}")
    
    # Load data based on file type
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath, sep=separator)
    elif filepath.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(filepath)
    elif filepath.endswith('.json'):
        df = pd.read_json(filepath)
    elif filepath.endswith('.parquet'):
        df = pd.read_parquet(filepath)
    else:
        raise ValueError("Unsupported file format! Use CSV, Excel, JSON, or Parquet")
    
    print(f"✅ Dataset loaded successfully! Shape: {df.shape}\n")
    
    # Initialize and run EDA
    eda = AutoEDA(df, target_col=target_column)
    report = eda.run_complete_eda()
    
    # Generate report
    report_path = filepath.replace('.csv', '_eda_report.txt').replace('.xlsx', '_eda_report.txt')
    eda.generate_report(save_path=report_path)
    
    return eda, report


if __name__ == "__main__":
    """
    Usage from command line:
    python quick_eda.py <filepath> <target_column>
    
    Example:
    python quick_eda.py data/titanic.csv Survived
    """
    
    if len(sys.argv) < 2:
        print("❌ Usage: python quick_eda.py <filepath> [target_column]")
        print("\nExample:")
        print("  python quick_eda.py data/housing.csv price")
        sys.exit(1)
    
    filepath = sys.argv[1]
    target_col = sys.argv[2] if len(sys.argv) > 2 else None
    
    quick_eda(filepath, target_column=target_col)
