# Use an official Python runtime as the base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Set PYTHONPATH to include the src directory
ENV PYTHONPATH="/app/src"

# Copy your dependency file (requirements.txt) into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your app will run on (e.g., 8000 for FastAPI)
EXPOSE 8000

# Specify the command to run your app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
