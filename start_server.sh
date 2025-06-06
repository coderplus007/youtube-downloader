#!/bin/bash

# Stop any processes using port 8080
echo "Checking for processes using port 8080..."
PORT_PID=$(lsof -ti:8080)
if [ ! -z "$PORT_PID" ]; then
    echo "Killing process using port 8080: $PORT_PID"
    kill -9 $PORT_PID
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Make sure necessary directories exist
mkdir -p downloads instance

# Start the Flask application
echo "Starting YouTube Downloader server on port 8080..."
python app.py