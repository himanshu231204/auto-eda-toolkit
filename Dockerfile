# Dockerfile for Auto EDA Toolkit

FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create directories for data and outputs
RUN mkdir -p examples outputs

# Expose port for Streamlit (if using web app)
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command (run demo)
CMD ["python", "demo.py"]

# Alternative commands (uncomment as needed):
# For Streamlit app:
# CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# For interactive shell:
# CMD ["/bin/bash"]

# For Jupyter notebook:
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
