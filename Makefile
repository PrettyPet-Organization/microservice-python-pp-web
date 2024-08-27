migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

