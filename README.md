# Hello App

## How to build

### 1.Clone this repo.
### 2.Create .env file and change all the data inside <> to actual values

    cp .env.dev secrets.env

### 3.Build docker image:

    docker-compose build

### 4.launch server for the first time:

    docker-compose up

### 5.Move to http://0.0.0.0:8000 in your browser. You should be able to see the main page.

## How to upload on Heroku

### 1.Install Heroku
### 2.Login:

    heroku login

### 3.Make the port read from Heroku. Change Dockerfile last line from

    CMD gunicorn wsgi:app --bind 0.0.0.0:8000 --workers 3

    to

    CMD gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 3

### 4.After login create an application:

    heroku create <your_app_name>

### 5.Login to the Heroku container registry:

    heroku container:login

### 6.Push container to Heroku:

    heroku container:push web --app <your_app_name>

### 7.After app's container builds, release it to Heroku:

    heroku container:release web --app <your_app_name>

### 8.Move to http:/<your_app_name>.herokuapp.com in your browser.