# 🎯 AUTO EDA TOOLKIT - QUICK START


## 📦 What You Got:

```
auto-eda-toolkit/
│
├── 📄 README.md                  # Complete documentation
├── 📄 USAGE_GUIDE.md            # Detailed usage guide  
├── 📄 requirements.txt          # All dependencies
├── 📄 .gitignore               # Git ignore file
│
├── 🐍 quick_eda.py             # One-line EDA script
├── 🐍 demo.py                  # Demo with sample data
│
├── 📁 src/
│   ├── eda_engine.py           # Main EDA engine (CORE FILE)
│   ├── advanced_eda.py         # Advanced features
│   └── config.py               # Configuration settings
│
├── 📁 notebooks/
│   └── tutorial.ipynb          # Jupyter notebook tutorial
│
├── 📁 tests/
│   └── test_eda.py            # Testing suite
│
├── 📁 examples/               # Sample datasets (empty, fill with your data)
└── 📁 outputs/                # Generated reports & plots
```

---

## ⚡ 3 WAYS TO USE:

### 1️⃣ EASIEST - Command Line
```bash
python quick_eda.py your_data.csv target_column
```

### 2️⃣ SIMPLE - Python Script
```python
from src.eda_engine import AutoEDA
import pandas as pd

df = pd.read_csv('your_data.csv')
eda = AutoEDA(df, target_col='target')
eda.run_complete_eda()
```

### 3️⃣ DETAILED - Jupyter Notebook
Open `notebooks/tutorial.ipynb` and follow examples!

---

## 🚀 GET STARTED IN 3 STEPS:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Try the Demo
```bash
python demo.py
```

### Step 3: Use Your Data
```bash
python quick_eda.py path/to/your/data.csv your_target_column
```

---

## ✨ KEY FEATURES:

✅ **Automatic Column Type Detection**
   - Numerical, Categorical, DateTime

✅ **Complete Missing Value Analysis**
   - Counts, percentages, visualizations

✅ **Numerical Analysis**
   - Distributions, correlations, outliers
   - Box plots, histograms, heatmaps

✅ **Categorical Analysis**
   - Value counts, frequencies
   - Bar charts for distributions

✅ **Outlier Detection**
   - IQR method with bounds

✅ **Target Variable Analysis**
   - Classification: class balance
   - Regression: distribution analysis

✅ **Feature-Target Relationships**
   - Automatic correlation analysis
   - Visual relationships

✅ **Report Generation**
   - Text reports with all findings

✅ **Advanced Features**
   - Time series analysis
   - Text analysis
   - Data quality scoring
   - Feature engineering suggestions

---

## 📊 WHAT IT COVERS (90-95% of EDA):

### Basic Analysis:
- Dataset shape, size, types
- Memory usage
- First/last rows
- Duplicate detection

### Quality Checks:
- Missing values (count, %, visualization)
- Data type validation
- Duplicate rows

### Statistical Analysis:
- Mean, median, mode, std
- Quartiles, min, max
- Skewness, kurtosis

### Visualizations:
- Distribution plots (histograms)
- Box plots (outlier detection)
- Correlation heatmaps
- Category bar charts
- Feature-target relationships

### Advanced:
- Time series patterns
- Text length analysis
- Feature engineering tips
- Data quality score

---

## 💡 EXAMPLES:

### Example 1: E-commerce Data
```python
df = pd.read_csv('sales_data.csv')
eda = AutoEDA(df, target_col='revenue')
eda.run_complete_eda()
```

### Example 2: Customer Churn
```python
df = pd.read_csv('customers.csv')
eda = AutoEDA(df, target_col='churn')
eda.run_complete_eda()
eda.generate_report('outputs/churn_report.txt')
```

### Example 3: House Prices
```python
df = pd.read_csv('housing.csv')
eda = AutoEDA(df, target_col='price')
eda.run_complete_eda()
```

---

## 🎯 NEXT STEPS:

1. **Install**: `pip install -r requirements.txt`
2. **Demo**: `python demo.py`
3. **Your Data**: `python quick_eda.py your_file.csv`
4. **Learn**: Open `notebooks/tutorial.ipynb`
5. **Customize**: Edit `src/config.py`
6. **Advanced**: Use `src/advanced_eda.py`

---

## 🔧 CUSTOMIZATION:

Edit `src/config.py` to change:
- Plot styles and colors
- Statistical thresholds
- Categorical limits
- Figure sizes
- And much more!

---

## 📚 FILES YOU NEED TO KNOW:

1. **src/eda_engine.py** - Main EDA logic (90% of work happens here)
2. **quick_eda.py** - Quick start script
3. **src/config.py** - All settings
4. **notebooks/tutorial.ipynb** - Learn by examples

---

## 🎓 TIPS FOR SUCCESS:

1. **Large Datasets?** Sample first:
   ```python
   df_sample = df.sample(n=10000, random_state=42)
   ```

2. **Save Everything:**
   ```python
   eda.generate_report('my_analysis.txt')
   ```

3. **Step by Step:**
   Run specific analyses instead of all at once

4. **Customize:**
   Modify settings in config.py for your needs

---

## ⚠️ TROUBLESHOOTING:

**Issue**: Module not found
**Fix**: `pip install -r requirements.txt`

**Issue**: Memory error
**Fix**: Sample your data first

**Issue**: Too many categories
**Fix**: Keep only top N categories

**Issue**: Plots not showing
**Fix**: Use `%matplotlib inline` in Jupyter

---

## 📞 SUPPORT:

- Check `USAGE_GUIDE.md` for detailed help
- Open `notebooks/tutorial.ipynb` for examples
- Review `README.md` for full documentation

---



**Start with:**
```bash
python demo.py
```

---

**Happy Analyzing! 🚀📊**

*Created with ❤️ for data scientists who hate repetitive EDA!*
