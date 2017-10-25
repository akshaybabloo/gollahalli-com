# Gollahalli Micro CMS

| Version | Codecov | CI | Requirements |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Master | [![codecov](https://codecov.io/gh/akshaybabloo/gollahalli-com/branch/master/graph/badge.svg)](https://codecov.io/gh/akshaybabloo/gollahalli-com) | [![Build Status](https://travis-ci.org/akshaybabloo/gollahalli-com.svg?branch=master)](https://travis-ci.org/akshaybabloo/gollahalli-com) | [![Requirements Status](https://requires.io/github/akshaybabloo/gollahalli-com/requirements.svg?branch=master)](https://requires.io/github/akshaybabloo/gollahalli-com/requirements/?branch=master) |
| V2 | N/A | N/A | [![Requirements Status](https://requires.io/github/akshaybabloo/gollahalli-com/requirements.svg?branch=Django-Python-3)](https://requires.io/github/akshaybabloo/gollahalli-com/requirements/?branch=Django-Python-3) |


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/akshaybabloo/gollahalli-com)

> Warning: Master branch is not production ready (yet) :warning:. Use [Django-Python-3](https://github.com/akshaybabloo/gollahalli-com/tree/Django-Python-3), to create your website based on JSON. If you like PHP then see [PHP5](https://github.com/akshaybabloo/gollahalli-com/tree/PHP5) branch.

**TOC**

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Introduction](#introduction)
- [Running Locally (Development)](#running-locally-development)
- [Requirements](#requirements)
- [GraphQL as an API](#graphql-as-an-api)
- [Template Usage](#template-usage)
	- [Regular Pages](#regular-pages)
	- [Google AMP](#google-amp)
- [License](#license)

<!-- /TOC -->

## Introduction

I have been sick of complicated CMS, so I set out to develop a micro-CMS. A very simple one-page website creator that supports Django Templates and GraphQL API calls.

For extra security, I have included Authy's two-factor authentication with Django's built-in user authentication system.

**Portal**

![Portal](https://raw.githubusercontent.com/akshaybabloo/gollahalli-com/master/screenshot/portal.JPG)

## Running Locally (Development)

If you want to test how it works, you might want to install `PostgreSQL` from [bigsql.org](http://bigsql.org/), because I have used JSON field inside the models, which will only work on PostgreSQL.

Then search for `plsql` and type in the following SQL query to create the `user` and the `table`

```sql
CREATE USER akshay WITH PASSWORD 'akshay12';
CREATE DATABASE gollahalli_com_django_test;
GRANT ALL PRIVILEGES ON DATABASE "gollahalli_com_django_test" to akshay;
```

Once you have created the user and database, install these dependencies (Python 3.5 or 3.6)

```
See requirements.txt
```

Now, clone the repo and open your `cmd` or `terminal`. Change to the cloned directory and type in the following commands.

```cmd
python managey.py makemigration
python manage.py collectstatic
```

Also, create a superuser by typing in

```cmd
python manage.py createsuperuser
```

If there are no errors, then type in

```cmd
python manage.py runserver
```

## Requirements

This library heavily depends on the following services:

1. Heroku (web deployment)
2. Amazon AWS S3 (storage) - That's because Heroku doesnt provide storage system.
3. Authy (Two-factor authentication)
4. Cloudinary (Optional, for images)
5. PostgreSQL (database)

## GraphQL as an API

Content coming soon.

## Template Usage

Content coming soon.

### Regular Pages

Content coming soon.

### Google AMP

Content coming soon.

## License

Provided under [MIT License](https://github.com/akshaybabloo/gollahalli-com/blob/master/LICENSE.md).
