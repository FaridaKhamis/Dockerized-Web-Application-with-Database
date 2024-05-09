 # Use the official Python 3.8 slim image as the base
FROM python:3.8-slim        

# Set the working directory inside the container to /app
WORKDIR /app               

# Copy the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/      

# Install the Python dependencies listed in requirements.txt       
# The --no-cache-dir flag ensures that pip does not cache the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the application code from the host to the container's /app directory
COPY . /app

# Expose port 3000 on the container
EXPOSE 3000

# Define the command to run when the container starts
CMD ["python", "app.py"]
