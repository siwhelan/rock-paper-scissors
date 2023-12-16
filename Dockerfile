# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code to the working directory
COPY . .

# Set the command to run the app
CMD ["python", "app.py"]
# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install pipenv
RUN pip install pipenv

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in Pipfile
RUN pipenv install --system --deploy

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install any needed packages specified in package.json
RUN npm install

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]