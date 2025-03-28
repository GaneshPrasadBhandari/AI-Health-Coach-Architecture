# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gcc \
    unzip \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files
COPY . .

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install extra tools
RUN pip install mlflow dvc[azure] apache-airflow evidently

# Expose port for Streamlit/FastAPI if used later
EXPOSE 8501

# Default command (optional)
CMD ["mlflow", "--version"]
