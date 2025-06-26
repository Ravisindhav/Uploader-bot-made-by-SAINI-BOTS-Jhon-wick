# Use a base image with Python
FROM python:3.10.6-slim-buster

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    curl ffmpeg libsm6 libxext6 \
    build-essential python3-dev \
    ca-certificates \
    && apt-get clean

# Make sure SSL certificates are up to date
RUN update-ca-certificates

# Set working directory
WORKDIR /app

# Copy everything into container
COPY . .

# Install Python packages (make sure certifi is in requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Run app using gunicorn + python if needed
CMD gunicorn app:app & python3 main.py
