FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies, Node.js, and npm
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs \
    && npm install -g prettier \
    && rm -rf /var/lib/apt/lists/*

# Copy pyproject.toml and install Python dependencies
COPY pyproject.toml .
RUN pip install --upgrade pip setuptools wheel && \
    pip install .

# Copy the rest of the application
COPY . .

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Command to run the app and format with prettier before starting the API
CMD prettier . --write && uvicorn app:app --host 0.0.0.0 --port 8000 --reload
