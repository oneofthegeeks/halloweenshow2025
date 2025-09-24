# 🎃 ScarePi Enhanced Docker Container 🦇
# Marketing Platform + Haunted House Control System

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libasound2-dev \
    portaudio19-dev \
    ffmpeg \
    sqlite3 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements_docker.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p /app/static /app/templates /app/data

# Set permissions
RUN chmod +x /app/install.sh /app/setup_local.sh /app/start_local.sh

# Create non-root user
RUN useradd -m -u 1000 scarepi && chown -R scarepi:scarepi /app
USER scarepi

# Expose port
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/api/status || exit 1

# Default command
CMD ["python", "app_docker.py"]
