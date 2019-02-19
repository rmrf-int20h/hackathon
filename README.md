Docker image to develop app
==============

How it works:
--------------
**Connections:**

**WORLD** <--*port 8000*--> docker [ **NginX** <--*internal bridge*--> **Docker+Gunicorn** <--*internal bridge*--> **Postgresql client** <--*db interface*--> **database1** ]

How to use:
--------------
**Name:** *hackapp*

   $ docker-compose run djangoapp hackapp/manage.py collectstatic --no-input
   
   $ docker-compose up
