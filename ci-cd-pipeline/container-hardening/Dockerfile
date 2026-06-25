# nTrust Shield MVP - Container Hardening & Secure Base
FROM python:3.11-slim AS base
LABEL maintainer="devsecops@ntrust.ai"
LABEL security.level="high"

# Security Headers & Non-Root User Setup
RUN groupadd -r appgroup && useradd -r -g appgroup -d /home/app -s /bin/bash appuser

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    python -c "import security_baseline; print('Baseline verified')"

# Security Hardening Steps
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy application code with restricted permissions
COPY . .
RUN chown -R appuser:appgroup /app && \
    find /app -type d -exec chmod 750 {} \; && \
    find /app -type f -exec chmod 640 {} \;

USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
