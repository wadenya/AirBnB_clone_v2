#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install nginx

#create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

# create symbolic links
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Ownership to ubuntu
sudo chown -hR ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name zanderlex.tech;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart