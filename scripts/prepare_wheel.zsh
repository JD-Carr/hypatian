#!/usr/bin/env zsh
# vim: ft=sh
set -euxo pipefail

if [[ -f ./wheelhouse/*.whl ]] || [[ -f ./wheelhouse/*.gz ]]; then
	printf "\033[33m[PROCESS] Removing existing files...\033[0m\n"
	# Clear contents of wheelhouse folder
	rm --recursive --force ./wheelhouse/*
fi

printf "\033[33m[PROCESS] Building hypatian wheel file...\033[0m\n"

# Ignore non-error output
python -m build --outdir ./wheelhouse &> /dev/null

printf "\033[33m[REPORT ] Wheel file successfully built.\033[0m\n"
