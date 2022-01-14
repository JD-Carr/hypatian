#!/usr/bin/env zsh

set -o errexit

printf "\033[33m[PROCESS] Removing existing files...\033[0m\n"
# Clear contents of wheelhouse folder.
#rm --recursive --force ./wheelhouse/*

printf "\033[33m[PROCESS] Building hypatian wheel file...\033[0m\n"

python -m build --outdir ./wheelhouse

printf "\033[33m[REPORT ] Wheel file successfully built.\033[0m\n"
