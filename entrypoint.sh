#!/usr/bin/env bash

./manage.py migrate
./manage.py collectstatic --noinput

gunicorn --workers 4 --worker-class gevent --reuse-port --chdir /app --bind 0.0.0.0:8000 ares.wsgi:application
