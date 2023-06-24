# Django Runserver Setup

This guide will walk you through the steps to set up and run a Django development server using the `runserver` command. The instructions assume you have Python and Django installed on your system.

## Prerequisites

Before starting, make sure you have the following prerequisites:

- Python 3 installed on your machine
- `venv` module installed (usually comes with Python 3)
- Django framework installed

## Setup Instructions

1. Create a Python virtual environment:

```shell
python3 -m venv env
```

2. Activate the virtual environment:

```shell
source env/bin/activate
```

3. Install project requirements:

```shell
pip install -r requirements.txt
```

4. Run the Django development server:

```shell
python manage.py runserver
```

5. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access your Django application.

## Admin Page Access

To access the Django admin page, follow these steps:

1. Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Use the following credentials to log in:
   - Username: root
   - Password: root

## Creating a Superuser

To create a superuser account, which has additional privileges in the Django admin interface, execute the following command:

```shell
python manage.py createsuperuser
```

Follow the prompts to enter a username, email (optional), and password for the superuser account.

## User Login for History Saving

If you want to save your history, you need to log in as a user. You can create a user account through the Django registration feature or by using custom logic in your application.

## Conclusion

By following these steps, you should now have a Django development server up and running. You can access your application through the specified local address and explore the admin interface using the provided credentials. Remember to log in as a user if you wish to save your history. Happy coding!
