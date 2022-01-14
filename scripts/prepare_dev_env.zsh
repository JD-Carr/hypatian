#!/usr/bin/env zsh

[[ ! -d "${CWD}/.venv" ]] && python -m venv .venv

source ./.venv/bin/activate

python -m pip install -r requirements-dev.txt

python -m pip install -r requirements.txt
