FROM python:3.7

MAINTAINER <berserg2010@gmail.com>

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/hardware_inventory

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000
