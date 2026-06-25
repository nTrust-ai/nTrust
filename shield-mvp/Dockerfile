# nTrust Shield MVP: TrustAudit Engine Dockerfile
# Architecture: Python 3.11 Slim + Uvicorn ASGI Server
# Mandate: Local-First MVP, Zero Cloud Dependency

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for PostgreSQL adapter & security scanners
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Expose standard API port for local development & orchestration
EXPOSE 8000

# Run Uvicorn with hot-reload disabled for production parity, enabled via env in dev
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
