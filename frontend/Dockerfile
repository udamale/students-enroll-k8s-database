# Use an official Nginx image to serve the static frontend files
FROM nginx:alpine

# Copy the frontend files into the default nginx public directory
COPY index.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
