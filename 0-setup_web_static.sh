#!/usr/bin/env bash
# Installs Ningx Web Server if not installed and Configures it to server web static contents
# shellcheck disable=SC2154

if ! dpkg -l | grep -q 'nginx' ; then
	sudo apt-get update
	sudo apt-get install nginx
fi

# creates files and directories for the static content
if [ ! -e /data/ ];
then
	sudo mkdir /data/
fi

if  [ ! -e /data/web_static/ ];then
	sudo mkdir /data/web_static/
fi

if [ ! -e /data/web_static/releases/ ];
then
	sudo mkdir /data/web_static/releases/test/
fi

if [ ! -e /data/web_static/shared/ ];
then
	sudo mkdir /data/web_static/shared/
fi

if [ ! -e /data/web_static/releases/test/ ];
then
	sudo mkdir /data/web_static/releases/test/
fi

sudo tee /data/web_static/releases/test/index.html > /dev/null << EOF 
AirBnB Clone
EOF
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

if [ -h /data/web_static/current ];
then
	rm /data/web_static/current
fi
# creates a symlink

# Configurations

sudo tee -a /etc/nginx/sites-available/default > /dev/null << EOF
server {
	listen 80;
	listen [::]:80;
	server_name techsorce.tech;
	
	root /data/web_static/current/;
	index index.html;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
	location / {
		try_files $uri $uri/ =404; 
	}
}
EOF
sudo service nginx restart
