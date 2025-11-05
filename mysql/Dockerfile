# Use the official MySQL image as base
FROM mysql:8.0

# Set environment variables for MySQL initialization
ENV MYSQL_ROOT_PASSWORD=yourRootPasswordHere \
    MYSQL_DATABASE=registrationdb \
    MYSQL_USER=admin \
    MYSQL_PASSWORD=adminPasswordHere

# Copy your SQL initialization script into the right folder so it’s executed on first run
COPY    DBtables.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306

# The base image defines its own ENTRYPOINT / CMD to start mysqld
