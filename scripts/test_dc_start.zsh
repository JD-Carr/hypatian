#!/usr/bin/env zsh
container=test_flask

printf "\033[33m[PROCESS ] Starting <container: ${container}>\033[0m\n"

docker exec --interactive --tty "${container}" /bin/bash
