#!/usr/bin/env bash
# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the required directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content
nginx_config="
server {
    listen 80;
    listen [::]:80;

    location /hbnb_static {
        alias /data/web_static/current/;
        autoindex off;
    }
}
"

# Add the configuration to Nginx (Assuming default Nginx configuration file. Adjust if necessary)
echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo systemctl restart nginx

