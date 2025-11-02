# Stage 1: Static site served by Nginx
FROM nginx:alpine

# Copy all frontend files (HTML, CSS, JS, etc.) into the nginx default web root
COPY . /usr/share/nginx/html

# Expose port 80 for web traffic
EXPOSE 80

# Run Nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
