
from setuptools import setup, find_packages
import pathlib

# Read README
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="auto-eda-toolkit",
    version="1.0.0",
    author="Himanshu Kumar",
    author_email="himanshu231204@gmail.com",
    
    description="90-95% EDA Automation for Any Dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/himanshu231204/auto-eda-toolkit",
    project_urls={
        "Bug Reports": "https://github.com/himanshu231204/auto-eda-toolkit/issues",
        "Source": "https://github.com/himanshu231204/auto-eda-toolkit",
        "Documentation": "https://github.com/himanshu231204/auto-eda-toolkit#readme",
    },
    
    # Package configuration
    packages=find_packages(),
    package_data={
        "": ["*.md", "*.txt"],
    },
    
    # Python version requirement
    python_requires=">=3.7",
    
    # Dependencies
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0",
        "scikit-learn>=0.24.0",
        "openpyxl>=3.0.0",
    ],
    
    # Optional dependencies
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
        "web": [
            "streamlit>=1.0.0",
        ],
    },
    
    # Entry points for command-line scripts
    entry_points={
        "console_scripts": [
            "auto-eda=quick_eda:main",
        ],
    },
    
    # PyPI classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    # Keywords for search
    keywords="eda, exploratory data analysis, data science, machine learning, pandas, visualization, automation",
    
    # Include LICENSE
    license="MIT",
)
