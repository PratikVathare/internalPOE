# Dockerfile
# This file builds a container for the project using Python 3.11.
# It copies the script into the container and runs it.

FROM python:3.11-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the Python script into the container.
COPY hello.py .

# Run the script when the container starts.
CMD ["python", "hello.py"]
