"""
Configuration file for Auto EDA Toolkit
Customize settings here!
"""

# Column Type Detection
CATEGORICAL_THRESHOLD = 10  # Max unique values to consider as categorical
DATETIME_AUTO_DETECT = True

# Visualization Settings
PLOT_STYLE = 'whitegrid'  # seaborn styles: whitegrid, darkgrid, white, dark, ticks
FIGURE_SIZE = (12, 6)
COLOR_PALETTE = 'husl'  # seaborn palettes: deep, muted, bright, pastel, dark, colorblind

# Statistical Settings
OUTLIER_METHOD = 'IQR'  # IQR or Z-score
IQR_MULTIPLIER = 1.5
CORRELATION_THRESHOLD = 0.7  # For high correlation detection

# Missing Value Settings
MISSING_THRESHOLD = 0.5  # Drop columns with >50% missing values (if enabled)
AUTO_DROP_MISSING = False

# Visualization Limits
MAX_CATEGORIES_TO_PLOT = 20  # Max categories in bar plots
MAX_FEATURES_IN_CORRELATION = 50  # Max features in correlation heatmap

# Report Settings
SAVE_PLOTS = False
PLOT_OUTPUT_DIR = 'outputs/plots/'
REPORT_OUTPUT_DIR = 'outputs/reports/'

# Advanced Settings
ENABLE_WARNINGS = False
RANDOM_STATE = 42

# Performance Settings
SAMPLE_SIZE = None  # Set to number if you want to sample large datasets
CHUNK_SIZE = 10000  # For processing large files

# Text Analysis Settings
MIN_TEXT_LENGTH = 10  # Minimum characters to consider as text
MAX_TEXT_PREVIEW = 100  # Max characters to show in preview

# Time Series Settings
ROLLING_WINDOW = 7  # Days for rolling average
SEASONALITY_PERIODS = [7, 30, 365]  # Check for weekly, monthly, yearly patterns

# Feature Engineering
AUTO_SUGGEST_FEATURES = True
SKEW_THRESHOLD = 1.0  # Threshold for suggesting transformations
HIGH_CARDINALITY_THRESHOLD = 50  # Threshold for categorical encoding suggestions

# Target Analysis
CLASS_IMBALANCE_RATIO = 3.0  # Ratio to flag class imbalance
TARGET_BINS = 10  # Bins for regression target distribution

# Export Settings
EXPORT_FORMAT = 'txt'  # txt, html, pdf, csv
INCLUDE_PLOTS_IN_REPORT = True

# Custom Color Schemes
CUSTOM_COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e',
    'success': '#2ca02c',
    'warning': '#d62728',
    'info': '#9467bd'
}

# Profiling Settings
DETAILED_PROFILING = True
INCLUDE_INTERACTIONS = False  # Computationally expensive
