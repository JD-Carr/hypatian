#!/usr/bin/env zsh

image=dev_flask
tag=latest
container=dev_flask
service=dev
#dir_logs=./volumes/dev_logs
dc_file=docker-compose.dev.yml

#[[ ! -d ${dir_logs} ]] && mkdir --parents ${dir_logs}

printf "[REPORT ] Checking for running <service: ${service}>\n"

# Stop service containers gracefully, if service is in the running state.
if docker-compose -f ${dc_file} ps --services --filter status=running | grep -q "${service}"; then
	# Report if service was found.
	printf "[REPORT ] Found running <service: ${service}>\n"

	# Stop running service.
	printf "[PROCESS] Stopping & removing <service: ${service}>\n"

	docker-compose -f ${dc_file} stop "${service}"

	docker-compose -f ${dc_file} down "${service}"
	printf "[REPORT ] <service: ${service}> stopped\n"
fi

# Build the image.
printf "[PROCESS] Building <service: ${service}> ...\n"
docker-compose -f ${dc_file} build ${service}
printf "[REPORT ] <service: ${service}> built\n"

# Run the container in a background process.
printf "[PROCESS] Starting <service: ${service}>\n"
docker-compose -f ${dc_file} up --detach ${service}
printf "[REPORT ] <service: ${service}> started\n"
