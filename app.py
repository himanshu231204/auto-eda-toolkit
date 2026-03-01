
import streamlit as st
import pandas as pd
import sys
import io
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns

# Configure page
st.set_page_config(
    page_title="Auto EDA Toolkit",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        text-align: center;
        margin-bottom: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Import EDA engine
sys.path.append('./src')
try:
    from eda_engine import AutoEDA
    from advanced_eda import AdvancedEDA
except ImportError:
    st.error("⚠️ Cannot import EDA modules. Make sure src/eda_engine.py exists!")
    st.stop()

# Header
st.markdown('<h1 class="main-header">🚀 Auto EDA Toolkit</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">90-95% EDA Automation for Any Dataset</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ Configuration")
st.sidebar.markdown("---")

# File upload
uploaded_file = st.sidebar.file_uploader(
    "📁 Upload Your Dataset",
    type=['csv', 'xlsx', 'xls'],
    help="Supported formats: CSV, Excel"
)

# Analysis options
st.sidebar.markdown("### 🎯 Analysis Options")
target_col = st.sidebar.text_input(
    "Target Column (optional)",
    help="Specify target column for supervised learning analysis"
)

run_advanced = st.sidebar.checkbox(
    "🔬 Run Advanced Analysis",
    value=False,
    help="Include time series, text analysis, and feature suggestions"
)

# Analysis type
analysis_type = st.sidebar.radio(
    "📊 Analysis Type",
    ["Complete EDA", "Step-by-Step", "Custom"],
    help="Choose how detailed you want the analysis"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 About")
st.sidebar.info(
    "This toolkit automatically performs 90-95% of standard EDA tasks. "
    "Upload your dataset and let the magic happen! ✨"
)

# Main content
if uploaded_file is not None:
    try:
        # Load data
        with st.spinner("📂 Loading dataset..."):
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ Dataset loaded successfully! Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Dataset preview
        with st.expander("👀 Preview Dataset", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Rows", f"{df.shape[0]:,}")
            with col2:
                st.metric("Total Columns", df.shape[1])
            with col3:
                st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
            
            st.dataframe(df.head(10), use_container_width=True)
        
        # Target column validation
        target = None
        if target_col:
            if target_col in df.columns:
                target = target_col
                st.info(f"🎯 Target column set: **{target}**")
            else:
                st.warning(f"⚠️ Column '{target_col}' not found in dataset!")
        
        # Run EDA button
        if st.button("🚀 Run EDA Analysis", type="primary", use_container_width=True):
            
            # Initialize EDA
            eda = AutoEDA(df, target_col=target)
            
            if analysis_type == "Complete EDA":
                with st.spinner("🔄 Running complete EDA... This may take a moment..."):
                    
                    # Create tabs for different sections
                    tab1, tab2, tab3, tab4, tab5 = st.tabs([
                        "📊 Overview",
                        "🔢 Numerical",
                        "📋 Categorical",
                        "🎯 Target",
                        "📝 Report"
                    ])
                    
                    with tab1:
                        st.subheader("📊 Dataset Overview")
                        
                        # Column types
                        eda.identify_column_types()
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Numerical Columns", len(eda.numerical_cols))
                            st.write(eda.numerical_cols)
                        with col2:
                            st.metric("Categorical Columns", len(eda.categorical_cols))
                            st.write(eda.categorical_cols)
                        with col3:
                            st.metric("DateTime Columns", len(eda.datetime_cols))
                            st.write(eda.datetime_cols)
                        
                        # Missing values
                        st.markdown("### 🔍 Missing Values")
                        missing = df.isnull().sum()
                        missing_pct = (missing / len(df)) * 100
                        missing_df = pd.DataFrame({
                            'Column': missing.index,
                            'Missing_Count': missing.values,
                            'Missing_Percentage': missing_pct.values
                        }).sort_values('Missing_Count', ascending=False)
                        
                        cols_with_missing = missing_df[missing_df['Missing_Count'] > 0]
                        if len(cols_with_missing) > 0:
                            st.dataframe(cols_with_missing, use_container_width=True)
                            
                            # Plot
                            fig, ax = plt.subplots(figsize=(10, 6))
                            sns.barplot(data=cols_with_missing.head(10), y='Column', x='Missing_Percentage', ax=ax)
                            ax.set_title('Top 10 Columns with Missing Values')
                            ax.set_xlabel('Missing Percentage (%)')
                            st.pyplot(fig)
                        else:
                            st.success("✅ No missing values found!")
                        
                        # Duplicates
                        dup_count = df.duplicated().sum()
                        if dup_count > 0:
                            st.warning(f"⚠️ Found {dup_count:,} duplicate rows ({dup_count/len(df)*100:.2f}%)")
                        else:
                            st.success("✅ No duplicate rows found!")
                    
                    with tab2:
                        st.subheader("🔢 Numerical Analysis")
                        
                        if len(eda.numerical_cols) > 0:
                            # Statistical summary
                            st.markdown("### 📈 Statistical Summary")
                            summary = df[eda.numerical_cols].describe().T
                            st.dataframe(summary, use_container_width=True)
                            
                            # Distributions
                            st.markdown("### 📊 Distributions")
                            selected_num_col = st.selectbox(
                                "Select column to visualize",
                                eda.numerical_cols
                            )
                            
                            if selected_num_col:
                                fig, axes = plt.subplots(1, 2, figsize=(12, 4))
                                
                                # Histogram
                                df[selected_num_col].hist(bins=30, ax=axes[0], edgecolor='black')
                                axes[0].set_title(f'Distribution: {selected_num_col}')
                                axes[0].set_xlabel(selected_num_col)
                                axes[0].set_ylabel('Frequency')
                                
                                # Box plot
                                sns.boxplot(y=df[selected_num_col], ax=axes[1])
                                axes[1].set_title(f'Box Plot: {selected_num_col}')
                                
                                plt.tight_layout()
                                st.pyplot(fig)
                            
                            # Correlation matrix
                            if len(eda.numerical_cols) > 1:
                                st.markdown("### 🔗 Correlation Matrix")
                                corr = df[eda.numerical_cols].corr()
                                
                                fig, ax = plt.subplots(figsize=(10, 8))
                                sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
                                          square=True, linewidths=1, fmt='.2f', ax=ax)
                                ax.set_title('Correlation Matrix')
                                st.pyplot(fig)
                        else:
                            st.info("ℹ️ No numerical columns found in the dataset.")
                    
                    with tab3:
                        st.subheader("📋 Categorical Analysis")
                        
                        if len(eda.categorical_cols) > 0:
                            selected_cat_col = st.selectbox(
                                "Select categorical column",
                                eda.categorical_cols
                            )
                            
                            if selected_cat_col:
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    st.markdown("### 📊 Value Counts")
                                    value_counts = df[selected_cat_col].value_counts().head(10)
                                    st.dataframe(value_counts, use_container_width=True)
                                
                                with col2:
                                    st.markdown("### 📈 Distribution")
                                    if df[selected_cat_col].nunique() <= 20:
                                        fig, ax = plt.subplots(figsize=(8, 6))
                                        value_counts.plot(kind='bar', ax=ax, edgecolor='black')
                                        ax.set_title(f'Distribution: {selected_cat_col}')
                                        ax.set_xlabel(selected_cat_col)
                                        ax.set_ylabel('Count')
                                        plt.xticks(rotation=45, ha='right')
                                        st.pyplot(fig)
                                    else:
                                        st.warning(f"Too many unique values ({df[selected_cat_col].nunique()}) to visualize")
                        else:
                            st.info("ℹ️ No categorical columns found in the dataset.")
                    
                    with tab4:
                        st.subheader("🎯 Target Variable Analysis")
                        
                        if target:
                            if target in eda.numerical_cols:
                                st.markdown("### 📊 Regression Target")
                                
                                col1, col2, col3 = st.columns(3)
                                with col1:
                                    st.metric("Mean", f"{df[target].mean():.2f}")
                                with col2:
                                    st.metric("Median", f"{df[target].median():.2f}")
                                with col3:
                                    st.metric("Std Dev", f"{df[target].std():.2f}")
                                
                                fig, axes = plt.subplots(1, 2, figsize=(12, 4))
                                
                                df[target].hist(bins=30, ax=axes[0], edgecolor='black')
                                axes[0].set_title(f'Distribution: {target}')
                                
                                sns.boxplot(y=df[target], ax=axes[1])
                                axes[1].set_title(f'Box Plot: {target}')
                                
                                st.pyplot(fig)
                                
                            else:
                                st.markdown("### 📊 Classification Target")
                                
                                value_counts = df[target].value_counts()
                                st.dataframe(value_counts, use_container_width=True)
                                
                                # Check imbalance
                                max_class = value_counts.max()
                                min_class = value_counts.min()
                                ratio = max_class / min_class if min_class > 0 else float('inf')
                                
                                if ratio > 3:
                                    st.warning(f"⚠️ Class imbalance detected! Ratio: {ratio:.2f}:1")
                                else:
                                    st.success("✅ Classes are relatively balanced")
                                
                                fig, ax = plt.subplots(figsize=(8, 6))
                                value_counts.plot(kind='bar', ax=ax, edgecolor='black')
                                ax.set_title(f'Target Distribution: {target}')
                                plt.xticks(rotation=45)
                                st.pyplot(fig)
                        else:
                            st.info("ℹ️ No target column specified. Add one in the sidebar for target analysis.")
                    
                    with tab5:
                        st.subheader("📝 Complete Report")
                        
                        # Generate report
                        report = eda.generate_report()
                        
                        # Display report
                        report_text = f"""
# EDA REPORT

## Dataset Information
- **Shape**: {df.shape[0]} rows × {df.shape[1]} columns
- **Memory**: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB
- **Duplicates**: {df.duplicated().sum():,} rows

## Column Types
- **Numerical**: {len(eda.numerical_cols)}
- **Categorical**: {len(eda.categorical_cols)}
- **DateTime**: {len(eda.datetime_cols)}

## Missing Values
- **Columns with missing**: {len([col for col in df.columns if df[col].isnull().sum() > 0])}
- **Total missing cells**: {df.isnull().sum().sum():,}

## Analysis Complete ✅
"""
                        st.text_area("Report", report_text, height=400)
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Report",
                            data=report_text,
                            file_name="eda_report.txt",
                            mime="text/plain",
                            use_container_width=True
                        )
            
            # Advanced analysis
            if run_advanced:
                st.markdown("---")
                st.subheader("🔬 Advanced Analysis")
                
                advanced = AdvancedEDA(df)
                
                with st.expander("⭐ Data Quality Score"):
                    quality = advanced.data_quality_score()
                    st.metric("Overall Quality", f"{quality}/100")
                
                if target and target in eda.numerical_cols:
                    with st.expander("🔗 Top Correlated Features"):
                        advanced.correlation_with_target(target, top_n=10)
            
            st.success("✅ Analysis Complete!")
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.exception(e)

else:
    # Landing page
    st.markdown("### 👋 Welcome to Auto EDA Toolkit!")
    st.markdown("Upload a dataset to get started with automated exploratory data analysis.")
    
    # Features
    st.markdown("---")
    st.markdown("### 🎯 What This Tool Does:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📊 Basic Analysis
        - Dataset overview
        - Column type detection
        - Missing value analysis
        - Duplicate detection
        """)
    
    with col2:
        st.markdown("""
        #### 📈 Statistical Analysis
        - Numerical summaries
        - Distribution plots
        - Correlation matrices
        - Outlier detection
        """)
    
    with col3:
        st.markdown("""
        #### 🎯 Target Analysis
        - Classification support
        - Regression support
        - Feature relationships
        - Class imbalance detection
        """)
    
    # Demo
    st.markdown("---")
    st.markdown("### 🚀 Quick Start")
    st.markdown("""
    1. Upload your dataset (CSV or Excel)
    2. Optionally specify a target column
    3. Click "Run EDA Analysis"
    4. Explore the results!
    """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #888;">Made with ❤️ (Himanshu Kumar) | Auto EDA Toolkit v1.0</p>',
        unsafe_allow_html=True
    )
    
    st.divider()

st.markdown(
    """
    <div style="text-align:center; font-size:14px;">
        👨‍💻 Developed by <b>Himanshu Kumar</b><br><br>
        🔗 
        <a href="https://www.linkedin.com/in/himanshu231204" target="_blank">LinkedIn</a> |
        <a href="https://github.com/himanshu231204" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Resources")
st.sidebar.markdown("[GitHub Repo](https://github.com/himanshu231204/auto-eda-toolkit)")
st.sidebar.markdown("[Documentation](https://github.com/himanshu231204/auto-eda-toolkit#readme)")
st.sidebar.markdown("[Report Issues](https://github.com/himanshu231204/auto-eda-toolkit/issues)")


