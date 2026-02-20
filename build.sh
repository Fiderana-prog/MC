#!/usr/bin/env bash

pip install -r requirements.txt
python n8n/manage.py collectstatic --noinput
python n8n/manage.py migrate
gunicorn n8n.wsgi:application --bind