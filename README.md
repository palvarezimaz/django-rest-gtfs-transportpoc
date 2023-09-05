# Transport Timetable App - Proof of concept

### Summary
This Django app uses Django REST Framework to provide API responses on Transit Data.

The data source are a set of GTFS files.

### Features
- Display of arrival times of trains for a given stop
- List of all trips that run on a given day
- Access through the data as an API or as a form

## How to use the app

The app allows for GET requests that return (1) the arrival times of trains for a given stop
```
GET /arrivals/{stop_id}
```
and (2) all trips that run on a given day
```
GET /day-trips/{monday|tuesday|...}
```

There is also the option to use a browser using the url path or, for a user-friendlier experience, forms

### Installation guide

## GTFS to PSQL
After some considerations, I took the design choice of import the files into a PostgreSQL DB to take advantage of it's integration with Django.

And after some more considerations and asserting the data integrity through a [GTFS validator](https://github.com/MobilityData/gtfs-validator), I wrote a script to insert the data from the .txt files into the DB. To prevent some of the inherent complexities of the GTFS files, I'm treating every field as TEXT.

Notes to the GTFS to PSQL script:
To run:
```
$ cd utils
$ python gtfs_to_psql.py
```

The script will parse through the files on the harcoded set directory (../sources/schedule/).
- **It will NOT create** a database (this has to be done manually)
- For the time being, it **does not check** if the table exists. Running the script over an existing db will most likely throw a DuplicateTable error. If the data needs to be refreshed/updated, drop the database and run the script again.

Remember to connect Django to the PostgreSQL DB through settings.py

## PSQL to Django

Once the data is migrated into the DB, the models have to created for Django.

For this, run:
```
$ python manage.py inspectdb > models.py
```

Django will inspect the DB declared in settings and create models. This file has to be moved inside the app (in this case, `/transport`).

**Note:** The models need to be adjusted to the specifications of the GTFS files, setting primary keys and foreign keys to allow table joins and other db operations. Follow the specs from the [official documentation](https://developers.google.com/transit/gtfs/reference)

Once the models.py file is in the app and the models have been updated as per specs, perform the migrations
```
$ python manage.py makemigrations
$ python manage.py migrate
```
## TODO List
- Write unit tests. There seems to be a Django-inherent problem when generating unit tests as the build fails



