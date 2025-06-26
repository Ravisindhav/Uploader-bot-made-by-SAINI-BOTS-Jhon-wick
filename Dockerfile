# Set the base image 
FROM python:3.10.6-slim-buster 
# Install required system packages 
RUN apt-get update -qq >/dev/null 2>&1 && \
 apt-get install -yqq ffmpeg libsm6 libxext6 curl -qq >/dev/null 2>&1 && \
 apt-get install -yqq build-essential python3-dev -qq >/dev/null 2>&1 && \
 apt-get clean -qq >/dev/null 2>&1 
# Install yt-dlp 
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp && \
 chmod a+rx /usr/local/bin/yt-dlp 
# Set the working directory 
WORKDIR /app 
# requirements.txt file ko copy karein 
COPY requirements.txt .
# Virtual environment banayein 
RUN python3 -m venv /app/venv 
ENV PATH="/app/venv/bin:$PATH"
# Virtual environment activate karein aur dependencies install karein 
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt 
# Copy the rest of the application code 
COPY . .
# Environment variables set karein
ENV OWNER_ID=5459854363 
# Set the command to run the Python script 
#CMD ["python", "main.py"] 
CMD gunicorn app:app & python3 main.py
