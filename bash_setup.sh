#!/bin/bash

cd /home/project/
python3.11 -m ensurepip
python3.11 -m pip install Django

cd /home/project/customer360
python3.11 manage.py makemigrations customer360
python3.11 manage.py migrate
python3.11 manage.py runserver