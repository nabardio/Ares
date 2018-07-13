FROM python:3
MAINTAINER Mehdy Khoshnoody "mehdy.khoshnoody@gmail.com"

ENV PYTHONBUFFERED 1

RUN pip install gunicorn gevent

RUN mkdir /app
ADD . /app
WORKDIR /app

EXPOSE 8000

VOLUME ["/app/static", "/app/media"]

RUN pip install -r requirements.txt

RUN ./manage.py migrate --noinput

RUN ./manage.py collectstatic --noinput

ENTRYPOINT ["gunicorn",
    "--workers", "4",
    "--worker-class", "gevent",
    "--reuse-port",
    "--chdir", "/app",
    "--bind", "0.0.0.0:8000",
    "ares.wsgi:application"]