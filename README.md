Docker image to develop app
==============

How it works:
--------------
**Directory tree:**

  hack
  ├── config
  │   ├── db
  │   │   └── database1_env
  │   └── nginx
  │       └── conf.d
  │           └── local.conf
  ├── docker-compose.yml
  ├── Dockerfile
  ├── hackapp
  │   ├── hackapp
  │   │   ├── __init__.py
  │   │   ├── __pycache__
  │   │   │   ├── __init__.cpython-36.pyc
  │   │   │   ├── settings.cpython-36.pyc
  │   │   │   ├── urls.cpython-36.pyc
  │   │   │   └── wsgi.cpython-36.pyc
  │   │   ├── settings.py
  │   │   ├── urls.py
  │   │   └── wsgi.py
  │   └── manage.py
  └── README.md

**Connections:**

**WORLD** <--*port 8000*--> docker [ **NginX** <--*internal bridge*--> **Docker+Gunicorn** <--*internal bridge*--> **Postgresql client** <--*db interface*--> **database1** ]

How to use:
--------------
**Name:** *hackapp*

  $ docker-compose run djangoapp hackapp/manage.py collectstatic --no-input
  $ docker-compose up
