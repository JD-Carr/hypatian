#!/usr/bin/env bash

# Declare project directory here for easy modification per server OS.
dir="/var/www/hypatian/ssl"

dir_ca_root="${dir}/ca/root"
dir_ca_root_db="${dir_ca_root}/db"
dir_ca_root_certs="${dir_ca_root}/certs"
dir_ca_root_csr="${dir_ca_root}/csr"
ca_root_db="${dir_ca_root_db}/ca.db.txt"
ca_root_cnf="${dir_ca_root}/ca.cnf"
ca_root_csr="${dir_ca_root_csr}/ca.csr"
ca_root_crt="${dir_ca_root_certs}/ca.crt.pem"
ca_root_ext="req_ca_root_x509_ext"

dir_ca_int="${dir}/ca/intermediate"
dir_ca_int_db="${dir_ca_int}/db"
dir_ca_int_certs="${dir_ca_int}/certs"
dir_ca_int_csr="${dir_ca_int}/csr"
ca_int_db="${dir_ca_int_db}/intermediate.db.txt"
ca_int_cnf="${dir_ca_int}/intermediate.cnf"
ca_int_csr="${dir_ca_int_csr}/intermediate.csr"
ca_int_crt="${dir_ca_int_certs}/intermediate.crt.pem"
ca_int_ext="req_ca_intermediate_x509_ext"

dir_lh="${dir}/localhost"
dir_lh_certs="${dir_lh}/certs"
dir_lh_csr="${dir_lh}/csr"
lh_cnf="${dir_lh}/localhost.cnf"
lh_csr="${dir_lh_csr}/localhost.csr"
lh_crt="${dir_lh_certs}/localhost.crt.pem"
lh_chain_crt="${dir_lh_certs}/localhost.chain.crt.pem"
lh_ext="intermediate_server_ext"

[[ ! -f "${ca_root_db}" ]] && touch "${ca_root_db}"

openssl req -out "${ca_root_csr}" -new -config "${ca_root_cnf}"

openssl ca -config "${ca_root_cnf}" -selfsign -in "${ca_root_csr}" -out "${ca_root_crt}" -batch -extensions "${ca_root_ext}" -create_serial

[[ ! -f "${ca_int_db}" ]] && touch "${ca_int_db}"

openssl req -out "${ca_int_csr}" -new -config "${ca_int_cnf}"

openssl ca -config "${ca_root_cnf}" -in "${ca_int_csr}" -out "${ca_int_crt}" -batch -extensions "${ca_int_ext}" -rand_serial

cp "${ca_int_crt}" "${lh_chain_crt}"

cat "${ca_root_crt}" >> "${lh_chain_crt}"

openssl req -out "${lh_csr}" -new -config "${lh_cnf}"

openssl ca -config "${ca_int_cnf}" -in "${lh_csr}" -out "${lh_crt}" -batch -extensions "${lh_ext}" -rand_serial
