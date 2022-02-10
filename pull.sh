#!/bin/bash
set -e

ENV=immobiliare

source $WORKON_HOME/$ENV/bin/activate
git pull
cd django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
echo yes | python manage.py collectstatic
