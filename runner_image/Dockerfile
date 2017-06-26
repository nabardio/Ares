FROM python:3
MAINTAINER Mehdy Khoshnoody "mehdy.khoshnoody@gmail.com"

RUN mkdir /game
WORKDIR /game

ADD runner.py .

RUN pip install battlefield

ENTRYPOINT ["python", "runner.py"]
