#!/usr/bin/env zsh
# vim: ft=sh
container=dev_flask
service=dev

printf "\033[33m[PROCESS] Starting <container: ${container}>\033[0m\n"

docker exec --interactive --tty "${container}" /bin/bash
