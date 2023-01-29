#!/bin/bash

[[ -f run.sh ]] && source ./run.sh

if [[ ! -f .first_run ]] ; then
  # add wait db
  poetry run flask db upgrade
  poetry run flask create-superuser
  poetry run flask create-tag
  touch .first_run
fi

while true; do
  poetry run flask db upgrade
  poetry run python ./wsgi.py
  sleep 1m
done