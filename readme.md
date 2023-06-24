create django runserver setup

create a python environment
``` python3 -m venv env ```
activate the environment
``` source env/bin/activate ```

install requirements
``` pip install -r requirements.txt ```

run the server
``` python manage.py runserver ```

open the browser and go to http://127.0.0.1:8000/

access the admin page
username: root
password: root

if you want to create a superuser
``` python manage.py createsuperuser ```

if you logined as a admin you can see the admin option on top right corner of the page navigation bar

if you want to save your  history you need to login as a user.
