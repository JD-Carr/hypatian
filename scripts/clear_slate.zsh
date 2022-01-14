#!/usr/bin/env zsh

printf "\033[33m[REPORT] Deleting dev database file\033[0m\n"
rm --recursive --force ./database/*

printf "\033[33m[REPORT] Deleting all dev log files\033[0m\n"
rm --recursive --force ./logs/*
