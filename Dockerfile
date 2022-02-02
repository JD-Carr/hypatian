# syntax=docker/dockerfile:1
#------------------------------------------------------------------------------#
ARG OS_DIST=debian
ARG OS_TAG=bullseye
FROM $OS_DIST:$OS_TAG AS base

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update --quiet --quiet --yes
RUN apt-get install --quiet --quiet --yes apt-utils
RUN apt-get install --quiet --quiet --yes locales

RUN ln --force --no-dereference --symbolic /usr/share/zoneinfo/Etc/UTC /etc/localtime
RUN localedef --force --charmap=UTF-8 --inputfile=en_US en_US.UTF-8
RUN sed -i 's/^# *\(en_US.UTF-8 .*\)/\1/' /etc/locale.gen
RUN locale-gen --no-purge en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN echo locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8 | debconf-set-selections
RUN echo locales locales/default_environment_locale select en_US.UTF-8 | debconf-set-selections
RUN dpkg-reconfigure locales

RUN apt-get install --quiet --quiet --yes python3
RUN apt-get install --quiet --quiet --yes python3-dev
RUN apt-get install --quiet --quiet --yes python3-pip
RUN apt-get install --quiet --quiet --yes python3-venv
RUN apt-get install --quiet --quiet --yes sqlite3
RUN apt-get install --quiet --quiet --yes vim

RUN apt-get clean --quiet --quiet
RUN apt-get autoremove --quiet --quiet
RUN rm --recursive --force /var/lib/apt/lists/*

WORKDIR /var/www/hypatian
COPY ./hypatian ./hypatian
COPY ./ssl ./ssl
COPY ./.bashrc /root
COPY ./requirements.txt ./

ENV PIP_NO_CACHE_DIR=0
ENV VIRTUAL_ENV=/var/www/hypatian/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH=$VIRTUAL_ENV/bin:$PATH

RUN python3 -m pip install --upgrade pip wheel
RUN python3 -m pip install -r requirements.txt
RUN rm --force ./requirements.txt

COPY ./scripts/create_certs.sh ./
RUN chmod +x ./create_certs.sh
RUN ./create_certs.sh
RUN rm ./create_certs.sh

#------------------------------------------------------------------------------#
FROM base AS dev

WORKDIR /var/www/hypatian
COPY ./wsgi.py ./

#------------------------------------------------------------------------------#
FROM base AS apache

RUN apt-get update --quiet --quiet --yes
RUN apt-get --quiet --quiet --yes install apache2
RUN apt-get --quiet --quiet --yes install apache2-dev
RUN apt-get --quiet --quiet --yes install apache2-utils
RUN apt-get --quiet --quiet --yes install libapache2-mod-wsgi-py3
RUN apt-get --quiet --quiet --yes install lynx
#RUN apt-get --quiet --quiet --yes install ufw
RUN apt-get clean --quiet --quiet
RUN apt-get autoremove --quiet --quiet
RUN rm --recursive --force /var/lib/apt/lists/*

WORKDIR /var/www/hypatian
COPY ./hypatian.wsgi ./
COPY ./scripts/apache.sh ./

COPY ./requirements-test.txt ./requirements-test.txt
RUN python3 -m pip install -r requirements-test.txt
RUN rm --force ./requirements-test.txt

COPY ./wheelhouse/hypatian-1.0.0-py3-none-any.whl ./
RUN python -m pip install hypatian-1.0.0-py3-none-any.whl
RUN rm hypatian-1.0.0-py3-none-any.whl

RUN mkdir ./logs
RUN chown --recursive www-data:www-data ./

RUN a2dissite 000-default
RUN rm -rf /etc/apache2/sites-available/000-default.conf

RUN mkdir --parents /var/cache/ssl
RUN chown --recursive www-data:www-data /var/cache/ssl

COPY ./hypatian.conf /etc/apache2/sites-available
RUN chown --recursive www-data:www-data /etc/apache2/sites-available
RUN a2ensite hypatian
RUN a2enmod ssl

#------------------------------------------------------------------------------#
FROM apache AS test

WORKDIR /var/www/hypatian

#------------------------------------------------------------------------------#
FROM apache AS prod

WORKDIR /var/www/hypatian
