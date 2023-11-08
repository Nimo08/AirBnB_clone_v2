#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf  /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i ' 56i location /hbnb_static/ {\
	        alias /data/web_static/current/;\
	}' /etc/nginx/sites-available/default
service nginx restart
