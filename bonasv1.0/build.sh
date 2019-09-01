#!/bin/sh

docker stop bonas.nextcloud
docker rm bonas.nextcloud

docker stop bonas.db
docker rm bonas.db

docker run -id --restart=always --name=bonas.db -v /usr/local/bonas/db:/var/liblib/mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=320000 -e MYSQL_DATABASE=bonas -e MYSQL_USER=bonasdbusr -e MYSQL_PASSWORD=320000 --privileged=true  mariadb 
docker run -d --restart=always --name=bonas.nextcloud  --link=bonas.db:db -p  80:80 -v /usr/local/bonas/data:/data docker.io/nextcloud

