#!/usr/bin/env bash
# This script that sets up your web servers for the deployment of web_static

# Install nginx if not already installed
if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# create folders
if [ ! -e /data/web_static/shared/ ]; then
	sudo mkdir -p /data/web_static/shared/
fi

if [ ! -e /data/web_static/releases/test/ ]; then
	sudo mkdir -p /data/web_static/releases/test/
fi
echo "Hello from testing" | sudo tee /data/web_static/releases/test/index.html > /dev/null

if [ -h /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# back up nginx config file
if [ ! -e /etc/nginx/sites-available/default.bak ]; then
	cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
fi

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo tee -a /etc/nginx/sites-available/default > /dev/null << EOF
server {
    listen 80;  # default_server;
    listen [::]:80;  #default_server;
    
    # Add custom header
    add_header X-Served-By \$hostname;

    server_name techinit.tech www.techinit.tech;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
    	alias /data/web_static/current/;
    }
    error_page 404 /404.html;

    location /404 {
    	root /var/www/html;
	internal;
    }
}
EOF

# check for synthax error
sudo nginx -t

# Restart nginx
sudo service nginx restart
exit 0
