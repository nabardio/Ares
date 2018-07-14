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

ENTRYPOINT ["./entrypoint.sh"]