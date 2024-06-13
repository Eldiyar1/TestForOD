FROM python:3.10

WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements /usr/src/app/requirements

COPY . .

RUN pip install -r requirements/production.txt

RUN python manage.py makemigrations
