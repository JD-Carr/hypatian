#!/usr/bin/env zsh

image=test_hypatian
tag=latest
container=test_flask
service=test

printf "\033[33m[PROCESS] Starting <container: ${container}>\033[0m\n"

docker exec --interactive --tty "${container}" /bin/bash
