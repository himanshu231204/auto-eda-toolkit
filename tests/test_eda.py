"""
Test script for Auto EDA Toolkit
Tests the toolkit with synthetic data
"""

import sys
sys.path.append('./src')

from eda_engine import AutoEDA
import pandas as pd
import numpy as np

def create_sample_dataset():
    """Create a sample dataset for testing"""
    np.random.seed(42)
    
    n_samples = 1000
    
    data = {
        # Numerical features
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.normal(50000, 15000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'loan_amount': np.random.normal(200000, 50000, n_samples),
        
        # Categorical features
        'gender': np.random.choice(['Male', 'Female'], n_samples),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples),
        'employment': np.random.choice(['Employed', 'Self-Employed', 'Unemployed'], n_samples),
        'city': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'], n_samples),
        
        # Target variable (binary classification)
        'loan_approved': np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    df.loc[df.sample(frac=0.05).index, 'income'] = np.nan
    df.loc[df.sample(frac=0.03).index, 'credit_score'] = np.nan
    
    # Add some outliers
    df.loc[df.sample(n=20).index, 'income'] = np.random.uniform(200000, 500000, 20)
    
    return df


def test_classification():
    """Test with classification dataset"""
    print("\n" + "="*80)
    print("TEST 1: CLASSIFICATION TASK")
    print("="*80 + "\n")
    
    df = create_sample_dataset()
    df.to_csv('examples/sample_classification.csv', index=False)
    print("✅ Sample dataset created: examples/sample_classification.csv\n")
    
    eda = AutoEDA(df, target_col='loan_approved')
    report = eda.run_complete_eda()
    
    print("\n✅ Classification test completed successfully!\n")
    return report


def test_regression():
    """Test with regression dataset"""
    print("\n" + "="*80)
    print("TEST 2: REGRESSION TASK")
    print("="*80 + "\n")
    
    df = create_sample_dataset()
    df['house_price'] = (df['income'] * 4 + 
                         df['credit_score'] * 500 + 
                         np.random.normal(0, 50000, len(df)))
    
    df.to_csv('examples/sample_regression.csv', index=False)
    print("✅ Sample dataset created: examples/sample_regression.csv\n")
    
    eda = AutoEDA(df, target_col='house_price')
    report = eda.run_complete_eda()
    
    print("\n✅ Regression test completed successfully!\n")
    return report


def test_no_target():
    """Test without target variable"""
    print("\n" + "="*80)
    print("TEST 3: NO TARGET (EXPLORATORY ANALYSIS)")
    print("="*80 + "\n")
    
    df = create_sample_dataset()
    df.to_csv('examples/sample_exploratory.csv', index=False)
    print("✅ Sample dataset created: examples/sample_exploratory.csv\n")
    
    eda = AutoEDA(df)
    report = eda.run_complete_eda()
    
    print("\n✅ Exploratory analysis test completed successfully!\n")
    return report


if __name__ == "__main__":
    print("\n")
    print("🧪 " + "="*74 + " 🧪")
    print("🧪" + " "*20 + "AUTO EDA TOOLKIT - TEST SUITE" + " "*25 + "🧪")
    print("🧪 " + "="*74 + " 🧪")
    
    try:
        # Run all tests
        test_classification()
        test_regression()
        test_no_target()
        
        print("\n")
        print("✅ " + "="*74 + " ✅")
        print("✅" + " "*20 + "ALL TESTS PASSED!" + " "*35 + "✅")
        print("✅ " + "="*74 + " ✅")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}\n")
        raise
