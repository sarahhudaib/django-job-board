# PostgreSQL

- To use PostgreSQL as the database for your Django project, you will need to install the `PostgreSQL` database server and the `psycopg2` package, which is a PostgreSQL adapter for Python.

```
pip install psycopg2
pip install psycopg2-binary
pip install postgres
pip install django-leaflet
pip install -r requirements.txt
```

after installing all the required libraries:
```
pip freeze > requirements.txt
```
- Next, you will need to update your Django settings file to use the PostgreSQL database. 

Open your Django settings file and find the `DATABASES` setting. It should look something like this:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

To use PostgreSQL as the database, change the `ENGINE` setting to '`django.db.backends.postgresql`' and specify the connection parameters for your PostgreSQL database:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": "localhost",
        "PORT":5432
    }
}
```
- Finally, run the following command to create the necessary tables in the PostgreSQL database:

```
python manage.py migrate
```
----------------------
## Deleting the `db.sqlite3` file?

If you are using PostgreSQL as the database for your Django project, you can leave the db.sqlite3 file in your project folder. It will not be used by Django when you are using PostgreSQL as the database.

However, if you want to completely remove the db.sqlite3 file, you can delete it from your project folder. It is not required for your Django project to run.

Keep in mind that deleting the db.sqlite3 file will also delete all the data stored in the SQLite database. Make sure to take a backup of the data if you need to keep it.

---------
## Backup of the data from the `db.sqlite3` file
- To take a backup of the data from the db.sqlite3 file, you can use the dumpdata management command provided by Django.

To create a backup of all the data in the db.sqlite3 file, run the following command:

```
python manage.py dumpdata > data.json
```
This will create a file called `data.json` in your project folder, which contains a `JSON` representation of all the data in your database.

- You can also specify the specific apps or models for which you want to create a backup. For example, to create a backup of the jobs app, run the following command:

```
python manage.py dumpdata jobs > data.json
```
- To restore the data from the `data.json` file, use the `loaddata` management command:

```
python manage.py loaddata data.json
```

This will load the data from the `data.json` file into the database.