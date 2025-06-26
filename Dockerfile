# Use official Python image
FROM python:3.10.6-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 curl build-essential python3-dev && \
    apt-get clean

# Download yt-dlp manually
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole project
COPY . .

# Expose port for web (Render default: 10000 or 8080)
EXPOSE 10000

# Run the bot + web server
CMD gunicorn app:app --bind 0.0.0.0:10000 & python3 main.py
