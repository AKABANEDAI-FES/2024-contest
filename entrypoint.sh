#!/bin/sh

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py makemigrations MediChat --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

if [ $DEBUG = "True"]
then
    exec python manage.py runserver 0.0.0.0:8000
else
    exec "$@"
fi