#!/bin/sh

docker stop bonas.nextcloud
docker rm bonas.nextcloud

docker stop bonas.mairadb
docker rm bonas.mariadb

docker run -id --restart=always --name=bonas.mariadb -v /usr/local/bonas/db:/var/lib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=320000 -e MYSQL_DATABASE=bonas -e MYSQL_USER=admin -e MYSQL_PASSWORD=320000 --privileged=true  mariadb 
docker run -d --restart=always --name=bonas.nextcloud  -p  80:80 -v /usr/local/bonas/data:/data docker.io/nextcloud

