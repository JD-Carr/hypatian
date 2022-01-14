#!/usr/bin/env bash

# Create Root Certificate Authority (CA).
# Create Intermediate (Signing) Certificate Authority (CA).
# Create server certificate.

dir="/srv/www/vhosts/hypatian/ssl"

dir_ca_root="${dir}/ca/root"
dir_ca_root_db="${dir_ca_root}/db"
dir_ca_root_private="${dir_ca_root}/private"
dir_ca_root_certs="${dir_ca_root}/certs"
dir_ca_root_csr="${dir_ca_root}/csr"
ca_root_db="${dir_ca_root_db}/ca.db.txt"
ca_root_cnf="${dir_ca_root}/ca.cnf"
ca_root_key="${dir_ca_root_private}/ca.key.pem"
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
ca_int_key="${dir_ca_int_private}/intermediate.key.pem"
ca_int_csr="${dir_ca_int_csr}/intermediate.csr"
ca_int_crt="${dir_ca_int_certs}/intermediate.crt.pem"

ca_int_crt_srl="${dir_ca_int_db}/intermediate.crt.srl"
ca_int_ext="req_ca_intermediate_x509_ext"

dir_lh="${dir}/localhost"
dir_lh_private="${dir_lh}/private"
dir_lh_certs="${dir_lh}/certs"
dir_lh_csr="${dir_lh}/csr"
lh_cnf="${dir_lh}/localhost.cnf"
lh_key="${dir_lh_private}/localhost.key.pem"
lh_csr="${dir_lh_csr}/localhost.csr"
lh_crt="${dir_lh_certs}/localhost.crt.pem"
lh_chain_crt="${dir_lh_certs}/localhost.chain.crt.pem"
lh_ext="intermediate_server_ext"

if [[ ! -f "${ca_root_db}" ]]; then
	printf "\033[33mCreating ca.db.txt\033[0m]\n"
	touch "${ca_root_db}"
else
	printf "\033[33mFound ca.db.txt\033[0m\n"
fi

printf "\033[33mCreating root ca certificate request file (ca.csr).\033[0m\n"
openssl req -new -config "${ca_root_cnf}" -out "${ca_root_csr}"

printf "\033[33mVerifying root ca key file (ca.key.pem).\033[0m\n"
openssl rsa -noout -text -in "${ca_root_key}"

printf "\033[33mVerifying root ca certificate request file (ca.csr).\033[0m\n"
openssl req -noout -text -in "${ca_root_csr}"

printf "\033[33mSigning root ca certificate (ca.crt.pem).\033[0m\n"
openssl ca -batch -create_serial -selfsign -config "${ca_root_cnf}" -extensions "${ca_root_ext}" -in "${ca_root_csr}" -out "${ca_root_crt}"

if [[ ! -f "${ca_int_db}" ]]; then
	printf "\033[33mCreating intermediate.db.txt\033[0m\n"
	touch "${ca_int_db}"
else
	printf "\033[33mFound intermediate.db.txt\033[0m\n"
fi

printf "\033[33mCreating intermediate ca certificate request file (intermediate.csr).\033[0m\n"
openssl req -new -config "${ca_int_cnf}" -out "${ca_int_csr}"

printf "\033[33mVerifying intermediate ca key file (intermediate.key.pem).\033[0m\n"
openssl rsa -noout -text -in "${ca_int_key}"

printf "\033[33mVerifying intermediate ca certificate request file (intermediate.csr).\033[0m\n"
openssl req -noout -text -in "${ca_int_csr}"

printf "\033[33mSigning intermediate ca certificate (intermediate.crt.pem).\033[0m\n"
openssl ca -batch -rand_serial -config "${ca_root_cnf}" -extensions "${ca_int_ext}" -in "${ca_int_csr}" -out "${ca_int_crt}"

printf "\033[33mVerifying intermediate ca certificate with root ca certificate.\033[0m\n"
openssl verify -CAfile "${ca_root_crt}" "${ca_int_crt}"

printf "\033[33mCreating intermediate ca chain certificate file (intermediate.chain.crt.pem).\033[0m\n"
cp "${ca_int_crt}" "${lh_chain_crt}"
cat "${ca_root_crt}" >> "${lh_chain_crt}"

printf "\033[33mCreating server certificate signing request file (localhost.csr).\033[0m\n"
openssl req -new -config "${lh_cnf}" -out "${lh_csr}"

printf "\033[33mVerifying server key file (localhost.key.pem).\033[0m\n"
openssl rsa -noout -text -in "${lh_key}"

printf "\033[33mVerifying server certificate request file (localhost.csr).\033[0m\n"
openssl req -noout -text -in "${lh_csr}"

printf "\033[33mSigning server certificate (localhost.crt.pem).\033[0m\n"
openssl ca -batch -rand_serial -config "${ca_int_cnf}" -extensions "${lh_ext}" -in "${lh_csr}" -out "${lh_crt}"

printf "\033[33mVerifying localhost certificate with intermediate ca certificate.\033[0m\n"
openssl verify -partial_chain -CAfile "${ca_int_crt}" "${lh_crt}"

printf "\033[33mVerifying localhost certificate with root ca and intermediate ca chain certificate.\033[0m\n"
openssl verify -CAfile "${lh_chain_crt}" "${lh_crt}"

printf "\033[33mChecking root ca database file.\033[0m\n"
cat "${ca_root_db}"

printf "\033[33mChecking intermediate ca database file.\033[0m\n"
cat "${ca_int_db}"
