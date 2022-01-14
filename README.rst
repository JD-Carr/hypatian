========
Hypatian
========

This is an early fork of an API server project I built.
This is a tinkering project, and no stability is ensured and updates may dramatically alter the source code.
This project is focused on learning more about Docker, Apache, Debian, and various Flask plugins.
This journey is to find new and better (for my needs) to configure and manage projects with many parts and systems.

From dyvers hands.

Important Commands
==================

python -m build --outdir wheelhouse
   * Build a wheel file for the project.
   * Place wheel file in the subdirectory: wheelhouse

docker-compose up --build --detach
   * ``up`` Creates the containers.
   * ``--build`` Force (re)building the Dockerfile images.
   * ``--detach`` Starts the containers and runs them in the background.

docker exec --interactive --tty {service} /bin/bash
   * Connect to the Docker container

Scripts
=======
create_certs.sh
   * Creates self-signed SLL certificates for development/testing environments.

prepare_py_wheel.zsh
   * Builds the python wheel file.
