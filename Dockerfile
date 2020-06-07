FROM python:3.7

MAINTAINER <berserg2010@gmail.com>

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/hardware_inventory

COPY backend/requirements.txt backend/requirements.txt

RUN pip install -r backend/requirements.txt

COPY backend/. backend/

EXPOSE 8000

