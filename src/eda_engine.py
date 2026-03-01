"""
Auto EDA Toolkit - Complete EDA Automation Engine
Handles 90-95% of EDA process for any dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

class AutoEDA:
    """
    Comprehensive EDA automation class for any dataset
    """
    
    def __init__(self, df, target_col=None):
        """
        Initialize with dataset
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataset
        target_col : str, optional
            Target column for supervised learning tasks
        """
        self.df = df.copy()
        self.target_col = target_col
        self.numerical_cols = []
        self.categorical_cols = []
        self.datetime_cols = []
        self.report = {}
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 6)
        
    def identify_column_types(self):
        """Automatically identify column types"""
        print("=" * 80)
        print("🔍 IDENTIFYING COLUMN TYPES")
        print("=" * 80)
        
        for col in self.df.columns:
            # Check for datetime
            if pd.api.types.is_datetime64_any_dtype(self.df[col]):
                self.datetime_cols.append(col)
            # Check for numerical
            elif pd.api.types.is_numeric_dtype(self.df[col]):
                # If unique values < 10 and integers, treat as categorical
                if self.df[col].nunique() < 10 and self.df[col].dtype in ['int64', 'int32']:
                    self.categorical_cols.append(col)
                else:
                    self.numerical_cols.append(col)
            # Everything else is categorical
            else:
                self.categorical_cols.append(col)
        
        print(f"✅ Numerical Columns ({len(self.numerical_cols)}): {self.numerical_cols}")
        print(f"✅ Categorical Columns ({len(self.categorical_cols)}): {self.categorical_cols}")
        print(f"✅ DateTime Columns ({len(self.datetime_cols)}): {self.datetime_cols}")
        print("\n")
        
        self.report['column_types'] = {
            'numerical': self.numerical_cols,
            'categorical': self.categorical_cols,
            'datetime': self.datetime_cols
        }
        
    def basic_info(self):
        """Display basic dataset information"""
        print("=" * 80)
        print("📊 BASIC DATASET INFORMATION")
        print("=" * 80)
        
        info = {
            'shape': self.df.shape,
            'rows': self.df.shape[0],
            'columns': self.df.shape[1],
            'memory_usage': f"{self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB",
            'duplicates': self.df.duplicated().sum()
        }
        
        print(f"📏 Shape: {info['shape']}")
        print(f"📈 Total Rows: {info['rows']:,}")
        print(f"📊 Total Columns: {info['columns']}")
        print(f"💾 Memory Usage: {info['memory_usage']}")
        print(f"🔄 Duplicate Rows: {info['duplicates']:,}")
        print("\n")
        
        # Display first few rows
        print("📋 First 5 Rows:")
        print(self.df.head())
        print("\n")
        
        # Data types
        print("📝 Data Types:")
        print(self.df.dtypes)
        print("\n")
        
        self.report['basic_info'] = info
        
    def missing_value_analysis(self):
        """Comprehensive missing value analysis"""
        print("=" * 80)
        print("🔍 MISSING VALUE ANALYSIS")
        print("=" * 80)
        
        missing = self.df.isnull().sum()
        missing_pct = (missing / len(self.df)) * 100
        
        missing_df = pd.DataFrame({
            'Column': missing.index,
            'Missing_Count': missing.values,
            'Missing_Percentage': missing_pct.values
        }).sort_values('Missing_Count', ascending=False)
        
        cols_with_missing = missing_df[missing_df['Missing_Count'] > 0]
        
        if len(cols_with_missing) > 0:
            print(f"⚠️  {len(cols_with_missing)} columns have missing values:\n")
            print(cols_with_missing.to_string(index=False))
            
            # Visualization
            if len(cols_with_missing) > 0:
                plt.figure(figsize=(12, max(6, len(cols_with_missing) * 0.3)))
                sns.barplot(data=cols_with_missing.head(20), y='Column', x='Missing_Percentage')
                plt.title('Missing Values by Column (Top 20)', fontsize=14, fontweight='bold')
                plt.xlabel('Missing Percentage (%)')
                plt.tight_layout()
                plt.show()
        else:
            print("✅ No missing values found!")
        
        print("\n")
        self.report['missing_values'] = cols_with_missing.to_dict('records')
        
    def numerical_analysis(self):
        """Comprehensive numerical column analysis"""
        if len(self.numerical_cols) == 0:
            print("⚠️  No numerical columns found!\n")
            return
            
        print("=" * 80)
        print("📊 NUMERICAL ANALYSIS")
        print("=" * 80)
        
        # Statistical summary
        print("📈 Statistical Summary:")
        summary = self.df[self.numerical_cols].describe().T
        summary['skewness'] = self.df[self.numerical_cols].skew()
        summary['kurtosis'] = self.df[self.numerical_cols].kurtosis()
        print(summary)
        print("\n")
        
        # Distribution plots
        n_cols = len(self.numerical_cols)
        n_rows = (n_cols + 2) // 3
        
        fig, axes = plt.subplots(n_rows, 3, figsize=(15, n_rows * 4))
        axes = axes.flatten() if n_cols > 1 else [axes]
        
        for idx, col in enumerate(self.numerical_cols):
            if idx < len(axes):
                # Histogram with KDE
                self.df[col].hist(bins=30, ax=axes[idx], alpha=0.7, edgecolor='black')
                axes[idx].set_title(f'Distribution: {col}', fontweight='bold')
                axes[idx].set_xlabel(col)
                axes[idx].set_ylabel('Frequency')
                
                # Add stats text
                mean_val = self.df[col].mean()
                median_val = self.df[col].median()
                axes[idx].axvline(mean_val, color='red', linestyle='--', label=f'Mean: {mean_val:.2f}')
                axes[idx].axvline(median_val, color='green', linestyle='--', label=f'Median: {median_val:.2f}')
                axes[idx].legend()
        
        # Hide extra subplots
        for idx in range(n_cols, len(axes)):
            axes[idx].axis('off')
            
        plt.tight_layout()
        plt.show()
        
        # Box plots for outlier detection
        if n_cols > 0:
            fig, axes = plt.subplots(n_rows, 3, figsize=(15, n_rows * 4))
            axes = axes.flatten() if n_cols > 1 else [axes]
            
            for idx, col in enumerate(self.numerical_cols):
                if idx < len(axes):
                    sns.boxplot(y=self.df[col], ax=axes[idx], color='skyblue')
                    axes[idx].set_title(f'Boxplot: {col}', fontweight='bold')
                    
            for idx in range(n_cols, len(axes)):
                axes[idx].axis('off')
                
            plt.tight_layout()
            plt.show()
        
        # Correlation heatmap
        if len(self.numerical_cols) > 1:
            print("🔗 Correlation Matrix:")
            corr = self.df[self.numerical_cols].corr()
            
            plt.figure(figsize=(12, 10))
            mask = np.triu(np.ones_like(corr, dtype=bool))
            sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', center=0,
                       square=True, linewidths=1, cbar_kws={"shrink": 0.8}, fmt='.2f')
            plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.show()
            
            # High correlations
            high_corr = []
            for i in range(len(corr.columns)):
                for j in range(i+1, len(corr.columns)):
                    if abs(corr.iloc[i, j]) > 0.7:
                        high_corr.append({
                            'Feature1': corr.columns[i],
                            'Feature2': corr.columns[j],
                            'Correlation': corr.iloc[i, j]
                        })
            
            if high_corr:
                print("\n⚠️  High Correlations (>0.7):")
                print(pd.DataFrame(high_corr).to_string(index=False))
        
        print("\n")
        self.report['numerical_summary'] = summary.to_dict()
        
    def categorical_analysis(self):
        """Comprehensive categorical column analysis"""
        if len(self.categorical_cols) == 0:
            print("⚠️  No categorical columns found!\n")
            return
            
        print("=" * 80)
        print("📋 CATEGORICAL ANALYSIS")
        print("=" * 80)
        
        for col in self.categorical_cols:
            print(f"\n📌 Column: {col}")
            print(f"   Unique Values: {self.df[col].nunique()}")
            print(f"   Most Frequent: {self.df[col].mode()[0] if len(self.df[col].mode()) > 0 else 'N/A'}")
            
            # Value counts
            value_counts = self.df[col].value_counts()
            print(f"\n   Top 10 Values:")
            print(value_counts.head(10).to_string())
            
            # Visualization for columns with reasonable unique values
            if self.df[col].nunique() <= 20:
                plt.figure(figsize=(12, 6))
                value_counts.head(20).plot(kind='bar', color='skyblue', edgecolor='black')
                plt.title(f'Distribution: {col}', fontsize=14, fontweight='bold')
                plt.xlabel(col)
                plt.ylabel('Count')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                plt.show()
            else:
                print(f"   ⚠️  Too many unique values ({self.df[col].nunique()}) to visualize")
        
        print("\n")
        
    def outlier_detection(self):
        """Detect outliers in numerical columns using IQR method"""
        if len(self.numerical_cols) == 0:
            return
            
        print("=" * 80)
        print("🎯 OUTLIER DETECTION (IQR Method)")
        print("=" * 80)
        
        outlier_summary = []
        
        for col in self.numerical_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            outlier_count = len(outliers)
            outlier_pct = (outlier_count / len(self.df)) * 100
            
            if outlier_count > 0:
                outlier_summary.append({
                    'Column': col,
                    'Outlier_Count': outlier_count,
                    'Percentage': f"{outlier_pct:.2f}%",
                    'Lower_Bound': f"{lower_bound:.2f}",
                    'Upper_Bound': f"{upper_bound:.2f}"
                })
        
        if outlier_summary:
            print(pd.DataFrame(outlier_summary).to_string(index=False))
        else:
            print("✅ No significant outliers detected!")
        
        print("\n")
        self.report['outliers'] = outlier_summary
        
    def target_analysis(self):
        """Analyze target variable if specified"""
        if self.target_col is None or self.target_col not in self.df.columns:
            return
            
        print("=" * 80)
        print(f"🎯 TARGET VARIABLE ANALYSIS: {self.target_col}")
        print("=" * 80)
        
        # Check if target is numerical or categorical
        if self.target_col in self.numerical_cols:
            # Regression task
            print("📊 Target Type: NUMERICAL (Regression)")
            print(f"   Mean: {self.df[self.target_col].mean():.2f}")
            print(f"   Median: {self.df[self.target_col].median():.2f}")
            print(f"   Std: {self.df[self.target_col].std():.2f}")
            print(f"   Min: {self.df[self.target_col].min():.2f}")
            print(f"   Max: {self.df[self.target_col].max():.2f}")
            
            # Distribution
            plt.figure(figsize=(12, 5))
            plt.subplot(1, 2, 1)
            self.df[self.target_col].hist(bins=30, edgecolor='black', alpha=0.7)
            plt.title(f'Distribution: {self.target_col}', fontweight='bold')
            plt.xlabel(self.target_col)
            plt.ylabel('Frequency')
            
            plt.subplot(1, 2, 2)
            sns.boxplot(y=self.df[self.target_col])
            plt.title(f'Boxplot: {self.target_col}', fontweight='bold')
            plt.tight_layout()
            plt.show()
            
        else:
            # Classification task
            print("📊 Target Type: CATEGORICAL (Classification)")
            value_counts = self.df[self.target_col].value_counts()
            print(f"\n   Class Distribution:")
            print(value_counts.to_string())
            
            # Check for imbalance
            max_class = value_counts.max()
            min_class = value_counts.min()
            imbalance_ratio = max_class / min_class if min_class > 0 else float('inf')
            
            if imbalance_ratio > 3:
                print(f"\n   ⚠️  IMBALANCED CLASSES detected! Ratio: {imbalance_ratio:.2f}:1")
            else:
                print(f"\n   ✅ Classes are relatively balanced")
            
            # Visualization
            plt.figure(figsize=(10, 6))
            value_counts.plot(kind='bar', color='skyblue', edgecolor='black')
            plt.title(f'Target Distribution: {self.target_col}', fontsize=14, fontweight='bold')
            plt.xlabel(self.target_col)
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        
        print("\n")
        
    def feature_target_relationship(self):
        """Analyze relationship between features and target"""
        if self.target_col is None or self.target_col not in self.df.columns:
            return
            
        print("=" * 80)
        print(f"🔗 FEATURE-TARGET RELATIONSHIP ANALYSIS")
        print("=" * 80)
        
        # Numerical features vs target
        if self.target_col in self.categorical_cols and len(self.numerical_cols) > 0:
            # Classification: Box plots for each numerical feature
            n_cols = len(self.numerical_cols)
            n_rows = (n_cols + 2) // 3
            
            fig, axes = plt.subplots(n_rows, 3, figsize=(15, n_rows * 4))
            axes = axes.flatten() if n_cols > 1 else [axes]
            
            for idx, col in enumerate(self.numerical_cols):
                if idx < len(axes):
                    sns.boxplot(data=self.df, x=self.target_col, y=col, ax=axes[idx])
                    axes[idx].set_title(f'{col} vs {self.target_col}', fontweight='bold')
                    axes[idx].tick_params(axis='x', rotation=45)
            
            for idx in range(n_cols, len(axes)):
                axes[idx].axis('off')
                
            plt.tight_layout()
            plt.show()
            
        elif self.target_col in self.numerical_cols and len(self.numerical_cols) > 1:
            # Regression: Scatter plots
            other_numerical = [col for col in self.numerical_cols if col != self.target_col]
            n_cols = len(other_numerical)
            n_rows = (n_cols + 2) // 3
            
            fig, axes = plt.subplots(n_rows, 3, figsize=(15, n_rows * 4))
            axes = axes.flatten() if n_cols > 1 else [axes]
            
            for idx, col in enumerate(other_numerical):
                if idx < len(axes):
                    axes[idx].scatter(self.df[col], self.df[self.target_col], alpha=0.5)
                    axes[idx].set_xlabel(col)
                    axes[idx].set_ylabel(self.target_col)
                    axes[idx].set_title(f'{col} vs {self.target_col}', fontweight='bold')
                    
                    # Add correlation
                    corr = self.df[[col, self.target_col]].corr().iloc[0, 1]
                    axes[idx].text(0.05, 0.95, f'Corr: {corr:.3f}', 
                                 transform=axes[idx].transAxes, 
                                 verticalalignment='top',
                                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
            
            for idx in range(n_cols, len(axes)):
                axes[idx].axis('off')
                
            plt.tight_layout()
            plt.show()
        
        print("\n")
        
    def generate_report(self, save_path=None):
        """Generate comprehensive EDA report"""
        print("=" * 80)
        print("📝 GENERATING EDA REPORT")
        print("=" * 80)
        
        report_text = f"""
{'=' * 80}
AUTOMATED EDA REPORT
{'=' * 80}

