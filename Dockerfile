# Use an official Python image
FROM python:3.8-slim

WORKDIR /app

# Copy application files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create log directory
RUN mkdir -p /var/log/myapp

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
