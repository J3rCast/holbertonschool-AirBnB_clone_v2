#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "im alive!" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
rm -f /etc/nginx/modules-available/default
cp config_file /etc/nginx/sites-available/default
