# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Clone the Git repository
RUN apt-get update && \
    apt-get install -y git && \
    git clone https://github.com/fai-aher/RASI-MEDICAL.git

# Change the working directory to /app/auth-app
WORKDIR /app/RASI-MEDICAL/auth-app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that your FastAPI app will run on
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
