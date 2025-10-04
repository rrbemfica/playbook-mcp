FROM python:3.11-slim

WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy source code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Run the server
CMD ["python", "-m", "src.server"]