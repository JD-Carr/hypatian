#!/usr/bin/env bash

dir="/var/www/hypatian/ssl"

dir_ca_root="${dir}/ca/root"
dir_ca_root_db="${dir_ca_root}/db"
dir_ca_root_private="${dir_ca_root}/private"
dir_ca_root_certs="${dir_ca_root}/certs"
dir_ca_root_csr="${dir_ca_root}/csr"
ca_root_db="${dir_ca_root_db}/ca.db.txt"
ca_root_cnf="${dir_ca_root}/ca.cnf"
ca_root_csr="${dir_ca_root_csr}/ca.csr"
ca_root_crt="${dir_ca_root_certs}/ca.crt.pem"
ca_root_crt_srl="${dir_ca_root_db}/ca.crt.srl"
ca_root_ext="req_ca_root_x509_ext"

dir_ca_int="${dir}/ca/intermediate"
dir_ca_int_db="${dir_ca_int}/db"
dir_ca_int_private="${dir_ca_int}/private"
dir_ca_int_certs="${dir_ca_int}/certs"
dir_ca_int_csr="${dir_ca_int}/csr"
ca_int_db="${dir_ca_int_db}/intermediate.db.txt"
ca_int_cnf="${dir_ca_int}/intermediate.cnf"
ca_int_csr="${dir_ca_int_csr}/intermediate.csr"
ca_int_crt="${dir_ca_int_certs}/intermediate.crt.pem"
ca_int_crt_srl="${dir_ca_int_db}/intermediate.crt.srl"
ca_int_ext="req_ca_intermediate_x509_ext"

dir_lh="${dir}/localhost"
dir_lh_private="${dir_lh}/private"
dir_lh_certs="${dir_lh}/certs"
dir_lh_csr="${dir_lh}/csr"
lh_cnf="${dir_lh}/localhost.cnf"
lh_csr="${dir_lh_csr}/localhost.csr"
lh_crt="${dir_lh_certs}/localhost.crt.pem"
lh_chain_crt="${dir_lh_certs}/localhost.chain.crt.pem"
lh_ext="intermediate_server_ext"

[[ ! -f "${ca_root_db}" ]] && touch "${ca_root_db}"

printf "\033[33mCreating root ca certificate request file (ca.csr).\033[0m\n"
openssl req -new -config "${ca_root_cnf}" -out "${ca_root_csr}"

printf "\033[33mSigning root ca certificate (ca.crt.pem).\033[0m\n"
openssl ca -batch -create_serial -selfsign -config "${ca_root_cnf}" -extensions "${ca_root_ext}" -in "${ca_root_csr}" -out "${ca_root_crt}"

[[ ! -f "${ca_int_db}" ]] && touch "${ca_int_db}"

printf "\033[33mCreating intermediate ca certificate request file (intermediate.csr).\033[0m\n"
openssl req -new -config "${ca_int_cnf}" -out "${ca_int_csr}"

printf "\033[33mSigning intermediate ca certificate (intermediate.crt.pem).\033[0m\n"
openssl ca -batch -rand_serial -config "${ca_root_cnf}" -extensions "${ca_int_ext}" -in "${ca_int_csr}" -out "${ca_int_crt}"

printf "\033[33mCreating intermediate ca chain certificate file (intermediate.chain.crt.pem).\033[0m\n"
cp "${ca_int_crt}" "${lh_chain_crt}"
cat "${ca_root_crt}" >> "${lh_chain_crt}"

printf "\033[33mCreating server certificate signing request file (localhost.csr).\033[0m\n"
openssl req -new -config "${lh_cnf}" -out "${lh_csr}"

printf "\033[33mSigning server certificate (localhost.crt.pem).\033[0m\n"
openssl ca -batch -rand_serial -config "${ca_int_cnf}" -extensions "${lh_ext}" -in "${lh_csr}" -out "${lh_crt}"
