For running the project, first you will need Python Interpreter (python.org). 


Then, you will require to install following two packages :-


Django - pip install django

Requests - pip install requests

Then, locate the manage.py file and run the following commands to dump database :-


python manage.py makemigrations

python manage.py migrate


To start development server :-


python manage.py runserver



Your application is visible at http://127.0.0.1:8000



If having (python:command not found) error use python3 in place of python. 
