#!/usr/bin/env bash

server_name=localhost

hosts_file=/etc/hosts
printf "127.0.0.1\t${server_name}\n" >> "${hosts_file}"

apache_file=/etc/apache2/httpd.conf
printf "ServerName ${server_name}\n" >> "${apache_file}"

printf "ServerName localhost\n" >> /etc/apache2/apache2.conf
