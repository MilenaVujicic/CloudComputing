FROM python:3.8.3-alpine

WORKDIR /usr/src

EXPOSE 8000
EXPOSE 5433

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
RUN apk update && apk add bash

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .


CMD cd WebApp && python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000 



