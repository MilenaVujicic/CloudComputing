#!/usr/bin/env bash

echo "DOCKER INSTALL"

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

echo "DOCKER INSTALL END"

echo "DOCKER COMPOSE INSTALL"

apt-get install curl
echo "Y" | curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "DOCKER COMPOSE INSTALL END"

echo "APP STARTING"

cd WebApp

docker-compose build
docker-compose up