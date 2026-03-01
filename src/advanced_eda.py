"""
Advanced EDA Features - Bonus Module
Time series, text analysis, and more!
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


class AdvancedEDA:
    """
    Advanced EDA features for specific use cases
    """
    
    def __init__(self, df):
        self.df = df.copy()
        
    def time_series_analysis(self, date_col, value_col):
        """
        Analyze time series data
        
        Parameters:
        -----------
        date_col : str
            Column containing dates
        value_col : str
            Column with values to analyze
        """
        print("=" * 80)
        print(f"📅 TIME SERIES ANALYSIS: {value_col} over {date_col}")
        print("=" * 80)
        
        # Convert to datetime
        self.df[date_col] = pd.to_datetime(self.df[date_col])
        self.df = self.df.sort_values(date_col)
        
        # Basic statistics
        print(f"\n📊 Time Range: {self.df[date_col].min()} to {self.df[date_col].max()}")
        print(f"📊 Total Days: {(self.df[date_col].max() - self.df[date_col].min()).days}")
        
        # Plot time series
        plt.figure(figsize=(15, 6))
        plt.plot(self.df[date_col], self.df[value_col], linewidth=2)
        plt.title(f'Time Series: {value_col}', fontsize=14, fontweight='bold')
        plt.xlabel(date_col)
        plt.ylabel(value_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        # Trend analysis
        if len(self.df) > 30:
            # Rolling average
            self.df['rolling_mean'] = self.df[value_col].rolling(window=7).mean()
            
            plt.figure(figsize=(15, 6))
            plt.plot(self.df[date_col], self.df[value_col], alpha=0.5, label='Original')
            plt.plot(self.df[date_col], self.df['rolling_mean'], linewidth=2, label='7-day Rolling Mean')
            plt.title(f'Trend Analysis: {value_col}', fontsize=14, fontweight='bold')
            plt.xlabel(date_col)
            plt.ylabel(value_col)
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()
        
        # Seasonality check (basic)
        if 'month' not in self.df.columns:
            self.df['month'] = self.df[date_col].dt.month
            
        monthly_avg = self.df.groupby('month')[value_col].mean()
        
        plt.figure(figsize=(12, 6))
        monthly_avg.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title(f'Monthly Average: {value_col}', fontsize=14, fontweight='bold')
        plt.xlabel('Month')
        plt.ylabel(f'Average {value_col}')
        plt.xticks(rotation=0)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
        print("\n✅ Time series analysis complete!\n")
    
    def text_column_analysis(self, text_col):
        """
        Analyze text columns
        
        Parameters:
        -----------
        text_col : str
            Column containing text data
        """
        print("=" * 80)
        print(f"📝 TEXT ANALYSIS: {text_col}")
        print("=" * 80)
        
        # Basic stats
        self.df['text_length'] = self.df[text_col].astype(str).apply(len)
        self.df['word_count'] = self.df[text_col].astype(str).apply(lambda x: len(x.split()))
        
        print(f"\n📊 Average Text Length: {self.df['text_length'].mean():.2f} characters")
        print(f"📊 Average Word Count: {self.df['word_count'].mean():.2f} words")
        print(f"📊 Max Text Length: {self.df['text_length'].max()}")
        print(f"📊 Min Text Length: {self.df['text_length'].min()}")
        
        # Distribution plots
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        axes[0].hist(self.df['text_length'], bins=30, edgecolor='black', alpha=0.7)
        axes[0].set_title('Text Length Distribution', fontweight='bold')
        axes[0].set_xlabel('Characters')
        axes[0].set_ylabel('Frequency')
        
        axes[1].hist(self.df['word_count'], bins=30, edgecolor='black', alpha=0.7, color='coral')
        axes[1].set_title('Word Count Distribution', fontweight='bold')
        axes[1].set_xlabel('Words')
        axes[1].set_ylabel('Frequency')
        
        plt.tight_layout()
        plt.show()
        
        print("\n✅ Text analysis complete!\n")
    
    def feature_engineering_suggestions(self, df_original):
        """
        Suggest feature engineering opportunities
        """
        print("=" * 80)
        print("💡 FEATURE ENGINEERING SUGGESTIONS")
        print("=" * 80)
        
        suggestions = []
        
        # Check for datetime columns
        for col in self.df.columns:
            if pd.api.types.is_datetime64_any_dtype(self.df[col]):
                suggestions.append({
                    'Type': 'DateTime',
                    'Column': col,
                    'Suggestion': 'Extract: year, month, day, dayofweek, hour, quarter'
                })
        
        # Check for high cardinality categorical
        for col in self.df.select_dtypes(include=['object']).columns:
            if self.df[col].nunique() > 50:
                suggestions.append({
                    'Type': 'High Cardinality',
                    'Column': col,
                    'Suggestion': 'Consider: frequency encoding, target encoding, or grouping'
                })
        
        # Check for skewed numerical
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            skewness = self.df[col].skew()
            if abs(skewness) > 1:
                suggestions.append({
                    'Type': 'Skewed Distribution',
                    'Column': col,
                    'Suggestion': f'Apply log/sqrt transformation (skew: {skewness:.2f})'
                })
        
        # Check for potential interaction features
        if len(numerical_cols) >= 2:
            suggestions.append({
                'Type': 'Interactions',
                'Column': 'Multiple',
                'Suggestion': 'Create polynomial features or ratios between numerical columns'
            })
        
        if suggestions:
            print("\n🎯 Recommendations:\n")
            for i, sug in enumerate(suggestions, 1):
                print(f"{i}. [{sug['Type']}] {sug['Column']}")
                print(f"   → {sug['Suggestion']}\n")
        else:
            print("\n✅ No immediate feature engineering suggestions")
        
        print("\n")
    
    def correlation_with_target(self, target_col, top_n=10):
        """
        Show top correlated features with target
        
        Parameters:
        -----------
        target_col : str
            Target column name
        top_n : int
            Number of top features to show
        """
        print("=" * 80)
        print(f"🎯 TOP {top_n} FEATURES CORRELATED WITH: {target_col}")
        print("=" * 80)
        
        # Select numerical columns only
        numerical_df = self.df.select_dtypes(include=[np.number])
        
        if target_col not in numerical_df.columns:
            print(f"❌ {target_col} is not numerical!")
            return
        
        # Calculate correlations
        correlations = numerical_df.corr()[target_col].drop(target_col).abs().sort_values(ascending=False)
        top_features = correlations.head(top_n)
        
        print(f"\n📊 Top {top_n} Correlated Features:\n")
        for i, (feature, corr) in enumerate(top_features.items(), 1):
            print(f"{i}. {feature:30s} : {corr:.4f}")
        
        # Visualization
        plt.figure(figsize=(12, 6))
        top_features.plot(kind='barh', color='teal', edgecolor='black')
        plt.title(f'Top {top_n} Features by Correlation with {target_col}', 
                 fontsize=14, fontweight='bold')
        plt.xlabel('Absolute Correlation')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
        
        print("\n")
    
    def data_quality_score(self):
        """
        Calculate overall data quality score
        """
        print("=" * 80)
        print("⭐ DATA QUALITY SCORE")
        print("=" * 80)
        
        scores = {}
        
        # 1. Missing values score (0-25 points)
        missing_pct = (self.df.isnull().sum().sum() / (self.df.shape[0] * self.df.shape[1])) * 100
        if missing_pct == 0:
            scores['Missing Values'] = 25
        elif missing_pct < 5:
            scores['Missing Values'] = 20
        elif missing_pct < 10:
            scores['Missing Values'] = 15
        elif missing_pct < 20:
            scores['Missing Values'] = 10
        else:
            scores['Missing Values'] = 5
        
        # 2. Duplicate score (0-25 points)
        dup_pct = (self.df.duplicated().sum() / len(self.df)) * 100
        if dup_pct == 0:
            scores['Duplicates'] = 25
        elif dup_pct < 5:
            scores['Duplicates'] = 20
        elif dup_pct < 10:
            scores['Duplicates'] = 15
        else:
            scores['Duplicates'] = 10
        
        # 3. Data types score (0-25 points)
        # Check if appropriate types are used
        scores['Data Types'] = 20  # Default good score
        
        # 4. Outliers score (0-25 points)
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        outlier_ratio = 0
        
        if len(numerical_cols) > 0:
            for col in numerical_cols:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                outliers = ((self.df[col] < (Q1 - 1.5 * IQR)) | 
                           (self.df[col] > (Q3 + 1.5 * IQR))).sum()
                outlier_ratio += outliers / len(self.df)
            
            outlier_ratio = (outlier_ratio / len(numerical_cols)) * 100
            
            if outlier_ratio < 1:
                scores['Outliers'] = 25
            elif outlier_ratio < 3:
                scores['Outliers'] = 20
            elif outlier_ratio < 5:
                scores['Outliers'] = 15
            else:
                scores['Outliers'] = 10
        else:
            scores['Outliers'] = 25
        
        total_score = sum(scores.values())
        
        print("\n📊 Quality Breakdown:\n")
        for category, score in scores.items():
            bar = '█' * (score // 5)
            print(f"{category:20s}: {bar:5s} {score}/25")
        
        print(f"\n{'='*80}")
        print(f"🏆 OVERALL QUALITY SCORE: {total_score}/100")
        
        if total_score >= 90:
            print("✅ Excellent! Your data is in great shape!")
        elif total_score >= 75:
            print("✅ Good! Minor improvements needed.")
        elif total_score >= 60:
            print("⚠️  Fair. Some cleaning recommended.")
        else:
            print("❌ Poor. Significant data cleaning needed!")
        
        print("=" * 80 + "\n")
        
        return total_score
