#!/bin/sh

echo "Applying migrations..."

python src/manage.py migrate

echo "Migrations applied successfully."