![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# django-foreignform

### Quickstart

1. Install the app.

  ```
  $ pip install django-foreignform
  ```

2. Add the app to your Django project and configure settings.

  ```python
  INSTALLED_APPS = [
      # ...
      'rest_framework',
      'foreignform',
  ]

  #########################
  # foreignform settings

  FOREIGNFORM_SECRET_KEY = ''
  FOREIGNFORM_AWS_ACCESS_KEY_ID = ''
  FOREIGNFORM_AWS_SECRET_ACCESS_KEY = ''
  FOREIGNFORM_AWS_REGION = ''
  FOREIGNFORM_AWS_S3_BUCKET = ''
  FOREIGNFORM_CLOUDFRONT_ALTERNATE_DOMAIN = ''
  FOREIGNFORM_S3_UPLOAD_ROOT = ''
  ```

### Developing

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server, which will automatically proxy Django's development server.

  ```
  $ cd foreignform/staticapp
  $ gulp
  ```

Want to not worry about it? Use the shortcut make command.

  ```
  $ make dev
  ```

##### Setting up a PostgreSQL database

1. Run the make command to setup a fresh database.

  ```
  $ make database
  ```

2. Add a connection URL to the `.env` file.

  ```
  DATABASE_URL="postgres://localhost:5432/foreignform"
  ```

3. Run migrations from the example app.

  ```
  $ cd example
  $ pipenv run python manage.py migrate
  ```
