# Installing Bucketie
This project assumes you intend on using postgres as your database system for
running this app.

## Preparing the Database
First, you need to create a database which the app stores it's data on your. To 
create the db, use

    CREATE DATABASE bucketie;

After creating a db, you need to create a user which you will further give privileges to access
your database on behalf of the app. Create the user following the example below

    CREATE USER tim WITH PASSWORD 'password';

Before granting priviledges, try to make sure you set the reasonable defaults for the
user. Theses settings gorvern how the user accesses the database.

    ALTER ROLE tim SET client_encoding TO 'utf8';
    ALTER ROLE tim SET default_transaction_isolation TO 'read committed';
    ALTER ROLE tim SET timezone TO 'UTC';

You can set the default timezone to whatever the intended timezone is (I'm using a
relatively neutral one here).
You can no grant all privileges to the user on the created db like so.

    GRANT ALL PRIVILEGES ON DATABASE bucketie TO tim;
    ALTER USER tim CREATEDB;

## Setting up a virtual environment
I'm not going to preach about virtual environments here (we've all heard the sermon,
and probably know the consequence of breaking the 11th commandment).

For guidiance, visit [python.org](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) or [virtualenv site](virtualenv.pypa.io/en/stable/installation/) or just [google](https://www.google.com.ng/search?q=how+to+install+virtualenv&oq=how+to+install+virtualenv) it.

## Installing the Django app
This app uses environment variables to keep things secret or just for config purposes. 
So, store the following keys on the following environment variables

### Required

    export BK_DB_PASSWORD=password
    export BK_SECRET=j#u@dvwuienq3o34mpjmv*3+jj3__ujd5ale=-%7s^g^r3*8#l^z@vjs1b9r6m3@ei03l@9-

### Optional
The values given here are the default if the environment variables are not set.

    export BK_DB_NAME=bucketie
    export BK_DB_USER=tim
    export BK_DB_HOST=localhost
    export BK_DB_PORT=''

Migrate the database

    python manage.py makemigrations
    python manage.py migrate

Create a super user who will be an admin

    python manage.py createsuperuser

Run SERVER!

    python manage.py runserver localhost:8000


#Running The Tests
This app has been tested to some extent. To run the unittests, enter

    python manage.py test --settings=settings.test --pattern="*"