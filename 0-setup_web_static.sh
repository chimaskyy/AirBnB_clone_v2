#!/usr/bin/env bash
# Installs Ningx Web Server if not installed and Configures it to server web static contents

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
	sudo mkdir -p /data/web_static/releases/test
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
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

if [ -h /data/web_static/current ];
then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
# creates a symlink

# Configurations
if [ ! -e /etc/nginx/sites-available/default.bak ];
then
	sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
fi
sudo tee /etc/nginx/sites-available/default > /dev/null << EOF
server {
	listen 80 default_server;
	server_name techsorce.tech;

	index index.html;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
	root /data/web_static/current/;
	location / {
		try_files \$uri \$uri/ =404;
		add_header X-served-BY \$hostname;
	}
	listen [::]:80 default_server;
}
EOF
sudo service nginx restart
exit 0
