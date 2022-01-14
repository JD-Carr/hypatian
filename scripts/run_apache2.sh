#!/bin/bash

# Make sure we're not confused by old, incompletely-shutdown apache/httpd
# context after restarting the container.  apache/httpd won't start correctly
# if it thinks it is already running.
rm --recursive --silent /run/httpd/* /tmp/httpd*

exec /usr/sbin/apache2ctl -DFOREGROUND
