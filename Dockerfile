# Use an official Python image
FROM python:3.8-slim

WORKDIR /app

# Copy app files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80
EXPOSE 80

# Run the application
CMD ["python", "app.py"]
