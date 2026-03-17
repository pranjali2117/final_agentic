# ========================================
# Stage 1: Builder
# ========================================
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies needed for compiling Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and construct wheels
COPY requirement.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirement.txt

# ========================================
# Stage 2: Runner
# ========================================
FROM python:3.10-slim

WORKDIR /app

# Create a non-root user
RUN addgroup --system appgroup && adduser --system --group appuser

# Copy wheels from builder and install
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirement.txt .
RUN pip install --no-cache /wheels/*

# Copy application code
COPY . .

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user for security
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
