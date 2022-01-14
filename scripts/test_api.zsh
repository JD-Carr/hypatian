#!/usr/bin/env zsh


curl --verbose --request GET http://127.0.0.1:5000/patients

curl --verbose --request GET http://127.0.0.1:5000/patients/1

curl --verbose --request DELETE http://127.0.0.1:5000/patients/1

curl --verbose --request PATCH http://127.0.0.1:5000/patients/1

curl --verbose --request POST http://127.0.0.1:5000/patients/1
