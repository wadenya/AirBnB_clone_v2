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
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

#Update Nginx configuration to serve the content
sudo sed -i "38i \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default

sudo service nginx restart
