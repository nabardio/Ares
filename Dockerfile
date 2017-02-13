FROM python:3
MAINTAINER Mehdy Khoshnoody "mehdy.Khoshnoody@gmail.com"

ENV DOCKERFILE_VERSION 0.1.0

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN mkdir /project
WORKDIR /project

VOLUME ["/project"]

EXPOSE 5000

CMD ["python", "manager.py", "run"]