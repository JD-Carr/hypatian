#!/usr/bin/env zsh

# TODO: Look into scripting creation of the SSL configuration files.

# Declare root project direectory.
dir="/home/projects/hypatian/ssl"

# Declare root Certificate Authority directory.
dir_ca_root="${dir}/ca/root"
dir_ca_root_db="${dir_ca_root}/db"
dir_ca_root_certs="${dir_ca_root}/certs"
dir_ca_root_csr="${dir_ca_root}/csr"
dir_ca_root_newcerts="${dir_ca_root}/newcerts"
dir_ca_root_private="${dir_ca_root}/private"

# Declare intermediate Certificate Authority directory.
dir_ca_int="${dir}/ca/intermediate"
dir_ca_int_db="${dir_ca_int}/db"
dir_ca_int_certs="${dir_ca_int}/certs"
dir_ca_int_csr="${dir_ca_int}/csr"
dir_ca_int_newcerts="${dir_ca_int}/newcerts"
dir_ca_int_private="${dir_ca_int}/private"

# Declare server / localhost Certificate Authority directory.
dir_lh="${dir}/localhost"
dir_lh_db="${dir_lh}/db"
dir_lh_certs="${dir_lh}/certs"
dir_lh_csr="${dir_lh}/csr"
dir_lh_newcerts="${dir_lh}/newcerts"
dir_lh_private="${dir_lh}/private"

[[ ! -d "${dir}" ]] && mkdir --parents "${dir}" || printf "\033[33mDirectory exists\033[0m\n"

#------------------------------------------------------------------------------#

[[ ! -d "${dir_ca_root}" ]] && printf "\033[33mMaking ${dir_ca_root}\n\033[0m" && mkdir --parents "${dir_ca_root}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_root_certs}" ]] && printf "\033[33mMaking ${dir_ca_root_certs}\n\033[0m" && mkdir --parents "${dir_ca_root_certs}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_root_csr}" ]] && printf "\033[33mMaking ${dir_ca_root_csr}\n\033[0m" && mkdir --parents "${dir_ca_root_csr}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_root_db}" ]] && printf "\033[33mMaking ${dir_ca_root_db}\n\033[0m" && mkdir --parents "${dir_ca_root_db}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_root_newcerts}" ]] && printf "\033[33mMaking ${dir_ca_root_newcerts}\n\033[0m" && mkdir --parents "${dir_ca_root_newcerts}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_root_private}" ]] && printf "\033[33mMaking ${dir_ca_root_private}\n\033[0m" && mkdir --parents "${dir_ca_root_private}" || printf "\033[33mDirectory exists\033[0m\n"

#------------------------------------------------------------------------------#

[[ ! -d "${dir_ca_int}" ]] && printf "\033[33mMaking ${dir_ca_int}\n\033[0m" && mkdir --parents "${dir_ca_int}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_int_certs}" ]] && printf "\033[33mMaking ${dir_ca_int_certs}\n\033[0m" && mkdir --parents "${dir_ca_int_certs}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_int_csr}" ]] && printf "\033[33mMaking ${dir_ca_int_csr}\n\033[0m" && mkdir --parents "${dir_ca_int_csr}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_int_db}" ]] && printf "\033[33mMaking ${dir_ca_int_db}\n\033[0m" && mkdir --parents "${dir_ca_int_db}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_int_newcerts}" ]] && printf "\033[33mMaking ${dir_ca_int_newcerts}\n\033[0m" && mkdir --parents "${dir_ca_int_newcerts}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_ca_int_private}" ]] && printf "\033[33mMaking ${dir_ca_int_private}\n\033[0m" && mkdir --parents "${dir_ca_int_private}" || printf "\033[33mDirectory exists\033[0m\n"

#------------------------------------------------------------------------------#

[[ ! -d "${dir_lh}" ]] && printf "\033[33mMaking ${dir_lh}\n\033[0m" && mkdir --parents "${dir_lh}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_lh_certs}" ]] && printf "\033[33mMaking ${dir_lh_certs}\n\033[0m" && mkdir --parents "${dir_lh_certs}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_lh_csr}" ]] && printf "\033[33mMaking ${dir_lh_csr}\n\033[0m" && mkdir --parents "${dir_lh_csr}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_lh_db}" ]] && printf "\033[33mMaking ${dir_lh_db}\n\033[0m" && mkdir --parents "${dir_lh_db}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_lh_newcerts}" ]] && printf "\033[33mMaking ${dir_lh_newcerts}\n\033[0m" && mkdir --parents "${dir_lh_newcerts}" || printf "\033[33mDirectory exists\033[0m\n"

[[ ! -d "${dir_lh_private}" ]] && printf "\033[33mMaking ${dir_lh_private}\n\033[0m" && mkdir --parents "${dir_lh_private}" || printf "\033[33mDirectory exists\033[0m\n"
