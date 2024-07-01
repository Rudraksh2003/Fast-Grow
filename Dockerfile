# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirement.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application code
COPY . .

# Expose the ports the app runs on
EXPOSE 5002
EXPOSE 5001

# Define the command to run the application
CMD ["python", "app.py"]

