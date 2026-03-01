"""
Demo Script - See Auto EDA in Action!
Generates sample data and runs complete analysis
"""

import sys
sys.path.append('./src')

from eda_engine import AutoEDA
from advanced_eda import AdvancedEDA
import pandas as pd
import numpy as np

def generate_demo_data():
    """Generate comprehensive demo dataset"""
    np.random.seed(42)
    n = 2000
    
    data = {
        # Demographics
        'age': np.random.randint(18, 70, n),
        'gender': np.random.choice(['Male', 'Female', 'Other'], n, p=[0.48, 0.48, 0.04]),
        'city': np.random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata'], n),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n, p=[0.3, 0.4, 0.25, 0.05]),
        
        # Employment & Income
        'employment_type': np.random.choice(['Salaried', 'Self-Employed', 'Business'], n, p=[0.6, 0.3, 0.1]),
        'years_employed': np.random.randint(0, 30, n),
        'monthly_income': np.random.gamma(2, 25000, n),
        
        # Financial
        'credit_score': np.random.normal(680, 80, n).clip(300, 850).astype(int),
        'existing_loans': np.random.poisson(1.2, n),
        'total_debt': np.random.gamma(2, 50000, n),
        'savings': np.random.gamma(1.5, 30000, n),
        
        # Loan Details
        'loan_amount': np.random.gamma(3, 50000, n),
        'loan_term_months': np.random.choice([12, 24, 36, 48, 60], n),
        'interest_rate': np.random.uniform(8, 18, n),
        
        # Behavioral
        'previous_defaults': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'late_payments': np.random.poisson(0.5, n),
        'credit_inquiries': np.random.poisson(2, n),
    }
    
    df = pd.DataFrame(data)
    
    # Create target based on logic
    df['loan_approved'] = (
        (df['credit_score'] > 650) & 
        (df['monthly_income'] > 30000) & 
        (df['previous_defaults'] == 0) &
        (df['debt_to_income'] < 0.4)
    ).astype(int)
    
    # Add calculated feature
    df['debt_to_income'] = (df['total_debt'] / (df['monthly_income'] * 12)).clip(0, 2)
    
    # Add some missing values
    missing_cols = ['monthly_income', 'credit_score', 'savings']
    for col in missing_cols:
        df.loc[df.sample(frac=0.08).index, col] = np.nan
    
    # Add outliers
    df.loc[df.sample(n=30).index, 'monthly_income'] = np.random.uniform(200000, 500000, 30)
    df.loc[df.sample(n=20).index, 'loan_amount'] = np.random.uniform(500000, 1000000, 20)
    
    return df


def run_demo():
    """Run complete demo"""
    print("\n" + "🎬 "*40)
    print("🎬" + " "*20 + "AUTO EDA DEMO - STARTING!" + " "*37 + "🎬")
    print("🎬 "*40 + "\n")
    
    # Generate data
    print("📊 Generating demo dataset...")
    df = generate_demo_data()
    df.to_csv('examples/demo_loan_data.csv', index=False)
    print(f"✅ Dataset created: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"✅ Saved to: examples/demo_loan_data.csv\n")
    
    # Basic EDA
    print("\n" + "="*80)
    print("PART 1: BASIC EDA")
    print("="*80 + "\n")
    
    eda = AutoEDA(df, target_col='loan_approved')
    report = eda.run_complete_eda()
    
    # Save report
    eda.generate_report(save_path='outputs/demo_report.txt')
    
    # Advanced EDA
    print("\n" + "="*80)
    print("PART 2: ADVANCED EDA")
    print("="*80 + "\n")
    
    advanced = AdvancedEDA(df)
    
    # Data quality score
    quality_score = advanced.data_quality_score()
    
    # Top correlated features
    advanced.correlation_with_target('loan_approved', top_n=10)
    
    # Feature engineering suggestions
    advanced.feature_engineering_suggestions(df)
    
    print("\n" + "🎉 "*40)
    print("🎉" + " "*20 + "DEMO COMPLETE! CHECK OUTPUTS/" + " "*32 + "🎉")
    print("🎉 "*40 + "\n")
    
    print("📁 Generated Files:")
    print("   1. examples/demo_loan_data.csv - Sample dataset")
    print("   2. outputs/demo_report.txt - EDA report")
    print("\n")
    
    print("💡 Next Steps:")
    print("   1. Check the outputs/ folder for reports")
    print("   2. Open notebooks/tutorial.ipynb for detailed examples")
    print("   3. Try with your own data: python quick_eda.py your_data.csv")
    print("\n")


if __name__ == "__main__":
    run_demo()
