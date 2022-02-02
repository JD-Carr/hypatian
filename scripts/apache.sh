#!/usr/bin/env bash
# vim: ft=sh
set -euxo pipefail

# Remove existing PID file
rm --force /var/run/apache2/apache2.pid

exec /usr/sbin/apache2ctl -D FOREGROUND
