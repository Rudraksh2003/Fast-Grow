# Use the official Python image from Docker Hub
FROM python:3.9

# Install Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirement.txt .

# Install the required dependencies for Flask apps
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the Flask application code
COPY . .

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the Flask app and Nginx ports
EXPOSE 5001
EXPOSE 5002
EXPOSE 90

# Start both Flask apps and Nginx using a simple script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run the script to start both services
CMD ["/start.sh"]
