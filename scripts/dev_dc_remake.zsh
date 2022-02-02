#!/usr/bin/env zsh
container=dev_flask
service=dev
dc_file=docker-compose.dev.yml

printf "[REPORT ] Checking for running <service: ${service}>\n"

# Stop service containers gracefully, if service is in the running state.
if docker-compose -f ${dc_file} ps --services --filter status=running | grep -q "${service}"; then
	printf "[REPORT ] Found running <service: ${service}>\n"

	printf "[PROCESS] Stopping & removing <service: ${service}>\n"
	docker-compose -f ${dc_file} stop "${service}"

	docker-compose -f ${dc_file} down "${service}" --rmi all
	printf "[REPORT ] <service: ${service}> stopped\n"
fi

printf "[PROCESS] Building <service: ${service}> ...\n"
docker-compose -f ${dc_file} build ${service}
printf "[REPORT ] <service: ${service}> built\n"

printf "[PROCESS] Starting <service: ${service}>\n"
docker-compose -f ${dc_file} up --detach ${service}
printf "[REPORT ] <service: ${service}> started\n"
