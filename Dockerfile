# Base image
FROM python:3.10.6-slim-buster

# Install system packages
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 curl && \
    apt-get install -y build-essential python3-dev && \
    apt-get clean

# Install yt-dlp
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
    chmod a+rx /usr/local/bin/yt-dlp

# Set working directory
WORKDIR /app

# ✅ ✅ ✅ Ye line zaroor likho
COPY . .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD gunicorn app:app & python3 main.py
