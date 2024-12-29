# Use an official Python runtime as the base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port your app will run on (e.g., 8000 for FastAPI or Flask)
EXPOSE 8000

# Command to run your application (adjust based on your entry point)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
