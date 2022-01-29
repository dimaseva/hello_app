FROM python:3.7-slim-stretch

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD gunicorn wsgi:app --bind 0.0.0.0:8000 --workers 3
