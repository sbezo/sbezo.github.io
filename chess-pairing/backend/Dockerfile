# Use a lightweight Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Expose Flask API port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]