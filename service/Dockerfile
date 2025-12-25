# Use an official lightweight Python image.
# This runs on Linux, so pyswisseph compiles easily here.
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies if needed (usually none for basic swisseph, 
# but sometimes build-essential is needed for compiling C extensions)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements and install
COPY service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Application Code
COPY service/app ./app

# Copy the Ephemeris Files from the PARENT directory context
# We will run the build command from the root 'vedic-astro-engine' folder
COPY local-ephe/ephe ./ephe

# Set Environment Variable for Ephemeris path
ENV EPHE_PATH=/app/ephe

# Expose port
EXPOSE 8080

# Command to run the app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]