# Use the official MySQL image as the base
FROM mysql:5.7

# Set the root password for the database
ENV MYSQL_ROOT_PASSWORD=cam

# Copy the initialization script to the image
COPY init.sql /docker-entrypoint-initdb.d/

# Set the port for the database connection
ENV MYSQL_PORT=3401

# Expose the port 3400 for the database connection
EXPOSE 3401
