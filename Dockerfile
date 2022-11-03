FROM python:3.10.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /music_service

WORKDIR /music_service

ADD . /music_service

RUN pip install -r requirements.txt

EXPOSE 8000:8000