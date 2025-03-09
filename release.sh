#!/bin/bash
set -s
python manage.py migrate
python manage.py collectstatic --noinput