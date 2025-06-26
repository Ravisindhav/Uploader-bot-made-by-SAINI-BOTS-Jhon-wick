# Set the base image 
FROM python:3.10.6-slim-buster 
# Install required system packages 
RUN apt-get update -qq 2>/dev/null && \
 apt-get install -yqq ffmpeg libsm6 libxext6 curl -qq 2>/dev/null && \
 apt-get install -yqq build-essential python3-dev -qq 2>/dev/null && \
 apt-get clean -qq 2>/dev/null 
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
# Set the command to run the Python script 
#CMD ["python", "main.py"] 
CMD gunicorn app:app & python3 main.py
