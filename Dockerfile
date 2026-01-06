#Use official Python image
FROM python:3.10-slim

#Set working directory
WORKDIR /app

#Install system dependencies (Chrome)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libgbm1 \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

#Copy automation files
COPY automation/ automation/
COPY frontend/ frontend/

#Install Python dependencies
RUN pip install --no-cache-dir -r automation/requirements.txt

#Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

#Run the Selenium test
CMD ["python", "automation/selenium_test.py"]
