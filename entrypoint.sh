#!/usr/bin/env sh

python manage.py migrate

gunicorn config.wsgi --bind 0.0.0.0:8000 --reload -w 4