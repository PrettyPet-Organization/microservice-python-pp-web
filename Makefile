freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt
venv:
	./venv/bin/activate

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/
	pip install -r requirements.txt

run: venv/bin/activate
	./venv/bin/python3 manage.py