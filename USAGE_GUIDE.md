# 🚀 Auto EDA Toolkit - Complete Usage Guide


## 📚 Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [Customization](#customization)
6. [Troubleshooting](#troubleshooting)
7. [Best Practices](#best-practices)

---

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/himanshu231204/auto-eda-toolkit.git
cd auto-eda-toolkit
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

### Method 1: Command Line (Easiest!)

```bash
# Basic usage
python quick_eda.py data/your_file.csv

# With target column
python quick_eda.py data/your_file.csv target_column_name

# Excel file
python quick_eda.py data/your_file.xlsx price
```

### Method 2: Python Script

```python
from src.eda_engine import AutoEDA
import pandas as pd

# Load data
df = pd.read_csv('your_data.csv')

# One line EDA!
eda = AutoEDA(df, target_col='target')
eda.run_complete_eda()
```

### Method 3: Demo

```bash
# Run demo with sample data
python demo.py
```

---

## 📊 Basic Usage

### 1. Without Target Variable (Exploratory)

```python
import pandas as pd
from src.eda_engine import AutoEDA

# Load your data
df = pd.read_csv('sales_data.csv')

# Initialize
eda = AutoEDA(df)

# Run complete EDA
eda.run_complete_eda()
```

**Use Case**: General data exploration, understanding dataset

---

### 2. With Target Variable (Classification)

```python
# Load data
df = pd.read_csv('customer_churn.csv')

# Specify target
eda = AutoEDA(df, target_col='churn')

# Run analysis
eda.run_complete_eda()

# Save report
eda.generate_report('outputs/churn_analysis.txt')
```

**Use Case**: Binary/Multi-class classification problems

---

### 3. With Target Variable (Regression)

```python
# Load data
df = pd.read_csv('house_prices.csv')

# Specify target
eda = AutoEDA(df, target_col='price')

# Run analysis
eda.run_complete_eda()
```

**Use Case**: Predicting continuous values

---

## 🎯 Advanced Usage

### 1. Step-by-Step Analysis

```python
from src.eda_engine import AutoEDA
import pandas as pd

df = pd.read_csv('data.csv')
eda = AutoEDA(df, target_col='target')

# Run specific analyses
eda.identify_column_types()      # Column type detection
eda.basic_info()                 # Dataset overview
eda.missing_value_analysis()     # Missing values
eda.numerical_analysis()         # Numerical columns
eda.categorical_analysis()       # Categorical columns
eda.outlier_detection()          # Outlier detection
eda.target_analysis()            # Target variable
eda.feature_target_relationship() # Feature-target relations
```

---

### 2. Advanced Features

```python
from src.advanced_eda import AdvancedEDA

# Initialize advanced EDA
advanced = AdvancedEDA(df)

# Time series analysis
advanced.time_series_analysis(
    date_col='date', 
    value_col='sales'
)

# Text analysis
advanced.text_column_analysis(text_col='reviews')

# Top correlated features
advanced.correlation_with_target('price', top_n=15)

# Feature engineering suggestions
advanced.feature_engineering_suggestions(df)

# Data quality score
quality = advanced.data_quality_score()
```

---

### 3. Multiple Datasets

```python
# Compare multiple datasets
datasets = {
    'Train': pd.read_csv('train.csv'),
    'Test': pd.read_csv('test.csv'),
    'Validation': pd.read_csv('val.csv')
}

for name, df in datasets.items():
    print(f"\n{'='*80}")
    print(f"Analyzing: {name}")
    print('='*80)
    
    eda = AutoEDA(df, target_col='target')
    eda.run_complete_eda()
```

---

## ⚙️ Customization

### 1. Modify Configuration

Edit `src/config.py`:

```python
# Change categorical threshold
CATEGORICAL_THRESHOLD = 15  # Default: 10

# Change plot style
PLOT_STYLE = 'darkgrid'  # Options: whitegrid, dark, white

# Change figure size
FIGURE_SIZE = (15, 8)  # Default: (12, 6)

# Change correlation threshold
CORRELATION_THRESHOLD = 0.8  # Default: 0.7
```

---

### 2. Custom Plotting

```python
# After running EDA, customize plots
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")
plt.rcParams['figure.figsize'] = (20, 10)

# Now run your analysis
eda.numerical_analysis()
```

---

### 3. Selective Column Analysis

```python
# Analyze only specific columns
numerical_subset = ['age', 'income', 'credit_score']
categorical_subset = ['gender', 'city']

# Temporarily modify
eda.numerical_cols = numerical_subset
eda.categorical_cols = categorical_subset

eda.numerical_analysis()
eda.categorical_analysis()
```

---

## 🔍 File Type Support

### CSV Files

```python
# Basic CSV
df = pd.read_csv('data.csv')

# With custom separator
df = pd.read_csv('data.csv', sep=';')

# With encoding
df = pd.read_csv('data.csv', encoding='latin-1')
```

### Excel Files

```python
# Single sheet
df = pd.read_excel('data.xlsx')

# Specific sheet
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Multiple sheets
sheets = pd.read_excel('data.xlsx', sheet_name=None)
```

### JSON Files

```python
df = pd.read_json('data.json')
```

### Parquet Files

```python
df = pd.read_parquet('data.parquet')
```

---

## 🐛 Troubleshooting

### Issue 1: Import Error

**Error**: `ModuleNotFoundError: No module named 'seaborn'`

**Solution**:
```bash
pip install -r requirements.txt
```

---

### Issue 2: Memory Error (Large Dataset)

**Error**: `MemoryError`

**Solution**:
```python
# Sample your data
df_sample = df.sample(n=50000, random_state=42)
eda = AutoEDA(df_sample, target_col='target')
```

---

### Issue 3: Too Many Categories

**Error**: Plot too crowded

**Solution**:
```python
# Filter top N categories before analysis
for col in categorical_cols:
    top_categories = df[col].value_counts().head(15).index
    df[col] = df[col].where(df[col].isin(top_categories), 'Other')
```

---

### Issue 4: Matplotlib Display Issues

**Error**: Plots not showing

**Solution**:
```python
import matplotlib.pyplot as plt
plt.ion()  # Turn on interactive mode

# Or in Jupyter
%matplotlib inline
```

---

## 💡 Best Practices

### 1. Data Loading

```python
# GOOD: Check data first
df = pd.read_csv('data.csv')
print(f"Shape: {df.shape}")
print(f"Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Then run EDA
eda = AutoEDA(df)
```

---

### 2. Large Datasets

```python
# Sample first
if len(df) > 100000:
    df_sample = df.sample(n=50000, random_state=42)
    eda = AutoEDA(df_sample)
else:
    eda = AutoEDA(df)
```

---

### 3. Save Your Work

```python
# Always save reports
eda.run_complete_eda()
eda.generate_report('outputs/my_analysis.txt')

# Save specific plots
plt.savefig('outputs/plots/correlation_matrix.png', dpi=300, bbox_inches='tight')
```

---

### 4. Iterative Analysis

```python
# First pass: Quick overview
eda = AutoEDA(df)
eda.basic_info()
eda.identify_column_types()

# Second pass: Deep dive
eda.numerical_analysis()
eda.categorical_analysis()

# Third pass: Advanced
from src.advanced_eda import AdvancedEDA
advanced = AdvancedEDA(df)
advanced.feature_engineering_suggestions(df)
```

---

### 5. Documentation

```python
# Document your findings
findings = """
# EDA Findings for Dataset X

## Key Insights:
1. Missing values in 'income' column (8%)
2. High correlation between 'age' and 'experience' (0.85)
3. Class imbalance: 70-30 split
4. Outliers detected in 'price' column (5% of data)

## Recommendations:
1. Impute missing income with median
2. Consider dropping one of age/experience
3. Use SMOTE for class balancing
4. Cap outliers at 99th percentile
"""

with open('outputs/findings.md', 'w') as f:
    f.write(findings)
```

---

## 🎓 Learning Resources

### Understanding Your Output

1. **Correlation Matrix**: 
   - Values close to 1/-1 = strong relationship
   - Values close to 0 = no relationship

2. **Box Plots**: 
   - Points outside whiskers = outliers
   - Box shows 25th to 75th percentile

3. **Distribution Plots**: 
   - Bell curve = normal distribution
   - Skewed left/right = transformation needed

4. **Missing Value Analysis**: 
   - >5% missing = imputation needed
   - >50% missing = consider dropping column

---

## 📞 Support

**Found a bug?** Open an issue on GitHub

**Need a feature?** Submit a pull request

**Questions?** Check the tutorial notebook: `notebooks/tutorial.ipynb`

---

## ✅ Checklist Before Running EDA

- [ ] Data loaded successfully
- [ ] Checked basic info (shape, columns)
- [ ] Identified target column (if applicable)
- [ ] Created output directory
- [ ] Virtual environment activated
- [ ] Dependencies installed

---

## 🚀 Quick Reference

```python
# Essential Commands
from src.eda_engine import AutoEDA
import pandas as pd

# 1. Load & Analyze
df = pd.read_csv('data.csv')
eda = AutoEDA(df, target_col='target')
eda.run_complete_eda()

# 2. Save Report
eda.generate_report('output.txt')

# 3. Advanced Analysis
from src.advanced_eda import AdvancedEDA
advanced = AdvancedEDA(df)
advanced.data_quality_score()
```

---

**Happy Analyzing! 🎉**

*Last Updated: March 2026*
