#!/usr/bin/env bash

# Note: we don't just use "apache2ctl" here because it itself is just a shell-script wrapper around apache2 which provides extra functionality like "apache2ctl start" for launching apache2 in the background.
# (also, when run as "apache2ctl <apache args>", it does not use "exec", which leaves an undesirable resident shell process)

printf "pre-set\n"

set -eo pipefail

printf "post-set\n"

#apache_run_dir=/var/run/apache2
#apache_run_user=www-data
#apache_run_group=www-data
#apache_pid_file=${run_dir}/apache.pid

printf "part01\n"

#ARGS='-DFOREGROUND'
#APACHE_CONFDIR=${APACHE_CONFDIR:=/etc/apache2}
#APACHE_ENVVARS=${APACHE_ENVVARS:=/etc/apache2/envvars}
#[[ -f ${APACHE_ENVVARS} ]] && . ${APACHE_ENVVARS}

HTTPD=/usr/sbin/apache2
ARGS='-k start'
exec ${HTTPD} ${ARGS}

/usr/sbin/apache2 -k start

#[ ! -d ${APACHE_RUN_DIR} ] && mkdir --force --parents ${APACHE_RUN_DIR}
#[ ! -d ${APACHE_LOCK_DIR} ] && mkdir ${APACHE_LOCK_DIR} && chown ${APACHE_RUN_USER} ${APACHE_LOCK_DIR}

#rm -f ${APACHE_RUN_DIR}/*ssl_scache*

#if [ ! -d ${apache_run_dir} ]; then
#	mkdir ${apache_run_dir}
#	chown ${apache_run_user}:${apache_run_group} ${apache_run_dir}
#fi

# Ensures no pre-existing pid-files exists.
#[[ -f ${apache_pid_file} ]] && rm --force ${apache_pid_file}

exec ${HTTPD} ${ARGS}

#exec apache2 -DFOREGROUND