Dataset Shape: {self.df.shape}
Total Rows: {self.df.shape[0]:,}
Total Columns: {self.df.shape[1]}

COLUMN TYPES:
- Numerical: {len(self.numerical_cols)}
- Categorical: {len(self.categorical_cols)}
- DateTime: {len(self.datetime_cols)}

MISSING VALUES:
- Columns with missing values: {len([col for col in self.df.columns if self.df[col].isnull().sum() > 0])}
- Total missing cells: {self.df.isnull().sum().sum():,}

DUPLICATES:
- Duplicate rows: {self.df.duplicated().sum():,}

{'=' * 80}
"""
        print(report_text)
        
        if save_path:
            with open(save_path, 'w') as f:
                f.write(report_text)
            print(f"✅ Report saved to: {save_path}")
        
        return self.report
    
    def run_complete_eda(self):
        """Run complete EDA pipeline"""
        print("\n")
        print("🚀 " + "=" * 76 + " 🚀")
        print("🚀" + " " * 20 + "AUTO EDA TOOLKIT - STARTING" + " " * 29 + "🚀")
        print("🚀 " + "=" * 76 + " 🚀")
        print("\n")
        
        # Run all analyses
        self.identify_column_types()
        self.basic_info()
        self.missing_value_analysis()
        self.numerical_analysis()
        self.categorical_analysis()
        self.outlier_detection()
        self.target_analysis()
        self.feature_target_relationship()
        
        print("\n")
        print("✅ " + "=" * 76 + " ✅")
        print("✅" + " " * 20 + "EDA COMPLETE! ALL DONE!" + " " * 33 + "✅")
        print("✅ " + "=" * 76 + " ✅")
        print("\n")
        
        return self.report
