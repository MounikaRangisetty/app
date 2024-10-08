

# Stage 1: Use an official Python runtime as the base image
FROM python:3.8-slim as base

# Set the working directory inside the container
WORKDIR /my-python-app

# Copy the requirements file first to leverage caching during the build process
COPY requirements.txt .
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV APP_ENV=production
ENV DEBUG=False

# Expose the port the app will run on (adjust if necessary)
EXPOSE 4001  
# Ensure this matches the port used in app.run()

# Add a health check to ensure the container is running correctly
HEALTHCHECK CMD curl --fail http://43.203.121.184:4001/health || exit 1

# Set the default command to run the application
CMD ["python", "addition.py"]

