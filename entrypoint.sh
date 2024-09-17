#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py makemigrations api --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
python manage.py createsuperuser --noinput

if [ $DEBUG = "True"]
then
    exec python manage.py runserver 0.0.0.0:8000
else
    exec "$@"
fi