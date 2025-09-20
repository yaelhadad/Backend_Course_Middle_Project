# Use Python 3.11 slim image for better performance and smaller size
FROM python:3.11-slim

# Set environment variables for optimization
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
# Using --no-install-recommends to reduce image size
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt /app/

# Install Python dependencies
# Using --no-cache-dir and --compile for optimization
RUN pip install --no-cache-dir --compile -r requirements.txt

# Copy project files
COPY . /app/

# Create directories for media and static files
RUN mkdir -p /app/media/logos /app/static

# Collect static files (for production optimization)
RUN python manage.py collectstatic --noinput --clear

# Create a non-root user for security
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000


# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
