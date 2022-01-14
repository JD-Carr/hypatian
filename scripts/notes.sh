#!/usr/env/bin bash
# https://newbedev.com/how-to-make-browser-trust-localhost-ssl-certificate
# https://www.golinuxcloud.com/add-x509-extensions-to-certificate-openssl/
# https://stackoverflow.com/questions/49553138/how-to-make-browser-trust-localhost-ssl-certificate
# https://gist.github.com/cecilemuller/9492b848eb8fe46d462abeb26656c4f8
# https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl
# https://examples.openshift.pub/certificate/
# https://unixcop.com/certificate-authority-with-openssl/
# TODO: Make a script to generate the CA files locally and install them before building container.

# Create Central Authority key
# Create Central Authrotiy certificate
# host.domain

# -selfsign: Use the extensions from the CSR and not from a CA CRT.

dir=/srv/www/vhosts/shuzhai/ssl
dir_ca="${dir}/ca"
dir_ca_private="${dir_ca}/private"

ca_key="${dev_ca_private}/ca.key.pem"

chmod 700 "${dir_ca}"

chmod 444 "${ca_key}"

openssl verify -partial_chain -CAfile ./ssl/ca/root/certs/ca.crt.pem ./ssl/localhost/certs/localhost.crt.pem

openssl verify -verbose -partial_chain -CAfile ./ssl/ca/intermediate/certs/intermediate.crt.pem ./ssl/localhost/certs/localhost.crt.pem

#the -x509 means that it is to be generated a certificate with x509 structure instead of a CSR.

# Dockerfile for test/prod?
# LINK apache config to docker logs.
# This outputs apache logs (error logs) to docker logs so that docker log <image_name> will show you apache logs
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log
RUN ln -sf /proc/self/fd/1 /var/log/apache2/error.log

# Manually set up the apache environment variables
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2.pid
