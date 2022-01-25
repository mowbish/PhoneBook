# PhoneBook

[![python](https://img.icons8.com/color/48/000000/python.png/)](https://www.python.org/)
[![django](https://img.icons8.com/color/48/000000/django.png)](https://www.djangoproject.com/)
[![DRF](https://img.icons8.com/color/48/000000/api.png)](https://www.django-rest-framework.org/)
[![postgresql](https://img.icons8.com/color/48/000000/postgresql.png)](https://www.postgresql.org/)
[![celery](https://img.icons8.com/color/48/000000/celery.png)](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html)

# Requirements

* Python (3.6, 3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.0, 3.1, 3.2, 4.0)
* psycopg2 (2.9.3)
* celery (5.2.3)
* django-filter (21.1)
* djangorestframework (3.13.1)
* and other things...

I **highly recommend** and only officially support the latest patch release of
each Python and Django series.

## What this project wanted from me:

In this challenge we want you to develop a basic phonebook and a
simple reporting system that works in the background. The final
result is a collection of API endpoints which follow RESTful principles.

### Project detail

In the phonebook project users can register and login into the
system via phone number. They can manage their contacts in the
phonebook. Each contact may have a few data fields such as name
of the contact, phone numbers, email, etc. There are also groups of
contacts such as close friends or family. Users can also manage
groups and add or remove contacts in the groups. In addition,
sometimes there are more than one contact per name, phone or
email. Provide API endpoints to find such contact and merge them on
demand.
At the end of each day a report will be sent to each user email. The
report contains the contacts count of that user for yesterday and
today. There is absolutely no need to make a complicated email
template. A simple message would be enough.
Following python code style, necessary and suitable tests are
expected as well.

### Expectations

+ Develop the phonebook project with Django.
+ Use Celery and Celery-Beat to implement background jobs.
+ Use git as your source control. Please make regular commits with useful commit messages and descriptions.
+ Provide a readme file in which there are all assumptions and necessary details about the project and how to test and launch it.
+ implementing appropriate structure for the project.
+ Email us the final project as a compressed file.

## Installation
---

First of all open the terminal or CMD and enter:

```shell
git clone https://github.com/mowbish/PhoneBook.git
```

After that go into the project folder and  create a virtual env


| Windows | Linux |
| --- | --- |
| ``> cd PhoneBook\  `` | ``$ cd PhoneBook/`` |
| ``> python -m venv venv `` | ``$ virtualenv venv`` |
| ``> venv\scripts\activate`` | ``$ source venv/bin/activate`` |

after activating venv now install requirements

```shell
pip install -r requirements.txt
```

Now edit the `conf/settings.py` module in your project:

```python

...

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PhoneBook', # Create data base with PhoneBook name
        'USER': 'admin', # Change or choose your own user
        'PASSWORD': 'your password', # A password that is the same here and in the database
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

...

```

Now enter this command:

```bash
python manage.py makemigrations
```

Now migrate all with this command:

```bash
python manage.py migrate
```

At the end you can run project with:

```bash
python manage.py runserver
```

Enjoy it ;)

#### Project Structure
---

```shell
├── docker-compose.yml
├── project
│   ├── conf
│   │   ├── asgi.py
│   │   ├── celery.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── wsgi.py
│   ├── contacts
│   │   ├── admin.py
│   │   ├── api
│   │   │   ├── serializers.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── management
│   │   │   └── commands
│   │   │       └── email_report.py
│   │   ├── managers.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── permissions.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   └── urls.py
│   ├── manage.py
│   └── requirements.txt
└── README.md
```

### why I use this structure to project

maybe you asked from your self why I preferd to use
from this structure to Project

The answer is simple

for **maintain structure and scalability**

in `contacts` app we have `api` folder that which contains three `serializers.py`, `views.py` and `urls.py` files

The purpose of this work was to keep the project clean and to separate the API(DRF) ``views`` from the normal ``views``

Also concise `` URLs`` to the API

in this structure i have been created `core` app which contains one file that `urls.py` to handle all the main things about the ``API's``

with `urls.py` we can versioning the API's and

I could have created the core as a folder and added it to the project, but I did not do so to **maintain structure and scalability**

so in future versions you can also use it (core) for other tasks and works

like adding `serializers.py` or `views.py` or etc

### Also Rout's of project:

first of all go to the:

`http://127.0.0.1:8000/`

after that you can go to this rout's

+ api/v1/signup
+ api/v1/create/contact/
+ api/v1/contacts/
+ api/v1/contact/<str:phone_number>/
+ api/v1/create/group/
+ api/v1/groups/
+ api/v1/group/<str:name>/

## Good Luck And Enjoy It ;)
