#!/bin/bash

# python -m venv .venv
# source .venv/bin/activate
# pip install --upgrade pip
# echo "django" > requirements.txt
# pip install -r requirements.txt
# pip freeze > requirements.txt
# django-admin startproject $1 .
# python manage.py startapp core

python create-project-aux/set.py $1



# python manage.py runserver