# 🚀 Auto EDA Toolkit

**90-95% EDA Automation for ANY Dataset**


[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

✅ **Automatic Column Type Detection** - Numerical, Categorical, DateTime  
✅ **Missing Value Analysis** - Complete visualization & statistics  
✅ **Numerical Analysis** - Distributions, correlations, outliers  
✅ **Categorical Analysis** - Value counts, top categories  
✅ **Outlier Detection** - IQR method with visualization  
✅ **Target Variable Analysis** - Classification & Regression support  
✅ **Feature-Target Relationships** - Automatic visualization  
✅ **Report Generation** - Save comprehensive EDA reports  
✅ **One-Line Usage** - Super simple interface  

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/auto-eda-toolkit.git
cd auto-eda-toolkit

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

### Method 1: One-Line Command (Easiest!)

```bash
python quick_eda.py data/your_dataset.csv target_column
```

### Method 2: Python Script

```python
from src.eda_engine import AutoEDA
import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Run complete EDA - That's it!
eda = AutoEDA(df, target_col='your_target')
report = eda.run_complete_eda()
```

### Method 3: Jupyter Notebook

Check `notebooks/tutorial.ipynb` for detailed examples!

## 📊 What You Get

### 1. **Basic Information**
- Dataset shape & size
- Memory usage
- Data types
- Duplicate detection

### 2. **Column Analysis**
- Automatic type detection
- Statistical summaries
- Distribution plots

### 3. **Missing Values**
- Count & percentage
- Visual heatmap
- Column-wise breakdown

### 4. **Numerical Features**
- Descriptive statistics
- Distribution histograms
- Box plots for outliers
- Correlation matrix
- Skewness & kurtosis

### 5. **Categorical Features**
- Unique value counts
- Top categories
- Distribution bar charts

### 6. **Outlier Detection**
- IQR method
- Count & percentage
- Upper/lower bounds

### 7. **Target Analysis**
- Classification: class imbalance
- Regression: distribution
- Feature-target relationships

## 💡 Usage Examples

### Example 1: Basic EDA (No Target)

```python
import pandas as pd
from src.eda_engine import AutoEDA

df = pd.read_csv('data.csv')
eda = AutoEDA(df)
eda.run_complete_eda()
```

### Example 2: Classification Task

```python
df = pd.read_csv('classification_data.csv')
eda = AutoEDA(df, target_col='target')
eda.run_complete_eda()

# Save report
eda.generate_report(save_path='eda_report.txt')
```

### Example 3: Regression Task

```python
df = pd.read_csv('house_prices.csv')
eda = AutoEDA(df, target_col='price')
eda.run_complete_eda()
```

### Example 4: Step-by-Step Analysis

```python
eda = AutoEDA(df, target_col='target')

# Run specific analyses
eda.identify_column_types()
eda.basic_info()
eda.missing_value_analysis()
eda.numerical_analysis()
eda.categorical_analysis()
eda.outlier_detection()
eda.target_analysis()
eda.feature_target_relationship()
```

## 📁 Project Structure

```
auto-eda-toolkit/
│
├── src/
│   └── eda_engine.py          # Main EDA engine
│
├── notebooks/
│   └── tutorial.ipynb         # Detailed tutorial
│
├── examples/
│   └── sample_datasets/       # Example datasets
│
├── outputs/
│   └── reports/               # Generated reports
│
├── tests/
│   └── test_eda.py           # Unit tests
│
├── quick_eda.py              # Quick start script
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🔧 Requirements

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
scikit-learn>=0.24.0
```

## 🎯 Supported File Formats

- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)
- JSON (`.json`)
- Parquet (`.parquet`)

## 📈 What This Covers (90-95% of EDA)

### ✅ Data Understanding
- Shape, size, types
- Memory usage
- First/last rows

### ✅ Data Quality
- Missing values
- Duplicates
- Data types validation

### ✅ Univariate Analysis
- Numerical distributions
- Categorical frequencies
- Statistical measures

### ✅ Bivariate Analysis
- Correlations
- Feature-target relationships
- Group comparisons

### ✅ Multivariate Analysis
- Correlation matrices
- Feature interactions

### ✅ Outlier Detection
- IQR method
- Visual identification

### ✅ Target Analysis
- Distribution
- Class balance
- Relationship with features

## 🎨 Customization

You can customize the toolkit by modifying `src/eda_engine.py`:

```python
# Change categorical threshold
if self.df[col].nunique() < 10:  # Change this number
    self.categorical_cols.append(col)

# Modify plot styles
sns.set_style("darkgrid")  # Change style
plt.rcParams['figure.figsize'] = (15, 8)  # Change size
```

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📝 License

MIT License - feel free to use in your projects!

## 🙏 Credits

Created with ❤️ for data scientists who want to focus on modeling, not repetitive EDA!

## 📞 Support

Have questions? Open an issue or reach out!

---

## 🎓 Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [EDA Best Practices](https://towardsdatascience.com)

---

**Happy Analyzing! 🚀**

*Remember: This toolkit handles 90-95% of standard EDA. For domain-specific analysis, you may need custom code!*
