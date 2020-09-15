# REST API Demo project #

## Setup ##
1. Pull the git repo to your machine, cd to the directory.
2. create a virtualenv - `python -m venv .venv`
3. activate it - `. .venv/bin/activate`
4. install requirements - `pip install -r requirements.txt`
5. cd into django_demo folder (should see manage.py)
6. Run db migration - `python manage.py migrate`
7. create a user - `python manage.py createsuperuser` - use username/password for username and password.
8. Run the server - `python manage.py runserver`