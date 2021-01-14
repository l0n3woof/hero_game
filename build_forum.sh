#!/bin/sh

python backend/heros/manage.py makemigrations
python backend/heros/manage.py migrate

