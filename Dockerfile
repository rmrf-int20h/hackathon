FROM python:3.6

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

RUN pip install gunicorn django psycopg2-binary

COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

CMD ["gunicorn", "--chdir", "hackapp", "--bind", ":8000", "hackapp.wsgi:application"]
