# Use the official MySQL 5.7 image as the base
FROM mysql:5.7

# Set environment variables for MySQL(name,password)
ENV MYSQL_DATABASE=studentdb
ENV MYSQL_ROOT_PASSWORD=rootpassword

# Copy the init.sql script from the host to the Docker container
# This script will be executed when the MySQL container is started
COPY init.sql /docker-entrypoint-initdb.d/
