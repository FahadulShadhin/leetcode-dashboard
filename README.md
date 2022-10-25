# LeetCode Dashboard

![demo screenshot](img/screenshot.png)

## Project Structure

```
.
├── manage.py
├── problems_list               # main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── migrations/
│   ├── templates
│   │   └── problems_list/
│   ├── templatetags/
│   ├── utils
│   │   └── problems_list/      utilities for the app
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── src                         # project directory   
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── bootstrap/
│   ├── css/
│   └── js/
└── templates/
```

## Versions

```
Python 3.9.5
Django 4.1.2
```

## Setup

* Install dependencies:

```
$ pip install -r requirements.txt
```

* Run development server:

```
$ python3 manage.py runserver
```

* Make initial migrations:

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

* Create a superuser to gain admin access:

```
$ python3 manage.py createsuperuser
```
