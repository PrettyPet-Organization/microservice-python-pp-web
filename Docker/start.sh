#!/bin/sh

Docker/migrate.sh

echo "Starting Django server..."
python src/manage.py runserver 0.0.0.0:8000